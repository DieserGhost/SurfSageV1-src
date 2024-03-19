from cx_Freeze import setup, Executable

setup(
    name="SurfSage Browser Alpha",
    version="1.0",
    description="A Real Surf Browser",
    executables=[Executable("Surfsage.py", icon="surfsage.ico")]
)