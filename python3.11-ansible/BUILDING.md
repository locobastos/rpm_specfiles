# How to build python3.11-ansible and dependancies on AlmaLinux 8 and Python 3.11

Follow this doc to build python3.11-ansible (+ dependancies) for AlmaLinux 8 and Python 3.11:

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
~/rpmbuild/RPMS/noarch/python3.11-ansible-8.6.0-1.el8.noarch.rpm
~/rpmbuild/RPMS/noarch/python3.11-ansible-core-2.15.6-1.el8.noarch.rpm
~/rpmbuild/RPMS/noarch/python3.11-jinja2-3.1.2-1.el8.noarch.rpm
~/rpmbuild/RPMS/noarch/python3.11-resolvelib-1.0.1-1.el8.noarch.rpm
~/rpmbuild/RPMS/x86_64/python3.11-markupsafe-2.1.3-1.el8.x86_64.rpm
```
