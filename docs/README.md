# Лабораторная работа 3
## unittest для файла rectangle.py
|Тест        |Входные данные|Expected     |Actual       |
|:----------:|:-------------|:-----------:|:-----------:|
|area(10,0)  |a=10,b=0      |Invalid input|Invalid input|
|area(2,3)   |a=2,b=3       |6            |6            |
|area(3,"A") |a=3,b="A"     |Invalid input|Invalid input|
|area(3,-1)  |a=3,b=-1      |Invalid input|Invalid input|
|area(2.3,3) |a=2.3,b=3     |Invalid input|Invalid input|
|area(3,True)|a=3,b=True    |Invalid input|Invalid input|
