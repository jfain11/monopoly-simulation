from Dice import *
from graphicsButton import *
from graphics import *

def main():

    win = GraphWin("Monopoly", 1200, 1000)
    win.setBackground("grey")
    x1 = 960
    x2 = 1040
    y1 = 860
    y2 = 940
    space = {}

    for num in range(11):
        num += 1
        space[num] = Rectangle(Point(x1, y1), Point(x2, y2))
        space[num].setFill("white")
        space[num].draw(win)
        x1 -= 80
        x2 -= 80

    x1 += 80
    x2 += 80
    y1 -= 80
    y2 -= 80

    for num in range(11, 21):

        num += 1
        space[num] = Rectangle(Point(x1, y1), Point(x2, y2))
        space[num].setFill("white")
        space[num].draw(win)
        y1 -= 80
        y2 -= 80

    x1 += 80
    x2 += 80
    y1 += 80
    y2 += 80

    for num in range(21, 31):
        num += 1
        space[num] = Rectangle(Point(x1, y1), Point(x2, y2))
        space[num].setFill("white")
        space[num].draw(win)
        x1 += 80
        x2 += 80

    x1 -= 80
    x2 -= 80
    y1 += 80
    y2 += 80

    for num in range(31, 40):

        num += 1
        space[num] = Rectangle(Point(x1, y1), Point(x2, y2))
        space[num].setFill("white")
        space[num].draw(win)
        y1 += 80
        y2 += 80

    space[2].setFill("brown")
    space[4].setFill("brown")

    space[7].setFill("light blue")
    space[9].setFill("light blue")
    space[10].setFill("light blue")

    space[12].setFill("hot pink")
    space[14].setFill("hot pink")
    space[15].setFill("hot pink")

    space[17].setFill("orange")
    space[19].setFill("orange")
    space[20].setFill("orange")

    space[22].setFill("red")
    space[24].setFill("red")
    space[25].setFill("red")

    space[27].setFill("yellow")
    space[29].setFill("yellow")
    space[30].setFill("yellow")

    space[32].setFill("green")
    space[33].setFill("green")
    space[35].setFill("green")

    space[38].setFill("blue")
    space[40].setFill("blue")

    nums = [2, 4, 7, 9, 10, 12, 14, 15, 17, 19, 20, 22, 24, 25, 27, 29, 30, 32, 33, 35, 38, 40]
    text = {}
    spaceTotal = {}
    for num in nums:
        text[num] = Text(space[num].getCenter(), "0")
        text[num].setSize(9)
        text[num].setStyle("bold")
        text[num].draw(win)

    for num in nums:
        spaceTotal[num] = 0





    e = Entry(Point(600, 500), 13)
    e.setFill("white")
    e.setSize(20)
    e.draw(win)

    buttonMain = Button(600, 560, 50, 120)
    buttonMain.setFill("white")
    buttonMain.setWidth(3)
    buttonMain.draw(win)

    buttonLabel = Text(Point(600, 560), "Start Simulation")
    buttonLabel.draw(win)

# Main Loop

    while True:
        click = win.getMouse()
        if buttonMain.isClicked(click):

            rolls = int(e.getText())
            dice = Dice(6)
            currentSpace = 1

            for i in range(rolls):
                roll1 = dice.rollDice()
                roll2 = dice.rollDice()
                total = roll1 + roll2
                if roll1 == roll2:
                    roll3 = dice.rollDice()
                    roll4 = dice.rollDice()
                    total += roll3 + roll4
                    if roll3 == roll4:
                        currentSpace = 31
                        continue

                currentSpace += total
                if currentSpace > 40:
                    currentSpace = currentSpace - 40

                if currentSpace in nums:
                    spaceTotal[currentSpace] += 1

        for num in nums:
            text[num].setText(str(spaceTotal[num]))




            
        else:
            continue






    win.getMouse()

if __name__ == '__main__':
    main()

