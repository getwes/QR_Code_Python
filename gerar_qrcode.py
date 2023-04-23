#importando
import qrcode

imagem = qrcode.make("https://github.com/getwes")
imagem.save("primeiro_qrcode.jpg")