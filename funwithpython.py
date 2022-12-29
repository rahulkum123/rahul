from datetime import datetime as dt
d=dt.now().date()
t=dt.now().time()
print(d)
print(t)
print(d.strftime("%d-%m-%y"))
print(d.strftime("%d/%m/%y"))
print(d.strftime("%d-%m-%Y"))
print(d.strftime("%d-%B-%Y"))
print(d.strftime("%d/%B/%y,%a"))
print(d.strftime("%D/%B/%y,%p"))

