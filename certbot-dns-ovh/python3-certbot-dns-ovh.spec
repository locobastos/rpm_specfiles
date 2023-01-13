Name:               python3-certbot-dns-ovh
Version:            1.22.0
Release:            1%{?dist}
Summary:            OVH DNS Authenticator plugin for Certbot

License:            MIT
URL:                https://github.com/certbot/certbot
Source0:            https://github.com/certbot/certbot/archive/refs/tags/v%{version}.tar.gz

BuildRequires:      python3-devel
BuildRequires:      python3-setuptools
Requires:           certbot
Requires:           python3-dns-lexicon

%global debug_package %{nil}

%description
OVH DNS Authenticator plugin for Certbot

%prep
%autosetup -n certbot-%{version}
%{__rm} -rf .azure-pipelines .coveragerc .dockerignore .editorconfig .envrc .git* .isort.cfg .pylintrc
%{__rm} -rf acme
%{__rm} -rf certbot
%{__rm} -rf certbot-apache
%{__rm} -rf certbot-ci
%{__rm} -rf certbot-compatibility-test
%{__rm} -rf certbot-dns-cloudflare
%{__rm} -rf certbot-dns-cloudxns
%{__rm} -rf certbot-dns-digitalocean
%{__rm} -rf certbot-dns-dnsimple
%{__rm} -rf certbot-dns-dnsmadeeasy
%{__rm} -rf certbot-dns-gehirn
%{__rm} -rf certbot-dns-google
%{__rm} -rf certbot-dns-linode
%{__rm} -rf certbot-dns-luadns
%{__rm} -rf certbot-dns-nsone
%{__rm} -rf certbot-dns-rfc2136
%{__rm} -rf certbot-dns-route53
%{__rm} -rf certbot-dns-sakuracloud
%{__rm} -rf certbot-nginx
%{__rm} -rf letsencrypt-auto-source
%{__rm} -rf letstest
%{__rm} -rf snap
%{__rm} -rf tests
%{__rm} -rf tools
%{__rm} -rf windows-installer
%{__rm} -f *.md *.ini
%{__rm} -f tox.cover.py README.rst linter_plugin.py LICENSE.txt Dockerfile-dev docker-compose.yml
%{__mv} certbot-dns-ovh/* .
%{__rm} -rf certbot-dns-ovh

%build
env CFLAGS="$RPM_OPT_FLAGS" /usr/bin/python3 setup.py build

%install
/usr/bin/python3 setup.py install --single-version-externally-managed -O1 --root=%{buildroot} --record=INSTALLED_FILES

%clean
%{__rm} -rf %{buildroot}

%files -f INSTALLED_FILES
%defattr(-,root,root)
%doc README.rst
%license LICENSE.txt
