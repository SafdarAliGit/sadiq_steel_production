from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in sadiq_steel_production/__init__.py
from sadiq_steel_production import __version__ as version

setup(
	name="sadiq_steel_production",
	version=version,
	description="Sadiq Steel Production",
	author="VUT",
	author_email="safdar211@gamil.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
