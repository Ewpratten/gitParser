
try:
    with open("./.git/config", "r") as f:
        data = f.read()
        f.close()
except:
    print("Not a git repo")

branchdata = []
for line in data.split("\n"):
    if line == "":
        continue
    if line[0] == "[":
        if line[1:-1].split(" ")[0] == "branch":
            branchdata.append(line[9:-2])

print(branchdata)
