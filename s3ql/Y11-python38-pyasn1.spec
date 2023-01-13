%define gitowner    etingof
%define gitrepo     pyasn1
%define gitversion  0.4.8

%define python_ver  3.8
%define python_mver 38

Name:               python%{python_mver}-%{gitrepo}
Version:            %{gitversion}
Release:            1%{?dist}
Summary:            Pure-Python implementation of ASN.1 types and DER/BER/CER codecs (X.208)

License:            MIT
URL:                https://github.com/%{gitowner}/%{gitrepo}
Source0:            https://github.com/%{gitowner}/%{gitrepo}/archive/refs/tags/v%{version}.tar.gz

BuildArch:          noarch
BuildRequires:      python%{python_mver}-devel
BuildRequires:      python%{python_mver}-setuptools

%description
This is a free and open source implementation of ASN.1 types and codecs as a Python package. It has been first
written to support particular protocol (SNMP) but then generalized to be suitable for a wide range of protocols
based on ASN.1 specification.

%prep
%autosetup -n %{gitrepo}-%{gitversion}

%build
/usr/bin/python%{python_ver} setup.py build

%install
/usr/bin/python%{python_ver} setup.py install --single-version-externally-managed -O1 --root=%{buildroot} --record=INSTALLED_FILES

%clean
%{__rm} -rf %{buildroot}

%files -f INSTALLED_FILES
%defattr(-,root,root)
%doc README.md
%license LICENSE.rst
