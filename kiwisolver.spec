#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : kiwisolver
Version  : 1.1.0
Release  : 31
URL      : https://files.pythonhosted.org/packages/16/e7/df58eb8868d183223692d2a62529a594f6414964a3ae93548467b146a24d/kiwisolver-1.1.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/16/e7/df58eb8868d183223692d2a62529a594f6414964a3ae93548467b146a24d/kiwisolver-1.1.0.tar.gz
Summary  : A fast implementation of the Cassowary constraint solver
Group    : Development/Tools
License  : BSD-3-Clause
Requires: kiwisolver-python = %{version}-%{release}
Requires: kiwisolver-python3 = %{version}-%{release}
Requires: setuptools
BuildRequires : buildreq-distutils3
BuildRequires : setuptools

%description
===============

%package python
Summary: python components for the kiwisolver package.
Group: Default
Requires: kiwisolver-python3 = %{version}-%{release}

%description python
python components for the kiwisolver package.


%package python3
Summary: python3 components for the kiwisolver package.
Group: Default
Requires: python3-core
Provides: pypi(kiwisolver)

%description python3
python3 components for the kiwisolver package.


%prep
%setup -q -n kiwisolver-1.1.0
cd %{_builddir}/kiwisolver-1.1.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1603394584
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
