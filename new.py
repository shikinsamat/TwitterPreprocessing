import csv
import codecs
p = codecs.open('all.csv', encoding = 'latin-1')
read = csv.reader(p)
#for row in read :
#    print (row[2]) 
outputFile = open('helleeeo.csv', 'w')
outputWriter = csv.writer(outputFile)
outputWriter.writerow(['spam', 'eggs', 'bacon', 'ham'])

