import pandas as pd
from DRSpy import log

class DataStruct():
    def __init__(self, filename, ftype):
        log(f"-> Creating DataFrame: {filename}")
        self.filename = filename
        # file extension
        self.ftype = ftype
        self.dtype = float
        # data ranges in file
        self.frange = {
                        "txt"   : [3, 153, 158, 308],
                        "txt_t" : [3, 154],
                        "xml" : [],
                            }
    def create_dataframe(self):
        if self.ftype == "txt":
            try:
                log("---> Converting CH0 to DataFrame: ", wait=True)
                self.ch0 = pd.read_table(self.filename, skiprows=lambda x: x not in range(self.frange["txt"][0], self.frange["txt"][1]+1), names=["D1", "D2", "N"])
                log("OK","green")
                log("---> Converting CH1 to DataFrame: ", wait=True)
                self.ch1 = pd.read_table(self.filename, skiprows=lambda x: x not in range(self.frange["txt"][2], self.frange["txt"][3]+1), names=["D1", "D2", "N"])
                log("OK","green")
            except Exception as e:
                log("---> Converting to DataFrame failed: \n{e}\n","red")
            else:
                log("---> Statistic CH0:")
                log(self.ch0.describe(),"yellow")
                log("---> Statistic CH1:")
                log(self.ch1.describe(),"yellow")
        elif self.ftype == "txt_t":
            try:
                log("---> Converting Delay to DataFrame: ", wait=True)
                self.delay = pd.read_table(self.filename, skiprows=lambda x: x not in range(self.frange["txt_t"][0], self.frange["txt_t"][1]+1), names=["D1", "D2", "N"])
                log("OK","green")
            except Exception as e:
                log("---> Converting to DataFrame failed: \n{e}\n","red")
            else:
                log("---> Statistic Delay:")
                log(self.delay.describe(),"yellow")
                
        else:
            raise TypeError(f"Unsupported file extension: {self.ftype}")
