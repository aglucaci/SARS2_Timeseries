#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Imports
import os
import pandas as pd
import plotly.graph_objects as go
import sys
#import os.path
# In[2]:


#Declares
DATADIR = "analysis/csvs"

#Get list of folders, which correspond to the date in the time series.
Dates = [x[0].replace(DATADIR+"/", "") for x in os.walk(DATADIR) if "Archive" not in x[0] and x[0] != DATADIR]
Dates.sort()
Dates.remove("20200513") # had a processing error.
print("List of Dates:", Dates)
#Dates.remove("2020-05-13") # had a processing error.

input_csv_gene = sys.argv[1]
print("Input CSV:", input_csv_gene)
#input_csv_gene = "S_valuecounts_with_total_and_freqs.csv"
#input_csv_gene = "ORF1a_valuecounts_with_total_and_freqs.csv"
#input_csv_gene = "M_valuecounts_with_total_and_freqs.csv"
#input_csv_gene = "N_valuecounts_with_total_and_freqs.csv"
#input_csv_gene = "ORF3a_valuecounts_with_total_and_freqs.csv"
#input_csv_gene = "ORF7a_valuecounts_with_total_and_freqs.csv"
#input_csv_gene = "ORF8_valuecounts_with_total_and_freqs.csv"

gene = input_csv_gene.split("_")[0]
print("Gene:", gene)

# In[3]:


#Dates


# In[4]:


# For the element, "Code", in May 30, get its values across all dates. 
# I need the "Set" of all codes
# So I have "Code"_1 and List_1 of all values across each date.
# x = Dates
# y = Frequency values of each "Code"
# and create a subplot for each one.

#Set of Codes.
# Open every "S_valuecounts_with_total_and_freqs.csv" and add to a list, return the set.

list_of_codes = []
print("Looping over dates and adding haplotypes to list")
for day in Dates:
    #print("Day:", day)
    search_dir = DATADIR + "/" + day
    search_file = search_dir + "/" + input_csv_gene
    df = pd.read_csv(search_file)
    Codes = df["Code"]
    for item in Codes:
        list_of_codes += [item]
    #end inner for
#end for

elements = {}
print("Creating a set of list items")
for n, item in enumerate(set(list_of_codes)):
    #print(n, item, "\n")
    elements[item] = {}


# In[ ]:

print("Processing the 'set' of unique haplotypes")
for n, item in enumerate(elements.keys()):
    print("\t", n, "Processing:", item)
    
    # For each element, 
    # Search each date.
    # Is the element present? If Yes, report the Freq. If no report 0
    for day in Dates:
        #print("\t\tWill check for the haplotype in", day)
        search_dir = DATADIR + "/" + day
        search_file = search_dir + "/" + input_csv_gene
        #import os.path
        #if not os.path.exists(file_path): continue
        assert os.path.exists(search_file)
        df = pd.read_csv(search_file)
        Codes = df["Code"]
        #Need to adjust "day" here
        day_adjusted = day[:4] + "-" + day[4:6] + "-" + day[6:8]
        elements[item][day_adjusted] = 0 # default value
        for n, seq_code in enumerate(Codes):
            if seq_code == item:
                elements[item][day_adjusted] = df["Frequency"][n]
            #end if
        #end second inner for
    #end inner for
#end outer for
        
#print("Elements:", elements)
""" Can save Elements to json here. It is a dict."""

# Plotting
# Plot "Elements"
# Key1 is the Sequence "Code"
# Key2 is the Date
# Key3 is the codes frequency on that date.
print("Creating plot")
Key1 = elements.keys()
#Key2 = Dates
Key2 = []
fig = go.Figure()

