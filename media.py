import webbrowser


class Movie():
    """ This class provides a way to store movie related information"""
    # VALID_RATINGS = ["G", "PG", "PG-13", "R"]
    """ This function initializes variables that store movie information"""
    def __init__(self, movie_title, movie_release, movie_genre,
                 movie_storyline, movie_cast, poster_image,
                 trailer_youtube):
        self.title = movie_title
        self.release = movie_release
        self.genre = movie_genre
        self.storyline = movie_storyline
        self.cast = movie_cast
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
    """ This function opens youtube url of the trailer"""
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
