%define name smeserver-rspamd
%define version 11.0
%define release 2
Summary: SME Server Rspamd
Name: %{name}
Version: %{version}
Release: %{release}%{?dist}
Source: %{name}-%{version}.tar.gz
License: GNU GPL version 2
Group: SMEserver/addon
BuildRoot: %{_tmppath}/%{name}-buildroot
Prefix: %{_prefix}
BuildArchitectures: noarch
BuildRequires: smeserver-devtools
Requires: smeserver-release >= 11.0
Requires: smeserver-redis
Requires: rspamd >= 4.2.3
Requires: qpsmtpd >= 1.0.0-5   # needs backport from https://github.com/smtpd/qpsmtpd/pull/360

AutoReqProv: no

%description
SME Server templates for Rspamd support

%changelog
* Fri Oct 23 2026 Vasarhelyi Zsolt <zsoltv@koozali.org> 11.0-2.sme
- switch to qpsmtpd milter plugin tracked by [SME: 13649]

* Wed Nov 05 2025 Vasarhelyi Zsolt <zsoltv@koozali.org> 11.0-1.sme
- Initial release

%prep

%setup -q

%build
perl createlinks

%install
rm -rf $RPM_BUILD_ROOT
(cd root   ; find . -depth -print | cpio -dump $RPM_BUILD_ROOT)
rm -f %{name}-%{version}-filelist
/sbin/e-smith/genfilelist $RPM_BUILD_ROOT \
> %{name}-%{version}-filelist
#echo "%doc COPYING"  >> %{name}-%{version}-filelist
#--dir <dir> 'attr(755,user,grp)' \
#--file <file> 'attr(755,root,root)' \

%clean
cd ..
rm -rf %{name}-%{version}

%pre

%preun

%post

%postun
#uninstall
%files -f %{name}-%{version}-filelist
%defattr(-,root,root)
