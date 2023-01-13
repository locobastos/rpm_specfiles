%define gitowner    python-dugong
%define gitrepo     python-dugong
%define gitversion  3.8.2

%define python_ver  3.8
%define python_mver 38

Name:               python%{python_mver}-dugong
Version:            %{gitversion}
Release:            1%{?dist}
Summary:            A HTTP 1.1 client module supporting asynchronous IO, pipelining and `Expect: 100-continue`. Designed for RESTful protocols.

License:            PSF
URL:                https://github.com/%{gitowner}/%{gitrepo}
Source0:            https://github.com/%{gitowner}/%{gitrepo}/archive/refs/tags/release-%{version}.tar.gz

BuildArch:          noarch
BuildRequires:      python%{python_mver}-devel
BuildRequires:      python%{python_mver}-setuptools

%description
The Python Dugong module provides an API for communicating with HTTP 1.1
servers. It is an alternative to the standard library's http.client
(formerly httplib) module.

%prep
%autosetup -n %{gitrepo}-release-%{version}

%build
/usr/bin/python%{python_ver} setup.py build

%install
/usr/bin/python%{python_ver} setup.py install --single-version-externally-managed -O1 --root=%{buildroot} --record=INSTALLED_FILES

%clean
%{__rm} -rf %{buildroot}

%files -f INSTALLED_FILES
%defattr(-,root,root)
%doc Changes.rst README.rst
%license LICENSE
