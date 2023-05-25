"""
Film
Write a program that gets information about a movie from the input 
and presents in the following format:

movie (dir. director) came out in year

The input format:

3 lines: first the title of the movie, 
then the name of the director and then the year of its release.

Sample Input 1:

Fight Club
David Fincher
1999
Sample Output 1:

Fight Club (dir. David Fincher) came out in 1999

"""

# Write your code here
movie = input()
director = input()
year = input()
print(movie + " (dir. " + director + ") came out in " + year)

# Sample Input 1:
# Fight Club
# David Fincher
# 1999
# Sample Output 1:
# Fight Club (dir. David Fincher) came out in 1999
# Sample Input 2:
# Pulp Fiction
# Quentin Tarantino
# 1994

