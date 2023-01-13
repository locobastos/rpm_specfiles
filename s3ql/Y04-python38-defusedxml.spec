%define gitowner    tiran
%define gitrepo     defusedxml
%define gitversion  0.7.1

%define python_ver  3.8
%define python_mver 38

Name:               python%{python_mver}-%{gitrepo}
Version:            %{gitversion}
Release:            1%{?dist}
Summary:            XML bomb protection for Python stdlib modules

License:            MIT
URL:                https://github.com/%{gitowner}/%{gitrepo}
Source0:            https://github.com/%{gitowner}/%{gitrepo}/archive/refs/tags/v%{version}.tar.gz

BuildArch:          noarch
BuildRequires:      python%{python_mver}-devel
BuildRequires:      python%{python_mver}-setuptools

%description
The results of an attack on a vulnerable XML library can be fairly dramatic.
With just a few hundred Bytes of XML data an attacker can occupy several Gigabytes
of memory within seconds. An attacker can also keep CPUs busy for a long time with
a small to medium size request. Under some circumstances it is even possible to access
local files on your server, to circumvent a firewall, or to abuse services to rebound
attacks to third parties.

The attacks use and abuse less common features of XML and its parsers.
The majority of developers are unacquainted with features such as processing instructions
and entity expansions that XML inherited from SGML. At best they know about <!DOCTYPE> from
experience with HTML but they are not aware that a document type definition (DTD) can generate
an HTTP request or load a file from the file system.

None of the issues is new. They have been known for a long time. Billion laughs was first
reported in 2003. Nevertheless some XML libraries and applications are still vulnerable
and even heavy users of XML are surprised by these features. It's hard to say whom to blame
for the situation. It's too short sighted to shift all blame on XML parsers and XML libraries
for using insecure default settings. After all they properly implement XML specifications.
Application developers must not rely that a library is always configured for security
and potential harmful data by default.

%prep
%autosetup -n %{gitrepo}-%{gitversion}

%build
/usr/bin/python%{python_ver} setup.py build

%install
/usr/bin/python%{python_ver} setup.py install --single-version-externally-managed -O1 --root=%{buildroot} --record=INSTALLED_FILES

%clean
%{__rm} -rf %{buildroot}

%files -f INSTALLED_FILES
%defattr(-,root,root)
%doc README.txt CHANGES.txt
%license LICENSE
