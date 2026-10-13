import pandas as pd

og= pd.read_excel(r"C:\Users\PASKAL\OneDrive\Desktop\aaradhya\Online Retail.xlsx")
df=pd.DataFrame(og)
df.dropna(subset=["Description"],inplace=True)
df.drop(columns=["CustomerID"],inplace=True)

df["InvoiceDate"] = pd.to_datetime(
    df["InvoiceDate"]
)

df=df.sort_values("InvoiceDate").reset_index(drop=True)
df["Revenue"]=df["Quantity"]*df["UnitPrice"]
items=df.groupby("Country").agg({"Quantity":"sum","Revenue":"sum"})
items=items.sort_values("Revenue",ascending=False)


items2=df.groupby("Description").agg({"Quantity":"sum","Revenue":"sum"})
items2=items2.sort_values("Revenue",ascending=False)

df["year"]=df["InvoiceDate"].dt.year
df=df.sort_values(by=["year"])
og=df.groupby("year")["Revenue"].sum()
df["month"]=df["InvoiceDate"].dt.month
m=df[df["year"]==2010]

print("2011")
yea=df[df["year"]==2011]
yea2=yea.groupby("month")["Revenue"].sum()
print(yea2)

bad=df[(df["year"]==2011)&(df["month"]==12)]
print("bad data")
pr=bad.groupby("Description")["Revenue"].sum().tail(10)
print(pr.sort_values(ascending=True))
print(bad["Revenue"].sum())
