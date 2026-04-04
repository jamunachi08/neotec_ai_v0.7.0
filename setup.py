from setuptools import setup, find_packages

setup(
    name="neotec_ai",
    version="0.7.0",
    description="Neotec AI cross-module automation platform for Frappe ERPNext",
    author="Neotec",
    author_email="support@neotec.ai",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
)
