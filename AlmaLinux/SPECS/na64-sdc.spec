%global debug_package %{nil}
%undefine _disable_source_fetch

%global _pver 0.5.0
%global _tagver v0.5

%global _sbuilddir %{_builddir}/%{name}-%{version}/sdc-%{_tagver}
%global _cbuilddir %{_builddir}/%{name}-%{version}/build

%global cmake_sdc_dir %{_libdir}/cmake/sdc

Summary: Calibration data based on a file structure
Name: na64-sdc
Version: %{_pver}
Release: 1.na64%{?dist}
License: LGPL 2.1
Vendor: CERN
URL: https://gitlab.cern.ch/na64-packaging/sdc
Group: Development/Libraries
BuildArch: %{_arch}
BuildRequires: cmake
BuildRequires: make
BuildRequires: chrpath
BuildRequires: root
BuildRequires: root-mathcore
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
AutoReqProv: yes
Source0: https://gitlab.cern.ch/na64-packaging/sdc/-/archive/%{_tagver}/sdc-%{_tagver}.tar.gz
Patch0: na64-sdc_cmake.patch

%description
Calibration data based on a file structure

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
      -Wno-dev \
      %{_sbuilddir}
make %{?_smp_mflags}

%install
cd %{_cbuilddir}
make install

mv %{buildroot}%{_prefix}/lib/cmake %{buildroot}%{_libdir}
rm -rf %{buildroot}%{_prefix}/lib


%clean
rm -rf %{buildroot}
rm -f %{SOURCE0}

%files
%defattr(-,root,root)
%{_libdir}/*.so.*

%package devel
Summary: Calibration data based on a file structure (development files)
Requires: %{name}
Requires: root
Requires: root-mathcore

%description devel
Calibration data based on a file structure (development files).

%files devel
%defattr(-,root,root)
%{_libdir}/*.so
%{_includedir}/*.h
%{_includedir}/*.hh
%{cmake_sdc_dir}/*.cmake

%changelog
* Fri Oct 17 2025 Paolo Andreetto <paolo.andreetto@pd.infn.it> - 0.5.0-1
- First release for AlmaLinux

