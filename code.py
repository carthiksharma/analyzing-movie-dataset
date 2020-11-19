# --------------
from csv import reader


def explore_data(dataset, start, end, rows_and_columns=False):
    """Explore the elements of a list.
    
    Print the elements of a list starting from the index 'start'(included) upto the index 'end'         (excluded).
    
    Keyword arguments:
    dataset -- list of which we want to see the elements
    start -- index of the first element we want to see, this is included
    end -- index of the stopping element, this is excluded 
    rows_and_columns -- this parameter is optional while calling the function. It takes binary          values, either True or False. If true, print the dimension of the list, else dont.
    """
    top5movies = dataset[start:end]
    for row in top5movies:
        print(row)
    return(top5movies)
    
        

def duplicate_and_unique_movies(dataset, index_):
    """Check the duplicate and unique entries.
    
    We have nested list. This function checks if the rows in the list is unique or duplicated based     on the element at index 'index_'.
    It prints the Number of duplicate entries, along with some examples of duplicated entry.
    
    Keyword arguments:
    dataset -- two dimensional list which we want to explore
    index_ -- column index at which the element in each row would be checked for duplicacy 
    
    """
    unique_list = []
    duplicate_list = []
    for x in dataset:
        compareset = x[index_]
        if compareset in unique_list:
            duplicate_list.append(compareset)
        else:
            unique_list.append(compareset)
    print('Count of duplicate movies:/n', len(duplicate_list))

print("-" *60)
print("\n")    


def movies_lang(dataset, index_, lang_):
    """Extract the movies of a particular language.
    
    Of all the movies available in all languages, this function extracts all the movies in a            particular laguage.
    Once you ahve extracted the movies, call the explore_data() to print first few rows.

    Keyword arguments:
    dataset -- list containing the details of the movie
    index_ -- index which is to be compared for langauges
    lang_ -- desired language for which we want to filter out the movies
    
    Returns:
    movies_ -- list with details of the movies in selected language
    
    """
    movies_ = []

    for i in dataset:
       lang = i[index_]
       if lang == lang_:
          movies_.append(i)    
    print("\nExamples of movies in English Language:\n")
    explore_data(movies_, 0,3)
    return movies_


def rate_bucket(dataset, rate_low, rate_high):
    """Extract the movies within the specified ratings.
    
    This function extracts all the movies that has rating between rate_low and high_rate.
    Once you ahve extracted the movies, call the explore_data() to print first few rows.
    
    Keyword arguments:
    dataset -- list containing the details of the movie
    rate_low -- lower range of rating
    rate_high -- higher range of rating
    
    Returns:
    rated_movies -- list of the details of the movies with required ratings
    """
    rated_movies = []
    for i in dataset:
        rating = float(i[11])
        #print("Rating type", type(i[11]))
        if (rating >= rate_low) and (rating <= rate_high):
            rated_movies.append(i)
    
    explore_data(rated_movies, 0 , 3)
    return rated_movies


# Read the data file and store it as a list 'movies'
opened_file = open(path, encoding="utf8")
read_file = reader(opened_file)
movies = list(read_file)


# The first row is header. Extract and store it in 'movies_header'.
movies_header = movies[0]
print("Movies header:\n", movies_header)
print('-' * 60)
print("\n\n")
# Subset the movies dataset such that the header is removed from the list and store it back in movies
movies = movies [1:]

# Delete wrong data

# Explore the row #4553. You will see that as apart from the id, description, status and title, no other information is available.
# Hence drop this row.
del movies[4553]


# Using explore_data() with appropriate parameters, view the details of the first 5 movies.
explore_data(movies, 0, 5)


# Our dataset might have more than one entry for a movie. Call duplicate_and_unique_movies() with index of the name to check the same.
duplicate_and_unique_movies(movies, 13)



# We saw that there are 3 movies for which the there are multiple entries. 
# Create a dictionary, 'reviews_max' that will have the name of the movie as key, and the maximum number of reviews as values.
reviews_max = {}
for i in movies:
    movie_name = i[13]
    movie_rvw = i[12]
    if movie_name in reviews_max and reviews_max[movie_name] < movie_rvw:
        reviews_max[movie_name] = movie_rvw
    elif movie_name not in reviews_max:
        reviews_max[movie_name] = movie_rvw
#print("Dictionary with the movie name having max no of review \n", reviews_max)
print("Dictionary with the movie name having max no of reviews in count \n", len(reviews_max))

print("\n\n")

# Create a list 'movies_clean', which will filter out the duplicate movies and contain the rows with maximum number of reviews for duplicate movies, as stored in 'review_max'. 

movies_clean = []
comp_set = []

for i in movies:
   mov_name = i[13]
   mov_rvw = i[12]
   if (reviews_max[mov_name] == mov_rvw) and (mov_name not in comp_set):
       movies_clean.append(i)
       comp_set.append(mov_name) 
print("Count of clean movies set is \n", len(movies_clean))
print("--" * 60)
print("\n\n")

# Calling movies_lang(), extract all the english movies and store it in movies_en.

movies_en = movies_lang(movies, 3, 'en')



# Call the rate_bucket function to see the movies with rating higher than 8.

high_rated_movies = rate_bucket(movies_en, 8.0, 10.0)









