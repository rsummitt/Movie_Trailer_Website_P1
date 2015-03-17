from video import Video


class TVShow(Video):
    """Class representing TVShow which inherits from Video"""
    def __init__(self, title, description, img, trailer_youtube_url, start_date, num_episodes):
        """TVShow constructor that takes parameters pertaining to a tv show"""
        Video.__init__(self, title, description, img, trailer_youtube_url)
        self.start_date = start_date
        self.num_episodes = num_episodes
