"""Restaurant rating lister."""

# put your code here

"""

Sort and return restaurant ratings

"""

def read_ratings(my_file):
# Sort and return restaurant ratings

    ratings_file = open(my_file)
    text = text_file.read()
    words = text.split(" ")
    for word in words:
        word = word.lower()
        word = word.strip(string.whitespace)
        word = word.rstrip(string.punctuation)
    c = collections.Counter(words)
    for word, count in c.items():
        print word, count
    # word_count = {}
    # for line in text:
    #     line = line.rstrip()
    #     words = line.split(" ")
    #     for word in words:
    #         word = word.lower()
    #         word = word.strip(string.punctuation)
    #         word_count[word] = word_count.get(word, 0) + 1
    # for word, count in word_count.items():
    #     print word, count
    text_file.close()


# Call the function
read_ratings(my_file = scores.txt)
  






