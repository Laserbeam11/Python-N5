#population growth
population = int(input("enter current population: "))
Growth_rate = float(input("enter growth rate %: ")) / 100
years = int(input("enter number of years: "))

def calculate_population(population, growth_rate, years):
    New_population = population * (growth_rate) ** years
    return New_population
print(" in", years, "years, the population will be", calculate_population(population, Growth_rate, years))