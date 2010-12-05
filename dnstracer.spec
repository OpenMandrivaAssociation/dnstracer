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


