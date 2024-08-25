# Programmer: Kristina Mueller
# Course: CS701/GB-731, Dr. Yalew
# Date: 08/24/2024
# Programming Assignment: 7
# Constants for column indices
# Function that loads movie data from a CSV file and returns it as a list of lists.
# Function that adds a profit column to the movie data.
# Function that prints the movies with the highest and lowest profits.
# Function that prints detailed information about a movie.
# Function that saves the movie data with the profit column to a new CSV file.

import csv

def main():
# Constants for column indices
    RELEASE_DATE = 0
    TITLE = 1
    COST = 2
    REVENUE = 3
    PROFIT = 4

# Function that loads movie data from a CSV file and returns it as a list of lists.
    def load_movie_data(file_path):
        with open('C:\\Users\\maren\\OneDrive\\Data Science M.S\\Summer 2024\\Intro to Programming\\PY_1932377\\CH01\\programming-assignment-7-mkmueller27\movies.csv', 
          mode ='r') as file:
            moviesFile = csv.reader(file)
            data = [row for row in moviesFile]
        return data
    
    file_path = 'C:\\Users\\maren\\OneDrive\\Data Science M.S\\Summer 2024\\Intro to Programming\\PY_1932377\\CH01\\programming-assignment-7-mkmueller27\movies.csv'
    movie_data = load_movie_data(file_path)
    print("Movie data is loaded")
    print(movie_data)   

    for row in movie_data:
        Release_Date = row[RELEASE_DATE]
        Title = row[TITLE]
        Cost = row[COST]
        Revenue = row[REVENUE]

        print("Release Date: " + Release_Date + ", Title: " + Title + ", Cost: " + Cost + ", Revenue: " + Revenue )


# Function that adds a profit column to the movie data.
    def add_profit_column(movie_data):
        data_updated = []
        for row in movie_data:
            
            Cost = float(row[COST])
            Revenue = float(row[REVENUE])
            Profit = Revenue - Cost
            Profit_formatted = "%.2f" % Profit
            additional_row = row + [Profit_formatted]
            data_updated.append(additional_row)
    
        return data_updated
   
    movie_data_w_profit = add_profit_column(movie_data)
    print("Movie data with profit column:")
    print(movie_data_w_profit)

    for row in movie_data_w_profit:
        Release_Date = row[RELEASE_DATE]
        Title = row[TITLE]
        Cost = row[COST]
        Revenue = row[REVENUE]
        Profit = row[-1]

        print("Release Date: " + Release_Date + ", Title: " + Title + ", Cost: " + Cost + ", Revenue: " + Revenue + ", Profit: " + str(Profit))

# Function that prints the movies with the highest and lowest profits.
    def print_min_and_max_profit(movie_data):
        max_profit = float(movie_data[0][PROFIT])
        min_profit = float(movie_data[0][PROFIT])
        max_profit_movie = movie_data[0]
        min_profit_movie = movie_data[0]

        for i in range(1, len(movie_data)) :
            try:
                profit = float(movie_data[i][PROFIT])
                if profit > max_profit :
                    max_profit = profit
                    max_profit_movie = movie_data[i]
        
                if profit < min_profit :
                    min_profit = profit
                    min_profit_movie = movie_data[i]
            except ValueError:
                pass
        print("Movie with the largest profit: " + max_profit_movie[TITLE] + " with " + str(max_profit))
        print("Movie with the lowest profit: " + min_profit_movie[TITLE] + " with " + str(min_profit))

    print_min_and_max_profit(movie_data_w_profit)

# Function that prints detailed information about a movie.

    def print_details(movie_data, title):
        for row in movie_data:
            if row[TITLE].lower() == title.lower():
                print("Here are the details about: " + row[TITLE])

                print("Release Date: " + row[RELEASE_DATE])
                print("Title: " + row[TITLE])
                print("Cost: " + row[COST])
                print("Revenue: " + row[REVENUE])
                print("Profit: " + str(row[PROFIT]))
                return
        
# try it out
    print_details(movie_data_w_profit, "Titanic")

# Function that saves the movie data with the profit column to a new CSV file.
    def save_movie_data(movie_data, output_filename):
        with open('movies.csv', mode= 'w') as csvfile:
            writer = csv.writer(csvfile)
            
            writer.writerows(movie_data)

        print("Movie data saved to: " + output_filename)

    save_movie_data(movie_data_w_profit, 'movies_with_profit.csv')  

if __name__ == "__main__":
    main()