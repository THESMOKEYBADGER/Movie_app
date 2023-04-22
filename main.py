import requests
import json
import re
import pulls as pull


def movie_enter():
    
    movie_input = input("Enter the title of the movie you'd like to see: ")
    return movie_input
  

def choose_movie(mylist):
    
    num = 1
      
    for i in mylist:      
        print(num,": ", i.get("title"), i.get("release_date"))
        num+=1
    
    while True:
        try:
            num_pick = int(input("\nEnter the number associated with the movie: "))
            break
        except ValueError:
            print("Please enter a valid numerical character in the range provided:  ")

    return num_pick


def __main__():
    
    mylist = pull.get_movies()

    while len(mylist) == 0:
        print("\n\033[31mERROR: No results found!\033[0m\n")
        mylist = pull.get_movies()
         

    num_pick = choose_movie(mylist)
    pull.get_movie_cast(mylist, num_pick)
    pull.get_movie_details(mylist,num_pick)
    
     

if __name__ == "__main__":
    __main__()
