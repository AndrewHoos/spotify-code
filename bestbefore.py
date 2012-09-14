## Author: Andrew Hoos
## File: bestbefore.py
## Purpose: The purpose of this file is to parse an ambiguous date of the form X/Y/Z to
## the earliest valid date between 2000 and 2999 inclusive. If no date order is valid
## the string is returned as invalid
## Limitations: The dates are assumed to be 
## usage: python rscan.py molecule.inp > molecule.log
## Version: 0.1
## Last edited: 5/10/12

import re
import sys
import itertools

	

def validMonth(month):
	value = int(month)
	if value in range(1,13):
		return True
	else:
		return False

def validDay(day):
	value = int(day)
	if value in range(1,32):
		return True
	else:
		return False
		

		
def leapYear(year):
	yearValue = int(year)
	if yearValue <2000:
		yearValue+=2000
	
	if yearValue%4==0:
		if yearValue%400==0:
			return True
		elif yearValue%100==0:
			return False
		else:
			return True
	return False
	
		
def validDayMonthYear(day, month, year):
	#dates are rejected based on likelihood of incorrect Value

	#reject values outside range
	if not validMonth(month):
		return False
	if not validDay(day):
		return False
	#assume year is valid
	dayValue = int(day)
	monthValue =int(month)
	
	
	# handle April, June, September, and november
	if dayValue > 30 and monthValue in [4,6,9,11]:
		return False
	# handle February
	if dayValue > 29 and monthValue == 2:
		return False
	#handle leap years
	if dayValue == 29 and monthValue == 2 and not leapYear(year):
		return False
	
	return True
	
#return list [day, month,year] with ints for strings
def dateForDayMonthYear(day,month,year):
	if int(year)<2000:
		yearValue = int(year)+2000
	else:
		yearValue = int(year)
		
	return [int(day),int(month), yearValue]

#expects list [day, month year] with ints. Return true if equal
def	dateOneIsEarlier(date1,date2):
	if date1[2] < date2[2]:
		return True
	elif date1[2] > date2[2]:
		return False
	else:
		if date1[1] < date2[1]:
			return True
		elif date1[1] > date2[1]:
			return False
		else:
			if date1[0] < date2[0]:
				return True
			elif date1[0] > date2[0]:
				return False
			else:
				return True;

def printDate(date):
	sys.stdout.write(str(date[2])+"-")
	if date[1] < 10:
		sys.stdout.write("0"+str(date[1])+"-")
	else:
		sys.stdout.write(str(date[1])+"-")
	if date[0] < 10:
		sys.stdout.write("0"+str(date[0]))
	else:
		sys.stdout.write(str(date[0]))
	sys.stdout.write("\n")

##read line and trim whitespace characters
line=sys.stdin.readline().strip()
##split on /
values = re.split("/",line)

validDates=[]
##check permutations and add each to valid list
for i in itertools.permutations(values):
	i = list(i)
	if validDayMonthYear(i[0],i[1],i[2]):
		validDates.append(dateForDayMonthYear(i[0],i[1],i[2]))
		
minDate = 0
##check valid list for minimum date
for i in range(len(validDates)):
	if dateOneIsEarlier(validDates[i],validDates[minDate]):
		minDate = i
		
if(len(validDates)):
	printDate(validDates[minDate])
else:
	print(line.strip()+" is illegal")



#print(dateOneIsEarlier([2, 3, 2001],[1, 2, 2003]))




	
	
	


########