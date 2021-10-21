
import os
from pytube import YouTube

try:
    newpath = r'Videos Descargados'
    if not os.path.exists(newpath):
        os.makedirs(newpath)

    print("███████╗███╗  ██╗███████╗ █████╗ ")
    print("██╔════╝████╗ ██║╚════██║██╔══██╗")
    print("█████╗  ██╔██╗██║  ███╔═╝██║  ██║")
    print("██╔══╝  ██║╚████║██╔══╝  ██║  ██║")
    print("███████╗██║ ╚███║███████╗╚█████╔╝")
    print("╚══════╝╚═╝  ╚══╝╚══════╝ ╚════╝ ")
    print("Programa echo por EnzooSP#7246")
    print("Descarga videos de youtube de forma rapida y en alta calidad")

    link = input("Link del video: ")
    video = YouTube(link).streams.filter(res="720p").first()
    print("Descargando...")
    video.download(r'Videos Descargados')
    print("Descargado !")

except SyntaxError:
    print("Ocurrio un error, Porfavor reinicie el programa")
