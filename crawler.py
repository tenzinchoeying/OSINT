#https://pastebin.com/0w4MpdBW
#https://www.circl.lu/doc/misp/feed-osint/

import re
import csv
import bs4
import sys
from urllib import urlopen
from bs4 import BeautifulSoup
from itertools import izip_longest as zip_longest

#Taking user input for the URL which is to be crawled
url = raw_input("Enter the URL: ")

#Accessing webpage
try:
	page = urlopen(url)
except:
	print("Error opening the URL")

#Using beautifulsoup to parse the webpage
soup = BeautifulSoup(page, 'html.parser')

#Checking if access was denied for the requested webpage
Access_Denied = re.search("Access Denied", soup.get_text(separator=' '))
access_denied = re.search("access denied", soup.get_text(separator=' '))

if Access_Denied or access_denied:
	print('Access to the webpage is denied.')
	exit()

#Extracting all relevant IOCs like emails,ips,hashes and urls
match = re.search("pastebin", url)
emails = re.findall(r'([\d\w\.]+@[\d\w\.\-]+\.\w+)', soup.get_text(separator=' '))
ips = re.findall(r'(\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b)', soup.get_text(separator=' '))
md5 = re.findall(r'(\b[0-9a-fA-F]{32}\b)', soup.get_text(separator=' '))
sha1 = re.findall(r'(\b[0-9a-fA-F]{40}\b)', soup.get_text(separator=' '))
sha256 = re.findall(r'(\b[A-Fa-f0-9]{64}\b)', soup.get_text(separator=' '))
urls = re.findall(r'(?:(?:https?|hxxps?|www):\/\/[^\s][^"]+)', soup.get_text(separator=''))

if match:
	#Extracting additional information if provided website is pastebin 
	attack_vector = re.findall(r'((?<=-\s)[A-Za-z][^0-9][^#*]*(?=:))', soup.get_text(separator=' '))
	number = re.findall(r'((?<=:\s)[0-9]*)', soup.get_text(separator=' '))
	number = list(filter(None, number))
	number = [int(i) for i in number]
	name = []

	for x in range(len(attack_vector)):
		name.append([])

	for x in range(len(name)):
		for i in range(0,number[x]):
			name[x].append(sha256[0])
			del sha256[0]

	export_data = zip_longest(*name, fillvalue = '')

	#Writing all extarcted IOCs to a CSV file 
	with open('/root/data.csv', 'wb+') as myfile:
		wr = csv.writer(myfile)
		wr.writerow((attack_vector))
		wr.writerows(export_data)
else:
	#Extracting additional information if provided website is other than pastebin 
	final_data = []
	row_title = []

	if len(emails) > 0:
		final_data.append(emails)
		row_title.append("emails")
	if len(ips) > 0:
		final_data.append(ips)
		row_title.append("ips")
	if len(md5) > 0:
		final_data.append(md5)
		row_title.append("md5")
	if len(sha1) > 0:
		final_data.append(sha1)
		row_title.append("sha1")
	if len(sha256) > 0:
		final_data.append(sha256)
		row_title.append("sha256")	
	if len(urls) > 0:
		final_data.append(urls)
		row_title.append("urls")
	
	export_data = zip_longest(*final_data, fillvalue = '')
	
	#Writing all extarcted IOCs to a CSV file
	with open('/root/data.csv', 'wb+') as myfile:
		wr = csv.writer(myfile)
		wr.writerow(row_title)
		wr.writerows(export_data)
