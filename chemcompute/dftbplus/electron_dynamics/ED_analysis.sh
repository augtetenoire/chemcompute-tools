#!/bin/bash



# Extract the spectra from the calcualtions
field_strength=$(grep 'FieldStrength' dftb_in.hsd | grep -oE '[0-9\.]+')
for i in 5 10 15 20 25 30 ; do 
conda run -n dftbplus-last calc_timeprop_spectrum -d ${i} -f ${field_strength}
mv spec-ev.dat spec-ev_d${i}.dat
mv spec-nm.dat spec-nm_d${i}.dat
done

ipython /Users/atetenoire/github/chemcompute-tools/chemcompute/dftbplus/electron_dynamics/plot_ed_uv-vis_general.py

# Extract data if molpopul file is present
if [ -a molpopul1.dat ]; then
ipython /Users/atetenoire/github/chemcompute-tools/chemcompute/dftbplus/electron_dynamics//plot_pop_orb.py
fi

echo 'To get maximum polarization, use :'
echo "calc_timeprop_maxpoldir -d 20.0 -w wavelength"
