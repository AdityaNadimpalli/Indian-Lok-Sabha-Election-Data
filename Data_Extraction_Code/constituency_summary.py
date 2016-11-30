import csv
import re


#Open the output file "Constituency_Summary"
c = csv.writer(open("Constituency_Summary.csv", "wb"))

#Open the file which contains raw data extracted by tabula (for 2014)
f=open('../2014/2014_constituency_summary_raw_data.csv')
csv_f=csv.reader(f)

#Headers for Output File "Contstituency_Summary"
c.writerow(["Year","State","Constituency","State_Code","Constituency_Number","Category",
"Candidates_Nominated_Men","Candidates_Nominated_Women","Candidates_Nominated_Others","Candidates_Nominated_Total",
"Nominations_Rejected_Men","Nominations_Rejected_Women","Nominations_Rejected_Others","Nominations_Rejected_Total",
"Candidates_Withdrawn_Men","Candidates_Withdrawn_Women","Candidates_Withdrawn_Others","Candidates_Withdrawn_Total",
"Contested_Men","Contested_Women","Contested_Others","Contested_Total",
"Forfeited_Men","Forfeited_Women","Forfeited_Others","Forfeited_Total",
"General_Electors_Men","General_Electors_Women","General_Electors_Others","General_Electors_Total",
"Overseas_Electors_Men","Overseas_Electors_Women","Overseas_Electors_Others","Overseas_Electors_Total",
"Service_Electors_Men","Service_Electors_Women","Service_Electors_Others","Service_Electors_Total",
"Total_Electors_Men","Total_Electors_Women","Total_Electors_Others","Total_Electors",
"General_Voters_Men","General_Voters_Women","General_Voters_Others","General_Voters_Total",
"Overseas_Voters_Men","Overseas_Voters_Women","Overseas_Electors_Others","Overseas_Voters_Total",
"Proxy_Voters",
"Postal_Voters_Men","Postal_Voters_Women","Postal_Voters_Total",
"Total_Voters_Men","Total_Voters_Women","Total_Voters",
"Total Votes Polled",
"Rejected_Votes","Votes Rejected Due To Other Reason","% of Votes Rejected","Rejected_Votes_Postal",
"Polling_Percentage_Men","Polling_Percentage_Women","Polling_Percentage_Total",
"Votes Not Retrieved From EVM",
"TOTAL VOTES POLLED ON EVM","TOTAL DEDUCTED VOTES FROM EVM","TOTAL VALID VOTES POLLED ON EVM",
"POSTAL VOTES COUNTED","POSTAL VOTES DEDUCTED","VALID POSTAL VOTES",
"Valid Votes",
"Total_Valid_Votes_Polled",
"TEST VOTES POLLED ON EVM",
"VOTES POLLED FOR NOTA",
"Missing_Votes",
"Ballot_Paper_Set_Apart",
"Tendered_Votes",
"Polling_Stations",
"Avg_Per_Polling_Station",
"Re-Poll_Stations",])


#Initialize Variables
year=2014
state=None
constituency=None
state_code=None
constituency_no=None
cat=None #category

mcn=None #Male Candidates Nominated
wcn=None #Women Candidates Nominated
ocn=None #Other Candidates Nominated
tcn=None #Total Candidates Nominated

mcnr=None #Male Candidate Nominations Rejected
wcnr=None #Women  Candidate Nominations Rejected
ocnr=None #Other Candidate Nominations Rejected
tcnr=None #Total Candidate Nominations Rejected

mcw=None #Male Candidates Withdrawn
wcw=None #Women Candidates Withdrawn
ocw=None #Other Candidates Withdrawn
tcw=None #Total Candidates Withdrawn

mcfd=None #Male Candidate Forfeited Deposits
wcfd=None #Women Candidate Forfeited Deposits
ocfd=None #Other Candidate Forfeited Deposits
tcfd=None #Total Candidates Forfeied Deposits

mcc=None #Male Candidates Contested
wcc=None #Women Candidates Contested
occ=None #Other Candidates Contested
tcc=None #Total Candidates Contested

meg=None #Male Electors General
weg=None #Women Electors General
oeg=None #Other Electors General
teg=None #Total Electors General

mes=None #Male Electors Service
wes=None #Woman Electors Service 
oes=None #Other Electors Service
tes=None #Total Electors Service

meo=None #Male Electors Overseas
weo=None #Woman Electors Overseas
oeo=None #Other Electors Overseas
teo=None #Total Electors Overseas

met=None #Male Electors Total
wet=None #Women Electors Total
oet=None #Other Electors Total
te=None #Total Electors

mvg=None #Male Voters General
wvg=None #Women Voters General
ovg=None #Other Voters General
tvg=None #Total Voters General

mvo=None #Male Voters Overseas
wvo=None #Women Voters Overseas
ovo=None #Other Voters Overseas
tvo=None #Total Voters Overseas

proxy=None #Proxy Voters

mvp=None #Male Voters Postal
wvp=None #Women Voters Postal
tvp=None #Total Voters Postal

mvt=None #Male Voters Total
wvt=None #Women Voters Total
tv=None #Total Voters

polled_votes=None #Polled Votes

rv=None #Rejected Votes
rv_other_reason=None #Rejected Votes (due to Other Reasons)
rejected_percent=None #% of Votes Rejected
rv_postal=None #Rejected Votes (Postal)

mpp=None #Male Polling Percentage
wpp=None #Women Polling Percentage
tpp=None #Total Polling Percentage


evm=None # Votes Not Retrieved from EVM 

evm_total=None #Total Votes Polled on EVM 
evm_deducted=None #Total EVM Votes Deducted
evm_valid=None #Total Valid EVM Votes Polled

postal_total=None #Total Postal Votes Polled
postal_deducted=None #Total Postal Votes Deducted
postal_valid=None #Total Valid Postal Votes Polled

valid_votes=None #Valid Votes
tvvp=None #Total Valid Votes Polled

test_votes=None 
nota_votes=None
missing_votes=None
bpsa=None #Ballot Paper Set Apart
tendered_votes=None
ps_no=None #Number of Polling Stations
ps_avg=None #Average Electors Per Polling Station
repoll=None #No of Re-poll Stations

#Function to Write Data into Output File
def write_data():
	#Declaring variables as Global
	global state
	global constituency
	global state_code
	global constituency_no
	global cat

	global mcn
	global wcn
	global ocn
	global tcn

	global mcnr
	global wcnr
	global ocnr
	global tcnr

	global mcw
	global wcw
	global ocw
	global tcw

	global mcfd
	global wcfd
	global ocfd
	global tcfd

	global mcc
	global wcc
	global occ
	global tcc

	global meg
	global weg
	global oeg
	global teg

	global mes
	global wes
	global oes
	global tes

	global meo
	global weo
	global oeo
	global teo

	global met
	global wet
	global oet
	global te

	global mvg
	global wvg
	global ovg
	global tvg

	global mvo
	global wvo
	global ovo
	global tvo

	global proxy

	global mvp
	global wvp
	global tvp

	global mvt
	global wvt
	global tv

	global polled_votes

	global rv
	global rv_other_reason
	global rejected_percent
	global rv_postal

	global mpp
	global wpp
	global tpp


	global evm

	global evm_total
	global evm_deducted
	global evm_valid

	global postal_total
	global postal_deducted
	global postal_valid

	global valid_votes
	global tvvp
	
	global test_votes
	global nota_votes
	global missing_votes
	global bpsa
	global tendered_votes
	global ps_no
	global ps_avg
	global repoll
	c.writerow([year,state,constituency,state_code,constituency_no,cat,mcn,wcn,ocn,tcn,mcnr,wcnr,ocnr,tcnr,mcw,wcw,ocw,tcw,mcc,wcc,occ,tcc,mcfd,wcfd,ocfd,tcfd,meg,weg,oeg,teg,meo,weo,oeo,teo,mes,wes,oes,tes,met,wet,oet,te,mvg,wvg,ovg,tvg,mvo,wvo,ovo,tvo,proxy,mvp,wvp,tvp,mvt,wvt,tv,polled_votes,rv,rv_other_reason,rejected_percent,rv_postal,mpp,wpp,tpp,evm,evm_total,evm_deducted,evm_valid,postal_total,postal_deducted,postal_valid,valid_votes,tvvp,test_votes,nota_votes,missing_votes,bpsa,tendered_votes,ps_no,ps_avg,repoll])

