import csv
import re
c = csv.writer(open("Candidate_Details.csv", "ab"))
#c.writerow(["Constituency","Serial Number","Candidate Name","Sex","Age","Category","Party","General Votes Secured","Postal Votes Secured","Total Votes Secured"])

year=2004
constituency=None
sno=None
candid_name=None
sex=None
age=None
category=None
party=None
symbol=None
valid_general=None
valid_postal=None
valid_total=None
tot_electors=None
tot_votes=None
percent=None
votes_general=None
votes_postal=None
votes_total=None
cat=None

f=open('../2004/2004_detailed_results_raw_output.csv')
csv_f=csv.reader(f)

flag=0
tmp1=[]
tmp2=[]

tmp3=[]

tmp=""
flag2=0

for row in csv_f:
	tmp=""
	tmp2=[]
	if not row:
		continue
	
	elif(row[0]!="" and row[1]!="" and row[2]!="" and row[3]!="" and row[4]!="" and row[5]!="" and ("Constituency" not in row[0])):
		if(flag==1):
			c.writerow([year,constituency,sno,candid_name,sex,age,cat,party,symbol,votes_general,votes_postal,votes_total,valid_general,valid_postal,valid_total,percent,tot_electors,tot_votes])
			
		flag=1
		flag2=1
		candid_name=""
		symbol=None
		tmp1=[]
		tmp2=[]
		tmp3=[]
		
		tmp1=row[0].split()
		n=len(tmp1)
		for x in range(2,n):
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
			age=0
			sex=""
		tmp2=row[2].split()
		cat=tmp2[0]
		party=tmp2[1]
		valid_general=int(row[3])
		valid_postal=int(row[4])
		valid_total=int(row[5])

				
	elif((row[0]!="" or row[3]!="") and (row[4]=="" and row[5]=="")and (flag2==1)):
				candid_name=candid_name+" "+row[0]
	elif("TOTAL" in row[1]):
		c.writerow([year,constituency,sno,candid_name,sex,age,cat,party,symbol,votes_general,votes_postal,votes_total,valid_general,valid_postal,valid_total,percent,tot_electors,tot_votes])
		flag2=0
		flag=0
	elif(row[0]!="" and ("Constituency" in row[0])):
		constituency=""
		for x in range(0,6):
			tmp=tmp+row[x]
		tmp2=re.findall(r"[\w']+", tmp)
		n=len(tmp2)
		if(tmp2[n-1]=="SC" or tmp2[n-1]=="ST"):
			for x in range(2,n-1):
				constituency=constituency+" "+tmp2[x]
		else:
			for x in range(2,n):
				constituency=constituency+" "+tmp2[x]
		flag2=0			
	else: flag2=0
#c.writerow([constituency,sno,candid_name,sex,age,cat,party,votes_general,votes_postal,votes_total])
f.close()