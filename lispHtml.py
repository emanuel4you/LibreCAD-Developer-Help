#!/usr/bin/env python3

import os

funcs = ("+", "-", "*", "/", "=", "/=", "<", "<=", ">", ">=", "~", "%", "1+", "1-", "abs", "action_tile", "add_list", "alert", "and", "append", "apply", "ascii", "assoc", "atan", "atof", "atoi", "atom", "atom?", "boolean?", "bound?", "boundp", "caddr", "cadr", "cdr", "car", "chr", "close", "command", "concat", "cond", "conj", "cons", "contains?", "copyright", "cos", "count", "credits", "debug-eval", "def!", "defmacro!", "defun", "deref", "dimx_tile", "dimy_tile", "dissoc", "done_dialog", "do", "double?", "empty?", "end_image", "end_list", "entdel", "entget", "entlast", "entnext", "eval", "exit", "exp", "expt", "false?", "file?", "fill_image", "first", "fix", "float", "fn?", "fn*", "foreach", "get", "getangle", "get_attr", "getcorner", "getdist", "getenv", "getfiled", "getint", "getkword", "getorient", "getpoint", "getreal", "getstring", "get_tile", "getvar", "hash-map", "help", "if", "initget", "integer?", "keys", "keyword", "keyword?", "last", "length", "let*", "license", "list", "list?", "listp", "lambda", "load", "load_dialog", "load-file", "log", "log10", "logand", "macro?", "map", "map?", "max", "member?", "meta", "min", "minus?", "minusp", "mode_tile", "new_dialog", "nil?", "not", "nth", "null", "number?", "numberp", "open", "or", "pix_image", "polar", "prin1", "princ", "print", "println", "prn", "progn", "prompt", "pr-str", "py-eval-float", "py-eval-integer", "py-eval-string", "py-eval-value","py-eval-vector", "py-simple-file", "py-simple-string", "quasiquote", "quote", "rand", "rand-int", "read-char", "read-line", "read-string", "rem", "repeat", "reset!", "rest", "reverse", "seq", "sequential?", "set", "setq", "set_tile", "setvar", "sin", "slide_image", "slurp", "sqrt", "startapp", "start_dialog", "start_image", "start_list", "str", "strcase", "strcat", "string?", "strlen", "subst", "substr", "swap!", "symbol", "symbol?", "tan", "term_dialog", "terpri", "text_image", "throw", "time-ms", "timeout", "trace", "true?", "try*", "type", "type?", "unload_dialog", "untrace", "vals", "vec", "vector", "vector?", "vector_image", "ver", "vl-consp", "vl-directory-files", "vl-file-copy", "vl-file-delete", "vl-file-directory-p", "vl-filename-base", "vl-filename-directory", "vl-filename-extension", "vl-filename-mktemp", "vl-file-rename", "vl-file-size", "vl-file-systime", "vl-mkdir", "vl-position", "wcmatch", "while", "with-meta", "write-char", "write-line", "zero?", "zerop")

