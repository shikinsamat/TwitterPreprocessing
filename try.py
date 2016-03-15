import csv
import codecs
p = codecs.open('all.csv', encoding = 'latin-1')
read = csv.reader(p)
#for row in read :
#    print (row[2]) 
outputFile = open('he12llo21.csv', 'w',newline='')
outputWriter = csv.writer(outputFile)
outputWriter.writerow(['hola'])
outputWriter.writerow(['abey chutiye!'])
outputFile.close()
print('Done')

