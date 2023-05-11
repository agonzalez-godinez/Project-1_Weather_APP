from gui import *


def main():
    window = Tk()
    window.geometry("440x600")
    window.resizable(False, False)
    window.title('Weather API Project')
    GUI(window)
    window.mainloop()


if __name__ == '__main__':
    main()
