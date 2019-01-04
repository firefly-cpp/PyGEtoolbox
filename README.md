# PyGEtoolbox - Gene expression toolbox in Python

## Objective


## Installation

    python setup.py install

## Features

- Downloading datasets from Gene Expression Omnibus (GEO)
- Parsing SOFT format, Affymetrix files
- Differentially Expressed genes analysis (TODO)

## CODE EXAMPLES:

```python
from PyGEtoolbox import *

#downloading GSE from GEO
series = Download()
series.download_SOFT_format("GSE105008") 

#downloading GDE from GEO
datasets = Download()
datasets.download_SOFT_format("GDS2003") 

#downloading CEL file
cel = Download()
cel.download_CEL_file("GSM270781")
```

```python
from PyGEtoolbox import *

a = Process_SOFT_format("../SOFT_format/GSE10714_family.soft.gz")  # path to the raw data
a.extract_metadata()
a.print_data()
a.extract_all_samples()
```

## Bugs

This project will be regularly updated during the 2019. Testing this package is more than welcome. 
Please report all bugs, suggestions and features that could be added.