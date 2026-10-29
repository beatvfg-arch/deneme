from pathlib import Path

i = input("İsminiz: ").strip()
s = input("Soyisminiz: ").strip()
dogum_yili = input("Doğum yılınız: ").strip()
sifre = i[0].upper() + s[0].upper() + dogum_yili[-2:] + i[:2].lower() + s[:2].lower()
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
    print("Tüm yetkilere sahipsiniz")
else:
    print("Sınırlı yetkilere sahipsiniz")
yas = input("yaşınızı giriniz: ")
if int(yas) > 18:
    print ("giriş yapabilirsiniz")
else:
    print ("ebeveyin onayı gereklidir")
eo = input("ebeveyin onayı için onay yazınız: ")
if eo =="onay":
    print ("giriş yapabilirsiniz")
hd = input("hangi zorlukta kaynak istiyorsunuz.(yüzde olarak)")
if int(hd) >0 and int(hd)<50:
    print("bilfen yayıncılık")
if int(hd)> 50 and int(hd)< 75:
    print("hız yayıncıkık")
if int (hd) > 75:
    print ("mozaik yayıncılık / ankara yayıncıkık")
input("çıkmak için enter tuşuna basınız...")
raise SystemExit("Program kapanıyor..." )

