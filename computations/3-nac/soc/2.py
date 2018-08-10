import math
import string

nsteps = range(0,2999)

energy_file=open("coupling.dat","w")
H=36
L=37

for minum_band in range(H-11,L+11+1):
    maximum_band = minum_band + 1
    coupling=0.0
    for n in nsteps:
       Re = "res/0_Ham_"+str(n)+"_im"
       FR = open(Re, "r")
       FRr = FR.readlines()
       FR.close()

       temp=[]
       temp = FRr[minum_band - 1].split()
       val1 = float(temp[maximum_band-1])*13.606*1000
       coupling += math.sqrt(val1**2)
       energy_file.write(" %d   %f    " % (n, val1) )
       energy_file.write(" \n ")

    coupling /= len(nsteps)
    print "H-"+str(H-minum_band), "L+"+str(maximum_band-L), coupling
