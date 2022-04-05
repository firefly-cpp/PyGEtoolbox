# PyGEtoolbox - Gene expression toolbox in Python

## Objective


## Installation

    python setup.py install

## Features

- Downloading GEO DataSets from Gene Expression Omnibus (GEO) ([see example](examples/download_SOFT_format.py))
- Downloading RAW format from GEO ([see example](examples/download_RAW_data.py))
- Downloading CEL files from GEO ([see example](examples/download_CEL_files.py))
- Parsing SOFT format ([see example](examples/parse_SOFT_format.py))
- Affymetrix probe set ID to gene id and gene description conversion ([see example](examples/affy_probe_set_id_to_gene_id.py))
- Differentially Expressed genes analysis (TODO)

## CODE EXAMPLES:

```python
from PyGEtoolbox import *

#downloading GSE from GEO
series = Download()
series.download_SOFT_format("GSE105008") 

#downloading GDS from GEO
datasets = Download()
datasets.download_SOFT_format("GDS2003") 

#downloading CEL file
cel = Download()
cel.download_CEL_file("GSM270781")

#downloading RAW data
raw_data = Download()
raw_data.download_RAW_data("GSE41657")
```

```python
from PyGEtoolbox import *

a = Process_SOFT_format("../SOFT_format/GSE10714_family.soft.gz")  # path to the data
a.extract_metadata()
a.print_data()
a.extract_all_samples()
```

## Bugs

This project will be regularly updated during the 2019. Testing this package is more than welcome. 
Please report all bugs, suggestions and features that could be added.

## References

Datasets were downloaded from Gene Expression Omnibus available at the following website: [https://www.ncbi.nlm.nih.gov/geo/](https://www.ncbi.nlm.nih.gov/geo/)

## License

This package is distributed under the BSD 2-Clause "Simplified" License.

## Disclaimer

This framework is provided as-is, and there are no guarantees that it fits your purposes or that it is bug-free. Use it at your own risk!