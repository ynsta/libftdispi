# FTDI SPI Library #

## Description ##
This library permits to use FTDI device as a SPI master.
It uses libftdi and so libusb to access to the device.
<br>
<br>

SPI Supported Modes:<br>
<ul><li>Master Mode only<br>
</li><li>Chip Select IDLE state setting<br>
</li><li>4 Mode settings (CPOL CPHA)<br>
</li><li>4 General Purpose Outputs</li></ul>

<h2>Portability</h2>
GNU/Linux, MS Windows and potentially all OS where libusb and libftdi are ported to.<br>
<br>
<h2>Build</h2>
The build system uses SCons (tested with SCons 1.1.0, 1.2.0 & 2.0.1)<br>
<br>
Tested build environments:<br>
<ul><li>Linux 32 & 64,<br>
</li><li>Windows MinGW,<br>
</li><li>Linux MinGW cross compilation (tested only with scons 2.0.1).</li></ul>

<h2>Tested Devices</h2>
<ul><li>FT4232H on the FT4232H mini module.</li></ul>

<h2>TODO</h2>
<ul><li>Improve documentation<br>
</li><li>RPM package generation with SCons<br>
</li><li>Give user the possibility to setup retry number and time