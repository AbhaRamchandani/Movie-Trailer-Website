import my_fav_movies
import media

# This file contains movie information for all the movies on the website
# This is the python file that must be executed to open the page

###############################################################################

kung_fu_panda = media.Movie(
    "Kung Fu Panda", "2008", "Anime",
    "In the Valley of Peace, Po the Panda finds himself chosen as the Dragon "
    "Warrior despite the fact that he is obese and a complete novice at "
    "martial arts.",
    "Jack Black, Ian McShane, Angelina Jolie",
    "https://upload.wikimedia.org/wikipedia/en/7/76/Kungfupanda.jpg",
    "https://www.youtube.com/watch?v=PXi3Mv6KMzY")

###############################################################################

despicable_me = media.Movie(
    "Despicable Me", "2010", "Anime",
    "When a criminal mastermind uses a trio of orphan girls as pawns for a "
    "grand scheme, he finds their love is profoundly changing him for the "
    "better.",
    "Steve Carell, Jason Segel, Russell Brand",
    "https://upload.wikimedia.org/wikipedia/en/d/db/Despicable_Me_Poster.jpg",
    "https://www.youtube.com/watch?v=sUkZFetWYY0")

###############################################################################

frozen = media.Movie(
    "Frozen", "2013", "Anime",
    "When the newly crowned Queen Elsa accidentally uses her power to turn "
    "things into ice to curse her home in infinite winter, her sister, Anna, "
    "teams up with a mountain man, his playful reindeer, and a snowman to "
    "change the weather condition.",
    "Kristen Bell, Idina Menzel, Jonathan Groff",
    "https://upload.wikimedia.org/wikipedia/en/0/05/Frozen_%282013_film%29_poster.jpg",
    "https://www.youtube.com/watch?v=TbQm5doF_Uc")

###############################################################################

ghostbusters = media.Movie(
    "Ghostbusters", "1984", "Comedy",
    "Three former parapsychology professors set up shop as a unique ghost "
    "removal service.",
    "Bill Murray, Dan Aykroyd, Sigourney Weaver",
    "https://upload.wikimedia.org/wikipedia/en/2/2f/Ghostbusters_%281984%29_theatrical_poster.png",
    "https://www.youtube.com/watch?v=vntAEVjPBzQ")

###############################################################################

caribbean_pirates = media.Movie(
    "Pirates of the Caribbean", "2003", "Comedy",
    "Blacksmith Will Turner teams up with eccentric pirate 'Captain' Jack "
    "Sparrow to save his love, the governor's daughter, from Jack's former "
    "pirate allies, who are now undead.",
    "Johnny Depp, Geoffrey Rush, Orlando Bloom",
    "https://upload.wikimedia.org/wikipedia/en/8/89/Pirates_of_the_Caribbean_-_The_Curse_of_the_Black_Pearl.png",
    "https://www.youtube.com/watch?v=eQkAXLIMNQM")

###############################################################################

the_intern = media.Movie(
    "The Intern", "2015", "Comedy",
    "70-year-old widower Ben Whittaker has discovered that retirement isn't "
    "all it's cracked up to be. Seizing an opportunity to get back in the "
    "game, he becomes a senior intern at an online fashion site, founded and "
    "run by Jules Ostin.",
    "Robert De Niro, Anne Hathaway, Rene Russo",
    "https://upload.wikimedia.org/wikipedia/en/c/c9/The_Intern_Poster.jpg",
    "https://www.youtube.com/watch?v=ZU3Xban0Y6A")

###############################################################################

the_blind_side = media.Movie(
    "The Blind Side", "2009", "Drama",
    "The story of Michael Oher, a homeless and traumatized boy who became an "
    "All American football player and first round NFL draft pick with the "
    "help of a caring woman and her family.",
    "Quinton Aaron, Sandra Bullock, Tim McGraw",
    "https://upload.wikimedia.org/wikipedia/en/6/60/Blind_side_poster.jpg",
    "https://www.youtube.com/watch?v=gvqj_Tk_kuM")

###############################################################################

life_of_pi = media.Movie(
    "Life of Pi", "2012", "Drama",
    "A young man who survives a disaster at sea is hurtled into an epic "
    "journey of adventure and discovery. While cast away, he forms an "
    "unexpected connection with another survivor: a fearsome Bengal tiger.",
    "Suraj Sharma, Irrfan Khan, Adil Hussain",
    "https://upload.wikimedia.org/wikipedia/en/5/57/Life_of_Pi_2012_Poster.jpg",
    "https://www.youtube.com/watch?v=j9Hjrs6WQ8M")

###############################################################################

piku = media.Movie(
    "Piku", "2015", "Drama",
    "A quirky comedy about the relationship between an ageing father and his "
    "young daughter, living in a cosmopolitan city, dealing with each other's "
    "conflicting ideologies while being fully aware that they are each "
    "other's only emotional support.",
    "Amitabh Bachchan, Deepika Padukone, Irrfan Khan",
    "https://upload.wikimedia.org/wikipedia/en/9/98/Piku.jpg",
    "https://www.youtube.com/watch?v=WWYofSzfQTI")

###############################################################################

hidden_figures = media.Movie(
    "Hidden Figures", "2016", "Drama",
    "The story of a team of female African-American mathematicians who "
    "served a vital role in NASA during the early years of the U.S. space "
    "program.",
    "Taraji P. Henson, Octavia Spencer, Janelle Monae",
    "https://upload.wikimedia.org/wikipedia/en/4/4f/The_official_poster_for_the_film_Hidden_Figures%2C_2016.jpg",
    "https://www.youtube.com/watch?v=5wfrDhgUMGI")

###############################################################################

movies = [kung_fu_panda, despicable_me, frozen, ghostbusters,
          caribbean_pirates, the_intern, the_blind_side, life_of_pi, piku,
          hidden_figures]

# frozen.show_trailer() #check trailer
my_fav_movies.open_movies_page(movies)
