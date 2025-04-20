#  Üretim Planlama - Dinamik Programlama Yaklaşımı

Bu projede dinamik programlama yöntemi kullanılarak bir üretim hattındaki işlerin makineler üzerinde minimum süreyle nasıl tamamlanabileceği optimize edilmiştir.

---

##  Problem Tanımı

- Bir üretim hattında sırayla yapılması gereken **n adet iş** vardır.
- Bu işler, **m farklı makinede** gerçekleştirilebilir.
- Her işin, her makinedeki tamamlanma süresi farklıdır.
- Ayrıca, makineler arası geçişlerde bir **geçiş maliyeti ** oluşur.
- Amaç, tüm işleri **minimum toplam süreyle** tamamlamaktır.

---

##  Matris Zinciri Çarpımı ile İlişki

Bu problem klasik "matris zinciri çarpımı" probleminin bir tür genellemesidir.  
Oradaki amaç, çarpma sırasını optimize ederek işlem sayısını minimize etmekti.  
Burada ise amaç, işleri makineler arasında sırayla en verimli şekilde dağıtarak toplam süreyi minimize etmektir.  
Her iş-makine kombinasyonu bir tablo (matris) ile temsil edildiği için, matris zinciri problemiyle yapısal bir benzerlik taşır.

---

##  Dinamik Programlama Stratejisi

- İlk işin her makinede yapılma süresi doğrudan tabloya yazılır.
- Sonraki işler için her makinedeki minimum süre, bir önceki işin hangi makinede yapıldığına ve geçiş maliyetlerine göre hesaplanır.
- Alt problemler bir tablo ile çözülerek tekrar hesaplamalar önlenmiştir.

---

##  Test Sonuçları

Test amaçlı çalıştırılan örnek veri setinde minimum toplam süre başarıyla bulunmuştur.

  İşlem Adımı  Sonuç:
  İşlem süreleri ve geçiş maliyetleri girildi 
  Dinamik programlama algoritması uygulandı 
  DP tablosu doğru şekilde oluşturuldu 
  Minimum toplam süre hesaplandı 

---

##  Zaman ve Bellek Karmaşıklığı

- **Zaman Karmaşıklığı:** O(n * m²)  
  Her iş ve her makine için diğer makinelerden geçiş kontrol edilir.

- **Bellek Karmaşıklığı:** O(n * m)  
  DP tablosu n satır ve m sütundan oluşur.

---

##  Nasıl Çalıştırılır?

1. `DP_programming.py` dosyasını Python 3 ile çalıştırın:
   ```
   python DP_programming.py
   ```
2. Konsolda minimum toplam süre ve DP tablosu çıktısını görebilirsiniz.

---

##  Video İçeriği

Video içeriğinde aşağıdaki konular teknik olarak anlatılmıştır:
- Problem tanımı
- Kodun nasıl çalıştığı
- DP tablosunun nasıl oluşturulduğu
- Örnek veri ile test sonuçları
- Zaman ve bellek analizleri
