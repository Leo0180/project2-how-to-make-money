import json
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.utils import simpleSplit

# Inlezen van de JSON-factuur
with open("factuur.json", "r") as f:
    factuur = json.load(f)

# PDF-bestand aanmaken
pdf_filename = f"{factuur['factuurnummer']}.pdf"
c = canvas.Canvas(pdf_filename, pagesize=A4)

# Basisinstellingen
c.setFont("Helvetica-Bold", 16)
c.drawString(50, 800, "Factuur")

c.setFont("Helvetica", 12)
c.drawString(50, 780, f"Factuurnummer: {factuur['factuurnummer']}")
c.drawString(50, 765, f"Factuurdatum: {factuur['factuurdatum']}")
c.drawString(50, 750, f"Vervaldatum: {factuur['vervaldatum']}")

# Klantgegevens
c.setFont("Helvetica-Bold", 12)
c.drawString(50, 720, "Klantgegevens:")
c.setFont("Helvetica", 12)
c.drawString(50, 705, f"Naam: {factuur['klant']['naam']}")
c.drawString(50, 690, f"Adres: {factuur['klant']['adres']}")
c.drawString(50, 675, f"Postcode: {factuur['klant']['postcode']}")
c.drawString(50, 660, f"Stad: {factuur['klant']['stad']}")
c.drawString(50, 645, f"KVK-nummer: {factuur['klant']['KVK-nummer']}")

# Tabel koppen
c.setFont("Helvetica-Bold", 12)
y_pos = 600
c.drawString(50, y_pos, "Product")
c.drawString(250, y_pos, "Aantal")
c.drawString(300, y_pos, "Prijs/stuk")
c.drawString(400, y_pos, "Excl. BTW")
c.drawString(480, y_pos, "BTW %")
c.drawString(530, y_pos, "Incl. BTW")

# Productregels
c.setFont("Helvetica", 12)
y_pos -= 20
for product in factuur["producten"]:
    c.drawString(50, y_pos, product["productnaam"])
    c.drawString(250, y_pos, str(product["aantal"]))
    c.drawString(300, y_pos, f"€ {product['prijs_per_stuk_excl_btw']:.2f}")
    c.drawString(400, y_pos, f"€ {product['prijs_excl_btw']:.2f}")
    c.drawString(480, y_pos, f"{product['btw_percentage']}%")
    c.drawString(530, y_pos, f"€ {product['prijs_incl_btw']:.2f}")
    y_pos -= 20

# Totaalbedragen
y_pos -= 20
c.setFont("Helvetica-Bold", 12)
c.drawString(400, y_pos, "Totaal excl. BTW:")
c.drawString(530, y_pos, f"€ {factuur['totaal_excl_btw']:.2f}")

y_pos -= 20
c.drawString(400, y_pos, "Totaal BTW:")
c.drawString(530, y_pos, f"€ {factuur['totaal_btw']:.2f}")

y_pos -= 20
c.drawString(400, y_pos, "Totaal incl. BTW:")
c.drawString(530, y_pos, f"€ {factuur['totaal_incl_btw']:.2f}")

# PDF opslaan
c.save()
print(f"Factuur opgeslagen als '{pdf_filename}'")