%define pypi_name    Jinja2
%define pypi_version 3.1.2
%define python_ver   3.9
%define python_mver  39

%undefine __brp_mangle_shebangs

Name:                python%{python_mver}-%{pypi_name}
Version:             %{pypi_version}
Release:             1%{?dist}
Summary:             A small but fast and easy to use stand-alone template engine written in pure python

License:             GPLv3+
URL:                 http://jinja.pocoo.org/
Source0:             https://files.pythonhosted.org/packages/source/%(echo %{pypi_name} | cut -c 1)/%{pypi_name}/%{pypi_name}-%{pypi_version}.tar.gz

BuildArch:           noarch
BuildRequires:       python%{python_mver}-devel
BuildRequires:       python%{python_mver}-setuptools
Requires:            python%{python_mver}-MarkupSafe = 2.1.1

%description
Jinja is a sandboxed template engine written in pure Python. It provides a Django like non-XML syntax
and compiles templates into executable python code. It’s basically a combination of Django templates and python code.

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
%doc README.rst
/usr/lib/python%{python_ver}/site-packages/jinja2
/usr/lib/python%{python_ver}/site-packages/%{pypi_name}-%{pypi_version}-py*.egg-info