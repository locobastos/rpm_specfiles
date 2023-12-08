# How to build python3.11-ansible and dependancies on AlmaLinux 8 and Python 3.11

Follow this doc to build python3.11-ansible (+ dependancies) for AlmaLinux 8 and Python 3.11:

## Check dependances

To know the dependancies:

```shell
dnf update -y
dnf install -y python3.11 python3.11-pip
pip3.11 install ansible==9.1.0 pipdeptree
pipdeptree
```

The last command will print the minimal required versions and the installed ones:

```shell
ansible==9.1.0
└── ansible-core [required: ~=2.16.1, installed: 2.16.1]
    ├── cryptography [required: Any, installed: 41.0.7]
    │   └── cffi [required: >=1.12, installed: 1.16.0]
    │       └── pycparser [required: Any, installed: 2.21]
    ├── Jinja2 [required: >=3.0.0, installed: 3.1.2]
    │   └── MarkupSafe [required: >=2.0, installed: 2.1.3]
    ├── packaging [required: Any, installed: 23.2]
    ├── PyYAML [required: >=5.1, installed: 6.0.1]
    └── resolvelib [required: >=0.5.3,<1.1.0, installed: 1.0.1]
```

## Prepare your OS

To build all dependancies AND ansible, you will need to install and activate all of this packages:

```shell
dnf install -y git rpmdevtools yum-utils
dnf update -y
rpmdev-setuptree
git clone https://github.com/locobastos/rpm_specfiles
cd rpm_specfiles/python3.11-ansible
yum-builddep -y python3.11-ansible.spec

for specfile in $(ls -1 *.spec | sort)
do
    spectool -g -C ~/rpmbuild/SOURCES/ -f ${specfile}
    rpmbuild -bb ${specfile}
done
```

RPM files are:

```
~/rpmbuild/RPMS/noarch/python3.11-ansible-9.1.0-1.el8.noarch.rpm
~/rpmbuild/RPMS/noarch/python3.11-ansible-core-2.16.1-1.el8.noarch.rpm
~/rpmbuild/RPMS/noarch/python3.11-jinja2-3.1.2-1.el8.noarch.rpm
~/rpmbuild/RPMS/noarch/python3.11-resolvelib-1.0.1-1.el8.noarch.rpm
~/rpmbuild/RPMS/x86_64/python3.11-markupsafe-2.1.3-1.el8.x86_64.rpm
```
