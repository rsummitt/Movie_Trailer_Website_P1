from video import Video


class Movie(Video):
    """Class representing a Movie that inherits from Video"""
    def __init__(self, title, description, img, trailer_youtube_url, duration, release_date):
        """Movie constructor that takes parameters pertaining to a movie"""
        Video.__init__(self, title, description, img, trailer_youtube_url)
        self.duration = duration
        self.release_date = release_date
