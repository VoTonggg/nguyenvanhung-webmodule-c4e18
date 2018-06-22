
from models.service import Service
import mlab


mlab.connect()

id_to_delete = input("Enter the id of service you want to delete : ")

service_to_delete = Service.objects.get( pk = id_to_delete )

service_to_delete.delete()

