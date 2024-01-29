import sys
import time
import turtle

screen = turtle.Screen()
screen.screensize(20, 20, "white")

pen = turtle.Turtle()
pen.shape("turtle")
pen.color("black")
pen.pensize(5)
pen.hideturtle()


# Creating a class for the bear parts
class BearParts:
    @staticmethod
    def draw_circle(pen, x, y, radius):
        pen.penup()
        pen.goto(x, y)
        pen.down()
        pen.circle(radius)


BearParts.draw_circle(pen, -155, -190, 60)  # Circle 1
BearParts.draw_circle(pen, 155, -190, 60)   # Circle 2
BearParts.draw_circle(pen, 0, -190, 150)     # Body
BearParts.draw_circle(pen, 0, 110, 80)       # Head
BearParts.draw_circle(pen, 100, 195, 50)     # Ear 1
BearParts.draw_circle(pen, -100, 195, 50)    # Ear 2
BearParts.draw_circle(pen, 100, -50, 60)     # Hand 1
BearParts.draw_circle(pen, -100, -50, 60)    # Hand 2


# Function to fill a circle with a given color
def fill_circle(pen, x, y, radius, color):
    pen.penup()
    pen.goto(x, y)
    pen.down()
    pen.begin_fill()
    pen.fillcolor(color)
    pen.circle(radius)
    pen.end_fill()


# Defining the primary color
def color_choice1():
    if choice1 == 1:
        return "RED"
    elif choice1 == 2:
        return "YELLOW"
    elif choice1 == 3:
        return "BLUE"
    else:
        return "WHITE"


# Defining the secondary color
def color_choice2():
    if choice2 == 5:
        return "GREEN"
    elif choice2 == 6:
        return "ORANGE"
    elif choice2 == 7:
        return "PURPLE"
    else:
        return "white"


# Loop to fill each shape individually
while True:
    text = ("\nWELCOME TO THE BEAR STATION"
            "\nLET'S FILL SOME BABY'S UP!!!!!"
            "\n\nFOLLOW INSTRUCTIONS FOR BETTER RESULT.ENJOY")
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.1)

    # Adding delay after the text
    delay_second = 1
    time.sleep(delay_second)

    # Get user input for primary color
    text2 = "\n\n****Select your primary color****"
    for char in text2:
        print(char, end='', flush=True)
        time.sleep(0.050)

    choice1 = int(input("\nFor RED press [1]"
                        "\nFor YELLOW press [2]"
                        "\nFor BLUE press [3]"
                        "\nEnter here:"))

    primary_color = color_choice1()
    print("The primary color is", primary_color)

    # Asking the user an input for secondary color
    text3 = "\n****Select your secondary color****"
    for char in text3:
        print(char, end='', flush=True)
        time.sleep(0.050)

    choice2 = int(input("\nFor GREEN press [5]"
                        "\nFor ORANGE press [6]"
                        "\nFor PURPLE press [7]"
                        "\nEnter here:"))

    secondary_color = color_choice2()
    print("The secondary color is", secondary_color)

    print("\n=================================================="
          "\n-----THE RESULT OF THE COLORS YOU HAVE CHOSEN-----"
          "\n==================================================")

    # Adding delay after the text
    delay_second = 1
    time.sleep(delay_second)

    text4 = "\nThe tertiary result is:"
    for char in text4:
        print(char, end='', flush=True)
        time.sleep(0.050)

    # Combining two variables by multiplying the number inputs of the user
    inputs = choice1 * choice2

    tertiary_result = ""
    if inputs == 5:
        tertiary_result = "YELLOW\nColor Code: #FFFF00"
    elif inputs == 6:
        tertiary_result = "VERMILION\nColor code: #E34234"
    elif inputs == 7:
        tertiary_result = "MAGENTA/RED-VIOLET\nColor code: #C71585"
    elif inputs == 10:
        print("YELLOW-GREEN\nColor code: #9ACD32")
    elif inputs == 12:
        print("AMBER\nColor code: #FFBF00")
    elif inputs == 14:
        print("BROWN\nColor code: #964B00")
    elif inputs == 15:
        print("TEAL\nColor code: #008080")
    elif inputs == 18:
        print("REDDISH-BROWN OF BURNT SIENNA\nColor code: #E97451")
    elif inputs == 21:
        print("BLUE-VIOLET\nColor code: #8a2be2")

    # Adding delay after the text
    delay_second = 1
    time.sleep(delay_second)

    # Selection for the Parts of the Bear
    part_selector = int(input("\nIn which part do you want to fill? (Please refer to the choices.)"
                              "\n[1] Feet"
                              "\n[2] Hand"
                              "\n[3] Body"
                              "\n[4] Head"
                              "\n[5] Ears"
                              "\nEnter here:"))

    if part_selector == 0:
        print("Program Completed.")
        break

    tcolor = input("Enter color code:")

    if part_selector == 1:
        fill_circle(pen, -155, -190, 60, tcolor)
        fill_circle(pen, 155, -190, 60, tcolor)
    elif part_selector == 2:
        fill_circle(pen, 100, -50, 60, tcolor)
        fill_circle(pen, -100, -50, 60, tcolor)
    elif part_selector == 3:
        fill_circle(pen, 0, -190, 150, tcolor)
    elif part_selector == 4:
        fill_circle(pen, 0, 110, 80, tcolor)
    elif part_selector == 5:
        fill_circle(pen, 100, 195, 50, tcolor)
        fill_circle(pen, -100, 195, 50, tcolor)
    else:
        print("Invalid part selection. Please enter a valid part number.")

    screen.update()  # Update the turtle screen

    # A question for the user
    end_question1 = int(input("\nAre all the parts filled?"
                              "\nIf yes press [1]"
                              "\nIf no press [2]"
                              "\nEnter here:"))

    if end_question1 == 1:
        print("Program Completed.")
        sys.exit()
    else:
        print("Well let's proceed.")

    # Adding delay after the text
    delay_second = 1
    time.sleep(delay_second)

    end_question2 = int(input("\nDo you want to continue?"
                              "\nIf yes press [1]"
                              "\nIf no press [2]"
                              "\nEnter here:"))

    if end_question2 == 1:
        print("Program Continued.")
        continue

    else:
        print("Program terminated.\nThank you!!!")
        break
# Close the turtle graphics window
turtle.done()
