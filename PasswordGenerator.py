import string, random, nltk, ctypes, time, sys

lettlower = """abcdefghijklmnopqrstuvwxyz""".split()
lettupper = """ABCDEFGHIJKLMNOPQRSTUVWXYZ""".split()
possible = """0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', '
	v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '
	!', '"', '#', '$', '%', '&', ''', '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~
	""".split("', '")
difficulty = input("How difficult would you like your password to be\n[Hard, Medium, Easy]\n?:")
digits = int(input("how many characters: "))
passw=''
if(difficulty[0] is "e" or difficulty[0] is "E"):
	from nltk.corpus import words
	word_list = words.words()
	passw=''
	count=0
	while(True):
		w=word_list[random.randint(0,236735)]
		count+=1
		if(passw == '' or len(passw)+len(w) <= digits):
			passw+=w
			continue
		elif(count>1000000):
			break
		else:
			continue
	while(True):
		passw+=str(random.randint(0, 9))
		if(len(passw) >= digits):
			break
	# prints 236736
	print(passw)
elif(difficulty[0] is "m" or difficulty[0] is "M"):
	from nltk.corpus import words
	word_list = words.words()
	count = 0
	w = ''
	while(True):
		count+=1
		w=word_list[random.randint(0,236735)]
		if(passw == '' or (len(passw)+len(w)) < digits):
			passw+=w
			count=0
			continue
		elif(count >= 25000000):
			break
		else:
			break
	while(True):
		passw+=str(random.randint(0, 9))
		if(len(passw) >= digits):
			break
	ran = random.randint(0, len(lettlower)-1)
	for l in range(random.randint(3, 6)):
		passw = passw.replace(lettlower[ran], lettupper[ran])

	passw = passw.replace('o', '0').replace('O', '0').replace('A', '4').replace('a', '4').replace('l', '1').replace('l', '1').replace('e', '3').replace('E', '3').replace('B', '8')

	# prints 236736
	print(passw)
elif(difficulty[0] is "h" or difficulty[0] is "H"):
	# print(possible)
	generated = int(''.join(str(ord(c)) for c in input("Smack your Keyboard a bit for me please, and kindly press enter when you are satisfied: ")))
	for i in range(digits):
		rand = generated%int(random.randint(0,65536))

		if rand > len(possible):
			rand = rand%(len(possible)-1)

			passw += possible[rand]

	print("".join(passw.split()))
