#!/usr/bin/env python3
"""Description:
Setup script for ggr-cwl-ipynb-gen
IPython Notebook generator for processing genomic data from GGR project, in CWL

This code is free software; you can redistribute it and/or modify it
under the terms of the BSD License (see the file LICENSE included with
the distribution).
"""
import sys
if sys.version_info[0] == 2:
    sys.exit("Sorry, Python 2 is not supported anymore. Please check and old branch (pre 2021)")
from setuptools import setup, find_packages

setup(
    long_description_content_type='text/markdown',
    url='https://github.com/alexbarrera/ggr-cwl-ipynb-gen',
    keywords='cwl, bioinformatics, development',
    scripts=[
        "ggr_cwl_ipynb_gen/ggr_cwl_ipynb_gen.py",
        "chipdb_upload/data_upload.py",
    ],
    include_package_data=True,
    py_modules=["ggr_cwl_ipynb_gen"],
    python_requires='>=3.1',
    install_requires=[
        'jinja2 >=2.8',
        'nbformat >=4.0.1',
        'numpy >=1.10.4',
        'pandas >=0.17.1',
        'xlrd >=1.0.0',
        'ruamel.yaml >=0.11.11',
        'setuptools',
        'pymongo >=3.4.0'
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
    ]

)