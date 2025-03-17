movie_list = ['The Godfather', 'The Shawshank Redemption', 'Pulp Fiction', 'The Dark Knight', 'Forrest Gump']
rating_list = [9.2, 9.3, 8.9, 9.0, 8.8]

movie_rating = dict(zip(movie_list, rating_list))
print(movie_rating)
# Output: {'The Godfather': 9.2, 'The Shawshank Redemption': 9.3, 'Pulp Fiction': 8.9, 'The Dark Knight': 9.0, 'Forrest Gump': 8.8}
# The zip() function takes two lists and combines them into a dictionary. The first list is used as the keys and the second list as the values.
print(list(zip(movie_list, rating_list)))
# Output: [('The Godfather', 9.2), ('The Shawshank Redemption', 9.3), ('Pulp Fiction', 8.9), ('The Dark Knight', 9.0), ('Forrest Gump', 8.8)]
# The zip() function takes two lists and combines them into a list of tuples. The first list is used as the first element of each tuple and the second list as the second element of each tuple.    