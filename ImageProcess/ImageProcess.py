from PIL import Image, ImageEnhance, ImageFilter

def satelite_image_processor(filename):
    img = Image.open(filename)
    print(f"Processing satelite data: {img.size}")

    img = ImageEnhance.Contrast(img).enhance(1.5)
    img = ImageEnhance.Sharpness(img).enhance(1.3)
    print("Enhance image contrast and sharpness")

    grayscale = img.convert('L')
    grayscale.save('grayscale_view.jpg')

    blackened = ImageEnhance.Contrast(grayscale).enhance(2.0)

    blackened.save('Blackened_view.jpg')

    vegetation = ImageEnhance.Color(img).enhance(1.8)
    vegetation.save('vegetation_analysis.jpg')

    print("Created: infrared_view.jpg, thermal_view.jpg, vegetation_analysis.jpg")

    rotated = img.rotate(45, expand=True)

    rotated.save('rotated_filter.jpg')

    ResizedImage = img.resize((800,600))
    print("Resized to 800,600")

    ResizedImage.save('resized_image.jpg')


satelite_image_processor('Davidp image process project.jpg')
