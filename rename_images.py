import os
os.getcwd()
collection = "E:/GIT_HUB_ALL_REPOSITORY/OBJECT_DETECTION/IMAGES/"
for i, filename in enumerate(os.listdir(collection)):
    os.rename("E:/GIT_HUB_ALL_REPOSITORY/OBJECT_DETECTION/IMAGES/" + filename, "E:/GIT_HUB_ALL_REPOSITORY/OBJECT_DETECTION/IMAGES/" + "image_"+str(i) + ".jpg")