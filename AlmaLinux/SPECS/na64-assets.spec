%global debug_package %{nil}
%undefine _disable_source_fetch

%global _pver 0.14.0
%global _tagver v14

%global _sbuilddir %{_builddir}/%{name}-%{version}/assets-%{_tagver}

Summary: Static assets for NA64 reconstruction frameworks
Name: na64-assets
Version: %{_pver}
Release: 1.na64%{?dist}
License: GPL v.3
Vendor: CERN
URL: https://gitlab.cern.ch/P348/assets
Group: Development/Libraries
BuildArch: %{_arch}
BuildRequires: make
Requires: na64-sw
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
AutoReqProv: yes
Source0: https://gitlab.cern.ch/P348/assets/-/archive/%{_tagver}/assets-%{_tagver}.tar.gz

%description
Static assets for NA64 reconstruction frameworks

%prep
%setup -c
rm -rf %{buildroot}
mkdir -p %{buildroot}

%build
echo "Nothing to build"

%install
mkdir -p %{buildroot}%{_datadir}/na64sw/calib
cp -r %{_sbuilddir}/calib/20* %{buildroot}%{_datadir}/na64sw/calib
mkdir -p %{buildroot}%{_datadir}/na64sw/multiplex_map
cp -r %{_sbuilddir}/multiplex_map/*.csv %{buildroot}%{_datadir}/na64sw/multiplex_map

%clean
rm -rf %{buildroot}
rm -f %{SOURCE0}

%files
%defattr(-,root,root)
%dir %{_datadir}/na64sw/calib
%dir %{_datadir}/na64sw/calib/2021
%{_datadir}/na64sw/calib/2021/*.txt
%dir %{_datadir}/na64sw/calib/2021mu
%{_datadir}/na64sw/calib/2021mu/*.txt
%dir %{_datadir}/na64sw/calib/2022
%{_datadir}/na64sw/calib/2022/*.txt
%dir %{_datadir}/na64sw/calib/2022mu
%{_datadir}/na64sw/calib/2022mu/*.txt
%dir %{_datadir}/na64sw/calib/2023
%{_datadir}/na64sw/calib/2023/*.txt
%dir %{_datadir}/na64sw/calib/2023mu
%{_datadir}/na64sw/calib/2023mu/*.txt
%dir %{_datadir}/na64sw/calib/2024
%{_datadir}/na64sw/calib/2024/*.txt
%dir %{_datadir}/na64sw/calib/2024mu
%{_datadir}/na64sw/calib/2024mu/*.txt
%dir %{_datadir}/na64sw/calib/2025
%{_datadir}/na64sw/calib/2025/*.txt
%dir %{_datadir}/na64sw/calib/2025hadr
%{_datadir}/na64sw/calib/2025hadr/*.txt
%dir %{_datadir}/na64sw/multiplex_map
%{_datadir}/na64sw/multiplex_map/*.csv

%changelog
* Wed May 06 2026 Paolo Andreetto <paolo.andreetto@pd.infn.it> - 0.14.0-1
- First release for AlmaLinux

