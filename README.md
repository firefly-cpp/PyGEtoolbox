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
series = Download("GSE105008")
series.download_SOFT_format() 

#downloading GDE from GEO
datasets = Download("GDS2003")
datasets.download_SOFT_format() 
```

```python
from PyGEtoolbox import *

a = Process_SOFT_format("../raw_data/GSE10714_family.soft.gz")  # path to the raw data
a.extract_metadata()
a.print_data()
a.extract_all_samples()
```

## Bugs

This project will be regularly updated during the 2019. Testing this package is more than welcome. 
Please report all bugs, suggestions and features that could be added.