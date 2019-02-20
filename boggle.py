"""
to test type in cosole:
python3 -m unitteest
"""

def make_grid(height, width):
    """
    Creat a grid that will hold all the tiles for a boggle game
    """
    
    
    return {(row, col): '' for row in range(height)
        for col in range(width)
    }
    
