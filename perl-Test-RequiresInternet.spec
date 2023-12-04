#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cpan
#
Name     : perl-Test-RequiresInternet
Version  : 0.05
Release  : 30
URL      : http://search.cpan.org/CPAN/authors/id/M/MA/MALLEN/Test-RequiresInternet-0.05.tar.gz
Source0  : http://search.cpan.org/CPAN/authors/id/M/MA/MALLEN/Test-RequiresInternet-0.05.tar.gz
Summary  : 'Easily test network connectivity'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-Test-RequiresInternet-license = %{version}-%{release}
Requires: perl-Test-RequiresInternet-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
NAME
Test::RequiresInternet - Easily test network connectivity
VERSION
version 0.05

%package dev
Summary: dev components for the perl-Test-RequiresInternet package.
Group: Development
Provides: perl-Test-RequiresInternet-devel = %{version}-%{release}
Requires: perl-Test-RequiresInternet = %{version}-%{release}

%description dev
dev components for the perl-Test-RequiresInternet package.


%package license
Summary: license components for the perl-Test-RequiresInternet package.
Group: Default

%description license
license components for the perl-Test-RequiresInternet package.


%package perl
Summary: perl components for the perl-Test-RequiresInternet package.
Group: Default
Requires: perl-Test-RequiresInternet = %{version}-%{release}

%description perl
perl components for the perl-Test-RequiresInternet package.


%prep
%setup -q -n Test-RequiresInternet-0.05
cd %{_builddir}/Test-RequiresInternet-0.05

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} -I. Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Test-RequiresInternet
cp %{_builddir}/Test-RequiresInternet-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/perl-Test-RequiresInternet/f93e41f283e6ffa249d7106244fbbe891f980cb6 || :
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

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Test::RequiresInternet.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Test-RequiresInternet/f93e41f283e6ffa249d7106244fbbe891f980cb6

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
