bread_slices = 2
peanut_butter = 0
jelly = 1

if bread_slices == 2 and peanut_butter == 1 and jelly == 1:
	print "You can make 1 PB&J sandwich."
elif bread_slices == 2 and ((peanut_butter == 1 and jelly == 0) or (jelly == 1 and peanut_butter == 0)):
	if peanut_butter == 1:
		print "You can make 1 peanut butter sandwich."
	else:
		print "You can make 1 jelly sandwich."
elif bread_slices % 2 == 0:
	if bread_slices > 2: 
		if peanut_butter >= (bread_slices/2) and jelly >= (bread_slices/2):
			print "You can make {0} full PB&Js.".format(bread_slices/2)
		elif peanut_butter < (bread_slices/2) or jelly < (bread_slices/2):
			if peanut_butter < jelly:
				print "You can make {0} PB&Js.".format(peanut_butter)
			else:
				print "You can make {0} PB&Js.".format(jelly)
		else:
			print "Head to the grocery store to buy ingredients."
elif bread_slices % 2 > 0:
	if bread_slices > 2: 
		if peanut_butter > (bread_slices/2) and jelly > (bread_slices/2):
			print "You can make {0} full and {1} open-faced PB&Js.".format(bread_slices/2, bread_slices%2)
		elif peanut_butter <= (bread_slices/2) or jelly <= (bread_slices/2):
			if peanut_butter < jelly:
				print "You can make {0} PB&Js.".format(peanut_butter)
			else:
				print "You can make {0} PB&Js.".format(jelly)
		else:
			print "Head to the grocery store to buy ingredients."
else: 
	print "Head to the grocery store to buy ingredients."

