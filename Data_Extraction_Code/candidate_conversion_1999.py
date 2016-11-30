import csv
import re

c = csv.writer(open("Candidate_Details.csv", "ab"))

#c.writerow(["Constituency","Category","Serial Number","Candidate Name","Sex","Party","Votes","Percentage"])

constituency=None
sno=None
candid_name=None
sex=None
age=None
year=1999
category=None
party=None
symbol=None
valid_general=None
valid_postal=None
valid_total=None
votes_general=None
votes_postal=None
votes_total=None
tot_electors=None
tot_votes=None
cat=""

f=open('../1999/1999_detailed_results_raw_output.csv')
csv_f=csv.reader(f)

flag=0
tmp1=[]
tmp2=[]

tmp3=[]

tmp=""
flag2=0
votes=None
percent=None
for row in csv_f:
	tmp=""
	tmp2=[]
	if not row:
		continue
	elif(row[0]!="" and row[1]!="" and row[2]!="" and ("ELECTORS" not in row[0]) and ("Constituency" not in row[0])):
		if(flag==1):
			c.writerow([year,constituency,sno,candid_name,sex,age,cat,party,symbol,votes_general,votes_postal,votes_total,valid_general,valid_postal,valid_total,percent,tot_electors,tot_votes])
		flag=1
		flag2=1
		candid_name=""
		symbol=None
		tmp1=[]
		tmp3=[]
		
		tmp1=row[0].split()
		n=len(tmp1)
		for x in range(2,n):
			candid_name=candid_name+" "+tmp1[x]
		sno=int(tmp1[0])
		if(row[1]!=""):
			tmp3=row[1].split()
			n=len(tmp3)
			if(n>3):
				for x in range(0,n-3):
					candid_name=candid_name+tmp3[x]
			sex=tmp3[n-3]
			party=tmp3[n-2]
			valid_total=int(tmp3[n-1])
		else:
			age=""
			sex=""
		percent=float(row[2].replace("%",""))

				
	elif((row[0]!="") and (row[1]=="" and row[2]=="")and (flag2==1)):
				candid_name=candid_name+" "+row[0]
	elif("ELECTORS" in row[0]):
		c.writerow([year,constituency,sno,candid_name,sex,age,cat,party,symbol,votes_general,votes_postal,votes_total,valid_general,valid_postal,valid_total,percent,tot_electors,tot_votes])
		flag=0
		flag2=0
	elif(row[0]!="" and ("Constituency" in row[0])):
		constituency=""
		for x in range(0,3):
			tmp=tmp+row[x]
		tmp2=re.findall(r"[\w']+", tmp)
		n=len(tmp2)
		if(tmp2[n-1]=="SC" or tmp2[n-1]=="ST"):
			for x in range(2,n-1):
				constituency=constituency+" "+tmp2[x]
			cat=tmp2[n-1]
		else:
			for x in range(2,n):
				constituency=constituency+" "+tmp2[x]
			cat="GEN"
		flag2=0				
	else: flag2=0

f.close()