#Reset all variables to Null/Zero
def reset():
	global state
	global constituency
	global state_code
	global constituency_no
	global cat

	global mcn
	global wcn
	global ocn
	global tcn

	global mcnr
	global wcnr
	global ocnr
	global tcnr

	global mcw
	global wcw
	global ocw
	global tcw

	global mcfd
	global wcfd
	global ocfd
	global tcfd

	global mcc
	global wcc
	global occ
	global tcc

	global meg
	global weg
	global oeg
	global teg

	global mes
	global wes
	global oes
	global tes

	global meo
	global weo
	global oeo
	global teo

	global met
	global wet
	global oet
	global te

	global mvg
	global wvg
	global ovg
	global tvg

	global mvo
	global wvo
	global ovo
	global tvo

	global proxy

	global mvp
	global wvp
	global tvp

	global mvt
	global wvt
	global tv

	global polled_votes

	global rv
	global rv_other_reason
	global rejected_percent
	global rv_postal

	global mpp
	global wpp
	global tpp


	global evm

	global evm_total
	global evm_deducted
	global evm_valid

	global postal_total
	global postal_deducted
	global postal_valid

	global valid_votes
	global tvvp
	
	global test_votes
	global nota_votes
	global missing_votes
	global bpsa
	global tendered_votes
	global ps_no
	global ps_avg
	global repoll
	
	state=None
	constituency=None
	state_code=None
	constituency_no=None
	cat=None

	mcn=None
	wcn=None
	ocn=None
	tcn=None

	mcnr=None
	wcnr=None
	ocnr=None
	tcnr=None

	mcw=None
	wcw=None
	ocw=None
	tcw=None

	mcfd=None
	wcfd=None
	ocfd=None
	tcfd=None

	mcc=None
	wcc=None
	occ=None
	tcc=None

	meg=None
	weg=None
	oeg=None
	teg=None

	mes=None
	wes=None
	oes=None
	tes=None

	meo=None
	weo=None
	oeo=None
	teo=None

	met=None
	wet=None
	oet=None
	te=None

	mvg=None
	wvg=None
	ovg=None
	tvg=None

	mvo=None
	wvo=None
	ovo=None
	tvo=None

	proxy=None

	mvp=None
	wvp=None
	tvp=None

	mvt=None
	wvt=None
	tv=None

	polled_votes=None

	rv=None
	rv_other_reason=None
	rejected_percent=None
	rv_postal=None

	mpp=None
	wpp=None
	tpp=None


	evm=None

	evm_total=None
	evm_deducted=None
	evm_valid=None

	postal_total=None
	postal_deducted=None
	postal_valid=None

	valid_votes=None
	tvvp=None
	
	test_votes=None
	nota_votes=None
	missing_votes=None
	bpsa=None
	tendered_votes=None
	ps_no=None
	ps_avg=None
	repoll=None
	
reset()

#Process 2014 Data
for row in csv_f:
	tmp=""
	tmp2=""
	tmp3=""
	if not row:
		continue
	elif("State" in row[0]):
		for x in range(0,5):
			tmp=tmp+" "+row[x]
		tmp1=re.findall(r"[\w']+", tmp)
		n=len(tmp1)
		
		state_code=tmp1[n-1]
	elif("Constituency" in row[0]):
		constituency=""
		tmp=row[0]+row[1]
		tmp=tmp.replace(":","")
		tmp1=tmp.split()
		n=len(tmp1)
		if(tmp1[n-1]=="(SC)" or tmp1[n-1]=="(ST)"):
			for x in range(1,n-1):
				constituency=constituency+" "+tmp1[x]
			if(tmp1[n-1]=="(SC)"):
				cat="SC"
			else: cat="ST"
		else:
			for x in range(1,n):
				constituency=constituency+" "+tmp1[x]
			cat="GEN"
		tmp2=row[3]+row[4]
		tmp1=re.findall(r"[\w']+", tmp2)
		n=len(tmp1)
		constituency_no=int(tmp1[n-1])
		cat=None
	elif("NOMINATED" in row[0] and "REJECTED" not in row[0]):
		mcn=int(row[1])
		wcn=int(row[2])
		ocn=int(row[3])
		tcn=int(row[4])
	elif("NOMINATION REJECTED" in row[0]):
		mcnr=int(row[1])
		wcnr=int(row[2])
		ocnr=int(row[3])
		tcnr=int(row[4])
	elif("WITHDRAWN" in row[0]):
		mcw=int(row[1])
		wcw=int(row[2])
		ocw=int(row[3])
		tcw=int(row[4])
	elif("CONTESTED" in row[0]):
		mcc=int(row[1])
		wcc=int(row[2])
		occ=int(row[3])
		tcc=int(row[4])
	elif("FORFEITED" in row[0]):
		mcfd=int(row[1])
		wcfd=int(row[2])
		ocfd=int(row[3])
		tcfd=int(row[4])
	elif("ELECTORS" in row[0]):
		flag=0
	elif("GENERAL" in row[0] and flag==0):
		meg=int(row[1])
		weg=int(row[2])
		oeg=int(row[3])
		teg=int(row[4])
	elif("OVERSEAS" in row[0] and flag==0):
		meo=int(row[1])
		weo=int(row[2])
		oeo=int(row[3])
		teo=int(row[4])
	elif("SERVICE" in row[0]):
		mes=int(row[1])
		wes=int(row[2])
		if(row[3]!=""):
			oes=int(row[3])
		else: oes=None
		tes=int(row[4])
	elif("TOTAL" in row[0] and "VOTES" not in row[0] and "VALID" not in row[0] and flag==0):
		
		met=int(row[1])
		wet=int(row[2])
		oet=int(row[3])
		te=int(row[4])
	elif("VOTERS" in row[0]):
		flag=1
	elif("GENERAL" in row[0] and flag==1):
		mvg=int(row[1])
		wvg=int(row[2])
		ovg=int(row[3])
		tvg=int(row[4])
	elif("OVERSEAS" in row[0] and flag==1):
		mvo=int(row[1])
		wvo=int(row[2])
		ovo=int(row[3])
		tvo=int(row[4])
	elif("PROXY" in row[0]):
	
		proxy=int(row[4])
	elif(("POSTAL" in row[0] or "POSTAL*" in row[0]) and "VOTES" not in row[0]):
		
		tvp=int(row[4])
	elif("TOTAL" in row[0] and "VALID" not in row[0] and "VOTES" not in row[0] and flag==1):
		tv=int(row[4])
	elif("POLLING PERCENTAGE" in row[0]):
		tmp1=row[0].split()
		n=len(tmp1)
		tpp=float(tmp1[n-1])
	elif("Votes Rejected" in row[0]):
		rv_other_reason=int(row[4])
	elif("TOTAL VOTES POLLED ON EVM" in row[0]):
		evm_total=int(row[4])
	elif("TOTAL DEDUCTED" in row[0]):
		evm_deducted=int(row[4])
	elif("TOTAL VALID VOTES POLLED ON EVM" in row[0]):
		evm_valid=int(row[4])
	elif("POSTAL VOTES COUNTED" in row[0]):
		postal_total=int(row[4])
	elif("POSTAL VOTES DEDUCTED" in row[0]):
		postal_deducted=int(row[4])
	elif("VALID POSTAL VOTES" in row[0]):
		postal_valid=int(row[4])
	elif("TOTAL VALID VOTES POLLED" in row[0] and "EVM" not in row[0]):
		tvvp=int(row[4])
	elif("TEST VOTES" in row[0]):
		test_votes=int(row[4])
	elif("TENDERED" in row[0]):
		tendered_votes=row[4]
	elif("NOTA" in row[0]):
		nota_votes=int(row[4])
	elif("NUMBER" in row[0] and "OF" not in row[0]):
		for x in range(0,5):
			tmp=tmp+row[x]
		tmp1=re.findall(r"[\w']+", tmp)
		n=len(tmp1)
		
		ps_no=int(tmp1[1])
		ps_avg=int(tmp1[n-1])
	elif("NUMBER OF" in row[0]):
		
		if("IL" in row[4]):
			repoll=0
		else:	
			repoll=int(row[4].replace(",",""))
	elif("MARGIN" in row[0]):
		write_data()
		state=""
		constituency=""
		win_candidate=""
		run_candidate=""
f.close()
reset()

