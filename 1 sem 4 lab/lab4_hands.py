class Main:
    def __init__(self, string):
        self.string = string
        self.lines = []
        self.temp = []
        self.print = ""

    def parser(self):
        self.string.pop(0)
        self.string.pop(-1)
        for i in self.string:
            line = ''.join(i.split())
            self.lines.append(line.replace(",", "").replace("\"", ""))

    def reWriting(self):
        level = 0
        for i in range(len(self.lines)):
            line = self.lines[i]
            if line != "{" and line != "}":
                parts = line.split(":", 1)
                tag = parts[0]
                key = parts[1]
                if key == "":
                    self.print += " "*4*level + "<" + tag + ">\n"
                    self.temp.append(tag)
                else:
                    self.print += " "*4*level + "<" + tag + ">" + key + "</" + tag + ">\n"
            else:
                if line == "{":
                    level += 1
                if line == "}":
                    level -= 1
                    self.print += " " * 4 * level + "</" + self.temp[-1] + ">\n"
                    self.temp.pop(-1)


file_json = open("test.json", "r", encoding="utf-8")
arr = file_json.read().splitlines()
file_xml = open("test.xml", "w", encoding="utf-8")

p = Main(arr)
p.parser()
p.reWriting()
file_xml.write(p.print)

file_json.close()
file_xml.close()
