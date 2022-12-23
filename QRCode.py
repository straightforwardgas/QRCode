# Creates QR code


import qrcode

def main():

    # Data to be encoded
    data = 'QR Code using make() function'

    # Encoding data using make() function
    img = qrcode.make(data)

    # Saving as an image file
    img.save('QRCode1.png')


    return


#auto run 'main' function
if __name__ == "__main__":
    main()
