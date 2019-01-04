import gzip
import sys
import urllib2
from Functions import chunk_report, chunk_read

# class for downloading series (GSE) and datasets (GDS) from GEO


class Download(object):

    def __init__(self, data):
        self.data = data

    def download_SOFT_format(self):
        if "GSE" in self.data:
            identifier = self.data + "_family.soft.gz"
            url = "ftp://ftp.ncbi.nlm.nih.gov/geo/series/" + \
                self.data[:-3] + "nnn/" + self.data + "/soft/" + identifier
        elif "GDS" in self.data:
            identifier = self.data + "_full.soft.gz"
            url = "ftp://ftp.ncbi.nlm.nih.gov/geo/datasets/" + \
                self.data[:-3] + "nnn/" + self.data + "/soft/" + identifier
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

            print("Successfully downloaded dataset: ", self.data)
        except Exception as e:
            print("Exception: ", e, " at ", url)
 
