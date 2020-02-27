from display import *
from matrix import *
from draw import *

"""
Goes through the file named filename and performs all of the actions listed in that file.
The file follows the following format:
     Every command is a single character that takes up a line
     Any command that requires arguments must have those arguments in the second line.
     The commands are as follows:
         line: add a line to the edge matrix -
               takes 6 arguemnts (x0, y0, z0, x1, y1, z1)
         ident: set the transform matrix to the identity matrix -
         scale: create a scale matrix,
                then multiply the transform matrix by the scale matrix -
                takes 3 arguments (sx, sy, sz)
         move: create a translation matrix,
                    then multiply the transform matrix by the translation matrix -
                    takes 3 arguments (tx, ty, tz)
         rotate: create a rotation matrix,
                 then multiply the transform matrix by the rotation matrix -
                 takes 2 arguments (axis, theta) axis should be x y or z
         apply: apply the current transformation matrix to the edge matrix
         display: clear the screen, then
                  draw the lines of the edge matrix to the screen
                  display the screen
         save: clear the screen, then
               draw the lines of the edge matrix to the screen
               save the screen to a file -
               takes 1 argument (file name)
         quit: end parsing

See the file script for an example of the file format
"""
def parse_file( fname, points, transform, screen, color ):
    f = open(fname, "r")
    lines = f.readlines()
    lines = [s.strip() for s in lines]
    # print(lines)
    ind = 0
    while (ind < len(lines)):
        if lines[ind] == "line":
            ind = ind + 1
            endpoints = lines[ind].split(" ")
            # print(endpoints)
            endpoints = [int(x) for x in endpoints]
            add_edge(points, endpoints[0], endpoints[1], endpoints[2], endpoints[3], endpoints[4], endpoints[5])

        if lines[ind] == "ident":
            ident(transform)

        if lines[ind] == "scale":
            ind = ind + 1
            abc = lines[ind].split(" ")
            abc = [int(x) for x in abc]
            new = make_scale(abc[0], abc[1], abc[2])
            # print("scale")
            # print_matrix(new)
            matrix_mult(new, transform)

        if lines[ind] == "move":
            ind = ind + 1
            abc = lines[ind].split(" ")
            abc = [int(x) for x in abc]
            new = make_translate(abc[0], abc[1], abc[2])
            # print("translate")
            # print_matrix(new)
            matrix_mult(new, transform)

        if lines[ind] == "rotate":
            ind = ind + 1
            abc = lines[ind].split(" ")
            theta = int(abc[1])
            if abc[0] == "x":
                new = make_rotX(theta)
            if abc[0] == "y":
                new = make_rotY(theta)
            if abc[0] == "z":
                new = make_rotZ(theta)
            # print("rotate")
            # print_matrix(new)
            matrix_mult(new, transform)

        if lines[ind] == "apply":
            matrix_mult(transform, points)

        if lines[ind] == "display":
            # print_matrix (points)
            clear_screen(screen)
            draw_lines(points, screen, color)
            # display(screen)

        if lines[ind] == "save":
            ind = ind + 1
            clear_screen(screen)
            draw_lines(points, screen, color)
            save_ppm(screen, "image.ppm")
            save_extension(screen, lines[ind])

        if lines[ind] == "quit":
            break

        ind = ind + 1
    f.close()
