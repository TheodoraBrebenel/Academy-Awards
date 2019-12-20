# shows info about Award winning films based on user's choice from the given menu
def main():
    print("Welcome to the Award Winning Films App!")
    file_name = input("Enter the filename to load: ")
    if file_name != "BestFilms.txt":
        print("Can't find this file. Program will use the BestFilms.txt instead.")
        infile = open("BestFilms.txt", "r")                 # opens BestFilms.txt even if that is not what the user inputted
    else:
        infile = open("BestFilms.txt", "r")                 # opens BestFilms.txt
    movie_list = infile.readlines()                        
    for i in range(len(movie_list)):
        movie_list[i]= movie_list[i].split("###")           
        movie_list[i][2]=movie_list[i][2].rstrip("\n")      
    
    # made a new nested list but every character is lower-case
    big_films_list = []
    for index in movie_list:
        small_films_list = []
        for ch in index:
            if ch.isalnum() == True or ch.istitle() == True or ch.isupper() == True or ch.isalpha() == True:
                small_films_list.append(ch.lower())
            else:
                small_films_list.append(ch.lower())
        big_films_list.append(small_films_list)        

    flag = True
    while flag:
        print("Choose one of the following options: ")
        print("1. Display all film-titles in the database (and their IMDB scores).")
        print("2. Display the winning film for a specific year.")
        print("3. Display the genre and IMBD score for a specific film.")
        print("4. Display the film-title with the highest IMDB score.")
        print("5. Display the film-title with the lowest IMDB score.")
        print("6. Display the different(unique) genres (categories) of all the winning films.")
        print("7. Display all the film-titles for a specific genre.")
        print("8. Add your prediction (film-title, genre) for 2020.")
        print("9. Quit")
        choice = (input("Enter your choice: "))
        print("\n")
        
        if choice == "1":  #shows films and their IMDB scores
            for film_info in big_films_list:  
                print("Best Film: ", film_info[0].title(), "\nScore: ", (film_info[2]),"\n")
            print("\n")

        elif choice == "2":  # shows winning film of specific year
            year_flag = True
            while year_flag:
                year_option = eval(input("Enter a year from 1929 - 2019: "))        
                if 1929 <= year_option <= 2019:                                
                    year_option -= 1929                                        
                    print("Best Film: ", big_films_list[year_option][0].title(), "\nGenre:", big_films_list[year_option][1].title(), "\nIMDB Score: ",big_films_list[year_option][2])
                    print("\n")
                    year_flag = False
                else:
                    print("Invalid input!\nYou must choose a year between 1929-2019!\nTry again!\n")
                    continue

        elif choice == "3": #shows genre and IMDB score of a specific film
            count = 0
            inputted_film_option = input("Enter the film-title: ")
            film_option = inputted_film_option.lower()                         
            for film_info in big_films_list:                                         
                if film_info[0] == film_option:                               
                    print("Genre: ", big_films_list[count][1].title(), "\nIMDB Score: ", big_films_list[count][2])   
                else:
                    count +=1                                                 
            print("\n")

        elif choice == "4":  # film with highest IMDB score
            largest_num = "0"
            large_best_film = []
            for film_info in big_films_list:
                if (film_info[2]) > largest_num:                                     
                    largest_num = film_info[2]                                
                    large_best_film.append(film_info)                        
            print("Best Film:" , large_best_film[-1][0].title(), "\nGenre: ", large_best_film[-1][1].title(), "\nIMDB Score: ", large_best_film[-1][2])
            print("\n")

        elif choice == "5": # film with lowest IMDB score
            smallest_num = "9.9"
            small_best_film = [] 
            for film_info in big_films_list:
                if (film_info[2]) < smallest_num:
                    smallest_num = film_info[2]
                    small_best_film.append(film_info)
            print("Best Film:" , small_best_film[-1][0].title(), "\nGenre: ", small_best_film[-1][1].title(), "\nIMDB Score: ", small_best_film[-1][2])
            print("\n")

        elif choice == "6": # shows all the genres
            genre_list = []
            print("Film genres of Award Winning Films (in alphabetical order):")
            for film in big_films_list:
                if film[1] in genre_list:
                    continue
                else:
                    genre_list.append(film[1])
            genre_list.sort()
            print("  ".join(genre_list))
            print("\n")
            
            
        elif choice == "7": # shows films of a specific genre
            chosen_genre = input("Enter genre: ")
            print("\n")
           
            count = 0
            for film in big_films_list:
                if film[1] == chosen_genre.lower():
                    count += 1
            if count >= 1:
                print('The Academy Award winners in the "', chosen_genre.title(), '" genre are:', sep= "")
                for film in big_films_list:
                    if film[1] == chosen_genre.lower():
                        print("    ",film[0].title())
                print("\n")
            elif count == 0:
                official_chosen_genre = chosen_genre.lower()
                print('There are no Academy Award winners in the "', official_chosen_genre.title(), '" genre.\n', sep= "")
        
        elif choice == "8": #add prediction for 2020 
            
            
            movie_prediction = input("Enter film-title: ")
            genre_prediction = input("Enter genre: ")
            prediction = [movie_prediction, genre_prediction,"7.5"]
            big_films_list.append(prediction)
            print("\n")

        elif choice == "9":  # quit   
            infile.close()
            save = input("Would you like to save any changes you made to the database? ")
            if save.startswith("y") or save.startswith("Y"):
                infile2 = open("BestFilms_updated.txt", "w")
                updated_films_list = []
                for films in big_films_list:
                    films[0]=films[0].title()
                    films[1]=films[1].title()
                    films[2] = films[2]+"\n"
                    updated_films_list.append("###".join(films))
                big_films_string = "".join(updated_films_list)
                print("Great! Your prediction will be added to the database!")
                infile2.write(big_films_string)
                infile2.close()
                print("Thank you for using the Award Winning Films Apps. Goodbye!")
                flag = False

            else:
                infile2 = open("BestFilms_updated.txt", "w")
                updated_films_list = []                
                for films in movie_list:
                    films[0]=films[0].title()
                    films[1]=films[1].title()
                    films[2] = films[2]+"\n"
                    updated_films_list.append("###".join(films))
                movie_list = "".join(updated_films_list)
                infile2.write(movie_list)
                infile2.close()
                print("Thank you for using the Award Winning Films Apps. Goodbye!")
                flag = False 
        else:
            print("Invalid choice. Try again!")
            continue
    
main()