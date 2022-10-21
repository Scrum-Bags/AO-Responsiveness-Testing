import os
# for root, dirs, files in os.walk("..", topdown=False):
#    for name in files:
#       print(os.path.join(root, name))
#    for name in dirs:
#       print(os.path.join(root, name))

# ../.screenshots/SwagLabsHeadlessWebSize/
# ..\.screenshots\SwagLabsHeadlessWebSize\

imageFolders = []
imageFolders.append("SwagLabsHeadlessWebSize")

for folder in imageFolders:
    for image in os.listdir("../.screenshots/"+folder+"/"):
        print(image)
    print(folder)
