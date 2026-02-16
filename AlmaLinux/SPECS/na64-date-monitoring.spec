%global debug_package %{nil}
%undefine _disable_source_fetch

%global _pver 0.0.1
%global _tagver 6ba2693a14f730272a2b1e75e71c6edb70204071

%global _sbuilddir %{_builddir}/%{name}-%{version}/p348-daq-%{_tagver}/date/monitoring/
%global _cbuilddir %{_builddir}/%{name}-%{version}/p348-daq-%{_tagver}/date/monitoring/Linux

Summary: DAQ Test Environment, monitoring libraries
Name: na64-date-monitoring
Version: %{_pver}
Release: 1.na64%{?dist}
License: GPL v.3
Vendor: CERN
URL: https://gitlab.cern.ch/P348
Group: Development/Libraries
BuildArch: %{_arch}
BuildRequires: make
BuildRequires: root
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
AutoReqProv: yes
Source0: https://gitlab.cern.ch/P348/p348-daq/-/archive/%{_tagver}/p348-daq-%{_tagver}.zip
Source1: na64-date-monitoring_cmakeconfig.cmake
Patch0: na64-date-monitoring_gmake.patch

%description
Libraries for the monitoring system of the DAQ Test Environment

%prep
%setup -c
rm -rf %{buildroot}
mkdir -p %{buildroot}
patch %{_sbuilddir}/GNUmakefile %{PATCH0}

%build
mkdir %{_cbuilddir}
cd %{_sbuilddir}
unset CFLAGS
make ./Linux/
make ./Linux/libmonitor.so

%install
mkdir -p %{buildroot}%{_libdir}
mkdir -p %{buildroot}%{_includedir}/date-monitoring
mkdir -p %{buildroot}%{_libdir}/cmake/date-monitoring
cp %{_cbuilddir}/libmonitor.so %{buildroot}%{_libdir}/libdate-monitoring.so
cp %{_sbuilddir}/*.h %{buildroot}%{_includedir}/date-monitoring
cp %{SOURCE1} %{buildroot}%{_libdir}/cmake/date-monitoring/DATEMONITORINGConfig.cmake
printf "set(PACKAGE_VERSION \"%{_pver}\")\n" \
    | tee %{buildroot}%{_libdir}/cmake/date-monitoring/DATEMONITORINGConfigVersion.cmake

%clean
rm -rf %{buildroot}
rm -f %{SOURCE0}

%files
%defattr(-,root,root)
%{_libdir}/*.so

%package devel
Summary: DAQ Test Environment, monitoring libraries (development files)
Requires: %{name}
Requires: root

%description devel
Development files for the monitoring system of the DAQ Test Environment.

%files devel
%defattr(-,root,root)
%dir %{_includedir}/date-monitoring
%{_includedir}/date-monitoring/*.h
%dir %{_libdir}/cmake/date-monitoring
%{_libdir}/cmake/date-monitoring/*.cmake

%changelog
* Wed Jan 21 2026 Paolo Andreetto <paolo.andreetto@pd.infn.it> - 0.0.1-1
- First release for AlmaLinux


