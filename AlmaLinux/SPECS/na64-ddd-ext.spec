%global debug_package %{nil}
%undefine _disable_source_fetch

%global _pver 1.1.1
%global _tagver 52273c323ec237b8b028f1a93265912315f411b9

%global _sbuilddir %{_builddir}/%{name}-%{version}/ddd-ext-%{_tagver}
%global _cbuilddir %{_builddir}/%{name}-%{version}/build

Summary: Extensions of basic DDD API
Name: na64-ddd-ext
Version: %{_pver}
Release: 1.na64%{?dist}
License: GPL v.3
Vendor: CERN
URL: https://gitlab.cern.ch/na64-packaging/catsc
Group: Development/Libraries
BuildArch: %{_arch}
BuildRequires: cmake
BuildRequires: make
BuildRequires: chrpath
BuildRequires: na64-coral-daq-devel
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
AutoReqProv: yes
Source0: https://gitlab.cern.ch/na64-packaging/ddd-ext/-/archive/%{_tagver}/ddd-ext-%{_tagver}.tar.gz
Patch0: na64-ddd-ext_CMakeLists.patch
Patch1: na64-ddd-ext_findDDD.patch

%description
This project provides few useful extensions of basic DDD API facilitating data
chunk file indexing, random access to events, etc.

%prep
%setup -c
rm -rf %{buildroot}
mkdir -p %{buildroot}
patch %{_sbuilddir}/CMakeLists.txt %{PATCH0}
patch %{_sbuilddir}/cmake/FindDDD.cmake %{PATCH1}

%build
mkdir %{_cbuilddir}
cd %{_cbuilddir}
cmake -DCMAKE_INSTALL_PREFIX=%{buildroot}%{_prefix} \
      -DCMAKE_BUILD_TYPE=RelWithDebInfo \
      -DCMAKE_CXX_STANDARD=17 \
      -DNA64_DATE_PREFIX=/usr \
      -Wno-dev \
      %{_sbuilddir}
make %{?_smp_mflags}

%install
cd %{_cbuilddir}
make install

chrpath --delete %{buildroot}%{_libdir}/*.so %{buildroot}%{_bindir}/ddd-*

%clean
rm -rf %{buildroot}
rm -f %{SOURCE0}

%files
%defattr(-,root,root)
%{_libdir}/*.so.*
%{_bindir}/ddd-*

%package devel
Summary: Extensions of basic DDD API (development files)
Requires: %{name}
Requires: na64-coral-daq-devel

%description devel
This project provides few useful extensions of basic DDD API facilitating data
chunk file indexing, random access to events, etc.

%files devel
%defattr(-,root,root)
%{_libdir}/*.so
%dir %{_includedir}/na64/ddd-ext
%{_includedir}/na64/ddd-ext/*.hh

%changelog
* Wed Apr 29 2026 Paolo Andreetto <paolo.andreetto@pd.infn.it> - 1.1.1-1
- First release for AlmaLinux






