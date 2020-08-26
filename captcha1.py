from captcha.image import ImageCaptcha
# from captcha.audio import AudioCaptcha

image = ImageCaptcha()
# audio = AudioCaptcha()

# data = audio.generate('abcd')
# audio.write('abcd','1.wav')

data = image.generate('abcd')
image.write('abcd','captcha.png')
