from lum import assembly


#lets test all possible links, non github links, non secured etc

test_list = [
    "https://github.com/Far3000-YT/lumen", #normal link
    "http://github.com/Far3000-YT/lumen", #non secured (http)
    "github.com/Far3000-YT/lumen", #no https no www
    "www.github.com/Far3000-YT/lumen", #www only
    "https://www.github.com/Far3000-YT/lumen", #https and www
    "https://youtube.com", #non github link
    "https://github.com/Far3000-YT/lumen.git" #ends with .git
]

for test in test_list: #see if we can make link
    result = assembly.make_github_api_link(test)
    print(result)

print("\n\n")

for test in test_list: #see if we can send a request well
    result = assembly.check_repo(test)
    print(result)