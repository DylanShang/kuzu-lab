from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

with open("kuzu_wasm/__init__.py", "r") as file:
    first_line = file.readline().strip()
    exec(first_line)
    _version = __version__  # type: ignore # noqa

setup(
    name="kuzu_wasm",
    version=_version,  # type: ignore # noqa
    description="Python wheel for kuzu_wasm",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/DylanShang/kuzu-lab",
    author="DylanShang",
    author_email="lantu.april@gmail.com",
    classifiers=[],
    keywords="jupyterlite kuzu wasm",
    packages=find_packages(exclude=["tests"]),
    include_package_data=True,
    install_requires=["pandas","networkx"]
)
