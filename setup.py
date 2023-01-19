import cx_Freeze

executables = [cx_Freeze.Executable("main.py")]

cx_Freeze.setup(
    name="Tu hermana 1",
    options={"build_exe": {"packages":["pygame","pygame.mixer","pygame.sndarray"], "include_files":["musica/hola.ogg","musica/bebe.ogg","musica/perdiste.ogg"]}},
    executables=executables
)