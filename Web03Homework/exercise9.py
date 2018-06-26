from models.river import River
import mlab7

mlab7.connect()

river_in_SAmerica_lt1000km = River.objects(continent = "S. America", length__lt=1000) 

for river in river_in_SAmerica_lt1000km:
    print(river.name)
    print(river.length)
    print("* "*20)