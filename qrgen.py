import qrcode

img = qrcode.make("Hello Testing")

img.save("Test.png")