#Process 2009 Data
c = csv.writer(open("Constituency_Summary.csv", "ab"))
f=open('../2009/2009_constituency_summary_raw_data.csv')
csv_f=csv.reader(f)
year=2009
for row in csv_f:
	tmp=""
	tmp2=""
	tmp3=""
	if not row:
		continue
	elif("State" in row[1]):
		for x in range(0,5):
			tmp=tmp+" "+row[x]
		tmp1=re.findall(r"[\w']+", tmp)
		n=len(tmp1)
		state_code=tmp1[n-1]
	elif(row[1]=="" and row[2]=="" and row[3]=="" and "No" in row[4]):
		tmp1=re.findall(r"[\w']+", row[4])
		n=len(tmp1)
		constituency_no=int(tmp1[n-1])
	elif("Constituency" in row[1]):
		constituency=""
		tmp=(row[1]+row[2]).replace(":","")
		tmp1=tmp.split()
		n=len(tmp1)
		if(tmp1[n-1]=="(SC)" or tmp1[n-1]=="(ST)"):
			for x in range(2,n-1):
				constituency=constituency+" "+tmp1[x]
			if(tmp1[n-1]=="(SC)"):
				cat=None
			else: cat=None
		else:
			for x in range(1,n):
				constituency=constituency+" "+tmp1[x]
			cat=None
		
	elif("NOMINATED" in row[1] and "REJECTED" not in row[1]):
		mcn=int(row[2])
		wcn=int(row[3])
		tcn=int(row[4])
	elif("NOMINATION REJECTED" in row[1]):
		mcnr=int(row[2])
		wcnr=int(row[3])
		tcnr=int(row[4])
	elif("WITHDRAWN" in row[1]):
		mcw=int(row[2])
		wcw=int(row[3])
		tcw=int(row[4])
	elif("CONTESTED" in row[1]):
		mcc=int(row[2])
		wcc=int(row[3])
		tcc=int(row[4])
	elif("FORFEITED" in row[1]):
		mcfd=int(row[2])
		wcfd=int(row[3])
		tcfd=int(row[4])
	elif("ELECTORS" in row[1]):
		flag=0
	elif("GENERAL" in row[1] and flag==0):
		meg=int(row[2])
		weg=int(row[3])
		teg=int(row[4])
	elif("SERVICE" in row[1]):
		mes=int(row[2])
		wes=int(row[3])
		tes=int(row[4])
	elif("TOTAL" in row[1] and "VALID" not in row[1] and flag==0):
		met=int(row[2])
		wet=int(row[3])
		te=int(row[4])
	elif("VOTERS" in row[1]):
		flag=1
	elif("GENERAL" in row[1] and flag==1):
		mvg=int(row[2])
		wvg=int(row[3])
		tvg=int(row[4])
	elif("PROXY" in row[1]):
		proxy=int(row[4])
	elif(("POSTAL" in row[1] or "POSTAL*" in row[1]) and "VOTES" not in row[1]):
		
		tvp=int(row[4])
	elif("TOTAL" in row[1] and "VALID" not in row[1] and flag==1):
		tv=int(row[4])
	elif("POLLING PERCENTAGE" in row[1]):
		tmp1=row[1].split()
		n=len(tmp1)
		tpp=float(tmp1[n-1])
	elif("REJECTED VOTES" in row[1]):
		rv_postal=int(row[4])
	elif("VOTES NOT" in row[1]):
		evm=int(row[4])
	elif("VALID VOTES" in row[1]):
		tvvp=int(row[4])
	elif("TENDERED" in row[1]):
		tendered_votes=int(row[4])
	elif("NUMBER" in row[1] and "OF" not in row[1]):
		for x in range(0,5):
			tmp=tmp+row[x]
		tmp1=re.findall(r"[\w']+", tmp)
		n=len(tmp1)
		ps_no=int(tmp1[1])
		ps_avg=int(tmp1[n-1])
	elif("NUMBER OF" in row[1]):
		
		if("NIL" in row[4]):
			repoll=0
		else:	
			repoll=int(row[4].replace(",",""))
	elif("MARGIN" in row[1]):
		write_data()
		state=""
		constituency=""
		win_candidate=""
		run_candidate=""
f.close()
reset()

#Process 2004 data
c = csv.writer(open("Constituency_Summary.csv", "ab"))
f=open('../2004/2004_constituency_summary_raw_data.csv')
csv_f=csv.reader(f)
year=2004

for row in csv_f:
	tmp=""
	tmp2=""
	tmp3=""
	if not row:
		continue
	elif("STATE" in row[0]):
		state=""
		tmp=row[0]+row[1]
		tmp1=tmp.split()
		n=len(tmp1)
		for x in range(2,n):
			state=state+" "+tmp1[x]
		state_code=row[3]
	elif("CONSTITUENCY" in row[0]):
		constituency=""
		tmp=row[0]+row[1]
		tmp1=tmp.split()
		n=len(tmp1)
		if(tmp1[n-1]=="(SC)" or tmp1[n-1]=="(ST)"):
			for x in range(2,n-1):
				constituency=constituency+" "+tmp1[x]
			if(tmp1[n-1]=="(SC)"):
				cat="SC"
			else: cat="ST"
		else:
			for x in range(2,n):
				constituency=constituency+" "+tmp1[x]
			cat="GEN"
		constituency_no=int(row[3])
	elif("NOMINATED" in row[0] and "REJECTED" not in row[0]):
		mcn=int(row[1])
		wcn=int(row[2])
		tcn=int(row[3])
	elif("NOMINATION REJECTED" in row[0]):
		mcnr=int(row[1])
		wcnr=int(row[2])
		tcnr=int(row[3])
	elif("WITHDRAWN" in row[0]):
		mcw=int(row[1])
		wcw=int(row[2])
		tcw=int(row[3])
	elif("CONTESTED" in row[0]):
		mcc=int(row[1])
		wcc=int(row[2])
		tcc=int(row[3])
	elif("FORFEITED" in row[0]):
		mcfd=int(row[1])
		wcfd=int(row[2])
		tcfd=int(row[3])
	elif("ELECTORS" in row[0]):
		flag=0
	elif("GENERAL" in row[0] and flag==0):
		meg=int(row[1])
		weg=int(row[2])
		teg=int(row[3])
	elif("SERVICE" in row[0]):
		mes=int(row[1])
		wes=int(row[2])
		tes=int(row[3])
	elif("TOTAL" in row[0] and "VALID" not in row[0] and flag==0):
		met=int(row[1])
		wet=int(row[2])
		te=int(row[3])
	elif("VOTERS" in row[0]):
		flag=1
	elif("GENERAL" in row[0] and flag==1):
		mvg=int(row[1])
		wvg=int(row[2])
		tvg=int(row[3])
	elif("PROXY" in row[0]):
		proxy=int(row[3])
	elif("POSTAL" in row[0] or "POSTAL*" in row[0]):
		tvp=int(row[3])
	elif("TOTAL" in row[0] and "VALID" not in row[0] and flag==1):
		tv=int(row[3])
	elif("POLLING PERCENTAGE" in row[0]):
		mpp=float(row[1])
		wpp=float(row[2])
		tpp=float(row[3])
	elif("REJECTED VOTES" in row[0]):
		rv_postal=int(row[3])
	elif("VOTES NOT" in row[0]):
		evm=int(row[3])
	elif("VALID VOTES" in row[0]):
		tvvp=int(row[3])
	elif("TENDERED" in row[0]):
		tendered_votes=int(row[3])
	elif("NUMBER" in row[0] and "OF" not in row[0]):
		for x in range(0,4):
			tmp=tmp+row[x]
		tmp1=re.findall(r"[\w']+", tmp)
		n=len(tmp1)
		ps_no=int(tmp1[1])
		ps_avg=int(tmp1[n-1])
	elif("NUMBER OF" in row[0]):
		if("NIL" in row[3]):
			repoll=0
		else:	
			repoll=int(row[3])
	elif("rptConstituencySummary" in row[0]):
		write_data()
		state=""
		constituency=""
		win_candidate=""
		run_candidate=""
f.close()
reset()

#Process 1999 Data
c = csv.writer(open("Constituency_Summary.csv", "ab"))
f=open('../1999/1999_constituency_summary_raw_data.csv')
csv_f=csv.reader(f)
year=1999

nominated=0
for row in csv_f:
	tmp=""
	tmp2=""
	tmp3=""
	if not row:
		continue
	elif("STATE" in row[0]):
		state=""
		tmp=row[0]+row[1]
		tmp1=tmp.split()
		n=len(tmp1)
		for x in range(2,n):
			state=state+" "+tmp1[x]
		state_code=row[3]
	elif("CONSTITUENCY" in row[0]):
		constituency=""
		tmp=row[0]+row[1]
		tmp1=tmp.split()
		n=len(tmp1)
		if(tmp1[n-1]=="(SC)" or tmp1[n-1]=="(ST)"):
			for x in range(2,n-1):
				constituency=constituency+" "+tmp1[x]
			if(tmp1[n-1]=="(SC)"):
				cat="SC"
			else: cat="ST"
		else:
			for x in range(2,n):
				constituency=constituency+" "+tmp1[x]
			cat="GEN"
		constituency_no=int(row[3])
	elif("NOMINATED" in row[0]):
		mcn=int(row[1])
		wcn=int(row[2])
		tcn=int(row[3])
		nominated=1
	elif("REJECTED" in row[0] and nominated==1):
		mcnr=int(row[1])
		wcnr=int(row[2])
		tcnr=int(row[3])
		nominated=0
	elif("WITHDRAWN" in row[0]):
		mcw=int(row[1])
		wcw=int(row[2])
		tcw=int(row[3])
	elif("CONTESTED" in row[0]):
		mcc=int(row[1])
		wcc=int(row[2])
		tcc=int(row[3])
	elif("FORFEITED" in row[0]):
		mcfd=int(row[1])
		wcfd=int(row[2])
		tcfd=int(row[3])
	elif("ELECTORS" in row[0] and "VOTED" not in row[0]):
		flag=0
	elif("GENERAL" in row[0] and flag==0):
		meg=int(row[1])
		weg=int(row[2])
		teg=int(row[3])
	elif("SERVICE" in row[0]):
		mes=int(row[1])
		wes=int(row[2])
		tes=int(row[3])
	elif("TOTAL" in row[0] and flag==0):
		met=int(row[1])
		wet=int(row[2])
		te=int(row[3])
	elif("VOTED" in row[0]):
		flag=1
	elif("GENERAL" in row[0] and flag==1):
		mvg=int(row[1])
		wvg=int(row[2])
		tvg=int(row[3])
	
	elif("POSTAL" in row[0] or "POSTAL*" in row[0]):
		mvp=int(row[1])
		wvp=int(row[2])
		tvp=int(row[3])
	elif("TOTAL" in row[0] and flag==1):
		mvt=int(row[1])
		wvt=int(row[2])
		tv=int(row[3])
	
	elif("POLLED" in row[0]):
		polled_votes=int(row[1])
		tmp1=re.findall(r"[\w']+", row[2])
		n=len(tmp1)
		x=tmp1[0]+"."+tmp1[1]
		tpp=float(x)
	elif("VALID" in row[0]):
		valid_votes=int(row[1])
	elif("REJECTED" in row[0] and nominated==0):
		rv=int(row[1])
		tmp1=re.findall(r"[\w']+", row[2])
		n=len(tmp1)
		x=tmp1[0]+"."+tmp1[1]
		rejected_percent=float(x)
	elif("MISSING" in row[0]):
		missing_votes=int(row[1])
	
	elif("TENDERED" in row[0]):
		tendered_votes=int(row[1])
	elif("NUMBER" in row[0]):
		for x in range(0,4):
			tmp=tmp+" "+row[x]
		tmp1=re.findall(r"[\w']+", tmp)
		n=len(tmp1)
		ps_no=int(tmp1[1])
		ps_avg=int(tmp1[n-1])

	elif("rptConstituencySummary" in row[0]):
		write_data()
		state=""
		constituency=""
