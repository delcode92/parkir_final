import os, webbrowser
from fpdf import FPDF
# pdf = FPDF()
# pdf.set_font('Arial', '', 8)

# lap_name = f"laporan_file1.pdf"
# pdf.output(f'./{lap_name}', 'F')

# path1 = os.path.abspath(lap_name)


# lap_name = f"laporan_file2.pdf"
# pdf.output(f'./{lap_name}', 'F')

# path2 = os.path.abspath(lap_name)

# webbrowser.open_new("file://"+path1)
# webbrowser.open_new("file://"+path2)

# stat_kendaraan = "masuk"

# print(type(stat_kendaraan))

# stat_kendaraan=("masuk",)
# print(type(stat_kendaraan))


def tes(jns_transaksi=""):
    jns_trans = "" if jns_transaksi=="" else f"AND (jns_transaksi='{jns_transaksi.lower()}' OR jns_transaksi='{jns_transaksi}')"
    print(jns_trans)

tes("Voucher")

# def tes(x={}):
#     print(x)

# tes({"k":"val"})