def csvcutter(filelocation, filename, numheads, cutby, network):
    # Cuts CSV files where:
    # filelocation is a string of the directory, WITH FORWARD SLASHES
    # FOR MAC
    # filename is a string of the name of the original file
    # numheaders is the length (in rows) of the header
    # cutby is the column number by which the data is cut (output files
    # are named identically)
    # network is additional data point added to file name
    import os
    import xlwt
    os.chdir(filelocation)
    import csv
    original = open(filename, "rU")
    original_csv = csv.reader(original)
    # opens SBR report/CSV file for use
    count = 0
    header = []
    for row in original_csv:
        count = count + 1
        if count < (numheads + 1):
            header.append(row)
        else:
            break
    # Creates header for document if first TWO rows in CSV are headers
    from operator import itemgetter
    # Imports functions for quick ordering
    data = []
    count = 0
    for row in original_csv:
        count = count + 1
        if count > numheads:
            data.append(row)
    # Creates new data frame with ONLY the data
    # Takes out slashes
    count = 0
    data = sorted(data, key=itemgetter((cutby-1)))
    labels = zip(*data)[(cutby-1)]
    labels = sorted(list(set(labels)))
    # Sorts data by label name
    for label in labels:
        data_new = []
        for rows in data:
            if label in rows:
                data_new.append(rows)
    # Creates new data structure, named 'data_tool' that has ONLY the data rows
        label_current = []
        for row in header:
            label_current.append(row)
        for row in data_new:
            label_current.append(row)
    # label now contains ALL the values needed in a CSV file
        label = label.replace('/', '')
        file_name = filelocation + '/' + str(row[(network-1)]) + '.'
                    + str(label) + '.csv'
    # Creates new file name
        new_file = open(file_name, 'w')
        wr_newfile = csv.writer(new_file, dialect='excel')
        for row in label_current:
            wr_newfile.writerow(row)
        new_file.close()
        del new_file
        del wr_newfile
        del label_current
    # Writes new file, and closes it
