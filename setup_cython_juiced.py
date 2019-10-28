from distutils.core import setup
from Cython.Build import cythonize
# from setuptools import Extension

# ext_modules = [
    # Extension("juiced.cythonized.carriable", ["juiced/cythonized/carriable.pyx"]),
    # Extension("juiced.cythonized.character", ["juiced/cythonized/character.pyx"])
    # Extension("juiced.cythonized.interactable", ["juiced/cythonized/interactable.pyx"]),
    # Extension("juiced.cythonized.level", ["juiced/cythonized/metadata.pyx"]),
    # Extension("juiced.cythonized.stage", ["juiced/cythonized/stage.pyx"]),
    # Extension("juiced.cythonized.metadata", ["juiced/cythonized/metadata.pyx"])
# ]

setup(
    ext_modules = cythonize(["juiced/cythonized/*.pyx"])
)