f.close()
reset()

#Process 1998 Total
c = csv.writer(open("Constituency_Summary.csv", "ab"))
f=open('../1998/1998_constituency_summary_raw_data.csv')
csv_f=csv.reader(f)
nominated=0

year=1998
for row in csv_f:
	tmp=""
	tmp2=""
	tmp3=""
	if not row:
		continue
	elif("STATE" in row[0]):
		state=""
		tmp=row[0]+row[1]
		tmp1=tmp.split()
		n=len(tmp1)
		for x in range(2,n):
			state=state+" "+tmp1[x]
		state_code=row[3]
	elif("CONSTITUENCY" in row[0]):
		constituency=""
		tmp=row[0]+row[1]
		tmp1=tmp.split()
		n=len(tmp1)
		if(tmp1[n-1]=="(SC)" or tmp1[n-1]=="(ST)"):
			for x in range(2,n-1):
				constituency=constituency+" "+tmp1[x]
			if(tmp1[n-1]=="(SC)"):
				cat="SC"
			else: cat="ST"
		else:
			for x in range(2,n):
				constituency=constituency+" "+tmp1[x]
			cat="GEN"
		constituency_no=int(row[3])
	elif("NOMINATED" in row[0]):
		mcn=int(row[1])
		wcn=int(row[2])
		tcn=int(row[3])
		nominated=1
	elif("REJECTED" in row[0] and nominated==1):
		mcnr=int(row[1])
		wcnr=int(row[2])
		tcnr=int(row[3])
		nominated=0
	elif("WITHDRAWN" in row[0]):
		mcw=int(row[1])
		wcw=int(row[2])
		tcw=int(row[3])
	elif("CONTESTED" in row[0]):
		mcc=int(row[1])
		wcc=int(row[2])
		tcc=int(row[3])
	elif("FORFEITED" in row[0]):
		mcfd=int(row[1])
		wcfd=int(row[2])
		tcfd=int(row[3])
	elif("ELECTORS" in row[0] and "VOTED" not in row[0]):
		flag=0
	elif("GENERAL" in row[0] and flag==0):
		meg=int(row[1])
		weg=int(row[2])
		teg=int(row[3])
	elif("SERVICE" in row[0]):
		mes=int(row[1])
		wes=int(row[2])
		tes=int(row[3])
	elif("TOTAL" in row[0] and flag==0):
		met=int(row[1])
		wet=int(row[2])
		te=int(row[3])
	elif("VOTED" in row[0]):
		flag=1
	elif("GENERAL" in row[0] and flag==1):
		
		if(row[1]!=""):
			mvg=int(row[1])
		else: mvg=None
		if(row[1]!=""):
			wvg=int(row[2])
		else: 
			wvg=None
			
		tvg=int(row[3])
	
	elif("POSTAL" in row[0] or "POSTAL*" in row[0]):
		if(row[1]!=""):
			mvp=int(row[1])
		else: mvp=None
		if(row[1]!=""):
			wvp=int(row[2])
		else: 
			wvp=None
		tvp=int(row[3])
	elif("TOTAL" in row[0] and flag==1):
		if(row[1]!=""):
			mvt=int(row[1])
		else: mvt=None
		if(row[1]!=""):
			wvt=int(row[2])
		else: 
			wvt=None
		tv=int(row[3])
	
	elif("POLLED" in row[0]):
		polled_votes=int(row[1])
		tmp1=re.findall(r"[\w']+", row[2])
		n=len(tmp1)
		x=tmp1[0]+"."+tmp1[1]
		tpp=float(x)
	elif("VALID" in row[0]):
		valid_votes=int(row[1])
	elif("REJECTED" in row[0] and nominated==0):
		rv=int(row[1])
		tmp1=re.findall(r"[\w']+", row[2])
		n=len(tmp1)
		x=tmp1[0]+"."+tmp1[1]
		rejected_percent=float(x)
	elif("MISSING" in row[0]):
		missing_votes=int(row[1])
	
	elif("TENDERED" in row[0]):
		tendered_votes=int(row[1])
	elif("NUMBER" in row[0]):
		for x in range(0,4):
			tmp=tmp+" "+row[x]
		tmp1=re.findall(r"[\w']+", tmp)
		n=len(tmp1)
		ps_no=int(tmp1[1])
		ps_avg=int(tmp1[n-1])

	elif("rptConstituencySummary" in row[0]):
		write_data()
		state=""
		constituency=""
f.close()
reset()

#Process 1996 Data
c = csv.writer(open("Constituency_Summary.csv", "ab"))
f=open('../1996/1996_constituency_summary_raw_data.csv')
csv_f=csv.reader(f)

year=1996
nominated=0
for row in csv_f:
	tmp=""
	tmp2=""
	tmp3=""
	if not row:
		continue
	elif("STATE" in row[0]):
		state=""
		tmp=row[0]+row[1]
		tmp1=tmp.split()
		n=len(tmp1)
		for x in range(2,n):
			state=state+" "+tmp1[x]
		state_code=row[3]
	elif("CONSTITUENCY" in row[0]):
		constituency=""
		tmp=row[0]+row[1]
		tmp1=tmp.split()
		n=len(tmp1)
		if(tmp1[n-1]=="(SC)" or tmp1[n-1]=="(ST)"):
			for x in range(2,n-1):
				constituency=constituency+" "+tmp1[x]
			if(tmp1[n-1]=="(SC)"):
				cat="SC"
			else: cat="ST"
		else:
			for x in range(2,n):
				constituency=constituency+" "+tmp1[x]
			cat="GEN"
		constituency_no=int(row[3])
	elif("NOMINATED" in row[0]):
		mcn=int(row[1])
		wcn=int(row[2])
		tcn=int(row[3])
		nominated=1
	elif("REJECTED" in row[0] and nominated==1):
		mcnr=int(row[1])
		wcnr=int(row[2])
		tcnr=int(row[3])
		nominated=0
	elif("WITHDRAWN" in row[0]):
		mcw=int(row[1])
		wcw=int(row[2])
		tcw=int(row[3])
	elif("CONTESTED" in row[0]):
		mcc=int(row[1])
		wcc=int(row[2])
		tcc=int(row[3])
	elif("FORFEITED" in row[0]):
		mcfd=int(row[1])
		wcfd=int(row[2])
		tcfd=int(row[3])
	elif("ELECTORS" in row[0] and "VOTED" not in row[0]):
		flag=0
	elif("GENERAL" in row[0] and flag==0):
		meg=int(row[1])
		weg=int(row[2])
		teg=int(row[3])
	elif("SERVICE" in row[0]):
		mes=int(row[1])
		wes=int(row[2])
		tes=int(row[3])
	elif("TOTAL" in row[0] and flag==0):
		met=int(row[1])
		wet=int(row[2])
		te=int(row[3])
	elif("VOTED" in row[0]):
		flag=1
	elif("GENERAL" in row[0] and flag==1):
		
		if(row[1]!=""):
			mvg=int(row[1])
		else: mvg=None
		if(row[1]!=""):
			wvg=int(row[2])
		else: 
			wvg=None
			
		tvg=int(row[3])
	
	elif("POSTAL" in row[0] or "POSTAL*" in row[0]):
		if(row[1]!=""):
			mvp=int(row[1])
		else: mvp=None
		if(row[1]!=""):
			wvp=int(row[2])
		else: 
			wvp=None
		tvp=int(row[3])
	elif("TOTAL" in row[0] and flag==1):
		if(row[1]!=""):
			mvt=int(row[1])
		else: mvt=None
		if(row[1]!=""):
			wvt=int(row[2])
		else: 
			wvt=None
		tv=int(row[3])
	
	elif("POLLED" in row[0]):
		polled_votes=int(row[1])
		tmp1=re.findall(r"[\w']+", row[2])
		n=len(tmp1)
		x=tmp1[0]+"."+tmp1[1]
		tpp=float(x)
	elif("VALID" in row[0]):
		valid_votes=int(row[1])
	elif("REJECTED" in row[0] and nominated==0):
		rv=int(row[1])
		tmp1=re.findall(r"[\w']+", row[2])
		n=len(tmp1)
		x=tmp1[0]+"."+tmp1[1]
		rejected_percent=float(x)
	elif("MISSING" in row[0]):
		missing_votes=int(row[1])
	
	elif("TENDERED" in row[0]):
		tendered_votes=int(row[1])
	elif("NUMBER" in row[0]):
		for x in range(0,4):
			tmp=tmp+" "+row[x]
		tmp1=re.findall(r"[\w']+", tmp)
		n=len(tmp1)
		ps_no=int(tmp1[1])
		ps_avg=int(tmp1[n-1])

	elif("rptConstituencySummary" in row[0]):
		write_data()
		state=""
		constituency=""
