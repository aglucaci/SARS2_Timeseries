#!/bin/bash
DATADIR=$2
#Date="2020-03-30"
# Passed from previous bash script.
Date=$1
#echo "Searching for data in: "$DATADIR
mkdir -p analysis
mkdir -p analysis/csvs

echo "    Datadir: "$DATADIR
echo "    Date: "$Date

# ==================================================================================================================================
# Step 1
# python MS_Analysis_mod.py {Fasta} {List of Sites} > {Output CSV}
# ==================================================================================================================================

mkdir -p "analysis/csvs/"$Date
echo "    Analyzing compressed fastas in: "$Date

#exit

echo "    -Processing ORF3a"
python3 silverback_scripts/MS_Analysis_mod.py $DATADIR$Date"/"$Date".ORF3a.ALL.fas" 42,43,57,68,99,125,131,240 > "analysis/csvs/"$Date"/"$Date"_ORF3a_multisite_analysis.csv"

echo "    -Processing M"
python3 silverback_scripts/MS_Analysis_mod.py $DATADIR$Date"/"$Date".M.ALL.fas" 30,69,109,132,141,143 > "analysis/csvs/"$Date"/"$Date"_M_multisite_analysis.csv"

echo "    -Processing N"
python3 silverback_scripts/MS_Analysis_mod.py $DATADIR$Date"/"$Date".N.ALL.fas" 13,20,24,55,67,108,119,139,144,151,173,207,208,210,218,253,291,305,318,360,377,393,397,417 > "analysis/csvs/"$Date"/"$Date"_N_multisite_analysis.csv"

echo "    -Processing ORF1a"
python3 silverback_scripts/MS_Analysis_mod.py $DATADIR$Date"/"$Date".ORF1a.ALL.fas" 16,84,86,92,166,210,265,274,286,333,398,428,454,447,486,519,549,580,609,650,652,717,748,872,892,894,924,1100,1143,1158,1160,1168,1202,1208,1250,1330,1352,1415,1640,1822,1840,1921,2062,2067,2098,2124,2144,2153,2242,2249,2391,2405,2470,2497,2500,2557,2575,2635,2796,2839,2842,3027,3058,3070,3071,3072,3076,3090,3227,3278,3308,3323,3353,3357,3447,3483,3512,3542,3580,3603,3606,3639,3644,3714,3725,3755,3757,3777,3856,3858,3870,3884,3899,3958,3983,4023,4097,4177,4220,4379,4381,4389 > "analysis/csvs/"$Date"/"$Date"_ORF1a_multisite_analysis.csv"

echo "    -Processing: ORF7a"
python3 silverback_scripts/MS_Analysis_mod.py $DATADIR$Date"/"$Date".ORF7a.ALL.fas" 70,92,121 > "analysis/csvs/"$Date"/"$Date"_ORF7a_multisite_analysis.csv"

echo "    -Processing: ORF8"
python3 silverback_scripts/MS_Analysis_mod.py $DATADIR$Date"/"$Date".ORF8.ALL.fas" 8,84,121 > "analysis/csvs/"$Date"/"$Date"_ORF8_multisite_analysis.csv"

echo "    -Processing: S"
python3 silverback_scripts/MS_Analysis_mod.py $DATADIR$Date"/"$Date".S.ALL.fas" 29,61,138,231,294,598,614,620,623,675,723,731,824,934,936,1044,1100 > "analysis/csvs/"$Date"/"$Date"_S_multisite_analysis.csv"

#echo "Processing: ORF6"
#python3 MS_Analysis_mod.py $DATADIR"/"$Date"/sequences.ORF6.compressed.fas" > "analysis/csvs/"$Date"/ORF6_multisite_analysis.csv"


mkdir -p "analysis/images"
mkdir -p "analysis/images/"$Date


# ==================================================================================================================================
# End of file
# ==================================================================================================================================
