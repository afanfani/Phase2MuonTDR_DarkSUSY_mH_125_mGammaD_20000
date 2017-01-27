
cmsDriver.py GEMCode/GEMValidation/Pythia8HadronizerFilter_14TeV_cfi \
--conditions 90X_upgrade2023_realistic_v1 -n 10 \
--era Phase2C2_timing \
--eventcontent FEVTDEBUG  \
-s GEN,SIM --datatier GEN-SIM \
--beamspot HLLHC14TeV \
--filetype LHE \
--filein file:DarkSUSY_mH_125_mGammaD_20000_ctau_10_14TeV_madgraph452_bridge224_events80k.lhe \
--python_filename DarkSUSY_mH_125_mGammaD_20000_ctau_10_14TeV_madgraph452_bridge224_events80k_cfi_GEN_SIM.py \
--geometry Extended2023D4 \
--no_exec --fileout file:step1.root

cmsDriver.py GEMCode/GEMPhysics/SingleNuPt5-40_cff \
--conditions 90X_upgrade2023_realistic_v1 -n 10 \
--era Phase2C2_timing \
--eventcontent FEVTDEBUG  \
-s GEN,SIM --datatier GEN-SIM \
--beamspot HLLHC14TeV \
--python_filename SingleNu_cfi_GEN_SIM.py \
--geometry Extended2023D4 \
--no_exec --fileout file:step1.root

DIGI PU0
cmsDriver.py step2 \
--conditions 90X_upgrade2023_realistic_v1 \
-n 10 --era Phase2C2_timing \
--eventcontent FEVTDEBUGHLT \
-s DIGI:pdigi_valid,L1 \
--datatier GEN-SIM-DIGI-RAW \
--geometry Extended2023D4 \
--python DigiFullPU0_2023tiltedPU.py \
--no_exec \
--filein file:step1.root \
--fileout file:step2.root

DIGI PU140
cmsDriver.py step2 \
--conditions 90X_upgrade2023_realistic_v1 \
--pileup_input das/MinBias_TuneCUETP8M1_14TeV-pythia8/PhaseIIFall16GS82-90X_upgrade2023_realistic_v1-v1/GEN-SIM \
-n 10 --era Phase2C2_timing \
--eventcontent FEVTDEBUGHLT \
-s DIGI:pdigi_valid,L1 \
--datatier GEN-SIM-DIGI-RAW \
--pileup AVE_140_BX_25ns \
--geometry Extended2023D4 \
--python DigiFullPU140_2023tiltedPU.py \
--no_exec \
--filein file:step1.root \
--fileout file:step2.root

DIGI PU200
cmsDriver.py step2 \
--conditions 90X_upgrade2023_realistic_v1 \
--pileup_input das:/MinBias_TuneCUETP8M1_14TeV-pythia8/PhaseIIFall16GS82-90X_upgrade2023_realistic_v1-v1/GEN-SIM \
-n 10 --era Phase2C2_timing \
--eventcontent FEVTDEBUGHLT \
-s DIGI:pdigi_valid,L1 \
--datatier GEN-SIM-DIGI-RAW \
--pileup AVE_200_BX_25ns \
--geometry Extended2023D4 \
--python DigiFullPU200_2023tiltedPU.py \
--no_exec \
--filein file:step1.root \
--fileout file:step2.root
