%define pypi_name    PyYAML
%define pypi_version 6.0
%define python_ver   3.9
%define python_mver  39

%undefine __brp_mangle_shebangs

Name:                python%{python_mver}-%{pypi_name}
Version:             %{pypi_version}
Release:             1%{?dist}
Summary:             YAML parser and emitter for Python

License:             MIT
URL:                 https://pyyaml.org/
Source0:             https://files.pythonhosted.org/packages/source/%(echo %{pypi_name} | cut -c 1)/%{pypi_name}/%{pypi_name}-%{pypi_version}.tar.gz

BuildArch:           noarch
BuildRequires:       python%{python_mver}-devel
BuildRequires:       python%{python_mver}-setuptools

%description
YAML is a data serialization format designed for human readability and interaction with scripting languages.
PyYAML is a YAML parser and emitter for Python.

PyYAML features a complete YAML 1.1 parser, Unicode support, pickle support, capable extension API,
and sensible error messages. PyYAML supports standard YAML tags and provides Python-specific tags that
allow to represent an arbitrary Python object.

PyYAML is applicable for a broad range of tasks from complex configuration files to object serialization and persistence.

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
/usr/lib64/python%{python_ver}/site-packages/_yaml
/usr/lib64/python%{python_ver}/site-packages/yaml
/usr/lib64/python%{python_ver}/site-packages/%{pypi_name}-%{pypi_version}-py*.egg-info