%global debug_package %{nil}
%undefine _disable_source_fetch

%global _pver 0.6.1
%global _tagver fed4d2cc8b97de09a65584920507c4d5b832c66c

%global _sbuilddir %{_builddir}/%{name}-%{version}/na64sw-%{_tagver}
%global _cbuilddir %{_builddir}/%{name}-%{version}/build

Summary: Framework for analysis and reconstruction of NA64 experimental data
Name: na64-sw
Version: %{_pver}
Release: 1.na64%{?dist}
License: GPL v.3
Vendor: CERN
URL: https://gitlab.cern.ch/P348/na64sw
Group: Development/Libraries
BuildArch: %{_arch}
BuildRequires: cmake
BuildRequires: make
BuildRequires: chrpath
BuildRequires: crankone-hdql-devel
BuildRequires: crankone-catsc-devel
BuildRequires: crankone-sdc-devel
BuildRequires: na64utils-msadc-devel
BuildRequires: genfit-devel
BuildRequires: na64-coral-daq-devel
BuildRequires: log4cpp-devel
BuildRequires: avro-c-devel
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
AutoReqProv: yes
Source0: https://gitlab.cern.ch/P348/na64sw/-/archive/%{_tagver}/na64sw-%{_tagver}.zip
Source1: na64-sw_setup.sh
Source2: na64-sw_setup.csh
Patch0: na64-sw_CMakeLists.patch

%description
Framework for analysis and reconstruction of NA64 experimental data

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
      -DCORAL_DAQ_MAPS_DIR=/usr/share/CoralDAQ \
      %{_sbuilddir}
make %{?_smp_mflags}

%install
cd %{_cbuilddir}
make install
mv %{buildroot}%{_prefix}/lib %{buildroot}%{_libdir}
mv %{buildroot}%{_prefix}/etc %{buildroot}

mkdir -p %{buildroot}%{_sysconfdir}/profile.d
cp %{SOURCE1} %{buildroot}%{_sysconfdir}/profile.d/na64sw-setup.sh
cp %{SOURCE2} %{buildroot}%{_sysconfdir}/profile.d/na64sw-setup.csh

rm -rf %{buildroot}/%{_datadir}/na64sw/run

