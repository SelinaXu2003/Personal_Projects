# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 13:16:39 2020

@author: selin
"""
# w= up, d= right, a= left and s= down

import turtle
import time
import random

delay= 0.2
score= 0
high_score= 0

# set upt the screen
wn= turtle.Screen()
wn.title("Snakey")
wn.bgcolor("green")
wn.setup(width=600, height=600,startx=0 ,starty=0)
wn.tracer(0)

# functions
def go_up():
    if head.direction != "down":
        head.direction= "up"
    
def go_down():
    if head.direction != "up":
        head.direction= "down"
    
def go_left():
    if head.direction != "right":
        head.direction= "left"
    
def go_right():
    if head.direction != "left":
        head.direction= "right"
    
def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y+20)
        
    if head.direction == "down":
        y = head.ycor()
        head.sety(y-20)
        
    if head.direction == "left":
        x = head.xcor()
        head.setx(x-20)
        
    if head.direction == "right":
        x = head.xcor()
        head.setx(x+20)
    
# snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0,0)
head.direction= "stop"

# the food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0,100)

#segments
segments= []

# pen
pen= turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Score= 0 High score= 0", align="center", font=("Courier", 24, "normal"))


#keyboard binfings
wn.listen()
wn.onkeypress(go_up,"w")
wn.onkeypress(go_left,"a")
wn.onkeypress(go_down,"s")
wn.onkeypress(go_right,"d")

# main game loop
while True:
    wn.update()
    
    #check for border collisions
    if head.xcor()> 290 or head.xcor()< -290 or head.ycor()> 290 or head.ycor()< -290:
        time.sleep(1)
        head.goto(0,0)
        head.direction= "stop"
        
        #hide segments
        for segment in segments:
            segment.goto(1000,1000)
            
        #clear segments
        segments.clear()
        
        #reset the score
        score =0
        pen.clear()
        pen.write("Score: {} High Score: {}". format(score, high_score), align="center", font=("Courier", 24, "normal"))
    
    #make the food appear and collisions
    if head.distance(food) < 20:
    
        #move food to random coordinate
        x= random.randint(-290,290)
        y= random.randint(-290,290)
        food.goto(x,y)
        
        #snake body, ie adding segments
        new_segment= turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)
        
        # incease score
        score += 100
        if score > high_score:
            high_score= score
        
        pen.clear()
        pen.write("Score: {} High Score: {}". format(score, high_score), align="center", font=("Courier", 24, "normal"))
        
    # move the end segments first
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x,y)
        
    #move segment 0 to where head is
    if len(segments)>0:
        x= head.xcor()
        y=head.ycor()
        segments[0].goto(x,y)

    move()
    
    #check for body collisions
    for segment in segments:
        if segment.distance(head)< 20:
            time.sleep(1)
            head.goto(0,0)
            head.direction= "stop"
        
             #hide segments
            for segment in segments:
                segment.goto(1000,1000)
            #clear segments
            segments.clear()
              
            #reset score
            score =0
            pen.clear()
            pen.write("Score: {} High Score: {}". format(score, high_score), align="center", font=("Courier", 24, "normal"))
            
    time.sleep(delay)

wn.mainloop()

