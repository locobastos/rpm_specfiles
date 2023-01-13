# How to install s3ql on AlmaLinux 8

Follow this doc to install s3ql on AlmaLinux 8.

## Fork information

My initial repository was a fork from tardfree/s3ql-rpm repo.
This fork's aim is to package s3ql for AlmaLinux 8 for my needs only, without any warranty or support.
Everything was done from a minimal install of AlmaLinux 8 from AlmaLinux-8.6-x86_64-minimal.iso

## Install s3ql

To install s3ql, you will need to install and activate all of this packages/repositories.
Either install all 11 Y* RPM built, or publish theses RPM in an available repository.

```shell
dnf config-manager --set-enabled powertools
dnf module enable -y python38-devel
dnf update -y
dnf install -y s3ql
```
