#
# spec file for package interception-tools
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:            interception-tools
Version:         0.1.1
Release:         1%{?dist}
Summary:         A minimal composable infrastructure on top of libudev and libevdev
License:         GPL3
URL:             https://gitlab.com/interception/linux/tools
Requires:        libevdev2
Requires:        systemd
Source0:         https://gitlab.com/interception/linux/tools/repository/v%{version}/archive.tar.gz
# Source1:       udevmon.service
# BuildRequires: boost
BuildRequires:   cmake
BuildRequires:   gcc
BuildRequires:        libevdev-devel
BuildRequires:        yaml-cpp-devel
BuildRequires:        libudev-devel
BuildRoot:       %{_tmppath}/%{name}-%{version}-build

%description
A minimal composable infrastructure on top of libudev and
libevdev.

The Interception Tools is a small set of utilities for operating on input
events of evdev devices.

%prep
%setup -n tools-v%{version}-92830567d8d86384fd42502aa0eb3de12584cdaf

%build
%cmake
make %{?_smp_mflags}

%install
#cd ${srcdir}/tools-v${pkgver}-*;
#mkdir -p "${pkgdir}/usr/share/licenses/${pkgname}";
#install -m 444 LICENSE.md "${pkgdir}/usr/share/licenses/${pkgname}";
#mkdir -p "${pkgdir}/usr/lib/systemd/system";
cat <<EOF > udevmon.service
[Unit]
Description=udevmon
After=systemd-user-sessions.service

[Service]
ExecStart=/usr/bin/nice -n -20 /usr/bin/udevmon -c /etc/udevmon.yaml

[Install]
WantedBy=multi-user.target
EOF
install -D -m 644 "udevmon.service" %{buildroot}%{_unitdir}/udevmon.service
#make install
cd build/
make install DESTDIR=%{buildroot}

%pre
%service_add_pre udevmon.service

%post
%service_add_post udevmon.service

%preun
%service_del_preun udevmon.service

%postun
%service_del_postun udevmon.service

%files
# TODO: Add files
/usr/bin/intercept
/usr/bin/udevmon
/usr/bin/uinput
/usr/lib/systemd/system/udevmon.service

%changelog
* Thu Dec 21 2017 grimsleydl <grimsleydl@gmail.com> - 0.1.1
- Initial version
