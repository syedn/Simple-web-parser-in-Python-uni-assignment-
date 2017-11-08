import urllib 

def downloadPage(url,fileName):
    #retrieve web page and its header
    print("==================================================")
    print('==> Header Information for ',fileName)
    local_filename, headers = urllib.request.urlretrieve(url,fileName+'.html')
    print(headers)
    #create file to store header
    headerFile = open(fileName+'Header.txt','w')
    #convert HTTPMessage to string
    headerFile.write(str(headers))
    headerFile.close() 
    print("==================================================")
 

downloadPage('http://west.uni-koblenz.de/en/studying/courses/ws1617/introduction-to-web-science','intro-to-web')
downloadPage('https://west.uni-koblenz.de/de','west')
