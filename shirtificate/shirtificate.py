from fpdf import FPDF

name = input("Name: ")

pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.add_page()

pdf.image(r"shirtificate.png", x=16, y=60, w=180, h=200)

pdf.set_font("Arial", size=30)
pdf.text(65, 40, "CS50 Shirtificate")

pdf.set_font("Arial", size=20)
pdf.set_text_color(255, 255, 255)
pdf.text(60, 125, f"{name} took CS50")


pdf.output("shirtificate.pdf")
