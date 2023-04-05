people = {"andrejs": 19, "aleksandrs": 7, "dmitrijs": 47}
for name, age in people.items():
  if age > 18:
    print(f"{name} ir 18 gadi")
  else:
    print(f"{name} nav 18 gadi")