for i in range(1, 15+1):
	fizz = (i % 3 == 0)
	buzz = (i % 5 == 0)

	if fizz or buzz:
		print('Fizz'*fizz + 'Buzz'*buzz)
	else:
		print(f'{i}')
