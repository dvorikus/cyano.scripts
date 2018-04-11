### A short python script using Dendropy library
### It concatenates two nexus tree lists from MCMC chain run into one
### and it converts it to newick format
### Additional information about the options can be find at: 
### https://pythonhosted.org/DendroPy/index.html

import dendropy

# these files are lists of file names to be processed
my_file_0 = open('names.0.txt', 'r')
my_file_1 = open('names.1.txt', 'r')

for x in  my_file_0:
    for y in my_file_1:
        post_trees = dendropy.TreeList()
        post_trees.read(
            file=open(x.splitlines()[0]),
            schema="nexus",
            tree_offset=200)
        post_trees.read(
            file=open(y.splitlines()[0]),
            schema="nexus",
            tree_offset=200)
        post_trees.write(
            path="res." + x.splitlines()[0],
            schema="newick")
        break