func_alias = ("addition_operator", "subtraction_operator", "multiplication_operator", "division_operator", "equal_to_operator", "not_equal_to_operator", "less_than_operator", "less_than_or_equal_to_operator", "greater_than_operator", "greater_than_or_equal_to_operator", "1s_compliment", "modulo_operator", "1+", "1-", "abs", "action_tile", "add_list", "alert", "and", "append", "apply", "ascii", "assoc", "atan", "atof", "atoi", "atom", "atom_q", "boolean_q", "bound_q", "boundp", "caddr", "cadr", "cdr", "car", "chr", "close", "command", "concat", "cond", "conj", "cons", "contains_q", "copyright", "cos", "count", "credits", "debug-eval", "def", "defmacro", "defun", "deref", "dimx_tile", "dimy_tile", "dissoc", "done_dialog", "do", "double_q", "empty_q", "end_image", "end_list", "entdel", "entget", "entlast", "entnext", "eval", "exit", "exp", "expt", "false_q", "file_q", "fill_image", "first", "fix", "float", "fn_q", "fn", "foreach", "get", "getangle", "get_attr", "getcorner", "getdist", "getenv", "getfiled", "getint", "getkword", "getorient", "getpoint", "getreal", "getstring", "get_tile", "getvar", "hash-map", "help", "if", "initget", "integer_q", "keys", "keyword", "keyword_q", "last", "length", "let", "license", "list", "list_q", "listp", "lambda", "load", "load_dialog", "load-file", "log", "log10", "logand", "macro_q", "map", "map_q", "max", "member_q", "meta", "min", "minus_q", "minusp", "mode_tile", "new_dialog", "nil_q", "not", "nth", "null", "number_q", "numberp", "open", "or", "pix_image", "polar", "prin1", "princ", "print", "println", "prn", "progn", "prompt", "pr-str", "py-eval-float", "py-eval-integer", "py-eval-string", "py-eval-value", "py-eval-vector", "py-simple-file", "py-simple-string", "quasiquote", "quote", "rand", "rand-int", "read-char", "read-line", "read-string", "rem", "repeat", "reset", "rest", "reverse", "seq", "sequential_q", "set", "setq", "set_tile", "setvar", "sin", "slide_image", "slurp", "sqrt", "startapp", "start_dialog", "start_image", "start_list", "str", "strcase", "strcat", "string_q", "strlen", "subst", "substr", "swap", "symbol", "symbol_q", "tan", "term_dialog", "terpri", "text_image", "throw", "time-ms", "timeout", "trace", "true_q", "try", "type", "type_q", "unload_dialog", "untrace", "vals", "vec", "vector", "vector_q", "vector_image", "ver", "vl-consp", "vl-directory-files", "vl-file-copy", "vl-file-delete", "vl-file-directory-p", "vl-filename-base", "vl-filename-directory", "vl-filename-extension", "vl-filename-mktemp", "vl-file-rename", "vl-file-size", "vl-file-systime", "vl-mkdir", "vl-position", "wcmatch", "while", "with-meta", "write-char", "write-line", "zero_q", "zerop", "lisp-compatibility")

h2_List = ("LISP Functions", "LISP Compatibility")
h4_List = ("NOTE", "NOTES", "Valid Attributes", "EXAMPLES", "EXAMPLE", "More about...", "Functions Unique to LibreLisp", "Functions Not Supported by LibreCAD")

root_dir = "html/lisp/"

proto = "qrc:/"

bold_List = (
"LibreCAD",
"LibreLisp",
"LibreDcl",
"AutoLISP",
"DCL",
"Clojure",
"LISP",
"Lisp",
)

developer_urls = (
(proto + root_dir + "lisp-functions.html", "LISP Functions"),
(proto + root_dir + "lisp.html", "Programming Overview of the LISP (LISt Processing) Language"),
(proto + root_dir + "lisp-compatibility.html", "LISP Compatibility"),
(proto + root_dir + "lisp-functions.html", "LISP Functions"),
("qrc:/html/python/python.html", "Programming Overview of the Python Language"),
("qrc:/html/python/python-functions.html", "Python Functions"),
("qrc:/html/dcl-tiles/dcl.html", "Overview of the DCL (Dialog Control Language)"),
("qrc:/html/dcl-tiles/dcl-tiles.html", "DCL Tiles"),
("qrc:/html/predefined-attributes/predefined-attributes.html", "Predefined Attributes"),
("qrc:/html/predefined-attributes/about-predefined-attributes.html", "About Predefined Attributes"),
("https://github.com/emanuel4you/LibreCAD-Developer-Examples", "Code Examples from the LibreCAD Developer Reference")
)

def replaceInlineLink(line):
    line = line.strip()
    replaceList = []
    if "[link]" in line:
        #print("[replaceInlineLink] found link!")
        pos = list(i for i in range(len(line)-6) if line[i] + line[i+1] + line[i+2] + line[i+3] + line[i+4] + line[i+5] == "[link]")
        #print("[replaceInlineLink] pos:", pos)
        for i in pos:
            #print("[replaceInlineLink] i:", i)
            link = line[i+6:].split()[0]
            #print("[replaceInlineLink] link:", link)
            if link in funcs:
                index = func_alias.index(link)
                alias = funcs[index]
                replaceList.append((link, alias))

        for link in funcs:
            if "[link]" + link in line:
                #print("[replaceInlineLink] link:", link)
                index = func_alias.index(link)
                alias = funcs[index]
                replaceList.append((link, alias))

        if len(replaceList):
            for func, link in replaceList:
                link = proto + root_dir + link
                func.replace("(","")
                func.replace(")","")
                line = line.replace("[link]" + func , "<a href=\"" + link + ".html\" title=\"LISP Function (" + func + ")\">(" + func + ")</a>")

    return line

