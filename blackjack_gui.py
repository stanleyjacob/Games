from graphics import *
import time

win = GraphWin("blackjack", 600, 400)

start_pixel = 170
temp = Image(Point(start_pixel, 280), "/Users/qldo18/Desktop/cards4/2_of_clubs.gif")
temp2 = Image(Point(start_pixel + 60, 280), "/Users/qldo18/Desktop/cards4/4_of_clubs.gif")

temp.draw(win)
temp2.draw(win)

temp5 = Image(Point(start_pixel, 110), "/Users/qldo18/Desktop/cards4/back.gif")
temp6 = Image(Point(start_pixel + 60, 110), "/Users/qldo18/Desktop/cards4/queen_of_hearts.gif")

temp5.draw(win)

# time.sleep(10)

min_pt_x = 250
min_pt_y = 325
max_pt_x = 350
max_pt_y = 375
temp = Rectangle(Point(min_pt_x, min_pt_y), Point(max_pt_x, max_pt_y))
temp.draw(win)

tempPt = Point(10, 10)
tempPt.setFill("red")
tempPt.draw(win)

tempPt = Point(100, 100)
tempPt.setFill("red")
tempPt.draw(win)

tempPt = Point(10, 100)
tempPt.setFill("red")
tempPt.draw(win)

tempPt = Point(100, 10)
tempPt.setFill("red")
tempPt.draw(win)

while(1):
	# deal initial dealer cards, 2 user calls
	curr_point = win.getMouse() # every click is a hit
	if curr_point.x > min_pt_x and curr_point.x < max_pt_x and \
		curr_point.y > min_pt_y and curr_point.y < max_pt_y:	
		temp6.draw(win)

