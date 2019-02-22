"""
to test type in cosole:
python3 -m unitteest
to profile type in console:
python3 -m cProfile boggle.py
"""
from string import ascii_uppercase
from random import choice # choice function return item from list at random

def make_grid(height, width):
    """
    Create a grid that will hold all the tiles for a boggle game
    """
    
    
    return {(row, col): choice(ascii_uppercase)
        for row in range(height)
        for col in range(width)}
    
def neighbours_of_positon(coords):
    """
    Get neighbours of a given position
    """
    
    row = coords[0]
    col = coords[1]
    
    # Assign each of the neighbours
    # The '(row col)' coordinates passed to this
    # function are situated here
    
    # Top-left to top-right
    top_left = (row -1, col -1)
    top_center = (row -1, col)
    top_right = (row - 1, col +1)

    # Left to right
    left = (row, col -1)
    right = (row, col +1)
    
    # Bottom-left to bottom-right
    bottom_left = (row +1, col -1)
    bottom_center = (row +1, col)
    bottom_right = (row +1, col +1)
    
    return [top_left, top_center, top_right,
            left, right,
            bottom_left, bottom_center, bottom_right]
            
def all_grid_neighbours(grid):
    """
    Get all of the possible neighbours for each 
    position in the grid
    """
    neighbours = {}
    for position in grid:
        position_neighbours = neighbours_of_positon(position)
        neighbours[position] =[p for p in position_neighbours if p in grid]
    return neighbours
            
            
def path_to_word(grid, path):
    """
    Add all of the letters on the path to a string
    """
    return ''.join([grid[p] for p in path])

    
def search(grid, dictionary):
    """
    Search through the paths to locate words by matching strings to words in dictionary first we get neighbours of every position in the grid and then we get the paths list to capture all paths that form valid words, we store words as paths rather than strings as letter my repeat in grid several times, so if we save two A's we won't know which one is it...
    'do_search' function which is valid in nest function, function exists within a scope of 'search' function code, it can't be called directly, has access to the other variables to find within 'search' function such as the path list, which it can add to.
    The 'do_search' function can be called by 'search' function and can call itself recursivelly to build paths.
    The 'search' start to search by passing single position to a 'do_search', this is a path of one letter, the 'do_search' converts whatever path is given into a word and checks if it's in dictionary.
    If a path makes a word it's added to a paths list. Whether the path is word or not 'do_search' gets each of neighbours of last letter, checks that neigbouring letter is not already in a path and then continues the searching from that letter. 
    So, 'do_search' could call itself eight times for each starting position and again for each of a various neighbours of each neighbour and so on... For each position in a grid for doing search nad convert all the paths to make valid words into words and return them into list. 
    """
    neighbours = all_grid_neighbours(grid)
    paths = []
    full_words, stems = dictionary
    
    def do_search(path):
        word = path_to_word(grid, path)
        if word in full_words:
            paths.append(path)
        if word not in stems:
            return
        for next_pos in neighbours[path[-1]]:
            if next_pos not in path:
                do_search(path + [next_pos])
                
    for position in grid:
        do_search([position])
        
    words = []
    for path in paths:
        words.append(path_to_word(grid, path))
    return set(words)
    

def get_dictionary(dictionary_file):
    """
    Load dictionary file
    """
    full_words, stems = set(), set()
    
    with open(dictionary_file) as f:
        for word in f:
            word = word.strip().upper()
            full_words.add(word)
            
            for i in range(1, len(word)):
                stems.add(word[:i])
    return full_words, stems 
        

def main():
    """
    This is the function that will run the whole project
    """
    grid = make_grid(100, 100)
    dictionary = get_dictionary('words.txt')
    words = search(grid, dictionary)
    for word in words:
        print(word)
    print("Found %s words" % len(words))
    
if __name__ == "__main__":
    main()
    



# grid = make_grid(2,2)

# print(grid)

# print(path_to_word(grid, [(0, 0), (1, 1)]))

# print(all_grid_neighbours(make_grid(2, 2)))