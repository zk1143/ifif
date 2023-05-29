driving = input('你有沒有開過車?:')
if driving !='有' or driving !='沒有':
	print('只能回答有跟沒有')
	raise SystemExit
age = input('你的年齡:')
age = int(age)
if driving == ('有'):
	if age >= 18:
		print('ok')
	else:
		print('你怎麼開過車?')
elif driving == ('沒有'):
	if age <= 18:
		print('很好，過幾年後就可以考')
	else :
		print('這麼大了還不去考，都給人接送嗎?')
