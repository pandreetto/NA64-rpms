%global debug_package %{nil}
%undefine _disable_source_fetch

%global _pver 0.0.1
%global _tagver 6ba2693a14f730272a2b1e75e71c6edb70204071

%global _sbuilddir %{_builddir}/%{name}-%{version}/p348-daq-%{_tagver}/coral/src/DaqDataDecoding
%global _cbuilddir %{_builddir}/%{name}-%{version}/p348-daq-%{_tagver}/coral/src/DaqDataDecoding/build

Summary: Data acquisition library from Coral suite
Name: na64-coral-daq
Version: %{_pver}
Release: 1.na64%{?dist}
License: GPL v.3
Vendor: CERN
URL: https://gitlab.cern.ch/P348
Group: Development/Libraries
BuildArch: %{_arch}
BuildRequires: cmake
BuildRequires: make
BuildRequires: na64-date-monitoring-devel
BuildRequires: expat-devel
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
AutoReqProv: yes
Source0: https://gitlab.cern.ch/P348/p348-daq/-/archive/%{_tagver}/p348-daq-%{_tagver}.zip
Source1: CoralDAQ_CMakeLists.txt
Source2: na64-coral-daq_cmakeconfig.cmake

%description
Data acquisition library from Coral suite.

%prep
%setup -c
rm -rf %{buildroot}
mkdir -p %{buildroot}
cp %{SOURCE1} %{_sbuilddir}/CMakeLists.txt

%build
mkdir %{_cbuilddir}
cd %{_cbuilddir}
cmake -DCMAKE_INSTALL_PREFIX=%{buildroot}%{_prefix} \
      -DCMAKE_BUILD_TYPE=RelWithDebInfo \
      -DCMAKE_CXX_STANDARD=17 \
      -DDATEMONITORING_DIR=/usr/lib64/cmake/date-monitoring \
      -Wno-dev \
      %{_sbuilddir}
make %{?_smp_mflags}

%install
cd %{_cbuilddir}
make install
mkdir -p %{buildroot}%{_libdir}/cmake/CoralDAQ
cp %{SOURCE2} %{buildroot}%{_libdir}/cmake/CoralDAQ/CoralDAQConfig.cmake
printf "set(PACKAGE_VERSION \"%{_pver}\")\n" \
    | tee %{buildroot}%{_libdir}/cmake/CoralDAQ/CoralDAQConfigVersion.cmake

mkdir -p %{buildroot}%{_datadir}/CoralDAQ
cp -r %{_sbuilddir}/../../../maps/*.xml %{buildroot}%{_datadir}/CoralDAQ

%clean
rm -rf %{buildroot}
rm -f %{SOURCE0}

%files
%defattr(-,root,root)
%{_libdir}/*.so
%dir %{_datadir}/CoralDAQ
%dir %{_datadir}/CoralDAQ/20*.xml
%{_datadir}/CoralDAQ/20*.xml/*.xml
%dir %{_datadir}/CoralDAQ/test.xml
%{_datadir}/CoralDAQ/test.xml/*.xml

%package devel
Summary: Data acquisition library from Coral suite (development files)
Requires: %{name}
Requires: na64-date-monitoring-devel
Requires: expat-devel

%description devel
Data acquisition library from Coral suite (development files).

%files devel
%defattr(-,root,root)
%dir %{_includedir}/na64/ddd-ext
%{_includedir}/na64/ddd-ext/*.h
%dir %{_libdir}/cmake/CoralDAQ
%{_libdir}/cmake/CoralDAQ/*.cmake


%changelog
* Mon Feb 16 2026 Paolo Andreetto <paolo.andreetto@pd.infn.it> - 0.0.1-1
- First release for AlmaLinux

