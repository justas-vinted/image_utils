import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="image-utils",
    version="0.0.1",
    author="Justas",
    author_email="jst.dbr@gmail.com",
    description="Image augmentation utils",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/justas-vinted/image_utils",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)