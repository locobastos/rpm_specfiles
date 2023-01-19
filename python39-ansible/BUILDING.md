# How to build python39-ansible and dependancies on AlmaLinux 8 and Python 3.9

Follow this doc to build python39-ansible (+ dependancies) for AlmaLinux 8 and Python 3.9:

## Prepare your OS

To build all dependancies AND ansible, you will need to install and activate all of this packages:

```shell
dnf install -y git rpmdevtools yum-utils
dnf update -y
rpmdev-setuptree
git clone https://github.com/locobastos/rpm_specfiles
cd rpm_specfiles/python39-ansible

for specfile in $(ls -1 *.spec | sort)
do
    spectool -g -C ~/rpmbuild/SOURCES/ -f ${specfile}
    yum-builddep -y ${specfile}
    rpmbuild -bb ${specfile}
done
```

RPM files are:

```
~/rpmbuild/RPMS/noarch/python39-ansible-7.1.0-1.el8.noarch.rpm
~/rpmbuild/RPMS/noarch/python39-ansible-core-2.14.1-1.el8.noarch.rpm
~/rpmbuild/RPMS/noarch/python39-Jinja2-3.1.2-1.el8.noarch.rpm
~/rpmbuild/RPMS/noarch/python39-pycparser-2.21-1.el8.noarch.rpm
~/rpmbuild/RPMS/noarch/python39-PyYAML-6.0-1.el8.noarch.rpm
~/rpmbuild/RPMS/noarch/python39-resolvelib-0.8.1-1.el8.noarch.rpm
~/rpmbuild/RPMS/x86_64/python39-cffi-1.15.1-1.el8.x86_64.rpm
~/rpmbuild/RPMS/x86_64/python39-MarkupSafe-2.1.1-1.el8.x86_64.rpm
```
