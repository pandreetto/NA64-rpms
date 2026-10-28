%global debug_package %{nil}
%undefine _disable_source_fetch

%global _pver 0.0.8
%global _tagver 263f0f16abb341798e2f4490b61ef0d63c9f2303

%global _cbuilddir %{_builddir}/%{name}-%{version}/build
%global _sbuilddir %{_builddir}/%{name}-%{version}

Summary: Geant4 simulator for CRILIN detector
Name: na64-crilin-simulation
Version: %{_pver}
Release: 1.na64%{?dist}
License: GPL v.3
Vendor: CERN
URL: https://gitlab.cern.ch/paandree/na64-crilin-simulation
Group: Development/Libraries
BuildArch: %{_arch}
BuildRequires: cmake
BuildRequires: make
BuildRequires: na64-geant4-lib-devel
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
AutoReqProv: yes
Source0: https://gitlab.cern.ch/paandree/na64-crilin-simulation/-/archive/%{_tagver}/na64-crilin-simulation-%{_tagver}.zip

%description
Geant4 simulator for CRILIN detector.

%prep
rm -rf %{_builddir}/%{name}-%{version}
git clone https://gitlab.cern.ch/paandree/na64-crilin-simulation.git %{_builddir}/%{name}-%{version}
cd %{_builddir}/%{name}-%{version}
git checkout %{_tagver}

rm -rf %{buildroot}
mkdir -p %{buildroot}

%build
mkdir %{_cbuilddir}
cd %{_cbuilddir}
cmake -DCMAKE_INSTALL_PREFIX=%{buildroot}%{_prefix} \
      -DCMAKE_BUILD_TYPE=RelWithDebInfo \
      -DCMAKE_CXX_STANDARD=20 \
      -Wno-dev \
      %{_sbuilddir}
make %{?_smp_mflags}

%install
cd %{_cbuilddir}
make install

%clean
rm -rf %{buildroot}
rm -f %{SOURCE0}

%files
%defattr(-,root,root)
%{_bindir}/mkgeant4

%changelog
* Wed Oct 28 2026 Paolo Andreetto <paolo.andreetto@pd.infn.it> - 0.0.8-1
- Default values for trigger thresholds
* Thu Oct 22 2026 Paolo Andreetto <paolo.andreetto@pd.infn.it> - 0.0.7-1
- Fixed bug disabling crilin
* Tue Oct 20 2026 Paolo Andreetto <paolo.andreetto@pd.infn.it> - 0.0.6-1
- ECal in the geometry
* Mon Oct 19 2026 Paolo Andreetto <paolo.andreetto@pd.infn.it> - 0.0.5-1
- Default position for crilin
* Fri Oct 16 2026 Paolo Andreetto <paolo.andreetto@pd.infn.it> - 0.0.4-1
- Multi geometry support
* Wed Oct 07 2026 Paolo Andreetto <paolo.andreetto@pd.infn.it> - 0.0.3-1
- Minor changes
* Fri Aug 28 2026 Paolo Andreetto <paolo.andreetto@pd.infn.it> - 0.0.2-1
- Working DM physics
* Mon Aug 24 2026 Paolo Andreetto <paolo.andreetto@pd.infn.it> - 0.0.1-1
- First release for AlmaLinux

