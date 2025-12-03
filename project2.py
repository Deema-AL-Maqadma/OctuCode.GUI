from turtle import Turtle, Screen
sam = Turtle()
sam.shape("turtle") # turtle,square,tringle,circle,classic,arrowسهم
sam.color("medium purple")
sam.speed("fastest")
for _ in range(360): #لوب لعمل دائرة لكن يستهلك مساحة كبيرة
    sam.forward(1)
    sam.left(1)
# طريقة اخرلى لعمل دائرة باستخدام ميثود جاهزة ونعطيها نصف القطر
sam.speed("slowest")
sam.circle(100)

# لجعل الكائن يرسم شيء او يوقف عن الرسم كانه ماسك فرشاة
sam.penup() # رفع الفرشاة لن يرسم شي
sam.forward(100)
sam.pendown() # انزل الفرشاة وارسم
sam.pensize(10) # الحجم للخط بالبكسل
sam.forward(50)

window = Screen()
window.exitonclick()