f.close()
reset()

year=1992
#Process 1991 Data
c = csv.writer(open("Constituency_Summary.csv", "ab"))
f=open('../1992/1992_constituency_summary_raw_data.csv')
csv_f=csv.reader(f)

nominated=0
for row in csv_f:
	tmp=""
	tmp2=""
	tmp3=""
	if not row:
		continue
	elif("STATE" in row[0]):
		state=""
		tmp=row[0]+row[1]
		tmp1=tmp.split()
		n=len(tmp1)
		for x in range(2,n):
			state=state+" "+tmp1[x]
		state_code=row[3]
	elif("CONSTITUENCY" in row[0]):
		constituency=""
		tmp=row[0]+row[1]
		tmp1=tmp.split()
		n=len(tmp1)
		if(tmp1[n-1]=="(SC)" or tmp1[n-1]=="(ST)"):
			for x in range(2,n-1):
				constituency=constituency+" "+tmp1[x]
			if(tmp1[n-1]=="(SC)"):
				cat="SC"
			else: cat="ST"
		else:
			for x in range(2,n):
				constituency=constituency+" "+tmp1[x]
			cat="GEN"
		constituency_no=int(row[3])
	elif("NOMINATED" in row[0]):
		
		nominated=1
	elif("REJECTED" in row[0] and nominated==1):
		
		nominated=0
	elif("WITHDRAWN" in row[0]):
		continue
	elif("CONTESTED" in row[0]):
		mcc=int(row[1])
		wcc=int(row[2])
		tcc=int(row[3])
	elif("FORFEITED" in row[0]):
		mcfd=int(row[1])
		wcfd=int(row[2])
		tcfd=int(row[3])
	elif("ELECTORS" in row[0] and "VOTED" not in row[0]):
		flag=0
	elif("GENERAL" in row[0] and flag==0):
		meg=int(row[1])
		weg=int(row[2])
		teg=int(row[3])
	elif("SERVICE" in row[0]):
		mes=int(row[1])
		wes=int(row[2])
		tes=int(row[3])
	elif("TOTAL" in row[0] and flag==0):
		met=int(row[1])
		wet=int(row[2])
		te=int(row[3])
	elif("VOTED" in row[0]):
		flag=1
	elif("GENERAL" in row[0] and flag==1):
		
		if(row[1]!=""):
			mvg=int(row[1])
		else: mvg=None
		if(row[1]!=""):
			wvg=int(row[2])
		else: 
			wvg=None
			
		tvg=int(row[3])
	
	elif("POSTAL" in row[0] or "POSTAL*" in row[0]):
		if(row[1]!=""):
			mvp=int(row[1])
		else: mvp=None
		if(row[1]!=""):
			wvp=int(row[2])
		else: 
			wvp=None
		tvp=int(row[3])
	elif("TOTAL" in row[0] and flag==1):
		if(row[1]!=""):
			mvt=int(row[1])
		else: mvt=None
		if(row[1]!=""):
			wvt=int(row[2])
		else: 
			wvt=None
		tv=int(row[3])
	
	elif("POLLED" in row[0]):
		polled_votes=int(row[1])
		tmp1=re.findall(r"[\w']+", row[2])
		n=len(tmp1)
		x=tmp1[0]+"."+tmp1[1]
		tpp=float(x)
	elif("VALID" in row[0]):
		valid_votes=int(row[1])
	elif("REJECTED" in row[0] and nominated==0):
		
		rv=int(row[1])
		tmp1=re.findall(r"[\w']+", row[2])
		n=len(tmp1)
		x=tmp1[0]+"."+tmp1[1]
		rejected_percent=float(x)
	elif("MISSING" in row[0]):
		if(row[1]!=""):
			missing_votes=int(row[1])
		else: missing_votes=None
	elif("BALLOT" in row[0]):
		bpsa=int(row[1])
	elif("TENDERED" in row[0]):
		tendered_votes=int(row[1])
	elif("NUMBER" in row[0]):
		for x in range(0,4):
			tmp=tmp+" "+row[x]
		tmp1=re.findall(r"[\w']+", tmp)
		n=len(tmp1)
		ps_no=int(tmp1[1])
		ps_avg=int(tmp1[n-1])

	elif("rptConstituencySummary" in row[0]):
		write_data()
		state=""
		constituency=""
f.close()
reset()

#Process 1991 Data
year=1991
nominated=0

c = csv.writer(open("Constituency_Summary.csv", "ab"))
f=open('../1991/1991_constituency_summary_raw_data.csv')
csv_f=csv.reader(f)
for row in csv_f:
	tmp=""
	tmp2=""
	tmp3=""
	if not row:
		continue
	elif("STATE" in row[0]):
		state=""
		tmp=row[0]+row[1]
		tmp1=tmp.split()
		n=len(tmp1)
		for x in range(2,n):
			state=state+" "+tmp1[x]
		state_code=row[3]
	elif("CONSTITUENCY" in row[0]):
		constituency=""
		tmp=row[0]+row[1]
		tmp1=tmp.split()
		n=len(tmp1)
		if(tmp1[n-1]=="(SC)" or tmp1[n-1]=="(ST)"):
			for x in range(2,n-1):
				constituency=constituency+" "+tmp1[x]
			if(tmp1[n-1]=="(SC)"):
				cat="SC"
			else: cat="ST"
		else:
			for x in range(2,n):
				constituency=constituency+" "+tmp1[x]
			cat="GEN"
		constituency_no=int(row[3])
	elif("NOMINATED" in row[0]):
		
		nominated=1
	elif("REJECTED" in row[0] and nominated==1):
		
		nominated=0
	elif("WITHDRAWN" in row[0]):
		continue
	elif("CONTESTED" in row[0]):
		mcc=int(row[1])
		wcc=int(row[2])
		tcc=int(row[3])
	elif("FORFEITED" in row[0]):
		mcfd=int(row[1])
		wcfd=int(row[2])
		tcfd=int(row[3])
	elif("ELECTORS" in row[0] and "VOTED" not in row[0]):
		flag=0
	elif("GENERAL" in row[0] and flag==0):
		meg=int(row[1])
		weg=int(row[2])
		teg=int(row[3])
	elif("SERVICE" in row[0]):
		mes=int(row[1])
		wes=int(row[2])
		tes=int(row[3])
	elif("TOTAL" in row[0] and flag==0):
		met=int(row[1])
		wet=int(row[2])
		te=int(row[3])
	elif("VOTED" in row[0]):
		flag=1
	elif("GENERAL" in row[0] and flag==1):
		
		if(row[1]!=""):
			mvg=int(row[1])
		else: mvg=None
		if(row[1]!=""):
			wvg=int(row[2])
		else: 
			wvg=None
			
		tvg=int(row[3])
	
	elif("POSTAL" in row[0] or "POSTAL*" in row[0]):
		if(row[1]!=""):
			mvp=int(row[1])
		else: mvp=None
		if(row[1]!=""):
			wvp=int(row[2])
		else: 
			wvp=None
		tvp=int(row[3])
	elif("TOTAL" in row[0] and flag==1):
		if(row[1]!=""):
			mvt=int(row[1])
		else: mvt=None
		if(row[1]!=""):
			wvt=int(row[2])
		else: 
			wvt=None
		tv=int(row[3])
	
	elif("POLLED" in row[0]):
		polled_votes=int(row[1])
		tmp1=re.findall(r"[\w']+", row[2])
		n=len(tmp1)
		x=tmp1[0]+"."+tmp1[1]
		tpp=float(x)
	elif("VALID" in row[0]):
		valid_votes=int(row[1])
	elif("REJECTED" in row[0] and nominated==0):
		
		rv=int(row[1])
		tmp1=re.findall(r"[\w']+", row[2])
		n=len(tmp1)
		x=tmp1[0]+"."+tmp1[1]
		rejected_percent=float(x)
	elif("MISSING" in row[0]):
		if(row[1]!=""):
			missing_votes=int(row[1])
		else: missing_votes=None
	elif("BALLOT" in row[0]):
		bpsa=int(row[1])
	elif("TENDERED" in row[0]):
		tendered_votes=int(row[1])
	elif("NUMBER" in row[0]):
		for x in range(0,4):
			tmp=tmp+" "+row[x]
		tmp1=re.findall(r"[\w']+", tmp)
		n=len(tmp1)
		ps_no=int(tmp1[1])
		ps_avg=int(tmp1[n-1])

	elif("rptConstituencySummary" in row[0]):
		write_data()
		state=""
		constituency=""
f.close()
reset()

#Process 1989 Data
year=1989
nominated=0

