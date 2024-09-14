from song_functions import *

all_songs = {
    "12332": {
      "title": "Cardigan",
      "artist": "Taylor Swift",
      "length": "03:59",
      "album": "Folklore",
      "genre": ["folk", "indie rock"],
      "rating": 4,
      "released": "07/27/2020",
      "favorite": True,
      "uid" : 12332
      },
   "14567": {
      "title": "Soul Meets Body",
      "artist": "Death Cab for Cutie",
      "length": "",
      "album": "Plans",
      "genre": ["indie pop", "indie rock"],
      "rating": 5,
      "released": "07/16/2005",
      "favorite": True,
      "uid":14567
      },
   "78210": {
      "title": "Fake Love",
      "artist": "BTS",
      "length": "04:02",
      "album": "",
      "genre": ["hip hop", "electro pop", "Korean pop"],
      "rating": 3,
      "released": "05/18/2018",
      "favorite": False,
      "uid":78210
      },
    "99105": {
      "title": "Foil",
      "artist": "'Weird Al' Yankovic",
      "length": "02:22",
      "album": "Mandatory Fun",
      "genre": ["pop", "parody"],
      "rating": 5,
      "released": "07/15/2014",
      "favorite": True,
      "uid": 99105
      }
    }



the_menu ={
    "L" : "List",
    "A" : "Add",
    "E" : "Edit",
    "D" : "Delete",
    "M" : "Show statistical data on",
    "S" : "Save the data to file",
    "R" : "Restore data from file",
    "Q" : "Quit this program"
     }# TODO 1: add the options from the instructions

list_menu = {
    "A": "all songs - full",
    "B": "all songs - titles only",
    "F": "favorite songs",
    "G": "songs of a specific genre"
    }

rating_map = {
    "1": "Hate",
    "2": "Dislike",
    "3": "Neutral",
    "4": "Like",
    "5": "Love!"
    }
opt = None

