#
# spec file for package libtorrent-rasterbar
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


%define _name   libtorrent
%define sover   9
%define _version RC_1_1
%bcond_with     examples
%bcond_with     tests
Name:           libtorrent-rasterbar
Version:        RC_1_1
Release:        0
Summary:        Libtorrent is a C++ implementation of the BitTorrent protocol
License:        BSD-3-Clause
Group:          Development/Libraries/C and C++
Url:            http://libtorrent.org/
Source:         https://github.com/arvidn/%{_name}/archive/%{name}-%{version}.tar.gz
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  python-devel
BuildRequires:  pkgconfig(openssl)
%if 0%{?suse_version} > 1320
BuildRequires:  libboost_chrono-devel
BuildRequires:  libboost_python-devel
BuildRequires:  libboost_python3-devel
BuildRequires:  libboost_random-devel
BuildRequires:  libboost_system-devel
BuildRequires:  python3-devel
%else
BuildRequires:  boost-devel >= 1.54
# For quadmath.h we need gcc-fortran on openSUSE Leap 14.x and older.
BuildRequires:  gcc-fortran
%endif

%description
libtorrent-rasterbar is a C++ library that aims to be a good
alternative to all the other bittorrent implementations around.
It is a library and not a full featured client, although it comes
with a working example client.

The main goals of libtorrent-rasterbar are:
 * To be cpu efficient.
 * To be memory efficient.
 * To be very easy to use.

This package holds the sample client and example files for
libtorrent-rasterbar.

%package -n %{name}%{sover}
Summary:        Libtorrent is a C++ implementation of the BitTorrent protocol
Group:          System/Libraries

%description -n %{name}%{sover}
libtorrent-rasterbar is a C++ library that aims to be a good
alternative to all the other bittorrent implementations around.
It is a library and not a full featured client, although it comes
with a working example client.

The main goals of libtorrent-rasterbar are:
 * To be cpu efficient.
 * To be memory efficient.
 * To be very easy to use.

%package -n python2-%{name}
Summary:        Python Bindings for libtorrent-rasterbar
# python-libtorrent-rasterbar was last used in openSUSE Leap 14.2.
Group:          Development/Libraries/Python
Provides:       python-%{name} = %{version}
Obsoletes:      python-%{name} < %{version}

%description -n python2-%{name}
Python Bindings for the libtorrent-rasterbar package.

%if 0%{?suse_version} > 1320
%package -n python3-%{name}
Summary:        Python Bindings for libtorrent-rasterbar
Group:          Development/Libraries/Python

%description -n python3-%{name}
Python Bindings for the libtorrent-rasterbar package.
%endif

%if %{with examples}
%package tools
Summary:        Example tools from libtorrent-rasterbar
Group:          Development/Libraries/C and C++

%description tools
Example tools from the libtorrent-rasterbar package.
%endif

%package devel
Summary:        Libtorrent is a C++ implementation of the BitTorrent protocol
Group:          Development/Libraries/C and C++
Requires:       %{name}%{sover} = %{version}
Requires:       gcc-c++
Requires:       pkgconfig(openssl)
%if 0%{?suse_version} > 1320
Requires:       libboost_headers-devel
%else
Requires:       boost-devel >= 1.54
%endif

%description devel
libtorrent-rasterbar is a C++ library that aims to be a good
alternative to all the other bittorrent implementations around.
It is a library and not a full featured client, although it comes
with a working example client.

The main goals of libtorrent-rasterbar are:
 * To be cpu efficient.
 * To be memory efficient.
 * To be very easy to use.

This package holds the development files for libtorrent-rasterbar.

%package doc
Summary:        Documentation for libtorrent-rasterbar
Group:          Documentation/HTML

%description doc
Documentation for the libtorrent-rasterbar package.

%prep
%setup -n %{_name}-%{version}

%build
export CFLAGS="%{optflags} -fno-strict-aliasing"
export CXXFLAGS="$CFLAGS"
%if 0%{?suse_version} <= 1320
export CXXFLAGS="$CXXFLAGS -std=c++11"
%ifarch aarch64
# Some architectures require explicit linkage to libboost_atomic on boost 1.55 and older.
export LIBS="$LIBS -lboost_atomic"
%endif
%endif

%global _configure ../configure
%if 0%{?suse_version} > 1320
for py in python python3; do
%else
for py in python; do
%endif
    mkdir -p "build-$py"
    pushd "build-$py"
    export PYTHON="$py"
    %configure \
      --disable-static                \
      --disable-silent-rules          \
      --with-libiconv                 \
%if %{with tests}
      --enable-tests                  \
%endif
%if %{with examples}
      --enable-examples               \
%endif
      --with-boost-python="boost_$py" \
      --enable-python-binding
    make %{?_smp_mflags} V=1
    popd
done

%install
%make_install -C build-python
%if 0%{?suse_version} > 1320
%make_install -C build-python3
%endif

find %{buildroot} -type f -name "*.la" -delete -print
# Move doc to a separate package.
mkdir -p %{buildroot}%{_docdir}/%{name}/
cp -r docs/* %{buildroot}%{_docdir}/%{name}/

%if %{with examples}
# Drop tests binaries from the libtorrent-rasterbar-tools subpackage.
rm -v %{buildroot}%{_bindir}/{client_test,connection_tester,enum_if} \
  %{buildroot}%{_bindir}/{fragmentation_test,parse_hash_fails} \
  %{buildroot}%{_bindir}/{parse_request_log,rss_reader,upnp_test,utp_test}
%endif

%if %{with tests}
%check
make check %{?_smp_mflags} V=1 -C build-python
%if 0%{?suse_version} > 1320
make check %{?_smp_mflags} V=1 -C build-python3
%endif
%endif

%post -n %{name}%{sover} -p /sbin/ldconfig

%postun -n %{name}%{sover} -p /sbin/ldconfig

%if %{with examples}
%files tools
%{_bindir}/dump_torrent
%{_bindir}/make_torrent
%{_bindir}/simple_client
%endif

%files -n %{name}%{sover}
%doc AUTHORS ChangeLog COPYING
%{_libdir}/%{name}.so.%{sover}*

%files -n python2-%{name}
%{python_sitearch}/%{_name}*.so
%{python_sitearch}/python_%{_name}-*

%if 0%{?suse_version} > 1320
%files -n python3-%{name}
%{python3_sitearch}/%{_name}*.so
%{python3_sitearch}/python_%{_name}-*
%endif

%files devel
%{_includedir}/%{_name}/
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

%files doc
%doc %{_docdir}/%{name}/

%changelog