c = csv.writer(open("Constituency_Summary.csv", "ab"))
f=open('../1989/1989_constituency_summary_raw_data.csv')
csv_f=csv.reader(f)
for row in csv_f:
	tmp=""
	tmp2=""
	tmp3=""
	if not row:
		continue
	elif("STATE" in row[0]):
		state=""
		tmp=row[0]+row[1]
		tmp1=tmp.split()
		n=len(tmp1)
		for x in range(2,n):
			state=state+" "+tmp1[x]
		state_code=row[3]
	elif("CONSTITUENCY" in row[0]):
		constituency=""
		tmp=row[0]+row[1]
		tmp1=tmp.split()
		n=len(tmp1)
		if(tmp1[n-1]=="(SC)" or tmp1[n-1]=="(ST)"):
			for x in range(2,n-1):
				constituency=constituency+" "+tmp1[x]
			if(tmp1[n-1]=="(SC)"):
				cat="SC"
			else: cat="ST"
		else:
			for x in range(2,n):
				constituency=constituency+" "+tmp1[x]
			cat="GEN"
		constituency_no=int(row[3])
	elif("NOMINATED" in row[0]):
		
		nominated=1
	elif("REJECTED" in row[0] and nominated==1):
		
		nominated=0
	elif("WITHDRAWN" in row[0]):
		continue
	elif("CONTESTED" in row[0]):
		continue
		mcc=int(row[1])
		wcc=int(row[2])
		tcc=int(row[3])
	elif("FORFEITED" in row[0]):
		continue
		mcfd=int(row[1])
		wcfd=int(row[2])
		tcfd=int(row[3])
	elif("ELECTORS" in row[0] and "VOTED" not in row[0]):
		flag=0
	elif("GENERAL" in row[0] and flag==0):
		meg=int(row[1])
		weg=int(row[2])
		teg=int(row[3])
	elif("SERVICE" in row[0]):
		mes=int(row[1])
		wes=int(row[2])
		tes=int(row[3])
	elif("TOTAL" in row[0] and flag==0):
		met=int(row[1])
		wet=int(row[2])
		te=int(row[3])
	elif("VOTED" in row[0]):
		flag=1
	elif("GENERAL" in row[0] and flag==1):
		
		if(row[1]!=""):
			mvg=int(row[1])
		else: mvg=None
		if(row[1]!=""):
			wvg=int(row[2])
		else: 
			wvg=None
		if(row[3]!=""):
			tvg=int(row[3])
		else:
			tvg=None
	elif("POSTAL" in row[0] or "POSTAL*" in row[0]):
		if(row[1]!=""):
			mvp=int(row[1])
		else: mvp=None
		if(row[1]!=""):
			wvp=int(row[2])
		else: 
			wvp=None
		if(row[3]!=""):
			tvp=int(row[3])
		else: tvp=None
	elif("TOTAL" in row[0] and flag==1):
		if(row[1]!=""):
			mvt=int(row[1])
		else: mvt=None
		if(row[1]!=""):
			wvt=int(row[2])
		else: 
			wvt=None
		if(row[3]!=""): tv=int(row[3])
		else: tv=None
	elif("POLLED" in row[0]):
		if(row[1]!=""):
			polled_votes=int(row[1])
			tmp1=re.findall(r"[\w']+", row[2])
			n=len(tmp1)
			x=tmp1[0]+"."+tmp1[1]
			tpp=float(x)
		else:
			polled_votes=None
			tpp=None
	elif("VALID" in row[0]):
		if(row[1]!=""):
			valid_votes=int(row[1])
		else: valid_votes=None
	elif("REJECTED" in row[0] and nominated==0):
		if(row[1]!=""):
			rv=int(row[1])
			tmp1=re.findall(r"[\w']+", row[2])
			n=len(tmp1)
			x=tmp1[0]+"."+tmp1[1]
			rejected_percent=float(x)
		else:
			rejected_percent=None
			rv=None
	elif("MISSING" in row[0]):
		if(row[1]!=""):
			missing_votes=int(row[1])
		else: missing_votes=None
	
	elif("TENDERED" in row[0]):
		if(row[1]!=""):
			tendered_votes=int(row[1])
		else: tendered_votes=None
	elif("NUMBER" in row[0]):
		for x in range(0,4):
			tmp=tmp+" "+row[x]
		tmp1=re.findall(r"[\w']+", tmp)
		n=len(tmp1)
		ps_no=int(tmp1[1])
		ps_avg=int(tmp1[n-1])

	elif("rptConstituencySummary" in row[0]):
		write_data()
		state=""
		constituency=""
f.close()

reset()

#Process 1985 Data
c = csv.writer(open("Constituency_Summary.csv", "ab"))
f=open('../1985/1985_constituency_summary_raw_data.csv')
csv_f=csv.reader(f)
year=1985
nominated=0

for row in csv_f:
	tmp=""
	tmp2=""
	tmp3=""
	if not row:
		continue
	elif("STATE" in row[0]):
		state=""
		tmp=row[0]+row[1]
		tmp1=tmp.split()
		n=len(tmp1)
		for x in range(2,n):
			state=state+" "+tmp1[x]
		state_code=row[3]
	elif("CONSTITUENCY" in row[0]):
		constituency=""
		tmp=row[0]+row[1]
		tmp1=tmp.split()
		n=len(tmp1)
		if(tmp1[n-1]=="(SC)" or tmp1[n-1]=="(ST)"):
			for x in range(2,n-1):
				constituency=constituency+" "+tmp1[x]
			if(tmp1[n-1]=="(SC)"):
				cat="SC"
			else: cat="ST"
		else:
			for x in range(2,n):
				constituency=constituency+" "+tmp1[x]
			cat="GEN"
		constituency_no=int(row[3])
	elif("NOMINATED" in row[0]):
		
		nominated=1
	elif("REJECTED" in row[0] and nominated==1):
		
		nominated=0
	elif("WITHDRAWN" in row[0]):
		continue
	elif("CONTESTED" in row[0]):
		
		mcc=int(row[1])
		wcc=int(row[2])
		tcc=int(row[3])
	elif("FORFEITED" in row[0]):
		
		mcfd=int(row[1])
		wcfd=int(row[2])
		tcfd=int(row[3])
	elif("ELECTORS" in row[0] and "VOTED" not in row[0]):
		flag=0
	elif("GENERAL" in row[0] and flag==0):
		meg=int(row[1])
		weg=int(row[2])
		teg=int(row[3])
	elif("SERVICE" in row[0]):
		mes=int(row[1])
		wes=int(row[2])
		tes=int(row[3])
	elif("TOTAL" in row[0] and flag==0):
		met=int(row[1])
		wet=int(row[2])
		te=int(row[3])
	elif("VOTED" in row[0]):
		flag=1
	elif("GENERAL" in row[0] and flag==1):
		
		if(row[1]!=""):
			mvg=int(row[1])
		else: mvg=None
		if(row[1]!=""):
			wvg=int(row[2])
		else: 
			wvg=None
		if(row[3]!=""):
			tvg=int(row[3])
		else:
			tvg=None
	elif("POSTAL" in row[0] or "POSTAL*" in row[0]):
		if(row[1]!=""):
			mvp=int(row[1])
		else: mvp=None
		if(row[1]!=""):
			wvp=int(row[2])
		else: 
			wvp=None
		if(row[3]!=""):
			tvp=int(row[3])
		else: tvp=None
	elif("TOTAL" in row[0] and flag==1):
		if(row[1]!=""):
			mvt=int(row[1])
		else: mvt=None
		if(row[1]!=""):
			wvt=int(row[2])
		else: 
			wvt=None
		if(row[3]!=""): tv=int(row[3])
		else: tv=None
	elif("POLLED" in row[0]):
		if(row[1]!=""):
			polled_votes=int(row[1])
			tmp1=re.findall(r"[\w']+", row[2])
			n=len(tmp1)
			x=tmp1[0]+"."+tmp1[1]
			tpp=float(x)
		else:
			polled_votes=None
			tpp=None
	elif("VALID" in row[0]):
		if(row[1]!=""):
			valid_votes=int(row[1])
		else: valid_votes=None
	elif("REJECTED" in row[0] and nominated==0):
		if(row[1]!=""):
			rv=int(row[1])
			tmp1=re.findall(r"[\w']+", row[2])
			n=len(tmp1)
			x=tmp1[0]+"."+tmp1[1]
			rejected_percent=float(x)
		else:
			rejected_percent=None
			rejected_votes=None
	elif("MISSING" in row[0]):
		if(row[1]!=""):
			missing_votes=int(row[1])
		else: missing_votes=None
	
	elif("TENDERED" in row[0]):
		if(row[1]!=""):
			tendered_votes=int(row[1])
		else: tendered_votes=None
	elif("NUMBER" in row[0]):
		for x in range(0,4):
			tmp=tmp+" "+row[x]
		tmp1=re.findall(r"[\w']+", tmp)
		n=len(tmp1)
		ps_no=int(tmp1[1])
		ps_avg=int(tmp1[n-1])

	elif("rptConstituencySummary" in row[0]):
		write_data()
		state=""
		constituency=""
f.close()
reset()

#Process 1984 Data
year=1984
c = csv.writer(open("Constituency_Summary.csv", "ab"))
f=open('../1984/1984_constituency_summary_raw_data.csv')
csv_f=csv.reader(f)
nominated=0

