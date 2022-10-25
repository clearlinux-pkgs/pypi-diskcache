#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-diskcache
Version  : 5.4.0
Release  : 23
URL      : https://files.pythonhosted.org/packages/c7/34/d23a9bc5b2a84917879b977f00fdb97a7700b186a32bf7b0cf5f29f4c2d9/diskcache-5.4.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/c7/34/d23a9bc5b2a84917879b977f00fdb97a7700b186a32bf7b0cf5f29f4c2d9/diskcache-5.4.0.tar.gz
Summary  : Disk Cache -- Disk and file backed persistent cache.
Group    : Development/Tools
License  : Apache-2.0
Requires: pypi-diskcache-license = %{version}-%{release}
Requires: pypi-diskcache-python = %{version}-%{release}
Requires: pypi-diskcache-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
DiskCache: Disk Backed Cache
============================
`DiskCache`_ is an Apache2 licensed disk and file backed cache library, written
in pure-Python, and compatible with Django.

%package license
Summary: license components for the pypi-diskcache package.
Group: Default

%description license
license components for the pypi-diskcache package.


%package python
Summary: python components for the pypi-diskcache package.
Group: Default
Requires: pypi-diskcache-python3 = %{version}-%{release}

%description python
python components for the pypi-diskcache package.


%package python3
Summary: python3 components for the pypi-diskcache package.
Group: Default
Requires: python3-core
Provides: pypi(diskcache)

%description python3
python3 components for the pypi-diskcache package.


%prep
%setup -q -n diskcache-5.4.0
cd %{_builddir}/diskcache-5.4.0
pushd ..
cp -a diskcache-5.4.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1656407935
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-diskcache
cp %{_builddir}/diskcache-5.4.0/LICENSE %{buildroot}/usr/share/package-licenses/pypi-diskcache/19f288ce8d17f0eec41b2b296ede6208a3074183
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-diskcache/19f288ce8d17f0eec41b2b296ede6208a3074183

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
