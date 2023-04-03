import random
class Movie:
   def __init__(self,title, year,genre,number_of_plays):
       self.title = title
       self.year = year
       self.genre = genre
       self.number_of_plays = number_of_plays
      
       #self.current_number_of_plays=0

   def play(self):
       self.number_of_plays += 1

   def __str__(self) -> str:
      return f"{self.title} ({self.year}) -- {self.number_of_plays}"
   
    
class Series(Movie):
   def __init__(self,number_of_episode, number_of_season, *args, **kwargs):
       super().__init__(*args, **kwargs)
       self.number_of_episode = number_of_episode
       self.number_of_season = number_of_season   

   def __str__(self) -> str:
      return f"{self.title} S{self.number_of_season}E{self.number_of_episode} -- {self.number_of_plays}"
            
                                                  

movie1 =Movie(title="aBond",year=2000,genre= "Action", number_of_plays=2)
movie2 =Movie(title="cBond",year=2000,genre= "Action", number_of_plays=10)
movie3 =Movie(title="bond",year=2000,genre= "Action", number_of_plays=8)

series1=Series(title="Friends",year="1990", genre="comedy", number_of_episode="24",number_of_season="10",number_of_plays=12)
list=[movie1,series1, movie2, movie3]


def get_movies(moviesAndSeriesList):
   moviesList=[]
   for movieOrSeries in moviesAndSeriesList:
      if type(movieOrSeries) == Movie:
         moviesList.append(movieOrSeries)
   moviesList = sorted(moviesList, key = lambda movie:movie.title)
   return moviesList


def search(list):
    searchTitle = input("Podaj szukany tytuł:    ")
    for movie in list:
        if searchTitle == movie.title:
             print ("Podany tytuł jest w bibliotece") 
             return movie
    print (" Podanego tytułu nie ma w bibiotece")


def generate_views(moviesList):
   aMovie=random.choice(moviesList)
   randomNumber=random.randint(1,100)
   aMovie.number_of_plays += randomNumber
   print(aMovie)

#generate_views(list)

def generateRandomViews(movies):
    for i in range(1,11):
     generate_views(movies)

def top_titles(movies):
    sorted_movies = sorted(movies, key = lambda movie:movie.number_of_plays,reverse = True)
    return sorted_movies[0:2]
     

print(top_titles(list))



#print(search(list))

#  moviesListSorted = get_movies(list);
for aMovie in top_titles(list):
   print(aMovie)



