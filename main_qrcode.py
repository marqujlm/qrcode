import streamlit as st
import qrcode
from PIL import Image
import os

st.set_page_config(
    page_title="Gerador de QR CODE - code.py Programação",
    page_icon="logo.png",
    layout="centered",
    initial_sidebar_state="auto",
    menu_items={
        'Get Help': 'https://www.codepy.com.br',
        'Report a bug': "https://www.codepy.com.br",
        'About': "Gerador de QR CODE desenvolvido por code.py Programação"
    }
)


st.image('logo.png')

st.title('Gerador de QR CODE')
st.subheader('code.py Programação')
st.markdown('')

option = st.selectbox(
    'Deseja adicionar uma imagem no QR CODE?',
    ('Sim', 'Não'))

if option == 'Sim':
    st.markdown('Insira uma imagem no QR CODE:')

    arquivo = st.file_uploader("Escolha o arquivo")

    url = st.text_input('Insira aqui o URL para o QR CODE:')
    # taking url or text
    qr_code = st.text_input('Insira o nome do seu QR CODE:')

    color = st.color_picker('Escolha a cor do QR CODE:', '#000000')

    if st.button('Gerar QR CODE'):
        Logo_link = arquivo

        logo = Image.open(Logo_link)

        # taking base width
        basewidth = 100

        # adjust image size
        wpercent = (basewidth / float(logo.size[0]))
        hsize = int((float(logo.size[1]) * float(wpercent)))
        logo = logo.resize((basewidth, hsize), Image.LANCZOS)
        QRcode = qrcode.QRCode(
            error_correction=qrcode.constants.ERROR_CORRECT_H
        )

        # adding URL or text to QRcode
        QRcode.add_data(url)

        # generating QR code
        QRcode.make()

        # taking color name from user
        QRcolor = color

        # adding color to QR code
        QRimg = QRcode.make_image(
            fill_color=QRcolor, back_color="white").convert('RGB')

        # set size of QR code
        pos = ((QRimg.size[0] - logo.size[0]) // 2,
               (QRimg.size[1] - logo.size[1]) // 2)
        QRimg.paste(logo, pos)

        # save the QR code generated
        QRimg.save(f'{qr_code}.png')

        st.write('QR CODE gerado com sucesso!')

        with open(f'{qr_code}.png', "rb") as file:
            btn = st.download_button(
                label="Download QR CODE",
                data=file,
                file_name=f'{qr_code}.png',
                mime="image/png"
            )
        os.remove(f'{qr_code}.png')
else:
    url = st.text_input('Insira aqui o URL para o QR CODE:')
    # taking url or text
    qr_code = st.text_input('Insira o nome do seu QR CODE:')

    color = st.color_picker('Escolha a cor do QR CODE:', '#000000')

    if st.button('Gerar QR CODE'):
         # taking base width
        basewidth = 100

        # adjust image size
        QRcode = qrcode.QRCode(
            error_correction=qrcode.constants.ERROR_CORRECT_H
        )

        # adding URL or text to QRcode
        QRcode.add_data(url)

        # generating QR code
        QRcode.make()

        # taking color name from user
        QRcolor = color

        # adding color to QR code
        QRimg = QRcode.make_image(
            fill_color=QRcolor, back_color="white").convert('RGB')

        # save the QR code generated
        QRimg.save(f'{qr_code}.png')

        st.write('QR CODE gerado com sucesso!')

        with open(f'{qr_code}.png', "rb") as file:
            btn = st.download_button(
                label="Download QR CODE",
                data=file,
                file_name=f'{qr_code}.png',
                mime="image/png"
            )
        os.remove(f'{qr_code}.png')

