import requests
from selenium import webdriver
from bs4 import BeautifulSoup
import time

def scrape_movies(url):
    try:
        response = requests.get(url)

        if (response.status_code != 200):
            print(f"Failed to get the webpage: {response.status_code}")
        
        soup = BeautifulSoup(response.text, 'html.parser')

        # Finding all movie titles using a more stable identifier like the 'data-test-id'
        top_movies = soup.find_all('div', {'data-test-id': 'movie-list-item'})
        print(top_movies)
    
        # Loop through each movie block and extract the title
        for movie in top_movies:
            title = movie.find('span', {'class': 'styles_mainTitle__IFQyZ'}).text
            print(title)


        # top_movies = soup.find_all('span', class_='styles_mainTitle__IFQyZ styles_activeMovieTittle__kJdJj')
        # return top_movies

    except Exception as e:
        print(f"An error has occured: {e}")
        return []

    print(url)

def choose_genre():
    status = False
    genre_dict = {"1":"anime", "2":"biography", "3":"action", "4":"western", "5":"war", 
                    "6":"mystery", "7":"drama", "8":"history", "9":"comedy", "10":"crime", 
                    "11":"romance", "12":"animation", "13":"musical", "14":"adventure", 
                    "15":"sport", "16":"thriller", "17":"horror", "18":"sci-fi", "19":"fantasy"}
   
    while (status == False):
        genre = input(
        '''Genres list: 
            1. Anime
            2. Biography
            3. Action
            4. Western
            5. Military
            6. Mystery
            7. Drama
            8. History
            9. Comedy
            10. Crime
            11. Romance
            12. Animation
            13. Musical
            14. Adventure
            15. Sport
            16. Thriller
            17. Horror
            18. Sci-fi
            19. Fantasy
Enter the choice (1-19): ''')

        if ( 1 <= int(genre) <= 19):
            status = True
            return genre_dict[genre]
        else:
            status = False
            print("Invalid input! Try again!") 

def main():

    status = False
    while (status == False): 

        filter_enable = input('''Would you like to choose the genre?
                            1. All genres
                            2. Choose genre
Enter 1 or 2: ''')
        
        if filter_enable == '1':
            status = True
            url = "https://www.kinopoisk.ru/lists/movies/top250/genre--all/?utm_referrer=www.kinopoisk.ru"
        elif filter_enable == '2':
            status = True

            url = f"https://www.kinopoisk.ru/lists/movies/top250/genre--{choose_genre()}/?utm_referrer=www.kinopoisk.ru"                
        else:
            status = 0
            print("Enter a valid input!")    

    movies = scrape_movies(url)
    #print(movies)

if __name__ == "__main__":
    main()