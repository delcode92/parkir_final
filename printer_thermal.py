from escpos.printer import Usb

p=Usb(0x0483, 0x5840, 0, in_ep=0x81, out_ep=0x01)

p.set('center', density=0)
p.text("tester....")

p.cut(mode="FULL")
p.close() 