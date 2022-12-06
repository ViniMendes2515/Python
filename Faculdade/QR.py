import qrcode
import getpass


def wifi_code(ssid, hidden, authentication_type, password=None):

    hidden = 'true' if hidden else 'false'
    if authentication_type in ('WPA', 'WEP'):
        if password is None:
            raise TypeError('For WPA and WEP, password should not be None.')
        return 'WIFI:T:{type};S:{ssid};P:{password};H:{hidden};;'.format(
            type=authentication_type, ssid=ssid, password=password, hidden=hidden
        )
    elif authentication_type == 'nopass':
        if password is not None:
            raise TypeError('For nopass, password should be None.')
        return 'WIFI:T:nopass;S:{ssid};H:{hidden};;'.format(
            ssid=ssid, hidden=hidden
        )
    raise ValueError(
        'Unknown authentication_type: {!r}'.format(authentication_type))


def wifi_qrcode(ssid, hidden, authentication_type, password=None, **kwargs):
    return qrcode.make(wifi_code(ssid, hidden, authentication_type, password), **kwargs).get_image()


def main():
    while True:
        ssid = input("SSID: ")
        if ssid == "":
            print("Entrada inválida!")
        else:
            break

    while True:
        hidden = input("A rede é invisível (default is false)?: ").lower()
        if hidden in ['yes', 'y', 'true', 't']:
            hidden = True
            break
        elif hidden in ['', 'no', 'n', 'false', 'f']:
            hidden = False
            break
        else:
            print("Entrada inválida!")

    while True:
        print("Authentication types: WPA/WPA2, WEP, nopass")
        authentication_type = input("Tipo de autenticação (default is WPA/WPA2): ").lower()
        if authentication_type in ['', 'wpa2', 'wpa', 'wpa/wpa2', 'wpa2/wpa']:
            authentication_type = 'WPA'
            break
        elif authentication_type == 'wep': 
            authentication_type = 'WEP'
            break
        elif authentication_type == 'nopass':
            authentication_type = 'nopass'
            break
        else:
            print("Entrada inválida!")

    while True:
        if authentication_type == 'nopass':
            password = None
            break
        password = getpass.getpass("Senha: ")
        if password == "":
            print("Senha inválida!")
        else:
            break
    qrcode = wifi_qrcode(ssid, hidden, authentication_type, password)
    qrcode.save(ssid + '.png')
    print("O QRCODE foi armazenado no diretório atual")


if __name__ == '__main__':
    main()
