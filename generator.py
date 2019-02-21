import jinja2
import json
import os

with open('versions.json') as f:
    data = json.load(f)

for version in data["versions"]:
    
    path = version["eb"] + "/python" + version["python"] + "-" + version["os"]  + "/"
    if not os.path.exists(path):
        os.makedirs(path)
    
    templateLoader = jinja2.FileSystemLoader(searchpath="./")
    templateEnv = jinja2.Environment(loader=templateLoader)
    template = templateEnv.get_template("./templates/" + version["os"] + ".j2")
    outputText = template.render(
        python_version=version["python"],
        os_version=version["os"],
        eb_version=version["eb"]
    )
    
    with open(path + "Dockerfile", "wb") as dockerfile:
        dockerfile.write(outputText)
