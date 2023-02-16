
def piyoda(ip, fp):
    if fp[0] == ip[0] and fp[1] - 1 == ip[1]:
        return True
    else:
        return False


def rux(ip, fp):
    if fp != ip:
        if fp[0] == ip[0] or fp[1] == ip[1]:
            return True
        else:
            return False
    else:
        return False


def ot(ip, fp):
    if [ip[0] + 1, ip[1] + 2] == fp or [ip[0] + 2, ip[1] - 1] == fp or [ip[0] - 1, ip[1] - 2] or [ip[0] - 2, ip[1] + 1]:
        return True
    else:
        return False


def fil(ip, fp):
    pass


def vazir(ip, fp):
    pass


def qirol(ip, fp):
    pass


def main():
    ip = list(input("Boshlang'ich nuqtani kiriting x,y: ").split(" "))
    fp = list(input("Oxirgi nuqtani kiriting z,t: ").split(" "))
    ip[0] = int(ip[0])
    ip[1] = int(ip[1])
    fp[0] = int(fp[0])
    fp[1] = int(fp[1])

    piece = input("Ro'yxatdagi donalardan birini raqamini tanlang va uni kiriting:\n"
                  "1.Piyoda, 2.Rux , 3.Ot, 4.Fil, 5.Vazir, 6.Qirol: \n")
    piece_name = ""

    can_move = ""

    if piece == '1':
        piece_name = 'piyoda'
        if piyoda(ip, fp):
            can_move = "oladi"
        else:
            can_move = "olmaydi"
    elif piece == '2':
        piece_name = 'rux'
        if rux(ip, fp):
            can_move = "oladi"
        else:
            can_move = "olmaydi"
    elif piece == '3':
        piece_name = 'ot'
        if ot(ip, fp):
            can_move = "oladi"
        else:
            can_move = "olmaydi"
    elif piece == '4':
        piece_name = 'fil'
        if fil(ip, fp):
            can_move = "oladi"
        else:
            can_move = "olmaydi"
    elif piece == '5':
        piece_name = 'vazir'
        if vazir(ip, fp):
            can_move = "oladi"
        else:
            can_move = "olmaydi"
    elif piece == '6':
        piece_name = 'qirol'
        if qirol(ip, fp):
            can_move = "oladi"
        else:
            can_move = "olmaydi"

    print(f"Berilgan boshlang'ich {ip} nuqtadan {piece_name}, {fp} nuqtaga yura {can_move}\n")
    cont = input("O'yinni davom ettirasimi 1.Ha. 2. Yo'q:   ")

    if cont == '1':
        return True
    else:
        print("O'yin uchun rahmat!")
        return False


while main():
    main()
