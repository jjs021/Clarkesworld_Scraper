

import requests
r = requests.get('https://clarkesworldmagazine.com/')





import pandas as pd





from bs4 import BeautifulSoup
soup = BeautifulSoup(r.text, 'html.parser')





results = soup.find_all(attrs={"class":("index-table")})









records = []
i = 0
issue_number = ''
issue_date = ''
category = ''
for itable in soup.find(attrs={"class":("index-table")}).find_all(attrs={"class":("index-table")}):
    h1 = itable.find('h1', attrs={"class":("issue")})
    if h1:
        (issue_number, issue_date) = h1.text.split(" – ")
    section = itable.find('p', attrs={"class":("section")})
    if section:
        category = section.text
    stories = itable.find_all('p', attrs={"class":("story")})
    bylines = itable.find_all('p', attrs={"class":("byline")})
    for idx, story in enumerate(stories):
        story_link = story.find('a')
        title = story_link.text
        url = story_link['href']
        author = bylines[idx].find("span", attrs ={"class":("authorname")}).text
        records.append([title, author, url, category, issue_number, issue_date])









df = pd.DataFrame(records, columns=['Title', 'Author', 'url', 'Category', 'Issue_number', 'Issue_date'])






df.to_csv('Clarkesworld.csv', index=False)


