import csv
import re
c = csv.writer(open("Constituency_Totals.csv", "ab"))
f=open('../2004/2004_detailed_results_raw_output.csv')

csv_f=csv.reader(f)
#c.writerow(["State","Constituency","Category","Total General Votes Secured","Total Postal Votes Secured","Total Votes Secured"])

state=""
constituency=""
year=2004
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
cat=""
flag=1
tmp=""
tmp2=[]
for row in csv_f:
	tmp=""
	tmp2=[]
	if not row:
		continue
	elif(row[0]!="" and row[2]=="" and row[3]=="" and row[4]=="" and row[5]=="" and flag==1 and ("Constituency" not in row[0])): #Lines containing state name will match this condition
		state=row[0]+row[1]
		flag=0 #state name can come only after line containing constituency totals
	elif(row[0]!="" and ("Constituency" in row[0])): #Name of constituency and category in one line in input file
		constituency=""
		for x in range(0,6):
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
		flag=0
	elif (("TOTAL" in row[1]) and ("INDIA" not in row[3])): #constituency totals in one line in input file
		con_valid_general=int(row[3])
		con_valid_postal=int(row[4])
		con_valid_total=int(row[5])
		c.writerow([year,state,constituency,cat,con_total_electors,con_total_voters,con_pp,con_general_votes,con_postal_votes,con_total_votes,con_valid_general,con_valid_postal,con_valid_total,con_percentage_electors,con_percentage_votes])
		flag=1
	else: 
		flag=0
f.close()
