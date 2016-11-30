import csv
import re

#Open Output File to which the 2009 data will be appended
c = csv.writer(open("Candidate_Details.csv", "ab"))

#The following line of code to write the headers of the csv file need not be executed if we are appending to the 2014 data, which already contains the required headers 
#c.writerow(["Constituency","Serial Number","Candidate Name","Sex","Age","Category","Party","General Votes Secured","Postal Votes Secured","Total Votes Secured","% of votes secured out of total electors","% of votes secured out of total votes polled"])
constituency=None
sno=None
year=2009
candid_name=None
sex=None #Candidate Sex
age=None #Candidate Age

party=None #Political Party

symbol=None #Party Symbol
votes_general=None #General Votes Secured
votes_postal=None #Postal Votes Secured
votes_total=None #Total Votes Secured
tot_electors=None #% of votes secured out of total electors
tot_votes=None #% of votes secured out of total votes polled
cat=None #Category
valid_general=None
valid_postal=None
valid_total=None
percent=None

f=open('../2009/2009_detailed_results_raw_output.csv')
csv_f=csv.reader(f)

flag=0
flag2=0
tmp1=[]
tmp2=[]

tmp3=[]

tmp=""
sum=0
for row in csv_f:
	tmp=""
	tmp2=[]
	if not row:
		continue
	elif(row[0]!="" and row[1]!="" and row[2]!="" and row[3]!="" and row[4]!="" and row[5]!="" and row[6]!="" and row[7]!=""):
		if(flag==1):
			c.writerow([year,constituency,sno,candid_name,sex,age,cat,party,symbol,votes_general,votes_postal,votes_total,valid_general,valid_postal,valid_total,percent,tot_electors,tot_votes])
			
		flag=1
		flag2=1
		candid_name=""
		symbol=None
		party=""
		tmp1=[]
		tmp2=[]
		tmp3=[]

		tmp1=row[0].split()
		n=len(tmp1)
		for x in range(1,n):
			candid_name=candid_name+" "+tmp1[x]
		sno=int(tmp1[0])
		if(row[1]!=""):
			
			tmp3=row[1].split()
			n=len(tmp3)
			if(n>2):
				for x in range(0,n-2):
					candid_name=candid_name+tmp3[x]
			sex=tmp3[n-2]
			
			age=int(tmp3[n-1])
			
		else:
			age=None
			sex=""
		cat=row[2]
		tmp2=row[2].split()
		cat=tmp2[0]
		n=len(tmp2)
		for x in range(1,n):
			party=party+" "+tmp2[x]
		
		votes_general=int(row[3])
		votes_postal=int(row[4])
		votes_total=int(row[5])
		tot_electors=float(row[6])
		tot_votes=float(row[7])
		sum=sum+votes_general		
	elif((row[0]!="" or row[3]!="") and (row[4]=="" and row[5]=="" and row[6]=="" and row[7]=="" and flag2==1)):
				candid_name=candid_name+" "+row[0]
				
	elif("TOTAL" in row[1] and "INDIA" not in row[1]):
		c.writerow([year,constituency,sno,candid_name,sex,age,cat,party,symbol,votes_general,votes_postal,votes_total,valid_general,valid_postal,valid_total,percent,tot_electors,tot_votes])
		flag2=0
		flag=0
		if(sum!=int(row[3])):
			print constituency
		sum=0
	elif(row[0]!="" and ("CONSTITUENCY" in row[0])):
		constituency=""
		for x in range(0,8):
			tmp=tmp+row[x]
		tmp2=re.findall(r"[\w']+", tmp)
		n=len(tmp2)
		y=2
		while("Total" not in tmp2[y]):
			constituency=constituency+" "+tmp2[y]
			y=y+1	
		flag2=0
	else: flag2=0
f.close()