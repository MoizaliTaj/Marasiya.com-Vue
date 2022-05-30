import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import sys

current_dir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__, template_folder="templates")
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///" + os.path.join(current_dir, "database.sqlite3")
db = SQLAlchemy()
db.init_app(app)
app.app_context().push()

class File_Info(db.Model):
    __tablename__ = 'file_info'
    title = db.Column(db.String, nullable=False)
    file_name = db.Column(db.String, nullable=False)
    file_id = db.Column(db.String, primary_key=True)
    category = db.Column(db.String, nullable=False)
    type = db.Column(db.String, nullable=False)

def categorylist():
    categorydata = File_Info.query.with_entities(File_Info.category).order_by(File_Info.category).distinct()
    categorylist = []
    for i in categorydata:
        categorylist.append(i[0])
    return categorylist

def titlelist(category):
    titlesdata = File_Info.query.filter_by(category=category).with_entities(File_Info.title).order_by(File_Info.title).distinct()
    titlelist = []
    for i in titlesdata:
        titlelist.append(i[0])
    return titlelist
def kalaamdetails(category,title,type):
    kalaamdata = File_Info.query.filter_by(category=category,title=title,type=type).with_entities(File_Info.file_name,File_Info.file_id).order_by(File_Info.file_name).all()
    if (kalaamdata):
        kalaamoutcome=[]
        for i in kalaamdata:
            kalaamoutcome.append(i)
        return kalaamoutcome
    else:
        return "None"


def titlecount(category):
    titlecount = File_Info.query.filter_by(category=category).with_entities(File_Info.title).order_by(File_Info.title).distinct().count()
    return titlecount

def audiocount(category):
    audiocount = File_Info.query.filter_by(category=category,type="Audio").with_entities(File_Info.file_name).order_by(File_Info.file_name).distinct().count()
    return audiocount

def pdfcount(category):
    pdfcount = File_Info.query.filter_by(category=category,type="PDF").with_entities(File_Info.file_name).order_by(File_Info.file_name).distinct().count()
    return pdfcount

def sitemap_xml():
    urls = ['http://marasiya.com/#/']
    categorydata = File_Info.query.with_entities(File_Info.category).order_by(File_Info.category).distinct()
    categorylist = []
    for i in categorydata:
        categorylist.append(i[0])
    page_list = []
    for i in categorylist:
        page_list.append((i,i))
        urls.append('http://marasiya.com/#/'+str(i))
    for a in page_list:
        title_data = File_Info.query.filter_by(category=a[0]).with_entities(File_Info.title).distinct().order_by(File_Info.title).all()
        for i in title_data:
            urls.append('http://marasiya.com/#/'+str(a[1])+'/'+i[0].replace(' ','%20'))
    xml_content = '''<?xml version="1.0" encoding="UTF-8"?>
<urlset 
      xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"
      xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
      xmlns:xhtml="http://www.w3.org/1999/xhtml"
      xsi:schemaLocation="http://www.sitemaps.org/schemas/sitemap/0.9
http://www.sitemaps.org/schemas/sitemap/0.9/sitemap.xsd
http://www.w3.org/1999/xhtml
http://www.w3.org/2002/08/xhtml/xhtml1-strict.xsd">

'''
    from datetime import datetime

    for i in urls:
        priority_count = i.count('/')
        if priority_count == 2:
            priority = 1.00
        elif priority_count == 3:
            priority = 0.80
        elif priority_count == 4:
            priority = 0.64
        date_time = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S+00:00')
        Out_inst = '<url>\n  <loc>' + i + '</loc>\n  <lastmod>' + str(date_time) + '</lastmod>\n  <priority>' + str(
            priority) + '</priority>\n</url>\n'
        xml_content = xml_content + Out_inst
    xml_content = xml_content + '\n</urlset>'
    temp = open("../sitemap.xml","w")
    temp.write(xml_content)
    temp.close()


file = open("../static/app.js","r")
lines = file.readlines()
file.close()

firstline = ""
firstline = firstline + "let database = ["
categoryss = categorylist()
for a in categoryss:
    category = a
    titles = titlelist(category)
    firstline = firstline + '{category:"'+str(category)+'",data:['
    for i in titles:
        firstline = firstline + '{title:"'+str(i)+'",'
        audioinfo = kalaamdetails(category, i, "Audio")
        if audioinfo == "None":
            firstline = firstline + "audio:[],"
        else:
            firstline = firstline + "audio:["
            for k in audioinfo:
                firstline = firstline + '{filename:"'+str(k[0])+'",audiolink:"https://docs.google.com/uc?export=download&id='+str(k[1])+'",downloadlink:"https://drive.google.com/uc?authuser=0&id='+str(k[1])+'&export=download"},'
            firstline = firstline + "],"
        pdfinfo = kalaamdetails(category, i, "PDF")
        if pdfinfo == "None":
            firstline = firstline + "pdf:[],"
        else:
            firstline = firstline + "pdf:["
            for k in pdfinfo:
                firstline = firstline + '{filename:"' + str(k[0]) + '",pdflink:"https://drive.google.com/file/d/' + str(k[1]) + '/preview",downloadlink:"https://drive.google.com/uc?authuser=0&id=' + str(k[1]) + '&export=download"},'
            firstline = firstline + "],"
        firstline = firstline + "},"
    firstline = firstline + "],},"
firstline = firstline + "]"
category = categorylist()
outstring="let titledata = {"
for i in category:
    outstring = outstring+(str(i)+"Title:"+str(titlecount(i))+",")+(str(i) + "Audio:" + str(audiocount(i))+",")+(str(i) + "PDF:" + str(pdfcount(i))+",")
outstring=outstring+"}"
updatedstring = ""
for j in outstring:
    if j == '-':
        updatedstring = updatedstring + '_'
    else:
        updatedstring = updatedstring + j
secondline = updatedstring
lines[0] = firstline + "\n"
lines[1] = secondline + "\n"
file = open("../static/app.js","w")
file.writelines(lines)
sitemap_xml()