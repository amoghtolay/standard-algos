'''
Codechef January Cook-off
3rd January 2012
Amogh Tolay
http://www.codechef.com/JAN13/problems/CVOTE
The problem basically boils down to this:
First few lines gives names of chefs and their countries. Next few lines
give the votes. The more votes a chef gets, he wins. More votes a
country gets, it wins. Find winner.
'''

s = raw_input()
numChefs, numVotes = [int(i) for i in s.split(' ')]
maxChef = ['name',0]
maxCountry = ['country', 0]

chefList = {}
countrySet = set()
countryList = {}
for i in range(numChefs):
	namePlace = raw_input()
	name, country = [item for item in namePlace.split(' ')]
	chefList[name] = [country, 0]
	countrySet.add(country)

for country in countrySet:
	countryList[country] = 0

for i in range(numVotes):
	chef = raw_input()
	# Update chef's vote count, check for max and clashes
	chefList[chef][1] = chefList[chef][1] + 1
	country = chefList[chef][0]
	countryList[country] = countryList[country] + 1
	
	if maxChef[1] < chefList[chef][1] :
		maxChef = [chef,chefList[chef][1]]
	elif maxChef[1] == chefList[chef][1]:
		if maxChef[0] > chef:
			maxChef = [chef,chefList[chef][1]]
	
	if maxCountry[1] < countryList[country] :
		maxCountry = [country,countryList[country]]
	elif maxCountry[1] == countryList[country]:
		if maxCountry[0] > country:
			maxCountry = [country,countryList[country]]
print maxCountry[0]
print maxChef[0]
