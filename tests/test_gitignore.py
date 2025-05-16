from lum import gitignore

print(gitignore.gitignore_exists(root = "")) #true
#running this from the project path, so there is a gitignore

print(gitignore.gitignore_exists(root = "tests")) #false
#here adding some folder like, going into tests and checking if there is a gitignore (tested by adding / removing gitignore from both root + folder path, works fine)

#gitignore.gitignore_read(root = "")
#testing line.strip if it works well (no more "\n")