# Conan rpi eepromutils

## Description

Simple Conan recipe for https://www.github.com/raspberrypi/hats

Which is a collection of tools for writing, reading and flashing raspberry pi HAT EEPROM's

* eepmake
* eepdump
* eepflash.sh

## Useage

Example conanfile.txt for consumers
```
[build_requires]
rpi_eepromutils/1.0-next

[generators]
virtualrunenv
```

Example commands
```sh
$ source activate_run.sh
$ sudo eepflash.sh -d=0 -t=24c256 -w -f=hat.eep
$ source deactivate_run.sh
```
