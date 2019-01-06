import sys
sys.path.append('../')

from PyGEtoolbox import *

#downloading RAW data
raw_data = Download()
raw_data.download_RAW_data("GSE41657")
