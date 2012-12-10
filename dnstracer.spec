Summary:	A tool to trace dns queries
Name:		dnstracer
Version:	1.9
Release:	%mkrel 3
License:	BSD
Group:		Networking/Other
URL:		http://www.mavetju.org/unix/general.php
Source:		http://www.mavetju.org/download/%{name}-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-buildroot

%description
dnstracer determines where a given Domain Name Server (DNS) gets
its information from, and follows the chain of DNS servers back to
the servers which know the data.

%prep
%setup -q

%build
%configure2_5x
%make

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}
%makeinstall

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc CHANGES README
%{_bindir}/*
%{_mandir}/*/*




%changelog
* Sun Dec 05 2010 Oden Eriksson <oeriksson@mandriva.com> 1.9-3mdv2011.0
+ Revision: 610260
- rebuild

  + Sandro Cazzaniga <kharec@mandriva.org>
    - Clean spec file and fix rpmlint's warning

* Tue Jan 12 2010 Jérôme Brenier <incubusss@mandriva.org> 1.9-1mdv2010.1
+ Revision: 490026
- new version 1.9

* Thu Sep 03 2009 Thierry Vignaud <tv@mandriva.org> 1.8-6mdv2010.0
+ Revision: 428289
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 1.8-5mdv2009.0
+ Revision: 244442
- rebuild

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 1.8-3mdv2008.1
+ Revision: 136369
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Fri Dec 22 2006 Oden Eriksson <oeriksson@mandriva.com> 1.8-3mdv2007.0
+ Revision: 101671
- use the mkrel macro
- use the mrel macro
- Import dnstracer

* Sun Dec 25 2005 Oden Eriksson <oeriksson@mandriva.com> 1.8-2mdk
-rebuild

* Mon Nov 29 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 1.8-1mdk
- 1.8
- make it rpmbuildupdate aware

* Mon May 17 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 1.7-2mdk
- use macros

