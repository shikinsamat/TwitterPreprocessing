Basic python script to clean tweets. 

Regular expressions used for the following cases:
    Remove hashtags for words. #happy becomes happy.
    Remove @username
    Remove any special characters like ~, %,^,*
    Remove RT(Re tweets)
    Replace the URLS with the word URL

Input file format should be the same as allNew.csv

Only the clean tweets are written to a new file, allNewProcessed.csv in this case.
