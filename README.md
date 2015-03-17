# Movie Trailer Website
## How to run this project
To run this application use the following command

```
python main.py
```

## Project Structure
__media__

This directory contains all the classes necessary to create movie and tv show instances.
Video is the base class and Movie and TVShow inherit from it.

__utils__

Contains the html_generator module which helps build html based on a collection using templates.
It also contains the media_collection module that generates a collection of static movies and
TV shows.

__main.py__

The main module contains a method that utilizes the html_generator module to generate an html file
and open this file into a new tab in a browser.

## Additions to Project
This project contains two types of media including TV shows and movies.  Movies will display their
duration while TV shows will display the number of episodes.  The banner also has been changed to
"Rob's Favorite Movies and Shows".  The TV Show template has been modified to display shows cards
without distortion.

## Purpose
This project is the result of an assignment for the Udacity Full Stack Web Developer Nanodegree


