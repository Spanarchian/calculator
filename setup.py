import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
     name='calculator-pkg-spanarchian',
     version='0.0.2',
     author="Spanarchian",
     author_email="spanarchian@gmail.com",
     description="A calculator utility package",
     long_description=long_description,
     slong_description_content_type="text/markdown",
     url="https://github.com/javatechy/dokr",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )
