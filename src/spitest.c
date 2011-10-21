#include <stdio.h>
#include "ftdispi.h"

int main(int argc, char **argv)
{
	struct ftdi_context fc;
	struct ftdispi_context fsc;
	int i;

	if (ftdi_init(&fc) < 0) {
		fprintf(stderr, "ftdi_init failed\n");
		return 1;
	}
	i = ftdi_usb_open(&fc, 0x0403, 0x6011);
	if (i < 0 && i != -5) {
		fprintf(stderr, "OPEN: %s\n", ftdi_get_error_string(&fc));
		exit(-1);
	}
	ftdispi_open(&fsc, &fc, INTERFACE_A);
	ftdispi_setmode(&fsc, 1, 0, 0, 0, 0, 0);
	ftdispi_setclock(&fsc, 200000);
	ftdispi_setloopback(&fsc, 0);
	ftdispi_write(&fsc, "Test", 4, 0);
	ftdispi_close(&fsc, 1);
	return 0;
}
