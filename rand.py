import random

r = random.randint(1,100)
i = 0 # 猜幾次
while True:
	num = input('請輸入一個數字： ')
	num = int(num)
	i = i + 1 # 可以寫： i+=1
	if num == r:
		print('終於猜對了, 這是你猜的第', i , '次')
		break
	elif num > r:  # 可以用 elif
		print('比答案大, 這是你猜的第', i , '次')
	elif num < r:
		print('比答案小, 這是你猜的第', i , '次')