from selenium.webdriver.common.by import By

site = "https://www.google.com/search?q="

def getLinks(browser, searchT:str, limit = 100):
    
    backupSearchT = searchT
    searchT = site + searchT
    searchT = searchT.replace(' ', '+')
    # print(searchT)
    browser.get(searchT)

    # print(soup.prettify())
    # print(soup)
    links = []

    try:
        results = browser.find_element(By.ID, 'rso')
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
            if ('http' in link) and ('google.com' not in link) and (link not in links):
                counter += 1
                # print(link)
                links.append(link)
        return links        
    except:
        counter = 0
    # browser.quit()
    return links



# getLinks("kws site:unityassetcollection.com")