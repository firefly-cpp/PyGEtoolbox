import sys
sys.path.append('../')

from PyGEtoolbox import *

a = Process_SOFT_format("../SOFT_format/GSE10714_family.soft.gz")  
a.extract_metadata()

b = a.extract_gene_information()

gene = a.affy_probe_set_ID_to_gene_id_and_description('1405_i_at')

print "Gene id is: ", gene[1], " description is: ", gene[0]


