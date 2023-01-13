%define gitowner    etingof
%define gitrepo     pyasn1-modules
%define gitversion  0.2.8

%define python_ver  3.8
%define python_mver 38

Name:               python%{python_mver}-%{gitrepo}
Version:            %{gitversion}
Release:            1%{?dist}
Summary:            ASN.1 modules for pyasn1 library.

License:            MIT
URL:                https://github.com/%{gitowner}/%{gitrepo}
Source0:            https://github.com/%{gitowner}/%{gitrepo}/archive/refs/tags/v%{version}.tar.gz

BuildArch:          noarch
BuildRequires:      python%{python_mver}-devel
BuildRequires:      python%{python_mver}-setuptools

%description
The pyasn1-modules package contains a collection of ASN.1 data structures expressed as Python classes based on pyasn1 data model.
If ASN.1 module you need is not present in this collection, try using Asn1ate tool that compiles ASN.1 documents into pyasn1 code.

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
%license LICENSE.txt
