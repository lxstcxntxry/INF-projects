import json


def reWriting(json_obj, line_padding=""):
    result = list()
    json_obj_type = type(json_obj)

    if json_obj_type is dict:
        for tag in json_obj:
            sub_obj = json_obj[tag]
            result.append(line_padding + "<" + tag + ">")
            result.append(reWriting(sub_obj, "\t" + line_padding))
            result.append(line_padding + "</" + tag + ">")

        return "\n".join(result)

    return line_padding + json_obj


json_file = open("test.json", "r", encoding="utf-8")
xml_file = open("test_libs.xml", "w", encoding="utf-8")
xml_file.write(reWriting(json.load(json_file)))

json_file.close()
xml_file.close()
