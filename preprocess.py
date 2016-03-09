import re
import codecs

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

#Read the tweets one by one and process it
fp = codecs.open('C:/Users/shubham_15294/Desktop/Insight/Twitter Evaluation/TestDataArk.txt', encoding = 'utf-8')
#with f = codecs.open('file.txt', encoding='utf-8'):  # GOOD--gives you Unicode

line = fp.readline()
target = open('C:/Users/shubham_15294/Desktop/Insight/Twitter Evaluation/TestDataARKProcessed.txt', 'w')

while line:
    processedTweet = processTweet(line)
    #print (processedTweet)
    if processedTweet:
        target.write(processedTweet + "\n")
    #break
    line = fp.readline()
#end loop
print("Done !")
fp.close()
target.close()
