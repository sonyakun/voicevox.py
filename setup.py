from setuptools import setup, find_packages

setup(
    name="voicevox.py",
    version="1.0.0",
    author="sonyakun",
    packages=find_packages(),
    install_requires=["requests","urlib","asyncio"],
    include_package_data=True,
)