#!/bin/bash

# wrapper
if [[ "$1" == "purge" ]]; then
    /usr/bin/purge "${@:2}"
else
    /usr/bin/dnf "$@"
fi
