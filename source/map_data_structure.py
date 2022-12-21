""" 
Description
-----------

Script to generate a new data map image. This uses metadata information 
drawn from README.json files in the data directory (/projects/NS9039K/data/).

If the map does not include new directories, check that they have README.json
files.

Author
------
tarkan.bilge@uib.no 

"""
# ==============================================================================
# Imports
# ==============================================================================

from pathlib import Path
import os
import json
import pydot

# ==============================================================================
# User input
# ==============================================================================

PATH = '/projects/NS9039K/data/'

# Prefixes
space = '    '
branch = '|   '
# Pointers
tee = '|---'
last = '|___'

# ==============================================================================
# Functions
# ==============================================================================

def tree(dir_path, prefix=''):
    """
    A recursive generator, given a directory Path object
    will yield a visual tree structure line by line
    with each line prefixed by the same characters.
    Adapted from: 
    'https://stackoverflow.com/questions/9727673/list-directory-tree-structure-in-python'
    """    
    # Gets the paths for files in the initial path.
    # Is called again later to get the files in the next level path etc. 
    contents = list(dir_path.iterdir())
    filenames = [file.name for file in contents]
    
    pointers = [tee] * (len(contents) - 1) + [last]
    for pointer, path in zip(pointers, contents):
        # If the path is a directory.    
        if path.is_dir():
            # If the path contains a README.json
            readme = Path(os.path.join(path, 'README.json'))
            if os.path.exists(readme): 
                json_file = open(readme)
                json_dict = json.load(json_file)
                isCollection = json_dict['isCollection']
                isDataset = json_dict['isDataset']
                
                if isCollection:
                    print(f'{path} is a collection')
                elif isDataset:
                    print(f'{path} is a dataset')
                else:
                    pass
                
                # Don't yield for README.json files.
                yield prefix + pointer + path.name
                extension = branch if pointer == tee else space 
                yield from tree(path, prefix=prefix+extension)

def produce_text_data_rst(dir_path, output_file): 
    """ Produces a documentation page with a text data structure. """
    with open(output_file, 'w') as f:
        f.write('Data structure map')
        f.write('\n')
        f.write('==================')
        f.write('\n')
        f.write('\n')
        f.write('Below is a data structure map for the NIRD NS9039K data directory.')
        f.write('\n')
        f.write('\n')
        f.write('/projects/NS9039K/data/')
        f.write('\n')
        f.write('\n')
        f.write('::')
        f.write('\n')
        f.write('\n')
        for line in tree(dir_path):
            f.write(line)
            f.write('\n')

def plot_graph(rootdir, output_name, collection_color, dataset_color):
    """ Creates a png of the structure of a given directory. """ 
    # Initiate graph. 
    graph = pydot.Dot("my_graph", graph_type="digraph", bgcolor="white", splines="ortho", style="filled", fillcolor=collection_color)
    for root, dirs, files in os.walk(rootdir):
        for subdir in dirs:
            readme = os.path.join(root, subdir, 'README.json')
            if os.path.exists(readme):
                # Read README.json
                json_file = open(readme)
                json_dict = json.load(json_file)
                isCollection = json_dict['isCollection']
                isDataset = json_dict['isDataset']
            
                # Node colour
                if isCollection:
                    node_color = collection_color
                elif isDataset:
                    node_color = dataset_color
                else:
                    raise ValueError(f"Subdirectory '{subdir}' is not a Dataset or Collection...")

                node_name = os.path.join(root, subdir)
                node_label = subdir

                # Add to graph. 
                graph.add_node(pydot.Node(node_name, style="filled", fillcolor=node_color, label=node_label))
                graph.add_edge(pydot.Edge(root, node_name))    

    graph.write_png(output_name)

def produce_png_data_rst(rootdir, out_png, out_rst):
    plot_graph(rootdir=rootdir, output_name=out_png, collection_color='white', dataset_color='grey')
    # If you select an out_rst then it creates a new data_map.rst file. 
    if out_rst:
        with open(out_rst, 'w') as f:
            f.write('Data structure map')
            f.write('\n')
            f.write('==================')
            f.write('\n')
            f.write('\n')
            f.write('Below is a data structure map for the NIRD NS9039K data directory.')
            f.write('\n')
            f.write('\n')
            f.write('.. figure::')
            f.write('\n')
            f.write(f'  {out_png}')
            f.write('\n')
            f.write('  :name: data-map')
            f.write('\n')
            f.write('  :width: 800')
            f.write('\n')

# ==============================================================================
# Main
# ==============================================================================

if __name__ == '__main__':
    # produce_text_data_rst(dir_path=Path(PATH), output_file='/projects/NS9039K/www/tbi045/BCPU-data-structure/source/data_map.rst')
    # produce_png_data_rst(rootdir='/projects/NS9039K/data', out_png='data_map.png', out_rst=False)
    plot_graph(rootdir='/projects/NS9039K/data', output_name='data_map.png', collection_color='white', dataset_color='grey')
