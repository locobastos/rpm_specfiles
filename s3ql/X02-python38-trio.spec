%define gitowner    python-trio
%define gitrepo     trio
%define gitversion  0.21.0

%define python_ver  3.8
%define python_mver 38

Name:               python%{python_mver}-%{gitrepo}
Version:            %{gitversion}
Release:            1%{?dist}
Summary:            A friendly Python library for async concurrency and I/O

License:            MIT OR Apache-2.0
URL:                https://github.com/%{gitowner}/%{gitrepo}
Source0:            https://github.com/%{gitowner}/%{gitrepo}/archive/refs/tags/v%{version}.tar.gz

BuildArch:          noarch
BuildRequires:      python%{python_mver}-devel
BuildRequires:      python%{python_mver}-setuptools

%description
The Trio project's goal is to produce a production-quality, permissively
licensed, async/await-native I/O library for Python. Like all async libraries,
its main purpose is to help you write programs that do multiple
things at the same time with parallelized I/O. A web spider that
wants to fetch lots of pages in parallel, a web server that needs to
juggle lots of downloads and websocket connections at the same time, a
process supervisor monitoring multiple subprocesses... that sort of
thing. Compared to other libraries, Trio attempts to distinguish
itself with an obsessive focus on usability and
correctness. Concurrency is complicated; we try to make it easy
to get things right.

%prep
%autosetup -n %{gitrepo}-%{version}

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
