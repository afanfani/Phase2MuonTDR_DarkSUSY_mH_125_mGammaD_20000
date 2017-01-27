import os

inputdir = [
    '/fdata/hepx/store/user/tahuang/MinBias_TuneCUETP8M1_14TeV-pythia8/crab_MinbiasOnly_90X_upgrade2023_Copy/170119_190734/0000/',
    '/fdata/hepx/store/user/tahuang/MinBias_TuneCUETP8M1_14TeV-pythia8/crab_MinbiasOnly_90X_upgrade2023_Copy/170119_190734/0001/',
    '/fdata/hepx/store/user/tahuang/MinBias_TuneCUETP8M1_14TeV-pythia8/crab_MinbiasOnly_90X_upgrade2023_Copy/170119_190734/0002/',
    '/fdata/hepx/store/user/tahuang/MinBias_TuneCUETP8M1_14TeV-pythia8/crab_MinbiasOnly_90X_upgrade2023_Copy/170119_190734/0003/',
    '/fdata/hepx/store/user/tahuang/MinBias_TuneCUETP8M1_14TeV-pythia8/crab_MinbiasOnly_90X_upgrade2023_Copy/170119_190734/0004/',
    '/fdata/hepx/store/user/tahuang/MinBias_TuneCUETP8M1_14TeV-pythia8/crab_MinbiasOnly_90X_upgrade2023_Copy/170119_190734/0005/',
    '/fdata/hepx/store/user/tahuang/MinBias_TuneCUETP8M1_14TeV-pythia8/crab_MinbiasOnly_90X_upgrade2023_Copy/170119_190734/0006/',
    '/fdata/hepx/store/user/tahuang/MinBias_TuneCUETP8M1_14TeV-pythia8/crab_MinbiasOnly_90X_upgrade2023_Copy/170119_190734/0007/',
    '/fdata/hepx/store/user/tahuang/MinBias_TuneCUETP8M1_14TeV-pythia8/crab_MinbiasOnly_90X_upgrade2023_Copy/170119_190734/0008/']

def getInputFiles(inputDir, onEOS = True):
    theInputFiles = []
    for d in range(len(inputDir)):
        my_dir = inputDir[d]
        if not os.path.isdir(my_dir):
            print "ERROR: This is not a valid directory: ", my_dir
            if d==len(inputDir)-1:
                print "ERROR: No input files were selected"
                exit()
            continue
        ls = os.listdir(my_dir)
        if onEOS:
            #theInputFiles.extend(['file:' + my_dir[:] + x for x in ls if x.endswith('root')])
            theInputFiles.extend([my_dir[11:] + x for x in ls if x.endswith('root')])
    return theInputFiles

inputFiles = getInputFiles(inputdir)

print inputFiles
