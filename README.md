# csv-remove-duplicates-python
A simple Python script developed to identify check if a title is unique between two CSVs. If the title is unique, it gets added to a new CSV. The script can easily be adapted to other columns. Ensure no full stops are placed at the end of a title to avoid returning titles that have been explored in the filtered dataset sheet. 

##Instuctions
Place your existing data, or the data that will act as the haystack, in the filtered_data.csv
Place the data you wish to check over in the search_data.csv. If you are using this to perform a manual search for a literature review or other research review:
  - Copy and paste your references into the CSV
  - Remove all other data apart from titles
  - Make sure the titles do not contain full stops at the end
  - Remove empty rows for efficiency. You can do this with Excel.

Run the script. The resulted CSV (named test.csv) produces a list that shows titles that were not present in the haystack.
