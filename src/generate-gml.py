import glob, json
files = glob.glob("./output/clean/*")

channels = [] 


gml = ["graph", "["]

for i in files:
    #print(type(i))
    gml.append("node")
    gml.append("[")
    gml.append(f"id {i}")
    gml.append("]")
    with open(i) as a:
        channels.append([i, json.load(a)])

for i in range(len(channels)):
    j = i + 1
    while j < len(channels):
        if len(set(channels[i][1]) & set(channels[j][1])) > 0:
            gml.append("edge")
            gml.append("[")
            gml.append(f"source {channels[i][0]}")
            gml.append(f"target {channels[j][0]}")
            gml.append(f"weight {len(set(channels[i][1]) & set(channels[j][1]))}")
            gml.append("]")
        j+=1


gml.append("]")

print("\n".join(gml))






