# Save a dictionary into a pickle file
import cPickle as pickle

favorite_color = { "lion": "yellow", "kitty":"red"}

pickle.dump( favorite_color, open("save.p", "wb"))