import os 
import subprocess

JPEXS_PATH = "E:\\Game\!Tool\\FFDEC\\ffdec.jar"
OUTPUT_PATH = "E:\Apps\swf2image\output"
INPUT_PATH = "C:\\Users\\Hartawan\\AppData\\Roaming\\"


root = os.getcwd()
dirName = ['items']
for type in dirName:
    os.chdir(INPUT_PATH+"\\"+type)
    targetFiles = [file for file in os.listdir() if file.endswith(('swf'))]
    for fname in targetFiles:
        output_dir = OUTPUT_PATH+'\\'+type+'\\'+fname.replace('.swf','')
        if not (os.path.exists(output_dir)):
            os.makedirs(output_dir)
        command = 'java -jar "'+JPEXS_PATH+'" -export shape "'+output_dir+'" "'+INPUT_PATH+'\\'+type+'\\'+fname+'"'
        subprocess.run(command)