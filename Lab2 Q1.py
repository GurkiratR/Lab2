num_years = int(input("Enter the number of years: "))

for year in range(1, num_years+1):
    total_rainfall = 0
    for month in range(1, 13):
        rainfall = float(input(f"Enter the rainfall amount for year {year}, month {month}: "))
        total_rainfall += rainfall
    avg_monthly_rainfall = total_rainfall / 12
    print(f"Total rainfall: {total_rainfall} cm")
    print(f"Average monthly rainfall: {avg_monthly_rainfall:.2f} cm\n")
