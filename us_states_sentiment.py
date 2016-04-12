import sys
import json

states = {
        'AK': 'Alaska',
        'AL': 'Alabama',
        'AR': 'Arkansas',
        'AS': 'American Samoa',
        'AZ': 'Arizona',
        'CA': 'California',
        'CO': 'Colorado',
        'CT': 'Connecticut',
        'DC': 'District of Columbia',
        'DE': 'Delaware',
        'FL': 'Florida',
        'GA': 'Georgia',
        'GU': 'Guam',
        'HI': 'Hawaii',
        'IA': 'Iowa',
        'ID': 'Idaho',
        'IL': 'Illinois',
        'IN': 'Indiana',
        'KS': 'Kansas',
        'KY': 'Kentucky',
        'LA': 'Louisiana',
        'MA': 'Massachusetts',
        'MD': 'Maryland',
        'ME': 'Maine',
        'MI': 'Michigan',
        'MN': 'Minnesota',
        'MO': 'Missouri',
        'MP': 'Northern Mariana Islands',
        'MS': 'Mississippi',
        'MT': 'Montana',
        'NA': 'National',
        'NC': 'North Carolina',
        'ND': 'North Dakota',
        'NE': 'Nebraska',
        'NH': 'New Hampshire',
        'NJ': 'New Jersey',
        'NM': 'New Mexico',
        'NV': 'Nevada',
        'NY': 'New York',
        'OH': 'Ohio',
        'OK': 'Oklahoma',
        'OR': 'Oregon',
        'PA': 'Pennsylvania',
        'PR': 'Puerto Rico',
        'RI': 'Rhode Island',
        'SC': 'South Carolina',
        'SD': 'South Dakota',
        'TN': 'Tennessee',
        'TX': 'Texas',
        'UT': 'Utah',
        'VA': 'Virginia',
        'VI': 'Virgin Islands',
        'VT': 'Vermont',
        'WA': 'Washington',
        'WI': 'Wisconsin',
        'WV': 'West Virginia',
        'WY': 'Wyoming'
}

states_fullname = dict( zip(states.values(),states.keys()) )

def findHappiestStateFromTweets(tweet_file, sentiment):
	lineCount = 0
	tweetSentimentScores = []
	tweetState = []
	for line in open(tweet_file):
		tweetData = json.loads(line)
		
		#Determine Tweet Sentiment Score
		score = 0 # Default score is zero if not a real tweet or no hits in sentiment dictionary
		if 'text' in tweetData: # If the key "text" exists for the tweet, then encode and print
			tweet = tweetData['text'].encode('utf-8')
			wordsInTweet = str.split(tweet)
			print "Tweet:", wordsInTweet
			for word in wordsInTweet:
				if word in sentiment:
					wordScore = sentiment[word]
					score += wordScore
					print "*****Found", word , "worth", wordScore, "pts from above tweet*****"
			
		tweetSentimentScores.append(score) #Order of score corresponds to order of tweet
		
		#Determine Tweet Location Method 1: User 
		if 'user' in tweetData:
			userData = tweetData['user']
			if 'location' in userData:
				userLoc = userData['location'].encode('utf-8')
				userLoc = userLoc.replace(",","")	 #Get rid of commas
				userLoc = userLoc.replace("/"," ") #Treat / delimiters same as space
				wordsInLoc = userLoc.split()
				print "Location:", wordsInLoc
				stateFound = 0
				for word in wordsInLoc:
					possibleStateAbbr = word.upper()
					possibleStateName = word.capitalize()
					if possibleStateAbbr in states:
						tweetState.append(possibleStateAbbr)
						stateFound = 1
						print possibleStateAbbr
						break
					elif possibleStateName in states_fullname and possibleStateName != 'Washington':
						tweetState.append(states_fullname[possibleStateName])
						stateFound = 1
						print states_fullname[possibleStateName]
						break
				if stateFound == 0:
					tweetState.append("NO_STATE_FOUND")
		
		#Iterator, increment counter and separate output
		lineCount += 1
		print "\n"
	
	stateSentiment = zip( tweetState, tweetSentimentScores )
	print stateSentiment
	happiest_state = ""
	maxScore = 0
	for stateData in stateSentiment:
		state = stateData[0]
		score = stateData[1]
		if state != 'NO_STATE_FOUND' and len(state) == 2 :
			if score > maxScore:
				maxScore = score
				happiest_state = state
	
	print happiest_state # Print the happiest state only
			

def convertSentFile(sent_file):
	afinnfile = open(sent_file)
	scores = {} # initialize an empty dictionary
	for line in afinnfile:
		term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
		scores[term] = int(score)  # Convert the score to an integer.
	#print scores.items() # Print every (term, score) pair in the dictionary
	return scores;

def main():
	s = convertSentFile(sys.argv[1])
	findHappiestStateFromTweets(sys.argv[2], s)

if __name__ == '__main__':
    main()

