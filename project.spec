Name:           purge-command
Version:        1.3
Release:        1%{?dist}
Summary:        This is a plugin for DNF that is similar to the apt purge functionality

License:        GPLv3+
URL:            https://github.com/acidburnmonkey/dnf-purge-command 
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch
Requires:       bash python3.12
BuildRequires:  bash python3.12  

%description
This is a plugin for DNF that aims to bring the apt purge functionality
to fedora. It calls for uninstall normally , then checks for leftover files on
user's home directory

%prep
%setup -c -T -q
tar -xzf %{SOURCE0}

%build

%install
# Remove any existing build root to start clean
rm -rf %{buildroot}

# Get Python 3 version
PYTHON_VERSION=$(python3 --version | awk '{print $2}' | awk -F. '{print $1"."$2}')
INSTALL_DIR="%{buildroot}/lib/python${PYTHON_VERSION}/site-packages/dnf-plugins"

# Create the necessary directory
mkdir -p ${INSTALL_DIR}

# Copy the script to the build root directory
cp -a the-purge.py ${INSTALL_DIR}/the-purge.py

%files
%defattr(-,root,root,-)
/lib/python*/site-packages/dnf-plugins/the-purge.py

%changelog
* Sat Jul 27 2024  acidburnmonkey  acidburnmonkey@gmail.com - 1.0-1
- Initial package
