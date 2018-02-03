#
# spec file for package caps2esc
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


Name:            caps2esc
Version:         0.1.3
Release:         1%{?dist}
Summary:         A minimal composable infrastructure on top of libudev and libevdev
License:         GPL3
URL:             https://github.com/grimsleydl/caps2esc
Requires:        interception-tools
Source0:         https://github.com/grimsleydl/%{name}/archive/v%{version}/archive.tar.gz
# BuildRequires: boost
BuildRequires:   cmake
BuildRequires:   gcc
BuildRoot:       %{_tmppath}/%{name}-%{version}-build

%description
caps2esc: transforming the most useless key ever in the most useful one

%prep
%setup -n %{name}-%{version}

%build
%cmake
make %{?_smp_mflags}

%install
cat <<EOF > udevmon.yaml
- JOB: "intercept -g \$DEVNODE | caps2esc | uinput -d \$DEVNODE"
  DEVICE:
    EVENTS:
      EV_KEY: [KEY_CAPSLOCK, KEY_ESC]
EOF
install -D -m 644 "udevmon.yaml" %{buildroot}/etc/udevmon.yaml
cd build/
make install DESTDIR=%{buildroot}

%files
# TODO: Add files
/usr/bin/caps2esc
/etc/udevmon.yaml

%changelog
* Thu Dec 21 2017 grimsleydl <grimsleydl@gmail.com> - 0.1.1
- Initial version
