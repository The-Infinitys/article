import os
import datetime
from sys import exit
import json
def listfolders(dir_path):
  result = [
      f for f in os.listdir(dir_path) if os.path.isdir(os.path.join(dir_path, f))
  ]
  return result
def listfiles(dir_path):
  result = [
      f for f in os.listdir(dir_path) if os.path.isfile(os.path.join(dir_path, f))
  ]
  return result
now=datetime.datetime.now()
json_files_name="./index/"+str(now.year)+"-"+str(now.month)+".json"
result_obj={"info":[]}
root_dir="./"
def end():
  f=open(json_files_name,mode="w")
  f.write(json.dumps(result_obj,indent=2))
  print(json.dumps(result_obj,indent=2))
  f.close()

def renew():
  os.system("git config user.name github-actions")
  os.system("git config user.email github-actions@github.com")
  os.system("git add .")
  os.system("git commit -m \"made with Infinity Style Static Site Generator\"")
  os.system("git push")
#プログラムの実行
if not os.path.isdir(root_dir):
  print("No datas")
  exit()
for article_dir in listfolders(root_dir):
  path = root_dir+"/"+article_dir
  file_names = listfiles(path)
  index_path = None
  thumbnail_path = None
  for file_name in file_names:
    if file_name.startswith("index"):
      index_path=file_name
    elif file_name.startswith("thumbnail"):
      thumbnail_path = file_name
  if index_path == None or thumbnail_path == None:
    print("Something was losted: at "+path)
  else:
    article_data=open(path+"/"+index_path)
    article_text=article_data.read()
    article_data.close()
    title=article_text[article_text.find("<title>")+7:article_text.find("</title>")]
    title=title.encode("unicode-escape").decode("unicode-escape")
    add_path="/"+root_dir.replace("./","")+"/"+article_dir+"/"
    result_obj["info"].append({"index":add_path,"thumbnail":add_path+thumbnail_path,"name":article_dir,"title":title})
end()
renew()