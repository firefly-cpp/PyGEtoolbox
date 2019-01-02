import sys
sys.path.append('../')

from PyGEtoolbox import *

a = Process_GSE_data("../raw_data/GSE10714_family.soft.gz")  # path to the raw data
a.extract_metadata()
a.print_data()
a.extract_sample_data()