for row in csv_f:
	tmp=""
	tmp2=""
	tmp3=""
	if not row:
		continue
	elif("STATE" in row[0]):
		state=""
		tmp=row[0]+row[1]
		tmp1=tmp.split()
		n=len(tmp1)
		for x in range(2,n):
			state=state+" "+tmp1[x]
		state_code=row[3]
	elif("CONSTITUENCY" in row[0]):
		constituency=""
		tmp=row[0]+row[1]
		tmp1=tmp.split()
		n=len(tmp1)
		if(tmp1[n-1]=="(SC)" or tmp1[n-1]=="(ST)"):
			for x in range(2,n-1):
				constituency=constituency+" "+tmp1[x]
			if(tmp1[n-1]=="(SC)"):
				cat="SC"
			else: cat="ST"
		else:
			for x in range(2,n):
				constituency=constituency+" "+tmp1[x]
			cat="GEN"
		constituency_no=int(row[3])
	elif("NOMINATED" in row[0]):
		
		nominated=1
	elif("REJECTED" in row[0] and nominated==1):
		
		nominated=0
	elif("WITHDRAWN" in row[0]):
		continue
	elif("CONTESTED" in row[0]):
		
		mcc=int(row[1])
		wcc=int(row[2])
		tcc=int(row[3])
	elif("FORFEITED" in row[0]):
		
		mcfd=int(row[1])
		wcfd=int(row[2])
		tcfd=int(row[3])
	elif("ELECTORS" in row[0] and "VOTED" not in row[0]):
		flag=0
	elif("GENERAL" in row[0] and flag==0):
		meg=int(row[1])
		weg=int(row[2])
		teg=int(row[3])
	elif("SERVICE" in row[0]):
		mes=int(row[1])
		wes=int(row[2])
		tes=int(row[3])
	elif("TOTAL" in row[0] and flag==0):
		met=int(row[1])
		wet=int(row[2])
		te=int(row[3])
	elif("VOTED" in row[0]):
		flag=1
	elif("GENERAL" in row[0] and flag==1):
		
		if(row[1]!=""):
			mvg=int(row[1])
		else: mvg=None
		if(row[1]!=""):
			wvg=int(row[2])
		else: 
			wvg=None
		if(row[3]!=""):
			tvg=int(row[3])
		else:
			tvg=None
	elif("POSTAL" in row[0] or "POSTAL*" in row[0]):
		if(row[1]!=""):
			mvp=int(row[1])
		else: mvp=None
		if(row[1]!=""):
			wvp=int(row[2])
		else: 
			wvp=None
		if(row[3]!=""):
			tvp=int(row[3])
		else: tvp=None
	elif("TOTAL" in row[0] and flag==1):
		if(row[1]!=""):
			mvt=int(row[1])
		else: mvt=None
		if(row[1]!=""):
			wvt=int(row[2])
		else: 
			wvt=None
		if(row[3]!=""): tv=int(row[3])
		else: tv=None
	elif("POLLED" in row[0]):
		if(row[1]!=""):
			polled_votes=int(row[1])
			tmp1=re.findall(r"[\w']+", row[2])
			n=len(tmp1)
			x=tmp1[0]+"."+tmp1[1]
			tpp=float(x)
		else:
			polled_votes=None
			tpp=None
	elif("VALID" in row[0]):
		if(row[1]!=""):
			valid_votes=int(row[1])
		else: valid_votes=None
	elif("REJECTED" in row[0] and nominated==0):
		if(row[1]!=""):
			rv=int(row[1])
			tmp1=re.findall(r"[\w']+", row[2])
			n=len(tmp1)
			x=tmp1[0]+"."+tmp1[1]
			rejected_percent=float(x)
		else:
			rejected_percent=None
			rejected_votes=None
	elif("MISSING" in row[0]):
		if(row[1]!=""):
			missing_votes=int(row[1])
		else: missing_votes=None
	
	elif("TENDERED" in row[0]):
		if(row[1]!=""):
			tendered_votes=int(row[1])
		else: tendered_votes=None
	elif("NUMBER" in row[0]):
		for x in range(0,4):
			tmp=tmp+" "+row[x]
		tmp1=re.findall(r"[\w']+", tmp)
		n=len(tmp1)
		ps_no=int(tmp1[1])
		ps_avg=int(tmp1[n-1])

	elif("rptConstituencySummary" in row[0]):
		write_data()
		state=""
		constituency=""
f.close()

reset()

#Process 1980 Data
year=1980
c = csv.writer(open("Constituency_Summary.csv", "ab"))
f=open('../1980/1980_constituency_summary_raw_data.csv')
csv_f=csv.reader(f)
nominated=0
for row in csv_f:
	tmp=""
	tmp2=""
	tmp3=""
	if not row:
		continue
	elif("STATE" in row[0]):
		state=""
		tmp=row[0]+row[1]
		tmp1=tmp.split()
		n=len(tmp1)
		for x in range(2,n):
			state=state+" "+tmp1[x]
		state_code=row[3]
	elif("CONSTITUENCY" in row[0]):
		constituency=""
		tmp=row[0]+row[1]
		tmp1=tmp.split()
		n=len(tmp1)
		if(tmp1[n-1]=="(SC)" or tmp1[n-1]=="(ST)"):
			for x in range(2,n-1):
				constituency=constituency+" "+tmp1[x]
			if(tmp1[n-1]=="(SC)"):
				cat="SC"
			else: cat="ST"
		else:
			for x in range(2,n):
				constituency=constituency+" "+tmp1[x]
			cat="GEN"
		constituency_no=int(row[3])
	elif("NOMINATED" in row[0]):
		
		nominated=1
	elif("REJECTED" in row[0] and nominated==1):
		
		nominated=0
	elif("WITHDRAWN" in row[0]):
		continue
	elif("CONTESTED" in row[0]):
		
		mcc=int(row[1])
		wcc=int(row[2])
		tcc=int(row[3])
	elif("FORFEITED" in row[0]):
		
		mcfd=int(row[1])
		wcfd=int(row[2])
		tcfd=int(row[3])
	elif("ELECTORS" in row[0] and "VOTED" not in row[0]):
		flag=0
	elif("GENERAL" in row[0] and flag==0):
		meg=int(row[1])
		weg=int(row[2])
		teg=int(row[3])
	elif("SERVICE" in row[0]):
		mes=int(row[1])
		wes=int(row[2])
		tes=int(row[3])
	elif("TOTAL" in row[0] and flag==0):
		met=int(row[1])
		wet=int(row[2])
		te=int(row[3])
	elif("VOTED" in row[0]):
		flag=1
	elif("GENERAL" in row[0] and flag==1):
		
		if(row[1]!=""):
			mvg=int(row[1])
		else: mvg=None
		if(row[1]!=""):
			wvg=int(row[2])
		else: 
			wvg=None
		if(row[3]!=""):
			tvg=int(row[3])
		else:
			tvg=None
	elif("POSTAL" in row[0] or "POSTAL*" in row[0]):
		if(row[1]!=""):
			mvp=int(row[1])
		else: mvp=None
		if(row[1]!=""):
			wvp=int(row[2])
		else: 
			wvp=None
		if(row[3]!=""):
			tvp=int(row[3])
		else: tvp=None
	elif("TOTAL" in row[0] and flag==1):
		if(row[1]!=""):
			mvt=int(row[1])
		else: mvt=None
		if(row[1]!=""):
			wvt=int(row[2])
		else: 
			wvt=None
		if(row[3]!=""): tv=int(row[3])
		else: tv=None
	elif("POLLED" in row[0]):
		if(row[1]!=""):
			polled_votes=int(row[1])
			tmp1=re.findall(r"[\w']+", row[2])
			n=len(tmp1)
			x=tmp1[0]+"."+tmp1[1]
			tpp=float(x)
		else:
			polled_votes=None
			tpp=None
	elif("VALID" in row[0]):
		if(row[1]!=""):
			valid_votes=int(row[1])
		else: valid_votes=None
	elif("REJECTED" in row[0] and nominated==0):
		if(row[1]!=""):
			rv=int(row[1])
			tmp1=re.findall(r"[\w']+", row[2])
			n=len(tmp1)
			x=tmp1[0]+"."+tmp1[1]
			rejected_percent=float(x)
		else:
			rejected_percent=None
			rv=None
	elif("MISSING" in row[0]):
		if(row[1]!=""):
			missing_votes=int(row[1])
		else: missing_votes=None
	
	elif("TENDERED" in row[0]):
		if(row[1]!=""):
			tendered_votes=int(row[1])
		else: tendered_votes=None
	elif("NUMBER" in row[0]):
		for x in range(0,4):
			tmp=tmp+" "+row[x]
		tmp1=re.findall(r"[\w']+", tmp)
		n=len(tmp1)
		ps_no=int(tmp1[1])
		ps_avg=int(tmp1[n-1])

	elif("rptConstituencySummary" in row[0]):
		write_data()
		state=""
		constituency=""
f.close()

reset()

