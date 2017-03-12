# Cython Example


Create a dynamic library

``` bash
g++ -dynamiclib Rectangle.cpp -o libRectangle.so
```

Run setup.py

``` python
python setup.py build_ext --inplace
```

``` bash

ipython
import Python 2.7.12 |Continuum Analytics, Inc.| (default, Jul  2 2016, 17:43:17)
Type "copyright", "credits" or "license" for more information.

IPython 5.1.0 -- An enhanced Interactive Python.
?         -> Introduction and overview of IPython's features.
%quickref -> Quick reference.
help      -> Python's own help system.
object?   -> Details about 'object', use 'object??' for extra details.

In [1]: import rect

In [2]: r = rect.PyRectangle(1, 1, 2, 2)

In [3]:

```

