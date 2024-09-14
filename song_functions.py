def print_main_menu(the_menu):
    """parm: the_menu - a dictionary that stores the user menu options
    this function allows for the dictionary the_menu to work and allows for it to be printed
    """
    print('==========================')
    for i, x in the_menu.items():
        print(f' {i} : {x}')
    print('==========================')

def get_written_date(date_list):
    """
    The function returns the date written out
    """
    x =''
    month_names = {
        1: "January",
        2: "February",
        3: "March",
        4: "April",
        5: "May",
        6: "June",
        7: "July",
        8: "August",
        9: "September",
        10: "October",
        11: "November",
        12: "December",
    }
    # Finish the function
    
    # Return the date string in written format
    if type(date_list) == list:
        l = date_list
        month = int(l[0])
        day = int(l[1])
        day1 = str(day)
        x += month_names[month] + ' ' + day1 +", "+ str(l[2])
        return x
    elif type(date_list) == str:
        l = date_list.split('/')
        month = int(l[0])
        day = int(l[1])
        day1 = str(day)
        x += month_names[month] + ' ' + day1 +", "+ str(l[2])
        return x
    
######## LIST OPTION ########

def get_selection(action, suboptions, to_upper = True, go_back = False):
    """
    param: action (string) - the action that the user
            would like to perform; printed as part of
            the function prompt
    param: suboptions (dictionary) - contains suboptions
            that are listed underneath the function prompt.
    param: to_upper (Boolean) - by default, set to True, so
            the user selection is converted to upper-case.
            If set to False, then the user input is used
            as-is.
    param: go_back (Boolean) - by default, set to False.
            If set to True, then allows the user to select the
            option M to return back to the main menu

    The function displays a submenu for the user to choose from. 
    Asks the user to select an option using the input() function. 
    Re-prints the submenu if an invalid option is given.
    Prints the confirmation of the selection by retrieving the
    description of the option from the suboptions dictionary.

    returns: the option selection (by default, an upper-case string).
            The selection be a valid key in the suboptions
            or a letter M, if go_back is True.
    """
    selection = None
    if go_back:
        if 'm' in suboptions or 'M' in suboptions:
            print("Invalid submenu, which contains M as a key.")
            return None

    while selection not in suboptions:
        print(f"::: What would you like to {action.lower()}?")
        for key in suboptions:
            print(f"{key} - {suboptions[key]}")
        if go_back == True:
            selection = input(f"::: Enter your selection "
                              f"or press 'm' to return to the main menu\n> ")
        else:
            selection = input("::: Enter your selection\n> ")
        if to_upper:
            selection = selection.upper() # to allow us to input lower- or upper-case letters
        if go_back and selection.upper() == 'M':
            return 'M'

    if to_upper:    
        print(f"You selected |{selection}| to",
              f"{action.lower()} |{suboptions[selection].lower()}|.")
    else:
        print(f"You selected |{selection}| to",
          f"{action.lower()} |{suboptions[selection]}|.")
    return selection
