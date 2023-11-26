import qrcode

img = qrcode.make("BeWeb.DEV")

img.save("Test.png")