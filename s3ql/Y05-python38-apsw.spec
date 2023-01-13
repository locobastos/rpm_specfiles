%define gitowner    rogerbinns
%define gitrepo     apsw
%define gitversion  3.26.0
# 3.26.0-r1 is the latest version compatible with SQLite 3.26.0 available on AlmaLinux 8

%define python_ver  3.8
%define python_mver 38

Name:               python%{python_mver}-%{gitrepo}
Version:            %{gitversion}
Release:            r1%{?dist}
Summary:            Another Python SQLite wrapper

License:            MIT
URL:                https://github.com/%{gitowner}/%{gitrepo}
Source0:            https://github.com/%{gitowner}/%{gitrepo}/archive/refs/tags/%{version}-r1.tar.gz

BuildArch:          x86_64
BuildRequires:      gcc
BuildRequires:      python%{python_mver}-devel
BuildRequires:      python%{python_mver}-setuptools
BuildRequires:      sqlite-devel

%global debug_package %{nil}

%description
A Python wrapper for the SQLite embedded relational database engine.
APSW exposes SQLite as it really is, while the stdlib sqlite3 module makes SQLite
look like other databases via DBAPI. Everything you can do from the SQLite C API, you can do from APSW.

%prep
%autosetup -n %{gitrepo}-%{gitversion}-r1

%build
/usr/bin/python%{python_ver} setup.py build

%install
/usr/bin/python%{python_ver} setup.py install --single-version-externally-managed -O1 --root=%{buildroot} --record=INSTALLED_FILES

%clean
%{__rm} -rf %{buildroot}

%files -f INSTALLED_FILES
%defattr(-,root,root)
%doc README.rst
%license LICENSE
