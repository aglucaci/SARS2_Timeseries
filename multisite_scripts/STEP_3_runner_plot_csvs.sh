#!/bin/bash

#input_csv_gene = "S_valuecounts_with_total_and_freqs.csv"
#input_csv_gene = "ORF1a_valuecounts_with_total_and_freqs.csv"
#input_csv_gene = "M_valuecounts_with_total_and_freqs.csv"
#input_csv_gene = "N_valuecounts_with_total_and_freqs.csv"
#input_csv_gene = "ORF3a_valuecounts_with_total_and_freqs.csv"
#input_csv_gene = "ORF7a_valuecounts_with_total_and_freqs.csv"
#input_csv_gene = "ORF8_valuecounts_with_total_and_freqs.csv"
clear
echo "# #################################"
echo "# Starting Step 3"
echo "# #################################"

# Main subroutine
python multisite_scripts/plot_csvs.py S_valuecounts_with_total_and_freqs.csv
python multisite_scripts/plot_csvs.py ORF1a_valuecounts_with_total_and_freqs.csv
python multisite_scripts/plot_csvs.py M_valuecounts_with_total_and_freqs.csv
python multisite_scripts/plot_csvs.py N_valuecounts_with_total_and_freqs.csv
python multisite_scripts/plot_csvs.py ORF3a_valuecounts_with_total_and_freqs.csv
python multisite_scripts/plot_csvs.py ORF7a_valuecounts_with_total_and_freqs.csv
python multisite_scripts/plot_csvs.py ORF8_valuecounts_with_total_and_freqs.csv

#cat clarifying_text.txt html/*_stackedbar.html > html/mutation_fingerprint_full.html

mkdir -p output

cat clarifying_text.txt html/*.html > output/mutation_fingerprint_full.html

cat clarifying_text_bottom_for_tables.txt >> output/mutation_fingerprint_full.html

(echo "<p><b>Data Table for M</b><br></p>"; cat analysis/tables/2020-05-12/M.html) >> output/mutation_fingerprint_full.html
(echo "<p><b>Data Table for N</b><br></p>"; cat analysis/tables/2020-05-12/N.html) >> output/mutation_fingerprint_full.html
(echo "<p><b>Data Table for ORF1a</b><br></p>"; cat analysis/tables/2020-05-12/ORF1a.html) >> output/mutation_fingerprint_full.html
(echo "<p><b>Data Table for ORF3a</b><br></p>"; cat analysis/tables/2020-05-12/ORF3a.html) >> output/mutation_fingerprint_full.html
(echo "<p><b>Data Table for ORF7a</b><br></p>"; cat analysis/tables/2020-05-12/ORF7a.html) >> output/mutation_fingerprint_full.html
(echo "<p><b>Data Table for ORF8</b><br></p>"; cat analysis/tables/2020-05-12/ORF8.html) >> output/mutation_fingerprint_full.html
(echo "<p><b>Data Table for S</b><br></p>"; cat analysis/tables/2020-05-12/S.html) >> output/mutation_fingerprint_full.html
#End of file.
