Basic python script to clean tweets. 

Regular expressions used for the following cases:
1. Remove hashtags for words. #happy becomes happy.
2. Remove @username
3. Remove any special characters like ~, %,^,*
4. Remove RT(Re tweets)
5. Replace the URLS with the word URL

Input file format should be the same as allNew.csv

Only the clean tweets are written to a new file, allNewProcessed.csv in this case.
