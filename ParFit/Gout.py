#!/usr/bin/env python

import sys
from Scan import DihAScan,BondScan,AnglScan
from _IO import ginp_inp

def pf_out_run(input_fname):
  
   prog_type,scan_type,gopt_s_fnameb,tup,bes=ginp_inp(input_fname)

   if scan_type=="diha":
      bes=map(int,bes)
      ds=DihAScan(None,gopt_s_fnameb,None,"mm3",None,None,None,bes,tup)
      ds=DihAScan(None,gopt_s_fnameb,None,"mm3",None,None,None,bes,tup)
      if prog_type=="nwchem":
         ds.read_nwchem_outputs()
      else:
         ds.read_gamess_outputs()
      ds.write_gouts_data()
   elif scan_type=="bond":
      bes=map(lambda x:10.*x,bes)
      bes=map(int,bes)
      ds=BondScan(None,gopt_s_fnameb,None,"mm3",None,None,None,bes,tup)
      if prog_type=="nwchem":
         ds.read_nwchem_outputs()
      else:
         ds.read_gamess_outputs()
      ds.write_gouts_data()
   elif scan_type=="angl":
      bes=map(lambda x:10.*x,bes)
      bes=map(int,bes)
      ds=AnglScan(None,gopt_s_fnameb,None,"mm3",None,None,None,bes,tup)
      if prog_type=="nwchem":
         ds.read_nwchem_outputs()
      else:
         ds.read_gamess_outputs()
      ds.write_gouts_data()

GO_input_fname="gout_inp"

lsa=len(sys.argv)
if lsa>2:
   print
   print 'Use: "./Gout.py name_of_Gout_input_file"'
   print
elif lsa==2:
   GO_input_fname=h=sys.argv[1]

pf_out_run(GO_input_fname)
