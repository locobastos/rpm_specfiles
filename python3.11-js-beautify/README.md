# How to install js-beautify on AlmaLinux 8 and using Python 3.11

js-beautify is a tool to reformat and re-indent bookmarklets, ugly JavaScript, unpack scripts packed by Dean Edward’s popular packer.

More information on the official GitHub repository: https://github.com/beautify-web/js-beautify

## Build js-beautify RPM

To build the RPM on AlmaLinux 8, you must enable nodejs:20 module first:

```shell
dnf module enable -y nodejs:20
```

Then, you can proceed with the common way to build the RPM:

```shell
yum-builddep -y python3.11-js-beautify.spec
spectool -g -C . python3.11-js-beautify.spec
rpmbuild -bb --define "_sourcedir $(pwd)" python3.11-js-beautify.spec
```
