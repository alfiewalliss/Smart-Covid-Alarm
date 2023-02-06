import setuptools
with open("docs/READ_ME.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="smart_alarm_pkg-A-Walliss", # Replace with your own username
    version="0.0.1",
    author="Alfie Walliss",
    author_email="aw840@exeter.ac.uk",
    description="A smart alarm that gives weather and news insites along with corona virus stats",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/alfiewalliss/smart_alarm_pkg-A-Walliss/tree/main",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache-2.0",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)