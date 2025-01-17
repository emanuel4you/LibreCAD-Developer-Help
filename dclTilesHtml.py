#!/usr/bin/env python3

import os

#ls | sed -e 's/\.txt//g' | awk '{ printf "\"%s\", ",$1}'


dclTiles = ("boxed_column", "boxed_radio_column", "boxed_radio_row", "boxed_row", "button", "column", "concatenation", "dialog", "dial", "edit_box", "errtile", "image_button", "image", "list_box", "name", "ok_cancel_help_errtile", "ok_cancel_help_info", "ok_cancel_help", "ok_cancel", "ok_only", "paragraph", "popup_list", "radio_button", "radio_column", "radio_row", "register", "row", "scroll", "slider", "spacer_0", "spacer_1", "spacer", "tab", "text_part", "text", "toggle", "dcl", "DCL")

attributes = ("action", "alignment", "allow_accept", "aspect_ratio", "big_increment", "children_alignment", "children_fixed_height", "children_fixed_width", "color", "edit_limit", "edit_width", "fixed_height", "fixed_width_font", "fixed_width", "height", "initial_focus", "is_bold", "is_cancel", "is_default", "is_enabled", "is_tab_stop", "key", "label", "layout", "list", "max_value", "min_value", "mnemonic", "multiple_select", "password_char", "small_increment", "tabs", "tab_truncate", "value", "width")

alias = ("position", "left", "right", "top", "bottom", "centered", "horizontal", "vertical", "dialog_line", "dialog_foreground", "dialog_background", "false", "graphics_background", "black", "red", "yellow", "green", "cyan", "blue", "magenta", "true", "white", "graphics_foreground")

h2_List = ("DCL Tiles", "DCL Attributes", "DCL", "Overview of the DCL (Dialog Control Language)")
h4_List = ("NOTE", "NOTES", "Valid Attributes", "EXAMPLES", "EXAMPLE", "Related DCL Tiles", "More about...", "Related DCL Tiles", "Valid Attribute", "Valid Attributes", "Valid Tiles", "Tiles", "Cluster Tiles", "Attributes", "The DCL File Format", "Tile Meaning", "Attribute Meaning")

root_dir = "html/dcl-tiles/"

proto = "qrc:/"

def replaceInlineLink(line):
    #linkLine = line.strip()
    linkLine = line
    replaceList = []
    if "[link]" in linkLine:
        print("[replaceInlineLink] found link!")
        pos = list(i for i in range(len(linkLine)-6) if linkLine[i] + linkLine[i+1] + linkLine[i+2] + linkLine[i+3] + linkLine[i+4] + linkLine[i+5] == "[link]")
        #print("[replaceInlineLink] pos:", pos)
        for i in pos:
            link = linkLine[i+6:].split()[0].split()[0]
            link = link.replace(".","").replace(";","").replace(",","").replace(")","")
            if link == ":":
                link = linkLine[i+8:].split()[0].replace(".","").replace(";","").replace(")","")

            #print("[replaceInlineLink] link:", link)
            if link in dclTiles:
                print("[replaceInlineLink] link is dclTile:", link)
                replaceList.append((link, proto + root_dir + link.lower(), "DCL Tile: " + link))

            if link in attributes:
                print("[replaceInlineLink] link is attribut!", link)
                replaceList.append((link, proto + "html/predefined-attributes/" + link, "DCL Attribute: " + link))

        if "[link]Predefined Attributes" in line:
            path = proto + "html/predefined-attributes/predefined-attributes"
            replaceList.append(("Predefined Attributes", path, "DCL: Predefined Attributes"))

        if "[link]About Predefined Attributes" in line:
            path = proto + "html/predefined-attributes/about-predefined-attributes"
            replaceList.append(("About Predefined Attributes", path, "DCL: About Predefined Attributes"))

        if "[link]PYTHON Funktions" in line:
            path = proto + "html/python/python-functions"
            replaceList.append(("PYTHON Funktions", path, "DCL: PYTHON Functions"))

        if len(replaceList):
            for link, path, title in replaceList:
                linkLine = linkLine.replace("[link]: " + link , "<a href=\"" + path + ".html\" title=\": " + title + "\">: " + link + "</a>")
                linkLine = linkLine.replace("[link]" + link , "<a href=\"" + path + ".html\" title=\"" + title + "\">" + link + "</a>")

    return linkLine

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

    #print("link:",link)
    #print("line.strip():",line.strip())
    #print("line:",line.strip()[8:].split()[0])

    if link in dclTiles:
        link = line.strip()[6:].split()[0].strip()
        path = proto + root_dir + link.lower()
        title = "DCL Tile: " + link

    if link in attributes:
        #print("link in dcl tiles",link)
        path = proto + "html/predefined-attributes/" + link.lower()
        title = "DCL Tile: " + link

    if line.strip()[8:].split()[0].strip() in dclTiles:
        partsCount = 2
        link = ": " + line.strip()[8:].split()[0].strip()
        rest = line.strip().replace("[link]: " + line.strip()[8:].split()[0].strip(), "")
        print("link in dcl tiles",link)
        path = proto + root_dir + line.strip()[8:].split()[0].strip()
        print("link in dcl tiles path:",path)
        title = "DCL Tile: " + ": " + line.strip()[8:].split()[0].strip()

    if line.strip()[6:] == "Predefined Attributes":
        #print("line.strip():",line.strip())
        partsCount = 1
        link = "Predefined Attributes"
        path = proto + "html/predefined-attributes/predefined-attributes"
        title = "DCL: Predefined Attributes"

    if line.strip()[6:] == "About Predefined Attributes":
        #print("line.strip():",line.strip())
        partsCount = 1
        link = "About Predefined Attributes"
        path = proto + "html/predefined-attributes/about-predefined-attributes"
        title = "DCL: About Predefined Attributes"

    if line.strip()[6:] == "PYTHON Funktions":
        #print("line.strip():",line.strip())
        partsCount = 1
        link = "PYTHON Funktions"
        path = proto + "html/python/python-functions"
        title = "DCL: PYTHON Functions"

    if line.strip()[6:] == "DCL Tiles":
        #print("line.strip():",line.strip())
        partsCount = 1
        link = "DCL Tiles"
        path = proto + "html/dcl-tiles/dcl-tiles"
        title = "DCL: Tiles"

    print("end path:",path)

    para = "<p>"
    if whites > 3:
        para = "<p style=\"padding-left: " + str(whites*5) + "px;\">"

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
            line = line.replace(" " + link, " <i>" + link + "</i>")

    return line

