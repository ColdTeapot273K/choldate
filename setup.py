from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext
import numpy
from Cython.Build import cythonize

setup(
    name='choldate',
    version='0.1.0',
    py_modules=['choldate.test'],
    cmdclass = {'build_ext': build_ext},
    ext_modules = cythonize([Extension("choldate", ["choldate.pyx"],include_dirs = [numpy.get_include()])
    ]), requires=['numpy']

)
