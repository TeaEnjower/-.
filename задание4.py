class Train:
    
    def __init__(self, departure_point, destination_point, departure_time, arrival_time):
        self.departure_point = departure_point
        self.destination_point = destination_point
        self.departure_time = departure_time
        self.arrival_time = arrival_time

    def __add__(self, other):
        if self.destination_point == other.departure_point and self.arrival_time <= other.departure_time:

            new_departure_point = self.departure_point
            new_destination_point = other.destination_point
            new_departure_time = self.arrival_time
            new_arrival_time = other.arrival_time
            return Train(new_departure_point, new_destination_point, new_departure_time, new_arrival_time)
        else:
            return "Невозможно сложить два поезда"


train1 = Train("Москва", "Санкт-Петербург", "10:00", "15:00")
train2 = Train("Санкт-Петербург", "Новосибирск", "15:30", "22:00")

result = train1 + train2

print(result.departure_point, result.destination_point, result.departure_time, result.arrival_time)
    