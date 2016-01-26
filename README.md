# FTDI SPI Library
## Description

This library permits to use FTDI device as a SPI master. It uses libftdi and so libusb to access to the device.

SPI Supported Modes:
 * Master Mode only
 * Chip Select IDLE state setting
 * 4 Mode settings (CPOL CPHA)
 * 4 General Purpose Outputs 

## Portability

GNU/Linux, MS Windows and potentially all OS where libusb and libftdi are ported to.
Build

The build system uses SCons (tested with SCons 1.1.0, 1.2.0 & 2.0.1)

Tested build environments:

 * Linux 32 & 64,
 * Windows MinGW,
 * Linux MinGW cross compilation (tested only with scons 2.0.1). 

Tested Devices:

 * FT4232H on the FT4232H mini module. 

## License

See the LICENSE file in the root directory of this project for licensing information.