def print_song(song, rating_map, title_only = False, showid=False):
    """
    param: song (dict) - a single song dictionary
    param: rating_map (dict) - a dictionary object that is expected
            to have the string keys that correspond to the "rating"
            integer values stored in the song; the stored value is displayed for the
            rating field, instead of the numeric value.
    param: title_only (Boolean) - by default, set to False.
            If True, then only the name of the song is printed.
            Otherwise, displays the formatted song fields.
    param: show_id (Boolean) - by default, set to False.
            If False, then the id number of the song is not displayed.
            Otherwise, displays the id number.

    returns: None; only prints the song values

    Helper functions:
    - get_written_date() to display the 'duedate' field
        You created a similar function in a previous lab.
    """
    # TO-DO: print some or all information of one song (dict),
    #              depending on the options in the parameters
    #    You have to ensure that you use f-strings with the following padding settings:
    #              pad your string labels with 9 spaces and justify right.
    #    To see what these should look like, see further below for example runs.
    if title_only == True and showid == True:
        print(f"      ID: {song['uid']} |   TITLE: {song['title']}")
    if title_only == True and showid == False:
        print(f"   TITLE: {song['title']}")
    if title_only == False and showid == True:
        for i in song:
            if i == 'title':
                if not song['title'] == '':
                    print(f"      ID: {song['uid']} |   TITLE: {song['title']}")
            if i == 'artist':
                if not song['artist'] == '':
                    print(f"  ARTIST: {song['artist']}")
            if i == 'length':
                if not song['length'] == '':
                    print(f"  LENGTH: {song['length']}")
            if i == 'album':
                if not song['album'] == '':
                    print(f"   ALBUM: {song['album']}")
            if i == 'genre':
                if not song['genre'] == []:
                    p = ''
                    for x in song['genre']:
                        p += x.title() + ', '
                    print(f"   GENRE: {p[:-2]}")
            if i == 'rating':
                if not song['rating'] == '':
                    print(f"  RATING: {rating_map[str(song['rating'])]}")
            if i == 'released':
                if not song['released'] == '':
                    date = get_written_date(song['released'].split("/"))
                    print(f"RELEASED: {date}")
            if i == 'favorite':
                if not song['favorite'] == '':
                    print(f"FAVORITE: {song['favorite']}")
        print("*"*42)
    if title_only == False and showid == False:
        for i in song:
            if i == 'title':
                if not 'title' == '':
                    print(f"   TITLE: {song['title']}")     
            if i == 'artist':
                    print(f"  ARTIST: {song['artist']}")
            if i == 'length':
                if not song['length'] == '':
                    print(f"  LENGTH: {song['length']}")
            if i == 'album':
                if not song['album'] == '':
                    print(f"   ALBUM: {song['album']}")
            if i == 'genre':
                if not song['genre'] == []:
                    p = ''
                    for x in song['genre']:
                        p += x.title() + ', '
                    print(f"   GENRE: {p[:-2]}")
            if i == 'rating':
                if not song['rating'] == '':
                    print(f"  RATING: {rating_map[str(song['rating'])]}")
            if i == 'released':
                if not song['released'] == '':
                    date = get_written_date(song['released'].split("/"))
                    print(f"RELEASED: {date}")
            if i == 'favorite':
                if not song['favorite'] == '':
                    print(f"FAVORITE: {song['favorite']}")
        print("*"*42)
                    
    

        
    
def print_songs(song_dict, rating_map, title_only = False, showid = False, fave = False, get_genre = False):
    """
    param: song_dict (dict) - a dictionary containing dictionaries with
            the song data
    param: rating_map (dict) - a dictionary object that is expected
            to have the integer keys that correspond to the "rating"
            integer values stored in the song; the stored value is displayed 
            for the rating field, instead of the numeric value.
    param: title_only (Boolean) - by default, set to False.
            If True, then only the title of the song is printed.
            Otherwise, displays the formatted song fields.
    param: show_id (Boolean) - by default, set to False.
            If False, then the key (unique ID number) of the song is not displayed.
            Otherwise, displays the id number.
    param: fave (Boolean) - by default, set to False, and prints all songs.
            Otherwise, if it is set to True, prints only the songs marked as favorite.
            This parameter is meant to be used exclusive of get_genre
            (i.e. if fave=True, then get_genre should be False, and vice versa).
    param: get_genre (Boolean) - by default, set to False, and prints all songs.
            If set to True, then the function should ask the user for a
            genre keyword (string) and print only those songs that contain that string in its genre value.
            This parameter is meant to be used exclusive of fave (i.e. if fave=True, then get_genre should be False, and vice versa).
            NOTE: If a song has multiple instances of that genre keyword, you should only print the song once.

    returns: None; only prints the song values from the song_list

    Helper functions:
    - print_song() to print individual songs
    """
    
    # Check to see if get_genre is True, so that you can ask for the genre keyword
    print("******************************************")
    if get_genre == True:
        genre = input('Enter genre:: ')
    
   # Go through all the songs in the song dictionary:
    for song in song_dict:
        # if not asking for favorites or specific genres: print everything
        if fave == False and get_genre == False :
            print_song(song_dict[song], rating_map, title_only, showid)
        # otherwise: if asking for favorites, print just those:
        elif fave == True:
            if song_dict[song]["favorite"] == True:
                print_song(song_dict[song], rating_map, title_only, showid)
        # otherwise: if asking for a specific genre, print just those:
        elif get_genre == True:
            for single_genre in song_dict[song]["genre"]:
                if genre in single_genre:
                    print_song(song_dict[song], rating_map, title_only, showid,)
                    break
            # search all the songs' genres for the genre keyword
            # and print only those songs where that keyword appears in the genre value
            # NOTE: You should only print a song *once* 
            # even if the genre keyword appears more than once in it
            
            
        # ... TO DO: fill in the missing parts of this function
def is_valid_addlist(song):
    ''''
    parm: song - a list containing all of the details for a song
    this function checks to see if the addlist is valid by seeing if its a string made up of 9 different sections'''
    if len(song) != 9:
        return False
    for i in song:
        if type(i) != str:
            return False
    return True
