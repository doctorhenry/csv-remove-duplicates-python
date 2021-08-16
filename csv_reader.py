import csv

title =[]
author =[]
doi =[]
filtered = []

with open('search_dataset.csv', 'r') as dataset:
    csv_reader = csv.reader(dataset,delimiter=',')    
    for row in csv_reader:
        #if there is a DOI, attempt a match on title, author and doi
        if row[4] != "":
            if row[0] not in title and row[1] not in author and row[4] not in doi:
                title.append(row[0])
                author.append(row[1])
                doi.append(row[4])
                filtered.append([row[0],row[1],row[2],row[3],row[4]])
        else:  #there is no DOI, so match on title and author
            if row[0] not in title and row[1] not in author:
                title.append(row[0])
                author.append(row[1])
                filtered.append([row[0],row[1],row[2],row[3],""])
        
    #create a csv file containing the filtered results
    with open('filtered_dataset.csv', 'w', newline='') as write_csv:        
        writer = csv.writer(write_csv, delimiter=',', quotechar='"', quoting = csv.QUOTE_MINIMAL)
        for i in range(len(filtered)):
            if filtered[i] != "":
                writer.writerow(filtered[i])

        print('Filtered CSV created')
    
