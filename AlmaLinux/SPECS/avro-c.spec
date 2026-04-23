%global debug_package %{nil}
%undefine _disable_source_fetch

%global _pver 1.12.0
%global _tagver 1.12.0

%global _sbuilddir %{_builddir}/%{name}-%{version}/avro-c-%{_tagver}
%global _cbuilddir %{_builddir}/%{name}-%{version}/build

Summary: Data serialization system
Name: avro-c
Version: %{_pver}
Release: 1.na64%{?dist}
License: GPL v.3
Vendor: CERN
URL: https://avro.apache.org
Group: Development/Libraries
BuildArch: %{_arch}
BuildRequires: cmake
BuildRequires: make
BuildRequires: chrpath
BuildRequires: jansson-devel
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
AutoReqProv: yes
Source0: https://dlcdn.apache.org/avro/avro-%{_tagver}/c/avro-c-%{_tagver}.tar.gz

%description
Data serialization system

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
      %{_sbuilddir}
make %{?_smp_mflags}

%install
cd %{_cbuilddir}
make install
chrpath --delete %{buildroot}%{_libdir}/*.so %{buildroot}%{_bindir}/avro*
sed -i -e 's|%{buildroot}/usr|%{_prefix}|g' %{buildroot}%{_libdir}/pkgconfig/*.pc

%clean
rm -rf %{buildroot}
rm -f %{SOURCE0}

%files
%defattr(-,root,root)
%{_bindir}/avro*
%{_libdir}/*.so.*

%package devel
Summary: Data serialization system (development files)
Requires: %{name}
Requires: jansson-devel

%description devel
Data serialization system (development files)

%files devel
%defattr(-,root,root)
%{_libdir}/*.so
%{_libdir}/*.a
%{_libdir}/pkgconfig/*.pc
%dir %{_includedir}/avro
%{_includedir}/avro.h
%{_includedir}/avro/*.h

%changelog
* Thu Apr 23 2026 Paolo Andreetto <paolo.andreetto@pd.infn.it> - 1.12.0-1
- First release for AlmaLinux


