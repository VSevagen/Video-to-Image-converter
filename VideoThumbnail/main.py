# Execute thumbnail.py first to generate the thumbnails
with open("thumbnail.py", "rb") as source_file:
    code = compile(source_file.read(), "thumbnail.py", "exec")
exec(code)

# Execute removeDup.py to remove the duplicates and similar images
with open("removeDup.py", "rb") as source_file:
    code = compile(source_file.read(), "removeDup.py", "exec")
exec(code)

prompt = int(input("Make a pdf out of the images 0(No) 1(Yes) >>>"))
if prompt == 1:
    with open("pdfMaker.py", "rb") as source_file:
        code = compile(source_file.read(), "pdfMaker.py", "exec")
    exec(code)