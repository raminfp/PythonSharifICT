from PIL import Image

size = (500, 500)
img = Image.open("1.png")
new_img = img.resize(size)
# new_img.show()
print(img.format)
# print(new_img.size)
new_img.save("new_image.png")
