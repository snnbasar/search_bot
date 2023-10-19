from googlesearch import search as g_search
from colorama import Fore, Style
import webbrowser
import argparse
from plugins import bing
from plugins import google
from plugins import duckduckgo
from selenium import webdriver



searchSiteFile = 'searchbotSites.txt'
foundLinks = []

def getSearchStringWithSites():
    file1 = open(searchSiteFile, 'r')
    Lines = file1.readlines()
    finalString = textToSearch
    counter = 0
    for i in Lines:
        if(counter != 0):
            finalString += ' |'
        finalString += ' site:' + i.strip()
        counter += 1
    return finalString

def getSearchStringWithSites_DDG():
    file1 = open(searchSiteFile, 'r')
    Lines = file1.readlines()
    finalString = textToSearch
    counter = 0
    for i in Lines:
        if(counter != 0):
            finalString += ' |' + " " + textToSearch
        finalString += ' site:' + i.strip()
        counter += 1
    return finalString

def getSearchSites():
    file1 = open(searchSiteFile, 'r')
    Lines = file1.readlines()
    links = []
    for i in Lines:
        links.append(i.strip())
    return Lines

def googleSearch_New(browser):
    print(txt_rd("Google Search Results: "))
    searchT = textToSearch

    if(bool_specific):
        # searchT = getSearchStringWithSites()
        for s in getSearchSites():
            newSearchT = str(searchT) + " site:" + s
            print(newSearchT)
            links = google.getLinks(browser, newSearchT, limit)
            for i in links:
                printLink(i)
    else:
        links = google.getLinks(browser, searchT, limit)
        for i in links:
            printLink(i)
        

def duckduckgoSearch(browser):
    print(txt_rd("DuckDuckGo Search Results: "))
    searchT = textToSearch

    if(bool_specific):
        # searchT = getSearchStringWithSites_DDG()
        for s in getSearchSites():
            newSearchT = str(searchT) + " site:" + s
            print(newSearchT)
            # ddg_Search(newSearchT)
            ddg_Search_New(browser, newSearchT, limit)
            # time.sleep(1)        
    else:
        # ddg_Search(newSearchT)
        ddg_Search_New(browser, searchT, limit)

def ddg_Search_New(browser, newSearchT, limit):
    links = duckduckgo.getLinks(browser, newSearchT, limit)
    for link in links:
        printLink(link)
               

def bingSearch_New(browser):
    print(txt_rd("Bing Search Results: "))
    searchT = textToSearch
    

    if(bool_specific):
        # searchT = getSearchStringWithSites()
        for s in getSearchSites():
            newSearchT = str(searchT) + " site:" + s
            print(newSearchT)
            links = bing.getLinks(browser, newSearchT, limit)
            # if (links is None) or (len(links) <= 0):
            #     print("Sonuç yok veya ip block yedi")
            for i in links:
                printLink(i)
    else:
        links = bing.getLinks(browser, searchT, limit)
        for i in links:
            printLink(i)
    browser.quit()



def CheckForOpenUrl(url=""):
    if(openUrl):
        webbrowser.open(url)

def txt_grn(text):
    return Fore.GREEN + text + Style.RESET_ALL


def txt_rd(text):
    return Fore.RED + text + Style.RESET_ALL


def txt_yel(text):
    return Fore.YELLOW + text + Style.RESET_ALL

def printLink(link):
    if link in foundLinks:
        return
    foundLinks.append(link)
    print(txt_yel(link))
    CheckForOpenUrl(link)

def main():
    
    parser = argparse.ArgumentParser(description="search site")
    parser.add_argument("-o", "--openurl",
                        default=False,
                        action="store_true",
                        dest="url",
                        help="open url")
    parser.add_argument("-s", "--specific",
                        default=True,
                        action="store_true",
                        dest="specific",
                        help="specific sites")
    parser.add_argument("-l", "--limit",
                        default=10,
                        type=int,
                        dest="limit",
                        help="limit searches, default 10")
    parser.add_argument("-d", "--duckduckgo",
                        default=False,
                        action="store_true",
                        dest="useddg",
                        help="only use duckduckgo")
    parser.add_argument("-g", "--google",
                        default=False,
                        action="store_true",
                        dest="usegoogle",
                        help="only use google")
    parser.add_argument("-b", "--bing",
                        default=False,
                        action="store_true",
                        dest="usebing",
                        help="only use bing")
    
    args = parser.parse_args()
    global openUrl
    openUrl = args.url
    global bool_specific
    bool_specific = args.specific
    global limit
    limit = args.limit
    global useddg
    useddg = args.useddg
    global usegoogle
    usegoogle = args.usegoogle
    global usebing
    usebing = args.usebing

    query = input("Anahtar Kelime: ")
    global textToSearch
    textToSearch = query

    print(getSearchStringWithSites())
    print(getSearchStringWithSites_DDG())
    print("----- search site -----")

    browser = webdriver.Chrome()
    if(useddg is False 
       and usegoogle is False 
       and usebing is False):
        googleSearch_New(browser)
        duckduckgoSearch(browser)
        bingSearch_New(browser) 
    elif(usegoogle is True):
        googleSearch_New(browser)
    elif(useddg is True):
        duckduckgoSearch(browser)
    elif(usebing is True):
        bingSearch_New(browser)      
    # yandexSearch()
    # webSearch()
    # bingSearch()
    browser.quit()


if __name__ == "__main__":
    main()
