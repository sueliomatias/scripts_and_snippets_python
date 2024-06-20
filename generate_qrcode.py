import qrcode
from pyzbar.pyzbar import decode
from PIL import Image

# função para gerar o QR Code
def gerar_qrcode(dados, nome_arquivo):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(dados)
    qr.make(fit=True)

    imagem = qr.make_image(fill_color="black", back_color="white")
    imagem.save(nome_arquivo)

# função para decodificar o QR Code
def decodificar_qrcode(nome_arquivo):
    imagem = Image.open(nome_arquivo)
    dados = decode(imagem)
    return dados

# exemplo de uso
dados = "https://www.github.com"
nome_arquivo = "qrcode.png"
gerar_qrcode(dados, nome_arquivo)
print("QR Code gerado com sucesso!")
decodificar_qrcode(nome_arquivo)