for i, seq_Code in enumerate(elements.keys()):
    #print("Processing:", seq_Code)
    #sys.stdout.write("Download progress: %d%%   \r" % (progress) )
    #sys.stdout.flush()
    print("Processing (for plot):", i)
    list_of_Frequencies = []
    for day in Dates:
        day_adjusted = day[:4] + "-" + day[4:6] + "-" + day[6:8]
        Key2.append(day_adjusted)
        list_of_Frequencies += [elements[seq_Code][day_adjusted]]
    #end for
    #print(seq_Code, Dates, list_of_Frequencies)
    
    #print("Adding:", seq_Code, Dates, list_of_Frequencies)
    #print()
    
    #fig.add_trace(go.Scatter(x=Key2, y=list_of_Frequencies, name=seq_Code, text=seq_Code))
    #
    fig.add_trace(go.Bar(x=Key2, y=list_of_Frequencies, name=seq_Code, text=seq_Code))
    #x unified
    #hover_name="country", hover_data=["continent", "pop"]
#end for
print("Added subplots")

"""

    marker={'color': list_of_Frequencies,
    'colorscale': 'Viridis'}
    
    aliceblue, antiquewhite, aqua, aquamarine, azure,
      beige, bisque, black, blanchedalmond, blue,
      blueviolet, brown, burlywood, cadetblue,
      chartreuse, chocolate, coral, cornflowerblue,
      cornsilk, crimson, cyan, darkblue, darkcyan,
      darkgoldenrod, darkgray, darkgrey, darkgreen,
      darkkhaki, darkmagenta, darkolivegreen, darkorange,
      darkorchid, darkred, darksalmon, darkseagreen,
      darkslateblue, darkslategray, darkslategrey,
      darkturquoise, darkviolet, deeppink, deepskyblue,
      dimgray, dimgrey, dodgerblue, firebrick,
      floralwhite, forestgreen, fuchsia, gainsboro,
      ghostwhite, gold, goldenrod, gray, grey, green,
      greenyellow, honeydew, hotpink, indianred, indigo,
      ivory, khaki, lavender, lavenderblush, lawngreen,
      lemonchiffon, lightblue, lightcoral, lightcyan,
      lightgoldenrodyellow, lightgray, lightgrey,
      lightgreen, lightpink, lightsalmon, lightseagreen,
      lightskyblue, lightslategray, lightslategrey,
      lightsteelblue, lightyellow, lime, limegreen,
      linen, magenta, maroon, mediumaquamarine,
      mediumblue, mediumorchid, mediumpurple,
      mediumseagreen, mediumslateblue, mediumspringgreen,
      mediumturquoise, mediumvioletred, midnightblue,
      mintcream, mistyrose, moccasin, navajowhite, navy,
      oldlace, olive, olivedrab, orange, orangered,
      orchid, palegoldenrod, palegreen, paleturquoise,
      palevioletred, papayawhip, peachpuff, peru, pink,
      plum, powderblue, purple, red, rosybrown,
      royalblue, rebeccapurple, saddlebrown, salmon,
      sandybrown, seagreen, seashell, sienna, silver,
      skyblue, slateblue, slategray, slategrey, snow,
      springgreen, steelblue, tan, teal, thistle, tomato,
      turquoise, violet, wh

"""
#fig.add_trace(go.Scatter(x=list_of_Dates, y=list_of_Frequencies, name=seq_Code)


#fig.add_trace(go.Figure(data=[go.Table(header=dict(values=['A Scores', 'B Scores']),
##                 cells=dict(values=[[100, 90, 80, 90], [95, 85, 75, 95]]))
##                    ]))


# Edit the layout
fig.update_layout(title='SARS-CoV-2 (' + gene + ') Mutation Fingerprint - Timeseries Analysis (num_codes=' + str(len(elements.keys())) + ')',
                   xaxis_title='',
                   yaxis_title='Frequency',
                   width=1000, height=600)

#fig.update_layout(showlegend=False)

# Change the bar mode
fig.update_layout(barmode='stack')
fig.update_layout(legend_orientation="h")
#fig.update_layout(hovermode="x unified")
fig.update_layout(autosize=True)
fig.show()


import plotly.express as px

#fig =px.scatter(x=range(10), y=range(10))
os.system("mkdir -p html")
fig.write_html("html/" + input_csv_gene.replace(".csv","") + "_stackedbar.html")


# In[ ]:


#End of file

