class Video():
    """This is the base class for different media types (eg. Movie and TVShow)"""
    def __init__(self, title, description, img, trailer_youtube_url):
        self.title = title
        self.description = description
        self.img = img
        self.trailer_youtube_url = trailer_youtube_url