def is_valid_title(song):
    '''
    parm: song - a string containing the info for this section
    checks to see if the title is atleast 2 characters and at most 40'''
    if 2 <= len(song) <= 40:
        return True
    else:
        return False
def is_valid_time(song):
    '''
    parm: song - a string containing the info for this section
    this function checks to see that the length of the song is digits and that the middle charcter is :'''
    if len(song) != 5:
        return False
    if song[0].isdigit() == False:
        return False
    if song[1].isdigit() == False:
        return False
    if song[2] != ":":
        return False
    if song[3].isdigit() == False:
        return False
    if song[4].isdigit() == False:
        return False
    return True


def is_valid_date(song):
    '''
    parm: song - a string containing the info for this section
    this function checks to see if the date is valid by seeing if each character is a digit and if it has the slashes inthe right places'''
    date_list = song[6].split("/")
    if not song[0].isdigit():
        return False
    if not song[1].isdigit():
        return False
    if song[2] != "/":
        return False
    if not song[3].isdigit():
        return False
    if not song[4].isdigit():
        return False
    if song[5] != "/":
        return False
    if not song[6].isdigit():
        return False
    if not song[7].isdigit():
        return False
    if not song[8].isdigit():
        return False
    if not song[9].isdigit():
        return False
    if is_valid_day(song) == False:
        return False
    if is_valid_month(song) == False:
        return False
    if is_valid_year(song) == False:
        return False
    return True




def is_valid_day(song):
    '''
    parm: song - a string containing the info for this section
    this function checks to see if the number of days does not exceed the correct amount for each month'''
    song = song.split('/')
    num_days = {
        1: 31,
        2: 28,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31
    }
    if int(song[0]) not in num_days:
        return False
    elif song[1].isdigit() == False:
        return False
    elif int(song[1]) < 1:
        return False
    elif int(song[1]) > num_days[int(song[0])]:
        return False
    elif int(song[1]) == num_days[int(song[0])]:
        return True
    return True
def is_valid_month(song):
    '''
    parm: song - a string containing the info for this section
    this function checks to see if the month number is not over 12 or less than 1'''
    song = song.split('/')
    if song[0].isdigit() == False:
        return False
    elif int(song[0]) > 12 or int(song[0]) < 1:
        return False
    return True
def is_valid_year(song):
    '''
    parm: song - a string containing the info for this section
    this function checks to see if the year is over 1000 and if its a string'''
    song = song.split('/')
    if type(song[2]) == str:
        if int(song[2]) > 1000:
            return True
    return False
        

def is_valid_uid(s, key_list):
    '''
    parm: s - a string containing the uid
    parm: key_list - a list of all keys in the song dictonary
    checks to see if the uid is unique and that its between 10000 and 99999'''
    if s in key_list:
        return False
    if len(s) != 5:
        return False
    if not s.isdigit():
        return False
    if not 10000 <= int(s) <= 99999:
        return False
    return True    

def get_new_song(song, rating_map, key_list):
    """
    parm: song - a list that includes the song
    parm: key_list - a list of all keys in the song dictonary
    parm: rating_map - a dictonary that includes information for the rating
    this function allows for new songs to be implented into the dictonary but it must validate the songs first

    """
    
    if is_valid_addlist(song) == False:
        return ("Bad list. Found non-string, or bad length" , 0)
    if song[2] != '' and is_valid_time(song[2]) == False:
        return ("Invalid time format for Length", -2)
    if song[5] != '1' and song[5] != '2' and song[5] != '3' and song[5] !=  '4' and song[5] != '5' and song[5] != '':
        return ("Invalid Rating value", -3)
    if song[6] != '' and is_valid_date(song[6]) == False:
        return ("Invalid date format for Release Date", -4)
    if song[7] != '' and song[7][0] != 'T' and song[7][0] != 't' and song[7][0] != 'F' and song[7][0] != 'f':
        return ("Invalid value for Favorite", -5)
    if is_valid_uid(song[8], key_list) == False:
        return("Unique ID is invalid or non-unique", -6)
    if is_valid_title(song[0]) == False:
        return ("Bad Title length", -1)
    new_song = {}
    new_song['title'] = song[0]
    new_song['artist'] = song[1]
    new_song['length'] = song[2]
    new_song['album'] = song[3]
    new_song['genre'] = song[4].split(",")
    if song[4] == "":
        new_song["genre"] = []
    if song[5] != '':
        new_song['rating'] = int(song[5])
    else:
        new_song['rating'] = ''
    new_song['released'] = song[6]
    if song[7] == '':
        song[7] == ''
    elif song[7][0] == 'T' or song[7][0] == 't':
        song[7] = True
    elif song[7][0] == 'F' or song[7][0] == 'f':
        song[7] = False
    new_song['favorite'] = song[7]
    new_song['uid'] = int(song[8])
    return new_song
        
    

