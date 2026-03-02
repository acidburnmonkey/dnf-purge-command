#!/bin/bash

set -e

#escalate sudo
if [[ $EUID -ne 0 ]]; then
    exec sudo "$0" "$@"
fi

sudo cp the-purge.py /usr/bin/purge
sudo chmod +x /usr/bin/purge

## add completions
mkdir -p /usr/share/zsh/site-functions/
cp completions/_purge /usr/share/zsh/site-functions/
cp completions/_dnf_purge /usr/share/zsh/site-functions/
sudo chmod +x /usr/share/bash-completion/completions/_dnf_purge
sudo chmod +x /usr/share/bash-completion/completions/_purge

mkdir -p /usr/share/bash-completion/completions/
cp completions/purge.bash /usr/share/bash-completion/completions/
sudo chmod +x /usr/share/bash-completion/completions/purge.bash

mkdir -p /usr/share/fish/vendor_completions.d/
cp completions/purge.fish /usr/share/fish/vendor_completions.d/
sudo chmod +x /usr/share/fish/vendor_completions.d/purge.fish

#wrapper
cat << 'EOF' > /usr/local/bin/dnf
#!/bin/bash

# wrapper
if [[ "$1" == "purge" ]]; then
    /usr/bin/purge "${@:2}"
else
    /usr/bin/dnf "$@"
fi

EOF

sudo chmod +x  /usr/local/bin/dnf

echo "purge command installed , reload shell to load it "
