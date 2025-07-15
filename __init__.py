def imported() :
    print("\n\nsetup V1 [public-version] GitHub repository\n")
    print("Hello!\n")

imported()

class ask :
    def MissingPygame(self) :
        try : 
            import pygame
            print("Pygame installed")
        except : 
            print("Installing pygame")
            import subprocess

            pygameInstall = "pip install pygame"
            subprocess.Popen(pygameInstall, shell = True)
    def MissingColorama(self) :
        try :
            import colorama
            print("Colorama installed")
        except :
            print("Installing Colorama")
            import subprocess

            coloramaInstall = "pip install colorama"
            subprocess.Popen(coloramaInstall, shell = True)


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
    