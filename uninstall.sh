#!/bin/bash


#escalate sudo
if [[ $EUID -ne 0 ]]; then
    exec sudo "$0" "$@"
fi

sudo  rm /usr/bin/purge

rm /usr/share/zsh/site-functions/_dnf_purge
rm /usr/share/zsh/site-functions/_purge
rm  /usr/share/bash-completion/completions/purge.bash
rm /usr/share/fish/vendor_completions.d/purge.fish
rm /usr/local/bin/dnf

echo "purge plugin removed"
