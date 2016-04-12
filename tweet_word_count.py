import sys
import json

def computeTermFreq(tweet_file):
	allTweetsWordCount = 0
	termFreq = {} # How many times a term appears across multiple tweets
	for line in open(tweet_file):
		tweetData = json.loads(line)
		
		if 'text' in tweetData: # If the key "text" exists for the tweet, then encode and print
			tweet = tweetData['text'].encode('utf-8')
			wordsInTweet = str.split(tweet)
			allTweetsWordCount += len(wordsInTweet)
			#print wordsInTweet
			for word in wordsInTweet:
				if word not in termFreq:
					termFreq[word] = 1
				else:
					termFreq[word] += 1

	#print termFreq
	#print allTweetsWordCount
	for term in termFreq:
		print term, "", termFreq[term] / float(allTweetsWordCount)

def main():
	computeTermFreq(sys.argv[1])

if __name__ == '__main__':
    main()
