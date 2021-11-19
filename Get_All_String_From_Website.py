import urllib

link="http://xmh57jrzrnw6insl.onion/"
def Get_All_String_From_Website(link):
    f = urllib.urlopen(link)
    myfile = f.read()
    print myfile

Get_All_String_From_Website(link)