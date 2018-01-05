#
# spec file for package fsearch
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


Name:           fsearch
Version:        master
Release:        1%{?dist}
Summary:        Fast file search utility inspired by Everything Search Engine
License:        GPL-2.0
Group:          Productivity/File utilities
Url:            https://github.com/cboxdoerfer/fsearch
Source0:        %{name}-%{version}.tar.gz
BuildRequires:  autoconf automake libtool glib2-devel intltool autoconf-archive gtk3-devel update-desktop-files
Requires:       gtk3
BuildRoot:      %{_tmppath}/%{name}-%{version}-build


%description
FSearch is a fast file search utility for GNU/Linux operating systems, inspired by Everything Search Engine.

%prep
%setup -q

%build
./autogen.sh
%configure
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}
%find_lang %{name}
%suse_update_desktop_file -r %{name} %{name} System Filesystem

%files -f %{name}.lang
%defattr(-,root,root,-)
%doc README* License
%{_datadir}/applications/fsearch.desktop
%{_datadir}/locale/de/LC_MESSAGES/fsearch.mo
/usr/bin/fsearch

%changelog
#noop


