"""把 index.html（Artifact 源文件，没有 <html>/<head>）包成完整页面，输出到 site/index.html。"""
from pathlib import Path

root = Path(__file__).resolve().parent.parent
src = (root / "index.html").read_text(encoding="utf-8")
head, sep, rest = src.partition("<style>")
page = (
    "<!doctype html>\n<html lang=\"zh-CN\">\n<head>\n<meta charset=\"utf-8\">\n"
    "<meta name=\"viewport\" content=\"width=device-width, initial-scale=1, viewport-fit=cover\">\n"
    + head + sep + rest.split("</style>", 1)[0] + "</style>\n</head>\n<body>\n"
    + rest.split("</style>", 1)[1] + "\n</body>\n</html>\n"
)
(root / "site").mkdir(exist_ok=True)
(root / "site" / "index.html").write_text(page, encoding="utf-8", newline="\n")
print("site/index.html", len(page), "bytes")
