from distutils.core import setup, Extension

setup(name='sample',
      ext_modules=[
          Extension('sample',
                    ['pysample.c'],
                    include_dirs=['/root/sources/c_python/py_module/'],
                    define_macros=[('FOO', '1')],
                    undef_macros=['BAR'],
                    library_dirs=['/usr/local/lib', '/root/sources/c_python/py_module'],
                    libraries=['sample']
                    )
      ])