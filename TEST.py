
import urllib
import sqlite3 as lt
import sys
max_limit=5



def Id_Number_For_SQL():
    file = open('Number_Id.txt', 'r')
    Id_Number=int(file.read())
    Id_Number2=Id_Number+1
    file2= open('Number_Id.txt', 'w')
    file2.write(repr(Id_Number2))
    return Id_Number



def Get_All_String_From_Website(link):
    f = urllib.urlopen(link)
    myfile = f.read()
    return myfile

def Insert_Data_To_DataBase(identical,urladress,datainpage):
    con=lt.connect('DataBase.db')
    with con:
        cur=con.cursor()
        cur.execute("INSERT OR IGNORE INTO Websites_To_Search_In VALUES (?,?,?)",(identical,buffer(urladress),buffer(datainpage)))
    cur.close()

def PutInArrayForSQL(URL):
    Insert_Data_To_DataBase(Id_Number_For_SQL(),str(URL),str(Get_All_String_From_Website(URL)))

def DataBase_Printer():
    con=lt.connect('DataBase.db')
    with con:
        cur=con.cursor()
        cur.execute("SELECT * FROM Websites_To_Search_In")
        rows=cur.fetchall()
        for x in rows:
            print(x)
    cur.close()



def get_page(url):#This function is just to return the webpage contents; the source of the webpage when a url is given.
	try:
		f = urllib.urlopen(url)
		page = f.read()
		f.close()
		#print page
		return page
	except:	
		return ""
	return ""
def union(a,b):#The union function merges the second list into first, with out duplicating an element of a, if it's already in a. Similar to set union operator. This function does not change b. If a=[1,2,3] b=[2,3,4]. After union(a,b) makes a=[1,2,3,4] and b=[2,3,4]
	for e in b:
		if e not in a:
			a.append(e)

def get_next_url(page):
	start_link=page.find("a href")
	if(start_link==-1):
		return None,0
	start_quote=page.find('"',start_link)
	end_quote=page.find('"',start_quote+1)
	url=page[start_quote+1:end_quote]
	return url,end_quote
def get_all_links(page):
	links=[]
	while(True):
		url,n=get_next_url(page)
		page=page[n:]
		if url:
			links.append(url)
		else:
			break
	return links
def Look_up(index,keyword):#This function is for given an index, it finds the keyword in the index and returns the list of links
	#f=[]
	if keyword in index:
		return index[keyword]
	return []
#The format of element in the index is <keyword>,[<List of urls that contain the keyword>]
def add_to_index(index,url,keyword):

	if keyword in index:
		if url not in index[keyword]:
			index[keyword].append(url)
		return
	index[keyword]=[url]
def add_page_to_index(index,url,content):#Adding the content of the webpage to the index
	for i in content.split():
		add_to_index(index,url,i)

def compute_ranks(graph):#Computing ranks for a given graph -> for all the links in it
	d=0.8
	numloops=10
	ranks={}
	npages=len(graph)
	for page in graph:
		ranks[page]=1.0/npages
	for i in range(0,numloops):
		newranks={}
		for page in graph:
			newrank=(1-d)/npages
			for node in graph:
				if page in graph[node]:
					newrank=newrank+d*ranks[node]/len(graph[node])
			newranks[page]=newrank
		ranks=newranks
	return ranks
	
def Crawl_web(seed):#The website to act as seed page is given as input
	tocrawl=[seed]
	crawled=[]
	index={}
	graph={}#new graph
	global max_limit
	while tocrawl:
		p=tocrawl.pop()
		if p not in crawled:#To remove the looping, if a page is already crawled and it is backlinked again by someother link we are crawling, we need not crawl it again
			max_limit-=1
			print max_limit
			if max_limit<=0:
				break
			c=get_page(p)
			add_page_to_index(index,p,c)
			f=get_all_links(c)
			union(tocrawl,f)
			graph[p]=f
			crawled.append(p)#As soon as a link is crawled it is appended to crawled. In the end when all the links are over, we will return the crawled since it contains all the links we have so far
	return crawled,index,graph #Returns the list of links

#print index	



def QuickSort(pages,ranks):#Sorting in descending order
	if len(pages)>1:
		piv=ranks[pages[0]]
		i=1
		j=1
		for j in range(1,len(pages)):
			if ranks[pages[j]]>piv:
				pages[i],pages[j]=pages[j],pages[i]
				i+=1
		pages[i-1],pages[0]=pages[0],pages[i-1]
		QuickSort(pages[1:i],ranks)
		QuickSort(pages[i+1:len(pages)],ranks)

def Look_up_new(index,ranks,keyword):
	pages=Look_up(index,keyword)
	print '\nPrinting the results as is with page rank\n'
	for i in pages:
		##Insert_Data_To_DataBase(Id_Number_For_SQL(),pages[i],Get_All_String_From_Website(pages[i]))
		URL=str(i)
		PutInArrayForSQL(URL)
		print i+" --> "+str(ranks[i])#Displaying the lists, so that you can see the page rank along side




#print index
numRow=0
print "Enter the URL page"
seed_page=raw_input()
print "Enter What you want to search"
search_term=raw_input()
try:
	print "Enter the depth you wanna go"
	max_limit=int(raw_input())
except:
	f=None
print '\nStarted crawling, presently at depth..'
crawled,index,graph=Crawl_web(seed_page)#printing all the links

ranks=compute_ranks(graph)#Calculating the page ranks
Look_up_new(index,ranks,search_term)
##Sites_To_Put_In_DataBase=Look_up(index,search_term)
##id_In_DataBase=Id_Number_For_SQL()
##Insert_Data_To_DataBase(id_In_DataBase,index,Get_All_String_From_Website(index))
##for website in Sites_To_Put_In_DataBase:
    ##site_String=Get_All_String_From_Website("%n" %Sites_To_Put_In_DataBase[website])
    ##Insert_Data_To_DataBase(id_In_DataBase,Sites_To_Put_In_DataBase[website],site_String)
    ##id_In_DataBase+=1
##    print(Sites_To_Put_In_DataBase[website])
	