lfrom distutils.core import setup
from catkin_pkg.python_setup import generate_distutils_setup

d = generate_distutils_setup(
	scripts=['scripts/srf_08_rangefinder_node.py']
)

setup(**d)
