# dnf-purge-command
This is a plugin for DNF . It will call for uninstallation of the given package and seek to remove the dangling configuration files unlike the normal  dnf remove <package>  command .  It can also be used to check and remove old configs of programs that are not currently installed.

## ⚠️ Warnig currently not working with dnf5

Am working on porting it but the plugging creation tool are bugged https://github.com/rpm-software-management/dnf5/issues/1913#issuecomment-2539206186


## Installation 
### copr-build
```
sudo dnf copr enable acidburnmonkey/purge-command
sudo dnf install purge-command
```
### Manual Installation
Simply copy the-purge.py into your current version of python. For example current version : /lib/python3.12/site-packages/dnf-plugins.

check by using ``` python3 --version ```

> or follow this commands
```
	git clone https://github.com/acidburnmonkey/dnf-purge-command.git
	cd dnf-purge-command
	sudo cp the-purge.py /lib/python3.12/site-packages/dnf-plugins
``` 

## Usage
Just call it from terminal 
```
sudo dnf purge package1 package2 package3
```
Recently added support to purge same amout as arguments dnf takes 

### Switch with --nuke
This will try to manually remove binaries not detected by dnf + any associated service , dont use unless you realy overtaken by rage.
```
sudo dnf purge --nuke package
```


# Donate.
<a href="https://www.buymeacoffee.com/acidburn" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/default-orange.png" alt="Buy Me A Coffee" height="41" width="174"></a>

## Monero <img src="https://www.getmonero.org/press-kit/symbols/monero-symbol-1280.png" width="60" height="60">
<img src="https://lh3.googleusercontent.com/pw/AJFCJaXk5yBCwXdQRjlyJfkain1Y_VNRaQLrBOzpd-TGANvD6uetoA134EINH1czVS-RpkwnFn2DspjRivfV2kPuTsN5f1NzJjyoT6rl7hhCfIJI7HyUnclACO24NKyyEES5Uly6lmvfig7G3vTH0Sx3Djw=w240-h240-s-no?authuser=0" width="150" height="150">

43Sxiso2FHsYhP7HTqZgsXa3m3uHtxHQdMeHxECqRefyazZfpGVCLVsf1gU68jxJBo1G171AC181q1BqAUaG1m554MLsspG


## Bitcon <img src="https://upload.wikimedia.org/wikipedia/commons/4/46/Bitcoin.svg" width="60" height="60">
<img src="https://lh3.googleusercontent.com/pw/AJFCJaVUsxqiheJBMWH1azt3kO00SdVw-hnJ8brWx1RNf-JozK_yy2-ZXwLpCEDeKePfp78I5Ca63I3A0TWujiMqydrdygMsmujaOvNp-OqZUwafXyleDKbD-enEg75WweataJivtVJmCenNvuIpBzq51mc=w352-h355-s-no?authuser=0" width="150" height="150">

bc1qk06cyheffclx7x434zpxjzcdl50452r9ducw0x


