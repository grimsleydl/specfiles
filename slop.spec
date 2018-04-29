#
# spec file for package slop
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
Name:           slop
Version:        7.4
Release:        0
Summary:        Query for a selection from the user and print the region to stdout
License:        GPL-3.0+
Group:          Productivity/Graphics/Other
Url:            https://github.com/naelstrof/slop
Source0:        https://github.com/naelstrof/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  gengetopt
BuildRequires:  glm-devel
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(glew)
BuildRequires:  pkgconfig(glu)
BuildRequires:  pkgconfig(imlib2)
BuildRequires:  pkgconfig(xrandr)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
slop (Select Operation) queries for a selection from the user and prints
the region to stdout. It grabs the mouse and turns it into a crosshair,
lets the user click and drag to make a selection (or click on a window)
while drawing a pretty box around it, then finally prints the selection's
dimensions to stdout.

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

%clean
echo NOOP

%files
%defattr(-,root,root,-)
%doc COPYING README.md
%{_bindir}/%{name}
%{_includedir}/%{name}.*
%{_libdir}/libslopy.so*
%{_mandir}/man1/%{name}.*

%changelog
