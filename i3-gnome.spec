#
# spec file for package i3-gnome
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
%global commit    28ff65cf74f8869c7ea6bc897f46ca6693235fc4
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           i3-gnome
Version:        master
Release:        0
License:        MIT
Summary:        Opinionated i3 configuration with GNOME Session integration
Url:            https://github.com/51v4n/i3-gnome
Group:          System/GUI/Other
Source0:        https://github.com/51v4n/%{name}/archive/%{version}.tar.gz
#PreReq:
#Provides:
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description

%prep
%setup -q

%build

%install
make install DESTDIR=%{buildroot} %{?_smp_mflags}

%files
%defattr(-,root,root)
# %doc CHANGELOG.md CONTRIBUTING.md LICENSE.txt README.md
%{_bindir}/i3-gnome
%{_datadir}/applications/i3-gnome.desktop
%{_datadir}/gnome-session/sessions/i3-gnome.session
%{_datadir}/xsessions/i3-gnome.desktop



# git@github.com:
