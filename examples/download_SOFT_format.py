import sys
sys.path.append('../')

from PyGEtoolbox import *

#downloading GSE from GEO
series = Download()
series.download_SOFT_format("GSE105008") 

#downloading GDE from GEO
datasets = Download()
datasets.download_SOFT_format("GDS2003") 


