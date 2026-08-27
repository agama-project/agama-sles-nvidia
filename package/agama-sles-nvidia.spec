#
# spec file for package agama-sles-nvidia
#
# Copyright (c) 2026 SUSE LLC
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


Name:           agama-sles-nvidia
#               This will be set by osc services, that will run after this.
Version:        0
Release:        0
Summary:        SLES for NVIDIA product definition and CSS branding for the Agama installer
License:        GPL-2.0-only
URL:            https://github.com/agama-project/agama-sles-nvidia
BuildArch:      noarch
Source0:        agama-sles-nvidia.tar

%description
Products definition for Agama installer.

%prep
%autosetup -a0 -n agama-sles-nvidia

%build

%install
env \
  SRCDIR=. \
  DESTDIR=%{buildroot} \
  datadir=%{_datadir} \
  %{_builddir}/agama-sles-nvidia/install.sh

%package product
Summary: Product definition for the Agama installer

%description product
Definition of the SLES for NVIDIA product for the Agama installer.

%files product
%doc README.md
%license LICENSE
%dir %{_datadir}/agama
%dir %{_datadir}/agama/products.d
%{_datadir}/agama/products.d/*.yaml

%package branding
License: GPL-2.0-only and OFL-1.1
Summary: Branding for the SLES for NVIDIA product

%description branding
Specific CSS branding for the Agama installer for the SLES for NVIDIA product.

%files branding
%doc README.md
%license LICENSE
%license branding/Rubik-OFL.txt
%dir %{_datadir}/agama
%{_datadir}/agama/web_ui

%changelog
