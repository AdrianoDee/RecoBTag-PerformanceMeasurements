# RecoBTag-PerformanceMeasurements

## Software setup for CMSSW_11_1_0_pre3
* **Step #1** : create local CMSSW area and add the relevant packages.
```
cmsrel CMSSW_11_1_0_pre3
cd CMSSW_11_1_0_pre3/src
cmsenv

git cms-init

git cms-addpkg RecoBTag
git cms-addpkg RecoBTag/TensorFlow
git cms-addpkg RecoBTag/Combined

# [optional] PR#28976 (fix to realistic SIM-Clusters)
git cms-merge-topic felicepantaleo:fix_realistic_sim_clusters_11_1_0_pre3

git clone -b PrunedTraining_NoPuppi https://github.com/emilbols/RecoBTag-Combined RecoBTag/Combined/data
wget https://raw.githubusercontent.com/cms-data/RecoBTag-Combined/master/DeepCSV_PhaseII.json -P RecoBTag/Combined/data/
git clone -b PhaseIIOnline --depth 1 https://github.com/johnalison/RecoBTag-PerformanceMeasurements.git RecoBTag/PerformanceMeasurements

git clone https://github.com/missirol/JMETriggerAnalysis.git -o missirol -b phase2_devel

scram b -j8

```


* **Step #2** : generate customized configuration file to run TRK(v02)+PF+JME+BTV HLT-like reconstruction on RAW.
Already done in `RecoBTag/PerformanceMeasurements/python/hltPhase2_TRKv02_cfg`
```
cmsDriver.py step3 \
  --geometry Extended2026D49 --era Phase2C9 \
  --conditions auto:phase2_realistic_T15 \
  --processName RECO2 \
  --step RAW2DIGI,RECO \
  --eventcontent RECO \
  --datatier RECO \
  --filein /store/mc/Phase2HLTTDRWinter20DIGI/QCD_Pt-15to3000_TuneCP5_Flat_14TeV-pythia8/GEN-SIM-DIGI-RAW/PU200_castor_110X_mcRun4_realistic_v3-v2/10000/05BFAD3E-3F91-1843-ABA2-2040324C7567.root \
  --mc \
  --nThreads 4 \
  --nStreams 4 \
  --python_filename hltPhase2_TRKv02_cfg.py \
  --no_exec \
  -n 10 \
  --customise SLHCUpgradeSimulations/Configuration/aging.customise_aging_1000,Configuration/DataProcessing/Utils.addMonitoring \
  --customise JMETriggerAnalysis/Common/hltPhase2_TRKv02.customize_hltPhase2_TRKv02 \
  --customise JMETriggerAnalysis/Common/hltPhase2_JME.customize_hltPhase2_JME \
  --customise JMETriggerAnalysis/Common/hltPhase2_BTV.customize_hltPhase2_BTV \
  --customise_commands 'process.schedule.remove(process.RECOoutput_step)\ndel process.RECOoutput\ndel process.RECOoutput_step\n'
```

* **Step #3** : Run `cmsRun` with bTagHLTAnalyzer in `/test/python/PhaseII/runHLTBTagAnalyzer_PhaseII_cfg.py`
