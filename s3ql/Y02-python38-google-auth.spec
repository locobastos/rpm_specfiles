%define gitowner    googleapis
%define gitrepo     google-auth-library-python
%define gitversion  2.9.1

%define python_ver  3.8
%define python_mver 38

Name:               python%{python_mver}-google-auth
Version:            %{gitversion}
Release:            1%{?dist}
Summary:            Google Authentication Library.

License:            MIT
URL:                https://github.com/%{gitowner}/%{gitrepo}
Source0:            https://github.com/%{gitowner}/%{gitrepo}/archive/refs/tags/v%{version}.tar.gz

BuildArch:          noarch
BuildRequires:      python%{python_mver}-devel
BuildRequires:      python%{python_mver}-setuptools

%description
This library simplifies using Google’s various server-to-server authentication mechanisms to access Google APIs.

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
