%define __jar_repack 0
%define debug_package %{nil}
%define name         jnetpcap
%define _prefix      /opt/local/lib
%define _conf_dir    %{_sysconfdir}/jnetpcap
%define _log_dir     %{_var}/log/jnetpcap

Summary: jNetPcap is an open-source java library.

Name: jnetpcap
Version: %{version}
Release: %{build_number}
License: Apache License, Version 2.0
Group: Applications/Databases
URL: http://sourceforge.net/projects/jnetpcap/files/jnetpcap/1.3/jnetpcap-1.3.0-1.fc.x86_64.tgz
Source: http://sourceforge.net/projects/jnetpcap/files/jnetpcap/1.3/jnetpcap-1.3.0-1.fc.x86_64.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Prefix: %{_prefix}
Vendor: Apache Software Foundation
Packager: zard <we_zard@163.com>
Provides: jnetpcap

%description
jNetPcap is an open-source java library.

%prep

%setup

%build

%install

mkdir -p $RPM_BUILD_ROOT%{_prefix}/jnetpcap
cp -r $RPM_BUILD_DIR/jnetpcap-1.3.0 $RPM_BUILD_ROOT%{_prefix}/
rm -rf $RPM_BUILD_ROOT%{_prefix}/jnetpcap

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root)
%{_prefix}

%changelog
* Sat Aug 8 2015 zard <we_zard@163.com> - 1.3.0
- initial release
