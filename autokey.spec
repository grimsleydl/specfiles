Name:               autokey
Version:            0.94.0
Release:            0
Summary:            A desktop automation utility for Linux and X11
License:            GPL-3.0
Group:              System/X11/Utilities
Source:             %{name}-%{version}.tar.gz
Url:                https://github.com/autokey-py3/autokey
BuildRequires:      python3-setuptools
BuildRequires:      python3-dbus-python
BuildRequires:      desktop-file-utils
BuildRequires:      fdupes
Requires:           wmctrl
Requires:           hicolor-icon-theme
Requires:           python3-dbus-python

%description
AutoKey-Py3 (GitHub) is a Python 3 port of AutoKey, a desktop automation utility for Linux and X11.
New features have since been added to AutoKey-Py3 after the initial porting. Read new features for details.

%prep
%setup -q

%build

%install
python3 setup.py install --root=%{buildroot} --optimize=1

desktop-file-install --delete-original          \
		     --dir %{buildroot}%{_datadir}/applications \
		     --add-category Accessibility            \
		     %{buildroot}%{_datadir}/applications/%{name}-qt.desktop

desktop-file-install --delete-original          \
		     --dir %{buildroot}%{_datadir}/applications \
		     --add-category Accessibility            \
		     %{buildroot}%{_datadir}/applications/%{name}-gtk.desktop
%fdupes

%files
%defattr(-,root,root,-)
/usr/lib/python3.6/site-packages
%{_datadir}/icons/Humanity
%{_datadir}/icons/hicolor
%{_datadir}/applications/*.desktop
%{_datadir}/kde4
%{_datadir}/icons/ubuntu-mono-light
%{_datadir}/icons/ubuntu-mono-dark
%{_datadir}/man/man1/*.gz
%{_bindir}/autokey-*
