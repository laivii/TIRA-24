def count(r):
     grid = create_grid(r)
     rooms = 0
     
     for row in range(1, len( grid ) - 1):
          for tile in range(1, len( grid[ row ] ) - 1):
               if grid[ row ][ tile ] == ".":
                    scout_room( grid, row, tile )
                    rooms += 1

     return rooms

def create_grid( labyrinth ):
     grid = []

     for row in labyrinth:
        new_row = []
        for tile in row:
            new_row.append( tile )

        grid.append( new_row )

     return grid

def scout_room( grid, y, x ):
     if grid[ y ][ x ] != ".":
          return 

     grid[ y ][ x ] = "T"

     scout_room( grid, y-1, x )
     scout_room( grid, y+1, x )
     scout_room( grid, y, x-1 )
     scout_room( grid, y, x+1 )

if __name__ == "__main__":
    r = ["########",
         "#..#...#",
         "####.#.#",
         "#..#.#.#",
         "########"]

    print(count(r)) # 3