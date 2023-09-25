from escpos.printer import Usb
from datetime import datetime

print(datetime.now())
print(type(datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

print(type(datetime.strptime(
    datetime.now().strftime("%Y-%m-%d %H:%M:%S"), 
    '%Y-%m-%d %H:%M:%S'))
)
# p=Usb(0x0483, 0x5840, 0, in_ep=0x81, out_ep=0x03)

# p.set('center', density=0)
# p.text("tester....")

# p.cut(mode="FULL")
# p.close() 