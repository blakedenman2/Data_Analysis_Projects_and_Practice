from fpdf import FPDF

pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(False)
pdf.set_margin(0)

name = input("Name: ")

url = "https://cs50.harvard.edu/python/2022/psets/8/shirtificate/shirtificate.png"
image_width = 100
page_width = pdf.w
page_center = page_width/2

pdf.add_page()
pdf.set_font("Helvetica", size=36)
pdf.cell(page_width, 40, "CS50 Shirtificate", align="C")
pdf.set_y(40)
pdf.image(url)
pdf.set_y(100)
pdf.set_font("helvetica", size=20)
pdf.set_text_color(r=255)
pdf.cell(page_width, 20, f"{name} took CS50", align="C")
pdf.output("shirtificate.pdf")
