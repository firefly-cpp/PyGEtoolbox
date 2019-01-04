import sys
sys.path.append('../')

from PyGEtoolbox import *

a = Process_SOFT_format("../SOFT_format/GSE10714_family.soft.gz")  # path to the raw data
a.extract_metadata()
a.print_data()
a.extract_all_samples()
