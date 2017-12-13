import urllib2
import urllib
import pandas as pd
zillowKey = "<PLACE ZILLOW API KEY HERE>"
df = pd.read_csv('profiles.csv')
saved_column = df.location.unique() #you can also use df['column_name']
city = []
for s in saved_column:
    cityString = s.split(",")
    if(cityString[1] == " california"):
        city.append(cityString[0])
print(city)
f = open('demographics.xml','w')
demographic_data = []
for s in city:
    currCity = urllib.quote_plus(s)
    print currCity
    demographic_data.append(urllib2.urlopen("http://www.zillow.com/webservice/GetDemographics.htm?state=ca&city="+currCity+"&zws-id="+zillowKey).read())
f.write("<demographics type=\"array\">" + "\n")
for s in demographic_data:
    f.write(s)
f.write("<\demographics>")
f.close()    

