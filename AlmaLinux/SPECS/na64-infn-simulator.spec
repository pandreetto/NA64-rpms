%global debug_package %{nil}
%undefine _disable_source_fetch

%global _pver 0.0.2
%global _tagver b3f41829e1d6aeb026c77e22ae3e8cf3ee365d32

%global _sbuilddir %{_builddir}/%{name}-%{version}/geant4/simulation/examples/example_crilin
%global _cbuilddir %{_builddir}/%{name}-%{version}/build

Summary: NA64 detector simulator with crilin
Name: na64-infn-simulator
Version: %{_pver}
Release: 1.na64%{?dist}
License: GPL v.3
Vendor: CERN
URL: https://gitlab.cern.ch/P348/na64-simulation
Group: Development/Libraries
BuildArch: %{_arch}
BuildRequires: cmake
BuildRequires: make
BuildRequires: root
BuildRequires: na64-geant4-lib-devel
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
AutoReqProv: yes

%description
NA64 detector simulator with crilin

%prep
rm -rf %{_builddir}/%{name}-%{version}
git clone https://gitlab.cern.ch/P348/na64-simulation.git %{_builddir}/%{name}-%{version}
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

%files
%defattr(-,root,root)
%{_bindir}/mkgeant4

%changelog
* Wed Nov 04 2026 Paolo Andreetto <paolo.andreetto@pd.infn.it> - 0.0.2-1
- New geometries available
* Mon Nov 02 2026 Paolo Andreetto <paolo.andreetto@pd.infn.it> - 0.0.1-1
- First release for AlmaLinux

