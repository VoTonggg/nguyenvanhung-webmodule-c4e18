from models.river import River
import mlab7

mlab7.connect()

river_in_Africa = River.objects(continent = "Africa")

for river in river_in_Africa:
    print(river.name)
    print(river.length)
    print("* "*20)