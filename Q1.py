#function to break domain in domain and sub-domains
def breakDomains(domain):
    domainsList = []
    count = domain.count('.') #count number of domains
    for eachDomain in domain.split('.'):#break at dots in domain
        domainsList.append(eachDomain) 
    for printDomain in range(count+1): #print each domain
        if(printDomain == count): #if last domain fetched then it's TLD
            print("        TLD:: ", domainsList[printDomain])
        else: #sub-domains
            print("        Sub Domain:: ",domainsList[printDomain]) 
     
            
#function to parse url                   
def urlparser(url):
    urlPortions = {}
    
    print('===============================================')
    if not url:
        print("No URL Found")
    else:
        print(url)   
    print('-------------------------------------------')    
    
    # Scheme
    if '://' in url:
        urlPortions['Scheme'], url = url.split('://', 1)
    #domain and Port/url
    if ':' in url: #if true that means url contains port number
        urlPortions['domain'], url = url.split(':',1)
        # if(:) in url that means we had a port in url so 
        #after : and before / comes port number
        urlPortions['port'], url = url.split('/',1)

    elif '/' in url: #if no port number in url then domain & path
        urlPortions['domain'], url = url.split('/',1)

         
    #path
    if '?' in url:
        urlPortions['path'], url = url.split('?',1)
        
        if '#' in url:
            urlPortions['query'], urlPortions['fragment'] = url.split('#')
        elif url: 
            urlPortions['query'] = url
            
    elif '#' in url:
        urlPortions['path'], urlPortions['fragment'] = url.split('#')
    else:
        if url:
            urlPortions['path'] = url
    
    #print URL portions
    for key in urlPortions:
        if key == 'domain':
            print(key,' : ', urlPortions[key])
            breakDomains(urlPortions[key])
        else:
            print(key,' : ', urlPortions[key])
    print('===============================================')
    

#Call Function
URL = "http://www.google.uk:1000/path/to/myfile.html?key1=value1&key2=value2#InTheDocument"
urlparser(URL)
URL = "http://www.google.a.c.d.e.uk:1000/path/to/myfile.html?key1=value1&key2=value2#InTheDocument"
urlparser(URL)
URL = "https://www.overleaf.com/9565720ckjijuhzpbccsd#/347876331/"
urlparser(URL)
URL = "http://www.example.com/ajax.html#!mystate"
urlparser(URL)
URL = "http://www.example.com/ajax.html?_escaped_fragment_=mystate"
urlparser(URL)

