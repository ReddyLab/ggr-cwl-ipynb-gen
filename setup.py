#!/usr/bin/env python3
"""Description:
Setup script for ggr-cwl-ipynb-gen
IPython Notebook generator for processing genomic data from GGR project, in CWL

This code is free software; you can redistribute it and/or modify it
under the terms of the BSD License (see the file LICENSE included with
the distribution).
"""
from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

# Get the long description from the README file
long_description = (here / 'README.md').read_text(encoding='utf-8')

# Load version as VERSION environmental variable
exec(open("VERSION.py").read())

setup(
    name='ggr_cwl_ipynb_gen',
    version=VERSION,
    description='IPython notebook generator for GGR CWL processing pipelines of genomic data',
    long_description=long_description,  # Optional
    long_description_content_type='text/markdown',
    url='https://github.com/alexbarrera/ggr-cwl-ipynb-gen',
    author='Alejandro Barrera',
    author_email='alejandro.barrera@duke.edu',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering :: Bio-Informatics',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9'
    ],
    keywords='cwl, bioinformatics, development',
    scripts=[
        "ggr_cwl_ipynb_gen/ggr-cwl-ipynb-gen.py",
        "chipdb_upload/data_upload.py",
    ],
    include_package_data=True,
    py_modules=["ggr_cwl_ipynb_gen"],
    python_requires='>=2.7, <4',
    install_requires=[
        'jinja2 >=2.8',
        'nbformat >=4.0.1',
        'numpy >=1.10.4',
        'pandas >=0.17.1',
        'xlrd >=1.0.0',
        'ruamel.yaml >=0.11.11',
        'setuptools',
        'pymongo'
    ],  # Optional
    data_files=[
        ('templates', ['ggr_cwl_ipynb_gen/templates/cwl_json_gen.j2']),
        ('templates', ['ggr_cwl_ipynb_gen/templates/cwl_slurm_array_gen.j2']),
        ('templates', ['ggr_cwl_ipynb_gen/templates/data_upload.j2']),
        ('templates', ['ggr_cwl_ipynb_gen/templates/download_fastq_files.j2']),
        ('templates', ['ggr_cwl_ipynb_gen/templates/generate_plots.j2']),
        ('templates', ['ggr_cwl_ipynb_gen/templates/generate_qc_cell.j2']),
        ('templates', ['ggr_cwl_ipynb_gen/templates/merge_lanes_fastq.j2']),
        ('templates', ['ggr_cwl_ipynb_gen/templates/ungzip_fastq_files.j2']),
    ],  # Optional
    project_urls={
        'Bug Reports': 'https://github.com/alexbarrera/ggr-cwl-ipynb-gen/issues',
        'Source': 'https://github.com/alexbarrera/ggr-cwl-ipynb-gen/',
    }

)