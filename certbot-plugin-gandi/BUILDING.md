# How to build python3-certbot-plugin-gandi on AlmaLinux 8 and Python 3.6

Follow this doc to build python3-certbot-plugin-gandi for AlmaLinux 8 and Python 3.6.

* Original sources: https://github.com/obynio/certbot-plugin-gandi

Note: certbot is available on EPEL8 but for Python 3.6 only.
It's why python3-certbot-plugin-gandi is for python3.6 and not newer version of python.

To build python3-certbot-plugin-gandi:

```shell
dnf install -y rpmdevtools rpm-build git yum-utils python3-rpm-macros
rpmdev-setuptree
dnf update -y
git clone https://github.com/locobastos/certbot-plugin-gandi
cd certbot-plugin-gandi

spectool -g -C ~/rpmbuild/SOURCES/ -f python3-certbot-plugin-gandi.spec
yum-builddep -y python3-certbot-plugin-gandi.spec
rpmbuild -bb python3-certbot-plugin-gandi.spec
```

RPM file is located to: ~/rpmbuild/RPMS/x86_64/python3-certbot-plugin-gandi-1.3.2-1.el8.x86_64.rpm
