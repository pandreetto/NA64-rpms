%global debug_package %{nil}
%undefine _disable_source_fetch

%global _pver 0.0.2
%global _tagver 6796e6c7a1714aa7c97e3df513af7fce758766aa

%global _sbuilddir %{_builddir}/%{name}-%{version}/tracking-tools-%{_tagver}
%global _cbuilddir %{_builddir}/%{name}-%{version}/build

Summary: Generic library for tracking
Name: p348-tracking-tools
Version: %{_pver}
Release: 1.na64%{?dist}
License: GPL v.3
Vendor: NA64 project
URL: https://gitlab.cern.ch/P348/tracking-tools
Group: Development/Libraries
BuildArch: %{_arch}
BuildRequires: cmake
BuildRequires: make
BuildRequires: chrpath
BuildRequires: boost-devel
BuildRequires: eigen3-devel
BuildRequires: root
BuildRequires: root-geom
BuildRequires: genfit-devel
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
AutoReqProv: yes
Source0: https://gitlab.cern.ch/P348/tracking-tools/-/archive/%{_tagver}/tracking-tools-%{_tagver}.zip

%description
This library is a generic library for tracking using a given set of track candidates.
It relies on the use of different tracking algorithms and is built is such a way that it only cares about the inputs

%prep
%setup -c
rm -rf %{buildroot}
mkdir -p %{buildroot}

%build
mkdir %{_cbuilddir}
cd %{_cbuilddir}
cmake -DCMAKE_INSTALL_PREFIX=%{buildroot}%{_prefix} \
      -DCMAKE_BUILD_TYPE=RelWithDebInfo \
      -DCMAKE_CXX_STANDARD=17 \
      -DCMAKE_INSTALL_LIBDIR=lib64 \
      -DGENFIT_INCLUDE_DIR=/usr/include/GenFit \
      -Wno-dev \
      %{_sbuilddir}
make %{?_smp_mflags}

%install
cd %{_cbuilddir}
make install

rm -rf %{buildroot}%{_prefix}/lib

%clean
rm -rf %{buildroot}
rm -f %{SOURCE0}

%files
%defattr(-,root,root)
%{_libdir}/*.so.*

%package devel
Summary: Generic library for tracking (development files)
Requires: %{name}

%description devel
Experiment-independent framework for particle track reconstruction (development files).

%files devel
%defattr(-,root,root)
%{_libdir}/*.so
%dir %{_includedir}/TrackingTools
%{_includedir}/TrackingTools/*.hh
%{_datadir}/cmake/*.cmake


%changelog
* Mon Jan 19 2026 Paolo Andreetto <paolo.andreetto@pd.infn.it> - 0.0.2-1
- First release for AlmaLinux

