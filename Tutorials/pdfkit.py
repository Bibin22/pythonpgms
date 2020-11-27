import pdfkit
config = pdfkit.configuration(wkhtmltopdf="C:\Program Files\wkhtmltopdf\bin\wkhtml.pdf")
pdfkit.from_url("https://www.google.co.in/", "google.pdf", configuration=config)
