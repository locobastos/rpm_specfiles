%define pypi_name    ansible
%define pypi_version 9.1.0
%define python_ver   3.11

%undefine __brp_mangle_shebangs

Name:                python%{python_ver}-%{pypi_name}
Version:             %{pypi_version}
Release:             1%{?dist}
Summary:             Radically simple IT automation

License:             GPLv3+
URL:                 https://ansible.com/
Source0:             https://files.pythonhosted.org/packages/source/%(echo %{pypi_name} | cut -c 1)/%{pypi_name}/%{pypi_name}-%{pypi_version}.tar.gz

BuildArch:           noarch
BuildRequires:       python%{python_ver}-devel
BuildRequires:       python%{python_ver}-setuptools
Requires:            python%{python_ver}-ansible-core = 2.16.1

%description
Ansible is a radically simple IT automation system. It handles configuration management,
application deployment, cloud provisioning, ad-hoc task execution, network automation,
and multi-node orchestration. Ansible makes complex changes like zero-downtime rolling updates
with load balancers easy.

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
%doc README.rst
/usr/bin/ansible-community
/usr/lib/python%{python_ver}/site-packages/ansible_collections
/usr/lib/python%{python_ver}/site-packages/%{pypi_name}-%{pypi_version}-py*.egg-info