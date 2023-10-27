%undefine           _disable_source_fetch

Name:               prometheus
Version:            2.45.1
Release:            1%{?dist}
Summary:            The Prometheus monitoring system and time series database.

License:            Apache-2.0
URL:                https://prometheus.io/
Source0:            https://github.com/prometheus/prometheus/releases/download/v%{version}/prometheus-%{version}.linux-amd64.tar.gz
Source1:            prometheus.service

BuildArch:          x86_64

%description
Prometheus, a Cloud Native Computing Foundation project, is a systems and service monitoring system.
It collects metrics from configured targets at given intervals, evaluates rule expressions,
displays the results, and can trigger alerts when specified conditions are observed.

The features that distinguish Prometheus from other metrics and monitoring systems are:
  . A multi-dimensional data model (time series defined by metric name and set of key/value dimensions)
  . PromQL, a powerful and flexible query language to leverage this dimensionality
  . No dependency on distributed storage; single server nodes are autonomous
  . An HTTP pull model for time series collection
  . Pushing time series is supported via an intermediary gateway for batch jobs
  . Targets are discovered via service discovery or static configuration
  . Multiple modes of graphing and dashboarding support
  . Support for hierarchical and horizontal federation

%prep
%setup -n prometheus-%{version}.linux-amd64

%install
%{__install} -D --mode=0644 --directory %{buildroot}/etc/prometheus/consoles
%{__install} -D --mode=0644 --directory %{buildroot}/etc/prometheus/console_libraries
%{__install} -D --mode=0644 --directory %{buildroot}/usr/bin
%{__install} -D --mode=0644 --directory %{buildroot}/var/lib/prometheus
%{__install} -D --mode=0644 --directory %{buildroot}%{_unitdir}/
%{__install} -D --preserve-timestamps --mode=0644 %{_builddir}/prometheus-%{version}.linux-amd64/prometheus.yml %{buildroot}/etc/prometheus/
%{__install} -D --preserve-timestamps --mode=0644 %{_builddir}/prometheus-%{version}.linux-amd64/consoles/* %{buildroot}/etc/prometheus/consoles/
%{__install} -D --preserve-timestamps --mode=0644 %{_builddir}/prometheus-%{version}.linux-amd64/console_libraries/* %{buildroot}/etc/prometheus/console_libraries/
%{__install} -D --preserve-timestamps --mode=0644 %{_builddir}/prometheus-%{version}.linux-amd64/prometheus %{buildroot}/usr/bin/
%{__install} -D --preserve-timestamps --mode=0644 %{_builddir}/prometheus-%{version}.linux-amd64/promtool %{buildroot}/usr/bin/
%{__install} -D --preserve-timestamps --mode=0644 %{SOURCE1} %{buildroot}%{_unitdir}/

%clean
%{__rm} --recursive --force %{buildroot} %{_builddir}

%pretrans
if ! id prometheus >/dev/null 2>&1
then
    adduser --no-create-home --system --shell /sbin/nologin prometheus
fi

%post
if systemctl >/dev/null 2>&1
then
    systemctl daemon-reload
fi

%postun
if systemctl >/dev/null 2>&1
then
    systemctl daemon-reload
fi

%files
%defattr(0644,prometheus,prometheus,0644)
%license LICENSE
%attr(0644,root,root) /usr/lib/systemd/system/prometheus.service
%attr(0755,root,root) /usr/bin/prometheus
%attr(0755,root,root) /usr/bin/promtool
/etc/prometheus/console_libraries/menu.lib
/etc/prometheus/console_libraries/prom.lib
/etc/prometheus/consoles/index.html.example
/etc/prometheus/consoles/node-cpu.html
/etc/prometheus/consoles/node-disk.html
/etc/prometheus/consoles/node-overview.html
/etc/prometheus/consoles/node.html
/etc/prometheus/consoles/prometheus-overview.html
/etc/prometheus/consoles/prometheus.html
/etc/prometheus/prometheus.yml
