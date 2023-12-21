import qrcode
import time
import pyfiglet
import datetime
date_time = datetime.datetime.now()
print(date_time)
print(pyfiglet.figlet_format("QR _ GENERATOR V1"))
time.sleep(10)
time.get_clock_info
print("en unos segundos tendras el QR")
print("en 10 segundos estara el QR...")
image_creater = 1
print(image_creater)
codigo = True
print(codigo)
save_qr = 1 == 1
print(save_qr)
color_1 = "negro"
print(color_1)
color_2 = "blanco"
print(color_2)
url = "usa vim o nano para cambiar el valor de este texto, borra este texto y coloca lo que gustes"
img = qrcode.make(url)
img.save("sleeper.png")

while True:
    print(img)
    listo = "ya esta el QR"
    print(listo) 
    exit_loop = input("para salir solo pon ctrl + c")
    if exit_loop.lower() == "c":
        break
   
    