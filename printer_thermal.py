from escpos.printer import Usb
from datetime import datetime

# print(datetime.now())
# print(type(datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

# print(type(datetime.strptime(
#     datetime.now().strftime("%Y-%m-%d %H:%M:%S"), 
#     '%Y-%m-%d %H:%M:%S'))
# )

# print(datetime.now().strftime("%H%M%S"))

# p=Usb(0x0483, 0x5840, 0, in_ep=0x81, out_ep=0x03)

# p.set('center', density=0)
# p.text("tester....")

# p.cut(mode="FULL")
# p.close() 

jm_masuk = "10:00"
jm_keluar = "12:10"

j,m = jm_masuk.split(":")
j2,m2 = jm_keluar.split(":")

jm_masuk_seconds = (int(j)*3600) +  (int(m)*60)
jm_keluar_seconds = (int(j2)*3600) +  (int(m2)*60)

diff = jm_keluar_seconds - jm_masuk_seconds

print("diff seconds", diff)