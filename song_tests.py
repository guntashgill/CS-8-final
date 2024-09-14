

from song_functions import *

rating_map = {
    "1": "Hate",
    "2": "Dislike",
    "3": "Neutral",
    "4": "Like",
    "5": "Love!"
    }

addlist_4 = ["H", "Taylor Swift", "03:59", "Folklore", "folk, indie rock", 4, "07/27/2020", "True", "12332"]

addlist_5 = ["H", "Taylor Swift", "03:59", "Folklore", "folk, indie rock", "7", "07/27/2020", "True", "14680"]

addlist_6 = ["H", "Taylor Swift", "03:59", "Folklore", "folk, indie rock", "4", "07/27/2020", "True", "15790"]
addlist_7 = ["H", "Taylor Swift", "03:59", "Folklore", "folk, indie rock", "4", "07/27/2020", "True", "12332"]


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


assert get_written_date('01/03/1970') == "January 3, 1970"
assert get_written_date('02/10/2022') == "February 10, 2022"
assert get_written_date('03/22/2010') == "March 22, 2010"



assert is_valid_addlist(addlist_4) == False
assert is_valid_addlist(addlist_5) == True
assert is_valid_addlist('this_is_a_string') == False

assert is_valid_title("hello") == True
assert is_valid_title("H") == False
assert is_valid_title("") == False

assert is_valid_time("11:23") == True
assert is_valid_time("21:b7") == False
assert is_valid_time("22:45") == True

assert is_valid_date("11/12/2022") == True
assert is_valid_date("12/b4/2022") == False
assert is_valid_date("12/12/1000") == False

assert is_valid_day("11/12/2022") == True
assert is_valid_day("11/34/2022") == False
assert is_valid_day("11/00/2022") == False

assert is_valid_month("12/12/2012") == True
assert is_valid_month("13/12/2012") == False
assert is_valid_month("14/12/2012") == False

assert is_valid_year("12/20/2022") == True
assert is_valid_year("12/20/999") == False
assert is_valid_year("10/20/2012") == True

assert is_valid_uid("34987", all_songs.keys()) == True
assert is_valid_uid("1000", all_songs.keys()) == False
assert is_valid_uid("100000", all_songs.keys()) == False

assert get_new_song(addlist_7, rating_map, all_songs.keys()) == ("Unique ID is invalid or non-unique", -6)
assert get_new_song(addlist_5, rating_map, all_songs.keys()) == ("Invalid Rating value", -3)
assert get_new_song(addlist_6, rating_map, all_songs.keys()) == ("Bad Title length", -1)


assert edit_song({}, '12345', rating_map, 'rating', '3', all_songs.keys()) == 0
assert edit_song(all_songs, '14567', rating_map, 12, '3', all_songs.keys()) == -1
assert edit_song(all_songs, '14567', rating_map, 'length', 'B0:U7', all_songs.keys()) == 'length'


assert save_to_csv(all_songs, 'hello') == -1
assert save_to_csv(all_songs, 'coding') == -1
assert save_to_csv(all_songs, 'coding.csv') == None


assert load_from_csv('file.cs', all_songs, rating_map, all_songs.keys()) == -1
assert load_from_csv('haha.csv', all_songs, rating_map, all_songs.keys()) == None
assert load_from_csv('hehe.csv', all_songs, rating_map, all_songs.keys()) == None


assert delete_song({}, '12345') == 0
assert delete_song(all_songs, '12345') == -1
assert delete_song(all_songs, '55555') == -1





