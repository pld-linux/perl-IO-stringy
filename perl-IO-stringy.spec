#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%define		pdir	IO
%define		pnam	stringy
Summary:	IO-stringy - I/O on in-core objects like strings and arrays
Summary(pl.UTF-8):	IO-stringy - operacje I/O na obiektach takich jak łańcuchy i tablice
Name:		perl-IO-stringy
Version:	2.111
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/IO/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	e91acf0a800b190d13585a47de775bdd
URL:		https://metacpan.org/release/IO-stringy
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This toolkit primarily provides modules for performing both
traditional and object-oriented I/O on things other than normal
filehandles; in particular, IO::Scalar, IO::ScalarArray, and
IO::Lines.

%description -l pl.UTF-8
Ten zestaw narzędzi dostarcza głównie modułów do wykonywania zarówno
tradycyjnych jak i obiektowo zorientowanych operacji wejścia/wyjścia
na rzeczach innych niż normalne uchwyty plików, w szczególności:
IO::Scalar, IO::ScalarArray i IO::Lines.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING README
%{perl_vendorlib}/IO/AtomicFile.pm
%{perl_vendorlib}/IO/InnerFile.pm
%{perl_vendorlib}/IO/Lines.pm
%{perl_vendorlib}/IO/Scalar.pm
%{perl_vendorlib}/IO/ScalarArray.pm
%{perl_vendorlib}/IO/Stringy.pm
%{perl_vendorlib}/IO/Wrap.pm
%{perl_vendorlib}/IO/WrapTie.pm
%{_mandir}/man3/IO::AtomicFile.3pm*
%{_mandir}/man3/IO::InnerFile.3pm*
%{_mandir}/man3/IO::Lines.3pm*
%{_mandir}/man3/IO::Scalar.3pm*
%{_mandir}/man3/IO::ScalarArray.3pm*
%{_mandir}/man3/IO::Stringy.3pm*
%{_mandir}/man3/IO::Wrap.3pm*
%{_mandir}/man3/IO::WrapTie.3pm*
