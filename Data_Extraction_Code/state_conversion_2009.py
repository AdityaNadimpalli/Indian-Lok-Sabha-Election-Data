import csv
import re
c = csv.writer(open("Constituency_Totals.csv", "ab"))
f=open('../2009/2009_detailed_results_raw_output.csv')

csv_f=csv.reader(f)
#c.writerow(["State","Constituency","Total Electors","Total General Votes Secured","Total Postal Votes Secured","Total Votes Secured","% of votes secured out of total electors","% of votes secured out of total votes polled"])
tmp=""
tmp2=[]
state=""
constituency=""
year=2009
con_total_electors=None
con_total_voters=None
con_pp=None
con_general_votes=None
con_postal_votes=None
con_total_votes=None
con_valid_general=None
con_valid_postal=None
con_valid_total=None
con_percentage_electors=None
con_percentage_votes=None
cat=None
flag=1
flag3=1
tmp=""
tmp2=[]

for row in csv_f:
	tmp=""
	tmp2=[]
	tmp3=[]
	if not row:
		continue
	elif(row[0]!="" and row[1]!="" and row[2]!="" and row[3]!="" and row[4]!="" and row[5]!="" and row[6]!="" and row[7]!="" and flag3==1):
		tmp3=row[2].split()
		cat=tmp3[0]
		flag3=0
	elif(row[0]!="" and row[2]=="" and row[3]=="" and row[4]=="" and row[5]=="" and row[6]=="" and row[7]=="" and flag==1):
		state=row[0]+row[1]
		flag=0
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
		con_total_electors=tmp2[y+2]
		flag=0
	elif (("TOTAL" in row[1]) and ("INDIA" not in row[1])):
		con_general_votes=row[3]
		con_postal_votes=row[4]
		con_total_votes=row[5]
		con_percentage_electors=row[6]
		con_percentage_votes=row[7]
		c.writerow([year,state,constituency,cat,con_total_electors,con_total_voters,con_pp,con_general_votes,con_postal_votes,con_total_votes,con_valid_general,con_valid_postal,con_valid_total,con_percentage_electors,con_percentage_votes])
		flag=1
		flag3=1
	else: 
		flag=0
f.close()
