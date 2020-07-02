import pyqrcode

def createQRpng(url,name):
    QR = pyqrcode.create(url)
    QR.png(name+'.png', scale = 6)

if __name__ == "__main__":
    # url = pyqrcode.create('https://www.google.com')
    # url.png('qr.png')
    # url.show()
    createQRpng('https://www.google.com','test')