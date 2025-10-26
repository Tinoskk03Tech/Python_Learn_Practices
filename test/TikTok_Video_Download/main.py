import yt_dlp

print("\n📥 Téléchargeur TikTok / Instagram\n")

url = input("🔗 Entrez l'URL de la vidéo : ")

ydl_opts = {
    'outtmpl': '~/Downloads/%(title)s.%(ext)s',
    'progress_hooks': [lambda d: print(f"⏳ {d['_percent_str']} téléchargé...") if d['status'] == 'downloading' else None],
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    print("\n🔍 Récupération des informations...")
    info = ydl.extract_info(url, download=False)
    print(f"🎬 Titre : {info.get('title')}")
    print(f"👤 Auteur : {info.get('uploader')}")
    print(f"📅 Date : {info.get('upload_date')}")
    
    print("\n⬇️ Téléchargement en cours...\n")
    ydl.download([url])
    print("\n✅ Téléchargement terminé !\n")
