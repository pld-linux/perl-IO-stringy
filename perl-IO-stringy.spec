%include	/usr/lib/rpm/macros.perl
%define	pdir	IO
%define	pnam	stringy
Summary:	IO-stringy - I/O on in-core objects like strings and arrays
Name:		perl-IO-stringy
Version:	2.108
Release:	3
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This toolkit primarily provides modules for performing both traditional
and object-oriented i/o) on things I<other> than normal filehandles; in
particular, L<IO::Scalar|IO::Scalar>, L<IO::ScalarArray|IO::ScalarArray>,
and L<IO::Lines|IO::Lines>.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{perl_sitelib}/IO/*.pm
%{_mandir}/man3/*
