"""
sample.py is a sample python3 program using turtle graphics.
"""
import turtle

def drawSquare():
    """
    drawSquare draws a square with sides of length 100.
    """
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)

def main():
    """
    main program draws a square and waits user to hit Enter key.
    """
    drawSquare()
    print('Close the canvas window to end the program...')
    turtle.done()

if __name__ == '__main__':
    main()