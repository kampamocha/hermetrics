import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="hermetrics",
    version="0.1.1",
    author="kampamocha",
    author_email="diego.campos.sobrino@gmail.com",
    description="A package for string distance and similarity metrics",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kampamocha/hermetrics",
    packages=setuptools.find_packages(),
    license="MIT License",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    keywords="string metric distance similarity",
    python_requires=">=3.0",
    install_requires=['matplotlib']
)