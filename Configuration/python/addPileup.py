import FWCore.ParameterSet.Config as cms
from Phase2MuonTDR_DarkSUSY_mH_125_mGammaD_20000.Configuration.fileNamesPU import fileNamesPU

def addPileup(process):
    process.mix.input.fileNames = fileNamesPU
    return process
