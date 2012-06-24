#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Email
%define	pnam	IsFree
Summary:	Email::IsFree - detect whether e-mail is from free provider
Summary(pl):	Email::IsFree - sprawdzanie, czy poczta jest od darmowego providera
Name:		perl-Email-IsFree
Version:	0.02
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	8bc5f325901d81fc07d702ad73b834f0
BuildRequires:	perl-devel >= 5.6
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl(Test)
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module can be used to screen credit card orders based on e-mail.
Many credit card scamsters use free, anonymous email accounts with
another person's name to place fraudulent orders.

%description -l pl
Ten modu� mo�e by� u�ywany do filtrowania zam�wie� z u�yciem kart
kredytowych w oparciu o adres pocztowy. Wielu oszust�w do wysy�ania
oszuka�czych zam�wie� u�ywa darmowych, anonimowych kont pocztowych z
nazwiskiem innej osoby.

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
%doc README Changes
%{perl_vendorlib}/%{pdir}/*.pm
%{_mandir}/man3/*
