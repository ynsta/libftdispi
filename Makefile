all:
	@scons

clean:
	@scons -c


distclean:
	@scons -c distclean


doc:
	@mkdir -p share/doc
	@doxygen share/ftdispi/Doxyfile

install:
	@scons -Q install
