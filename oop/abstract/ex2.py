from abc import ABC, abstractmethod

class Image(ABC):
    @abstractmethod
    def load_image(self, filename):
        pass

    @abstractmethod
    def save_image(self, filename):
        pass

class Bitmap(Image):
    def __init__(self):
        super()

    def load_image(self,filename):
        print(f'loading bitmap file {filename}')

    def save_image(self,filename):
        print(f'saving bitmap file {filename}')

class Jpeg(Image):
    def __init__(self):
        super()

    def load_image(self,filename):
        print(f'loading jpeg file {filename}')

    def save_image(self,filename):
        print(f'saving jpeg file {filename}')


if __name__ == "__main__":
    bitmap1 = Bitmap()
    bitmap1.save_image("kku.bmp")
    bitmap1.load_image("kku.bmp")
    jpeg1 = Jpeg()
    jpeg1.save_image("en.jpg")
    jpeg1.load_image("en.jpg")
