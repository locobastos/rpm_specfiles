%define gitowner    grantjenks
%define gitrepo     python-sortedcontainers
%define gitversion  2.4.0

%define python_ver  3.8
%define python_mver 38

Name:               python%{python_mver}-sortedcontainers
Version:            %{gitversion}
Release:            1%{?dist}
Summary:            Sorted Containers -- Sorted List, Sorted Dict, Sorted Set

License:            MIT
URL:                https://github.com/%{gitowner}/%{gitrepo}
Source0:            https://github.com/%{gitowner}/%{gitrepo}/archive/refs/tags/v%{version}.tar.gz

BuildArch:          noarch
BuildRequires:      python%{python_mver}-devel
BuildRequires:      python%{python_mver}-setuptools

%description
Sorted Containers is an Apache2 licensed sorted collections library,
written in pure-Python, and fast as C-extensions.

Python's standard library is great until you need a sorted collections
type. Many will attest that you can get really far without one, but the moment
you really need a sorted list, sorted dict, or sorted set, you're faced
with a dozen different implementations, most using C-extensions without great
documentation and benchmarking.

In Python, we can do better. And we can do it in pure-Python!

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
%doc README.rst
%license LICENSE
