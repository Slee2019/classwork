import arcade


WIDTH = 640
HEIGHT = 480
x = WIDTH / 2
y = HEIGHT / 2
r = 50
arcade.open_window(WIDTH, HEIGHT, "My Drawing")
arcade.set_background_color(arcade.color.BLACK)

arcade.start_render()
# Begin drawing

arcade.draw_circle_filled(x, y, r, arcade.color.YELLOW)
arcade.draw_triangle_filled(400, 290, 240, 290, 320, 400, arcade.color.LIGHT_BROWN)

# End drawing
arcade.finish_render()
arcade.run()
