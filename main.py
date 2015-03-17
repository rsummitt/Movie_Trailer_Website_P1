import webbrowser
import os
from utils.html_generator import main_page_head
from utils.html_generator import main_page_content
from utils.html_generator import create_movie_tiles_content
from utils.html_generator import create_tv_show_tiles_content
from utils.media_collection import get_collection


def open_movies_page(collection):
    """Creates html file based on a collection and opens it in a new browser tab"""
    # Create or overwrite the output file
    output_file = open('RobsCollection.html', 'w')

    # Replace the placeholder for the movie tiles with the actual dynamically generated content
    rendered_content = main_page_content.format(movie_tiles=create_movie_tiles_content(collection.get('movies')),
                                                tv_show_tiles=create_tv_show_tiles_content(collection.get('tv_shows')))

    # Output the file
    output_file.write(main_page_head + rendered_content)
    output_file.close()

    # open the output file in the browser
    url = os.path.abspath(output_file.name)
    webbrowser.open('file://' + url, new=2)  # open in a new tab, if possible

open_movies_page(get_collection())
