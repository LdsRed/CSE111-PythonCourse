from random import randint
from draw2d import \
    start_drawing, draw_line, draw_oval, draw_arc, \
    draw_rectangle, draw_polygon, draw_text, finish_drawing


def draw_star(canvas,bottom,width,height):
    # Draw dots as starts
    star_x0 = randint(0,width)
    star_y0 = randint(bottom,height)
    star_x1 = star_x0 + 4
    star_y1 = star_y0 + 4
    star_color = f'gray{randint(70,99)}'
    draw_oval(canvas,star_x0, star_y0,star_x1, star_y1, width=0,fill=star_color)

def draw_mountain(canvas,center_x,bottom,height):
    # Draw a mountain
    skirt_width = height
    skirt_left = center_x - skirt_width / 2
    skirt_bottom = bottom
    peak_x = center_x
    peak_y= bottom + height
    skirt_right = center_x + skirt_width / 2
    draw_polygon(canvas,skirt_left,skirt_bottom,peak_x,peak_y,skirt_right,skirt_bottom,outline="brown",fill="brown")

def draw_small_pine_tree_two(canvas, peak_x, peak_y):
    """Draw one pine tree at location (peak_x, peak_y)"""

    # Compute the coordinates of the skirt and trunk.
    skirt_left  = peak_x - 40
    skirt_right = peak_x + 40
    skirt_bottom = peak_y - 150
    trunk_left  = peak_x - 10
    trunk_right = peak_x + 10
    trunk_bottom = peak_y - 200

    # Draw the tree trunk.
    draw_rectangle(canvas, trunk_left, trunk_bottom,
            trunk_right, skirt_bottom, fill="brown")

    # Draw the tree skirt.
    draw_polygon(canvas, skirt_left, skirt_bottom, peak_x, peak_y,
            skirt_right, skirt_bottom, fill="forestGreen")


def draw_small_pine_tree(canvas, peak_x, peak_y):
    """Draw one pine tree at location (peak_x, peak_y)"""

    # Compute the coordinates of the skirt and trunk.
    skirt_left  = peak_x - 50
    skirt_right = peak_x + 50
    skirt_bottom = peak_y - 160
    trunk_left  = peak_x - 10
    trunk_right = peak_x + 10
    trunk_bottom = peak_y - 200

    # Draw the tree trunk.
    draw_rectangle(canvas, trunk_left, trunk_bottom,
            trunk_right, skirt_bottom, fill="brown")

    # Draw the tree skirt.
    draw_polygon(canvas, skirt_left, skirt_bottom, peak_x, peak_y,
            skirt_right, skirt_bottom, fill="forestGreen")


def draw_pine_tree(canvas, peak_x, peak_y):
    """Draw one pine tree at location (peak_x, peak_y)"""

    # Compute the coordinates of the skirt and trunk.
    skirt_left  = peak_x - 70
    skirt_right = peak_x + 70
    skirt_bottom = peak_y - 210
    trunk_left  = peak_x - 10
    trunk_right = peak_x + 10
    trunk_bottom = peak_y - 260

    # Draw the tree trunk.
    draw_rectangle(canvas, trunk_left, trunk_bottom,
            trunk_right, skirt_bottom, fill="brown")

    # Draw the tree skirt.
    draw_polygon(canvas, skirt_left, skirt_bottom, peak_x, peak_y,
            skirt_right, skirt_bottom, fill="forestGreen")

def draw_sky(canvas, scene_width, scene_height):
    """Draw the sky and all the objects in the sky."""
    draw_rectangle(canvas, 0, scene_height / 3,
                   scene_width, scene_height, width=0, fill="gray1")

def draw_grid(canvas, width, height, interval, color="blue"):
    # Draw a vertical line at every x interval.
    label_y = 15
    for x in range(interval, width, interval):
        draw_line(canvas, x, 0, x, height, fill=color)
        draw_text(canvas, x, label_y, f"{x}", fill=color)

    # Draw a horizontal line at every y interval.
    label_x = 15
    for y in range(interval, height, interval):
        draw_line(canvas, 0, y, width, y, fill=color)
        draw_text(canvas, label_x, y, f"{y}", fill=color)
def draw_ground(canvas, scene_width, scene_height):
    """Draw the ground and all the objects on the ground."""
    draw_rectangle(canvas, 0, 0, scene_width, scene_height / 3, width=0, fill="tan4")

def draw_sun(canvas,center_x,sun_left,sun_bottom,sun_right,sun_top):
    sun_x0 = center_x - sun_left
    sun_y0 = sun_bottom
    sun_x1 = center_x + sun_right
    sun_y1 = sun_top
    #sun_color = f'grey{randint(85,99)}'
    draw_oval(canvas,sun_x0, sun_y0,sun_x1, sun_y1, width=0,fill="yellow")

def main():
    # Width and height of the scene in pixels
    scene_width = 800
    scene_height = 500

    # Call the start_drawing function in the draw2d.py
    # library which will open a window and create a canvas.
    canvas = start_drawing("Scene", scene_width, scene_height)


    

    draw_ground(canvas, scene_width, 700)
    draw_grid(canvas, scene_width, scene_height, 50)
    draw_sky(canvas, 800, 700)
    for i in range(5,100):
        draw_star(canvas,i+300,scene_width,scene_height)

    draw_mountain(canvas,0,230,150)
    draw_mountain(canvas,50,230,100)
    draw_mountain(canvas,100,230,75)

    draw_mountain(canvas,600,230,150)
    draw_mountain(canvas,650,230,100)
    draw_mountain(canvas, 700,230,75)

    draw_sun(canvas,400,50,390,50,490)
    draw_small_pine_tree_two(canvas, 390, 420)
    draw_small_pine_tree(canvas, 340, 400)
    draw_small_pine_tree(canvas, 280, 350)
    draw_pine_tree(canvas, 230, 350)
    draw_pine_tree(canvas, 150, 300 )

    draw_small_pine_tree_two(canvas, 480, 420)
    draw_small_pine_tree(canvas, 530, 400)
    draw_small_pine_tree(canvas, 570, 350)
    draw_pine_tree(canvas, 630, 350)
    draw_pine_tree(canvas, 680, 300)

    draw_line(canvas, 150, 40, 120, 60, width=1, fill="green1")
    draw_line(canvas, 150, 40, 180, 60, width=1, fill="green1")
    draw_line(canvas, 150, 30, 120, 60, width=1, fill="green1")
    draw_line(canvas, 150, 30, 180, 60, width=1, fill="green1")

    draw_line(canvas, 150, 30, 140, 60, width=1, fill="green1")
    draw_line(canvas, 150, 30, 190, 60, width=1, fill="green1")
    draw_line(canvas, 150, 30, 170, 60, width=1, fill="green1")
    draw_line(canvas, 150, 30, 120, 60, width=1, fill="green1")
    #draw_line(canvas, 0, 2, 100, 250, width=10, fill="grey")

    # Call the finish_drawing function
    # in the draw2d.py library.
    finish_drawing(canvas)


main()