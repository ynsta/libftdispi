import re
import os
import sys
import platform

from SCons.Script import *
from SCons.Script.Main import *

def InstallSharedLib(env, target, source, version):
    libname = os.path.basename(source)
    vl      = version.split('.')
    isso = (libname[-3:].lower() == '.so')

    if not isso or os.name != 'posix':
        res = env.Install(target, source)
    else:
        libfullname = libname + '.' + version
        res = env.InstallAs(os.path.join(target, libfullname), source)
        for i in range(len(vl)):
            ext = '.' + '.'.join(vl[:i] + ['so'])
            slib = libname[:-3] + ext
            lnk = os.path.join(target, slib)
            res = res + env.Command(lnk, source,
                                    'ln -sf "' + libfullname + '" "$TARGET"')
    return res

AddMethod(Environment, InstallSharedLib)

AddOption('--mingw',
          dest='mingw',
          action='store_true',
          default=False,
          help='Use MinGW32 target (cross compile on linux)')

AddOption('--debug-flags',
          dest='debug_flags',
          action='store_true',
          default=False,
          help='Activate debug compilation flags')

AddOption('--prefix',
          dest='prefix',
          type='string',
          nargs=1,
          action='store',
          metavar='PREFIX',
          default='/usr/local',
          help='Install files in PREFIX. When you run scons install,'
          ' libraries will be placed in PREFIX/lib, executables in'
          ' PREFIX/bin, and so on. The default is /usr/local if this'
          ' argument is not passed to configure. Also set PREFIX/lib'
          ' and PREFIX/include in libraries and includes lookup path')

tools   = ['packaging']
mingw   = GetOption('mingw')
ccflags = []
prefix  = []
libpath = []

if mingw:
    if sys.platform == 'win32':
        tools = ['mingw'] + tools
    else:
        tools = ['crossmingw'] + tools
else:
    tools = ['default'] + tools

if GetOption('mingw') or platform.machine() != 'x86_64':
    libdir = 'lib'
else:
    libdir = 'lib64'


if not GetOption('clean'):

    ccflags.append('-Wall')
    if GetOption('debug_flags'):
        ccflags.append('-g')
    else:
        ccflags.append('-O2')

    prefix = GetOption('prefix')

    if prefix:
        ccflags.append('-I' + os.path.join(prefix, 'include'))
        libpath.append(os.path.join(prefix, libdir))

    libpath.append(libdir)

    machine = platform.machine()
    if not machine:
        machine = 'x'+ re.sub('[^0-9]', '', platform.architecture()[0])


Export({'PREFIX'  : prefix,
        'LIBPATH' : libpath,
        'LIBDIR'  : libdir,
        'CCFLAGS' : ccflags,
        'TOOLS'   : tools,
        'MINGW'   : mingw})
