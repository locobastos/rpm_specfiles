# HAProxy RPM for CentOS 6, CentOS 7 and AlmaLinux 8

This repository contains necessary build files of HAProxy with no support and no expectation of stability.
The recommended way of using the repository is to build and test your own packages.

This repository fills my needs. I am not expecting to handle all CentOS environments and all HAProxy features.

All of this work starts from the latest HAProxy source RPM from CentOS 6 repositories: `haproxy-1.5.18-1.el6.src.rpm`.
For each newer version, I've read the Makefiles and the Changelogs to know what to adapt.

I've used official and fully updated docker images to build RPMs on each OS.

## How I've built RPMs

    # Install deps (CentOS 6 and CentOS 7)
    yum install -y rpmdevtools yum-utils

    # Install deps (AlmaLinux 8)
    dnf install -y dnf-utils rpmdevtools yum-utils
    dnf config-manager --set-enabled powertools

    # Build RPM
    yum-builddep -y haproxy.spec
    spectool -g -C "$(pwd)" haproxy.spec
    rpmbuild --define "_sourcedir $(pwd)" -bb haproxy.spec

## How I've tested

I've a configuration file with 2 backends, one redirecting to an Amazon RDS and a second one redirecting to an internal LDAP (389-ds).

For each version of HAProxy with my configuration file, I've checked that:
- The WebUI interface is reachable and show green line on my backends,
- An SQL connection to my Amazon RDS database works,
- An LDAP query works.

## Compilation information

Regarding the compilation parameters:

* TARGET="linux2628" from 1.5.19 to 1.9.16 included and TARGET="linux-glibc-legacy" from 2.0.0,
* OPENSSL is used. On a fully updated CentOS 6, the version of OpenSSL is 1.0.1e-58,
* GETADDRINFO is used since 1.5.19,
* PCRE is used from 1.5.19 to 1.7.14,
* PCRE2 and PCRE2_JIT are used since 1.8.0,
* LUA 5.3.6 is used from 1.6.0 to 2.0.16/2.1.7/2.2.1 and LUA 5.4.4 is used since 2.0.17/2.1.8/2.2.2/2.3.0,
* From 1.8.0 to 1.8.3 included, GCC threads are disabled as GCC is too old to compile HAProxy 1.8 with threads,
* But since 1.8.4, HAProxy added support for gcc < 4.7 and GCC threads are re-enabled,
* PROMETHEUS EXPORTER is used since 2.0.0,
* Using GLIBC RealTime shared library (USE_RT) since 2.0.0 because GLIBC < 2.17.

These parameters fill specific needs, feel free to adapt my work.

## Warnings

HAProxy (from 1.5.19 to 1.6.16 included) is incompatible with OpenSSL >= 1.1.0 due to the API changes.
