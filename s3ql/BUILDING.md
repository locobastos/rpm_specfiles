# How to build s3ql and dependancies on AlmaLinux 8 and Python 3.8

Follow this doc to build s3ql for AlmaLinux 8 and Python 3.8.

* Original sources: https://github.com/s3ql/s3ql

## Prepare your OS

To build all dependancies AND s3ql, you will need to install and activate all of this packages/repositories:

```shell
dnf install -y rpmdevtools rpm-build git yum-utils python3-rpm-macros
dnf config-manager --set-enabled powertools
dnf module enable -y python38-devel
dnf update -y
rpmdev-setuptree
git clone https://github.com/locobastos/s3ql-rpm-al8.git
cd s3ql-rpm-al8
```

## Build

### Dependancies

Specfiles beginning with X are the s3ql BuildRequires packages.
Specfiles beginning with Y are the s3ql Requires packages.

```shell
for specfile in $(ls -1 {X,Y}*.spec | sort)
do
    spectool -g -C ~/rpmbuild/SOURCES/ -f ${specfile}
    yum-builddep -y ${specfile}
    rpmbuild -bb ${specfile}
done
```

### s3ql

Either install all 6 X* RPM built during the previous step, or publish theses RPM in an available repository.

```shell
spectool -g -C ~/rpmbuild/SOURCES/ -f s3ql.spec
yum-builddep -y s3ql.spec
rpmbuild -bb s3ql.spec
```

## TODO

* Check if all licenses are the original ones
* Check if '%doc' and '%license' are complete
* Generate documentations for all packages which have documentation
* Test all source code with pytest (for package which have tests)