def boldFunction(line):
    #print("[boldFunction] - start")
    line = line.strip()

    if ": " in line.strip():
        link = line.strip()[line.strip().index(":"):]
        #print("link1:", link)
        link = link.split(" ")[0] + " " + link.split(" ")[1]
        #print("link2: >%s<" %link)

        if link[2:] in dclTiles:
            line = line.replace(link, "<b>" + link + "</b>")

    else:
        both=set(attributes).intersection(line.split(" "))
        #print("line.split:",line.split(" "))
        #print("both:", both)
        for link in attributes:
            if link in both:
                #print (link, "in line")
                line = line.replace(link, "<b>" + link + "</b>")

    #line = line.replace("true", "<b>true</b>")
    #line = line.replace("T)", "<b>T)</b>")
    #line = line.replace(" T ", " <b>T</b> ")
    #line = line.replace("false", "<b>false</b>")
    #line = line.replace("nil", "<b>nil</b>")
    line = line.replace("Dialog Control Language", "<b>Dialog Control Language</b>")
    line = line.replace("LibreCAD", "<b>LibreCAD</b>")
    line = line.replace("LibreCAD", "<b>LibreDcl+</b>")
    line = line.replace("DCL", "<b>DCL</b>")
    line = line.replace("<b></b>","")

    return line

