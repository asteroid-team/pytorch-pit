from setuptools import setup, find_packages

version = "0.0.1"

with open("README.md", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="torch_pit",
    version=version,
    author="Manuel Pariente",
    author_email="manuel.pariente@loria.fr",
    url="https://github.com/asteroid-team/pytorch-pit",
    description="Permutation invariant training in PyTorch made easy.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT",
    python_requires=">=3.6",
    install_requires=[
        "scipy",
        "torch",
    ],
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
