import qrcode

class MyQR:
    def __init__(self, size: int, padding: int):
        self.qr = qrcode.QRCode(box_size=size, border=padding)

    def create_qr(self, file_name: str, fg: str, bg: str):
        user_input: str = input('Enter text:\n ')

        try:
            self.qr.add_data(user_input)
            qr_image = self.qr.make_image(fill_color=fg, back_color=bg)
            qr_image.save(file_name)

            print(f'Successfully created! ({file_name})')

        except Exception as e:
            print(f'Error: {e}')


def main(title: str):
    myqr = MyQR(size=30, padding=2)
    myqr.create_qr(f'{title}',
                   fg='black',
                   bg='white', )


if __name__ == '__main__':
    user_title: str = input('Name Your New QRcode:\n') + '.png'
    main(user_title)
