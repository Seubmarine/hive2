def pi(P):
	from decimal import Decimal
	# attention, nombre pair obligatoire (voir commentaire)
	C = Decimal(4) / 1
	I = 1
	for i in range(P, 0, -1):
	    z = Decimal(4) / (I+2)
	    if i%2 == 0:
	        z = Decimal.copy_negate(z)
	    C += z
	    I += 2

pi(10000000000000000)