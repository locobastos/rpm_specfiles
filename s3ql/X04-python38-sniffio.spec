%define gitowner    python-trio
%define gitrepo     sniffio
%define gitversion  1.2.0

%define python_ver  3.8
%define python_mver 38

Name:               python%{python_mver}-%{gitrepo}
Version:            %{gitversion}
Release:            1%{?dist}
Summary:            Sniff out which async library your code is running under

License:            MIT
URL:                https://github.com/%{gitowner}/%{gitrepo}
Source0:            https://github.com/%{gitowner}/%{gitrepo}/archive/refs/tags/v%{version}.tar.gz

BuildArch:          noarch
BuildRequires:      python%{python_mver}-devel
BuildRequires:      python%{python_mver}-setuptools

%description
You're writing a library. You've decided to be ambitious, and support multiple async I/O packages,
like Trio and asyncio and ... You've written a bunch of clever code to handle all the differences. But...
how do you know which piece of clever code to run?

This is a tiny package whose only purpose is to let you detect which async library your code is running under.

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
%license LICENSE LICENSE.MIT LICENSE.APACHE2
