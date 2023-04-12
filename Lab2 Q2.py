def get_positive_input(prompt):
    while True:
        value = input(prompt)
        try:
            value = float(value)
            if value <= 0:
                raise ValueError
            return value
        except ValueError:
            print("Please enter a positive number.")

def calculate_species(start_count, daily_increase, num_days):
    print("Day Approximate                          Population")
    print(f" 1                                         {start_count} ")
    for day in range(2, num_days+1):
        start_count *= (1 + daily_increase)
        print(f"{day:2}                                         {start_count:.2f} ")

start_count = get_positive_input("Starting number of organisms: ")
daily_increase = get_positive_input("Average daily percentage increase: ") / 100
num_days = int(get_positive_input("Enter the number of days to display the final data: "))

calculate_species(start_count, daily_increase, num_days)
