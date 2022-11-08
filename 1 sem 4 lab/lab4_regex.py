import re


class Main:
    def __init__(self, json_obj):
        self.json_obj = json_obj
        self.lines = []
        self.temp = []
        self.print = ""

    def parser(self):
        self.json_obj.pop(0)
        self.json_obj.pop(-1)
        for i in self.json_obj:
            line = ''.join(re.split(" ", i))
            self.lines.append(re.sub(",", "", line).replace("\"", ""))

    def reWriting(self):
        line_padding = 0
        for i in range(len(self.lines)):
            line = self.lines[i]
            if line != "{" and line != "}":
                parts = re.split(":", line, 1)
                tag = parts[0]
                key = parts[1]
                if key == "":
                    self.print += " "*4*line_padding + "<" + tag + ">\n"
                    self.temp.append(tag)
                else:
                    self.print += " "*4*line_padding + "<" + tag + ">" + key + "</" + tag + ">\n"
            else:
                if line == "{":
                    line_padding += 1
                if line == "}":
                    line_padding -= 1
                    self.print += " " * 4 * line_padding + "</" + self.temp[-1] + ">\n"
                    self.temp.pop(-1)


file_json = open("test.json", "r", encoding="utf-8")
arr = file_json.read().splitlines()
file_xml = open("test_regex.xml", "w", encoding="utf-8")

p = Main(arr)
p.parser()
p.reWriting()
file_xml.write(p.print)

file_json.close()
file_xml.close()
