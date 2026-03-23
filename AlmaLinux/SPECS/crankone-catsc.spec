%global debug_package %{nil}
%undefine _disable_source_fetch

%global _pver 1.0.0
%global _tagver 1.0

%global _sbuilddir %{_builddir}/%{name}-%{version}/catsc-%{_tagver}
%global _cbuilddir %{_builddir}/%{name}-%{version}/build

Summary: Generic C/C++ implementation of cellular automata for track finding
Name: crankone-catsc
Version: %{_pver}
Release: 1.na64%{?dist}
License: MPL 2.0
Vendor: CERN
URL: https://github.com/CrankOne/catsc
Group: Development/Libraries
BuildArch: %{_arch}
BuildRequires: cmake
BuildRequires: make
BuildRequires: chrpath
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
AutoReqProv: yes
Source0: https://github.com/CrankOne/catsc/archive/refs/tags/v%{_tagver}.tar.gz

%description
This code is based on the algorithm of cellular automaton evolution proposed for track finding.
Algorithm is designed to perform initial track finding for experiments in High energy physics, 
yet its topological properties may imply a broader usage.

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
      -DBUILD_TESTS=OFF \
      -Wno-dev \
      %{_sbuilddir}
make %{?_smp_mflags}

%install
cd %{_cbuilddir}
make install

mv %{buildroot}%{_prefix}/lib %{buildroot}%{_libdir}
sed -i -e 's|%{buildroot}/usr|%{_prefix}|g' %{buildroot}%{_libdir}/pkgconfig/catsc.pc
sed -i -e 's|lib/libcatsc|lib64/libcatsc|g' %{buildroot}%{_libdir}/cmake/catsc/catscTargets-relwithdebinfo.cmake

%clean
rm -rf %{buildroot}
rm -f %{SOURCE0}

%files
%defattr(-,root,root)
%{_libdir}/*.so.*

%package devel
Summary: Generic C/C++ implementation of cellular automata for track finding (development files)
Requires: %{name}
Requires: root
Requires: root-geom
Requires: root-smatrix
Requires: root-montecarlo-eg
Requires: root-graf3d-eve
Requires: root-genvector

%description devel
This code is based on the algorithm of cellular automaton evolution proposed for track finding.
Algorithm is designed to perform initial track finding for experiments in High energy physics, 
yet its topological properties may imply a broader usage.

%files devel
%defattr(-,root,root)
%{_libdir}/*.so
%dir %{_includedir}/catsc
%{_includedir}/catsc/*.h
%{_includedir}/catsc/*.hh
%dir %{_libdir}/cmake/catsc
%{_libdir}/cmake/catsc/*.cmake
%{_libdir}/pkgconfig/catsc.pc

%changelog
* Mon Jan 19 2026 Paolo Andreetto <paolo.andreetto@pd.infn.it> - 1.0.0-1
- First release for AlmaLinux


