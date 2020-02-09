import setuptools

requirements = ["click >= 7.0", "Pillow >= 7.0.0"]
dev_requirements = ["black >= 19.10b0", "pre-commit >= 1.20.0"]
test_requirements = ["pytest >= 5.2.4", "pytest-cov >= 2.8.1", "pytest-mock >= 2.0.0"]

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="embroidery",
    version="0.0.1",
    author="Gustavo Barbosa",
    author_email="gustavocsb@gmail.com",
    description="Embroider build variants to your mobile app icon",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/barbosa/embroidery",
    packages=setuptools.find_packages(),
    install_requires=requirements,
    extras_require={"dev": dev_requirements, "test": test_requirements},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points="""
        [console_scripts]
        embroidery = embroidery:embroidery
    """,
    zip_safe=False,
    include_package_data=True,
)
