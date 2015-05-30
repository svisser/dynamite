from setuptools import find_packages, setup


setup(
    name='dynamite',
    version='0.0.1',
    description='Python DNS server',
    url='https://github.com/svisser/dynamite',
    author='Simeon Visser',
    author_email='simeonvisser@gmail.com',
    license='Apache2',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Internet :: Name Service (DNS)',
    ],
)
