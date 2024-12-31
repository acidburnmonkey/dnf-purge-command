Name:           purge-command
Version:        1.4
Release:        1%{?dist}
Summary:        DNF plugin adding apt purge functionality
License:        GPLv3+
URL:            https://github.com/acidburnmonkey/dnf-purge-command
Source0:        %{name}-%{version}.tar.gz
BuildArch:      noarch
Requires:       bash python3
BuildRequires:  bash python3-devel

%description
This is a plugin for DNF that aims to bring apt purge functionality to Fedora.
It calls for uninstall normally, then checks for leftover files in the user's home directory.

%prep
%setup -c -T -q
tar -xzf %{SOURCE0}

%build

%install
mkdir -p %{buildroot}/usr/bin
cp -a the-purge.py %{buildroot}/usr/bin/purge

%files
/usr/bin/purge

%changelog
* Sat Dec 30 2024 Acidburn Monkey <acidburnmonkey@gmail.com> - 1.4-1
- Initial release for Copr

