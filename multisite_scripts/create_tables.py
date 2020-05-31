

#


import numpy as np
import pandas as pd
import sys

df = pd.read_csv(sys.argv[1], index_col=[0])
date = sys.argv[2]
gene = sys.argv[3]

output_dir = "analysis/tables/" + date

df2 = df.head(5)

df2.to_html(output_dir + "/" + gene+'.html')
