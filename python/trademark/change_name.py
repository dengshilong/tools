import execjs

# with open("change_name.js", "r", encoding="utf-8") as f:
with open("change_name.js", 'rb') as f:
    content = f.read().decode("utf-8")
    # print(content)
    t = execjs.compile(content)
    # print(t.call("_$PH", 'test sdfd \n , sdf. sdfsdf'))
    # t.call("_$PH")
    t.call("_$test")
