import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
     name='pyOpenAnnotate',  
     version='0.2',
     scripts=['annotate'] ,
     author="Kukil Kashyap Borgohain",
     author_email="kukilp213@gmail.com",
     description="Automated single class annotation tool using OpenCV.",
     long_description=long_description,
   long_description_content_type="text/markdown",
     url="https://github.com/kXborg/pyOpenAnnotate",
     packages=setuptools.find_packages(),
     py_modules = ['annotations'],
     install_requires=['opencv-python', 'natsort'],
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )
