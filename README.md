# Phase2MuonTDR_DarkSUSY_mH_125_mGammaD_20000
LHE files for dark SUSY samples targeting Phase2 Muon TDR MC production
 <BR>
Instructions to produce LHE files: https://github.com/cms-tamu/MuJetAnalysis_DarkSusySamples_LHE_Generation <BR>
 <BR>
Beam-energy: 7 TeV <BR>
Number of events: 50,000 <BR>
Number of files: 8 x 50,000 = 4 x 100,000 <BR>
Displacements: cTau = 0mm, 10mm, 100mm, 1000mm (100,000 event per displacement) <BR>
Seeds: 1111, 2222, 3333, 4444, 5555, 6666, 7777, 8888 <BR>
 <BR>
To change the displacement, run https://github.com/cms-tamu/MuJetAnalysis_DarkSusySamples_LHE_Generation/blob/master/replace_lifetime_in_LHE.py <BR>
<BR>

## Output LHE files (before adding displacement!): <BR>
   * 1111: DarkSUSY_mH_125_mGammaD_20000_14TeV_madgraph452_bridge224_events50k_v1.lhe (Sven) <BR>
      * https://github.com/dildick/MuJetAnalysis_DarkSusySamples_LHE_Generation/blob/master/MG_ME_V4.5.2_CompiledBackup/MG_ME_V4.5.2/BRIDGE/DarkSUSY_mH_125_mGammaD_20000_14TeV_madgraph452_bridge224_events50k_v1.lhe.tar.gz
   * 2222: DarkSUSY_mH_125_mGammaD_20000_14TeV_madgraph452_bridge224_events50k_v2.lhe (Sven) <BR>
      * https://github.com/dildick/MuJetAnalysis_DarkSusySamples_LHE_Generation/blob/master/MG_ME_V4.5.2_CompiledBackup/MG_ME_V4.5.2/BRIDGE/DarkSUSY_mH_125_mGammaD_20000_14TeV_madgraph452_bridge224_events50k_v2.lhe.tar.gz
   * 3333: DarkSUSY_mH_125_mGammaD_20000_14TeV_madgraph452_bridge224_events50k_v3.lhe (Sven) <BR>
      * https://github.com/dildick/MuJetAnalysis_DarkSusySamples_LHE_Generation/blob/master/MG_ME_V4.5.2_CompiledBackup/MG_ME_V4.5.2/BRIDGE/DarkSUSY_mH_125_mGammaD_20000_14TeV_madgraph452_bridge224_events50k_v3.lhe.tar.gz
   * 4444: DarkSUSY_mH_125_mGammaD_20000_14TeV_madgraph452_bridge224_events50k_v4.lhe (Sven) <BR>
      * https://github.com/dildick/MuJetAnalysis_DarkSusySamples_LHE_Generation/blob/master/MG_ME_V4.5.2_CompiledBackup/MG_ME_V4.5.2/BRIDGE/DarkSUSY_mH_125_mGammaD_20000_14TeV_madgraph452_bridge224_events50k_v4.lhe.tar.gz
<BR>

## output LHE file after adding displacement and each includes 100k events: <BR>
   * 1111 and 5555: ctau = 0mm <BR>
	* https://github.com/tahuang1991/Phase2MuonTDR_DarkSUSY_mH_125_mGammaD_20000/blob/master/DarkSUSY_LHE/DarkSUSY_mH_125_mGammaD_20_14TeV_cT_0_madgraph452_bridge224_events100k.lhe.tar.gz
   * 2222 and 6666: ctau = 0mm <BR>
	* https://github.com/tahuang1991/Phase2MuonTDR_DarkSUSY_mH_125_mGammaD_20000/blob/master/DarkSUSY_LHE/DarkSUSY_mH_125_mGammaD_20_14TeV_cT_10_madgraph452_bridge224_events100k.lhe.tar.gz
   * 3333 and 7777: ctau = 0mm <BR>
	* https://github.com/tahuang1991/Phase2MuonTDR_DarkSUSY_mH_125_mGammaD_20000/blob/master/DarkSUSY_LHE/DarkSUSY_mH_125_mGammaD_20_14TeV_cT_100_madgraph452_bridge224_events100k.lhe.tar.gz
   * 4444 and 8888: ctau = 0mm <BR>
	* https://github.com/tahuang1991/Phase2MuonTDR_DarkSUSY_mH_125_mGammaD_20000/blob/master/DarkSUSY_LHE/DarkSUSY_mH_125_mGammaD_20_14TeV_cT_1000_madgraph452_bridge224_events100k.lhe.tar.gz
<BR>

## validation plots for each samples: <BR>
  * ctau=0mm: https://github.com/tahuang1991/Phase2MuonTDR_DarkSUSY_mH_125_mGammaD_20000/tree/master/Validation/ctau0_all
  * ctau=10mm: https://github.com/tahuang1991/Phase2MuonTDR_DarkSUSY_mH_125_mGammaD_20000/tree/master/Validation/ctau10_all
  * ctau=100mm: https://github.com/tahuang1991/Phase2MuonTDR_DarkSUSY_mH_125_mGammaD_20000/tree/master/Validation/ctau100_all
  * ctau=1000mm: https://github.com/tahuang1991/Phase2MuonTDR_DarkSUSY_mH_125_mGammaD_20000/tree/master/Validation/ctau1000_all
	

