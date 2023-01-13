%define gitowner    sybrenstuvel
%define gitrepo     python-rsa
%define gitversion  4.7.2
# 4.7.2 is the latest version including setup.py file

%define python_ver  3.8
%define python_mver 38

Name:               python%{python_mver}-rsa
Version:            %{gitversion}
Release:            1%{?dist}
Summary:            Python-RSA is a pure-Python RSA implementation.

License:            MIT
URL:                https://github.com/%{gitowner}/%{gitrepo}
Source0:            https://github.com/%{gitowner}/%{gitrepo}/archive/refs/tags/version-%{version}.tar.gz

BuildArch:          noarch
BuildRequires:      python%{python_mver}-devel
BuildRequires:      python%{python_mver}-setuptools

%description
Python-RSA is a pure-Python RSA implementation. It supports encryption and decryption,
signing and verifying signatures, and key generation according to PKCS-1 version 1.5.

%prep
%autosetup -n %{gitrepo}-version-%{gitversion}

%build
/usr/bin/python%{python_ver} setup.py build

%install
/usr/bin/python%{python_ver} setup.py install --single-version-externally-managed -O1 --root=%{buildroot} --record=INSTALLED_FILES

%clean
%{__rm} -rf %{buildroot}

%files -f INSTALLED_FILES
%defattr(-,root,root)
%doc README.md CHANGELOG.md
%license LICENSE
