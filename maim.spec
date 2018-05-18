#
# spec file for package maim
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
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


# See also http://en.opensuse.org/openSUSE:Specfile_guidelines
Name:           maim
Version:        5.5.1
Release:        0
Summary:        Flexible screenshotting utility
License:        GPL-3.0+
Group:          Productivity/Graphics/Other
Url:            https://github.com/naelstrof/maim
Source0:        https://github.com/naelstrof/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  gengetopt
BuildRequires:  pkgconfig(imlib2)
BuildRequires:  pkgconfig(xfixes)
BuildRequires:  pkgconfig(xrandr)
# pkgconfig(imlib2) above is not enough for some reason
Requires:       imlib2
Requires:       slop
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
maim (Make Image) is a utility that takes screenshots of your desktop
using imlib2. It's meant to overcome shortcomings of scrot and performs
better in several ways.

%prep
%setup -q

%build
%cmake
make %{?_smp_mflags}

%install
# install executable
mkdir -p %{buildroot}%{_bindir}
pushd build
make DESTDIR=%{buildroot} install %{?_smp_mflags}
popd

# install man
install -Dm 0644 %{name}.1 %{buildroot}%{_mandir}/man1/%{name}.1

%files
%defattr(-,root,root,-)
%doc COPYING README.md
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1%{ext_man}

%changelog
