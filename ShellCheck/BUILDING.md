# How to build ShellCheck

```shell
yum install -y rpmdevtools yum-utils
yum update -y
rpmdev-setuptree
git clone https://github.com/locobastos/rpm_specfiles
cd rpm_specfiles/ShellCheck
spectool -g -C ~/rpmbuild/SOURCES/ -f ShellCheck.spec
rpmbuild -bb ShellCheck.spec
```

RPM files is located to:

```
~/rpmbuild/RPMS/x86_64/ShellCheck-0.9.0-1.el8.x86_64.rpm
```
