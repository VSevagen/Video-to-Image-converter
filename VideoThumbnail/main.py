# Execute thumbnail.py first to generate the thumbnails
with open("thumbnail.py", "rb") as source_file:
    code = compile(source_file.read(), "thumbnail.py", "exec")
exec(code)

# Execute removeDup.py to remove the duplicates and similar images
with open("removeDup.py", "rb") as source_file:
    code = compile(source_file.read(), "removeDup.py", "exec")
exec(code)