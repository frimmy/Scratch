# Load the dictionary back from the pickle file.
import cPickle as pickle

favorite_color = pickle.load( open( "save.p", "rb"))
# favorite_color is now { "lion": "yellow", "kitty":"red"}