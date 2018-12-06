#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Test-RequiresInternet
Version  : 0.05
Release  : 10
URL      : http://search.cpan.org/CPAN/authors/id/M/MA/MALLEN/Test-RequiresInternet-0.05.tar.gz
Source0  : http://search.cpan.org/CPAN/authors/id/M/MA/MALLEN/Test-RequiresInternet-0.05.tar.gz
Summary  : 'Easily test network connectivity'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-Test-RequiresInternet-license = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
NAME
Test::RequiresInternet - Easily test network connectivity
VERSION
version 0.05

%package dev
Summary: dev components for the perl-Test-RequiresInternet package.
Group: Development
Provides: perl-Test-RequiresInternet-devel = %{version}-%{release}

%description dev
dev components for the perl-Test-RequiresInternet package.


%package license
Summary: license components for the perl-Test-RequiresInternet package.
Group: Default

%description license
license components for the perl-Test-RequiresInternet package.


%prep
%setup -q -n Test-RequiresInternet-0.05

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Test-RequiresInternet
cp LICENSE %{buildroot}/usr/share/package-licenses/perl-Test-RequiresInternet/LICENSE
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.28.1/Test/RequiresInternet.pm

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Test::RequiresInternet.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Test-RequiresInternet/LICENSE
