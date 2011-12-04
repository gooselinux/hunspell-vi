Name: hunspell-vi
Summary: Vietnamese hunspell dictionaries
%define upstreamid 20080604
Version: 0.%{upstreamid}
Release: 3.1%{?dist}
Source: http://hunspell-spellcheck-vi.googlecode.com/files/vi_VN.zip
Group: Applications/Text
URL: http://code.google.com/p/hunspell-spellcheck-vi
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
License: GPL+
BuildArch: noarch

Requires: hunspell

%description
Vietnamese hunspell dictionaries.

%prep
%setup -q -c -n hunspell-vi

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/myspell
cp -p *.dic *.aff $RPM_BUILD_ROOT/%{_datadir}/myspell

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc README_vi_VN.txt Copyright
%{_datadir}/myspell/*

%changelog
* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 0.20080604-3.1
- Rebuilt for RHEL 6

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20080604-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20080604-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Sep 18 2006 Caolan McNamara <caolanm@redhat.com> - 0.20080604-1
- initial version
