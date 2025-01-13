#!/usr/bin/env python3

import os

#ls | sed -e 's/\.txt//g' | awk '{ printf "\"%s\", ",$1}'

funcs = ("actionTile", "addList", "command", "dimxTile", "dimyTile", "doneDialog", "endImage", "endList", "EvalSimpleFile", "EvalSimpleString", "fillImage", "getAttr", "getCorner", "getDist", "GetDoubleDialog", "GetIntDialog", "getInt", "getOrient", "getPoint", "getReal", "GetStringDialog", "getString", "getTile", "initGet", "loadDialog", "MessageBox", "modeTile", "newDialog", "newPositionedDialog", "OpenFileDialog", "pixImage", "prompt", "ReadCharDialog", "RunSimpleFile", "RunSimpleString", "setTile", "slideImage", "startDialog", "startImage", "startList", "termDialog", "textImage", "unloadDialog", "vectorImage")

alias = ("string", "integer", "double", "tuple", "list")

h2_List = ("PYTHON Functions", "DCL Tiles", "DCL Attributes")
h4_List = ("NOTE", "NOTES", "Valid Attributes", "EXAMPLES", "EXAMPLE", "Related DCL Tiles", "More about...", "Related DCL Tiles", "Valid Attribute", "Valid Attributes", "Valid Tiles")

root_dir = "html/python/"

proto = "qrc:/"

def replaceInlineLink(line):
    line = line.strip()
    replaceList = []
    if "[link]" in line:
        #print("[replaceInlineLink] found link!")
        pos = list(i for i in range(len(line)-6) if line[i] + line[i+1] + line[i+2] + line[i+3] + line[i+4] + line[i+5] == "[link]")
        #print("[replaceInlineLink] pos:", pos)
        for i in pos:
            link = line[i+6:].split()[0]
            if link in funcs:
                replaceList.append((link, link))

        if len(replaceList):
            for func, link in replaceList:
                link = proto + root_dir + link
                line = line.replace("[link]" + func , "<a href=\"" + link + ".html\" title=\"PYTHON Function " + func + "\">" + func + "</a>")

    return line

def replaceLink(line):
    whites = len(line[:len(line)-len(line.lstrip())])

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

    if link in funcs:
        path = proto + root_dir + link
        title = "PYTHON Function:: " + link

    para = "<p>"
    if whites > 3:
        para = "<p style=\"padding-left: " + str(whites*5) + "px;\">"

    if partsCount == 1:
        result = para + "<a href=\"" + path + ".html\" title=\"" + title + "\">" + link + "</a></p>\n"

    else:
        result = para + "<a href=\"" + path + ".html\" title=\"" + title + "\">" + link + "</a>" + rest + "</p>\n"

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
    line = line.strip()

    both=set(funcs).intersection(line)
    print("both:", both)
    for link in funcs:
        if link in both:
            #print (link, "in line")
            line.replace(link, "<b>" + link + "</b>")

    line = line.replace("True", "<b>True</b>")
    line = line.replace("False", "<b>False</b>")
    line = line.replace("None", "<b>None</b>")
    line = line.replace("None", "<b>None</b>")
    line = line.replace("<b></b>","")

    return line

def makeHtml(filename):
    notset = True
    ul_listClosed = True
    ol_listClosed = True
    htmlPath = root_dir + filename[:-4] + ".html"
    htmlFile = open(htmlPath,'w')
    print("[makeHtml] file:", htmlPath)

    htmlFile.write("<!DOCTYPE html>\n<html lang=\"en\">\n<head>\n\t<style>\n\t\t:root { font-family: sans-serif; }\n\t\tp { white-space: pre-wrap; padding-left: 15px; }\n     \t\tth { text-align: left; }\n\t</style>\n\t<titel>" + filename[:-4] + "</titel>\n</head>\n<body>\n")

    with open("python/" + filename, 'r') as file:
        for line in file:
            print("[makeHtml] line:", line.strip())
            print("[makeHtml] line.split()[0]:", line.strip().split())

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
    htmlFile.write("<!DOCTYPE html>\n<html lang=\"en\">\n<head>\n\t<style>\n\t\t:root { font-family: sans-serif; width: 800px; }\n\t</style>\n\t<titel>LibreCAD Developer Help</titel>\n</head>\n<body>\n\t\n\t<hr/>\n<h2>Python Functions</h2>\n\t<hr/>\n")

    index = 0
    for func in funcs:
        index += 1
        path = proto + root_dir + func
        htmlFile.write("\t<a href=\"" + path + ".html\" title=\"PYTHON Function " + func + "\">" + func + "</a><br/>\n")

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
