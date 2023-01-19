%define pypi_name    pycparser
%define pypi_version 2.21
%define python_ver   3.9
%define python_mver  39

%undefine __brp_mangle_shebangs

Name:                python%{python_mver}-%{pypi_name}
Version:             %{pypi_version}
Release:             1%{?dist}
Summary:             C parser in Python

License:             BSD
URL:                 https://github.com/eliben/pycparser
Source0:             https://files.pythonhosted.org/packages/source/%(echo %{pypi_name} | cut -c 1)/%{pypi_name}/%{pypi_name}-%{pypi_version}.tar.gz

BuildArch:           noarch
BuildRequires:       python%{python_mver}-devel
BuildRequires:       python%{python_mver}-setuptools

%description
Pure Python using the PLY parsing library.
It parses C code into an AST and can serve as a front-end for C compilers or analysis tools.

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
%doc README.rst
/usr/lib/python%{python_ver}/site-packages/%{pypi_name}
/usr/lib/python%{python_ver}/site-packages/%{pypi_name}-%{pypi_version}-py*.egg-info