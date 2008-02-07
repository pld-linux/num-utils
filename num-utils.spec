%include	/usr/lib/rpm/macros.perl
Summary:	Set of programs for dealing with numbers
Summary(pl.UTF-8):	Zestaw programów do operowania na liczbach
Name:		num-utils
Version:	0.5
Release:	1
License:	GPL
Group:		Applications/Text
Source0:	http://suso.suso.org/programs/num-utils/downloads/%{name}-%{version}.tar.gz
# Source0-md5:	58eed69761c2da97c3bfdfa422633427
BuildRequires:	rpm-perlprov
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The num-utils, short for numeric utilities are a set of programs
designed to work together from the Unix shell to do numeric operations
on input. They are basically the numeric equivilent of common Unix
text utilities and aim to help complete the Unix shell vocabulary.

%description -l pl.UTF-8
num-utils to zestaw programów przeznaczonych do pracy z poziomu
powłoki uniksowej nad operacjami numerycznymi na wejściu. Są one
odpowiednikiem powszechnych narzędzi tekstowych z Uniksa i pomagają
uzupełnić słownik uniksowej powłoki.

%prep
%setup -q

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} rpminstall \
	ROOT=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%doc CHANGELOG GOALS README WARNING template tests/
%{_mandir}/man?/*
