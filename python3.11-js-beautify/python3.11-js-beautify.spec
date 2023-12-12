Name:               python3.11-js-beautify
Version:            1.14.9
Release:            1%{?dist}
Summary:            Beautifier for javascript

License:            MIT
URL:                https://github.com/beautify-web/js-beautify
Source0:            https://github.com/beautify-web/js-beautify/archive/refs/tags/v%{version}.tar.gz

BuildRequires:      python3.11-devel
BuildRequires:      python3.11-setuptools
BuildRequires:      python3.11-pip
BuildRequires:      make
BuildRequires:      nodejs >= 1:20.0.0
Requires:           python3.11-six

%global debug_package %{nil}

%description
This little beautifier will reformat and re-indent bookmarklets, ugly JavaScript,
unpack scripts packed by Dean Edward's popular packer, as well as partly
deobfuscate scripts processed by the npm package javascript-obfuscator.

%prep
%autosetup -n js-beautify-%{version}
npm install mustache
pip3.11 install virtualenv
sed -i 's/python/python3.11/' %{_builddir}/js-beautify-%{version}/tools/python
/usr/bin/pathfix3.11.py -pni "/usr/bin/python3" .
%{__make} py
%{__make} pytest
%{__make} python/dist/*
%{__mv} -v python/dist/*.tar.gz %{_sourcedir}/

# jsbeautifier
cd %{_builddir}
%{__rm} --force --recursive jsbeautifier-%{version}/
%{__tar} --extract --verbose --file=%{_sourcedir}/jsbeautifier-%{version}.tar.gz
cd jsbeautifier-%{version}
%{__chmod} -Rf a+rX,u+w,g-w,o-w .

# cssbeautifier
cd %{_builddir}
%{__rm} --force --recursive cssbeautifier-%{version}/
%{__tar} --extract --verbose --file=%{_sourcedir}/cssbeautifier-%{version}.tar.gz
cd cssbeautifier-%{version}
%{__chmod} -Rf a+rX,u+w,g-w,o-w .

%build
cd %{_builddir}/jsbeautifier-%{version}/
/usr/bin/python3.11 setup.py build

cd %{_builddir}/cssbeautifier-%{version}/
/usr/bin/python3.11 setup.py build

%install
cd %{_builddir}/jsbeautifier-%{version}/
/usr/bin/python3.11 setup.py install --single-version-externally-managed -O1 --root=%{buildroot} --record=%{_builddir}/js-beautify-%{version}/INSTALLED_FILES_JS_BEAUTIFY

cd %{_builddir}/cssbeautifier-%{version}/
/usr/bin/python3.11 setup.py install --single-version-externally-managed -O1 --root=%{buildroot} --record=%{_builddir}/js-beautify-%{version}/INSTALLED_FILES_CSS_BEAUTIFY

cat %{_builddir}/js-beautify-%{version}/INSTALLED_FILES_JS_BEAUTIFY %{_builddir}/js-beautify-%{version}/INSTALLED_FILES_CSS_BEAUTIFY > %{_builddir}/js-beautify-%{version}/INSTALLED_FILES

%clean
%{__rm} --recursive --force %{buildroot}

%files -f INSTALLED_FILES
%defattr(-,root,root)
%doc README.md
%license LICENSE
