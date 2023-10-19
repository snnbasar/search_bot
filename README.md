A search bot for google, duckduckgo and bing.
You can write the sites you want to search in "searchbotSites.txt".
It searches the keyword in those sites and gives you the links.
Usefull for finding a file in the internet.

To install use this:
pip install -r requirements.txt

optional arguments:
  -h, --help            show this help message and exit
  -o, --openurl         open url
  -s, --specific        specific sites
  -l LIMIT, --limit LIMIT
                        limit searches, default 10
  -d, --duckduckgo      only use duckduckgo
  -g, --google          only use google
  -b, --bing            only use bing
