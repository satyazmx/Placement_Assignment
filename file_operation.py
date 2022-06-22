def fileUtility():
    #read input file
    input_file = open("example.txt", "rt")
    #read file contents to string
    data = input_file.read()
    #replace all occurrences of the required string
    data = data.replace('placement', 'screening')
    #close the input file
    input_file.close()
    #open the input file in write mode
    fin = open("example.txt", "wt")
    #overrite the input file with the resulting data
    fin.write(data)
    #close the file
    fin.close()
    
operate = fileUtility()