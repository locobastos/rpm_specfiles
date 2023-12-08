# ShellCheck for EL 7/8

This package provides up-to-date version of ShellCheck on CentOS 7 and AlmaLinux 8. I've not tested on other EL7/EL8 distributions.

## Context

If you install a CentOS 7 machine and run these commands:

    yum install -y epel-release
    yum update -y
    yum install ShellCheck

You will install ShellCheck version 0.3.8-1.el7

If you install a AlmaLinux 8 machine and run these commands:

	dnf install -y epel-release
	dnf update -y
	dnf install ShellCheck

You will install ShellCheck version 0.6.0-3.el8.

The latest version when I wrote this doc (2021/12/06) was ShellCheck 0.8.0.