def edit_song(song_dict, songid, rating_map, field_key, field_info, allkeys):
    """
    param: song_dict (dict) - dictionary of all songs
    param: songid (str) - a string that is expected to contain the key of
            a song dictionary (same value as its unique id)
    param: rating_map (dict) - a dictionary object that is expected
            to have the integer keys that correspond to the "rating"
            integer values stored in the song; the stored value is displayed 
            for the rating field, instead of the numeric value.
    param: field_key (string) - a text expected to contain the name
            of a key in the song dictionary whose value needs to 
            be updated with the value from field_info
    param: field_info (string) - a text expected to contain the value
            to validate and with which to update the dictionary field
            song_dict[field_key]. The string gets stripped of the
            whitespace and gets converted to the correct type, depending
            on the expected type of the field_key.
    param: allkeys (key_list) - a key_list of all keys in the song dictionary.

    The function first calls some of its helper functions
    to validate the provided field.
    If validation succeeds, the function proceeds with the edit.

    return:
    If song_dict is empty, return 0.
    If the field_key is not a string, return -1.
    If the remainder of the validation passes, return the dictionary song_dict[songid].
    Otherwise, return the field_key.

    Helper functions:
    The function calls the following helper functions depending on the field_key:
    - is_valid_title()
    - is_valid_time()
    - is_valid_date()
    - is_valid_uid()
    """
    if song_dict == {}:
        return 0
    if type(field_key) != str:
        return -1
    
    if field_key == 'title':
        if is_valid_title(field_info) == False:
            return field_key
        else:
            song_dict[songid]['title'] = field_info
    elif field_key == 'length':
        if is_valid_time(field_info) == False:
            return field_key
        else:
            song_dict[songid]['length'] = field_info
    elif field_key == 'released':
        if is_valid_date(field_info) == False:
            return field_key
        else:
            song_dict[songid]['released'] = field_info
    elif field_key == 'uid':
        if is_valid_uid(field_info) == False:
            return field_key
        else:
            song_dict[songid]['uid'] = field_info

    
    return song_dict[songid]

def delete_song(song_dict, songid):
    """
    param: song_dict - a dictionary of songs (dict of dict)
    param: songid (str) - a string that is expected to
            contain the key to a song dictionary (i.e. same as its unique ID)

    The function first checks if the dictionary of songs is empty.
    The function then validates the song ID to verify
    that the provided ID key can access an element from song_dict
    On success, the function saves the item's "title" from song_dict
    and returns that string ("title" value)
    after the item is deleted from song_dict.

    returns:
    If the input list is empty, return 0.
    If the ID is not valid (i.e. not found in the song_dict), return -1.
    Otherwise, on success, the entire song is removed from song_dict
    and the function returns the title of the deleted song.
    """
    if song_dict == {}:
        return 0
    if songid in song_dict:
        title = song_dict[songid]['title']
        del song_dict[songid]
        return title
    else:
        return -1

