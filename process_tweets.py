'''
    Xinmeng Zhang
    Program: process_tweets.py

    Check the functions below and make the requested changes
'''


from string import ascii_letters


def clean_line(line):
    '''
    Eliminates all non-alphabetical characters, except ' ', '@'' and '#',
    from the line.
    >>> clean_line("This is a #hashtag!, this a is a Number123  @userName")
    'this is a #hashtag this a is a number  @username'

    Hint: you can check if a character is alphabetical with this
    expression:
    `char in ascii_letters`
    '''
    # your code here
    temp = []
    candidate_letters = ascii_letters+' @#'
    for c in line:
        if c in candidate_letters:
            temp.append(c)
    
    line = ''.join(temp)
    
    return line


def get_tweet_text(line):
    '''
    Receives a line from the tweets file and get the twwet text from it
    and return all the words in a list.
    The line has the following structure:
    source, text,created_at, retweet_count, favorite_count, is_retweet,id_str

    >>> get_tweet_text("Twitter,Thank you!,11-15-2017 10:58:18,96,433,false,9307")
    'Thank you!'
    '''
    # your code here
    l = line.split(',')
    return l[1]


def read_stopwords():
    '''
    Read the stopwords from 'stopwords.txt' file and return list with the words
    '''
    # your code here
    wordlist = []
    f = open('stopwords.txt', 'r')
    for line in f:
        wordlist.append(line.strip('\n'))
    f.close()
    return wordlist


def process_tweet_text(text):
    '''
    Receives the tweet text and process it:
    - eliminates any non-alpabetical character, except ' ', '@'' and '#'
    - convert it to lowercase
    - separates it in words
    - filter out all the words which are stopwords
    - return the remaining words as a list
    >>> process_tweet_text("this is a #hashtag this a is a number  @username")
    ['#hashtag', 'number', '@username']
    '''
    stopwords = read_stopwords()
    words = clean_line(text).split()
    result = []
    # your code here
    for word in words:
        word = word.lower()
        if not word in stopwords:
            result.append(word)
    
    return result


def process_tweet_file(file_name):
    '''
    Receives the name of file contanining tweets. Process it to get
    all the tweet texts. Extract the words from it and count their frequencies
    Return the result as a dictionary, where the key are the words and the
    values are the word frequencies.
    '''
    word_freqs = {}
    with open(file_name) as tweets:
        for line in tweets:
            text = get_tweet_text(line)
            words = process_tweet_text(text)
            # your code here
            for word in words:
                if word in word_freqs.keys():
                    word_freqs[word] += 1
                else:
                    word_freqs[word] = 1
            
    return word_freqs


def print_statistics(word_freqs):
    '''
    Receives a dictionary with word frequencies and print statistics.
    '''
    # your code here
    tot_num_of_different_words = len(word_freqs.keys())
    tot_num_of_words = sum(word_freqs.values())
    most_frequent_word = sorted(word_freqs, key=lambda x:word_freqs[x])[-1]
    most_frequent_word_freq = word_freqs[most_frequent_word]
    print('The total number of words is:', tot_num_of_words)
    print('The total number of different words is:',
          tot_num_of_different_words)
    print('The most frequent word is:', most_frequent_word)
    print('With a frequency of:', most_frequent_word_freq)


def write_words(word_freqs, file_name):
    '''
    Write down the words along with their frequencies, one word per line
    with the word and the frequency separated by a space:
            great 484
            fabulous 200
    '''
    # your code here
    f = open(file_name, 'w')
    for key in word_freqs:
        f.write(key+" "+str(word_freqs[key])+'\n')
        
    f.close()
    
wf = process_tweet_file('tweets.txt')
print_statistics(wf)
write_words(wf, 'words.txt')

