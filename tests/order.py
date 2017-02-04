import json

with open("../data.json") as data_obj:
    data = json.load(data_obj)
data_obj.close()

for icon in data:
    if data[icon]["linux"]:
        root = data[icon]["linux"]
        if "symlinks" in root.keys() and len(root["symlinks"]) == 0:
            del data[icon]["linux"]["symlinks"]
        elif "symlinks" in root.keys() and len(root["symlinks]) != 0:
            sorted(data[icon]["linux"]["symlinks"], key=lambda icon_name: icon_name.lower())
sorted(data, key=lambda icon_name: icon_name.lower())

with open("../data.json", 'w') as fp:
    json.dump(data, fp, sort_keys=True, indent=4)
fp.close()
