from distutils.core import setup

setup(
    name="Duolingo Sync",
    version="0.1",
    packages=["duolingo_sync"],
    license="MIT",
    long_description=open("README.md").read(),
    extras_require={"dev": ["black", "pytest", "pytest-cov"]},
)
