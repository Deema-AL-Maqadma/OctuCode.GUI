from turtle import Turtle, Screen
import random

window = Screen()
window.setup(width=700,height=700)#للتحكم في حجم شاشة العرض
window.bgcolor("black") #لتغيير لون خلفية شاشة العرض

sam = Turtle() # الكائن الاول
sam.shape("turtle")
sam.color("white")
sam.pensize(5)
sam.speed("slow")
tom = Turtle() # الكائن الثاني
tom.shape("square")
tom.color("orange")
tom.pensize(5)
tom.speed("slow")
my_angles=[0,90,180,270] # قائمة بالزوايا العشوائية التي يمكن للكائن الحركة بها
my_distance=[20,30,40,50,60,70,80,90,100] #قائمة بالمسافات التي يتحركها الكائن

for _ in range(20):
    tom.forward(random.choice(my_distance))
    tom.left(random.choice(my_angles))

for _ in range(20):
    sam.forward(random.choice(my_distance))
    sam.left(random.choice(my_angles))

window.exitonclick()