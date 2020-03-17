import FWCore.ParameterSet.Config as cms

def customize_hltPhase2_BTV(process, name='HLTBTVSequence'):

    process.hltDeepCombinedSecondaryVertexBJetTagsPF = cms.EDProducer("DeepFlavourJetTagsProducer",
    	NNConfig = cms.FileInPath('RecoBTag/Combined/data/DeepCSV_PhaseII.json'),
    	checkSVForDefaults = cms.bool(True),
    	meanPadding = cms.bool(True),
    	src = cms.InputTag("hltDeepCombinedSecondaryVertexBJetTagsInfos"),
    	toAdd = cms.PSet(
    		probbb = cms.string('probb')
    	)
    )

    process.hltDeepCombinedSecondaryVertexBJetTagsInfos = cms.EDProducer("DeepNNTagInfoProducer",
    	computer = cms.PSet(
    		SoftLeptonFlip = cms.bool(False),
    		charmCut = cms.double(1.5),
    		correctVertexMass = cms.bool(True),
    		minimumTrackWeight = cms.double(0.5),
    		pseudoMultiplicityMin = cms.uint32(2),
    		pseudoVertexV0Filter = cms.PSet(
    			k0sMassWindow = cms.double(0.05)
    		),
    		trackFlip = cms.bool(False),
    		trackMultiplicityMin = cms.uint32(2),
    		trackPairV0Filter = cms.PSet(
    			k0sMassWindow = cms.double(0.03)
    		),
    		trackPseudoSelection = cms.PSet(
    			a_dR = cms.double(-0.001053),
    			a_pT = cms.double(0.005263),
    			b_dR = cms.double(0.6263),
    			b_pT = cms.double(0.3684),
    			jetDeltaRMax = cms.double(0.3),
    			maxDecayLen = cms.double(5),
    			maxDistToAxis = cms.double(0.07),
    			max_pT = cms.double(500),
    			max_pT_dRcut = cms.double(0.1),
    			max_pT_trackPTcut = cms.double(3),
    			min_pT = cms.double(120),
    			min_pT_dRcut = cms.double(0.5),
    			normChi2Max = cms.double(99999.9),
    			pixelHitsMin = cms.uint32(0),
    			ptMin = cms.double(0.0),
    			qualityClass = cms.string('any'),
    			sip2dSigMax = cms.double(99999.9),
    			sip2dSigMin = cms.double(2.0),
    			sip2dValMax = cms.double(99999.9),
    			sip2dValMin = cms.double(-99999.9),
    			sip3dSigMax = cms.double(99999.9),
    			sip3dSigMin = cms.double(-99999.9),
    			sip3dValMax = cms.double(99999.9),
    			sip3dValMin = cms.double(-99999.9),
    			# ~ totalHitsMin = cms.uint32(3),
    			totalHitsMin = cms.uint32(0),
    			useVariableJTA = cms.bool(False)
    		),
    		trackSelection = cms.PSet(
    			a_dR = cms.double(-0.001053),
    			a_pT = cms.double(0.005263),
    			b_dR = cms.double(0.6263),
    			b_pT = cms.double(0.3684),
    			jetDeltaRMax = cms.double(0.3),
    			maxDecayLen = cms.double(5),
    			maxDistToAxis = cms.double(0.07),
    			max_pT = cms.double(500),
    			max_pT_dRcut = cms.double(0.1),
    			max_pT_trackPTcut = cms.double(3),
    			min_pT = cms.double(120),
    			min_pT_dRcut = cms.double(0.5),
    			normChi2Max = cms.double(99999.9),
    			# ~ pixelHitsMin = cms.uint32(2),
    			pixelHitsMin = cms.uint32(0),
    			ptMin = cms.double(0.0),
    			qualityClass = cms.string('any'),
    			sip2dSigMax = cms.double(99999.9),
    			sip2dSigMin = cms.double(-99999.9),
    			sip2dValMax = cms.double(99999.9),
    			sip2dValMin = cms.double(-99999.9),
    			sip3dSigMax = cms.double(99999.9),
    			sip3dSigMin = cms.double(-99999.9),
    			sip3dValMax = cms.double(99999.9),
    			sip3dValMin = cms.double(-99999.9),
    			# ~ totalHitsMin = cms.uint32(3),
    			totalHitsMin = cms.uint32(0),
    			useVariableJTA = cms.bool(False)
    		),
    		trackSort = cms.string('sip2dSig'),
    		useTrackWeights = cms.bool(True),
    		vertexFlip = cms.bool(False)
    	),
    	svTagInfos = cms.InputTag("hltDeepSecondaryVertexTagInfosPF")
    )

    process.hltDeepSecondaryVertexTagInfosPF = cms.EDProducer("CandSecondaryVertexProducer",
    	beamSpotTag = cms.InputTag("offlineBeamSpot"),
    	constraint = cms.string('BeamSpot'),
    	extSVCollection = cms.InputTag("hltDeepInclusiveMergedVerticesPF"),
    	extSVDeltaRToJet = cms.double(0.3),
    	minimumTrackWeight = cms.double(0.5),
    	trackIPTagInfos = cms.InputTag("hltDeepBLifetimeTagInfosPF"),
    	trackSelection = cms.PSet(
    		a_dR = cms.double(-0.001053),
    		a_pT = cms.double(0.005263),
    		b_dR = cms.double(0.6263),
    		b_pT = cms.double(0.3684),
    		jetDeltaRMax = cms.double(0.3),
    		maxDecayLen = cms.double(99999.9),
    		maxDistToAxis = cms.double(0.2),
    		max_pT = cms.double(500),
    		max_pT_dRcut = cms.double(0.1),
    		max_pT_trackPTcut = cms.double(3),
    		min_pT = cms.double(120),
    		min_pT_dRcut = cms.double(0.5),
    		normChi2Max = cms.double(99999.9),
    		# ~ pixelHitsMin = cms.uint32(2),
    		pixelHitsMin = cms.uint32(1),
    		ptMin = cms.double(1.0),
    		qualityClass = cms.string('any'),
    		sip2dSigMax = cms.double(99999.9),
    		sip2dSigMin = cms.double(-99999.9),
    		sip2dValMax = cms.double(99999.9),
    		sip2dValMin = cms.double(-99999.9),
    		sip3dSigMax = cms.double(99999.9),
    		sip3dSigMin = cms.double(-99999.9),
    		sip3dValMax = cms.double(99999.9),
    		sip3dValMin = cms.double(-99999.9),
    		# ~ totalHitsMin = cms.uint32(3),
    		totalHitsMin = cms.uint32(0),
    		useVariableJTA = cms.bool(False)
    	),
    	trackSort = cms.string('sip3dSig'),
    	useExternalSV = cms.bool(True),
    	usePVError = cms.bool(True),
    	vertexCuts = cms.PSet(
    		distSig2dMax = cms.double(99999.9),
    		distSig2dMin = cms.double(2.0),
    		distSig3dMax = cms.double(99999.9),
    		distSig3dMin = cms.double(-99999.9),
    		distVal2dMax = cms.double(2.5),
    		distVal2dMin = cms.double(0.01),
    		distVal3dMax = cms.double(99999.9),
    		distVal3dMin = cms.double(-99999.9),
    		fracPV = cms.double(0.79),
    		massMax = cms.double(6.5),
    		maxDeltaRToJetAxis = cms.double(0.4),
    		minimumTrackWeight = cms.double(0.5),
    		multiplicityMin = cms.uint32(2),
    		useTrackWeights = cms.bool(True),
    		v0Filter = cms.PSet(
    			k0sMassWindow = cms.double(0.05)
    		)
    	),
    	vertexReco = cms.PSet(
    		finder = cms.string('avr'),
    		minweight = cms.double(0.5),
    		primcut = cms.double(1.8),
    		seccut = cms.double(6.0),
    		smoothing = cms.bool(False),
    		weightthreshold = cms.double(0.001)
    	),
    	vertexSelection = cms.PSet(
    		sortCriterium = cms.string('dist3dError')
    	)
    )

    process.hltDeepBLifetimeTagInfosPF = cms.EDProducer("CandIPProducer",
    	candidates = cms.InputTag("particleFlowTmp"),
    	computeGhostTrack = cms.bool(True),
    	computeProbabilities = cms.bool(True),
    	ghostTrackPriorDeltaR = cms.double(0.03),
    	jetDirectionUsingGhostTrack = cms.bool(False),
    	jetDirectionUsingTracks = cms.bool(False),
    	# ~ jets = cms.InputTag("hltPFJetForBtag"),
    	# jets = cms.InputTag("ak4PFJetsCHS"),
    	jets = cms.InputTag("hltAK4PFCHSJets"),
    	maxDeltaR = cms.double(0.4),
    	maximumChiSquared = cms.double(5.0),
    	maximumLongitudinalImpactParameter = cms.double(17.0),
    	maximumTransverseImpactParameter = cms.double(0.2),
    	# ~ minimumNumberOfHits = cms.int32(3),
    	minimumNumberOfHits = cms.int32(0),
    	# ~ minimumNumberOfPixelHits = cms.int32(2),
    	minimumNumberOfPixelHits = cms.int32(1),
    	minimumTransverseMomentum = cms.double(1.0),
    	# ~ primaryVertex = cms.InputTag("hltVerticesPFFilter"),
    	primaryVertex = cms.InputTag("offlinePrimaryVertices"),
    	useTrackQuality = cms.bool(False)
    )

    process.hltDeepInclusiveMergedVerticesPF = cms.EDProducer("CandidateVertexMerger",
    	maxFraction = cms.double(0.2),
    	minSignificance = cms.double(10.0),
    	secondaryVertices = cms.InputTag("hltDeepTrackVertexArbitratorPF")
    )



    process.hltDeepTrackVertexArbitratorPF = cms.EDProducer("CandidateVertexArbitrator",
    	beamSpot = cms.InputTag("offlineBeamSpot"),
    	dLenFraction = cms.double(0.333),
    	dRCut = cms.double(0.4),
    	distCut = cms.double(0.04),
    	fitterRatio = cms.double(0.25),
    	fitterSigmacut = cms.double(3),
    	fitterTini = cms.double(256),
    	maxTimeSignificance = cms.double(3.5),
    	# ~ primaryVertices = cms.InputTag("hltVerticesPFFilter"),
    	mightGet = cms.optional.untracked.vstring,   #new
    	primaryVertices = cms.InputTag("offlinePrimaryVertices"),
    	secondaryVertices = cms.InputTag("hltDeepInclusiveSecondaryVerticesPF"),
    	sigCut = cms.double(5),
    	trackMinLayers = cms.int32(4),
    	trackMinPixels = cms.int32(1),
    	trackMinPt = cms.double(0.4),
    	tracks = cms.InputTag("particleFlowTmp")
    )

    process.hltDeepInclusiveSecondaryVerticesPF = cms.EDProducer("CandidateVertexMerger",
    	maxFraction = cms.double(0.7),
    	minSignificance = cms.double(2),
    	secondaryVertices = cms.InputTag("hltDeepInclusiveVertexFinderPF")
    )


    process.hltDeepInclusiveVertexFinderPF = cms.EDProducer("InclusiveCandidateVertexFinder",
    	beamSpot = cms.InputTag("offlineBeamSpot"),
    	clusterizer = cms.PSet(
    		clusterMaxDistance = cms.double(0.05),
    		clusterMaxSignificance = cms.double(4.5),
    		clusterMinAngleCosine = cms.double(0.5),
    		distanceRatio = cms.double(20),
    		maxTimeSignificance = cms.double(3.5), #####new
    		seedMax3DIPSignificance = cms.double(9999),
    		seedMax3DIPValue = cms.double(9999),
    		seedMin3DIPSignificance = cms.double(1.2),
    		seedMin3DIPValue = cms.double(0.005)
    	),
    	fitterRatio = cms.double(0.25),
    	fitterSigmacut = cms.double(3),
    	fitterTini = cms.double(256),
    	maxNTracks = cms.uint32(30),
    	maximumLongitudinalImpactParameter = cms.double(0.3),
    	maximumTimeSignificance = cms.double(3),
    	mightGet = cms.optional.untracked.vstring, #####new
    	# ~ minHits = cms.uint32(8),
    	minHits = cms.uint32(0),
    	minPt = cms.double(0.8),
    	# ~ primaryVertices = cms.InputTag("hltVerticesPFFilter"),
    	primaryVertices = cms.InputTag("offlinePrimaryVertices"),
    	tracks = cms.InputTag("particleFlowTmp"),
    	useDirectVertexFitter = cms.bool(True),
    	useVertexReco = cms.bool(True),
    	vertexMinAngleCosine = cms.double(0.95),
    	vertexMinDLen2DSig = cms.double(2.5),
    	vertexMinDLenSig = cms.double(0.5),
    	vertexReco = cms.PSet(
    		finder = cms.string('avr'),
    		primcut = cms.double(1),
    		seccut = cms.double(3),
    		smoothing = cms.bool(True)
    	)
    )




    process.HLTBtagDeepCSVSequencePF = cms.Sequence(
        process.hltDeepBLifetimeTagInfosPF
        +process.hltDeepInclusiveVertexFinderPF
        +process.hltDeepInclusiveSecondaryVerticesPF
        +process.hltDeepTrackVertexArbitratorPF
        +process.hltDeepInclusiveMergedVerticesPF
        +process.hltDeepSecondaryVertexTagInfosPF
        +process.hltDeepCombinedSecondaryVertexBJetTagsInfos
        +process.hltDeepCombinedSecondaryVertexBJetTagsPF)

    return process
