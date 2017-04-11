"""Restaurant rating lister."""

# put your code here

def read_ratings(my_file):

    """

    Sort and return restaurant ratings

    """

    ratings_file = open(my_file)

    # create dictionary
    ratings = {}

    # In this loop, split text file into list of Restaurant + Rating
    for line in ratings_file:
        line = line.rstrip().split(":")
        ratings[line[0]] = line[1]
    
    # Creating a list of tuples with restaurant name + rating
    r_items = ratings.items()

    # Sort the list of restaurant name + rating tuples
    r_items.sort()


    # Uncomment the line below to print and confirm the  data

    # print r_items


    # Iterate through r_items, print RESTAURANT is rated at RATING
    # r_item[0] is Restaurant. r_item[1] is Rating.

    for r_item in r_items:
        print "%s is rated at %s." %(r_item[0], r_item[1])

    # close file
    ratings_file.close()


# Call the function
read_ratings(my_file = "scores.txt")
