#!/usr/bin/env python3

import os

#ls | sed -e 's/\.txt//g' | awk '{ printf "\"%s\", ",$1}'

funcs = ("actionTile", "addList", "command", "dimxTile", "dimyTile", "doneDialog", "endImage", "endList", "EvalSimpleFile", "EvalSimpleString", "fillImage", "getAttr", "getCorner", "getDist", "GetDoubleDialog", "GetIntDialog", "getInt", "getOrient", "getPoint", "getReal", "GetStringDialog", "getString", "getTile", "initGet", "loadDialog", "MessageBox", "modeTile", "newDialog", "newPositionedDialog", "OpenFileDialog", "pixImage", "prompt", "ReadCharDialog", "RunSimpleFile", "RunSimpleString", "setTile", "slideImage", "startDialog", "startImage", "startList", "termDialog", "textImage", "unloadDialog", "vectorImage", "python")

alias = ("string", "integer", "double", "tuple", "list")

h2_List = ("PYTHON Functions", "DCL Tiles", "DCL Attributes", "Programming Overview of the PYTHON Language")
h4_List = ("NOTE", "NOTES", "Valid Attributes", "EXAMPLES", "EXAMPLE", "Related DCL Tiles", "More about...", "Related DCL Tiles", "Valid Attribute", "Valid Attributes", "Valid Tiles", "Python Functions", "LibrePython", "import Modules")

proto = "qrc:/"
root_dir = "html/python/"

developer_urls = (
(proto + root_dir + "python.html", "PYTHON Functions"),
(proto + "html/dcl-tiles/dcl.html", "Overview of the DCL (Dialog Control Language)"),
("https://github.com/emanuel4you/LibreCAD-Developer-Examples", "Code Examples from the LibreCAD Developer Reference"),
("http://www.python.org", "www.python.org"),
)

def replaceInlineLink(line):
    replaceList = []
    if "[link]" in line:
        tmp = line.strip()
        #print("[replaceInlineLink] found link!")
        pos = list(i for i in range(len(tmp)-6) if tmp[i] + tmp[i+1] + tmp[i+2] + tmp[i+3] + tmp[i+4] + tmp[i+5] == "[link]")
        #print("[replaceIntmpLink] pos:", pos)
        for i in pos:
            link = tmp[i+6:].split()[0]
            if link in funcs:
                replaceList.append((link, link))

        if len(replaceList):
            for func, link in replaceList:
                link = proto + root_dir + link
                line = line.replace("[link]" + func, "<a href=\"" + link + ".html\" title=\"PYTHON Function " + func + "\">" + func + "</a>")

        for url, name in developer_urls:
            if name in line:
                line = line.replace("[link]" + name, "<a href=\"" + url + "\" title=\"" + name + "\">" + name + "</a></p>\n")

    return line

def replaceLink(line):
    whites = len(line[:len(line)-len(line.lstrip())])
    para = "<p>"

    if whites > 3:
        para = "<p style=\"padding-left: " + str(whites*5) + "px;\">"

    partsCount = len(line.strip()[6:].split())
    rest = ""
    parts = line.strip()[6:].split()
    del parts[0]

    for i in parts:
        rest += " "
        rest += i

    link = line.strip()[6:].split()[0]
    path = ""
    title = ""
    result = line

    for url, name in developer_urls:
        if name in line:
            return "<b>" + para + "<a href=\"" + url + "\" title=\"" + name + "\">" + name + "</a></p></b>\n"

    if link in funcs:
        path = proto + root_dir + link
        title = "PYTHON Function:: " + link
    else:
        return line

    if partsCount == 1:
        result = "<b>" + para + "<a href=\"" + path + ".html\" title=\"" + title + "\">" + link + "</a></p></b>\n"

    else:
        result = "<b>" + para + "<a href=\"" + path + ".html\" title=\"" + title + "\">" + link + "</a>" + rest + "</p></b>\n"

    return result

def replaceItalic(line):
    raws = line.split(" ")
    for i in raws:
        i.replace(".","")
        i.replace(",","")
        i.replace(";","")
    both=set(alias).intersection()
    #print("[replaceItalic] line.split:",line.split(" "))
    #print("[replaceItalic] both:", both)

    for link in alias:
        #print("[replaceItalic] link:", link)
        if link in both:
            #print (link, "[replaceItalic] in line")
            line = line.replace(link, "<i>" + link + "</i>")

    return line

def boldFunction(line):
    #line = line.strip()

    both=set(funcs).intersection(line)
    #print("both:", both)
    for link in funcs:
        if link in both:
            #print (link, "in line")
            line.replace(link, "<b>" + link + "</b>")


    line = line.replace("LibreCAD.", "<b>LibreCAD</b>.")
    line = line.replace(" LibreCAD ", " <b>LibreCAD</b> ")
    line = line.replace("LibreCAD,", "<b>LibreCAD</b>,")
    line = line.replace("LibreDCL+", "<b>LibreCAD</b>")
    line = line.replace("LibreLisp", "<b>LibreLisp</b>")
    line = line.replace("LibrePython", "<b>LibrePython</b>")
    line = line.replace("Python", "<b>Python</b>")
    line = line.replace("DCL", "<b>DCL</b>")
    line = line.replace("Dcl", "<b>Dcl</b>")
    line = line.replace("Lisp", "<b>Lisp</b>")
    line = line.replace("Ide", "<b>Ide</b>")
    line = line.replace("LISP", "<b>LISP</b>")


    #line = line.replace("True", "<b>True</b>")
    #line = line.replace("False", "<b>False</b>")
    #line = line.replace("None", "<b>None</b>")
    #line = line.replace("None", "<b>None</b>")
    line = line.replace("<b></b>","")

    return line

