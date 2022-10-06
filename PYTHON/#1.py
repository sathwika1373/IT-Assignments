#1.
var_count=df["variety"].value_counts()
var_count=dict(var_count)
A=["iris-setosa","iris-versicolor","iris-virginica"]


fig=plt.figure(figsize=(5,5))
explode=(0.1,0.1,0.1)
plt.pie(x=var_count.values(),labels=A,explode=explode,autopct='%1.1f%%',shadow=True)
plt.title("Iris Species %")
plt.show()
