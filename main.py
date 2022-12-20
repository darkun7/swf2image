import os 
import subprocess

JPEXS_PATH = "E:\\Game\!Tool\\FFDEC\\ffdec.jar"
RESULT_PATH = "E:\\decompile\\result"
INPUT_PATH = "E:\\decompile\\input"

root = os.getcwd()
dirName = ['items']
for type in dirName:
    os.chdir(root+"\\"+"input\\"+type)
    targetFiles = [file for file in os.listdir() if file.endswith(('swf'))]
    for fname in targetFiles:
    
        res_target = RESULT_PATH+'\\'+type+'\\1.png'
        res_rename = RESULT_PATH+'\\'+type+'\\'+fname.replace('.swf','.png')
        command = 'java -jar "'+JPEXS_PATH+'" -export frame "'+RESULT_PATH+'\\'+type+'" "'+INPUT_PATH+'\\'+type+'\\'+fname+'" -select 1'
        subprocess.run(command)
        os.rename(res_target,res_rename)
    