import requests


class MovieDB:
    def __init__(self):
        self.api_url = "https://api.themoviedb.org/3" 
        self.token = input("Enter your API key: ")

    def searchFilm(self, name):
        response = requests.get(self.api_url + "/search/keyword?api_key=" + self.token + "&query=" + name + "&page=1")
        return response.json()

    def bestFilms(self):
        response = requests.get(self.api_url + "/movie/popular" + "?api_key=" + self.token)
        return response.json()

    def nowFilms(self):
        response = requests.get(self.api_url + "/movie/now_playing" + "?api_key=" + self.token)
        return response.json()


moviedb = MovieDB()

while True:
    selection = input("1- Movie search\n2- Most popular movies\n3- Films in vision\n4- Exit\nOption: ")
    if selection == "4":
        print("Logging out...")
        break
    else:
        if selection == "1":
            name = input("Enter the name of the movie: ")
            result = moviedb.searchFilm(name)
            for r in result["results"]:
                print(r["name"])
        elif selection == "2":
            result = moviedb.bestFilms()
            for r in result["results"]:
                print(r['original_title'])

        elif selection == "3":
            result = moviedb.nowFilms()
            for r in result["results"]:
                print(r['original_title'])
        else:
            print("Yanlış tuşlama tekrar tuşlayınız")
            continue
