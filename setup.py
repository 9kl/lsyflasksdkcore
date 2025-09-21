from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    install_requires = [line.strip() for line in fh.readlines() if line.strip() and not line.startswith("#")]

with open("LICENSE", "r", encoding="utf-8") as fh:
    license_text = fh.read()

setup(
    name="lsyflasksdkcore",
    version="1.0.0",
    author="fhp",
    author_email="chinafengheping@outlook.com",
    description="领数云flask SDK核心库（https://github.com/9kl/lsyflasksdkcore）",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/9kl/lsyflasksdkcore",
    packages=find_packages(),
    license=license_text,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    install_requires=install_requires,
)
