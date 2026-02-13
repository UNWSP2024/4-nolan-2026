# By Nolan Nelsen
# Written on 2/13/2026
# Movie Tix

# Program #2: Movie Tix
# Write a program that has the user input various movie names and how many
# tickets are desired for each movie.
# At the end of the program it prints out the total number of tickets desired by the user.
# Use either a "for loop" or "while loop" to accomplish this.

def main():
    ticket_number = 0

    while True:
        movie_name = input("Enter movie name (enter 'done' when done): ")

        if movie_name == "done":
            break

        tickets = int(input(f"Enter how many tickets you would like for {movie_name}: "))
        ticket_number += tickets

    print("Total tickets: ", ticket_number)
    ######################
    # WRITE YOUR CODE HERE
    ######################


if __name__ == '__main__':
    main()
