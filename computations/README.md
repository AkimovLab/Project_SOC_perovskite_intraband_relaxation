# PROJECT_SOC_perovskite_intraband_relaxation
necessary files for runing the computations

0-opt:
	VASP input files to run geometry optimization
	OUTCAR - VASP output file

1-md:
	VASP input files to run ab initio molecular dynamics
	INCAR_heat - INCAR for bringing the system from 0K to 300K
	INCAR_md - INCAR for obtaining the nuclear trajectory for NAC calculation
	POSCAR - the optimized ground state structure
        XDATCAR - the nuclear trajectory from production run for NAC calculation

2-pdos:
	QE-pdos/NO-SOC/ - the directory for computation of pDOS without SOC  using QE
        QE-pdos/SOC/ - the directory for computation of pDOS with SOC usingg QE
	VASP-pdos/NO-SOC/ - the directory for computation of pDOS without SOC  using VASP
	VASP-pdos/SOC - the directory for computation of pDOS with SOC usingg VASP

3-nac:
	no-soc/  - the directory for NAC calculation without SOC
        soc/ - the directory for NAC calculation with SOC
        using the XDATCAR file from 1-md

4-namd:
	electron-no-soc.py - script for electron intraband relaxation without SOC
	electron-soc.py - script for electron intraband relaxation with SOC
	hole-no-soc.py -  script for hole intraband relaxation without SOC
	hole-soc.py - script for hole intraband relaxation with SOC

