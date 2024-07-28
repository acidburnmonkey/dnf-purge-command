Name:           purge-command
Version:        1.2
Release:        1%{?dist}
Summary:        This is a plugin for DNF that is similar to the apt purge functionality

License:        GPLv3+
URL:            https://github.com/acidburnmonkey/dnf-purge-command 
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch
Requires:       python3.12
BuildRequires:  python3.12  

%description
This is a plugin for DNF that aims to bring the apt purge functionality
to fedora. It calls for uninstall normally , then checks for leftover files on
user's home directory

%prep
%setup -c -T -q
tar -xzf %{SOURCE0}

%build

%install
# Create the necessary directory in the build root
mkdir -p %{buildroot}/lib/python3.12/site-packages/dnf-plugins

# Copy the script to the build root directory
cp -a the-purge.py %{buildroot}/lib/python3.12/site-packages/dnf-plugins/

%files
/lib/python3.12/site-packages/dnf-plugins/the-purge.py

%changelog
* Sat Jul 27 2024  acidburnmonkey  acidburnmonkey@gmail.com - 1.0-1
- Initial package
