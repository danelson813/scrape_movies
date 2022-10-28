import requests
from bs4 import BeautifulSoup as bs


def print_to_file(str):
    with open('Top_Movies.csv', 'a') as f:
        f.write(str)


url = "https://www.imdb.com/chart/top/?ref_=nv_mv_250"
base = "https://www.imdb.com"
r = requests.get(url)
soup = bs(r.text, 'html.parser')

movies = soup.find("tbody").find_all('tr')
for movie in movies:
    title = movie.find('td', class_='titleColumn').find('a').get_text()
    year = movie.find('td', class_='titleColumn').find('span').get_text()
    poster_link = movie.find("td", class_="posterColumn").find('a').find('img')['src']
    movie_link = base + movie.find('td', class_="posterColumn").find('a')['href']
    rank = movie.find('td').find('span', {'name': 'rk'})['data-value']
    data = f"rank: {rank}, title: {title}, year: {year}, movie_link: '{movie_link}', poster_link: '{poster_link}'\n"
    print_to_file(data)
    