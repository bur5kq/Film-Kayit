# Kullanıcının izlediği filmleri kaydettiği bir program
import json
import os
import time


class FilmArsiv:
    # Kullanıcıdan film ve tarih bilgisi al
    def __init__(self, film, date):
        self.film = film
        self.date = date

    # Nesne bilgilerini döndüren metot yani nesneyi cagırdıgında bu sekilde gelicek
    def __str__(self):
        return f"İzlenen Film: {film1.film} \nİzlenen Filmin Tarihi: {film1.date}"


# kullanıcı daha önce film kaydettiyse kayıtlı filmleri gösterir
if os.path.exists("data_film.json"):
    print("Daha önce kaydedilmiş filmler:")
    with open("data_film.json", "r", encoding="utf-8") as f:
        data_film = json.load(f)
    for i, kayit in enumerate(data_film, start=1):
        print(f"{i}. Film: {kayit['film']} | Tarih: {kayit['date']}")

    print()
    input("Devam etmek için Enter'a basın...") # programı kapatır
    print("Program sonlandırıldı.")
    time.sleep(2)
        
    ## programa kayıt edilen filmleri düzenleme veya çıkarma bulunmamaktadır kullanıcı json dosyasını manuel olarak düzenleyebilir veya silebilir

else:
    print("Film kaydetme programına hoş geldiniz!")
    print("İzlediğiniz filmleri ve tarihlerini kaydedebilirsiniz.")
    print("!!! programa kayıt edilen filmleri düzenleme veya çıkarma bulunmamaktadır kullanıcı json dosyasını manuel olarak düzenleyebilir veya silebilir ancak herhangi bir hatalı kaydetme durumunda program uzerinden kayıtı iptal edebilirsiniz")
    data_film = []
    while True:

        # Kullanıcıdan film ve tarih bilgisi al
        film_bilgi = input("İzlediğiniz filmi girin: ")
        tarih_bilgi = input("İzlediğiniz tarihi girin: ")

        film1 = FilmArsiv(film_bilgi, tarih_bilgi) #class ile nesne olusturduk
        print(film1) # nesneyi cagırdık
        print()
        # onaylama kısmı
        print("Kayıt işlemini onaylıyor musunuz? (E/H)") 
        onay = input("-> ").lower()

        if onay != "e" and onay != "evet": # onaylanmazsa programı kapatır
            print("Kayıt işlemi iptal edildi.")
            time.sleep(2)
            os.system("cls")
        else:
            # Verileri JSON dosyasına kaydet
            data_film.append({"film": film1.film, "date": film1.date})
            print("Film bilgisi kaydedildi.")
            print()
            # Film bilgisi kayıt edildikten sonra kullanıcı tekrardan film kaydetmek isterse
            print("Eklemek istediğiniz başka bir film var mı? (E/H)")
            ekle = input("-> ").lower()
            if ekle != "h" and ekle != "hayır":
                while True:
                    # Kullanıcıdan tekrar film ve tarih bilgisi al
                    film1_bilgi = input("İzlediğiniz filmi girin: ")
                    tarih1_bilgi = input("İzlediğiniz tarihi girin: ")

                    # daha önce class ile olusturdugumuz nesnenin bilgilerini degistiriyoruz
                    # aslında bu sekilde kullanmak dogru degil ama classi kaldirmadigim icin boyle kullandım
                    film1.film = film1_bilgi # classdaki nesnenin bilgilerini degistiriyoruz
                    film1.date = tarih1_bilgi
                    print(film1)
                    print()
                    print("Kayıt işlemini onaylıyor musunuz? (E/H)")
                    onay = input("-> ").lower()
                    
                    if onay != "e" and onay != "evet":
                        print()
                        print("Kayıt işlemi iptal edildi.")
                        with open("data_film.json", "w", encoding="utf-8") as f: 
                            json.dump(data_film, f, ensure_ascii=False, indent=4)
                        print("Eklenen filmler:")
                        for i, kayit in enumerate(data_film, start=1): # eklenen filmleri numaralandırarak gösterir
                            print(f"{i}. Film: {kayit['film']} | Tarih: {kayit['date']}")

                        input("Devam etmek için Enter'a basın...") # programı kapatır
                        print("Program sonlandırıldı.")
                        time.sleep(1.5)
                        exit()
                    else:
                        # Verileri JSON listesine ekle
                        data_film.append(
                            {"film": film1_bilgi, "date": tarih1_bilgi})
                        print("Film bilgisi kaydedildi.")
                    print("Eklemek istediğiniz başka bir film var mı? (E/H)")
                    ekle1 = input("-> ").lower()
                    if ekle1 != "h" and ekle1 != "hayır":
                        continue     
                    else:
                        with open("data_film.json", "w", encoding="utf-8") as f:
                            json.dump(data_film, f, ensure_ascii=False, indent=4)
                        print("Eklenen filmler:")
                        for i, kayit in enumerate(data_film, start=1):
                            print(f"{i}. Film: {kayit['film']} | Tarih: {kayit['date']}")
                        print("Program sonlandırıldı.")
                        exit()
            else:
                with open("data_film.json", "w", encoding="utf-8") as f:
                    json.dump(data_film, f, ensure_ascii=False, indent=4)
                print("Eklenen filmler:")
                for i, kayit in enumerate(data_film, start=1):
                    print(f"{i}. Film: {kayit['film']} | Tarih: {kayit['date']}")
                input("Devam etmek için Enter'a basın...") # programı kapatır
                print("Program sonlandırıldı.")
                time.sleep(1.5)
                exit()