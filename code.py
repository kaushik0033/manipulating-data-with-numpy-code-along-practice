# --------------
import numpy as np
# Not every data format will be in csv there are other file formats also.
# This exercise will help you deal with other file formats and how toa read it.
from numpy import genfromtxt
my_data = genfromtxt(path, delimiter=',',skip_header=1)
# Number of unique matches 
unique_team = np.unique(my_data[:,0],axis=0)
print("Uniue no of mataches=", unique_team.shape[0])
print("Set of unique_team which played match=", unique_team[:-1])
print("Sum of all extras in all delivery=",np.sum(my_data[:,17].astype(int), axis = 0))
print("Get all deliveries which given player is out,tell wickettype=",my_data[my_data[:,22]!=np.nan][:,11])
toss_won_by_mum=len(my_data[my_data[:,5]=='Mumbai Indians'])
print("Toss won by Mumbai indians=",toss_won_by_mum)
print("Batsman who scored 6 runs",my_data[my_data[:,16].astype(int)>=6].shape[0])
 # How many matches were held in total we need to know so that we can analyze further       statistics keeping that in mind.

# Number of unique teams

 # this exercise deals with you getting to know that which are all those six teams that   played in the tournament.

# Sum of all extras

 # An exercise to make you familiar with indexing and slicing up within data.

# Delivery number when a given player got out

 # Get the array of all delivery numbers when a given player got out. Also mention the wicket type.

# Number of times Mumbai Indians won the toss

 # this exercise will help you get the statistics on one particular team

# Filter record where batsman scored six and player with most number of sixex

 # An exercise to know who is the most aggresive player or maybe the scoring player 







