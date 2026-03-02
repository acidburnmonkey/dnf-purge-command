# fish completion for dnf purge subcommand
# /usr/share/fish/vendor_completions.d/dnf_purge.fish

complete -c dnf -n "__fish_seen_subcommand_from purge" -f -a "(purge __complete-programs (commandline -ct))"
