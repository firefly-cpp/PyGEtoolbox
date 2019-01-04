import sys
sys.path.append('../')

from PyGEtoolbox import *

#downloading GSE from GEO
series = Download("GSE105008")
series.download_SOFT_format() 

#downloading GDE from GEO
datasets = Download("GDS2003")
datasets.download_SOFT_format() 


