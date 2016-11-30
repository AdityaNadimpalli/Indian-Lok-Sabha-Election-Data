import csv
import re

#Open Output File
c = csv.writer(open("Constituency_Totals.csv", "wb"))

#Open Raw Data file from tabula
f=open('../2014/2014_detailed_results_raw_data.csv')
csv_f=csv.reader(f)

#Write Headers
c.writerow(["Year","State","Constituency","Category","Total Electors","Total Voters","Poll Percentage","Total General Votes Secured","Total Postal Votes Secured","Total Votes Secured","Total General Valid Votes","Total Postal Valid Votes","Total Valid Votes","% of votes secured out of total electors","% of votes secured out of total votes polled"])

#Data Variables
constituency=""
state=""
year=2014
con_total_electors=None #Constituency Total Electors
con_total_voters=None #Constituency Total Voters
con_pp=None #Constituency Poll Percentage
con_general_votes=None #Constituency General Votes Secured
con_postal_votes=None #Constituency Postal Votes Secured
con_total_votes=None #Constituency Total Votes
con_valid_general=None #Constituency Valid General Votes
con_valid_postal=None #Constituency Valid Postal Votes
con_valid_total=None #Constituency Valid Total Votes
con_percentage_electors=None
con_percentage_votes=None
cat=None

tmp=""
tmp2=[]
flag=1
flag3=1

for row in csv_f:
	tmp=""
	tmp2=[]
	if not row: #Skip empty rows
		continue
	elif(row[0]!="" and row[1]!="" and row[2]!="" and row[3]!="" and row[4]!="" and row[5]!="" and row[6]!="" and row[7]!="" and row[8]!="" and flag3==1): #Obtain constituency category from the first candidate in the constituency (only for 2014 and 2009 data)
		cat=row[2]
		flag3=0
	elif(row[0]!="" and row[2]=="" and row[3]=="" and row[4]=="" and row[5]=="" and row[6]=="" and row[7]=="" and row[8]=="" and flag==1): #Getting the state name
		state=row[0]+row[1]
		flag=0
	elif(row[0]!="" and ("CONSTITUENCY" in row[0])):
		constituency=""
		#concatenate all elements of the input file row so that names and numbers split across different columns in input file will get joined again
		for x in range(0,9):
			tmp=tmp+row[x]
		#separate the concatenated string into regular expressions which contain data
		tmp2=re.findall(r"[\w']+", tmp)
		n=len(tmp2)
		y=2
		#Constituency name and constituency total electors given in same line, first collect the constituency name and then the total electors number.
		while("Total" not in tmp2[y]):
			constituency=constituency+" "+tmp2[y]
			y=y+1
		con_total_electors=tmp2[y+2]
		flag=0
	elif (("TOTAL" in row[3]) and ("INDIA" not in row[3])):
		#all the following data is in one line in the input file
		con_general_votes=row[4]
		con_postal_votes=row[5]
		con_total_votes=row[6]
		con_percentage_electors=row[7]
		con_percentage_votes=row[8]
		#write the data into output file
		c.writerow([year,state,constituency,cat,con_total_electors,con_total_voters,con_pp,con_general_votes,con_postal_votes,con_total_votes,con_valid_general,con_valid_postal,con_valid_total,con_percentage_electors,con_percentage_votes])
		flag=1 #State name can come only after line containing constituency totals
		flag3=1 #new constituency to be read next, so category for next constituency should be set
	else: 
		flag=0
f.close()
