#
# Conditional build:
# _without_tests - do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	IO
%define	pnam	stringy
Summary:	IO-stringy - I/O on in-core objects like strings and arrays
Summary(pl):	IO-stringy - operacje I/O na obiektach takich jak ³añcuchy i tablice
Name:		perl-IO-stringy
Version:	2.108
Release:	5
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This toolkit primarily provides modules for performing both
traditional and object-oriented I/O on things other than normal
filehandles; in particular, IO::Scalar, IO::ScalarArray, and
IO::Lines.

%description -l pl
Ten zestaw narzêdzi dostarcza g³ównie modu³ów do wykonywania zarówno
tradycyjnych jak i obiektowo zorientowanych operacji wej¶cia/wyj¶cia
na rzeczach innych ni¿ normalne uchwyty plików, w szczególno¶ci:
IO::Scalar, IO::ScalarArray i IO::Lines.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make}

%{!?_without_tests:%{__make} test}

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
