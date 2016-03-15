import re
import codecs
import csv

#start process_tweet
def processTweet(tweet):
    tweet = tweet.lower()
    tweet = " " + tweet
    tweet = re.sub(r'[^\x00-\x7F]+','', tweet)
    #tweet = tweet.replace(" rt "," ")
    tweet = re.sub(' rt ','', tweet)
    tweet = re.sub('(\.)+','.', tweet)
    #tweet = re.sub('((www\.[^\s]+)|(https://[^\s]+) | (http://[^\s]+))','URL',tweet)
    tweet = re.sub('((www\.[^\s]+))','',tweet)
    tweet = re.sub('((http://[^\s]+))','',tweet)
    tweet = re.sub('((https://[^\s]+))','',tweet)
    tweet = re.sub('@[^\s]+','',tweet)
    tweet = re.sub('[\s]+', ' ', tweet)
    tweet = re.sub(r'#([^\s]+)', r'\1', tweet)
    tweet = re.sub('_','',tweet)
    tweet = re.sub('\$','',tweet)
    tweet = re.sub('%','',tweet)
    tweet = re.sub('^','',tweet)
    tweet = re.sub('&','',tweet)
    tweet = re.sub('\*','',tweet)
    tweet = re.sub('\(','',tweet)
    tweet = re.sub('\)','',tweet)
    tweet = re.sub('-','',tweet)
    tweet = re.sub('\+','',tweet)
    tweet = re.sub('=','',tweet)
    tweet = re.sub('"','',tweet)
    tweet = re.sub('~','',tweet)
    tweet = re.sub('`','',tweet)
    tweet = re.sub('!','',tweet)
    tweet = re.sub(':','',tweet)
    tweet = re.sub('^-?[0-9]+$','', tweet)
    tweet = tweet.strip('\'"')
    return tweet
#end

p = codecs.open('allNew.csv', encoding = 'latin-1')
read = csv.reader(p)
outputFile = open('allNewProcessed.csv', 'w',newline='')
outputWriter = csv.writer(outputFile)
for row in read :
    processedTweet = processTweet(row[2])
    outputWriter.writerow([processedTweet])

outputFile.close();
p.close();
print("Done !")
