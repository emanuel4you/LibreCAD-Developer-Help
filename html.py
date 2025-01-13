#!/usr/bin/env python3

import os, lispHtml, pythonHtml, dclTilesHtml, dclAttributesHtml

index_urls = (("https://dokuwiki.librecad.org/", "LibreCad Wiki"),
("https://librecad.readthedocs.io/", "LibreCad User's Manual"),
("https://librecad.readthedocs.io/en/latest/ref/tools.html", "LibreCad Commands"),
("https://librecad.readthedocs.io/en/latest/ref/customize.html#style-sheets", "LibreCad Style Sheets"),
("https://librecad.readthedocs.io/en/latest/ref/menu.html#widgets", "LibreCad Widgets"),
("___", ""),
("qrc:/html/developer.html", "LibreCad Developer Help"),
("___", ""),
("https://forum.librecad.org/", "LibreCad Forum"),
("https://librecad.zulipchat.com/", "LibreCad Zulip Chat")
)

developer_urls = (("qrc:/html/lisp/lisp.html", "Programming Overview of the LISP (LISt Processing) Language"),
("qrc:/html/lisp/lisp-compatibility.html", "LISP Compatibility"),
("qrc:/html/lisp/lisp-functions.html", "LISP Functions"),
("qrc:/html/python/python.html", "Programming Overview of the Python Language"),
("qrc:/html/python/python-functions.html", "Python Functions"),
("qrc:/html/dcl-tiles/dcl.html", "Overview of the DCL (Dialog Control Language)"),
("qrc:/html/dcl-tiles/dcl-tiles.html", "DCL Tiles"),
("qrc:/html/predefined-attributes/predefined-attributes.html", "Predefined Attributes"),
("qrc:/html/predefined-attributes/about-predefined-attributes.html", "About Predefined Attributes"),
("https://github.com/emanuel4you/LibreCAD-Developer-Examples", "Code Examples from the LibreCAD Developer Reference")
)

bold_List = (
"LISP",
"LibreCAD",
"LibreLisp",
"AutoLISP",
"DCL",
"setq",
"def!",
"first",
"nth",
"get",
"clojure"
)

h2_List = ("Programming Overview of the LISP (LISt Processing) Language",
"LISP Symbols",
)

h4_List = ("NOTE",
"NOTES",
"Valid Attributes",
"EXAMPLES",
"EXAMPLE",
"More about...",
"Integer Numbers",
"Real Numbers",
"Strings",
"Entity Names",
"Lists",
"Vectors (clojure)",
"Hash Maps (clojure)",
"Selection Sets",
"File Descriptors",
"LISP Functions"
)

root_dir = "html/"

def replaceInlineLink(line):
    line = line.strip()
    #replaceList = []
    if "[link]" in line:
        #print("[replaceInlineLink] found link!")
        line = line.replace("[link]LISP Compatibility" , "<a href=\"qrc:/html/lisp/lisp-compatibility.html\" title=\"LISP Compatibility\">LISP Compatibility</a>")

    return line

def replaceLink(line):
    whites = len(line[:len(line)-len(line.lstrip())])
    link = line.strip()[6:]
    print("link 1:",link)

    #if link.startswith("("):
     #   link = link[1:]
    #print("link 2:",link)

    #link = link.split(" ")[0]
    #print("link 3:",link)

    #if link.endswith(")"):
    #    link = link[:-1]
    #print("link 4:",link)

    para = "<p>"
    if whites > 3:
        para = "<p style=\"padding-left: " + str(whites*5) + "px;\">"

    for url, name in developer_urls:
        if name == link:
            return "\t<b>" + para + "<a href=\"" + url + "\" title=\"" + name + "\">" + name + "</a></p></b>\n"

    #else:
        #return link

    #return "\t" + para + "<a href=\"" + link + ".html\" title=\"LISP Function (" + line.strip()[6:] + ")\">" + line.strip()[6:] + "</a></p>\n"

    return line


def replaceItalic(line):
    #line = line.replace("true", "<i>true</i>")
    #line = line.replace("T", "<i>T</i>")
    #line = line.replace("false", "<i>false</i>")
    #line = line.replace("nil", "<i>nil</i>")
    return line

def boldFunction(line):
    line = line.strip()
    #if "(" in line and ")" in line:
        #print("found function!")
    #    link = line[line.index("("):][:line.index(")")][1:].split(" ")[0]
    #    if link.endswith(")"):
    #        link = link[:-1]
        #print("bold link:", link)
     #   if link in funcs:
     #       line = line.replace(link, "<b>" + link + "</b>")
    #else:
     #   both=set(funcs[15:]).intersection(line)
        #print("both:", both)
     #   for link in funcs[15:]:
     #       if link in both:
     #           #print (link, "in line")
     #           line.replace(link, "<b>" + link + "</b>")

    #line = line.replace("true", "<b>true</b>")
    #line = line.replace("T)", "<b>T)</b>")
    #line = line.replace(" T ", " <b>T</b> ")
    #line = line.replace("false", "<b>false</b>")
    #line = line.replace("nil", "<b>nil</b>")

    for i in bold_List:
        line = line.replace(i, "<b>" + i + "</b>")

    line = line.replace("<b></b>","")

    return line

