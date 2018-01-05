# Created by pyp2rpm-3.3.0
%global pypi_name rivalcfg

Name:           python-%{pypi_name}
Version:        2.6.0
Release:        1%{?dist}
Summary:        Configure SteelSeries Rival gaming mice

License:        WTFPL
URL:            https://github.com/flozz/rivalcfg
Source0:        https://files.pythonhosted.org/packages/source/r/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
# BuildRequires:  python3dist(setuptools)

%description
rivalcfg: Configure SteelSeries Rival gaming mice

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

# Requires:       python3dist(pyudev) >= 0.19.0
# Requires:       python3dist(setuptools)
%description -n python3-%{pypi_name}
rivalcfg: Configure SteelSeries Rival gaming mice

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%doc README.md README.rst
%{_bindir}/rivalcfg
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%changelog
* Fri Dec 29 2017 grimsleydl <grimsleydl@gmail.com> - 2.6.0-1
- Initial package.
