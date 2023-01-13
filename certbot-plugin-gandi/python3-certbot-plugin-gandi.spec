Name:               python3-certbot-plugin-gandi
Version:            1.3.2
Release:            1%{?dist}
Summary:            Certbot plugin for authentication using Gandi LiveDNS

License:            MIT
URL:                https://github.com/obynio/certbot-plugin-gandi
Source0:            https://github.com/obynio/certbot-plugin-gandi/archive/refs/tags/%{version}.tar.gz

BuildRequires:      python3-devel
BuildRequires:      python3-setuptools
Requires:           certbot

%global debug_package %{nil}

%description
This is a plugin for Certbot that uses the Gandi LiveDNS API to allow Gandi customers to prove control of a domain name.

%prep
%autosetup -n certbot-plugin-gandi-%{version}

%build
env CFLAGS="$RPM_OPT_FLAGS" /usr/bin/python3 setup.py build

%install
/usr/bin/python3 setup.py install --single-version-externally-managed -O1 --root=%{buildroot} --record=INSTALLED_FILES

%clean
%{__rm} -rf %{buildroot}

%files -f INSTALLED_FILES
%defattr(-,root,root)
%doc README.md
%license LICENSE
