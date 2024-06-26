import pyinputplus as pyip  #叫出pyip的工具箱
import math                 #叫出math的工具箱
side = pyip.inputNum('請輸入對邊',min=0,max=100) #pyip可以提醒錯誤或自動將字串轉為數值 inputNum可以設最大及最小範圍
another_side = pyip.inputNum('請輸入斜邊')
radian = math.asin(side / another_side)
degree = math.degrees(radian)
print(f"對邊:{side},斜邊:{another_side},角度:{round(degree,ndigits=2)}")