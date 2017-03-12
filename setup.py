import os
from distutils.core import setup, Extension
from Cython.Build import cythonize

dir_name = os.path.dirname(os.path.realpath(__name__))

os.environ['CFLAGS'] = '-O3 -Wall -std=c++11 -I"{}"'.format(dir_name)
os.environ['LDFLAGS'] = '-L"{}"'.format(dir_name)

extensions = [Extension("rect",
                        sources=["rect.pyx"],
                        libraries=["Rectangle"],  # link to libRectangle.so
                        language='c++'
                        )]

setup(ext_modules=cythonize(
    extensions,
))
