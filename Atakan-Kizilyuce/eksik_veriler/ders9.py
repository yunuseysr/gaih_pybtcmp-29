# -*- coding: utf-8 -*-
"""
Created on Mon Jun 27 15:24:17 2022

@author: Atakan
"""

#kutuphaneler
import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer #sci-kit learn

#verinin eklenmesi
veriler = pd.read_csv('eksikveriler.csv')
#print(veriler) #kontrol noktasi

#veri on isleme (eksik veriler)

#hangi verileri ne ile degistirmek istedigimiz kisim (bu ornek icin nan degerler)
imputer = SimpleImputer(missing_values=np.nan,strategy='mean')

#ortalama alma islemi icin once yas kolonundaki bilgileri cekmeliyiz
yas = veriler.iloc[:,1:4].values
print(yas)

#fit fonksiyonu egitmek için kullanılır
imputer = imputer.fit(yas[:,1:4])

#fit ile ogretip tranform ile ogrendigini uygulamasını sagliyoruz
yas[:,1:4] = imputer.transform(yas[:,1:4])
print(yas)
