# SHIV's string multiplication problem

def to_num(s):
	n = 0
	d = 1
	for c in reversed(s):
		n+= (ord(c)-48)*d
		d*=10
	return n	

# doing it the hard way cuz why not
def mult_str(s1, s2):
	s1 = to_num(s1.lower())
	s2 = to_num(s2.lower())
	return s1*s2

print(mult_str("234", '123'))
# Actual for verification
print(234*123)
