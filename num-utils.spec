%include	/usr/lib/rpm/macros.perl
Summary:	Set of programs for dealing with numbers
Summary(pl):	Zestaw programów do operowania na liczbach
Name:		num-utils
Version:	0.5
Release:	1
License:	GPL
Group:		Applications/Text
Source0:	http://suso.suso.org/programs/num-utils/downloads/%{name}-%{version}.tar.gz
# Source0-md5:	58eed69761c2da97c3bfdfa422633427
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The num-utils, short for numeric utilities are a set of programs
designed to work together from the unix shell to do numeric operations
on input. They are basically the numeric equivilent of common unix
text utilities and aim to help complete the unix shell vocabulary.

%description -l pl
num-utils to zestaw programów przeznaczonych do pracy z poziomu
pow³oki uniksowej nad operacjami numerycznymi na wej¶ciu. S± one
odpowiednikiem powszechnych narzêdzi tekstowych z Uniksa i pomagaj±
uzupe³niæ s³ownik uniksowej pow³oki.

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
