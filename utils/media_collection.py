from media.movie import Movie
from media.tv_show import TVShow

# This script contains methods to generate a media collection


# Returns
def get_collection():
    """Returns a generated dictionary of movies and tv shows"""
    return generate_dictionary()


def generate_dictionary():
    """Generates movie and tv show collections and returns them as a dictionary"""
    movie_collection = generate_movie_collection()
    tv_show_collection = generate_tv_show_collection()
    return {"movies": movie_collection, "tv_shows": tv_show_collection}


def generate_movie_collection():
    """Generates and Returns a movie collection"""
    toy_story = Movie("Toy Story",
                      "A story of a boy and his toys that come to life",
                      "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                      "https://www.youtube.com/watch?v=vwyZH85NQC4",
                      "81 minutes",
                      "11/22/1995")

    avatar = Movie("Avatar",
                   "A marine on an alien planet",
                   "http://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                   "https://www.youtube.com/watch?v=5PSNL1qE6VY",
                   "161 mintues",
                   "12/18/2009")

    gangs_of_new_york = Movie("Gangs of New York",
                              "Gangs fighting over territory in New York in 1863",
                              "http://upload.wikimedia.org/wikipedia/en/a/ae/Gangs_of_New_York_Poster.jpg",
                              "https://www.youtube.com/watch?v=1_CDJiYux1A",
                              "160 minutes",
                              "12/20/2002")

    boiler_room = Movie("Boiler Room",
                        "Welcome to the new American Dream",
                        "http://upload.wikimedia.org/wikipedia/en/5/5c/Boiler_room_ver3.jpg",
                        "https://www.youtube.com/watch?v=6VoXMvNrQro",
                        "120 minutes",
                        "2/18/2000")

    inception = Movie("Inception",
                      "Your mind is the scene of the crime",
                      "http://upload.wikimedia.org/wikipedia/en/7/7f/Inception_ver3.jpg",
                      "https://www.youtube.com/watch?v=66TuSJo4dZM",
                      "148 minutes",
                      "7/16/2010")

    shutter_island = Movie("Shutter Island",
                           "Some places never let you go",
                           "http://upload.wikimedia.org/wikipedia/en/7/76/Shutterislandposter.jpg",
                           "https://www.youtube.com/watch?v=5iaYLCiq5RM",
                           "138 minutes",
                           "2/19/2010")

    return [toy_story, avatar, gangs_of_new_york, boiler_room, inception, shutter_island]


def generate_tv_show_collection():
    """Generates and returns a TV show collection"""
    game_of_thrones = TVShow("Game of Thrones",
                             "A struggle for power in a kingdom where all lust for it",
                             "http://upload.wikimedia.org/wikipedia/en/d/d8/Game_of_Thrones_title_card.jpg",
                             "www.youtube.com/watch?v=522l0YE9hRQ",
                             "4/17/2011",
                             "40")

    house_of_cards = TVShow("House of Cards",
                            "Frank Underwood will do whatever it takes to rise to the top",
                            "http://upload.wikimedia.org/wikipedia/en/3/3f/House_of_Cards_title_card.png",
                            "https://www.youtube.com/watch?v=ULwUzF1q5w4",
                            "2/1/2013",
                            "39")

    return [game_of_thrones, house_of_cards]

