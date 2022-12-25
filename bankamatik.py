#Bankamatik uygulaması

iboHesap = {
    'ad': 'ibrahim seven',
    'hesapNo': '12354678',
    'bakiye': 3000,
    'ekBakiye': 2000
}

erenHesap = {
    'ad': 'ibrahim seven',
    'hesapNo': '12354678',
    'bakiye': 3000,
    'ekBakiye': 2000
}

def paraCekme(hesap,miktar):
    print(f"Merhaba {hesap['ad']}")
    if hesap['bakiye']>= miktar:
        hesap['bakiye']-= miktar
        print("Paranızı alabilirsiniz.")
    else:
        toplam = hesap['bakiye']+hesap['ekBakiye']
        if toplam>=miktar:
            soru = input("ek bakiye kullanmak ister misiniz (e/h)")
            if soru == 'e':
                hesap['bakiye'] = 0
                hesap['ekBakiye'] -= miktar - hesap['bakiye']
                print("ek bakiye kullanarak paranızı alabilirsiniz.")
            else:
                print(f"{hesap['hesapNo']} nolu hesabınızdan {miktar} tutarlı para çekme işlemi başarısız bakiyeniz: {hesap['bakiye']}")
        else:
            print("bakiyeniz ve ek bakiye toplamınız yetersiz")

def bakiyeSorgula(hesap):
    print(f"{hesap['hesapNo']} nolu hesabınızdaki bakiyeniz: {hesap['bakiye']} ek bakiyeniz: {hesap['ekBakiye']}")

bakiyeSorgula(iboHesap)
paraCekme(iboHesap,3000)
bakiyeSorgula(iboHesap)
print("***********")
paraCekme(iboHesap,2000)
bakiyeSorgula(iboHesap)

#dictionary tipinde bi hesap oluşturduğumuz için veriler ram de salanıyor biz bakiyeyi düşürdüğümüzde o verilerden de düşüyor 
#üstteki gibi bakiye sorgulayıp sonra para çekip tekrar bakiye sorguladığımızda bakiyenin eksildiğini
#görürüz.