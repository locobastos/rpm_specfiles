# How to install ansible on AlmaLinux 8 and using Python 3.11

Follow this doc to install ansible on AlmaLinux 8.

The aim is to package ansible for AlmaLinux 8 for my needs only, without any warranty or support.

## Install ansible

Once you have built and release all related RPMs to a Linux repository:

```shell
dnf install -y --enablerepo="powertools" python3.11-ansible
```
