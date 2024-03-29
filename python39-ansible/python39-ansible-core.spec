%define pypi_name    ansible-core
%define pypi_version 2.14.1
%define python_ver   3.9
%define python_mver  39

%undefine __brp_mangle_shebangs

Name:                python%{python_mver}-%{pypi_name}
Version:             %{pypi_version}
Release:             2%{?dist}
Summary:             Radically simple IT automation

License:             GPLv3+
URL:                 https://ansible.com/
Source0:             https://files.pythonhosted.org/packages/source/%(echo %{pypi_name} | cut -c 1)/%{pypi_name}/%{pypi_name}-%{pypi_version}.tar.gz

BuildArch:           noarch
BuildRequires:       python%{python_mver}-devel
BuildRequires:       python%{python_mver}-setuptools
Requires:            python%{python_mver}-cryptography
Requires:            python%{python_mver}-Jinja2 = 3.1.2
Requires:            python%{python_mver}-PyYAML = 6.0
Requires:            python%{python_mver}-resolvelib = 0.8.1
Requires:            python3-packaging
Requires:            sshpass

%description
Ansible is a radically simple IT automation system. It handles configuration management,
application deployment, cloud provisioning, ad-hoc task execution, network automation,
and multi-node orchestration. Ansible makes complex changes like zero-downtime rolling updates
with load balancers easy.

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
/usr/bin/ansible
/usr/bin/ansible-config
/usr/bin/ansible-connection
/usr/bin/ansible-console
/usr/bin/ansible-doc
/usr/bin/ansible-galaxy
/usr/bin/ansible-inventory
/usr/bin/ansible-playbook
/usr/bin/ansible-pull
/usr/bin/ansible-test
/usr/bin/ansible-vault
/usr/lib/python%{python_ver}/site-packages/ansible
/usr/lib/python%{python_ver}/site-packages/ansible_test
/usr/lib/python%{python_ver}/site-packages/ansible_core-%{pypi_version}-py*.egg-info