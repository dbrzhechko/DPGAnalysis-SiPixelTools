import FWCore.ParameterSet.Config as cms

process = cms.Process("MapWriter")
#process.load("CondCore.DBCommon.CondDBCommon_cfi")
#process.load("CondCore.CondDB.CondDB_cfi")
#process.load("Configuration.Geometry.GeometryExtended2017Reco_cff")
process.load('Configuration.Geometry.GeometryExtended2017NewFPixReco_cff')

process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:upgrade2017', '')
#process.GlobalTag.globaltag = autoCond['phase1_2017_design']
#process.GlobalTag = GlobalTag(process.GlobalTag, 'phase1_2017_design', '')

process.source = cms.Source("EmptyIOVSource",
    timetype = cms.string('runnumber'),
    firstValue = cms.uint64(1),
    lastValue = cms.uint64(1),
    interval = cms.uint64(1)
)

process.PoolDBOutputService = cms.Service("PoolDBOutputService",
    DBParameters = cms.PSet(
     messageLevel = cms.untracked.int32(0),
     authenticationPath = cms.untracked.string('.')
    ),
    timetype = cms.untracked.string('runnumber'),
    connect = cms.string("sqlite_file:cabling.db"),
    #process.CondDBCommon,
    toPut = cms.VPSet(cms.PSet(
        record =  cms.string('SiPixelFedCablingMapRcd'),
        tag = cms.string('SiPixelFedCablingMap_phase1_v2')
    )),
    # loadBlobStreamer = cms.untracked.bool(False)
)

process.MessageLogger = cms.Service("MessageLogger",
    debugModules = cms.untracked.vstring('*'),
    destinations = cms.untracked.vstring('log'),
    #log = cms.untracked.PSet( threshold = cms.untracked.string('DEBUG'))
    log = cms.untracked.PSet( threshold = cms.untracked.string('WARNING'))
)

process.mapwriter = cms.EDAnalyzer("SiPixelFedCablingMapWriter",
  record = cms.string('SiPixelFedCablingMapRcd'),
  fileName = cms.untracked.string('pixelToLNK.ascii_phase1_v2')
  #phase1 = cms.untracked.bool(True),
  #associator = cms.untracked.string('PixelToLNKAssociateFromAscii')
)

process.p1 = cms.Path(process.mapwriter)