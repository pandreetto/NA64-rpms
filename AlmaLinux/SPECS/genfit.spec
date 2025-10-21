%global debug_package %{nil}
%undefine _disable_source_fetch

%global _pver 2.0.6
%global _tagver af3993d6f6bd65beb75699436697125900b38933

%global _sbuilddir %{_builddir}/%{name}-%{version}/GenFit-%{_tagver}
%global _cbuilddir %{_builddir}/%{name}-%{version}/build

Summary: Experiment-independent framework for particle track reconstruction
Name: genfit
Version: %{_pver}
Release: 1.na64%{?dist}
License: GPL v.3
Vendor: FAIR
URL: https://github.com/GenFit/GenFit
Group: Development/Libraries
BuildArch: %{_arch}
BuildRequires: cmake
BuildRequires: make
BuildRequires: chrpath
BuildRequires: root
BuildRequires: root-geom
BuildRequires: root-smatrix
BuildRequires: root-montecarlo-eg
BuildRequires: root-graf3d-eve
BuildRequires: root-genvector
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
AutoReqProv: yes
Source0: https://github.com/GenFit/GenFit/archive/%{_tagver}.tar.gz

%description
Experiment-independent framework for particle track reconstruction

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
      -DBUILD_TESTING=OFF \
      %{_sbuilddir}
make %{?_smp_mflags}

%install
cd %{_cbuilddir}
make install

mkdir -p %{buildroot}%{_includedir}/GenFit
mv %{buildroot}%{_includedir}/*.h %{buildroot}%{_includedir}/GenFit

%clean
rm -rf %{buildroot}
rm -f %{SOURCE0}

%files
%defattr(-,root,root)
%{_libdir}/*.so.*
%{_libdir}/*.pcm

%package devel
Summary: Experiment-independent framework for particle track reconstruction (development files)
Requires: %{name}
Requires: geant4-devel
Requires: gsl-devel

%description devel
Experiment-independent framework for particle track reconstruction (development files).

%files devel
%defattr(-,root,root)
%{_libdir}/*.so
%dir %{_includedir}/GenFit
%{_includedir}/GenFit/*.h


%changelog
* Fri Oct 17 2025 Paolo Andreetto <paolo.andreetto@pd.infn.it> - 2.0.6-1
- First release for AlmaLinux

