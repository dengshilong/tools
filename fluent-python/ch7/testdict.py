from dis import dis
d = dict()
print(dis('d["a"]'))
print(dis('d.get("a")'))
