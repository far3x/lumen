from ptap import file_reader

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



content = file_reader.read_file("tests/file_to_read.py")

assert content == actual_content, f"Content different ! Content : {content}"