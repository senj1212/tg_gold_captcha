from io import BytesIO

from captcha.image import ImageCaptcha
from random import choice, randint
import string


def get_random_captcha(uid):
    length = randint(8, 12)
    characters = string.ascii_letters + string.digits
    l_patterns = [''.join(choice(characters) for _ in range(length)) for i in range(0, 8)]
    pattern = choice(l_patterns)
    image_captcha = ImageCaptcha(width=300, height=200)
    file_img = image_captcha.generate_image(pattern)
    image_io = BytesIO()

    file_img.save(image_io, 'JPEG')

    image_io.seek(0)

    return pattern, image_io, l_patterns
