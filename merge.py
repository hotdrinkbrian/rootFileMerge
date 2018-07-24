#!/usr/bin/env python
import os, re
import multiprocessing
import logging
import commands
import math, time
import sys
from ROOT import TObject, TFile, TH1, TH1F
#from Analysis.ALPHA.samples import sample
from array import array

LUMI        =  35867#36814# in pb-1

# use the following lists to include/exclude samples to be merged

blacklist = []
whitelist = []

TIP = "./"

DEST = "./"

########## DO NOT TOUCH BELOW THIS POINT ##########

import argparse

parser = argparse.ArgumentParser(description='combine the LSF outputs into one tree')
parser.add_argument('folder', help='the folder containing the LSF output')
args = parser.parse_args()

if not os.path.exists(os.path.expandvars(args.folder)):
    print '--- ERROR ---'
    print '  \''+args.folder+'\' path not found'
    print '  please point to the correct path to the folder containing the CRAB output' 
    print '  example on NAF: '
    print TIP
    print 
    exit()

jobs = []


def hadd_singoli(name):
    os.system('hadd -f '+DEST+'QCD_HT100To200_pfc'+'.root '+name+'/*.root')
pass

subdirs = [x for x in os.listdir(args.folder) if os.path.isdir(os.path.join(args.folder, x))]
#print subdirs

#print args.folder
os.chdir(args.folder)
#print "we are here:"
#os.system('pwd')
#print "list things"
#os.system('ls')
#exit()
for l in subdirs:
    p = multiprocessing.Process(target=hadd_singoli, args=(l,))
    #jobs.append(p)
    #print p.name
    p.start()

print "Ntuples ready in ", DEST
os.system('cd '+DEST+".. ")
