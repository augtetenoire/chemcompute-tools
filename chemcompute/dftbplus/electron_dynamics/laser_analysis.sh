#!/bin/bash

for i in 1 10 100 1000; do

echo -e  "\nRun python script for step ${i}\n"
ipython /Users/atetenoire/server/scripts/LASER_ANAL/ed_analysis_final.py molpopul1.dat ${i} 0

################################################
# Instead of const_detailed.sh
awk '/version/,/<k1/' < detailed.xml > d1  
awk '/\/k1/,/\/detailedout/' < detailed.xml > d2

cat d1 elec_dens d2 > detailed.xml_elec_dens
cat d1 hole_dens d2 > detailed.xml_hole_dens
rm d1 d2

#################################################
mkdir step_${i}
cp detailed.xml_elec_dens detailed.xml_hole_dens eigenvec.bin Transition_Decompo step_${i}/.
(
cd  step_${i}
pwd

# Create the waveplot_in.hsd
if [ -a 'waveplot_in.hsd' ]; then
rm waveplot_in.hsd
fi

cat >> waveplot_in.hsd <<eof


# General options

Options = { 
  TotalChargeDensity = yes             # Total density be plotted?
  TotalChargeDifference = no          # Total density difference plotted?
  ChargeDensity = yes           # Charge density for each state?
#  RealComponent = Yes                  # Plot real component of the wavefunction
  PlottedSpins = { 1 -1 }
  PlottedLevels = { 293 294 295 296 }                # Levels to plot
# PlottedKPoints = 1:-1               # For periodic calculations
  PlottedRegion = OptimalCuboid {}
  NrOfPoints = { 60 60 60 }            # Number of grid points in each direction
  NrOfCachedGrids = -1                 # Nr of cached grids (speeds up things)
  Verbose = Yes                        # Wanna see a lot of messages?
}

DetailedXML = "detailed.xml"           # File containing the detailed xml output
                                       # of DFTB+
EigenvecBin = "eigenvec.bin"           # File cointaining the binary eigenvecs


# Definition of the basis
Basis = { 
  Resolution = 0.01
  # Including mio-1-1.hsd. (If you use a set, which depends on other sets,
  # the wfc.*.hsd files for each required set must be included in a similar
  # way.)
  <<+ "/Users/atetenoire/server/dftb_parameters/mio-1-1/wfc.mio-1-1.hsd"
}
eof


#conda activate dftbplus-last
touch output_waveplot.out

echo -e "\nComputing wp-abs2_hole.cube\n"
mv detailed.xml_hole_dens detailed.xml
waveplot >> output_waveplot.out && echo Done
mv  wp-abs2.cube wp-abs2_hole.cube

echo -e "\nComputing wp-abs2_elec.cube\n"
mv detailed.xml_elec_dens detailed.xml
waveplot >> output_waveplot.out&& echo Done
mv  wp-abs2.cube  wp-abs2_elec.cube

)

rm detailed.xml_elec_dens detailed.xml_hole_dens Transition_Decompo

done