def replaceLink(line):
    whites = len(line[:len(line)-len(line.lstrip())])
    link = line.strip()[6:]
    print("link 1:",link)

    if link.startswith("("):
        link = link[1:]
    print("link 2:",link)

    link = link.split(" ")[0]
    print("link 3:",link)

    if link.endswith(")"):
        link = link[:-1]
    print("link 4:",link)

    para = "<p>"
    if whites > 3:
        para = "<p style=\"padding-left: " + str(whites*5) + "px;\">"

    for url, name in developer_urls:
        if name in line:
            return "\t<b>" + para + "<a href=\"" + url + "\" title=\"" + name + "\">" + name + "</a></p></b>\n"

    if link in funcs:
        index = funcs.index(link)
        link = proto + root_dir + func_alias[index]
    else:
        return link

    return "\t<b>" + para + "<a href=\"" + link + ".html\" title=\"LISP Function (" + line.strip()[6:].replace("(","").replace(")","") + ")\">" + line.strip()[6:] + "</a></p></b>\n"

def replaceItalic(line):
    #line = line.replace("true", "<i>true</i>")
    #line = line.replace("T", "<i>T</i>")
    #line = line.replace("false", "<i>false</i>")
    #line = line.replace("nil", "<i>nil</i>")
    return line

def boldFunction(line):
    line = line.strip()
    if "(" in line and ")" in line:
        #print("found function!")
        link = line[line.index("("):][:line.index(")")][1:].split(" ")[0]
        if link.endswith(")"):
            link = link[:-1]
        #print("bold link:", link)
        #if link in funcs:
        #    line = line.replace(link, "<b>" + link + "</b>")

        for link in funcs:
            if "(" + link + " " in line:
                #print("found:", link, line)
                line = line.replace("(" + link + " ", "(<b>" + link + "</b> ")

        for link in funcs:
            if "(" + link + ")" in line:
                #print("found:", link, line)
                line = line.replace("(" + link + ")", "(<b>" + link + "</b>)")
    else:
        both=set(funcs).intersection(line)
        #print("both:", both)
        for link in funcs:
            if link in both:
                #print (link, "in line")
                line.replace("(" + link, "(<b>" + link + "</b>")

    for i in bold_List:
        line = line.replace(i, "<b>" + i + "</b>")

    line = line.replace("<b></b>","")



    return line

def makeHtml(filename):
    notset = True
    ul_listClosed = True
    ol_listClosed = True
    tableClosed = True
    htmlPath = root_dir + filename[:-4] + ".html"
    htmlFile = open(htmlPath,'w')
    #print("open:", filename)
    print("[makeHtml] file:", htmlPath)

    htmlFile.write("<!DOCTYPE html>\n<html lang=\"en\">\n<head>\n\t<meta charset=\"utf-8\"/>\n\t<style>\n\t\t:root { font-family: sans-serif; }\n\t\tp { white-space: pre-wrap; padding-left: 15px; }\n\t\tth { text-align: left; }\n\t</style>\n\t<titel>" + filename[:-4] + "</titel>\n</head>\n<body>\n")

    with open("lisp/" + filename, 'r') as file:
        for line in file:
            #print(line.strip())
            if line.strip() == "" or line.strip().startswith("#"):
                pass

            elif notset and line.strip().startswith("(" + filename[:-4]):
                notset = False
                htmlFile.write("\t<h2>" + line.strip() + "</h2>\n")

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
    htmlFile = open(root_dir + "lisp-functions.html",'w')
    print("[makeIndexHtml] file: " + root_dir + "lisp-functions.html")
    htmlFile.write("<!DOCTYPE html>\n<html lang=\"en\">\n<head>\n\t<meta charset=\"utf-8\"/>\n\t<style>\n\t\t:root { font-family: sans-serif; width: 800px; }\n\t</style>\n\t<titel>LibreCAD Developer Help</titel>\n</head>\n<body>\n\t\n\t<hr/>\n<h2>Lisp Functions</h2>\n\t<hr/>\n")

    index = 0
    for func in funcs:
        link = proto + root_dir + func_alias[index]
        index += 1
        htmlFile.write("\t<b><a href=\"" + link + ".html\" title=\"LISP Function (" + func + ")\">(" + func + ")</a></b><br/>\n")

    htmlFile.write("</body>\n</html>")
    htmlFile.close()

def main():
    current_directory = os.getcwd()
    final_directory = os.path.join(current_directory, root_dir)
    if not os.path.exists(final_directory):
        os.makedirs(final_directory)

    for i in func_alias:
        makeHtml(i + ".txt")

    makeIndexHtml()

if __name__ == "__main__":
    main()
