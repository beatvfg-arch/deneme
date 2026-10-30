from pathlib import Path

isim = input("İsminiz: ").strip()
soyisim = input("Soyisminiz: ").strip()
dogum_yili = input("Doğum yılınız: ").strip()

sifre = isim[0].upper() + soyisim[0].upper() + dogum_yili[-2:] + isim[:2].lower() + soyisim[:2].lower()
print("Şifreniz:", sifre)

dosya = Path(__file__).with_name("gizsiz.txt")
with open(dosya, "a", encoding="utf-8") as sk:
    sk.write(sifre + "\n")
saş = input("Verilen şifreyi giriniz: ")
if saş == sifre:
    print ("sifre doğru")
else:
    print("Şifre yanlış")
    raise SystemExit("Program kapanıyor...")
if sifre == "BT13betı":
    print("Yönetici")
else:
    print ("kullanıcı")

    
if sifre == "BT13betı":
    print("Tüm yetkilere sahipsiniz")
else:
    print("Sınırlı yetkilere sahipsiniz")
yas = input("yaşınızı giriniz: ")
if int(yas) > 18:
    print ("giriş yapabilirsiniz")
    raise SystemExit("Program kapanıyor...")
else:
    print ("ebeveyn onayı gereklidir")
eo = input("ebeyin onayı için onay yazınız: ")
if eo =="onay":
    print ("giriş yapabilirsiniz")
