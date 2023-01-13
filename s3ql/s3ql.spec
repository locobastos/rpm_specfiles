%define gitowner    s3ql
%define gitrepo     s3ql
%define gitversion  4.0.0

%define python_ver  3.8
%define python_mver 38

Name:               %{gitrepo}
Version:            %{gitversion}
Release:            1%{?dist}
Summary:            Full-Featured File System for Online Data Storage

License:            GPLv3
URL:                https://github.com/%{gitowner}/%{gitrepo}
Source0:            https://github.com/%{gitowner}/%{gitrepo}/archive/refs/tags/release-%{version}.tar.gz

BuildArch:          x86_64
BuildRequires:      gcc
BuildRequires:      python%{python_mver}-Cython
BuildRequires:      python%{python_mver}-async-generator
BuildRequires:      python%{python_mver}-attrs
BuildRequires:      python%{python_mver}-devel
BuildRequires:      python%{python_mver}-idna
BuildRequires:      python%{python_mver}-outcome
BuildRequires:      python%{python_mver}-pyfuse3
BuildRequires:      python%{python_mver}-setuptools
BuildRequires:      python%{python_mver}-sniffio
BuildRequires:      python%{python_mver}-sortedcontainers
BuildRequires:      python%{python_mver}-trio
BuildRequires:      sqlite-devel
Requires:           python%{python_mver}-apsw
Requires:           python%{python_mver}-async-generator
Requires:           python%{python_mver}-attrs
Requires:           python%{python_mver}-cachetools >= 2.0.0
Requires:           python%{python_mver}-cryptography
Requires:           python%{python_mver}-defusedxml
Requires:           python%{python_mver}-dugong >= 3.4
Requires:           python%{python_mver}-google-auth
Requires:           python%{python_mver}-google-auth-oauthlib
Requires:           python%{python_mver}-oauthlib
Requires:           python%{python_mver}-outcome
Requires:           python%{python_mver}-pyasn1
Requires:           python%{python_mver}-pyasn1-modules >= 0.2.1
Requires:           python%{python_mver}-pyfuse3
Requires:           python%{python_mver}-requests
Requires:           python%{python_mver}-requests-oauthlib
Requires:           python%{python_mver}-rsa
Requires:           python%{python_mver}-sniffio
Requires:           python%{python_mver}-sortedcontainers
Requires:           python%{python_mver}-trio

%global debug_package %{nil}

%description
S3QL is a file system that stores all its data online using storage services
like Google Storage, Amazon S3 or OpenStack. S3QL effectively provides a hard
disk of dynamic, infinite capacity that can be accessed from any computer
with Internet access.

S3QL is a standard conforming, full featured UNIX file system that is
conceptually indistinguishable from any local file system. Furthermore, S3QL
has additional features like compression, encryption, data de-duplication,
immutable trees and snapshotting which make it especially suitable for on-line
backup and archival.

S3QL is designed to favor simplicity and elegance over performance and feature-
creep. Care has been taken to make the source code as readable and serviceable
as possible. Solid error detection and error handling have been included
from the very first line, and S3QL comes with extensive automated test cases
for all its components.

== Features ==
* Transparency. Conceptually, S3QL is indistinguishable from a local file 
system. For example, it supports hardlinks, symlinks, standard unix 
permissions, extended attributes and file sizes up to 2 TB.

* Dynamic Size. The size of an S3QL file system grows and shrinks dynamically 
as required.

* Compression. Before storage, all data may compressed with the LZMA, bzip2 
or deflate (gzip) algorithm.

* Encryption. After compression (but before upload), all data can AES 
encrypted with a 256 bit key. An additional SHA256 HMAC checksum is used to 
protect the data against manipulation.

* Data De-duplication. If several files have identical contents, the redundant
data will be stored only once. This works across all files stored in the file 
system, and also if only some parts of the files are identical while other 
parts differ.
* Immutable Trees. Directory trees can be made immutable, so that their 
contents can no longer be changed in any way whatsoever. This can be used to 
ensure that backups can not be modified after they have been made.

* Copy-on-Write/Snapshotting. S3QL can replicate entire directory trees 
without using any additional storage space. Only if one of the copies is 
modified, the part of the data that has been modified will take up additional 
storage space. This can be used to create intelligent snapshots that preserve 
the state of a directory at different points in time using a minimum amount 
of space.

* High Performance independent of network latency. All operations that do not 
write or read file contents (like creating directories or moving, renaming, 
and changing permissions of files and directories) are very fast because they 
are carried out without any network transactions.

S3QL achieves this by saving the entire file and directory structure in a 
database. This database is locally cached and the remote copy updated 
asynchronously.

* Support for low bandwidth connections. S3QL splits file contents into 
smaller blocks and caches blocks locally. This minimizes both the number of 
network transactions required for reading and writing data, and the amount of 
data that has to be transferred when only parts of a file are read or written.

%prep
%setup -qn s3ql-release-%{version}
# The build does not work with Cython-0.28.1
if [ -f /usr/bin/cython ]
then
    %{__mv} /usr/bin/cython /usr/bin/cython.bak
elif [ -L /usr/bin/cython ]
then
    %{__rm} -f /usr/bin/cython
fi
ln -s /usr/bin/cython-3.8 /usr/bin/cython
rm -rf doc/html/man
rm -rf doc/html/.buildinfo
rm -rf src/%{name}.egg-info
chmod 644 contrib/*

%build
/usr/bin/python%{python_ver} setup.py build_cython
/usr/bin/python%{python_ver} setup.py build_ext --inplace
/usr/bin/python%{python_ver} setup.py build

%install
/usr/bin/python%{python_ver} setup.py install --single-version-externally-managed -O1 --root=%{buildroot} --record=INSTALLED_FILES

%clean
# Restauring default Cython
if [ -f /usr/bin/cython.bak ]
then
    %{__rm} -f /usr/bin/cython
    %{__mv} /usr/bin/cython.bak /usr/bin/cython
fi
%{__rm} -rf %{buildroot}

%files -f INSTALLED_FILES
%defattr(-,root,root)
%doc Changes.txt README.rst
%license LICENSE
