from pytube import YouTube

# Ingresa la URL del video de YouTube que deseas descargar
def DescargarVideos(url):
    
    
    yt = YouTube(url)

    yt.streams.get_highest_resolution().download()


DescargarVideos("PONE_LA_URL_DEL_VIDEO")