def makelispHtml(filename):
    notset = True
    ul_listClosed = True
    ol_listClosed = True
    tableClosed = True
    htmlPath = root_dir + "lisp/" + filename[:-4] + ".html"
    htmlFile = open(htmlPath,'w')
    #print("open:", filename)
    print("[makeHtml] file:", htmlPath)

    htmlFile.write("<!DOCTYPE html>\n<html lang=\"en\">\n<head>\n\t<style>\n\t\t:root { font-family: sans-serif; }\n\t\tp { white-space: pre-wrap; padding-left: 15px; }\n     \t\tth { text-align: left; }\n\t</style>\n\t<titel>" + filename[:-4] + "</titel>\n</head>\n<body>\n")

    with open("lisp/" + filename, 'r') as file:
        for line in file:
            #print(line.strip())
            if line.strip() == "" or line.strip().startswith("#"):
                pass

            #elif notset and line.strip().startswith("(" + filename[:-4]):
            #    notset = False
            #    htmlFile.write("\t<h2>" + line.strip() + "</h2>\n")

            elif line.strip().startswith("Code") and line.strip().endswith("Returns"):
                tableClosed = False
                htmlFile.write("\t<table>\n\t<tr>\n\t<th>Code<th/>\n\t<th>Returns<th/>\n\t</tr>")

            elif line.strip() in h2_List:
                if not tableClosed:
                    htmlFile.write("\t</table>\n")
                    tableClosed = True
                if not ul_listClosed:
                    htmlFile.write("\t</ul>\n")
                    ul_listClosed = True
                if not ol_listClosed:
                    htmlFile.write("\t</ol>\n")
                    ol_listClosed = True

                htmlFile.write("\t<h2>" + line.strip() + "</h2>\n")
            elif line.strip() in h4_List:
                if not tableClosed:
                    htmlFile.write("\t</table>\n")
                    tableClosed = True
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
                if not tableClosed:
                    entry = line.strip().split(") ")
                    rest = line.strip().replace(entry[0]+ ")", "").strip()
                    htmlFile.write("\t<tr>\n\t<td>" + boldFunction(entry[0] + ")") + "<td/>\n\t<td>" + boldFunction(rest) + "<td/>\n\t</tr>")
                    continue
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
    htmlFile = open(root_dir + "index.html",'w')
    print("[makeIndexHtml] file:", root_dir + "index.html")
    htmlFile.write("<!DOCTYPE html>\n<html lang=\"en\">\n<head>\n\t<meta charset=\"utf-8\"/>\n\t<style>\n\t\t:root { font-family: sans-serif; }\n\t</style>\n\t<titel>LibreCad Help</titel>\n</head>\n<body>\n\t\n\t<hr/>\n<h2>LibreCad Help</h2>\n\t<hr/>\n")

    index = 0
    for url, name in index_urls:
        if url == "___":
            htmlFile.write("\t<hr/>\n")
        else:
            htmlFile.write("\t<a href=\"" + url + "\" title=\"" + name + "\">" + name + "</a><br/>\n")

    htmlFile.write("</body>\n</html>")
    htmlFile.close()

def makeDeveloperHtml():
    htmlFile = open(root_dir + "developer.html",'w')
    print("[makeIndexHtml] file:", root_dir + "developer.html")
    htmlFile.write("<!DOCTYPE html>\n<html lang=\"en\">\n<head>\n\t<meta charset=\"utf-8\"/>\n\t<style>\n\t\t:root { font-family: sans-serif; }\n\t</style>\n\t<titel>LibreCad Help</titel>\n</head>\n<body>\n\t\n\t<hr/>\n<h2>LibreCad Help</h2>\n\t<hr/>\n")

    index = 0
    for url, name in developer_urls:
        if url == "___":
            htmlFile.write("\t<hr/>\n")
        else:
            htmlFile.write("\t<b><a href=\"" + url + "\" title=\"" + name + "\">" + name + "</a></b><br/>\n")

    htmlFile.write("</body>\n</html>")
    htmlFile.close()

def main():
    current_directory = os.getcwd()
    final_directory = os.path.join(current_directory, root_dir + "lisp/")
    if not os.path.exists(final_directory):
        os.makedirs(final_directory)

    makelispHtml("lisp.txt")
    makeIndexHtml()
    makeDeveloperHtml()

    lispHtml.main()
    pythonHtml.main()
    dclTilesHtml.main()
    dclAttributesHtml.main()

if __name__ == "__main__":
    main()


