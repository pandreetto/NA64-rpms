%global debug_package %{nil}
%undefine _disable_source_fetch

%global _pver 0.0.3
%global _tagver 7846a45a75b34c405c24a58c9a53fd428fe22502

%global _cbuilddir %{_builddir}/%{name}-%{version}/build
%global _sbuilddir %{_builddir}/%{name}-%{version}/na64-crilin-simulation-%{_tagver}

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
%setup -c
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
* Wed Oct 07 2026 Paolo Andreetto <paolo.andreetto@pd.infn.it> - 0.0.3-1
- Minor changes
* Fri Aug 28 2026 Paolo Andreetto <paolo.andreetto@pd.infn.it> - 0.0.2-1
- Working DM physics
* Mon Aug 24 2026 Paolo Andreetto <paolo.andreetto@pd.infn.it> - 0.0.1-1
- First release for AlmaLinux

