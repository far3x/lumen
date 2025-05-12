from lum import smart_read

actual_content = """#LINE 1
#line2
#


#tsting spaces, utf or anything that could not be put in a string èèéé^^

\""";;::
12test
()()((()(())))
%%
$$**//\\\ will the double slash show as a single slash or as a double when read
\"""

#<>²²<([])>


#i think thats enough to read, now we test"""




content = smart_read.read_file("tests/file_to_read.py")
print("Test 1")
assert content == actual_content, f"Content different ! Content : {content}"
#if no output, then the read file was working well !

ipynb = smart_read.read_file("tests/test_ipynb.ipynb")
print("Test 2")
print(ipynb)
#make sure the ipynb file clearly shows the python cells + markdowns, and nothing else (no graphs or wtv)