# fish completion for purge command
# /usr/share/fish/vendor_completions.d/purge.fish

function __purge_dynamic
    purge __complete-programs (commandline -ct)
end

complete -c purge -f -a "(__purge_dynamic)" -d "Executable programs"

complete -c purge -l nuke -d "Manually remove binaries and services"
complete -c purge -l help -d "Show help message"
