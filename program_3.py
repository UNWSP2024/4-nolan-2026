# By Nolan Nelsen
# Written on 2/13/2026
# Average Rainfall

# Program #3: Average Rainfall
# Write a program that uses nested loops to collect data and calculate the average
# rainfall over a period of years.
# The program should first ask for the number of years.
# The outer loop will iterate once for each year.
# The inner loop will iterate twelve times, once for each month.
# Each iteration of the inner loop will ask the user for inches of rainfall for each month.
# After all iterations, the program should display the number of months,
# the total inches of rainfall, and the average rainfall per month for the entire period.

def main():
    years = int(input("Enter number of years: "))

    total_rain = 0
    months = 0

    for y in range(years):
        print("Year:", y + 1)

        for m in range(12):
            rain = float(input("Inches of rainfall for month " + str(m + 1) + ": "))
            total_rain = total_rain + rain
            months = months + 1

    average = total_rain / months

    print("Total months:", months)
    print("Total rainfall:", total_rain, "inches")
    print("Average rainfall per month:", average, "inches")

    ######################
    # WRITE YOUR CODE HERE
    ######################


if __name__ == '__main__':
    main()
