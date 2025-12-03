from turtle import Turtle, Screen #كلاسات للتحكم في السلحفاة  والتحكم في النافذة الظاهرة غلى الشاشة 
sam = Turtle() #اوبجكت من الشكل 
sam.shape("turtle") # لتحديد الشكل المتحرك
sam.color("red") #لتحديد اللون
sam.speed("slowest") #للتحكم في سرعة الشكل
for _ in range(4): #الفراغ لعدم كتابة شي في الذاكرة
    sam.forward(200) # للتقدم في الحركة
    sam.left(90) # للتوجه يسارا
sam.forward(400) 

window = Screen() # اوبجكت من النافذة الظاهرة للتنفيذ
window.exitonclick() # ميثود لتثبيت النافذة على الشاشة وعند الضغط على اي مكان تخرج منها
