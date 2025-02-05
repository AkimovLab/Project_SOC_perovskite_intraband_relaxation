from PYXAID2 import *
import os

nsteps_per_job = 750
tot_nsteps = 3000

# Step 1 - split MD trajectory on the time steps
# Provide files listed below: "x.md.out" and "x.scf.in"
# IMPORTANT: 
# 1) use only ABSOLUTE path for PP in x.scf.in file
# 2) provided input file is just a template, so do not include coordinates
xdatcar2inp.xdatcar2inp("XDATCAR","x0.scf.in","wd","x0.scf",0,tot_nsteps,1)  # neutral setup
#out2inp.out2inp("x.md.out","x1.scf.in","wd","x1.scf",0,tot_nsteps,1)  # charged setup


# Step 2 - distribute all time steps into groups(jobs) 
# several time steps per group - this is to accelerate calculations
# creates a "customized" submit file for each job and submit it - run
# a swarm in independent calculations (trajectory pieces)
# (HTC paradigm)
# Provide the files below: 
# submit_templ.pbs - template for submit files - manually edit the variables
# x.exp.in - file for export of the wavefunction

os.system("cp submit_templ.pbs wd")
os.system("cp x0.exp.in wd")
#os.system("cp x1.exp.in wd")
os.chdir("wd")
distribute.distribute(0,tot_nsteps,nsteps_per_job,"submit_templ.pbs",["x0.exp.in"],["x0.scf"],1) # 1 = PBS, 2 = SLURM, 0 = no run
#distribute.distribute(0,tot_nsteps,nsteps_per_job,"submit_templ.pbs",["x0.exp.in","x1.exp.in"],["x0.scf","x1.scf"],1)



