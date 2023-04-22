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


def print_actors(mylist, num_pick):

    actors = pull.get_movie_cast(mylist, num_pick)

    num = 1

    for actor in actors:
        print(num,": ", actor)
        num+=1


def print_movie_details(mylist, num_pick):

    data = pull.get_movie_details(mylist, num_pick)

    title = data.get("title")
    overview = data['overview']
    release_date = data['release_date']
    run_time = data['runtime']
    production_companies = [company['name'] for company in data['production_companies']]
    revenue = format(int(data['revenue']), ',')

    print("Title:", title)
    print("Overview:", overview)
    print("Release date:", release_date,)
    print("Run time:", run_time,  " minutes")
    print("Production companies:", ", ".join(production_companies))
    print("Revenue: $", revenue)



def __main__():
    
    mylist = pull.get_movies()

    while len(mylist) == 0:
        print("\n\033[31mERROR: No results found!\033[0m\n")
        mylist = pull.get_movies()

    if len(mylist) >= 1:
        print("\n\033[32mYResults found!\033[0m\n")

         

    num_pick = choose_movie(mylist)

    print_movie_details(mylist, num_pick)
    
    print_actors(mylist, num_pick)
    
    
    

if __name__ == "__main__":
    __main__()