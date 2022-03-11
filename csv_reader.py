import csv

htitle = []
dtitle = []
diftitles = []

def checkDuplicates(largerDataset, smallerDataset):
    for r in largerDataset:
        if r not in smallerDataset:
            thisTitle = [r]
            diftitles.append(thisTitle)

    # Create a csv file containing the unique titles
    with open('test.csv', 'w', newline='') as write_csv:        
        writer = csv.writer(write_csv)
        # writer.writerow(diftitles)
        for i in diftitles:
            writer.writerow(i)

        print('CSV created')


# Open the CSV files
dataset =  open('filtered_dataset.csv', 'r')
haystack = open('search_dataset.csv', 'r') 

# Use csv, read the CSV files and copy them locally
csv_dataset = csv.reader(dataset,delimiter=',')    
csv_haystack = csv.reader(haystack,delimiter=',') 

# Loop through the haystack CSV and add titles to list
for h in csv_haystack:
    htitle.append(h[0])

# Loop through the dataset/needle CSV and add titles to list
for d in csv_dataset:
    dtitle.append(d[0])

#Check which list has a longer length and loop over that one.
if len(htitle) > len(dtitle):
    print("htitle has more")
    checkDuplicates(htitle, dtitle)

else:
    print("dtitle has more")
    checkDuplicates(dtitle, htitle)


        

# for i in title:
#     print(i)
        #if there is a DOI, attempt a match on title, author and doi
    #     if row[4] != "":
    #         if row[0] not in title and row[1] not in author and row[4] not in doi:
    #             title.append(row[0])
    #             author.append(row[1])
    #             doi.append(row[4])
    #             filtered.append([row[0],row[1],row[2],row[3],row[4]])
    #     else:  #there is no DOI, so match on title and author
    #         if row[0] not in title and row[1] not in author:
    #             title.append(row[0])
    #             author.append(row[1])
    #             filtered.append([row[0],row[1],row[2],row[3],""])
        
    # #create a csv file containing the filtered results

    
