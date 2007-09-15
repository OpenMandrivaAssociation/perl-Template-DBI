%define module  Template-DBI
%define name	perl-%{module}
%define	modprefix Template

%define version 2.64

%define	rel	2
%define release %mkrel %{rel}

Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
Summary: 	Template interface to the DBI module
License:	Artistic/GPL
Group:		Development/Perl
Source:		http://www.cpan.org/modules/by-module/%{modprefix}/%{module}-%{version}.tar.bz2
URL:		http://www.template-toolkit.org
%if %{mdkversion} < 1010
Buildrequires:	perl-devel
%endif
BuildRequires:	perl(DBI) >= 1.0
BuildRequires:	perl(Template) >= 2.15
Requires:	perl-Template >= 2.15
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
The Template-DBI distribution contains the DBI plugin for the Template
Toolkit. At some point in the future it is likely to contain other
DBI-related plugins and extension modules for the Template Toolkit.

The DBI plugin was distributed as part of the Template Toolkit until
version 2.15 released in May 2006. At this time it was extracted into
this separate Template-DBI distribution.


%prep
%setup -q -n %{module}-%{version}

%{__perl} Makefile.PL INSTALLDIRS=vendor <<EOF
EOF
%make

##%check
##%__make test

%install
rm -rf %{buildroot}
%{makeinstall_std}

%clean
rm -rf %{buildroot}

%files
%defattr(644,root,root,755)
%doc README
%{perl_vendorlib}/%{modprefix}
%{_mandir}/*/*

