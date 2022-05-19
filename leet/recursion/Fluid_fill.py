import sys
im = [['..########################...........'],
        ['..#......................#...#####...'],
        ['..#..........########....#####...#...'],
        ['..#..........#......#............#...'],
        ['..#..........########.........####...'],
        ['..######......................#......'],
        ['.......#..#####.....###########......'],
        ['.......####...#######................']]
height = len(im)
width = len(im[0])
def fluidFill(image,x,y,newChar,oldChar = None):
            if oldChar == None:
                #oldChar defaults to the character at x,y.
                oldChar == image[x][y]
            if oldChar == newChar or image[y][x] != oldChar:
                #basecase
                return
            image[y][x] = newChar #cahnge the char
            #uncomment to view each step
            print(image)
            #change the neighbouring characters.
            if y+1 < height and image[y+1] == oldChar:
                #recursive case
                floodFill(image,x,y+1,newChar,oldChar)
            if y-1 >= 0 and image[y-1] == oldChar:
                #recursive case
                floodFill(image,x,y-1,newChar,oldChar)
            if x+1 < width and image[y][x+1]== oldChar:
                #RECURSIVE CASE
                floodFill(image,x+1,y,newChar,oldChar)
            if x-1 >= 0 and image[y][x-1] == oldChar:
                #recursive call
                floodFill(image,x-1,y,newChar,oldChar)
            return #base case
def printImage(image):
            for y in range(height):
                #print each row
                for x in range(width):
                    #print each column.
                    sys.stdout.write(image[y][x])
                sys.stdout.write("\n")
            sys.stdout.write("\n")
printImage(im)
fluidFill(im,3,3,"o")
print(im)

        



