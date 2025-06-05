from setuptools import setup,find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="Pediatric_Haemodynamic_Shock_Prediction",
    version="0.1",
    author="KshitijaCilbule",
    packages=find_packages(),
    install_requires = requirements,
)