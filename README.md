# MARF
	
Project Startup
Document
for
MARF
Version 0.3
Prepared by Ramazan Faruk OĞUZ, Hakan YÜKSEK and 
Himmet Toprak KESGİN,Selim Duvakli
Yildiz Technical University,Istanbul Medipol University
29.08.2019
     


     
1.	Giriş
1.1	Amaç
Bu belgenin amacı MARF projesinin çalışma şeklinin anlatılmasıdır. Bu belge 3 ana bölümden oluşmaktadır. Bu bölümler Proje İçeriği, Proje Nasıl Çalıştırılır ve Proje Geliştirme Ortamı ve Araçları ‘dır.
2.	Proje İçeriği

2.1	Projenin Alt Başlıkları
MARF projesi 4 farklı projenin birleşimi ile oluşmaktadır. Bu projelerin yanında bir de Kullanıcı Arayüzü bulunmaktadır. Bu projeler ve kısaca tanımlarına aşağıda yer verilmiştir. Projelerin ayrıntılı bilgileri SRS ve SDD dökümanlarından ulaşılabilir.

2.1.1	Task Planning and Scheduling with AI Techniques
Kullanıcıdan alacağı görevler için bir plan oluşturup yapay zeka teknikleri kullanarak, ilgili görevleri müsait araçlara tahsis edecek sistemdir.
2.1.2	Multi Agent Communication
Projeler arasındaki veri alışverişi görevini gerçekleştiren sistemdir. Web Servis üzerinden çalışarak sistemler arası haberleşmeyi sağlamaktadır.
2.1.3	AI-Based Path Planning
Çoklu ajanlar için çarpışma olmaksızın, başlangıç ve varış noktaları verilen araçlar için yol rotaları hesaplayan ve bu rotaları diğer sistemlere bildiren çalışmadır.
2.1.4	Drone Path Planning with AI Techniques
2 boyutlu engellerden oluşan bir harita üzerinde başlangıç ve bitiş noktaları arasında bir rota hesaplayan ve bu rotayı diğer sistemlere aktaran projedir.
3.	Proje Nasıl Çalıştırılır?
Projenin çalıştırılabilmesi için adımların sırasıyla uygulanması yeterlidir.

(Marf ve untitle 1 ayrı ayrı sekmelerde açılmalıdır )
1.	Multi Agent Communication sisteminin çalışacağı bilgisayarın IP adresi bilinmelidir.
2.	Bu IP adresi entegre sistemde yer alan 4 projede de ilgili kısımlarda güncellenmelidir. Bu güncelleme kayıt olma, veri gönderme ve veri alma ile ilgilidir.
3.	Daha sonra Multi Agent Communication sistemi Web Servisin kullanılabilmesi amacıyla başlatılır.
4.	Sırasıyla Task Planner, Drone Path Planner ve AI-Based Path Planning iletişim sistemine kayıt olur. Her birinin ID ‘si sırasıyla 0, 1 ve 2 şeklindedir.
(Bu sıralama da şöyledir app.py daha sonra System.py daha sonra Main ve daha sonra Path Planning package ının içindeki Main.py çalıştırılır.Sonrasında da marfın içerisinden Main windowa başlatılır)
(gerekli map bilgileri girildikten sonra starta basılır)
5.	Bağlantılar yapıldıktan sonra UI ekranı açılır ve map ve gerekli araç ve görevler oluşturulduktan sonra starta basılır.
6.	Her proje kendi görevini gerçekleştirir ve bilgiler iletişim sistemiyle projeler arasında aktarılır. Kullanıcı için komut ekranında çıktılar görselleştirilerek sunulur.
7.	Programın çalışması 4 bilgisayardan da takip edilebilir.
8.	Task Planner tüm görevleri bitirdiğinde kapanır. Diğer projelerin elle kapatılması gerekir.

     
4.	Proje Geliştirme Ortamı ve Araçları
4.1	Geliştirme Ortamı
Bu proje Python 3.7 versiyonu kullanılarak PyCharm ve Spyder geliştirme ortamına uygun olarak gerçeklenmiştir.
4.2	Geliştirme Araçları
Proje geliştirilirken kullanım kolaylığı bulunduğundan aşağıdaki kütüphaneler içerisinde bulunan fonksiyonlardan yararlanılmıştır. Kullanım amaçları kısaca özetlenmiştir.
•	Random
Genetik Algoritma’da popülasyon ilklendirilmesi için kullanılmıştır.


•	matplotlib.pyplot 
Üretilen yolların harita üzerinde gösterilebilmesi, haritanın komut ekranında görselleştirilmesi için kullanılmıştır.

•	Time
Algoritmaların performans sonuçlarının gösterilebilmesi için kullanılmıştır.

•	Requests
Web Servis kullanımının sağlanabilmesi için eklenen kütüphanedir.

•	Json
Veri aktarımında kullanılan formattır.

•	Flask
Web Servis için gerekli olan kütüphanedir. Multi Agent Communication Publisher/subscriber yapısını bu kütüphane ile gerçekleştirmiştir.

•	Jsonify
Verilerin json nesnesine çevrilmesi için kullanılan kütüphanedir.

•	Datetime
Görevlerin son bitirilme tarihi için kullanılmıştır.
     



     
