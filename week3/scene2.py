# Import the functions from the Draw 2-D library
# so that they can be used in this program.
from random import randint
from draw2d import \
    start_drawing, draw_line, draw_oval, draw_arc, \
    draw_rectangle, draw_polygon, draw_text, finish_drawing


def main():
    # Width and height of the scene in pixels
    scene_width = 800
    scene_height = 500

    # Call the start_drawing function in the draw2d.py
    # library which will open a window and create a canvas.
    canvas = start_drawing("Scene", scene_width, scene_height)

    # Call your drawing functions such
    # as draw_sky and draw_ground here.
    
    draw_land(canvas,400,150,100,color="gray17")
    draw_sky(canvas,400,300,-200,color="gray14")
    draw_land(canvas,400,0,150,color="darkslateGray")
    for i in range(5,100):
        draw_star(canvas,i+300,scene_width,scene_height)
    draw_moon(canvas,100,50,390,50,490)
    draw_pine_tree(canvas,700,150,250)
    draw_mountain(canvas,350,300,150)
    draw_mountain(canvas,450,300,100)
    draw_mountain(canvas,400,300,75)
    #draw_grid(canvas,scene_width,scene_height,50)
    

    # Call the finish_drawing function
    # in the draw2d.py library.
    finish_drawing(canvas)


# Define your functions such as
# draw_sky and draw_ground here.
def draw_pine_tree(canvas,center_x,bottom,height):
    # Draw tree trunk
    trunk_width = height / 10
    trunk_height = height / 4
    left_trunk = center_x - trunk_width / 2
    bottom_trunk = bottom
    right_trunk = center_x + trunk_width / 2
    trunk_top = bottom + trunk_height
    draw_rectangle(canvas,left_trunk, bottom_trunk, right_trunk, trunk_top, fill="tan4")


    # Draw skirt of the tree
    skirt_width = height / 2
    skirt_left = center_x - skirt_width / 2
    skirt_bottom = trunk_top
    peak_x = center_x
    peak_y= bottom + height
    skirt_right = center_x + skirt_width / 2
    draw_polygon(canvas,skirt_left,skirt_bottom,peak_x,peak_y,skirt_right,skirt_bottom,fill="forestgreen")

def draw_grid(canvas,width,height,interval):
    # Draw vertical line
    label_y = 15
    for x in range(interval,width,interval):
        draw_line(canvas,x,0,x,height,fill="gray90")
        draw_text(canvas,x,label_y,f"{x}",fill="gray90")

    # Draw horizontal line
    label_x = 15
    for y in range(interval,height,interval):
        draw_line(canvas,0,y,width,y,fill="gray90")
        draw_text(canvas,label_x,y,f"{y}",fill="gray90")

def draw_land(canvas,center_x,bottom,height,color):
    # Draw land with closer perspective
    left_side_x = center_x - center_x
    right_side_x = center_x * 2
    left_side_y = bottom
    right_side_y =center_x - height
    draw_rectangle(canvas,left_side_x,left_side_y,right_side_x,right_side_y,outline=color,fill=color)

def draw_sky(canvas,center_x,bottom,height,color):
    # Draw land with closer perspective
    left_side_x = center_x - center_x
    right_side_x = center_x * 2
    left_side_y = bottom
    right_side_y =center_x - height
    draw_rectangle(canvas,left_side_x,left_side_y,right_side_x,right_side_y,fill=color)

def draw_mountain(canvas,center_x,bottom,height):
    # Draw a mountain
    skirt_width = height
    skirt_left = center_x - skirt_width / 2
    skirt_bottom = bottom
    peak_x = center_x
    peak_y= bottom + height
    skirt_right = center_x + skirt_width / 2
    draw_polygon(canvas,skirt_left,skirt_bottom,peak_x,peak_y,skirt_right,skirt_bottom,outline="gray30",fill="gray30")
    

def draw_star(canvas,bottom,width,height):
    # Draw dots as starts
    star_x0 = randint(0,width)
    star_y0 = randint(bottom,height)
    star_x1 = star_x0 + 3
    star_y1 = star_y0 + 3
    star_color = f'gray{randint(70,99)}'
    draw_oval(canvas,star_x0, star_y0,star_x1, star_y1, width=0,fill=star_color)

def draw_moon(canvas,center_x,moon_left,moon_bottom,moon_right,moon_top):
    moon_x0 = center_x - moon_left
    moon_y0 = moon_bottom
    moon_x1 = center_x + moon_right
    moon_y1 = moon_top
    moon_color = f'gray{randint(85,99)}'
    draw_oval(canvas,moon_x0, moon_y0,moon_x1, moon_y1, width=0,fill=moon_color)

# Call the main function so that
# this program will start executing.
main()