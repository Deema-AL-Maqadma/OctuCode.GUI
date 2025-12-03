from turtle import Turtle, Screen
import random
sam = Turtle()
window = Screen()
shap_list = ["turtle","square","tringle","circle","classic","arrow"]
sizes_list = [2,4,6,8,10,12,14]
colors_list = ["green","purple","orange","red","black","blue","yellow","gray"]
sam.speed("slowest")
# ميثود عشان تبني مربع اضلاعه تختلف عشوائيا باللون والحجم وشكل الكائن المتحرك
def drowSquare():
    for _ in range(4):
        sam.color(random.choice(colors_list))
        sam.pensize(random.choice(sizes_list))
        sam.shape(random.choice(shap_list))
        sam.forward(200) # عدد الخطوات
        sam.left(90) # مقدار الزاوية المتحركة يسارا
drowSquare()
window.exitonclick()