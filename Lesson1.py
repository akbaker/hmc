print "Watch out world!"

twitter = "@hearmecode"
member = 902

print twitter #variable
print "twitter" #string

print "My governor's name is Martin O'Malley"
#print 'My governor's name is Martin O'Malley' 
#To fix the syntax error in the above quote, type 3 quotation marks on each end
print """My governor's name is Martin O'Malley"""
print "\n"
print "Contact Info:\n Shannon \t shannon@hearmecode.com"
print "\n"

print "Lesson \t\t Topic \n1 \t\t\t Strings and Conditionals \n2 \t\t\t Lists and Loops \n3 \t\t\t Dictionaries & Files"
#python counts the spaces within a print command after \n and \t

print "\n"
print len(twitter)
print len("@hearmecode")
print len("twitter")

print "\n"
print twitter[0]
print twitter[1:5] #python stops short of the index number at the end
print twitter[:5] #same as twitter[0:5]
print twitter[5:]
print twitter[:] #same as print twitter

print "\n"
phone = "(202) 456-7890"
print phone[0:5] #area code
print phone[6:9]

print "\n"
name = "Allison"
age = 27
print "My name is: {0} and my age is: {1}".format(name, age)
grade = "A+"
print "My name is: {0} and I received a {1}".format(name, grade)

print "\n"
phone = "202-555-6789"
print "Call {0} for great pizza".format(phone[4:])

print "\n"
phone = "202-555-9876"
print "Area Code: {0}".format(phone[:3])
print "Local: {0}".format(phone[4:])
print "Different format: ({0}) {1}".format(phone[:3], phone[4:])

print "\n"
email = "shannon@hearmecode.com"
print email.find("@") #returns the index number of the @ symbol
print email.find("Z")

print "\n"
twitter = "@hearmecode"
print twitter.replace("@", "#") #does not change the original variable
print twitter
twitter = twitter.replace("@", "#")
print twitter

print "\n"
length=len(twitter)
print length

print "\n"
students = 60
capacity = 50
assistants = 15

if students < capacity:
	print "Keep recruiting"
else:
	print "End ticket signups"

if assistants == 0: #use 2 equal signs if you're trying to compare something
	print "None? Uh oh!"
elif assistants < students / 5: #elif stands for else if
	print "Keep recruiting TAs"
else:
	print "Aren't the TAs great though?" 

print "\n"
print 5 == 7

print "\n"
volunteers = 120
goal = 100

if volunteers < goal:
	print "Keep recruiting! You need {0} more volunteers.".format(goal-volunteers)
elif volunteers == goal:
	print "There are exactly {0} volunteers. You can relax!".format(volunteers)
else: 
	print "Great work! There are {0} more volunteers than the goal.".format(-(goal-volunteers))
