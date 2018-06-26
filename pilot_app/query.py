from models.service import Service
import mlab

mlab.connect()

# all_service = Service.objects()
# first_service = all_service[0]

# print(first_service.address)

id_to_find = "5b2ba6aa5c9be2164c75b14e"

# hera = Service.objects.get( id = id_to_find)

service = Service.objects().with_id(id_to_find)

if service is not None:
    # hera.delete()
    print(service.yob)
    service.update(set__yob=2005)
    service.reload()
    print(service.yob)
else:
    print("Service not found")
