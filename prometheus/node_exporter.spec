%if 0%{?rhel} >= 7
%undefine           _disable_source_fetch
%endif

Name:               node_exporter
Version:            1.7.0
Release:            1%{?dist}
Summary:            Prometheus exporter for machine metrics.

License:            Apache-2.0
URL:                https://prometheus.io/
Source0:            https://github.com/prometheus/node_exporter/releases/download/v%{version}/node_exporter-%{version}.linux-amd64.tar.gz
Source1:            node_exporter.service
Source2:            node_exporter

BuildArch:          x86_64

%if 0%{?rhel} == 6
Requires:           daemonize
%endif

%description
Prometheus exporter for hardware and OS metrics exposed by *NIX kernels, written in Go with pluggable metric collectors.

%prep
%setup -n node_exporter-%{version}.linux-amd64

%install
%{__install} -D --mode=0644 --directory %{buildroot}/usr/bin
%{__install} -D --mode=0644 --directory %{buildroot}/var/run/node_exporter/
%{__install} -D --preserve-timestamps --mode=0644 %{_builddir}/node_exporter-%{version}.linux-amd64/node_exporter %{buildroot}/usr/bin/

%if 0%{?rhel} >= 7
%{__install} -D --mode=0644 --directory %{buildroot}/usr/lib/systemd/system/
%{__install} -D --preserve-timestamps --mode=0644 %{SOURCE1} %{buildroot}/usr/lib/systemd/system/
%else
%{__install} -D --mode=0644 --directory %{buildroot}/etc/rc.d/init.d/
%{__install} -D --preserve-timestamps --mode=0644 %{SOURCE2} %{buildroot}/etc/rc.d/init.d/
%endif

%clean
%{__rm} --recursive --force %{buildroot} %{_builddir}

%pretrans
if ! id node_exporter >/dev/null 2>&1
then
    adduser --no-create-home --system --shell /sbin/nologin node_exporter
fi

%post
if systemctl >/dev/null 2>&1
then
    systemctl daemon-reload
fi

%postun
if systemctl >/dev/null 2>&1
then
    systemctl daemon-reload
fi

%files
%defattr(0755,root,root,0755)
/usr/bin/node_exporter
/var/run/node_exporter/

%if 0%{?rhel} >= 7
%license LICENSE
%attr(0644,root,root) /usr/lib/systemd/system/node_exporter.service
%else
/etc/rc.d/init.d/node_exporter
%endif