def makeHtml(filename):
    notset = True
    ul_listClosed = True
    ol_listClosed = True
    htmlPath = root_dir + filename[:-4] + ".html"
    htmlFile = open(htmlPath,'w')
    print("[makeHtml] file:", htmlPath)

    htmlFile.write("<!DOCTYPE html>\n<html lang=\"en\">\n<head>\n\t<meta charset=\"utf-8\"/>\n\t<style>\n\t\t:root { font-family: sans-serif; }\n\t\tp { white-space: pre-wrap; padding-left: 15px; }\n     \t\tth { text-align: left; }\n\t</style>\n\t<titel>" + filename[:-4] + "</titel>\n</head>\n<body>\n")

    with open("python/" + filename, 'r') as file:
        for line in file:
            #print("[makeHtml] line:", line.strip())
            #print("[makeHtml] line.split()[0]:", line.strip().split())

            if line.strip() == "" or line.strip().startswith("#"):
                pass

            elif notset and len(line.strip().split()) > 1 and line.strip().split()[1].startswith(filename[:-4]):
                notset = False
                htmlFile.write("\t<h2>" + replaceItalic(line.strip()) + "</h2>\n")

            elif line.strip() in h2_List:
                if not ul_listClosed:
                    htmlFile.write("\t</ul>\n")
                    ul_listClosed = True
                if not ol_listClosed:
                    htmlFile.write("\t</ol>\n")
                    ol_listClosed = True

                htmlFile.write("\t<h2>" + line.strip() + "</h2>\n")
            elif line.strip() in h4_List:
                if not ul_listClosed:
                    htmlFile.write("\t</ul>\n")
                    ul_listClosed = True
                if not ol_listClosed:
                    htmlFile.write("\t</ol>\n")
                    ol_listClosed = True

                htmlFile.write("\t<h4>" + line.strip() + "</h4>\n")

            elif "____" in line.strip():
                htmlFile.write("\t<hr/>\n")

            elif line.strip().startswith("*"):
                if ul_listClosed:
                    htmlFile.write("\t<ul>\n")
                    ul_listClosed = False
                if not ol_listClosed:
                    htmlFile.write("\t</ol>\n")
                    ol_listClosed = True
                htmlFile.write("\t\t<li>" + replaceItalic(replaceInlineLink(boldFunction(line.strip()[1:].strip()))) + "</li></br>\n")

            elif line.strip()[0] in "123456789" and line.strip()[1] in ".":
                if ol_listClosed:
                    htmlFile.write("\t<ol>\n")
                    ol_listClosed = False
                if not ul_listClosed:
                    htmlFile.write("\t</ul>\n")
                    ul_listClosed = True
                htmlFile.write("\t\t<li>" + replaceItalic(replaceInlineLink(boldFunction(line.strip()[1:].strip()[2:]))) + "</li></br>\n")

            elif line.strip().startswith("[link]"):
                if not ul_listClosed:
                    htmlFile.write("\t</ul>\n")
                    ul_listClosed = True
                if not ol_listClosed:
                    htmlFile.write("\t</ol>\n")
                    ol_listClosed = True
                htmlFile.write(replaceLink(line))

            else:
                if not ul_listClosed:
                    htmlFile.write("\t</ul>\n")
                    ul_listClosed = True
                if not ol_listClosed:
                    htmlFile.write("\t</ol>\n")
                    ol_listClosed = True

                line = replaceInlineLink(line)
                line = replaceItalic(line)
                line = boldFunction(line)

                whites = len(line[:len(line)-len(line.lstrip())])

                if whites > 3:
                    htmlFile.write("<p style=\"padding-left: " + str(whites*5) + "px;\">" + line.strip() + "</p>\n")
                else:
                    htmlFile.write("<p>" + line.strip() + "</p>\n")

    htmlFile.write("</body>\n</html>")
    htmlFile.close()

def makeIndexHtml():
    htmlFile = open(root_dir + "python-functions.html",'w')
    print("[makeIndexHtml] file: " + root_dir + "python-functions.html")
    htmlFile.write("<!DOCTYPE html>\n<html lang=\"en\">\n<head>\n\t<meta charset=\"utf-8\"/>\n\t<style>\n\t\t:root { font-family: sans-serif; width: 800px; }\n\t</style>\n\t<titel>LibreCAD Developer Help</titel>\n</head>\n<body>\n\t\n\t<hr/>\n<h2>Python Functions</h2>\n\t<hr/>\n")

    index = 0
    for func in funcs:
        index += 1
        path = proto + root_dir + func
        htmlFile.write("\t<b><a href=\"" + path + ".html\" title=\"PYTHON Function " + func + "\">" + func + "</a></b><br/>\n")

    htmlFile.write("</body>\n</html>")
    htmlFile.close()

def main():
    current_directory = os.getcwd()
    final_directory = os.path.join(current_directory, root_dir)
    if not os.path.exists(final_directory):
        os.makedirs(final_directory)

    for i in funcs:
        makeHtml(i + ".txt")

    makeIndexHtml()

if __name__ == "__main__":
    main()
