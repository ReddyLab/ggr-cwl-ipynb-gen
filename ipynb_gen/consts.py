# ipynb Generator configuration
DATA_SOURCES_SFTP = 'sftp'
DATA_SOURCES_MISEQ = 'miseq'
DATA_SOURCES_DUKEDS = 'dukeds'
DATA_SOURCES_OTHER = 'other'
DATA_SOURCES_LOCAL = 'local'
DATA_SOURCES_GENEWIZ = 'genewiz'

DATA_SOURCES_SFTP_CORES = 16
DATA_SOURCES_GENEWIZ_SFTP_URL = 'sftp.genewiz.com'
DATA_SOURCES_SFTP_URL= 'dnaseq2.igsp.duke.edu'

data_sources = [
    DATA_SOURCES_DUKEDS,
    DATA_SOURCES_SFTP,
    DATA_SOURCES_MISEQ,
    DATA_SOURCES_OTHER,
    DATA_SOURCES_LOCAL,
    DATA_SOURCES_GENEWIZ
]
LIBRARY_TYPE_CHIP_SEQ = 'chip_seq'
LIBRARY_TYPE_RNA_SEQ = 'rna_seq'
LIBRARY_TYPE_ATAC_SEQ = 'atac_seq'
LIBRARY_TYPE_STARR_SEQ = 'starr_seq'
NOTEBOOK_BLURB = "This notebook will create all the necessary files, scripts and folders to pre-process " \
                 "the aforementioned project. Is designed to be used in a jupyter server deployed in a system running " \
                 "SLURM. The majority of the scripts and heavy-lifting processes are wrapped up in sbatch scripts." \
                 "As an end user, in order to pre-process your samples provided in the spread sheet, " \
                 "you will simply need to *run the entire notebook* (Cell > Run all) and the system should take care " \
                 "of the rest for you."


# Pipelines configuration
SOFTWARE_ROOTDIR = '/hpc/group/gersbachlab/software/cwl'
CWL_WORKFLOWS_ROOTDIR = '/hpc/group/gersbachlab/software/IGVF-cwl/v1.0'
STAR_GENOME = '/hpc/group/gersbachlab/Reference_Data/Genomes/hg38/STAR_genome_sjdbOverhang_49_novelSJDB'
SEPARATE_JSONS = True
MEM = {
    'chip_seq': 24000,
    'rna_seq': 48000,
    'atac_seq': 24000,
    'starr_seq': 32000
}
NTHREADS = {
    'chip_seq': 16,
    'rna_seq': 24,
    'atac_seq': 16,
    'starr_seq': 24
}
SEQ_ENDS = ['se', 'pe']
WITH_CONTROLS = [False, 'with-control']
STRANDNESSES = ['unstranded', 'stranded', 'revstranded']
BLACKLIST_REMOVAL = [None, 'blacklist-removal']
WITH_SJDB = True
WITH_UMIS = [None, 'umis']
SLURM_PARTITIONS = ["common"]

# Environment configuration
CONDA_ACTIVATE = '/hpc/group/gersbachlab/software/miniforge3/bin/activate'
CONTAMINATION_SCRIPT = '/data/reddylab/Darryl/GitHub/reddylab/contamination_check'  # not used
CONDA_ENVIRONMENT = '/hpc/group/gersbachlab/aeb84/mamba_envs/cwl10'
PLOT_SCRIPT = '/data/reddylab/Darryl/GitHub/reddylab/countFactors_metadata.sh'  # not used
QC_SCRIPT_DIR = '/hpc/group/gersbachlab/software/cwl/bin'
DATA_UPLOAD_SCRIPT = '/data/reddylab/Darryl/GitHub/reddylab/csv_to_mongo.py'  # not used
HOST_FOR_TUNNELED_DOWNLOAD = "Hardac-xfer.genome.duke.edu" # This will not work in DCC
ILLUMINA_BASESPACE_USER = 'Mitchell.MiSeq'
# Package constants
PACKAGE_NAME = "ipynb_gen"
