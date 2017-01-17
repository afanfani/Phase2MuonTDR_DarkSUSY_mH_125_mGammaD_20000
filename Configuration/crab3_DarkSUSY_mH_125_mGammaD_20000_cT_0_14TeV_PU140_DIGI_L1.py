from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()
config.General.requestName = 'DarkSUSY_mH_125_mGammaD_20000_cT_0_14TeV_PU140_DIGI_L1'
config.General.workArea = 'crab_space'
config.General.transferOutputs = True
config.General.transferLogs = True
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'DigiFullPU140_2023tiltedPU.py'
config.Data.inputDataset = '/DarkSUSY_mH_125_mGammaD_20000_cT_0_14TeV_GEN_SIM_90X/dildick-DarkSUSY_mH_125_mGammaD_20000_cT_0_14TeV_GEN_SIM_90X-41486bf69d26fe6e55da7a0e23096f9b/USER'
#config.Data.secondaryInputDataset = '/MinBias_TuneCUETP8M1_14TeV-pythia8/PhaseIIFall16GS82-90X_upgrade2023_realistic_v1-v1/GEN-SIM'
config.Data.splitting = 'FileBased'
config.Data.inputDBS = 'phys03'
config.Data.unitsPerJob = 1
config.Data.outLFNDirBase = '/store/user/dildick/'
config.Data.publication = True
config.Data.outputDatasetTag = config.General.requestName
#config.Data.useParent = False
config.Site.storageSite = 'T3_US_TAMU'
