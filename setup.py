from os import path

import setuptools

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setuptools.setup(
    name="jupyter-juicefs-proxy",
    version="0.1.0",
    url="https://github.com/TerenceLiu98/jupyter-juicefs-proxy",
    author="Terence Junjie LIU",
    description="me@cklau.cc",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
    ],
    install_requires=["jupyter-server-proxy>=1.5.0"],
    entry_points={
        "jupyter_serverproxy_servers": [
            "juicefs = jupyter_juicefs_proxy:setup_juicefs",
        ]
    },
    package_data={
        "jupyter_juicefs_proxy": ["icons/juicefs.svg"],
    },
)
