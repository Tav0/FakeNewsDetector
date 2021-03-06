import got

# Twitter's data

since = "2016-01-01"
until = "2016-12-31"

queries = [
    "obama pledge allegiance bans OR pledge OR allegiance",
    "Pope Trump endorse OR endorses OR endorsed OR endorsement",
    "Trump Africa Mexico ticket OR tickets leave OR leaving OR left OR offer OR offered OR offering OR give OR gave OR giving",
    "fbi agent hillary leaks dead OR deads OR death",
    "rage against machine trump reunite OR reuniting OR reunited",
    "trump marines own plane",
    "pizzage #pizzagate",
    "ireland trump refugee OR refugees OR accept OR accepting OR accepted OR take OR takes OR taking",
    "hillary isis weapons wikileaks",
    "obama trump leave office refuse OR refuses OR won't"
]

def write_to_file(tweets, num):
    textfile = "tweets_results_{num}.txt".format(num=num)
    f = open(textfile,"w+")

    """
    we can add:
    tweet.id, tweet.permalink, tweet.date, tweet.favorites, tweet.geo
    """
    for tweet in tweets:
        f.write("Username: %s\n" % tweet.username)
        f.write("ReTweets: %d\n" % tweet.retweets)
        if type(tweet.text) is unicode:
            convert_2_str = (tweet.text).encode('ascii', 'ignore')
            tweet.text = convert_2_str

        f.write("Message: %s\n" % tweet.text)
        f.write("Hashtags: %s\n" % tweet.hashtags)
        f.write("Mentions: %s\n\n" % tweet.mentions)

    f.close()


def main():
    global queries, since, until

    for i in range(len(queries)):
        print "start searching for: %s\n" % queries[i]
        tweet_criteria = got.manager.TweetCriteria().setQuerySearch(queries[i]).setSince(since).setUntil(until)
        tweets_results = got.manager.TweetManager.getTweets(tweet_criteria)
        write_to_file(tweets_results, i)


if __name__ == "__main__":
    print("starting...")
    main()
    print("end")
