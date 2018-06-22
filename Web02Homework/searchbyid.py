from models.service import Service
import mlab

mlab.connect()

id_to_find = input("Enter the id you want to find: ")

service_to_find = Service.objects.get( pk = id_to_find)

print(service_to_find.name)