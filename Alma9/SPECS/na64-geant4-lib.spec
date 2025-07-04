%global debug_package %{nil}
%undefine _disable_source_fetch

#
# This is a temporary package, no reference provided
#
%global _pver 1.0.0

%global _sbuilddir %{_builddir}/%{name}-%{version}/simulation
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
Source0: https://nexus.pd.infn.it/artifacts/repository/misc/na64-geant4-lib-%{version}.tar.gz
Source1: na64-geant4-lib-CMakeLists.txt
Source2: na64-geant4-lib-git-version.cc
Source3: NA64geant4Config.cmake
Source4: NA64geant4ConfigVersion.cmake.in

%description
Simulation library for NA64 project

%prep
%setup -c
rm -rf %{buildroot}
mkdir -p %{buildroot}
cp %{SOURCE1} %{_sbuilddir}/CMakeLists.txt
cp %{SOURCE2} %{_sbuilddir}/src/Utils/git_version.cc

%build
mkdir %{_cbuilddir}
cd %{_cbuilddir}
cmake -DCMAKE_INSTALL_PREFIX=%{buildroot}%{_prefix} \
      -DCMAKE_BUILD_TYPE=RelWithDebInfo \
      -DCMAKE_CXX_STANDARD=17 \
      -DDMG4_ROOT_DIR=%{_prefix} \
      %{_sbuilddir}
make %{?_smp_mflags}

%install
cd %{_cbuilddir}
make install

mkdir -p %{buildroot}%{cmake_na64g4_dir}
cp %{SOURCE3} %{buildroot}%{cmake_na64g4_dir}
# TODO missing versioning
cp %{SOURCE4} %{buildroot}%{cmake_na64g4_dir}/NA64geant4ConfigVersion.cmake

%clean
rm -rf %{buildroot}
rm -f %{SOURCE0}

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

