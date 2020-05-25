## Dictionary
print('....... DICTIONARIES IN PYTHON .......\n');

marks = {
	'Deepank':89,
	'Ashwin':97,
	'Pranav':98,
	'Vanssh':99
}

details = {
	'Deepank': ['Tanmay', 'Raunak', 'Mohit'],
	'Hobbies': ['Rnning', 'Exploring New Things' , 'Travelling']
}

print("MARKS : ", marks)
print("Details : ", details)

print('Keys: ', marks.keys())
print('Values: ', marks.values())

# print('->>> DELETE from Dictionary')
# del marks['Deepank']

print('->>> UPDATE Dictionary')
marks['Deepank']=95
print(marks)

print('->>> Find Key in Dictionary')
if 'Deepank' in marks:
	print('Key: Deepank Present in Dictionary')
else:
	print('Key: Deepank NOT Present in Dictionary')

print('... Length of dictionary: ',len(marks))

print('>>> Print Key-Value Pair')
for i in marks:
	print(i,marks[i])