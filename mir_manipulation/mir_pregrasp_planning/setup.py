#!/usr/bin/env python
"""
//TODO
"""
from distutils.core import setup

from catkin_pkg.python_setup import generate_distutils_setup

DIST_UTILS_OBJ = generate_distutils_setup(
    packages=["mir_pregrasp_planning_ros"],
    package_dir={"mir_pregrasp_planning_ros": "ros/src/mir_pregrasp_planning_ros"},
)

setup(**DIST_UTILS_OBJ)
