#Obsesif Kompulsif Bozukluk

"""Bir rehabilitasyon merkezinde çalıştığınızı düşünün.Obsesif-kompulsif bozukluklardan
muzdarip hastalar olsun. Bu hastalar her gün bir blogda günlük planlarını yazması
isteniyor.Program bazı anahtar kelimeleri arayarak hastaları gözetim altında tutacak.
Bu kelimeler şunlar:
alışveriş, tekrar, kumar, içki, bahis, oyun, para
Eğer bu kelimelerden herhangi biri blog girdilerinde geçiyorsa ekrana şunu yazdır:
"Bu konuda gerçekten biriyle konuşmanız gerekiyor, veya".
Ve sonrasında daha önceden belirlenmiş ve bir listede tutulan öneri listesinden rastgele
bir öneri sunmasını istiyoruz
Diğer durumda ekrana şunu yazdırabilirsiniz:
"Bloğunuzu güncellediğiniz için teşekkürler."
"""
import random
from random import randint

okb=["alışveriş","tekrar","kumar","içki","bahis","oyun","para"]
blog=input("Bugünün günlüğünü yazınız:")
yeni_blog=blog.split()
n=len(okb)

for i in range(0,n):
    if(okb[i] in yeni_blog):
        print("Bu konuda gerçekten biriyle konuşmanız gerekiyor, veya")
        print(["Yürüyüşe ne dersin?","Kitap okumak ister misin?","Müzik dinlemek ister misin?","Kahve içmek ister misin?"] [randint(0,5)])
        break
else:
    print("Bloğunuzu güncellediğiniz için teşekkürler.")


