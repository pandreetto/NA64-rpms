%global debug_package %{nil}
%undefine _disable_source_fetch

%global _pver 2.20.0
%global _tagver v2.20

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
BuildRequires: chrpath
BuildRequires: gsl-devel
BuildRequires: zlib-devel
BuildRequires: json-devel
BuildRequires: yaml-cpp-devel
BuildRequires: root
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
AutoReqProv: yes
Source0: https://gitlab.cern.ch/P348/na64utils-msadc/-/archive/%{_tagver}/na64utils-msadc-%{_tagver}.tar.gz
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

chrpath --delete %{buildroot}%{_bindir}/na64util-fit-waveforms %{buildroot}%{_libdir}/*.so

sed -i -e 's|%{buildroot}/usr|%{_prefix}|g' %{buildroot}%{_includedir}/na64/libna64utils-config.h

mkdir -p %{buildroot}%{_sysconfdir}/profile.d
printf "export LIBNA64UTILS_BASE_CONFIG_PATH=%{_datadir}/na64/libna64utils" \
       | tee %{buildroot}%{_sysconfdir}/profile.d/na64utils-msadc.sh
printf "setenv LIBNA64UTILS_BASE_CONFIG_PATH %{_datadir}/na64/libna64utils" \
       | tee %{buildroot}%{_sysconfdir}/profile.d/na64utils-msadc.csh

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
%{_sysconfdir}/profile.d/na64utils-msadc.*

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
%dir %{_includedir}/na64/sys-util/
%{_includedir}/na64/sys-util/*.hh
%dir %{_includedir}/na64/user-api/
%{_includedir}/na64/user-api/*.h
%{_includedir}/na64/user-api/*.hh
%dir %{_includedir}/na64/wf-fit
%{_includedir}/na64/wf-fit/*.hh
%{_includedir}/na64/wf-fit/*.h
%dir %{_includedir}/na64/wf-fit/moyal
%{_includedir}/na64/wf-fit/moyal/*.h
%{_includedir}/na64/wf-fit/moyal/*.hh
%dir %{_includedir}/na64/wf-fit/npole
%{_includedir}/na64/wf-fit/npole/*.h
%{_includedir}/na64/wf-fit/npole/*.hh
%dir %{_includedir}/na64/wf-fit/wf-templates
%{_includedir}/na64/wf-fit/wf-templates/*.h
%{_includedir}/na64/wf-fit/wf-templates/*.hh
%dir %{_includedir}/umff/
%{_includedir}/umff/*.h
%{_includedir}/umff/*.hh
%dir %{_includedir}/umff/algo
%{_includedir}/umff/algo/*.hh
%dir %{_includedir}/umff/fitters
%{_includedir}/umff/fitters/*.hh
%dir %{_includedir}/umff/fitters/gsl-workspaces
%{_includedir}/umff/fitters/gsl-workspaces/*.hh
%dir %{_includedir}/umff/model
%{_includedir}/umff/model/*.hh
%dir %{_includedir}/umff/model/multimodel
%{_includedir}/umff/model/multimodel/*.hh
%dir %{_includedir}/umff/model/parametric
%{_includedir}/umff/model/parametric/*.hh
%dir %{_includedir}/umff/model/parametric-multimodel-in-domain
%{_includedir}/umff/model/parametric-multimodel-in-domain/*.hh
%dir %{_includedir}/umff/model/parametric-multimodel
%{_includedir}/umff/model/parametric-multimodel/*.hh
%dir %{_includedir}/umff/numeric
%{_includedir}/umff/numeric/*.h
%{_includedir}/umff/numeric/*.hh



%changelog
* Tue Apr 28 2026 Paolo Andreetto <paolo.andreetto@pd.infn.it> - 2.20.0-1
- First release for AlmaLinux

