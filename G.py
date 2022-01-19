with open('input.txt', 'r') as file_in:
    n = int(file_in.readline().strip())
    data = [list(map(int, city.strip().split())) for city in file_in]
    range_car = (data[n])
    x, y = data[n+1]
    cities = data[:n]

def travel(cities, range_car, x, y, range=0):
    if abs(cities[y][0] - cities[x][0]) + abs(cities[y][1] + cities[x][1]) <= range_car[0]:
        print(range_car)


print(travel(cities, range_car, x, y))