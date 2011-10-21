# -*- python -*-

# Version is for the moment hardcoded but will be optained from vcs
version = '0.2'

# look at site_scons/site_init.py for options
Import("*") # for old version of scons (1.0.1 for example variable in
            # site_init.py are not directly visible from SConstruct so
            # Import/Export are used

# = Environment =======================================================
env = Environment(PREFIX  = PREFIX,
                  LIBPATH = LIBPATH,
                  CCFLAGS = CCFLAGS + ['-DEXPORT_DLL'],
                  tools   = TOOLS)

# = Configuration =====================================================
if not env.GetOption('clean'):
    conf = Configure(env)
    conferror = False
    for l in ['usb', 'ftdi']:
        if not conf.CheckLib(l):
            conferror = True
    if conferror:
        print 'Configure failed, exiting !'
        Exit(1)
    env = conf.Finish()

# = Compilation =======================================================
lib = env.SharedLibrary(LIBDIR + '/ftdispi', ['src/ftdispi.c'])
bin = env.Program('bin/spitest', ['src/spitest.c', 'src/ftdispi.c'])

# = Default Target ====================================================
Default(lib + bin)

# = Installation ======================================================
install = env.Install('$PREFIX/include', 'src/ftdispi.h')
for i in bin:
    install += env.Install('$PREFIX/bin', i)
for i in lib:
    install += env.InstallSharedLib('$PREFIX/'+ LIBDIR, str(i), version)
env.Alias('install', install)


# = Distclean =========================================================

env.Clean('distclean', ['.sconsign.dblite',
                        '.sconf_temp',
                        'config.log',
                        LIBDIR,
                        'bin',
                        'share/doc',
                        'share/man',
                        'src/ftdispi.os'])
