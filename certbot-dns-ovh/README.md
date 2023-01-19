# How to install certbot-dns-ovh on AlmaLinux 8

Follow this doc to install certbot-dns-ovh on AlmaLinux 8.

## Fork information

My initial repository was a fork from certbot/certbot.

This fork's aim is to package certbot-dns-ovh for AlmaLinux 8 for my needs only, without any warranty or support.
Everything was done from a minimal install of AlmaLinux 8 from AlmaLinux-8.6-x86_64-minimal.iso

## Install certbot-dns-ovh

To install certbot-dns-ovh, you will need to install and activate epel-release on which certbot is available.

```shell
dnf install -y epel-release
dnf update -y
dnf install -y python3-certbot-dns-ovh
```
