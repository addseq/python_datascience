import sys
import json
import operator

def getTopTenHashTags(tweet_file):
	
	hashTagFreq = {} # How many times a Hashtag appears across multiple tweets
	for line in open(tweet_file):
		tweetData = json.loads(line)
		
		if 'entities' in tweetData:
			entityData = tweetData['entities']
			if 'hashtags' in entityData:
				hashtagData = entityData['hashtags']
				hashtags = [x['text'].encode('utf-8') for x in hashtagData]
				#print hashtags
				for tag in hashtags:
					if tag not in hashTagFreq:
						hashTagFreq[tag] = 1
					else:
						hashTagFreq[tag] += 1
	
	# Reverse lists it from large to small
	sorted_hashTagFreqList = sorted(hashTagFreq.iteritems(), key=operator.itemgetter(1), reverse=True)
	sorted_hashTagFreqList_TopTen = sorted_hashTagFreqList[:10]
	
	for hashTagFreq in sorted_hashTagFreqList_TopTen:
		print hashTagFreq[0], "", hashTagFreq[1]

def main():
	getTopTenHashTags(sys.argv[1])

if __name__ == '__main__':
    main()
