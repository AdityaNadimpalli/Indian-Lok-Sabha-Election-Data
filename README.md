# Extraction of Indian (Lok Sabha) Election Data 1971-2014

This is an initiative to create an online repository of Indian election data that can be easily used by researchers. Most of the election data at present is present in scanned image or PDF form, from which it is difficult to plot graphs, observe trends and perform other calculations.
I used the JRuby API for Tabula and wrote additional Python code to extract Indian election data from PDF documents.

Tabula is a tool to extract tables from PDF documents into a CSV file	format. Tabula can be used through a GUI tool or accessed through JRuby and Java APIs.
The JRuby API for tabula was used to first extract raw data from the PDF document into the CSV format.

I used Python 2.7 to convert the raw output CSV files from the JRuby-Tabula program into a readable and well organized final output file. This step is necessary because of the structure of the Election Commission of India documents. Data in different parts of the same page is often spaced and presented differently. For example the top half of a page may have multiple columns of data whereas the bottom half may have only one or two columns with different indentations and spacing than the top half. 

Tabula was not able to pick up most of these finer differences and as a consequence, names and numbers are often split across multiple columns or lines and subsequent processing with the Python code I have written is necessary to clean and organize the election data. 

## Getting Started

Work Flow for Data Extraction:

•	Use jruby based tabula extractor code to roughly convert the data tables in a pdf document into csv format. The data in this raw csv file is not yet structured and readable.

•	Tabula uses column spacing dimensions to convert tabular data into csv format. For each year’s pdf documents, these dimensions need to be manually adjusted so that all the data in the document is correctly captured in the csv file.  

•	Use a python program to restructure the tabula output into a final readable data file.

Please refer the "Extraction Explanation" Document for clear explanation of the file contents in the project and the order of execution of the program files.



### Prerequisites

1.	JRuby (http://jruby.org/)

JRuby is a Java implementation of Ruby. At the time of working on this project in May 2015, I used a JRuby API for Tabula. I used JRuby version 1.7.20 along with Java 8, although later versions are now available. A direct Windows installer for JRuby can be downloaded at http://jruby.org/download. Java should be set up prior to installing and working with JRuby.

Examples of JRuby code for tabula can be seen at https://docs.omniref.com/github/tabulapdf/tabula-extractor/0.7.6
  
2.	Tabula
	Tabula (http://tabula.technology/) is a tool to extract tables from PDF documents into a CSV file 	format. Tabula can be used through a GUI tool or accessed through JRuby and Java APIs.
	For this project, I have used Tabula for Windows, version 0.9.7. Different versions of Tabula can 	be downloaded at https://github.com/tabulapdf/tabula/releases. 

3.	Python 2.7

## Acknowledgments

* The original Election Commission of India documents are taken from http://eci.nic.in/eci_main1/ElectionStatistics.aspx


