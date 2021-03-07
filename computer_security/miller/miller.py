A = [49, 80, 438]
St = [15,30,60,120,240,480]

p = 481

def Check(setup):
	if ((p - 1) in setup) and (setup[-1] == 1):
		return "Свидетель"
	if setup[0] == 1:
		return "Свидетель"
	return "Не свидетель"

def main():
	for a in A:
		exit = []

		for st in St:
			exit.append(a**st % p)
		
		print (a, exit, Check(exit))

if __name__ == '__main__':
	main()