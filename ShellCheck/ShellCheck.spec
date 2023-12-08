Name:       ShellCheck
Version:    0.7.1
Release:    1%{dist}
Summary:    Shell script analysis tool.
BuildArch:  x86_64
License:    GPL-3.0
URL:        https://github.com/koalaman/shellcheck
Source0:    https://github.com/koalaman/shellcheck/releases/download/v%{version}/shellcheck-v%{version}.linux.x86_64.tar.xz

%description
ShellCheck is an open source static analysis tool that automatically finds bugs in your shell scripts.

%prep
%setup -q -n shellcheck-v%{version}

%install
install -m 0755 -d $RPM_BUILD_ROOT/usr/bin
install -m 0755 %{_builddir}/shellcheck-v%{version}/shellcheck $RPM_BUILD_ROOT/usr/bin

%files
%license LICENSE.txt
%doc README.txt
/usr/bin/shellcheck
