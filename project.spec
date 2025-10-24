Name:           purge-command
Version:        2.6
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
install -Dm755 the-purge.py %{buildroot}%{_bindir}/purge

install -Dm644 completions/_purge-command \
  %{buildroot}%{_datadir}/zsh/site-functions/_purge-command

install -Dm644 completions/purge.bash \
  %{buildroot}%{_datadir}/bash-completion/completions/purge

install -Dm644 completions/purge.fish \
  %{buildroot}%{_datadir}/fish/vendor_completions.d/purge.fish

%files
%{_bindir}/purge
%{_datadir}/zsh/site-functions/_purge-command
%{_datadir}/bash-completion/completions/purge
%{_datadir}/fish/vendor_completions.d/purge.fish

%changelog
* %(date "+%a %b %d %Y") Acidburn Monkey <acidburnmonkey@gmail.com> - %{version}-%{release}
- added auto completion , also fixed version 1.5 -> 2.6

