import qrcode

cod = qrcode.QRCode(version = 1, box_size = 8,  border = 2)

cod.add_data("""
             Hello World !
             https://openclassrooms.com/fr/courses/4540341-apprenez-a-programmer-en-python/5394261-decouvrez-les-bases-de-la-programmation-avec-python
             """)
cod.make(fit = True)

img = cod.make_image(fill_color = "black", back_color = "white")
img.save("qrcode1.png")
img.show()

print("QR code généré avec succès et enregistré sous le nom 'qrcode1.png'.")