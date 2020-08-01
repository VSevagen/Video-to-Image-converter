# Execute thumbnail.py first to generate the thumbnails
with open("thumbnail.py", "rb") as source_file:
    code = compile(source_file.read(), "thumbnail.py", "exec")
exec(code)

# Execute removeDup.py to remove the duplicates and similar images
with open("removeDup.py", "rb") as source_file:
    code = compile(source_file.read(), "removeDup.py", "exec")
exec(code)

#Remove duplicates without down-sizing the images
with open("remove.py", "rb") as source_file:
    code = compile(source_file.read(), "remove.py", "exec")
exec(code)

facePrompt = int(input("Do you want to remove pictures that have 1 or more faces of a certain dimension 0(No) 1(Yes) >>> "))
if facePrompt == 1:
    with open("faceDetection.py", "rb") as source_file:
        code = compile(source_file.read(), "faceDetection.py", "exec")
    exec(code)

prompt = int(input("Make a pdf out of the images 0(No) 1(Yes) >>>"))
if prompt == 1:
    with open("pdfMaker.py", "rb") as source_file:
        code = compile(source_file.read(), "pdfMaker.py", "exec")
    exec(code)
