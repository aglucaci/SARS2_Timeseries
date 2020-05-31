#!/usr/bin/env python
# coding: utf-8

# =============================================================================
# Imports
# =============================================================================

import plotly.express as px
import pandas as pd
pd.options.mode.chained_assignment = None
import matplotlib.pyplot as plt
import sys
from matplotlib.pyplot import figure

# =============================================================================
# Declares
# =============================================================================
datafile = sys.argv[1] # Multisite CSV
gene = sys.argv[2]
figsize_width = int(sys.argv[3])
figsize_height = int(sys.argv[4])
Date = sys.argv[5]
#MultiSite_csv = sys.argv[6]

# =============================================================================
# Helper function
# =============================================================================
"""
Give a "code" in the value_counts csv, how many actual sequences in the original "total" alignment does this represent?
"""
def num_counts_in_original(code_tosearch, MultiSite_csv):
    df_handle = pd.read_csv(MultiSite_csv)
    num_count = 0
    for n, entry in enumerate(df_handle["Code"]):
        if entry == code_tosearch:
            #get sequence id.
            ID = df_handle["Sequence ID"][n]
            #print("Found ID:", ID)
            if ID != "":
                get_num = int(ID.split("_")[-1])
                num_count += get_num
            #end inner if
        #end outer if
    #end for
    return num_count
#end method

# =============================================================================
# Main
# =============================================================================
print("    # Processing:", datafile)
data = pd.read_csv(datafile)
#print("COLUMNS:", data.columns.tolist())
fig, ax = plt.subplots()
#plt.figure(figsize=(20,110))
data['Code'].value_counts().plot(ax=ax, kind='barh', figsize=(figsize_width, figsize_height), fontsize=12, title=gene + " MULTISITE ANALYSIS")

# The code is a concat'd string of SITE# and codon at that position
# site 42, codon CCT
# site 32, codon TTC , etc,
# This is only done for interesting sites

output = "analysis/images/"+Date+"/"+gene+".png"
print("\t\t# Saving:", output)
fig.savefig(output)

# Pie
fig, ax = plt.subplots()
#plt.figure(figsize=(20,110)) 
data['Code'].value_counts().plot(ax=ax, kind='pie', figsize=(figsize_width, figsize_height), fontsize=12, title=gene + " MULTISITE ANALYSIS")
output = "analysis/images/"+Date+"/"+gene+"_pie.png"
print("\t\t# Saving:", output)
fig.savefig(output)


# =============================================================================
# Saving to file, csv (value_counts)
# =============================================================================

#sys.exit(1)


df = data

df2 = df["Code"].value_counts()
#df2.columns = ["Code", "value_counts_compressed"]
#df2.rename({'': 'Code', 'Code': 'value_counts_compressed'}, inplace=True)

df2_output = "analysis/csvs/"+Date+"/"+Date+"_"+gene+"_valuecounts.csv"
print("\t\t# Saving dataframe (value_counts):", df2_output)
df2.to_csv(df2_output)

#df['count'] = df.groupby('group')['group'].transform('count')

#df["Counts"] = df[" Code"].value_counts()
#df[" Code"].value_counts().rename_axis('created_at').reset_index(name='count')

#print(df)

#datafile = datafile.replace(".csv", "")
#df.to_csv(datafile+"_withvaluecounts.csv")

###
"""
Dont need this part, since I am using the 'all' alignment.
So I dont need to
"""

###

#sys.exit(20)

df3 = pd.read_csv(df2_output)
#df3.rename({'Unnamed: 0':'a', 'Code': 'value_counts_compressed'})
df3.columns = ["Code", "value_counts_compressed"]
#print(df3, list(df3.columns.values))
#print(df3)


# Loop over each row, "Code"
# Search in the multisite_csv,
# Find list IDs that match this code
# get the total num of seqs that match, uncompressed.
df3["value_counts_total"] = 0

for n, item in enumerate(df3["Code"]):
    #print("\t", "Searching:", item)
    
    #This is old. We dont need this.
    #x = num_counts_in_original(item, datafile)
    
    #compressed number equals the total number. Because we are using ALL alignment file.
    x = df3["value_counts_compressed"][n]
    #print("\t", "Corresponds to:", x)
    df3["value_counts_total"][n] = x
    
#print(df3)

num_sum = df3["value_counts_total"].sum()
#print(num_sum)

df3["Frequency"] = 0.0
for n, item in enumerate(df3["value_counts_total"]):
    #print("\t", int(item) / num_sum)
    df3["Frequency"][n] = int(item) / num_sum

#print(df3)


df3_output = "analysis/csvs/"+Date+"/"+gene+"_valuecounts_with_total_and_freqs.csv"
print("\t\t# Saving dataframe (valuecounts_with_total_and_freqs):", df3_output)
df3.to_csv(df3_output)

# =============================================================================
# 
# =============================================================================
