# KronaClean
# Language: Python
# Input: TXT
# Output: KRONA
# Tested with: PluMA 1.1, Python 3.6

Forms thorough cleaning of Krona input, including matching up phylogenies,
removing selected taxa, fixing citations, replacing subspecies, etc.

Note: This for the moment is very tailored to the example. But the plugin
makes it clear where each case above is handled, so users can add/remove accordingly

Future goal is to make every category customizable

Plugin takes as input a TXT file of keyword-value pairs (tab-delimited):
kronafile: Name of KRONA file to purify
subspecies: File containing list of subspecies

Output KRONA file is the clean one
