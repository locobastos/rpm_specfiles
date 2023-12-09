%define haproxy_user           haproxy
%define haproxy_group          %{haproxy_user}
%define haproxy_homedir        %{_localstatedir}/lib/haproxy
%define haproxy_confdir        %{_sysconfdir}/haproxy
%define haproxy_datadir        %{_datadir}/haproxy

%global _hardened_build        1
%global _enable_debug_package  0
%global debug_package          %{nil}

Name:                          haproxy
Version:                       1.8.31
Release:                       1%{?dist}

Summary:                       HAProxy is a TCP/HTTP reverse proxy for high availability environments

Vendor:                        HAProxy Technologies, LLC
License:                       GPLv2+
URL:                           http://www.haproxy.org/
Packager:                      Bastien MARTIN (https://github.com/locobastos/haproxy)

Source0:                       https://www.haproxy.org/download/1.8/src/haproxy-%{version}.tar.gz
Source1:                       https://www.haproxy.org/download/1.8/src/haproxy-%{version}.tar.gz.sha256

%if 0%{?rhel} == 6
Source2:                       %{name}.init
%endif
%if 0%{?rhel} >= 7
Source2:                       %{name}.service
%endif
Source3:                       %{name}.cfg
Source4:                       %{name}.logrotate
Source5:                       %{name}.sysconfig
Source6:                       halog.1
Source7:                       http://www.lua.org/ftp/lua-5.3.6.tar.gz

BuildRequires:                 gcc
BuildRequires:                 make
BuildRequires:                 openssl-devel
BuildRequires:                 pcre-devel
BuildRequires:                 readline-devel
BuildRequires:                 zlib-devel

%if 0%{?rhel} >= 7
BuildRequires:                 systemd-units
%endif

Requires:                      openssl
Requires:                      pcre
Requires:                      setup >= 2.8.14-14

Requires(pre):                 %{_sbindir}/groupadd
Requires(pre):                 %{_sbindir}/useradd

%if 0%{?rhel} == 6
Requires(post):                /sbin/chkconfig
Requires(preun):               /sbin/chkconfig
Requires(preun):               /sbin/service
Requires(postun):              /sbin/service
%else
Requires(pre):                 shadow-utils
Requires(post):                systemd
Requires(preun):               systemd
Requires(postun):              systemd
%endif


%description
HAProxy is a TCP/HTTP reverse proxy which is particularly suited for high
availability environments. Indeed, it can:
 - route HTTP requests depending on statically assigned cookies
 - spread load among several servers while assuring server persistence
   through the use of HTTP cookies
 - switch to backup servers in the event a main one fails
 - accept connections to special ports dedicated to service monitoring
 - stop accepting connections without breaking existing ones
 - add, modify, and delete HTTP headers in both directions
 - block requests matching particular patterns
 - persists clients to the correct application server depending on
   application cookies
 - report detailed status as HTML pages to authenticated users from a URI
   intercepted from the application

%prep
cd %{_sourcedir}
sha256sum -c %{SOURCE1}
%setup -q -b 0
%setup -q -b 7
# Remove examples/check as we can't install it dependancies perl(IO::Socket::PortState)
%{__rm} --recursive --force examples/check*

%build
regparm_opts=
%ifarch %ix86 x86_64
regparm_opts="USE_REGPARM=1"
%endif

# Build LUA
pushd ../lua-5.3.6/src
sed -i '/^CFLAGS/ s/$/ -fPIC/' Makefile
%{__make} linux
popd

# Build HAPROXY
%{__make} %{?_smp_mflags} CPU="generic" TARGET="linux2628" ARCH="x86_64" USE_OPENSSL=1 USE_PCRE=1 USE_ZLIB=1 USE_LUA=1 USE_GETADDRINFO=1 ${regparm_opts} ADDINC="%{optflags}" EXTRA_OBJS="" LUA_INC=../lua-5.3.6/src LUA_LIB=../lua-5.3.6/src

pushd contrib/halog
%{__make} halog OPTIMIZE="%{optflags}"
popd

pushd contrib/iprange
%{__make} iprange OPTIMIZE="%{optflags}"
popd

%install
%{__make} install-bin DESTDIR=%{buildroot} PREFIX=%{_prefix} TARGET="linux2628"
%{__make} install-man DESTDIR=%{buildroot} PREFIX=%{_prefix}

%if 0%{?rhel} == 6
%{__install} --preserve-timestamps -D --mode=0755 %{SOURCE2} %{buildroot}%{_initrddir}/%{name}
%else
%{__install} --preserve-timestamps -D --mode=0644 %{SOURCE2} %{buildroot}%{_unitdir}/%{name}.service
%endif

%{__install} --preserve-timestamps -D --mode=0644 %{SOURCE3} %{buildroot}%{haproxy_confdir}/%{name}.cfg
%{__install} --preserve-timestamps -D --mode=0644 %{SOURCE4} %{buildroot}%{_sysconfdir}/logrotate.d/%{name}
%{__install} --preserve-timestamps -D --mode=0644 %{SOURCE5} %{buildroot}%{_sysconfdir}/sysconfig/%{name}
%{__install} --preserve-timestamps -D --mode=0644 %{SOURCE6} %{buildroot}%{_mandir}/man1/halog.1
%{__install} --directory --mode=0755 %{buildroot}%{haproxy_homedir}
%{__install} --directory --mode=0755 %{buildroot}%{haproxy_datadir}
%{__install} --directory --mode=0755 %{buildroot}%{_bindir}
%{__install} --preserve-timestamps --mode=0755 ./contrib/halog/halog %{buildroot}%{_bindir}/halog
%{__install} --preserve-timestamps --mode=0755 ./contrib/iprange/iprange %{buildroot}%{_bindir}/iprange
%{__install} --preserve-timestamps --mode=0644 ./examples/errorfiles/* %{buildroot}%{haproxy_datadir}

%{__rm} --force %{buildroot}%{_sbindir}/haproxy-systemd-wrapper

for httpfile in $(find ./examples/errorfiles/ -type f)
do
  %{__install} --preserve-timestamps --mode=0644 ${httpfile} %{buildroot}%{haproxy_datadir}
done

for textfile in $(find ./ -type f -name '*.txt' -o -name README)
do
  %{__mv} ${textfile} ${textfile}.old
  iconv --from-code ISO8859-1 --to-code UTF-8 --output ${textfile} ${textfile}.old
  %{__rm} --force ${textfile}.old
done

%clean
%{__rm} --recursive --force %{_builddir} %{_buildrootdir}

%pre
%{_bindir}/getent group %{haproxy_group} >/dev/null || %{_sbindir}/groupadd --system %{haproxy_group}
%{_bindir}/getent passwd %{haproxy_user} >/dev/null || %{_sbindir}/useradd --gid %{haproxy_group} --home-dir %{haproxy_homedir} --shell /sbin/nologin --system %{haproxy_user}

%post
%if 0%{?rhel} == 6
/sbin/chkconfig --add haproxy
%elif 0%{?rhel} >= 7
%{_bindir}/systemctl enable haproxy
%endif

echo ""
echo ""
echo -e "\e[1;31m ==============================================================================\e[0m"
echo -e "\e[1;31m  WARNING: This HAProxy RPM is not an official one.\e[0m"
echo ""
echo -e "\e[1;31m  To report bug fully related to HAProxy, please use their GitHub page:\e[0m"
echo -e "\e[1;31m        https://github.com/haproxy/haproxy/issues\e[0m"
echo ""
echo -e "\e[1;31m  To report bug related to this RPM itself or the files inside "SOURCES" folder,\e[0m"
echo -e "\e[1;31m  please use my GitHub page: https://github.com/locobastos/haproxy/issues\e[0m"
echo -e "\e[1;31m ==============================================================================\e[0m"
echo ""
echo ""

%preun
if [ "$1" -eq 0 ]
then
  if [ -e /sbin/service ]; then
    /sbin/service haproxy stop >/dev/null 2>&1
    /sbin/chkconfig --del haproxy
  elif [ -e /usr/bin/systemctl ]; then
    /usr/bin/systemctl disable haproxy
  fi
fi

%postun
if [ "$1" -ge 1 ]
then
  if [ -e /usr/bin/systemctl ]; then
    /usr/bin/systemctl daemon-reload
  fi
fi

%files
%defattr(-,root,root,-)
%doc doc/* examples/*
%doc CHANGELOG LICENSE README
%dir %{haproxy_confdir}
%dir %{haproxy_datadir}
%{haproxy_datadir}/*
%config(noreplace) %{haproxy_confdir}/%{name}.cfg
%config(noreplace) %{_sysconfdir}/logrotate.d/%{name}
%config(noreplace) %{_sysconfdir}/sysconfig/%{name}
%if 0%{?rhel} == 6
%{_initrddir}/%{name}
%endif
%if 0%{?rhel} >= 7
%{_unitdir}/%{name}.service
%endif
%{_sbindir}/%{name}
%{_bindir}/halog
%{_bindir}/iprange
%{_mandir}/man1/*
%attr(-,%{haproxy_user},%{haproxy_group}) %dir %{haproxy_homedir}
