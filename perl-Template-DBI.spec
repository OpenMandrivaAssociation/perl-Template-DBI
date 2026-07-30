%define upstream_name    Template-DBI
%define upstream_version 2.65
Name:		perl-%{upstream_name}
Version:	2.65
Release:	1

Summary:	Template interface to the DBI module
License:	Artistic/GPL
Group:		Development/Perl
URL:		https://www.template-toolkit.org
Source0:	https://cpan.metacpan.org/authors/id/R/RE/REHSACK/Template-DBI-2.65.tar.gz

BuildRequires:	make
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
%setup -q -n %{upstream_name}-%{version}

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


