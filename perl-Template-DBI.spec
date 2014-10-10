%define upstream_name    Template-DBI
%define upstream_version 2.65

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Template interface to the DBI module
License:	Artistic/GPL
Group:		Development/Perl
URL:		http://www.template-toolkit.org
Source0:	http://www.cpan.org/modules/by-module/Template/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(DBI) >= 1.0
BuildRequires:	perl(Template) >= 2.15

BuildArch:	noarch
Requires:	perl(Template) >= 2.15

%description
The Template-DBI distribution contains the DBI plugin for the Template
Toolkit. At some point in the future it is likely to contain other
DBI-related plugins and extension modules for the Template Toolkit.

The DBI plugin was distributed as part of the Template Toolkit until
version 2.15 released in May 2006. At this time it was extracted into
this separate Template-DBI distribution.


%prep
%setup -q -n %{upstream_name}-%{upstream_version}

perl Makefile.PL INSTALLDIRS=vendor <<EOF
EOF
%make

%check
##make test

%install
%makeinstall_std

%files
%defattr(644,root,root,755)
%doc README
%{perl_vendorlib}/Template
%{_mandir}/*/*


%changelog
* Sun Aug 15 2010 Jérôme Quelin <jquelin@mandriva.org> 2.650.0-1mdv2011.0
+ Revision: 569957
- update to 2.65

* Tue Jul 13 2010 Jérôme Quelin <jquelin@mandriva.org> 2.640.0-2mdv2011.0
+ Revision: 552005
- rebuild

* Fri Jul 10 2009 Jérôme Quelin <jquelin@mandriva.org> 2.640.0-1mdv2010.0
+ Revision: 394271
- fixed a require on package name, instead of metadata perl(...) that
  prevented perl-Template-Toolkit to be upgraded
- using %%perl_convert_version

* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 2.64-2mdv2009.0
+ Revision: 140717
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sat Sep 15 2007 Guillaume Rousse <guillomovitch@mandriva.org> 2.64-2mdv2008.0
+ Revision: 86929
- rebuild


* Fri May 26 2006 Scott Karns <scottk@mandriva.org> 2.64-1mdv2007.0
- Initial Mandriva package (was part of perl-Template < 2.15)

