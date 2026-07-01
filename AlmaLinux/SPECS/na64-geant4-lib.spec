%global debug_package %{nil}
%undefine _disable_source_fetch

%global _pver 1.0.1

%global _sbuilddir %{_builddir}/%{name}-%{version}/geant4/simulation
%global _cbuilddir %{_builddir}/%{name}-%{version}/build

%global cmake_na64g4_dir %{_libdir}/cmake/NA64geant4

Summary: Simulation library for NA64 project
Name: na64-geant4-lib
Version: %{_pver}
Release: 1.na64%{?dist}
License: GPL v.3
Vendor: CERN
URL: https://gitlab.cern.ch/P348/DMG4
Group: Development/Libraries
BuildArch: %{_arch}
BuildRequires: cmake
BuildRequires: make
BuildRequires: root
BuildRequires: na64-dmg4-devel
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
AutoReqProv: yes
Source0: na64-geant4-lib-CMakeLists.txt
Source1: na64-geant4-lib-git-version.cc
Source2: NA64geant4Config.cmake
Source3: NA64geant4ConfigVersion.cmake.in

%description
Simulation library for NA64 project

%prep
rm -rf %{_builddir}/%{name}-%{version}
git clone https://gitlab.cern.ch/P348/na64-simulation.git %{_builddir}/%{name}-%{version}

rm -rf %{buildroot}
mkdir -p %{buildroot}
cp %{SOURCE0} %{_sbuilddir}/CMakeLists.txt
cp %{SOURCE1} %{_sbuilddir}/src/Utils/git_version.cc

%build
mkdir %{_cbuilddir}
cd %{_cbuilddir}
cmake -DCMAKE_INSTALL_PREFIX=%{buildroot}%{_prefix} \
      -DCMAKE_BUILD_TYPE=RelWithDebInfo \
      -DCMAKE_CXX_STANDARD=20 \
      -DDMG4_ROOT_DIR=%{_prefix} \
      %{_sbuilddir}
make %{?_smp_mflags}

%install
cd %{_cbuilddir}
make install

mkdir -p %{buildroot}%{cmake_na64g4_dir}
cp %{SOURCE2} %{buildroot}%{cmake_na64g4_dir}
cp %{SOURCE3} %{buildroot}%{cmake_na64g4_dir}/NA64geant4ConfigVersion.cmake
sed -i -e 's|1.0.0|%{_pver}|g' %{buildroot}%{cmake_na64g4_dir}/NA64geant4ConfigVersion.cmake

%clean
rm -rf %{buildroot}
rm -rf %{_builddir}/%{name}-%{version}

%files
%defattr(-,root,root)
%{_libdir}/*.so


%package devel
Summary: Simulation library for NA64 project (development files)
Requires: %{name}
Requires: root
Requires: na64-dmg4-devel

%description devel
Simulation library for NA64 project (development files).

%files devel
%defattr(-,root,root)
%{_includedir}/*.hh
%{_includedir}/*.inc
%dir %{_includedir}/HistRoot
%{_includedir}/HistRoot/*.hh
%dir %{cmake_na64g4_dir}
%{cmake_na64g4_dir}/*.cmake

%changelog
* Wed Jul 01 2026 Paolo Andreetto <paolo.andreetto@pd.infn.it> - 1.0.1-1
- Second release for AlmaLinux
* Fri Oct 17 2025 Paolo Andreetto <paolo.andreetto@pd.infn.it> - 1.0.0-1
- First release for AlmaLinux

