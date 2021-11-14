import random
# 讓使用者決定範圍
end = input('請決定猜的範圍結束值：')
start = input('請決定猜的範圍開始值：')
start = int(start)
end = int(end)

r = random.randint(start,end)

i = 0 # 猜幾次
while True:
	num = input('請輸入一個數字： ')
	num = int(num)
	i = i + 1 # 可以寫： i+=1
	if num == r:
		print('終於猜對了')
		print('這是你猜的第', i , '次')
		break
	elif num > r:  # 可以用 elif
		print('比答案大')
	elif num < r:
		print('比答案小')
	print('這是你猜的第', i , '次')