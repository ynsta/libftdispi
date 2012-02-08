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

archive:
	@T=`git tag -l | tail -n 1`; git archive --format=tar --prefix=$(PROJECT)-$$T/ $$T | bzip2 > ../$(PROJECT)-$$T.tar.bz2
