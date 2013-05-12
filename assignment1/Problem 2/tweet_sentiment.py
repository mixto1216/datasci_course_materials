import sys
import urllib
import json

def hw():
    print 'Hello, world!'

def lines(fp): #count no. of lines and print it out	
    print str(len(fp.readlines()))

def main():
	sent_file = open(sys.argv[1])
	tweet_file = open(sys.argv[2])	
	#lines(sent_file) #if calls lines here, readlines() will drive pointer all the way to end of file, hence no lines left..	
	#lines(tweet_file)
	scores = {}
	# 2. Turn sentiment_file into dictionary-alike ref.data
	for line in sent_file:
		term, score = line.split("\t")		
		scores[term] = int(score)	
		
	#3 Loads Tweet file into JSON format	
	for line in tweet_file:	#While every "line" of file is JSON, file "as a whole" is NOT...
		json_tweet=json.loads(line) #load"s" reads every line, while load does a complete file?		
		flag=False
		for key in json_tweet.keys():
			if key=="text":	#not all lines contains the key "text"
				flag=True
				words=json_tweet["text"].encode("utf-8").split() #encode everything with utf-8, while split() without parameter splits by space
								
				count=0.0
				for w in words:						
					if scores.get(w)!=None:
						count = count + scores[w]
		if flag==True:
			print count
		else:
			print 0.0
		
				
if __name__ == '__main__':
    main()
