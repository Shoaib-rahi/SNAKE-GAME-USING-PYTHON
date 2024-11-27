import tkinter
import random



COLS =20
ROWS = 25
TILE_SIZE = 25
WINDOW_WIDTH = TILE_SIZE * ROWS
WINDOW_HEIFGT = TILE_SIZE * COLS





class tileSize:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        

# game window

window = tkinter.Tk()
window.title("            *************SNAKE GAME************")
window.resizable(False,False)


canvas = tkinter.Canvas(window,bg="black",width=WINDOW_WIDTH,height=WINDOW_HEIFGT,borderwidth=0,highlightthickness=0)
canvas.pack()
window.update()



# center window

window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_hegiht = window.winfo_screenheight()


window_x = int((screen_width/2) - (window_width/2))
window_y = int((screen_hegiht/2) - (window_height/2))

window.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")


snake = tileSize(5*TILE_SIZE,5* TILE_SIZE)
snake_body = []
food = tileSize(10*TILE_SIZE ,10*TILE_SIZE)
velocityX = 0
velocityY = 0
game_over =False



def change_direction(e):
    global velocityX,velocityY,game_over

    if(game_over):
        return


    if(e.keysym == "Up" and velocityY != 1):
        velocityX = 0
        velocityY = -1
    elif(e.keysym == "Down" and velocityY != -1):
        velocityX = 0
        velocityY = 1
    elif(e.keysym == "Left" and velocityX != 1):
        velocityY = 0
        velocityX = -1
    elif(e.keysym == "Right" and velocityX != -1):
        velocityY = 0
        velocityX = 1

def move():
    global snake_body,food,game_over,snake

    if(game_over):
        return
    if(snake.x < 0 or snake.x >= WINDOW_WIDTH or snake.y < 0 or snake.y >= WINDOW_HEIFGT):
        game_over  = False
        return

    # for tile in snake_body:
    #     if(snake.x == tile.x and snake.y == tile.y):
    #         game_over = True
    #         return

    snake.x += velocityX * TILE_SIZE
    snake.y += velocityY * TILE_SIZE


#   collision between food and snake
    if(food.x == snake.x and food.y == snake.y):
        snake_body.append(tileSize(food.x , food.y))
        food.x = random.randint(0,COLS-5) * TILE_SIZE
        food.y = random.randint(0, ROWS-5) * TILE_SIZE
    
    for i in range(len(snake_body)-1,-1,-1):
        tile = snake_body[i]
        if(i == 0):
            tile.x = snake.x
            tile.y = snake.y
        else:
            pre_tile = snake_body[i-1]
            tile.x = pre_tile.x
            tile.y = pre_tile.y
            

def draw():
    # global snake_body,food,game_over,snake



    move()
    canvas.delete("all")
    canvas.create_rectangle(food.x,food.y,food.x + TILE_SIZE,food.y + TILE_SIZE,fill="red")
    canvas.create_rectangle(snake.x,snake.y,snake.x + TILE_SIZE,snake.y + TILE_SIZE, fill="lime green")

    for tile in snake_body:
        canvas.create_rectangle(tile.x,tile.y, tile.x + TILE_SIZE , tile.y + TILE_SIZE,fill="lime green")


    window.after(100,draw)
draw()

window.bind("<KeyRelease>",change_direction)

window.mainloop()

