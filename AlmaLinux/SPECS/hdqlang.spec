%global debug_package %{nil}
%undefine _disable_source_fetch

%global _pver 0.2.1
%global _tagver 6a003d8e337ee7b961f2fae56c214a55b1b8942c

%global _sbuilddir %{_builddir}/%{name}-%{version}/hdql-%{_tagver}
%global _cbuilddir %{_builddir}/%{name}-%{version}/build

Summary: Hierarchical data query language
Name: hdqlang
Version: %{_pver}
Release: 1.na64%{?dist}
License: GPL v.3
Vendor: CERN
URL: https://github.com/CrankOne/hdql
Group: Development/Libraries
BuildArch: %{_arch}
BuildRequires: cmake
BuildRequires: make
BuildRequires: chrpath
BuildRequires: bison
BuildRequires: flex
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
AutoReqProv: yes
Source0: https://github.com/CrankOne/hdql/archive/%{_tagver}.zip
Source1: hdqlang_hdqlConfig.cmake
Patch0: hdqlang_CMakeLists.patch

%description
HDQLang is domain-specific language designed to be embeddable and reasonably
performant add-on to C/C++ projects dealing with streamed data of complex object model

%prep
%setup -c
rm -rf %{buildroot}
mkdir -p %{buildroot}
patch %{_sbuilddir}/CMakeLists.txt %{PATCH0}

%build
mkdir %{_cbuilddir}
cd %{_cbuilddir}
cmake -DCMAKE_INSTALL_PREFIX=%{buildroot}%{_prefix} \
      -DCMAKE_BUILD_TYPE=RelWithDebInfo \
      -DCMAKE_CXX_STANDARD=17 \
      -DCMAKE_INSTALL_LIBDIR=%{buildroot}%{_libdir} \
      -DBUILD_TESTS=OFF -DCOVERAGE=OFF \
      -Wno-dev \
      %{_sbuilddir}
make %{?_smp_mflags}

%install
cd %{_cbuilddir}
make install
chrpath --delete %{buildroot}%{_libdir}/*.so.*
cp %{SOURCE1} %{buildroot}%{_libdir}/cmake/hdql/hdqlConfig.cmake

%clean
rm -rf %{buildroot}
rm -f %{SOURCE0}

%files
%defattr(-,root,root)
%{_libdir}/*.so.*

%package devel
Summary: Hierarchical data query language (development files)
Requires: %{name}

%description devel
Hierarchical data query language (development files).

%files devel
%defattr(-,root,root)
%dir %{_includedir}/hdql
%dir %{_includedir}/hdql/helpers
%{_includedir}/hdql/*.h
%{_includedir}/hdql/helpers/*.h
%{_includedir}/hdql/helpers/*.hh
%{_libdir}/*.so
%dir %{_libdir}/cmake/hdql
%{_libdir}/cmake/hdql/*.cmake


%changelog
* Mon Mar 23 2026 Paolo Andreetto <paolo.andreetto@pd.infn.it> - 0.2.1-1
- First release for AlmaLinux

