class Dict(dict):
    def __getitem__(self, key):
        return 2

class TestMiss(dict):
    def __missing__(self, key):
        return 3

if __name__ == "__main__":
    d = Dict()
    d["key"] = "test"
    print(d.get("key"), d["key"], d.get("k"), d["k"])

    d = TestMiss()
    d["key"] = "test"
    print(d.get("key"), d["key"], d.get("k"), d["k"])
    
