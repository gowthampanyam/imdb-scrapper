from bs4 import BeautifulSoup
import requests, openpyxl

#Excel or .csv filehandling with pyhton
excel = openpyxl.Workbook()
sheet = excel.active
sheet.title= 'Top Rated Movies'
sheet.append(['Movie Rank', 'Movie Name', 'Release Year' , 'Movie Rating','Movie Reference' ])

imdb_html_content=requests.get('https://www.imdb.com/chart/top/?sort=rk,asc&mode=simple&page=1').text
soup = BeautifulSoup(imdb_html_content,'lxml')
movies = soup.find('tbody',class_='lister-list').find_all('tr')

for movie in movies:
    movie_name=movie.find('td',class_='titleColumn').a.text

    movie_ref=movie.find('td',class_='titleColumn').a['href']
    
    movie_ref_url="https://www.imdb.com/" + movie_ref
    
    movie_year=movie.find('span',class_='secondaryInfo').text.strip('()')
    
    movie_rating=movie.find('td',class_='ratingColumn imdbRating').find('strong').text
    
    movie_rank=movie.find('td',class_='titleColumn').text.split('.')[0].replace(' ','')
    
    sheet.append([movie_rank,movie_name,movie_year,movie_rating,movie_ref_url])
    #print(f'{movie_rank}. {movie_name}   {movie_year}   {movie_rating}')


excel.save('c:\\Users\\gowth\\Desktop\\Gowtham\\WebScraping\\IMDB Top 250.xlsx')
