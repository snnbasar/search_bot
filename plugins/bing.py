from selenium.webdriver.common.by import By

site = "https://www.bing.com/search?q="
# def getLinks(searchT:str, limit = 100):
    
#     backupSearchT = searchT
#     searchT = site + searchT
#     searchT = searchT.replace(' ', '%20')
#     print(searchT)
#     r = requests.get(searchT, )
#     soup = BeautifulSoup(r.content, 'html.parser')
#     time.sleep(1)

#     # print(soup.prettify())
#     # print(soup)
#     links = []

#     try:
#         results = soup.find('ol', id = 'b_results')
#         print(results)
#         links_raw = results.find_all('a', href=True)
#         print(links_raw)
#         # if (links_raw is None) or (len(links_raw) <= 0):
#         #     print("Sonuç yok veya ip block yedi")
#         counter = 0
#         for a in links_raw:
#             if ('http' in a['href']) and (counter <= limit):
#                 counter += 1
#                 # print(a['href'])
#                 links.append(a['href'])
#     except:
#         counter = 0
#     return links

def getLinks(browser, searchT:str, limit = 100):
    
    backupSearchT = searchT
    searchT = site + searchT
    searchT = searchT.replace(' ', '%20')
    # print(searchT)
    browser.get(searchT)

    # print(soup.prettify())
    # print(soup)
    links = []

    try:
        results = browser.find_element(By.ID, 'b_results')
        # print(results)
        links_raw = results.find_elements(By.TAG_NAME, 'a')
        # print(links_raw)
        # if (links_raw is None) or (len(links_raw) <= 0):
        #     print("Sonuç yok veya ip block yedi")
        counter = 0
        for a in links_raw:
            if counter >= limit:
                break
            link = a.get_attribute('href')
            if ('http' in link) and ('bing.com' not in link) and (link not in links):
                counter += 1
                # print(link)
                links.append(link)
        return links        
    except:
        counter = 0
    # browser.quit()
    return links



# getLinks("kws site:unityassetcollection.com")