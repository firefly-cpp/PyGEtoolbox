import gzip
import numpy as np
import pandas
import urllib

# class for downloading series from GEO

class Download(object):
    def __init__(self, series):
        self.series = series 
    
    def download(self):
        identifier = self.series + "_family.soft.gz"
        url = "ftp://ftp.ncbi.nlm.nih.gov/geo/series/" + self.series[:5] + "nnn/" + self.series + "/soft/" + identifier
        save_link = "../raw_data/" + identifier
        
        print "Retrieving data from GEO: "
        
        try:
            urllib.urlretrieve(url, save_link)
        except Exception as e :
            print "Exception: ",e," at ", url
        
        
# class for processing gene expression series from GEO

class Process_GSE_data(object):
    def __init__(self, series):
        self.GE_data = series

        self.series_title = None
        self.series_summary = None
        self.series_samples = []
        self.series_overall_design = None
        self.platform = None
        self.series_geo_accession = None

    def print_data(self):
        print self.series_title

        print self.series_summary

        print self.series_samples

        print self.series_overall_design

        print self.platform

        print self.series_geo_accession

    def save_samples(self, filename, dataset):
        folder = "../datasets/"
        path = folder + self.series_geo_accession + "/" + filename + ".pkl"
        dataset.to_pickle(path)

    def extract_metadata(self):  # extract metadata and list of samples
        with gzip.open(self.GE_data) as lines:
            for line in lines:
                if line.startswith("!Series_title"):
                    self.series_title = line.split("=")[1].strip()
                elif line.startswith("!Series_summary"):
                    self.series_summary = line.split("=")[1].strip()
                elif line.startswith("!Series_overall_design"):
                    self.series_overall_design = line.split("=")[1].strip()
                elif line.startswith("^PLATFORM"):
                    self.platform = line.split("=")[1].strip()
                elif line.startswith("!Series_sample_id"):
                    self.series_samples.append(line.split("=")[1].strip())
                elif line.startswith("!Series_geo_accession"):
                    self.series_geo_accession = line.split("=")[1].strip()

    def extract_sample_data(self):  # extract all samples
        for i in range(len(self.series_samples)):
            sample = []
            with gzip.open(self.GE_data) as lines:
                
                for line in lines:
                    search_sample = "^SAMPLE = " + str(self.series_samples[i])
                    if line.startswith(search_sample):
                        print "Processing sample: ", self.series_samples[i]

                        for line2 in lines:
                            if line2.startswith("!sample_table_begin"):
                                columns = lines.next().split("\t")
                                for line1 in lines:
                                    if line1.startswith("!sample_table_end"):
                                        break

                                    data = line1.rstrip().split("\t")
                                    sample.append(data)

                                break

            sample = np.array(sample)
            sample.flatten()

            dataset = pandas.DataFrame(
                {'ID_REF': sample[:, 0], 'VALUE': sample[:, 1], 'ABS_CALL': sample[:, 2], 'DETECTION P-VALUE': sample[:, 3]})

            # saving the dataset
            self.save_samples(self.series_samples[i], dataset)
            print "Successfully processed sample: ", self.series_samples[i]
