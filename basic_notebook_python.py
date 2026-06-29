kaydedilennot = ""
while True:

    print("****Not Defterine Hoş Geldiniz****")
    print("**********[1]Not Gir**************")
    print("***[2]Kaydedilen Notu Görüntüle***")
    print("***********[3]Çıkış***************")

    secim = input("Yapacağınız İşlemi Tuşlayınız: ")
    if secim.strip() == "":
        continue

    if secim == "1":
        kaydedilennot = input("Notunuzu Giriniz: ")
        print("n—————————————————————————————\n")
 
    elif secim == "2":
         if kaydedilennot == "":
             print("Kaydedilmiş Notunuz Bulunmamaktadır: ")
             print("\n——————————————————————————————\n")
         else:
             print("Notunuz: ")
             print(kaydedilennot)
             print("\n——————————————————————————————\n")
             
    
    elif secim == "3":
        break
    
    else:
        print("Hatalı Tuşlama Yaptınız")
        print("\n———————————————————\n")