while True:
    print_main_menu(the_menu) # TODO 2: define the function, uncomment, and call with the menu as an argument
    opt = input("::: Enter a menu option\n> ")
    opt = opt.upper() # to allow us to input lower- or upper-case letters
    
    if opt not in the_menu: # TODO 3: check of the character stored in opt is in the_menu dictionary
        print(f"WARNING: {opt} is an invalid menu option.\n")
        continue
    else:
        print(f"You selected option {opt} to > {the_menu[opt]}.")

    if opt == 'Q': # TODO 4: quit the program
        print("Goodbye!\n")
        break # exit the main `while` loop
    elif opt == 'L':
        if all_songs == {}:
            print("WARNING: There is nothing to display!")
            # Pause before going back to the main menu
            input("::: Press Enter to continue")
            continue

        subopt = get_selection(the_menu[opt], list_menu)
        print('******************************************')
        if subopt == 'A':
            print_songs(all_songs, rating_map, showid = True)
        elif subopt == 'B':
            print_songs(all_songs, rating_map, title_only = True)
        elif subopt == 'F':
            print_songs(all_songs, rating_map, fave = True)
        elif subopt == 'G':
            print_songs(all_songs, rating_map, get_genre = True)
    elif opt == 'A':
        continue_action = 'y'
        while continue_action == 'y':
            song_info = []
            print("::: Enter each required field:")
            # TODO: Get user inputs for all 9 song info fields (i.e. keys). 
            # Get *all* inputs as strings.
            song_info.append(input("Title: "))
            song_info.append(input("Artist: "))
            song_info.append(input("Length: "))               
            song_info.append(input("Album: "))
            song_info.append(input("Genre: "))
            song_info.append(input("Rating: "))
            song_info.append(input("Released: "))
            song_info.append(input("Favorite: "))
            song_info.append(input("uid: "))

            result = get_new_song(song_info, rating_map, all_songs.keys()) # TODO: attempt to create a new song
            if type(result) == dict:
                all_songs[str(result['uid'])] = result # TODO: add a new song to the list of songs
                print(f"Successfully added a new song!")
                print_song(result, rating_map)
            elif type(result) == tuple:
                print(f"WARNING: invalid data!")
                print(f"Error: {result[0]}")

            print("::: Would you like to add another song?", end=" ")
            continue_action = input("Enter 'y' to continue.\n> ")
            continue_action = continue_action.lower() 
    elif opt == 'E':
        continue_action = 'y'
        while continue_action == 'y':
            if all_songs == {}: # TODO
                print("WARNING: There is nothing to edit!")
                break
            print("::: Song list:")
            print('******************************************')
            print_songs(all_songs, rating_map, title_only = True, showid = True)
            print("::: Enter the song ID you wish to edit.")
            user_option = input(">")
            if user_option in all_songs: # TODO - check to see if that ID is in the song dictionary
                subopt = get_selection("edit", all_songs[user_option], to_upper = False, go_back = True)
                if subopt == 'M': # if the user changed their mind
                    break
                print(f"::: Enter a new value for the field |{subopt}|") # TODO
                field_info = input(">")
                result = edit_song(all_songs, user_option, rating_map, subopt, field_info, all_songs.keys()) #TODO
                if type(result) == dict:
                    print(f"Successfully updated the field |{subopt}|:")  # TODO
                    print_song(result, rating_map)  # TODO
                else: # edit_song() returned an error
                    print(f"WARNING: invalid information for the field |{subopt}|!")  # TODO
                    print(f"The song was not updated.")
            else: # song ID is incorrect/invalid
                print(f"WARNING: |{user_option}| is an invalid song ID!")  # TODO

            print("::: Would you like to edit another song?", end=" ")
            continue_action = input("Enter 'y' to continue.\n> ")
            continue_action = continue_action.lower()      
            # ----------------------------------------------------------------
            # ----------------------------------------------------------------
    elif opt == 'D':
        continue_action = 'y'
        while continue_action == 'y':
            if all_songs == {}:
                print("WARNING: There is nothing to delete!")
                break
            print("******************************************")
            print_songs(all_songs, rating_map, title_only = True, showid = True)
            print("Which song would you like to delete?")
            print("X - Delete all songs at once")
            print("::: OR Enter the number corresponding to the song ID")
            print("::: OR press 'M' to cancel and return to the main menu.")
            delete_option = input(">")
            if delete_option == 'X':
                print("::: WARNING! Are you sure you want to delete ALL songs?")
                print("::: Type Yes to continue the deletion.")
                delete_choice = input('>')
                if delete_choice == 'Yes':
                    all_songs = {}
                    print("Deleted all songs.")
                    print("::: Press Enter to continue")
            elif delete_option == 'M':
                   break
            elif delete_option not in all_songs:
                    print(f"WARNING: |{delete_option}| is an invalid song ID!")
            else:
                if delete_option in all_songs:
                    song_deleted = all_songs[delete_option]['title']
                    result = delete_song(all_songs, delete_option)
                    if result == 0:
                        print("WARNING: There is nothing to delete!")
                    else:
                        print("Success!")
                        print(f"Deleted the song |{song_deleted}|")
                
            print("::: Would you like to delete another song?", end=" ")
            continue_action = input("Enter 'y' to continue.\n> ")
            continue_action = continue_action.lower()

    elif opt == 'M':
        continue_action = 'y'
        while continue_action == 'y':
            print("::: What would you like to show statistical data on?")
            print("A - Mean value of all song ratings")
            print("B - Median value of all song ratings")
            print("C - Standard Deviation value of all song ratings")
            print("D - Histogram of all song ratings")
            subopt = do_stats(all_songs, opt)
            if subopt == "A":
                do_stats(all_songs, opt == "A")
                print("You selected |A| to show statistical data on |mean value of all song ratings|.")
            if subopt == "B":
                do_stats(all_songs, opt == "B")
                print("You selected |B| to show statistical data on |median value of all song ratings|.")
            if subopt == "C":
                do_stats(all_songs, opt == "C")
                print("You selected |C| to show statistical data on |standard deviation value of all song ratings|.")
            if subopt == "D":
                do_stats(all_songs, opt == "D")
                print("You selected |D| to show statistical data on |histogram of all song ratings|.")
            print("::: Would you like to get different statistics?")
            continue_action = input("Enter 'y' to continue.\n> ")
            continue_action = continue_action.lower()            
            
        
    elif opt == 'S':
        continue_action = 'y'
        while continue_action == 'y':
            print("::: Enter the filename ending with '.csv'.")
            filename = input("> ")
            save = save_to_csv(all_songs, filename) # TODO: Call the function with appropriate inputs and capture the output
            if  save == -1: # TODO
                print(f"WARNING: |{filename}| is an invalid file name!") # TODO
                print("::: Would you like to try again?", end=" ")
                continue_action = input("Enter 'y' to try again.\n> ")
            else:
                print(f"Successfully stored all the songs to |{filename}|")
                continue_action = 'n'

    elif opt == 'R':
        continue_action = 'y'
        while continue_action == 'y':
            print("::: Enter the filename ending with '.csv'.")
            file_name = input(">")
            restore = load_from_csv(file_name, all_songs, rating_map, all_songs.keys())
            if restore == -1:
                print(f"WARNING: invalid input - must end with '.csv'")
                print("::: Would you like to try again?", end=" ")
                
            elif restore == None:
                print(f"WARNING: |{file_name}| was not found!")
                print("::: Would you like to try again?", end=" ")
            elif restore == []:
                print(f"Successfully restored all songs from |{file_name}|")
                continue_action = 'n'
            else:
                print(f"WARNING: |{file_name}| contains invalid data!")
                print("The following rows from the file were not loaded:")
                print(restore)
            continue_action = input("Enter 'y' to try again.\n> ")
                
        
        
                
           


    # Pause before going back to the main menu
    input("::: Press Enter to continue")

print("Have a nice day!")
