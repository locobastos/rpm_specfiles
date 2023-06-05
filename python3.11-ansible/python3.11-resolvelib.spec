%define pypi_name    resolvelib
%define pypi_version 1.0.1
%define python_ver   3.11

%undefine __brp_mangle_shebangs

Name:                python%{python_ver}-%{pypi_name}
Version:             %{pypi_version}
Release:             1%{?dist}
Summary:             Resolve abstract dependencies into concrete ones

License:             ISCL
URL:                 https://github.com/sarugaku/resolvelib
Source0:             https://files.pythonhosted.org/packages/source/%(echo %{pypi_name} | cut -c 1)/%{pypi_name}/%{pypi_name}-%{pypi_version}.tar.gz

BuildArch:           noarch
BuildRequires:       python%{python_ver}-devel
BuildRequires:       python%{python_ver}-setuptools

%description
ResolveLib at the highest level provides a Resolver class that includes dependency resolution logic.
You give it some things, and a little information on how it should interact with them, and it will spit out a resolution result.

%prep
%autosetup -n %{pypi_name}-%{pypi_version}
# Fix Python3 shebang
/usr/bin/pathfix%{python_ver}.py -pni "/usr/bin/python3" .

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
/usr/lib/python%{python_ver}/site-packages/%{pypi_name}-%{pypi_version}-py%{python_ver}.egg-info