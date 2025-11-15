
from PIL import Image

import os
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r"C:\Users\DELL\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"


def run_ocr():
    print("\n=== OCR (image -> texte) ===")

    # 🔹 Demande du chemin d'image
    path = input("Fichier : ").strip()
    lang = input("Langue OCR (ex: fra ou eng) [Entrée = eng] : ").strip() or "eng"

    # 🔹 Vérifie si le chemin est vide
    if not path:
        print("❌ Chemin de fichier vide.")
        return

    # 🔹 Vérifie si le fichier existe avant d’essayer de l’ouvrir
    if not os.path.isfile(path):
        print(f"❌ Le fichier '{path}' est introuvable.")
        return

    try:
        # 🔹 Ouverture de l'image
        img = Image.open(path)
        print("✅ Fichier trouvé et ouvert avec succès !")

        # 🔹 Lancer l’OCR
        text = pytesseract.image_to_string(img, lang=lang)

        # 🔹 Résultat
        if text.strip():
            print("\n🧾 Texte détecté :\n")
            print(text.strip())
        else:
            print("⚠️ Aucun texte détecté dans l’image.")

    except Exception as e:
        print(f"❌ Erreur OCR ou ouverture de fichier : {e}")


