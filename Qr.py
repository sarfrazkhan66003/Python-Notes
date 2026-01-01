import qr
import image
qr = qr.Qr(
      version = 20,
      error_correction = qr.constants.ERROR_CORRECT_L,
      box_size = 10,
      border = 4
)
data = 'https://www.instagram.com/the.mohammad.sarfu.___/?hl=en'
qr.add_data(data)
qr.make(fit = True)
img = qr.make_image(fill_color = 'black', back_color = 'white')
img.save('Qr.png')