#Process 1977 Data
year=1977
c = csv.writer(open("Constituency_Summary.csv", "ab"))
f=open('../1977/1977_constituency_summary_raw_data.csv')
csv_f=csv.reader(f)
nominated=0
for row in csv_f:
	tmp=""
	tmp2=""
	tmp3=""
	if not row:
		continue
	elif("STATE" in row[0]):
		state=""
		tmp=row[0]+row[1]
		tmp1=tmp.split()
		n=len(tmp1)
		for x in range(2,n):
			state=state+" "+tmp1[x]
		state_code=row[3]
	elif("CONSTITUENCY" in row[0]):
		constituency=""
		tmp=row[0]+row[1]
		tmp1=tmp.split()
		n=len(tmp1)
		if(tmp1[n-1]=="(SC)" or tmp1[n-1]=="(ST)"):
			for x in range(2,n-1):
				constituency=constituency+" "+tmp1[x]
			if(tmp1[n-1]=="(SC)"):
				cat="SC"
			else: cat="ST"
		else:
			for x in range(2,n):
				constituency=constituency+" "+tmp1[x]
			cat="GEN"
		constituency_no=int(row[3])
	elif("NOMINATED" in row[0]):
		mcn=int(row[1])
		wcn=int(row[2])
		tcn=int(row[3])
		nominated=1
	elif("REJECTED" in row[0] and nominated==1):
		mcnr=int(row[1])
		wcnr=int(row[2])
		tcnr=int(row[3])
		nominated=0
	elif("WITHDRAWN" in row[0]):
		mcw=int(row[1])
		wcw=int(row[2])
		tcw=int(row[3])
	elif("CONTESTED" in row[0]):
		
		mcc=int(row[1])
		wcc=int(row[2])
		tcc=int(row[3])
	elif("FORFEITED" in row[0]):
		
		mcfd=int(row[1])
		wcfd=int(row[2])
		tcfd=int(row[3])
	elif("ELECTORS" in row[0] and "VOTED" not in row[0]):
		flag=0
	elif("GENERAL" in row[0] and flag==0):
		meg=int(row[1])
		weg=int(row[2])
		teg=int(row[3])
	elif("SERVICE" in row[0]):
		mes=int(row[1])
		wes=int(row[2])
		tes=int(row[3])
	elif("TOTAL" in row[0] and flag==0):
		met=int(row[1])
		wet=int(row[2])
		te=int(row[3])
	elif("VOTED" in row[0]):
		flag=1
	elif("GENERAL" in row[0] and flag==1):
		
		if(row[1]!=""):
			mvg=int(row[1])
		else: mvg=None
		if(row[1]!=""):
			wvg=int(row[2])
		else: 
			wvg=None
		if(row[3]!=""):
			tvg=int(row[3])
		else:
			tvg=None
	elif("POSTAL" in row[0] or "POSTAL*" in row[0]):
		if(row[1]!=""):
			mvp=int(row[1])
		else: mvp=None
		if(row[1]!=""):
			wvp=int(row[2])
		else: 
			wvp=None
		if(row[3]!=""):
			tvp=int(row[3])
		else: tvp=None
	elif("TOTAL" in row[0] and flag==1):
		if(row[1]!=""):
			mvt=int(row[1])
		else: mvt=None
		if(row[1]!=""):
			wvt=int(row[2])
		else: 
			wvt=None
		if(row[3]!=""): tv=int(row[3])
		else: tv=None
	elif("POLLED" in row[0]):
		if(row[1]!=""):
			polled_votes=int(row[1])
			tmp1=re.findall(r"[\w']+", row[2])
			n=len(tmp1)
			x=tmp1[0]+"."+tmp1[1]
			tpp=float(x)
		else:
			polled_votes=None
			tpp=None
	elif("VALID" in row[0]):
		if(row[1]!=""):
			valid_votes=int(row[1])
		else: valid_votes=None
	elif("REJECTED" in row[0] and nominated==0):
		if(row[1]!=""):
			rv=int(row[1])
			tmp1=re.findall(r"[\w']+", row[2])
			n=len(tmp1)
			x=tmp1[0]+"."+tmp1[1]
			rejected_percent=float(x)
		else:
			rejected_percent=None
			rv=None
	elif("MISSING" in row[0]):
		if(row[1]!=""):
			missing_votes=int(row[1])
		else: missing_votes=None
	
	elif("TENDERED" in row[0]):
		if(row[1]!=""):
			tendered_votes=int(row[1])
		else: tendered_votes=None
	elif("NUMBER" in row[0]):
		for x in range(0,4):
			tmp=tmp+" "+row[x]
		tmp1=re.findall(r"[\w']+", tmp)
		n=len(tmp1)
		ps_no=int(tmp1[1])
		ps_avg=int(tmp1[n-1])

	elif("rptConstituencySummary" in row[0]):
		write_data()
		state=""
		constituency=""
f.close()
reset()

#Process 1971 Data
year=1971
c = csv.writer(open("Constituency_Summary.csv", "ab"))
f=open('../1971/1971_constituency_summary_raw_data.csv')
csv_f=csv.reader(f)
nominated=0

for row in csv_f:
	tmp=""
	tmp2=""
	tmp3=""
	if not row:
		continue
	elif("STATE" in row[0]):
		state=""
		tmp=row[0]+row[1]
		tmp1=tmp.split()
		n=len(tmp1)
		for x in range(2,n):
			state=state+" "+tmp1[x]
		state_code=row[3]
	elif("CONSTITUENCY" in row[0]):
		constituency=""
		tmp=row[0]+row[1]
		tmp1=tmp.split()
		n=len(tmp1)
		if(tmp1[n-1]=="(SC)" or tmp1[n-1]=="(ST)"):
			for x in range(2,n-1):
				constituency=constituency+" "+tmp1[x]
			if(tmp1[n-1]=="(SC)"):
				cat="SC"
			else: cat="ST"
		else:
			for x in range(2,n):
				constituency=constituency+" "+tmp1[x]
			cat="GEN"
		constituency_no=int(row[3])
	elif("NOMINATED" in row[0]):
		mcn=int(row[1])
		wcn=int(row[2])
		tcn=int(row[3])
		nominated=1
	elif("REJECTED" in row[0] and nominated==1):
		mcnr=int(row[1])
		wcnr=int(row[2])
		tcnr=int(row[3])
		nominated=0
	elif("WITHDRAWN" in row[0]):
		mcw=int(row[1])
		wcw=int(row[2])
		tcw=int(row[3])
	elif("CONTESTED" in row[0]):
		
		mcc=int(row[1])
		wcc=int(row[2])
		tcc=int(row[3])
	elif("FORFEITED" in row[0]):
		
		mcfd=int(row[1])
		wcfd=int(row[2])
		tcfd=int(row[3])
	elif("ELECTORS" in row[0] and "VOTED" not in row[0]):
		flag=0
	elif("GENERAL" in row[0] and flag==0):
		meg=int(row[1])
		weg=int(row[2])
		teg=int(row[3])
	elif("SERVICE" in row[0]):
		mes=int(row[1])
		wes=int(row[2])
		tes=int(row[3])
	elif("TOTAL" in row[0] and flag==0):
		met=int(row[1])
		wet=int(row[2])
		te=int(row[3])
	elif("VOTED" in row[0]):
		flag=1
	elif("GENERAL" in row[0] and flag==1):
		
		if(row[1]!=""):
			mvg=int(row[1])
		else: mvg=None
		if(row[1]!=""):
			wvg=int(row[2])
		else: 
			wvg=None
		if(row[3]!=""):
			tvg=int(row[3])
		else:
			tvg=None
	elif("POSTAL" in row[0] or "POSTAL*" in row[0]):
		if(row[1]!=""):
			mvp=int(row[1])
		else: mvp=None
		if(row[2]!=""):
			wvp=int(row[2])
		else: 
			wvp=None
		if(row[3]!=""):
			tvp=int(row[3])
		else: tvp=None
	elif("TOTAL" in row[0] and flag==1):
		if(row[1]!=""):
			mvt=int(row[1])
		else: mvt=None
		if(row[1]!=""):
			wvt=int(row[2])
		else: 
			wvt=None
		if(row[3]!=""): tv=int(row[3])
		else: tv=None
	elif("POLLED" in row[0]):
		if(row[1]!=""):
			polled_votes=int(row[1])
			tmp1=re.findall(r"[\w']+", row[2])
			n=len(tmp1)
			x=tmp1[0]+"."+tmp1[1]
			tpp=float(x)
		else:
			polled_votes=None
			tpp=None
	elif("VALID" in row[0]):
		if(row[1]!=""):
			valid_votes=int(row[1])
		else: valid_votes=None
	elif("REJECTED" in row[0] and nominated==0):
		if(row[1]!=""):
			rv=int(row[1])
			tmp1=re.findall(r"[\w']+", row[2])
			n=len(tmp1)
			x=tmp1[0]+"."+tmp1[1]
			rejected_percent=float(x)
		else:
			rejected_percent=None
			rejected_votes=None
	elif("MISSING" in row[0]):
		if(row[1]!=""):
			missing_votes=int(row[1])
		else: missing_votes=None
	
	elif("TENDERED" in row[0]):
		if(row[1]!=""):
			tendered_votes=int(row[1])
		else: tendered_votes=None
	elif("NUMBER" in row[0]):
		continue
		for x in range(0,4):
			tmp=tmp+" "+row[x]
		tmp1=re.findall(r"[\w']+", tmp)
		n=len(tmp1)
		ps_no=int(tmp1[1])
		ps_avg=int(tmp1[n-1])

	elif("rptConstituencySummary" in row[0]):
		write_data()
		state=""
		constituency=""
f.close()