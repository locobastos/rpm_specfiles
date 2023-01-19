%define pypi_name    MarkupSafe
%define pypi_version 2.1.1
%define python_ver   3.9
%define python_mver  39

%undefine __brp_mangle_shebangs
%define debug_package %{nil}

Name:                python%{python_mver}-%{pypi_name}
Version:             %{pypi_version}
Release:             1%{?dist}
Summary:             Safely add untrusted strings to HTML/XML markup.

License:             BSD-3-Clause
URL:                 https://palletsprojects.com/p/markupsafe/
Source0:             https://files.pythonhosted.org/packages/source/%(echo %{pypi_name} | cut -c 1)/%{pypi_name}/%{pypi_name}-%{pypi_version}.tar.gz

BuildArch:           x86_64
BuildRequires:       python%{python_mver}-devel
BuildRequires:       python%{python_mver}-setuptools

%description
MarkupSafe implements a text object that escapes characters so it is safe to use in HTML and XML.
Characters that have special meanings are replaced so that they display as the actual characters.
This mitigates injection attacks, meaning untrusted user input can safely be displayed on a page.

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
%license LICENSE.rst
%doc README.rst
/usr/lib64/python%{python_ver}/site-packages/markupsafe
/usr/lib64/python%{python_ver}/site-packages/%{pypi_name}-%{pypi_version}-py*.egg-info