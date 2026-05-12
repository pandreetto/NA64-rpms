%global debug_package %{nil}
%undefine _disable_source_fetch

%global _pver 2.3.0
%global _tagver 02-03-00

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
Source0: https://github.com/GenFit/GenFit/archive/refs/tags/%{_tagver}.tar.gz

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
      -DCMAKE_CXX_STANDARD=20 \
      -DBUILD_TESTING=OFF \
      -Wno-dev \
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
Requires: root
Requires: root-geom
Requires: root-smatrix
Requires: root-montecarlo-eg
Requires: root-graf3d-eve
Requires: root-genvector

%description devel
Experiment-independent framework for particle track reconstruction (development files).

%files devel
%defattr(-,root,root)
%{_libdir}/*.so
%dir %{_includedir}/GenFit
%{_includedir}/GenFit/*.h


%changelog
* Mon Jan 19 2026 Paolo Andreetto <paolo.andreetto@pd.infn.it> - 2.3.0-1
- First release for AlmaLinux

