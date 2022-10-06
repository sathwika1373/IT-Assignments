#3.
a=list(df["petal.length"])
b=list(df["petal.width"])
setosa_pet_len=[a[i] for i in range(0,49)]
setosa_pet_wid=[b[i] for i in range(0,49)]

a=list(df["petal.length"])
b=list(df["petal.width"])
versi_pet_len=[a[i] for i in range(50,100)]
versi_pet_wid=[b[i] for i in range(50,100)]

a=list(df["petal.length"])
b=list(df["petal.width"])
vergi_pet_len=[a[i] for i in range(100,150)]
vergi_pet_wid=[b[i] for i in range(100,150)]

a1=(sum(setosa_sep_len)/50)#setosa_seplen_avg
a2=(sum(setosa_sep_wid)/50)#setosa_sepwid_avg
a3=(sum(setosa_pet_len)/50)#setosa_petlen_avg
a4=(sum(setosa_pet_wid)/50)#setosa_petwid_avg

b1=(sum(versi_sep_len)/50)#versi_seplen_avg
b2=(sum(versi_sep_wid)/50)#versi_sepwid_avg
b3=(sum(versi_pet_len)/50)#versi_petlen_avg
b4=(sum(versi_pet_wid)/50)#versi_petwid_avg

c1=(sum(vergi_sep_len)/50)#vergi_seplen_avg
c2=(sum(vergi_sep_wid)/50)#vergi_sepwid_avg
c3=(sum(vergi_pet_len)/50)#vergi_petlen_avg
c4=(sum(vergi_pet_wid)/50)#vergi_petwid_avg



df = pd.DataFrame({
    'Features': ['Sepal length', 'Sepal width', 'Petal length','Petal width'],
    'setosa': [a1,a2,a3,a4],
    'versicolor': [b1,b2,b3,b4],
    'verginica':[c1,c2,c3,c4]
     })

df.plot(x="Features", y=["setosa", "versicolor","verginica"], kind="bar",width=0.8,
        title="Bar graph",ylabel="Value in cm.")
