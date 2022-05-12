#!/usr/bin/python3

import os, shutil, markdown

# get sourceFolder, templateHTML, and output dir from program args
# TO DO: fix these from being hardcoded
source_folder = "exampleFolder"
template_HTML = "template.html"
output_dir = "output"

# delete output dir if it exists
if os.path.exists(output_dir):
    shutil.rmtree(output_dir, ignore_errors=True)

# make output dir
os.mkdir(output_dir)

# recursively for each file in sourceFolder explore subdirectories

# for every file, recreate it inside output dir with templatedHTML replaced
# with source stuff

def generateStaticHTML(template_text, output_dir, source_folder, cur_path="/"):
    print(f"searching folder: {source_folder+cur_path}")
    for file_name in os.listdir(source_folder+cur_path):
        file_dir = source_folder+cur_path+file_name
        if os.path.isdir(file_dir):
            #make path in output
            os.mkdir(output_dir+cur_path+file_name)
            generateStaticHTML(template_text, output_dir, source_folder, cur_path+file_name+"/")
        else:
            markdown_content = ""
            with open(source_folder+cur_path+file_name) as markdown_file:
                markdown_content = markdown_file.read()
            markdown_content = markdown.markdown(markdown_content)
            new_file_name = file_name.split(".")[0]+".html"
            with open(output_dir+cur_path+new_file_name, "w") as page:
                page.write( template_text.replace("{{content}}", markdown_content) )
            print(f"found file: {file_dir}")

template_text = ""
with open(template_HTML) as template_file:
    template_text = template_file.read()

generateStaticHTML(template_text, output_dir, source_folder)
