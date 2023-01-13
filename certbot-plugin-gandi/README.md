# How to install certbot-plugin-gandi on AlmaLinux 8

Follow this doc to install certbot-plugin-gandi on AlmaLinux 8.

## Fork information

My initial repository was a fork from obynio/certbot-plugin-gandi.
This fork's aim is to package certbot-plugin-gandi for AlmaLinux 8 for my needs only, without any warranty or support.
Everything was done from a minimal install of AlmaLinux 8 from AlmaLinux-8.6-x86_64-minimal.iso

## Install certbot-plugin-gandi

To install certbot-plugin-gandi, you will need to install and activate epel-release on which certbot is available.

```shell
dnf install -y epel-release
dnf update -y
dnf install -y python3-certbot-plugin-gandi
```
