%global debug_package %{nil}
%undefine _disable_source_fetch

#
# This is a temporary package, git reference 410c425e0a8fb0b953b52d00103f77474069c972
#
%global _pver 2.6.0

%global _sbuilddir %{_builddir}/%{name}-%{version}/DMG4-%{version}
%global _cbuilddir %{_builddir}/%{name}-%{version}/build

Summary: Simulation of Dark Matter production in the electron, positron and muon beams
Name: na64-dmg4
Version: %{_pver}
Release: 1.na64%{?dist}
License: GPL v.3
Vendor: CERN
URL: https://gitlab.cern.ch/P348/DMG4
Group: Development/Libraries
BuildArch: %{_arch}
BuildRequires: cmake
BuildRequires: make
BuildRequires: geant4-devel
BuildRequires: gsl-devel
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
AutoReqProv: yes
Source0: https://nexus.pd.infn.it/artifacts/repository/misc/na64-dmg4-%{version}.tar.gz
Patch0: na64-dmg4-localbuild.patch

%description
Simulation of Dark Matter production in the electron, positron and muon beams

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

%clean
rm -rf %{buildroot}
rm -f %{SOURCE0}

%files
%defattr(-,root,root)
%{_libdir}/*.so


%package devel
Summary: Simulation of Dark Matter production in the electron, positron and muon beams (development files)
Requires: %{name}
Requires: geant4-devel
Requires: gsl-devel

%description devel
Simulation of Dark Matter production in the electron, positron and muon beams (development files).

%files devel
%defattr(-,root,root)
%{_includedir}/*.hh
%dir %{_includedir}/DMG4
%{_includedir}/DMG4/*.hh
%dir %{_includedir}/DMG4/DMParticles
%{_includedir}/DMG4/DMParticles/*.hh
%dir %{_includedir}/DMG4/DMProcesses
%{_includedir}/DMG4/DMProcesses/*.hh
%dir %{_includedir}/UtilsDM
%{_includedir}/UtilsDM/*.hh

