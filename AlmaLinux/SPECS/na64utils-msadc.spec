%global debug_package %{nil}
%undefine _disable_source_fetch

%global _pver 2.15.1
%global _tagver e6c8ff61dd21d8ae2570dc6ff6fbfa6bfd3290e7

%global _sbuilddir %{_builddir}/%{name}-%{version}/na64utils-msadc-%{_tagver}
%global _cbuilddir %{_builddir}/%{name}-%{version}/build

Summary: Common numerical and reconstruction routines for NA64
Name: na64utils-msadc
Version: %{_pver}
Release: 1.na64%{?dist}
License: GPL v.3
Vendor: CERN
URL: https://gitlab.cern.ch/P348/na64utils-msadc
Group: Development/Libraries
BuildArch: %{_arch}
BuildRequires: cmake
BuildRequires: make
BuildRequires: gsl-devel
BuildRequires: zlib-devel
BuildRequires: json-devel
BuildRequires: yaml-cpp-devel
BuildRequires: root
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
AutoReqProv: yes
Source0: https://gitlab.cern.ch/P348/na64utils-msadc/-/archive/%{_tagver}/na64utils-msadc-%{_tagver}.zip
Patch0: na64utils-msadc_cmake.patch

%description
Common numerical and reconstruction routines for sampling ADC of NA64

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
      %{_sbuilddir}
make %{?_smp_mflags}

%install
cd %{_cbuilddir}
make install
mv %{buildroot}%{_prefix}/lib %{buildroot}%{_libdir}

%clean
rm -rf %{buildroot}
rm -f %{SOURCE0}

%files
%defattr(-,root,root)
%{_libdir}/*.so.*
%{_bindir}/*
%dir %{_datadir}/na64
%dir %{_datadir}/na64/libna64utils
%{_datadir}/na64/libna64utils/*.json
%dir %{_datadir}/na64/libna64utils/fit-procs
%{_datadir}/na64/libna64utils/fit-procs/*.json
%dir %{_datadir}/na64/libna64utils/wf-reco
%{_datadir}/na64/libna64utils/wf-reco/*.json

%package devel
Summary: Common numerical and reconstruction routines for NA64 (development files)
Requires: %{name}
Requires: gsl-devel
Requires: zlib-devel
Requires: json-devel
Requires: yaml-cpp-devel
Requires: root

%description devel
Common numerical and reconstruction routines for NA64 (development files).

%files devel
%defattr(-,root,root)
%{_libdir}/*.so
%dir %{_includedir}/na64
%{_includedir}/na64/*.hh
%{_includedir}/na64/*.h
%dir %{_includedir}/na64/baselines/
%{_includedir}/na64/baselines/*.h
%dir %{_includedir}/na64/ecal-calib/
%{_includedir}/na64/ecal-calib/*.h
%dir %{_includedir}/na64/moyal/
%{_includedir}/na64/moyal/*.h
%{_includedir}/na64/moyal/*.hh
%dir %{_includedir}/na64/npole/
%{_includedir}/na64/npole/*.h
%{_includedir}/na64/npole/*.hh
%dir %{_includedir}/na64/sys-util/
%{_includedir}/na64/sys-util/*.hh
%dir %{_includedir}/na64/user-api/
%{_includedir}/na64/user-api/*.h
%{_includedir}/na64/user-api/*.hh
%dir %{_includedir}/na64/wf-templates/
%{_includedir}/na64/wf-templates/*.h
%{_includedir}/na64/wf-templates/*.hh
%dir %{_includedir}/umff/
%{_includedir}/umff/*.h
%{_includedir}/umff/*.hh
%dir %{_includedir}/umff/algo
%{_includedir}/umff/algo/*.hh
%dir %{_includedir}/umff/fitters
%{_includedir}/umff/fitters/*.hh
%dir %{_includedir}/umff/numeric
%{_includedir}/umff/numeric/*.h
%{_includedir}/umff/numeric/*.hh


%changelog
* Mon Jan 19 2026 Paolo Andreetto <paolo.andreetto@pd.infn.it> - 2.15.1-1
- First release for AlmaLinux

