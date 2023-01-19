%define pypi_name    cffi
%define pypi_version 1.15.1
%define python_ver   3.9
%define python_mver  39

%undefine __brp_mangle_shebangs
%define debug_package %{nil}

Name:                python%{python_mver}-%{pypi_name}
Version:             %{pypi_version}
Release:             1%{?dist}
Summary:             Foreign Function Interface for Python calling C code.

License:             MIT
URL:                 http://cffi.readthedocs.org/
Source0:             https://files.pythonhosted.org/packages/source/%(echo %{pypi_name} | cut -c 1)/%{pypi_name}/%{pypi_name}-%{pypi_version}.tar.gz

BuildArch:           x86_64
BuildRequires:       gcc
BuildRequires:       libffi-devel
BuildRequires:       python%{python_mver}-devel
BuildRequires:       python%{python_mver}-setuptools
Requires:            python%{python_mver}-pycparser = 2.21

%description
C Foreign Function Interface for Python. Interact with almost any C code from Python,
based on C-like declarations that you can often copy-paste from header files or documentation.

%prep
%autosetup -n %{pypi_name}-%{pypi_version}
# Fix Python3 shebang
/usr/bin/pathfix3.9.py -pni "/usr/bin/python3" .

%build
/usr/bin/python%{python_ver} setup.py build

%install
/usr/bin/python%{python_ver} setup.py install -O2 --root=%{buildroot}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root)
%license LICENSE
%doc README.md
/usr/lib64/python%{python_ver}/site-packages/%{pypi_name}
/usr/lib64/python%{python_ver}/site-packages/_cffi_backend.cpython-39-x86_64-linux-gnu.so
/usr/lib64/python%{python_ver}/site-packages/%{pypi_name}-%{pypi_version}-py*.egg-info