#import libraries
import requests
from bs4 import BeautifulSoup
import re
# specify url

def return_web_content(url3):
    url1 = "https://timesofindia.indiatimes.com/india/pm-modi-hosts-dinner-for-russian-president-putin/articleshow/66075563.cms"
    url = "https://timesofindia.indiatimes.com/india/clown-prince-lied-on-rafale-npas-says-arun-jaitley/articleshow/65893427.cms"

    # request html
    page = requests.get(url3)

    # Parse html using BeautifulSoup, you can use a different parser like lxml if present
    soup = BeautifulSoup(page.content, 'html.parser')
    # find searches the given tag (div) with given class attribute and returns the first match it finds
    win_div = soup.find('div', class_='Normal')

    data = win_div.text
    article = ''
    for a in data:
        article += a
    readalso_pattern = re.compile('<strong>READ ALSO:(.+?)</strong>')
    data = re.findall(readalso_pattern, article)
    for a in data:
        article = article.replace(a, '')

    p = BeautifulSoup(article, 'html.parser')
    final_content = p.text.replace('READ ALSO:', '').replace('READ ALSO IN HINDI:', '')
    print(final_content)
    file_name = "content.txt"
    try:
        file = open(file_name, 'w')
        file.write(str(final_content))
    except IOError:
        print("Error: can't find file or read data")
    else:
        print("Written content in the file successfully")
        file.close()

    return final_content

