import base64
# Base64-encoded original info.html content
data = ""
with open("D:/codex/qingmiao/info.html", "w", encoding="utf-8") as f:
    f.write(base64.b64decode(data).decode("utf-8"))
print("Done")
