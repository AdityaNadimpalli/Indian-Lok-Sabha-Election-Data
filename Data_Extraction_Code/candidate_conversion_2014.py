import csv
import re

#Open OutputFile
c = csv.writer(open("Candidate_Details.csv", "wb"))

#Write Headers
c.writerow(["Year","Constituency","Serial Number","Candidate Name","Sex","Age","Category","Party","Symbol","General Votes Secured","Postal Votes Secured","Total Votes Secured","Valid General Votes","Valid Postal Votes","Valid Total Votes","Percent","% of votes secured out of total electors","% of votes secured out of total votes polled"])

#Initialize Data Variables

constituency=None 
sno=None
candid_name=None
sex=None #Candidate Sex
age=None #Candidate Age
percent=None #Percent of Votes 
valid_general=None #Valid General Votes
valid_postal=None #Valid Postal Votes
valid_total=None #Total Valid Votes

party=None

year=2014
symbol=None #party symbol
votes_general=None #General Votes Secured
votes_postal=None #Postal Votes Secured
votes_total=None #Total Votes Secured
tot_electors=None #% of votes secured out of total electors
tot_votes=None #% of votes secured out of total votes polled
cat=None #Category

#Open Raw Data Extracted by Tabula
f=open('../2014/2014_detailed_results_raw_data.csv')
csv_f=csv.reader(f)


#Temporary Variables
flag=0
flag2=None
tmp1=[]
tmp2=[]
tmp3=[]
tmp4=[]
tmp=""
sum=0

for row in csv_f:
	tmp=""
	tmp2=[]
	
	if not row:
		#Ignore Blank Rows
		continue
	
	elif(row[0]!="" and row[3]!="" and row[4]!="" and row[5]!="" and row[6]!="" and row[7]!="" and row[8]!=""): #Indicates Presence of a row with candidate details
		if(flag==1): #A candidates details have been loaded into the data variables, including details that may have extended to the next line
			#Write Data
			c.writerow([year,constituency,sno,candid_name,sex,age,cat,party,symbol,votes_general,votes_postal,votes_total,valid_general,valid_postal,valid_total,percent,tot_electors,tot_votes])
			
		flag=1 #A candidates details have been recorded, now data will be loaded with details for the next candidate
		flag2=1 #Row containing Candidate Details has been detected but some date may have carried on to next line
		candid_name=""
		symbol=""
		
		#Temporary Lists hold multiple data items that are present in the same column in the raw tabula output. These need to be further split to separate the column data into age, sex etc.
		tmp1=[]
		tmp2=[]
		tmp3=[]
		tmp4=[]
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
		tmp2=row[3].split()
		n=len(tmp2)
		party=tmp2[0]
		for x in range(1,n):
			symbol=symbol+" "+tmp2[x]
		
		tmp4=row[4].split()
		n=len(tmp4)
		if (n>1):
			symbol=symbol+tmp4[0]
			votes_general=int(tmp4[1])
		else:
			votes_general=int(row[4])
		votes_postal=int(row[5])
		votes_total=int(row[6])
		tot_electors=float(row[7])
		tot_votes=float(row[8])
		sum=sum+votes_general		
	elif((row[0]!="" or row[3]!="") and (row[4]=="" and row[5]=="" and row[6]=="" and row[7]=="" and row[8]=="" and flag2==1)): #Candidate's name or party symbol has carried over to the next line, hence this should be appended before writing the row of data for that candidate
				candid_name=candid_name+" "+row[0]
				symbol=symbol+" "+row[3]	
	elif("TOTAL" in row[3] and "INDIA" not in row[3]):
		#Writing the last row for a constituency
		c.writerow([year,constituency,sno,candid_name,sex,age,cat,party,symbol,votes_general,votes_postal,votes_total,valid_general,valid_postal,valid_total,percent,tot_electors,tot_votes])
		flag2=0
		flag=0
		if(sum!=int(row[4])):
			#Check if vote total of candidates matches the constituency total
			print constituency
		sum=0
	elif(row[0]!="" and ("CONSTITUENCY" in row[0])):
		constituency=""
		for x in range(0,9):
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