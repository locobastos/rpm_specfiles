%define gitowner    libfuse
%define gitrepo     pyfuse3
%define gitversion  3.2.1

%define python_ver  3.8
%define python_mver 38

Name:               python%{python_mver}-%{gitrepo}
Version:            %{gitversion}
Release:            1%{?dist}
Summary:            Python 3 bindings for libfuse 3 with async I/O support

License:            LGPL
URL:                https://github.com/%{gitowner}/%{gitrepo}
Source0:            https://github.com/%{gitowner}/%{gitrepo}/archive/refs/tags/release-%{version}.tar.gz

BuildArch:          x86_64
BuildRequires:      fuse3-devel
BuildRequires:      gcc
BuildRequires:      python%{python_mver}-Cython
BuildRequires:      python%{python_mver}-devel
BuildRequires:      python%{python_mver}-setuptools

%global debug_package %{nil}

%description
pyfuse3 is a set of Python 3 bindings for libfuse 3.
It provides an asynchronous API compatible with Trio and asyncio, and enables you to easily write a full-featured Linux filesystem in Python.

%prep
%autosetup -n %{gitrepo}-release-%{version}
# Build does not work with Cython-0.28.1
if [ -f /usr/bin/cython ]
then
    %{__mv} /usr/bin/cython /usr/bin/cython.bak
elif [ -L /usr/bin/cython ]
then
    %{__rm} -f /usr/bin/cython
fi
ln -s /usr/bin/cython-3.8 /usr/bin/cython

%build
env CFLAGS="$RPM_OPT_FLAGS" /usr/bin/python%{python_ver} setup.py build_cython
env CFLAGS="$RPM_OPT_FLAGS" /usr/bin/python%{python_ver} setup.py build_ext --inplace

%install
/usr/bin/python%{python_ver} setup.py install --single-version-externally-managed -O1 --root=%{buildroot} --record=INSTALLED_FILES

%clean
# Restauring default Cython
if [ -f /usr/bin/cython.bak ]
then
    %{__rm} -f /usr/bin/cython
    %{__mv} /usr/bin/cython.bak /usr/bin/cython
fi
%{__rm} -rf %{buildroot}

%files -f INSTALLED_FILES
%defattr(-,root,root)
%doc Changes.rst README.rst
%license LICENSE
