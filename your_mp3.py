from os import remove
import pytube
from pytube import Playlist
import tkinter
import tkinter.filedialog
import shutil
from moviepy.video.io.VideoFileClip import VideoFileClip



def crear_ventana(Titulo, descripcion):
    frame = tkinter.Tk()
    frame.title(Titulo)
    frame.geometry('400x300')
    frame.iconbitmap("ico.ico")
    frame.columnconfigure(0, weight=1)

# Así es el code del tkinter es ctrl +  C y ctrl + V xd

    def printInput():
        global inp
        inp = inputtxt.get(1.0, "end-1c")
        lbl.config(text="Provided Input: "+inp)
        frame.destroy()


# TextBox Creation
    inputtxt = tkinter.Text(frame, height=3, width=40)

    inputtxt.pack(padx=30, pady=30, ipadx=30, ipady=30)

# Button Creation
    printButton = tkinter.Button(frame, text="Aceptar", command=printInput)
    printButton.pack(padx=5, pady=5, ipadx=5, ipady=5)

# Label Creation
    lbl = tkinter.Label(frame, text=descripcion)
    lbl.pack()
    frame.mainloop()

# ----------------------------------------------------------------------------------------------


crear_ventana("Introduce una url", "Asegurate de poner bien el link y no poner otra cosa."
              + " \n También puedes poner una playlist y tener todos los vídeos o canciones.")

playlist = Playlist(inp)
video = inp

crear_ventana("¿Es una playlist?",
              "Solo pon Si o No , como pongas otra cosa no va a funcionar e.e")

while inp.lower() != "si" and inp.lower() != "no":

    crear_ventana("¿Es una playlist?",
                  "Te dije que solo pongas Si o No , como pongas otra cosa no va a funcionar e.e")

# -----------------------------------------------------------------------------------------------

if inp.lower() == "no":

    video = pytube.YouTube(video)

    crear_ventana("¿Quieres borrar el video original?",
              "Solo pon Si o No , como pongas otra cosa no va a funcionar e.e")

    while inp.lower() != "si" and inp.lower() != "no":

        crear_ventana("¿Quieres borrar el video original?", "Solo pon Si o No , como pongas otra cosa no va a funcionar e.e")

    print("Okay ahora introduce la carpeta que quieres para guardar el archivo (Saldrá una ventana escondida así que minimiza lo que tengas)")

    # preguntar por ruta

    root = tkinter.Tk()  # esto se hace solo para eliminar la ventanita de Tkinter
    root.withdraw()  # ahora se cierra
    # abre el explorador de archivos y guarda la ruta
    file_path = tkinter.filedialog.askdirectory()
    try:
        print("Se está descargando el vídeo un momentito.")

        file = video.streams.first().download(file_path)

        print("...")
        print("Okay todo correcto!.")
        print("Ahora vamos a convertir el vídeo en mp3...")

        mp3 = VideoFileClip(file)

        nombre_video = file.split("\\")

        nombre_audio = nombre_video[1].replace("mp4", "mp3")

        mp3.audio.write_audiofile(nombre_audio)

        shutil.move(nombre_audio, file_path + ("\\" + nombre_audio))

        mp3.close()
        print("Hecho!")

    except:
        print("Hubo un error :c...")

    while True:

        if(inp.lower() == "si" or inp.lower() == "s"):
            remove(nombre_video[0] + "/" + nombre_video[1])
            break
        elif(inp.lower() == "no" or inp.lower() == "n"):
            break
        else:
            print(
                "No has elegido una opción correcta... Tienes que elegir Si o No (Puedes poner S o N').")

elif inp.lower() == "si":

    crear_ventana("¿Quieres borrar los videos originales?",
              "Solo pon Si o No , como pongas otra cosa no va a funcionar e.e")

    while inp.lower() != "si" and inp.lower() != "no":

        crear_ventana("¿Quieres borrar los videos originales?", "Solo pon Si o No , como pongas otra cosa no va a funcionar e.e")

    print("Okay ahora introduce la carpeta que quieres para guardar el archivo (Saldrá una ventana escondida así que minimiza lo que tengas)")

    # preguntar por ruta

    root = tkinter.Tk()  # esto se hace solo para eliminar la ventanita de Tkinter
    root.withdraw()  # ahora se cierra
    # abre el explorador de archivos y guarda la ruta
    file_path = tkinter.filedialog.askdirectory()
    try:
        

        for video_i in playlist.videos:
             print("Se está descargando el vídeo un momentito.")
             video_i.streams.first().download()

             file = video_i.streams.first().download(file_path)

             print("...")
             print("Okay todo correcto!.")
             print("Ahora vamos a convertir el vídeo en mp3...")

             mp3 = VideoFileClip(file)

             nombre_video = file.split("\\")

             nombre_audio = nombre_video[1].replace("mp4", "mp3")

             mp3.audio.write_audiofile(nombre_audio)

             shutil.move(nombre_audio, file_path + ("\\" + nombre_audio))

             mp3.close()
             print("Hecho!")

            

             while True:
                 print("Eliminando...")
                 if(inp.lower() == "si" or inp.lower() == "s"):
                     remove(nombre_video[0] + "/" + nombre_video[1])
                     remove(nombre_video[1])
                     break
                 elif(inp.lower() == "no" or inp.lower() == "n"):
                    remove(nombre_video[1])
                    break
                 else:
                     print("No has elegido una opción correcta... Tienes que elegir Si o No (Puedes poner S o N').")
    except:
        print("Hubo un error :c...")