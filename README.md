# Conan rpi eepromutils

## Description

Simple Conan recipe for https://www.github.com/raspberrypi/hats

Which is a collection of tools for writing, reading and flashing raspberry pi HAT EEPROM's

* eepmake
* eepdump
* eepflash.sh

## Build and package

The following command will build and publish the Conan package to the local system cache:

```
conan create . 1.0-next@
```

## Useage

### Standalone
```
conan install -g virtualrunenv rpi_eepromutils/1.0-next@
```
**OR**
### Example conanfile.txt for consumers
```
[build_requires]
rpi_eepromutils/1.0-next

[generators]
virtualrunenv
```
### Running commands directly
```sh
$ source activate_run.sh
$ sudo eepflash.sh -d=0 -t=24c256 -w -f=hat.eep
$ source deactivate_run.sh
```
