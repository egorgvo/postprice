import pathlib
from setuptools import setup

HERE = pathlib.Path(__file__).parent

README = (HERE / "README.md").read_text()

setup(
    name="postprice",
    version="1.0.0",
    description="Calculates Russian Post delivery costs",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/egorgvo/postprice",
    author="Egor Gvo",
    author_email="work.egvo@ya.ru",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
    ],
    packages=["postprice"],
    install_requires=["requests==2.24.0"],
)