chrpath --delete %{buildroot}%{_bindir}/na64sw-* \
                 %{buildroot}%{_libdir}/*.so \
                 %{buildroot}%{_libdir}/na64sw-extensions/*.so
sed -i -e 's|%{buildroot}/usr|%{_prefix}|g' %{buildroot}%{_libdir}/pkgconfig/*.pc

%clean
rm -rf %{buildroot}
rm -f %{SOURCE0}

%files
%defattr(-,root,root)
%dir %{_libdir}/na64sw-extensions
%{_libdir}/libdddMap.so.*
%{_libdir}/libna64common.so
%{_libdir}/libna64sw-app.so.*
%{_libdir}/libna64sw-calib.so.*
%{_libdir}/libna64sw-detID.so.*
%{_libdir}/libna64sw-dp.so.*
%{_libdir}/libna64sw-event.so.*
%{_libdir}/libna64sw-util.so.*
%{_libdir}/na64sw-extensions/*
%{_bindir}/*
%dir %{_sysconfdir}/na64sw/
%{_sysconfdir}/na64sw/*.yaml
%{_sysconfdir}/profile.d/na64sw-setup.*
%dir %{_datadir}/na64sw
%dir %{_datadir}/na64sw/calibrations
%dir %{_datadir}/na64sw/calibrations/override
%dir %{_datadir}/na64sw/calibrations/override/2017
%dir %{_datadir}/na64sw/calibrations/override/2021
%dir %{_datadir}/na64sw/calibrations/override/2022
%dir %{_datadir}/na64sw/calibrations/override/2023
%dir %{_datadir}/na64sw/calibrations/override/arttrack
%{_datadir}/na64sw/*.yaml
%{_datadir}/na64sw/*.json
%{_datadir}/na64sw/calibrations/*.yaml
%{_datadir}/na64sw/calibrations/*.csv
%{_datadir}/na64sw/calibrations/override/2017/*
%{_datadir}/na64sw/calibrations/override/2021/*
%{_datadir}/na64sw/calibrations/override/2022/*
%{_datadir}/na64sw/calibrations/override/2023/*
%{_datadir}/na64sw/calibrations/override/arttrack/*

%package devel
Summary: Framework for analysis and reconstruction of NA64 experimental data (development files)
Requires: %{name}
Requires: crankone-hdql-devel
Requires: crankone-catsc-devel
Requires: crankone-sdc-devel
Requires: na64utils-msadc-devel
Requires: genfit-devel
Requires: na64-coral-daq-devel
Requires: log4cpp-devel
Requires: avro-c-devel

%files devel
%defattr(-,root,root)
%{_libdir}/libdddMap.so
%{_libdir}/libna64sw-app.so
%{_libdir}/libna64sw-calib.so
%{_libdir}/libna64sw-detID.so
%{_libdir}/libna64sw-dp.so
%{_libdir}/libna64sw-event.so
%{_libdir}/libna64sw-util.so
%{_libdir}/pkgconfig/na64sw.pc
%dir %{_includedir}/na64sw
%dir %{_includedir}/na64sw/extensions
%dir %{_includedir}/na64sw/extensions/ddd
%dir %{_includedir}/na64sw/extensions/exp
%dir %{_includedir}/na64sw/extensions/std
%dir %{_includedir}/na64sw/na64app
%dir %{_includedir}/na64sw/na64calib
%dir %{_includedir}/na64sw/na64calib/indices
%dir %{_includedir}/na64sw/na64calib/loaders
%dir %{_includedir}/na64sw/na64common
%dir %{_includedir}/na64sw/na64common/calib
%dir %{_includedir}/na64sw/na64detID
%dir %{_includedir}/na64sw/na64dp
%dir %{_includedir}/na64sw/na64event
%dir %{_includedir}/na64sw/na64event/data
%dir %{_includedir}/na64sw/na64utest
%dir %{_includedir}/na64sw/na64util
%dir %{_includedir}/na64sw/na64util/3rdparty
%dir %{_includedir}/na64sw/na64util/mem
%dir %{_includedir}/na64sw/na64util/na64
%dir %{_includedir}/na64sw/na64util/numerical

%{_includedir}/na64sw/*.h
%{_includedir}/na64sw/extensions/*.hh
%{_includedir}/na64sw/extensions/ddd/*.hh
%{_includedir}/na64sw/extensions/exp/*.h
%{_includedir}/na64sw/extensions/exp/*.hh
%{_includedir}/na64sw/extensions/std/*.h
%{_includedir}/na64sw/extensions/std/*.hh
%{_includedir}/na64sw/na64app/*.hh
%{_includedir}/na64sw/na64calib/*.hh
%{_includedir}/na64sw/na64calib/indices/*.hh
%{_includedir}/na64sw/na64calib/loaders/*.hh
%{_includedir}/na64sw/na64common/*.h
%{_includedir}/na64sw/na64common/*.hh
%{_includedir}/na64sw/na64common/calib/*.h
%{_includedir}/na64sw/na64common/calib/*.hh
%{_includedir}/na64sw/na64detID/*.h
%{_includedir}/na64sw/na64detID/*.hh
%{_includedir}/na64sw/na64dp/*.hh
%{_includedir}/na64sw/na64event/*.hh
%{_includedir}/na64sw/na64event/data/*.hh
%{_includedir}/na64sw/na64utest/*.hh
%{_includedir}/na64sw/na64util/*.h
%{_includedir}/na64sw/na64util/*.hh
%{_includedir}/na64sw/na64util/3rdparty/*.h
%{_includedir}/na64sw/na64util/mem/*.hh
%{_includedir}/na64sw/na64util/na64/*.h
%{_includedir}/na64sw/na64util/na64/*.hh
%{_includedir}/na64sw/na64util/numerical/*.h
%{_includedir}/na64sw/na64util/numerical/*.hh


%description devel
Framework for analysis and reconstruction of NA64 experimental data (development files).


%changelog
* Thu Apr 23 2026 Paolo Andreetto <paolo.andreetto@pd.infn.it> - 0.6.1-1
- First release for AlmaLinux

