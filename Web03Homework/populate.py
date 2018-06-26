from models.service import Service
import mlab

mlab.connect()

new_service = Service(
    name = "Linh Ka",
    yob = 1999,
    gender = 0,
    height = 169,
    phone = "123456781234",
    address = "Hà Nội",
    status = False,
    description = "Cute, đáng yêu",
    image = "static/image/linhka.jpg" ,
    measurements = [80,60,70],
)
new_service.save()
