#2.
a=list(df["sepal.length"])
b=list(df["sepal.width"])
setosa_sep_len=[a[i] for i in range(0,49)]
setosa_sep_wid=[b[i] for i in range(0,49)]

a=list(df["sepal.length"])
b=list(df["sepal.width"])
versi_sep_len=[a[i] for i in range(50,100)]
versi_sep_wid=[b[i] for i in range(50,100)]

a=list(df["sepal.length"])
b=list(df["sepal.width"])
vergi_sep_len=[a[i] for i in range(100,150)]
vergi_sep_wid=[b[i] for i in range(100,150)]

fig=plt.figure()
plt.scatter(setosa_sep_len,setosa_sep_wid,color="red")
plt.scatter(versi_sep_len,versi_sep_wid,color="green")
plt.scatter(vergi_sep_len,vergi_sep_wid,color="blue")
plt.ylabel("sepal width")
plt.xlabel("sepal length")
plt.xlim(4,8.5)
plt.ylim(1.5,5)
plt.grid(color = 'black', linestyle = '--', linewidth = 0.5)
plt.title("The Iris Data Set")
plt.legend(["iris setosa","iris versicolor","iris virginica"])
plt.show()

