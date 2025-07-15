# Download this file

def imported() :
    print("\n\nsetup V1.6 [public-version] GitHub repository\n")
    print("Hello!\n")

imported()

def autoInstall_Pygame() :
    import platform

    system = platform.system()
    if system == "Windows" :
        print("Installing pygame")
        import subprocess
        
        pygameInstall = "pip install pygame"
        subprocess.Popen(pygameInstall, shell = True)
    else : 
        print(f"Please install pygame, auto-install doesn't work with {system}")

def autoInstall_colorama() :
    import platform

    system = platform.system()
    if system == "Windows" :
        print("Installing Colorama")
        import subprocess
        
        coloramaInstall = "pip install colorama"
        subprocess.Popen(coloramaInstall, shell = True)
    else :
        print(f"Please install colorama, auto-install doesn't work with {system")


class ask :
    def MissingPygame(self) :
        try : 
            import pygame
            print("Pygame installed")
        except : 
            autoInstall_pygame()
    def MissingColorama(self) :
        try :
            import colorama
            print("Colorama installed")
        except :
            autoInstall_colorama()

class Color :
    def White(self) :
        white = 255, 255, 255
        return white
    def Red(self) :
        red = 255, 0, 0
        return red
    def Black(self) :
        black = 0, 0, 0
        return black
    def Green(self) :
        green = 0, 255, 0
        return green
    def Blue(self) :
        blue = 0, 0, 255
        return blue
    
