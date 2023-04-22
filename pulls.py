import requests
import json
import re
import main


class Getter:
     
    def __init__(self):      
        self.base_url = 'https://api.themoviedb.org/3/'

    def make_request(self,link):
         
        response = requests.request("GET",self.base_url + link)
        
        content = json.loads(response.content)

        return content
    
    
    def get_movies(self,movie_input):

        link  = f"search/movie?api_key=ff475e50eb788ac007dc0eb0bddede94&language=en-US&query={movie_input}&page=1&include_adult=false"
        
        return self.make_request(link)

    def get_cast(self,movie_id):

        link  = f"movie/{movie_id}/credits?api_key=ff475e50eb788ac007dc0eb0bddede94&language=en-US"
        
        return self.make_request(link)



getter_instance = Getter()       
         

def get_movies():
     
    movie_input =  main.movie_enter()

    content = getter_instance.get_movies(movie_input)

    formatted_data = json.dumps(content, indent=4)

    movies_list = list()

    for movie in content.get("results"): 

            if 'title' in movie: 
               
                movies_list.append(movie)
     
    return movies_list



def get_movie_cast(mylist,num_pick):


    movie_id = mylist[num_pick-1]["id"]
    
    content = getter_instance.get_cast(movie_id)


    actors = list()

    for person in content.get("cast"):
        if "known_for_department" in person:
            actor_name = person.get("name")
            actors.append(actor_name)

    print(actors)



def get_movie_details(mylist,num_pick):
         
    movie_id = mylist[num_pick-1]["id"]

    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=ff475e50eb788ac007dc0eb0bddede94&language=en-US"

    response = requests.request("GET", url)

    content = json.loads(response.content)

    formatted_data = json.dumps(content, indent=4)

    print(formatted_data)