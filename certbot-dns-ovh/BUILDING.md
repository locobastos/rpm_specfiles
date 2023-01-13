# How to build python3-certbot-dns-ovh on AlmaLinux 8 and Python 3.6

Follow this doc to build python3-certbot-dns-ovh for AlmaLinux 8 and Python 3.6.

* Original sources: https://github.com/certbot/certbot

Note: certbot is available on EPEL8 but for Python 3.6 only.
It's why python3-certbot-dns-ovh is for python3.6 and not newer version of python.

To build python3-certbot-dns-ovh:

```shell
dnf install -y rpmdevtools rpm-build git yum-utils python3-rpm-macros
rpmdev-setuptree
dnf update -y
git clone https://github.com/locobastos/certbot-dns-ovh
cd certbot-dns-ovh

spectool -g -C ~/rpmbuild/SOURCES/ -f python3-certbot-dns-ovh.spec
yum-builddep -y python3-certbot-dns-ovh.spec
rpmbuild -bb python3-certbot-dns-ovh.spec
```

RPM file is located to: ~/rpmbuild/RPMS/x86_64/python3-certbot-dns-ovh-1.22.0-1.el8.x86_64.rpm
