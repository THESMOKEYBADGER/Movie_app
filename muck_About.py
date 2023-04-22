import requests
import json
import re


def has_letters_and_numbers(name):
        
        pattern = r'[a-zA-Z].*\d|\d.*[a-zA-Z]'
        return bool(re.match(pattern, name))


def moive_choice():

    choice = input("Enter the movie you'd like to see the actors from: ")
    return choice


def get_actors():
  
        url = "https://online-movie-database.p.rapidapi.com/auto-complete"
        querystring = {"q":moive_choice()}

        headers = {
            "X-RapidAPI-Key": "b88b6503e2msh1825cfe7f8c9c5bp13b998jsneda4d70046c5",
            "X-RapidAPI-Host": "online-movie-database.p.rapidapi.com"
        }

        response = requests.request("GET", url, headers=headers, params=querystring)
        
        content = json.loads(response.content)

        formatted_data = json.dumps(content, indent=4)

        actors = set()

        for movie in content.get("d"): 

            if 's' in movie: 
                name = movie.get("s")

                if has_letters_and_numbers(name) == False:              
                    names = [n.strip() for n in name.split(',')]
                    for name in names:
                        if name != '':
                            actors.add(name)
        
        return actors 


def choose_actor():
   
    mylist = list(get_actors())
    
    num = 1
    
    for i in mylist:      
        print(num,": ", i)
        num+=1
    
    while True:
        try:
             actor_choice = input("Enter the number associated wiht the actor: ")
             break
        except ValueError:
             print("Please enter a valid numerical character in the range provided:  ")
        
              

    

    

         

    


def find_all_movies():
     
     return 
     
    
    








def __main__():

    choose_actor()
     

if __name__ == "__main__":
    __main__()
