%define upstream_name    Template-DBI
%define upstream_version 2.65

Name: 		perl-%{upstream_name}
Version: 	%perl_convert_version %{upstream_version}
Release: 	%mkrel 1

Summary: 	Template interface to the DBI module
License:	Artistic/GPL
Group:		Development/Perl
URL:		http://www.template-toolkit.org
Source0:	http://www.cpan.org/modules/by-module/Template/%{upstream_name}-%{upstream_version}.tar.gz

%if %{mdkversion} < 1010
Buildrequires:	perl-devel
%endif
BuildRequires:	perl(DBI) >= 1.0
BuildRequires:	perl(Template) >= 2.15
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}
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
%{perl_vendorlib}/Template
%{_mandir}/*/*
