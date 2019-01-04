import gzip
import sys
import urllib2
from Functions import chunk_report, chunk_read

# class for downloading series (GSE) and datasets (GDS) from GEO


class Download(object):

    def download_SOFT_format(self, dataset):
        if "GSE" in dataset:
            identifier = dataset + "_family.soft.gz"
            url = "ftp://ftp.ncbi.nlm.nih.gov/geo/series/" + \
                dataset[:-3] + "nnn/" + dataset + "/soft/" + identifier
        elif "GDS" in dataset:
            identifier = dataset + "_full.soft.gz"
            url = "ftp://ftp.ncbi.nlm.nih.gov/geo/datasets/" + \
                dataset[:-3] + "nnn/" + dataset + "/soft/" + identifier
        else:
            print("Unknown dataset")
            sys.exit(1)

        save_folder = "../raw_data/" + identifier

        print("Retrieving data from GEO: ")

        try:
            response = urllib2.urlopen(url)
            data = chunk_read(response, report=chunk_report)
            save_ = open(save_folder, 'w')
            save_.write(data)
            save_.close()

            print("Successfully downloaded dataset: ", dataset)
        except Exception as e:
            print("Exception: ", e, " at ", url)
 
 
    def download_CEL_file(self, sample):
        identifier = sample + ".CEL.gz"
        url = "ftp://ftp.ncbi.nlm.nih.gov/geo/samples/" + sample[:-3] + "nnn/" + sample + "/suppl/" + identifier
        
        save_folder = "../cel_data/" + identifier

        print("Retrieving CEL file from GEO: ")

        try:
            response = urllib2.urlopen(url)
            data = chunk_read(response, report=chunk_report)
            save_ = open(save_folder, 'w')
            save_.write(data)
            save_.close()

            print("Successfully downloaded CEL file: ", sample)
        except Exception as e:
            print("Exception: ", e, " at ", url)