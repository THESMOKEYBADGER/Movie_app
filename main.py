import os
import curses
import time
import pulls as pull
import menu as menu


def movie_enter():

    movie_input = input("\n" + "Enter the title of the movie you'd like to see: ")
    return movie_input


def choose_movie(mylist):

    this_list = mylist[:15]

    if len(mylist) <= 10:
        print(f"Here are the {len(mylist)} movies:\n")

    elif len(mylist) >= 15:
        print("Here are the top 15 results:\n")

    max_name_len = max(len(movie['title']) for movie in this_list)

    for movie in this_list:
        year = movie['release_date'][:4] if movie['release_date'] else 'Unknown'
        print(f"-> {movie['title']:<{max_name_len}} {year}")

    if len(mylist) >= 1:
        print("\n\033[32mResults found!\033[0m\n")


    print("Would you like to re-enter the title for a different set of results?")
    print("Y for yes, or any other key for no...")

    choice = (input().upper())

    if choice == "Y":

        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")
        
        movie_enter()
        choose_movie(mylist)

    print("\033[F\033[K", end="")
    print("\033[F\033[K", end="")
    print("\033[F\033[K", end="")


    while True:
        try:
            num_pick = int(
                input("Enter the number associated with the movie: "))
            if num_pick > len(mylist):
                print(
                    "\033[31mPlease enter a valid number in the range provided.\033[0m")
                continue
            break
        except ValueError:
            print("Please enter a valid numerical character in the range provided:  ")

    print(f"\n\033[32m{mylist[num_pick]['title']}\033[0m\n")

    return num_pick


def print_actors(mylist, num_pick):

    print("\n" + f"Here are the top acotors in \033[32m{mylist[num_pick]['title']}\033[0m:\n")

    actors = pull.get_movie_cast(mylist, num_pick)

    

    for actor in actors:
        print("- ", actor)


def print_movie_details(mylist, num_pick):

    data = pull.get_movie_details(mylist, num_pick)

    title = data.get("title")
    overview = data['overview']
    release_date = data['release_date']
    run_time = data['runtime']
    production_companies = [company['name']
                            for company in data['production_companies']]

    revenue = format(int(data['revenue']), ',')

    print("\n" + "Title:", f"\033[32m{title}\033[0m")
    print("Overview:", overview)
    print("Release date:", release_date,)
    print("Run time:", run_time,  " minutes")
    print("Production companies:", ", ".join(production_companies))
    print("Revenue: $", revenue + "/n")


def __main__():

    mylist = pull.get_movies()

    while len(mylist) == 0:
        print("\n\033[31mERROR: No results found!\033[0m\n")
        mylist = pull.get_movies()

    num_pick = choose_movie(mylist)

    menu.menu.print_menu(mylist, num_pick)

    # print_movie_details(mylist, num_pick)

    # print_actors(mylist, num_pick)


if __name__ == "__main__":
    __main__()
