# bash completion for purge command
# /usr/share/bash-completion/completions/purge

_purge_complete() {
    local cur prev words cword
    _init_completion || return

    local out
    out="$(purge __complete-programs -- "$cur" 2>/dev/null)"
    if [[ -n $out ]]; then
        COMPREPLY=( $(compgen -W "$out" -- "$cur") )
    fi
}

complete -F _purge_complete purge
