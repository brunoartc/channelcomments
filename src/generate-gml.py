import glob, json
files = glob.glob("./output/clean/*")

channels = [] 


gml = ["graph", "[", "directed 0"]

stats = {"P":[], "C":[], "M":[]}


statsDo = {"P":[], "C":[], "M":[]}
for i in files:
    #print(type(i))
    gml.append("node")
    gml.append("[")
    gml.append(f"id {i}")
    tipo = i.split("-")[0].split("\\")[1]
    gml.append(f"tipo {tipo}")
    gml.append("]")
    with open(i) as a:
        channels.append([i, json.load(a)])

for i in range(len(channels)):
    j = i + 1
    tipo = channels[i][0].split("-")[0].split("\\")[1]
    while j < len(channels):
        if len(set(channels[i][1]) & set(channels[j][1])) > 0:
            gml.append("edge")
            gml.append("[")
            gml.append(f"source {channels[i][0]}")
            gml.append(f"target {channels[j][0]}")
            gml.append(f"weight {len(set(channels[i][1]) & set(channels[j][1]))}")
            gml.append("]")
            
            stats[tipo].append(len(set(channels[i][1]) & set(channels[j][1])))

        j+=1
    statsDo[tipo] += channels[i][1]

gml.append("]")

print("\n".join(gml))




with open("stats1", "w") as filse:
    json.dump(statsDo, filse)

with open("stats2", "w") as filse:
    json.dump(stats, filse)






