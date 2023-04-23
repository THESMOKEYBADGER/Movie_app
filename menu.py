import main as main

class menu:

    def print_menu(mylist,num_pick):

        while True:

            # Display the menu options
            print("\n\x1b[34m-------------------------------\x1b[0m")
            print("Menu:")
            print("1. See movie Detials")
            print("2. See Cast")
            print("3. Option 3")
            print("4. Quit" )
            print("\x1b[34m-------------------------------\x1b[0m")

            choice = input("Enter your choice: " + "\n")

            print("\033[F\033[K", end="")
            print("\033[F\033[K", end="")

            if choice == '1': 
                print("\n" "Option 1 selected." "\n" )
                main.print_movie_details(mylist,num_pick)
                

            elif choice == "2":
                print("\n" "Option 2 selected." "\n" )
                main.print_actors(mylist,num_pick)
                

            elif choice == "3":
                # Do something for option 3
                return
                
            
            elif choice == "4":
                # Quit the program
                print("Quitting...")
                break
                
            else:
                # Handle invalid input
                print("\n\033[31mInvalid choice. Please try again.\033[0m")
        


