# --- How to run this script? ---
# 1. Install <https://lucasg.github.io/Dependencies/> in 'MTA San Andreas 1.5/deps'
# 2. Open a command line window in the 'MTA San Andreas 1.5' directory
# 3. Run this script with at least Python 3.5 (worked for me on Python 3.9)
# 4. Review output in 'MTA San Andreas 1.5/output' directory

from pathlib import Path
import subprocess
import json
import os

os.makedirs("output", exist_ok=True)

extensions = [".dll", ".exe"]
files = [p for p in Path().rglob("*") if p.suffix in extensions]

for path in sorted(files):
    if str(path).startswith("deps"):
        continue
    
    args = [".\\deps\\Dependencies.exe", "-json", "-imports", str(path)]
    imports_result = subprocess.run(args, stdout=subprocess.PIPE, encoding="utf-8")
    imports_result = json.loads(str(imports_result.stdout))

    args[2] = "-exports"
    exports_result = subprocess.run(args, stdout=subprocess.PIPE, encoding="utf-8")
    exports_result = json.loads(str(exports_result.stdout))

    output = open("output/{name}.md".format(name=str(path).replace("\\", "__")), "w")
    output.write("# {title}\n".format(title=path.name))

    output.write("\n## Imports\n\n")

    for importdll in imports_result["Imports"]:
        output.write("<details><summary><b>{name}</b> ({count})</summary><p>\n".format(name=importdll["Name"], count=importdll["NumberOfEntries"]))
        output.write("\n| Ordinal | Name |\n")
        output.write("| ------- | ---- |\n")

        for func in importdll["ImportList"]:
            output.write("| {ordinal} | {name} |\n".format(ordinal=func["Ordinal"], name=func["Name"]))

        output.write("\n</p></details>\n")

    output.write("\n## Exports\n\n")
    output.write("\n| Ordinal | Name |\n")
    output.write("| ------- | ---- |\n")

    for func in exports_result["Exports"]:
        output.write("| {ordinal} | {name} |\n".format(ordinal=func["Ordinal"], name=func["Name"]))
    
    output.write("\n</p></details>\n")
    output.close()
