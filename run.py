from remove_words import remove_words
from build_graph import build_graph
from train import train

dataset = 'mr'

print("Running Remove Stop Words\n")
remove_words(dataset)

print("Running Build Graph\n")
build_graph(dataset)

print("Running Train\n")
# train(dataset)
