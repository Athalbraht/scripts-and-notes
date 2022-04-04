import pandas as pd
import matplotlib.pyplot as plt
from DRSpy.main import log, click

import  matplotlib
matplotlib.use("Agg")
import  matplotlib.pyplot as plt

from scipy.optimize import curve_fit

class DataStruct():
    """
        DataStruct class
    """

    def __init__(self, fPtP=[], fdelay=[], fxml=[], fadecode=False, fverbose=False):
        self._data = pd.DataFrame({"Channel":[], "ChannelX":[], "Delay [ns]":[], "DelayX":[]})
        # row cuts for files
        self.cuts = {
                        "PtP-CH0"   : [3, 153],
                        "PtP-CH1"   : [158, 308],
                        "Delay"     : [3, 154]}
        self._fPtP, self._fdelay, self._fxml = fPtP, fdelay, fxml
        self._fadecode, self._fverbose = fadecode, fverbose
        log(f"-> Creating DataFrame: ")
        if self._fverbose: log("---> Verbose mode: ", wait=True); log("Enabled", "green")
        log(f"---> Filename autodecode: ", wait=True); log("Enabled", "green") if fadecode else log("Disabled", "red")
        log(f"---> Peak-to-Peak files to load: ", wait=True); log(f"{len(fPtP)}","green")
        log(f"---> Time delay files to load: ", wait=True); log(f"{len(fdelay)}","green")
        log(f"---> Waveform files to load: ", wait=True); log(f"{len(fdelay)}","green")
        log(f"---> Cuts: ", wait=True); log(f"{self.cuts}","green")

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, ns):
        try:
            if self._fverbose: log("---> Updating DataFrame: ", wait=True)
            self._data = pd.merge(self._data, ns, on=list(ns.columns[0:2]),  how="outer")
        except Exception as e:
            log(f"\n---> Updating DF Failed {e}")
        else:
            if self._fverbose: log("Done", "green")

    def _autodecode(self):
        try:
            log("---> Trying to decode filenames: ", wait=True)
        except Exception as e:
            log(f"\n---> Failed to decode filenames {e}", "red")
        else:
            log("Pass", "green")

    def initialize(self, fPtP=True, fdelay=True, fxml=True):
        if self._fadecode: self._autodecode()
        if fPtP:
            with click.progressbar(self._fPtP, label="---> Loading Peak2Peak files: ") as bar:
                for file in bar: self.load_file(file, "PtP")
            log("Done", "green")
        if fdelay:
            with click.progressbar(self._fdelay, label="---> Loading Delay files: ") as bar:
                for file in bar: self.load_file(file, "delay")
            log("Done", "green")
        if fxml:
            pass

    def load_file(self, filename, ftype):
        if ftype == "PtP":
            try:
                if self._fverbose: log("---> Converting (CH0, CH1) to DataFrame: ", wait=True)
                ch0 = pd.read_table(    filename,
                                        skiprows=lambda x: x not in range(self.cuts["PtP-CH0"][0], self.cuts["PtP-CH0"][1]+1),
                                        names=["Channel", "ChannelX", f"{filename[:-4]}-CH0_Counts"])
                if self._fverbose: log("(Done, ","green", wait=True)
                ch1 = pd.read_table(    filename,
                                        skiprows=lambda x: x not in range(self.cuts["PtP-CH1"][0], self.cuts["PtP-CH1"][1]+1),
                                        names=["Channel", "ChannelX", f"{filename[:-4]}-CH1_Counts"])
                if self._fverbose: log("Done), ","green", wait=True)
                log("  ", wait=True)
                ch01 = pd.merge(ch0,ch1, on=["Channel", "ChannelX"], how="outer")
                if self._fverbose: log("MERGED","green")

            except Exception as e:
                log(f"\n---> Converting to DataFrame failed: {e}","red")
                return False
            else:
                self.data = ch01
                return True
        elif ftype == "delay":
            try:
                if self._fverbose: log("---> Converting Delay to DataFrame: ", wait=True)
                _delay = pd.read_table( filename,
                                        skiprows=lambda x: x not in range(self.cuts["Delay"][0], self.cuts["Delay"][1]+1),
                                        names=["Delay [ns]", "DelayX", f"{filename[:-4]}-Delay_Counts"])
                if self._fverbose: log("Done","green")
            except Exception as e:
                log(f"\n---> Converting to DataFrame failed: {e}","red")
            else:
                self.data = _delay
                return True
        else:
            raise TypeError(f"Unsupported file extension: {ftype}")
            return False
        
