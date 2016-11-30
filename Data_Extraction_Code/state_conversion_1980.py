import csv
import re
c = csv.writer(open("Constituency_Totals.csv", "ab"))
f=open('../1980/1980_detailed_results_raw_output.csv')

csv_f=csv.reader(f)
#c.writerow(["State","Constituency","Category","Total Electors","Total Voters","Poll Percentage","Valid Votes"])

state=""
constituency=""
year=1980
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
a=""
b=""
tmp=""
tmp2=[]
for row in csv_f:
	tmp=""
	tmp2=[]
	tmp3=[]
	if not row:
		continue
		
	elif ("rptDetailedResults" in row[0]): #ignore page footers
		continue
	elif(row[0]!="" and row[2]=="" and flag==1 and ("Constituency" not in row[0])):
		state=row[0]+row[1]+row[2]
		flag=0
		#print sum,"\n"
		sum=0
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
		flag=0
	elif ("ELECTORS" in row[0]):
		elec=""
		for x in range(0,3):
			elec=elec+row[x]
		tmp3=re.findall(r"[\w']+", elec)
		n=len(tmp3)
		if(n>0):
			con_total_electors=int(tmp3[1])
			con_total_voters=int(tmp3[3])
			a=tmp3[6]
			b=tmp3[7]
			a=a+"."+b
			con_pp=float(a)
			con_valid_total=int(tmp3[10])
			c.writerow([year,state,constituency,cat,con_total_electors,con_total_voters,con_pp,con_general_votes,con_postal_votes,con_total_votes,con_valid_general,con_valid_postal,con_valid_total,con_percentage_electors,con_percentage_votes])

		flag=1
		sum=sum+con_valid_total
	else: 
		flag=0
f.close()
