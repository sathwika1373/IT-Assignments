#4.
df=pd.read_csv("iris.csv")

fig=plt.figure(figsize=(5,3))
plt.hist(x=list(df["sepal.length"]))
plt.xlabel("sepal length(cm)")
plt.ylabel("Frequency")
plt.show()

fig=plt.figure(figsize=(5,3))
plt.hist(x=list(df["sepal.width"]),color="orange")
plt.xlabel("sepal width(cm)")
plt.ylabel("Frequency")
plt.show()

fig=plt.figure(figsize=(5,3))
plt.hist(x=list(df["petal.length"]),color="green")
plt.xlabel("petal length(cm)")
plt.ylabel("Frequency")
plt.show()

fig=plt.figure(figsize=(5,3))
plt.hist(x=list(df["petal.width"]),color="red")
plt.xlabel("petal width(cm)")
plt.ylabel("Frequency")
plt.show()