def makeHtml(filename):
    notset = True
    ul_listClosed = True
    ol_listClosed = True
    htmlPath = root_dir + filename[:-4] + ".html"
    htmlFile = open(htmlPath,'w')
    #print("open:", filename)
    print("[makeHtml] file:", htmlPath)

    htmlFile.write("<!DOCTYPE html>\n<html lang=\"en\">\n<head>\n\t<meta charset=\"utf-8\"/>\n\t<style>\n\t\t:root { font-family: sans-serif; }\n\t\tp { white-space: pre-wrap; padding-left: 15px; }\n\t</style>\n\t<titel>" + filename[:-4] + "</titel>\n</head>\n<body>\n")

    with open("dcl-tiles/" + filename, 'r') as file:
        for line in file:
            #print(line.strip())
            if line.strip() == "" or line.strip().startswith("#"):
                pass

            elif notset and line.strip().startswith(": " + filename[:-4]):
                notset = False
                htmlFile.write("\t<h2>" + replaceItalic(boldFunction(line.strip())) + "</h2>\n")

            elif line.strip() in h2_List:
                if not ul_listClosed:
                    htmlFile.write("\t</ul>\n")
                    ul_listClosed = True
                if not ol_listClosed:
                    htmlFile.write("\t</ol>\n")
                    ol_listClosed = True

                htmlFile.write("\t<h2>" + boldFunction(line.strip()) + "</h2>\n")
            elif line.strip() in h4_List:
                if not ul_listClosed:
                    htmlFile.write("\t</ul>\n")
                    ul_listClosed = True
                if not ol_listClosed:
                    htmlFile.write("\t</ol>\n")
                    ol_listClosed = True

                htmlFile.write("\t<h4>" + boldFunction(line.strip()) + "</h4>\n")

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
    htmlFile = open(root_dir + "dcl-tiles.html",'w')
    print("[makeIndexHtml] file: " + root_dir + "dcl-tiles.html")
    htmlFile.write("<!DOCTYPE html>\n<html lang=\"en\">\n<head>\n\t<meta charset=\"utf-8\"/>\n\t<style>\n\t\t:root { font-family: sans-serif; }\n\t</style>\n\t<titel>LibreCAD Developer Help</titel>\n</head>\n<body>\n\t<h2>DCL Tiles</h2>\n\t<hr/>\n")

    index = 0
    for link in dclTiles:
        index += 1
        path = proto + root_dir + link
        htmlFile.write("\t<b><a href=\"" + path + ".html\" title=\"DCL Tiles " + link + "\">(" + link + ")</a></b><br/>\n")

    htmlFile.write("\t<br/>\n</body>\n</html>")
    htmlFile.close()

def makeDclHtml():
    notset = True
    ul_listClosed = True
    ol_listClosed = True
    htmlFile = open(root_dir + "dcl.html",'w')
    print("[makeIndexHtml] file: " + root_dir + "dcl.html")
    htmlFile.write("<!DOCTYPE html>\n<html lang=\"en\">\n<head>\n\t<meta charset=\"utf-8\"/>\n\t<style>\n\t\t:root { font-family: sans-serif; }\n\t\tp { white-space: pre-wrap; padding-left: 15px; }\n\t</style>\n\t<titel>LibreCAD Developer Help</titel>\n</head>\n<body>\n")

    with open("dcl-tiles/dcl.txt", 'r') as file:
        for line in file:
            #print(line.strip())
            if line.strip() == "" or line.strip().startswith("#"):
                pass

            elif line.strip() in h2_List:
                if not ul_listClosed:
                    htmlFile.write("\t</ul>\n")
                    ul_listClosed = True
                if not ol_listClosed:
                    htmlFile.write("\t</ol>\n")
                    ol_listClosed = True

                htmlFile.write("\t<h2>" + boldFunction(line.strip()) + "</h2>\n")
            elif line.strip() in h4_List:
                if not ul_listClosed:
                    htmlFile.write("\t</ul>\n")
                    ul_listClosed = True
                if not ol_listClosed:
                    htmlFile.write("\t</ol>\n")
                    ol_listClosed = True

                htmlFile.write("\t<h4>" + boldFunction(line.strip()) + "</h4>\n")

            elif "____" in line.strip():
                htmlFile.write("\t<hr/>\n")

            elif line.strip().startswith("*"):
                if ul_listClosed:
                    htmlFile.write("\t<ul>\n")
                    ul_listClosed = False
                if not ol_listClosed:
                    htmlFile.write("\t</ol>\n")
                    ol_listClosed = True
                htmlFile.write("\t\t<li>" + replaceItalic(boldFunction(replaceInlineLink(line.strip()[1:].strip()))) + "</li></br>\n")

            elif line.strip()[0] in "123456789" and line.strip()[1] in ".":
                if ol_listClosed:
                    htmlFile.write("\t<ol>\n")
                    ol_listClosed = False
                if not ul_listClosed:
                    htmlFile.write("\t</ul>\n")
                    ul_listClosed = True
                htmlFile.write("\t\t<li>" + replaceItalic(boldFunction(replaceInlineLink(line.strip()[1:].strip()[2:]))) + "</li></br>\n")

            elif line.strip().startswith("[link]"):
                #print("[link] line:",line)
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


    htmlFile.write("\t<br/>\n</body>\n</html>")
    htmlFile.close()

def main():
    current_directory = os.getcwd()
    final_directory = os.path.join(current_directory, root_dir)
    if not os.path.exists(final_directory):
        os.makedirs(final_directory)

    for i in dclTiles:
        if i == "DCL":
            continue
        makeHtml(i + ".txt")

    makeIndexHtml()
    makeDclHtml()

if __name__ == "__main__":
    #main()
    makeDclHtml()
