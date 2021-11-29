"""Set up files
"""

import setuptools

setuptools.setup(name="dipole",
	version = "1.0.0",
	description = "Calculations of dipole axis, dipole poles, and dipole tilt angle",
	author = "Laundal, K.M, packaged by Day, E.K",
	url = "https://github.com/ellioday/dipole",
	packages = setuptools.find_packages(exclude=["test"]),
	classifiers = ["Programming Language :: Python :: 3",
	],
	python_requires=">=3.6",
	install_requires=["numpy", "pandas"],
)
