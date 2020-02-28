from display import *
from draw import *
from parser import *
from matrix import *

# WIDTH = 6
# HEIGHT = 7
# WIDTH_HI = 175
# HEIGHT_HI = 125
screen = new_screen()
color = [ 0, 0, 0 ]
edges = []
transform = new_matrix()
#
# h = [[ 0 , 0 ],
#     [ 25 , 0 ],
#     [ 25 , 25 ],
#     [ 50 , 25 ],
#     [ 50 , 0 ],
#     [ 75 , 0 ],
#     [ 75 , 75 ],
#     [ 50 , 75 ],
#     [ 50 , 50 ],
#     [ 25 , 50 ],
#     [ 25 , 75 ],
#     [ 0 , 75 ]]
#
# i = [[ 100 , 0 ],
#     [ 125 , 0 ],
#     [ 125 , 75 ],
#     [ 100 , 75 ]]
#
# DEPTH = 25
#
# f = open("cube", "w+")
#
# for W in range(WIDTH):
#     for H in range(HEIGHT):
#         startx = W*WIDTH_HI
#         starty = H*HEIGHT_HI
#         for point in range(len(h)):
#
#             #front
#             if point == len(h) - 1:
#                 f.write("line\n")
#                 f.write(str(h[point][0] + startx) + " " + str(h[point][1] + starty) + " 0 ")
#                 f.write(str(h[0][0] + startx) + " " + str(h[0][1] + starty) + " 0\n")
#             else:
#                 f.write("line\n")
#                 f.write(str(h[point][0] + startx) + " " + str(h[point][1] + starty) + " 0 ")
#                 f.write(str(h[point + 1][0] + startx) + " " + str(h[point + 1][1] + starty) + " 0\n")
#
#             #side
#             f.write("line\n")
#             f.write(str(h[point][0] + startx) + " " + str(h[point][1] + starty) + " 0 ")
#             f.write(str(h[point][0] + startx) + " " + str(h[point][1] + starty) + " 25\n")
#
#             #Back
#             if point == len(h) - 1:
#                 f.write("line\n")
#                 f.write(str(h[point][0] + startx) + " " + str(h[point][1] + starty) + " 25 ")
#                 f.write(str(h[0][0] + startx) + " " + str(h[0][1] + starty) + " 25\n")
#             else:
#                 f.write("line\n")
#                 f.write(str(h[point][0] + startx) + " " + str(h[point][1] + starty) + " 25 ")
#                 f.write(str(h[point + 1][0] + startx) + " " + str(h[point + 1][1] + starty) + " 25\n")
#
#         for point in range(len(i)):
#
#             #front
#             if point == len(i) - 1:
#                 f.write("line\n")
#                 f.write(str(i[point][0] + startx) + " " + str(i[point][1] + starty) + " 0 ")
#                 f.write(str(i[0][0] + startx) + " " + str(i[0][1] + starty) + " 0\n")
#             else:
#                 f.write("line\n")
#                 f.write(str(i[point][0] + startx) + " " + str(i[point][1] + starty) + " 0 ")
#                 f.write(str(i[point + 1][0] + startx) + " " + str(i[point + 1][1] + starty) + " 0\n")
#
#             #side
#             f.write("line\n")
#             f.write(str(i[point][0] + startx) + " " + str(i[point][1] + starty) + " 0 ")
#             f.write(str(i[point][0] + startx) + " " + str(i[point][1] + starty) + " 25\n")
#
#             #Back
#             if point == len(i) - 1:
#                 f.write("line\n")
#                 f.write(str(i[point][0] + startx) + " " + str(i[point][1] + starty) + " 25 ")
#                 f.write(str(i[0][0] + startx) + " " + str(i[0][1] + starty) + " 25\n")
#             else:
#                 f.write("line\n")
#                 f.write(str(i[point][0] + startx) + " " + str(i[point][1] + starty) + " 25 ")
#                 f.write(str(i[point + 1][0] + startx) + " " + str(i[point + 1][1] + starty) + " 25\n")
#
#
# f.write("ident\nrotate\nz 50\nrotate\ny 45\nmove\n-20 -20 0\napply\nsave\ncube.png")
# f.close()


parse_file( 'script', edges, transform, screen, color )
print("\nImages saved as pic1.png, ..., pic5.png\n")
