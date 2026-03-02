#!/bin/bash

set -e

# get home before escalating
REAL_USER=${SUDO_USER:-$USER}
USER_HOME=$(getent passwd "$REAL_USER" | cut -d: -f6)

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

#bash completion
cat << 'EOF' >> USER_HOME/.bashrc
_dnf_wrapper() {
    local cur=${COMP_WORDS[COMP_CWORD]}
    local cmd=${COMP_WORDS[1]}

    if [[ "$cmd" == "purge" ]]; then
        local suggestions
        suggestions=$(purge __complete-programs "$cur")
        COMPREPLY=($(compgen -W "$suggestions" -- "$cur"))
    else
        _dnf
    fi
}

complete -F _dnf_wrapper dnf
EOF

mkdir -p USER_HOME/.config/fish/
#fish completion
cat << 'EOF' >> USER_HOME/.config/fish/config.fish
complete -c dnf -n "__fish_seen_subcommand_from purge" -f -a "(purge __complete-programs (commandline -ct))"
EOF

echo "purge command installed , reload shell to load it "
