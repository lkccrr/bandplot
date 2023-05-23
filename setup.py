from setuptools import setup, find_packages
from bandplot import __version__

setup(
    name='bandplot',
    version=__version__,
    author='kan',
    author_email='luokan@hrbeu.edu.cn',
    python_requires='>=3.6',
    license='MIT',
    license_files=('LICENSE'),
    platforms=['Unix', 'Windows'],
    keywords='DFT VASP DOS band plot Phonon',
    description='Band structure, DOS or phonon band structure plot from vaspkit or phonopy result.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/lkccrr/bandplot',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12'
    ],
    install_requires=[
        'numpy>=1.22.0',
        'matplotlib>=3.4.0'
    ],
    entry_points={
        'console_scripts': ['bandplot  = bandplot.wrapper:main',
                            'pbandplot = bandplot.wrapper:pmain'
                           ]
    },
    packages=find_packages(),
    include_package_data=True
)

