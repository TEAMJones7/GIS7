
import shapefile #mengimpor modul shapefil
w=shapefile.Writer() #untuk membuat shapefile baru
w.shapeType #menyeting menggunakan jenis shape apa (point,polygon)
#membuat dbs dengan 2 field, berupa kolom
w.field("Nama Bidang","Bidang Ke")
w.field("Nama Bidang","Bidang Ke")
#membuat dbs dengan 2 field, berupa kolom
w.record("Segitiga Siku-Siku","satu")
w.record("Segitiga Siku-Siku","dua")
w.record("Segitiga Siku-Siku","tiga")

#membuat 3 row karena menggunakan 3
w.poly(parts=[[[-7,7],[-1,7], [-7,1],[-7,7]]],shapeType=shapefile.POLYGON) #mengisi .shp dengan titik point
w.poly(parts=[[[7,7],[1,7], [7,1],[7,7]]],shapeType=shapefile.POLYGON) #mengisi .shp dengan titik point
w.poly(parts=[[[7,-7],[1,-7], [7,-1],[7,-7]]],shapeType=shapefile.POLYGON) #mengisi .shp dengan titik point
w.save("soal10")#melakukan save dengan nama (soal1)


import shapefile 
w=shapefile.Writer() 
w.shapeType 
w.field("Nama Bidang","Bidang Ke")
w.field("Nama Bidang","Bidang Ke")
w.record("Segitiga Siku-Siku","satu")
w.record("Segitiga Siku-Siku","dua")
w.record("Segitiga Siku-Siku","tiga")
w.poly(parts=[[[-7,7],[-1,7], [-7,1],[-7,7]]],shapeType=shapefile.POLYGON)
w.poly(parts=[[[7,7],[1,7], [7,1],[7,7]]],shapeType=shapefile.POLYGON)
w.poly(parts=[[[7,-7],[1,-7], [7,-1],[7,-7]]],shapeType=shapefile.POLYGON) 
w.save("soal10")