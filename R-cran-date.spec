%define		fversion	%(echo %{version} |tr r -)
%define		modulename	date
Summary:	Functions for handling dates
Summary(pl):	Funkcje do obs³ugi dat
Name:		R-cran-%{modulename}
Version:	1.2r18
Release:	1
License:	GPL
Group:		Applications/Math
Source0:	ftp://stat.ethz.ch/R-CRAN/src/contrib/%{modulename}_%{fversion}.tar.gz
# Source0-md5:	8bb9d6bc5cb0b06e250be6f478cf4c2a
BuildRequires:	R-base >= 2.0.0
Requires(post,postun):	R-base >= 2.0.0
Requires(post,postun):	perl-base
Requires(post,postun):	textutils
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Functions for handling dates.

%description -l pl
Funkcje do obs³ugi dat.

%prep
%setup -q -c

%build
R CMD build %{modulename}

%install
rm -rf $RPM_BUILD_ROOT
R CMD INSTALL %{modulename} --library=$RPM_BUILD_ROOT%{_libdir}/R/library/

%clean
rm -rf $RPM_BUILD_ROOT

%post
(cd %{_libdir}/R/library; umask 022; cat */CONTENTS > ../doc/html/search/index.txt
 R_HOME=%{_libdir}/R ../bin/Rcmd perl ../share/perl/build-help.pl --htmllist)

%postun
if [ -f %{_libdir}/R/bin/Rcmd ];then
	(cd %{_libdir}/R/library; umask 022; cat */CONTENTS > ../doc/html/search/index.txt
	R_HOME=%{_libdir}/R ../bin/Rcmd perl ../share/perl/build-help.pl --htmllist)
fi

%files
%defattr(644,root,root,755)
%doc %{modulename}/DESCRIPTION %{modulename}/ChangeLog
%{_libdir}/R/library/%{modulename}
