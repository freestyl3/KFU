import random

import numpy as np
from PIL import Image, ImageFilter

def tile(*images, vertical=False):
    width, height = images[0].width, images[0].height
    tiled_size = (
        (width, height * len(images))
        if vertical
        else (width * len(images), height)
    )
    tiled_img = Image.new(images[0].mode, tiled_size)
    row, col = 0, 0
    for image in images:
        tiled_img.paste(image, (row, col))
        if vertical:
            col += height
        else:
            row += width

    return tiled_img

def erode(cycles, image: Image):
    for _ in range(cycles):
         image = image.filter(ImageFilter.MinFilter(3))
    return image


def dilate(cycles, image: Image):
    for _ in range(cycles):
         image = image.filter(ImageFilter.MaxFilter(3))
    return image

def module_1():
    path = "C:\\Users\\Admin\\Documents\\Python\\KFU\\PythonApps\\images\\"
    filename = path + "4.png"
    with Image.open(filename) as img:
        img.load()

    print(type(img))
    print(isinstance(img, Image.Image))
    # img.show()

    print(img.format)
    print(img.size)
    print(img.mode)

    cropped_img = img.crop((805, 575, 875, 655))
    print(cropped_img.size)
    cropped_img.save(path + "cropped.png")
    # cropped_img.show()

    low_res_img = img.resize((img.width // 4, img.height // 4))
    reduced_img = img.reduce(4)
    low_res_img.save(path + "low_res.png")
    reduced_img.save(path + "reduced.png")
    # low_res_img.show()
    # reduced_img.show()

    # img.thumbnail((100, 100))
    # img.save(path + "thumbnail.png")

    converted_img = img.transpose(Image.Transpose.FLIP_TOP_BOTTOM)
    transposed_img = img.transpose(Image.Transpose.TRANSPOSE)
    transversed_img = img.transpose(Image.Transpose.TRANSVERSE)
    converted_img.save(path + "converted.png")
    transposed_img.save(path + "transposed.png")
    transversed_img.save(path + "transversed.png")

    rotated_img = img.rotate(random.randint(0, 360))
    expanded_rotated_img = img.rotate(random.randint(0, 360), expand=True)
    rotated_img.save(path + "rotated.png")
    expanded_rotated_img.save(path + "expanded_rotated.png")

def module_2():
    path = "C:\\Users\\Admin\\Documents\\Python\\KFU\\PythonApps\\images\\path2\\"
    filename = path + "1.jpg"
    with Image.open(filename) as img:
        img.load()

    cmyk_img = img.convert("CMYK")
    gray_img = img.convert("L")
    cmyk_img.save(path + "cmyk.jpg")
    gray_img.save(path + "gray.jpg")
    print(img.getbands())
    print(cmyk_img.getbands())
    print(gray_img.getbands())

    red, green, blue = img.split()
    print(red)
    print(red.mode)

    zero = red.point(lambda _: 0)

    red_merge = Image.merge("RGB", (red, zero, zero))
    green_merge = Image.merge("RGB", (zero, green, zero))
    blue_merge = Image.merge("RGB", (zero, zero, blue))
    red_merge.save(path + "red.jpg")
    green_merge.save(path + "green.jpg")
    blue_merge.save(path + "blue.jpg")

    tiled_image = tile(red_merge, green_merge, blue_merge)
    tiled_image.save(path + "tiled.jpg")

def module_3():
    path = "C:\\Users\\Admin\\Documents\\Python\\KFU\\PythonApps\\images\\"
    filename = path + "4.png"
    with Image.open(filename) as img:
        img.load()

    img.filter(ImageFilter.BLUR).save(path + "blur.png")

    img.filter(ImageFilter.BoxBlur(5)).save(path + "box_blur_small.png")
    img.filter(ImageFilter.BoxBlur(20)).save(path + "box_blur_big.png")
    img.filter(ImageFilter.GaussianBlur(3)).save(path + "gaussian_blur.png")

    img.filter(ImageFilter.SHARPEN).save(path + "sharp.png")
    img.filter(ImageFilter.SMOOTH).save(path + "smooth.png")

    tile(
        img.filter(ImageFilter.SHARPEN),
        img,
        img.filter(ImageFilter.SMOOTH),
        vertical=True
    ).save(path + "tiled.png")

    img.convert("L").filter(ImageFilter.FIND_EDGES).save(path + "edges.png")
    img.convert("L").filter(ImageFilter.FIND_EDGES).filter(ImageFilter.SMOOTH).save(path + "smooth_edges.png")
    img.convert("L").filter(ImageFilter.EDGE_ENHANCE).save(path + "edge_enchanced.png")
    img.convert("L").filter(ImageFilter.EMBOSS).save(path + "emboss.png")

def module_4():
    path = "C:\\Users\\Admin\\Documents\\Python\\KFU\\PythonApps\\images\\path2\\"
    cat_path = path + "3.jpg"

    with Image.open(cat_path) as cat_img:
        cat_img.load()

    cat_img_gray = cat_img.convert("L")
    red, green, blue = cat_img.split()

    threshold = 85
    cat_img_threshold = blue.point(
        lambda x: 255 if x > threshold else 0
    )
    cat_img_threshold = cat_img_threshold.point(
        lambda x: 255 if x == 0 else 0
    )

    cat_img_threshold.show()
    step_1 = dilate(10, cat_img_threshold)
    step_2 = erode(20, step_1)
    step_3 = dilate(20, step_2)
    step_4 = erode(24, step_3)
    cat_mask = dilate(10, step_4)

    cat_mask = cat_mask.filter(ImageFilter.BoxBlur(20))
    cat_mask.save(path + "cat_mask.jpg")

    blank = cat_img.point(lambda _: 0)
    cat_segmented = Image.composite(cat_img, blank, cat_mask)
    cat_segmented.save(path + "cat_segmented.jpg")

    filename_room = path + '279.jpg'
    with Image.open(filename_room) as img_room:
        img_room.load()

    img_room.paste(
        cat_img.resize((int(cat_img.width / 1.5), int(cat_img.height // 1.5))),
        (2024, 2309),
        cat_mask.resize((int(cat_mask.width // 1.5), int(cat_mask.height // 1.5))),
    )

    img_room.save(path + "img_room.jpg")

    logo_path = path + "GitHub-Logo.png"
    with Image.open(logo_path) as img_logo:
        img_logo.load()

    img_logo = img_logo.convert('L')
    img_logo = img_logo.resize((img_logo.width // 3, img_logo.height // 3))
    img_logo = img_logo.filter(ImageFilter.CONTOUR)
    img_logo = img_logo.point(lambda x: 0 if x == 255 else 255)
    img_logo = img_logo.crop((1, 1, img_logo.width - 1, img_logo.height - 1))
    img_logo.save(path + "logo_contour.png")

    centerX = img_room.width // 2
    centerY = img_room.height // 2
    img_room.paste(img_logo, (centerX - img_logo.width // 2, centerY - img_logo.height // 2), img_logo)
    img_room.save(path + 'img_room_with_logo.jpg')

def module_5():
    path = "C:\\Users\\Admin\\Documents\\Python\\KFU\\PythonApps\\images\\path3\\"
    img_path = path + "4.jpg"
    with Image.open(img_path) as img:
        img.load()

    # img = img.convert('RGB')

    left = img.crop((80, 0, 1455, img.height))
    right = img.crop((1545, 0, 2920, img.height))

    print(right.size)
    left_array = np.asarray(left)
    right_array = np.asarray(right)

    difference_array = right_array - left_array

    difference = Image.fromarray(difference_array)
    difference.show()

def module_6():
    square = np.zeros((600, 600))
    square[200:400, 200:400] = 255
    square_img = Image.fromarray(square)
    square_img.convert('L')
    # square_img.show()

    red = np.zeros((600, 600))
    green = np.zeros((600, 600))
    blue = np.zeros((600, 600))
    red[150:350, 150:350] = 255
    green[200:400, 200:400] = 255
    blue[250:450, 250:450] = 255

    red_img = Image.fromarray(red).convert('L')
    green_img = Image.fromarray(green).convert('L')
    blue_img = Image.fromarray(blue).convert('L')

    square_img = Image.merge('RGB', (red_img, green_img, blue_img))
    # square_img.show()

    square_animation = []
    for offset in range(0, 100, 2):
        print(offset)
        red = np.zeros((600, 600))
        green = np.zeros((600, 600))
        blue = np.zeros((600, 600))
        red[101 + offset : 301 + offset, 101 + offset : 301 + offset] = 255
        green[200:400, 200:400] = 255
        blue[299 - offset : 499 - offset, 299 - offset : 499 - offset] = 255

        red_img = Image.fromarray(red).convert('L')
        green_img = Image.fromarray(green).convert('L')
        blue_img = Image.fromarray(blue).convert('L')

        square_animation.append(
            Image.merge('RGB', (red_img, green_img, blue_img))
        )

        square_animation[0].save(
            'C:\\Users\\Admin\\Documents\\Python\\KFU\\PythonApps\\images\\animation.gif',
            save_all=True, append_images=square_animation[1:]
        )

def main():
    module_5()

if __name__ == '__main__':
    main()