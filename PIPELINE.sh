#!/bin/bash
# Alexander G Lucaci



#1
#bash silverback_scripts/STEP_1_pass_dirs_to_runner.sh

#2
#The above script will launch "runner_MS_analysis.sh"

#3 the script above will launch "MS_Analysis_mod.py"
#this produces the analysis/csvs/$Date/gene{X}.csv
#which has the haplotype (row) and count.

#4
#this will launch: plot_jupyter_mod.py
bash multisite_scripts/STEP_2.sh

#5
#bash multisite_scripts/STEP_3_runner_plot_csvs.sh

# End of file

