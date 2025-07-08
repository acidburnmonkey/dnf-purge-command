# dnf-purge-command

This is a plugin for DNF . It will call for uninstallation of the given package and seek to remove the dangling configuration files unlike the normal dnf remove <package> command . It can also be used to check and remove old configs of programs that are not currently installed. (DNF 5 does not support community plugins it has to be ran independently).

## Installation

### copr-build

```
sudo dnf copr enable acidburnmonkey/purge-command
sudo dnf install purge-command
```

### Manual Installation

```
git clone https://github.com/acidburnmonkey/dnf-purge-command.git
cd dnf-purge-command
sudo cp the-purge.py /usr/bin/purge
sudo chmod +x /usr/bin/purge
```

## Usage

Just call it from terminal

```
sudo  purge package1 package2 package3
```

Recently added support to purge same amount as arguments dnf takes

### Switch with --nuke

This will try to manually remove binaries not detected by dnf + any associated service , don't use unless you really overtaken by rage.

```
sudo purge --nuke package
```

# Donate.

<a href="https://www.buymeacoffee.com/acidburn" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/default-orange.png" alt="Buy Me A Coffee" height="41" width="174"></a>

## Monero <img src="https://www.getmonero.org/press-kit/symbols/monero-symbol-1280.png" width="60" height="60">

43Sxiso2FHsYhP7HTqZgsXa3m3uHtxHQdMeHxECqRefyazZfpGVCLVsf1gU68jxJBo1G171AC181q1BqAUaG1m554MLsspG

## Bitcon <img src="https://upload.wikimedia.org/wikipedia/commons/4/46/Bitcoin.svg" width="60" height="60">

bc1qk06cyheffclx7x434zpxjzcdl50452r9ducw0x
