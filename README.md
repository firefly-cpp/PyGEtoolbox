# PyGEtoolbox - Gene expression toolbox in Python

## Objective


## Installation

    python setup.py install

## Features

- Downloading datasets from Gene Expression Omnibus (GEO)
- Parsing Affymetrix files
- Differentially Expressed genes analysis (TODO)

## CODE EXAMPLES:

```python
from PyGEtoolbox import *

#downloading GSE from GEO
series = Download("GSE105008")
series.download() 

#downloading GDE from GEO
datasets = Download("GDS2003")
datasets.download() 
```

```python
from PyGEtoolbox import *

a = Process_GSE_data("../raw_data/GSE10714_family.soft.gz")  # path to the raw data
a.extract_metadata()
a.print_data()
a.extract_sample_data()
```

## Bugs

This project will be regularly updated during the 2019. Testing this package is more than welcome. 
Please report all bugs, suggestions and features that could be added.