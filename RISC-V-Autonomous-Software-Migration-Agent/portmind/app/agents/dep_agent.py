import re

class DependencyAgent:
    LIBS = ["SDL2","OpenGL","png","curl","openssl","zlib"]

    def scan(self, repo):
        found = set()
        for f in repo.rglob("*"):
            if f.is_file():
                try:
                    txt = f.read_text(errors="ignore")
                    for lib in self.LIBS:
                        if re.search(lib, txt, re.I):
                            found.add(lib)
                except Exception:
                    pass
        return list(found)
