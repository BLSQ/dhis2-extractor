from setuptools import setup, find_packages

setup(
    name="dhis2-extractor",
    version="0.1.0",
    description="Example dhis2 extraction utility",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
    ],
    keywords="dhis2 extraction",
    url="https://github.com/BLSQ/dhis2_extractor",
    author="Pierre Vanliefland",
    author_email="pvanliefland@bluesquarehub.com",
    license="MIT",
    packages=find_packages(include=["dhis2_extractor", "dhis2_extractor.*"]),
    install_requires=[
        "click==7.*",
        "dhis2.py==2.*",
        "numpy==1.*",
        "pandas==1.*",
        "pytest==6.*",
    ],
    entry_points="""
        [console_scripts]
        dhis2_extractor=dhis2_extractor.cli
    """,
)