def do_stats(song_dict, opt):
    """
    param: song_dict - a dictionary of songs (dict of dict)
    param: opt (str) - an option from the menu
    to do one of the following statistical calculations:
        "A" - find the mean (average) of all song ratings values
        "B" - find the median of all song ratings values
        "C" - find the standard deviation of all song ratings values
        "D" - print out a histogram of all song ratings values

    Helpful hint: see example on top of page in
    zyBook Ch. 8.4 to see how to do mean and stddev calculations.

    returns: Nothing! This function only PRINTS out results.    
    """
    if opt.upper() == "A":
        sum1 = 0
        number = 0
        for i in song_dict:
            sum1 += song_dict[i]['rating']
            number += 1
        mean = round(sum1/number, 2)
        print(f'The mean value of all ratings is: {mean}')
        


    if opt.upper() == "B":
        median = 0
        ratings = [song_dict[i]['rating'] for i in song_dict]
        middle = sorted(ratings)
        if(len(middle)%2!=0):
            median += round(middle[len(middle)//2], 2)
        else:
            med1 = middle[len(middle)//2]
            med2 = middle[len(middle)//2 - 1]
            median += round((med1 + med2)/2, 2)

        median = str(median)
        if (len(median.split(".")[1]) != 2):
            median = str(median) + "0"
        print(f'The median value of all ratings is: {median}')





    if opt.upper() == "C":
        rate = 0
        deviation = [song_dict[i]['rating'] for i in song_dict]
        sum1 = 0
        number = 0
        for i in song_dict:
            sum1 += song_dict[i]['rating']
            number += 1
        mean = sum1/number
        for d in deviation:
            rate += (d - mean )**2

        std_dev = (rate/len(deviation))**0.5
        std = round(std_dev, 2)
        print(f'The standard deviation value of all ratings is: {std}')
    if opt.upper() == "D":
        ratings = [song_dict[i]['rating'] for i in song_dict]
        dic = {1:0, 2:0, 3:0, 4:0, 5:0}
        for i in ratings:
            dic[i] += 1
        for i in [1,2,3,4,5]:
            print(i, "*"*dic[i])





def save_to_csv(song_dict, filename):
    """
    param: song_dict(dict of dict) - The dictionary of songs stored 
    param: filename (str) - A string that ends with '.csv' which represents
               the name of the file to which to save the songs. This file will
               be created if it is not present, otherwise, it will be overwritten.

    The function ensures that the last 4 characters of the filename are '.csv'.
    The function requires the `import csv` as well as `import os`.

    The function will use the `with` statement to open the file `filename`.
    After creating a csv writer object, the function uses a `for` loop
    to loop over every song in the dictionary and creates a new list
    containing only strings - this list is saved into the file by the csv writer
    object. The order of the elements in the dictionary is:

    * title
    * artist
    * length
    * album
    * genre (all element in the original list are converted to string
        joined with commas separating)
    * rating (converted to string)
    * released (written as string, i.e, "06/06/2022", NOT "June 6, 2022")
    * favorite (converted to string)
    * uid

    returns:
    -1 if the last 4 characters in `filename` are not '.csv'
    None if we are able to successfully write into `filename`
    """
    import csv
    if filename[-4:] == '.csv': 
        with open(filename, 'w', newline='') as myfile:
            writer = csv.writer(myfile)
            for dictionary in song_dict:
                new_list = []
                for i in song_dict[dictionary]:
                    if i == 'genre':
                        p = ""
                        for gen in song_dict[dictionary][i]:
                            p += gen
                            p += ","
                        p = p[:-1]
                        new_list.append(p)
                        continue
                    new_list.append(song_dict[dictionary][i])
                writer.writerow(new_list)
    else:
        return -1

def load_from_csv(filename, in_dict, rating_map, allkeys):
    """
    param: filename (str) - A string variable which represents the
            name of the file from which to read the contents.
    param: in_dict (dict of dict) - A dictionary of songs (dictionary objects) to which
            the songs read from the provided filename are added.
            If in_dict is not empty, the existing songs are not dropped.
    param: rating_map (dict) - a dictionary object that is expected
            to have the integer keys that correspond to the "rating"
            integer values stored in the song; the stored value is displayed 
            for the rating field, instead of the numeric value.
    param: allkeys (key_list) - a key_list of all keys in the song dictionary

    The function ensures that the last 4 characters of the filename are '.csv'.
    The function requires the `import csv` and `import os`.

    If the file exists, the function will use the `with` statement to open the
    `filename` in read mode. For each row in the csv file, the function will
    proceed to create a new song using the `get_new_song()` function.
    - If the function `get_new_song()` returns a valid song object,
    it gets added to `in_dict`.
    - If the `get_new_song()` function returns an error, the 1-based
    row index gets recorded and added to the NEW list that is returned.
    E.g., if the file has a single row, and that row has invalid song data,
    the function would return [1] to indicate that the first row caused an
    error; in this case, the `in_dict` would not be modified.
    If there is more than one invalid row, they get excluded from the
    in_dict and their indices will be appended to the new list that's
    returned.

    returns:
    * -1, if the last 4 characters in `filename` are not '.csv'
    * None, if `filename` does not exist.
    * A new empty list, if the entire file is successfully read from `in_dict`.
    * A list that records the 1-based index of invalid rows detected when
      calling get_new_song().

    Helper functions:
    - get_new_song()
    """
    import csv, os
    if filename[-4:] == '.csv':
        if os.path.exists(filename):
            with open(filename, 'r') as myfile:
                    reader = csv.reader(myfile, delimiter = ",")
                    new_list = []
                    row_num = 0
                    for row in reader:
                        row_num+=1
                
                        song_file = get_new_song(row, rating_map, allkeys)
                        if type(song_file) == tuple:
                            new_list.append(row_num)
                        elif type(song_file) == dict:
                            in_dict[str(song_file['uid'])] = song_file
                    return new_list
        return None
    return -1



