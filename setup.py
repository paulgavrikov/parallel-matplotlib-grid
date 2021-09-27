import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="parallelplot",
    version="0.0.4",
    author="Paul Gavrikov",
    author_email="paul.gavrikov@hs-offenburg.de",
    description="Parallel plotting of matplotlib subplots.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/paulgavrikov/parallel-matplolib-grid",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "matplotlib",
        "pillow",
        "numpy"
    ],
    python_requires=">=3.6"
)
