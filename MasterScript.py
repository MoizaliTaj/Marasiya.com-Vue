import pandas as pd
import datetime

MasterDB = []
date = str(datetime.datetime.now())[0:10]
class siteData():

    def __init__(self):
        self.Data_Dict = {}

    def getData(self):
        return self.Data_Dict

    def addEntry(self,Title,File_Name,File_ID,Type):
        if Title in self.Data_Dict.keys():
            if Type == 'Audio':
                self.Data_Dict[Title][0].append((File_Name,File_ID))
            elif Type == 'PDF':
                self.Data_Dict[Title][1].append((File_Name, File_ID))
        else:
            self.Data_Dict[Title] = [[],[]]
            if Type == 'Audio':
                self.Data_Dict[Title][0].append((File_Name,File_ID))
            elif Type == 'PDF':
                self.Data_Dict[Title][1].append((File_Name, File_ID))


def sheet_names(filename):
    xls = pd.ExcelFile(filename)
    sheets = xls.sheet_names
    return sheets


def Sheet_To_DB(fileName,sheetName):
    ExcelRead = pd.read_excel(fileName,sheet_name=sheetName,engine='openpyxl',dtype=object,header=None)
    ExcelData = ExcelRead.values.tolist()
    globals()[sheetName] = siteData()
    for index in range(1,len(ExcelData)):
        globals()[sheetName].addEntry(ExcelData[index][0],ExcelData[index][1],ExcelData[index][2],ExcelData[index][3])
    global MasterDB
    MasterDB.append((sheetName,globals()[sheetName].getData()))

def update_MasterDB():
    for Sheet in sheet_names("ExcelDB.xlsx"):
        Sheet_To_DB("ExcelDB.xlsx",Sheet)

def categorylist():
    global MasterDB
    categorylist = []
    for DB in MasterDB:
        categorylist.append(DB[0])
    return categorylist

def titlelist(category):
    global MasterDB
    titlelist = []
    for DB in MasterDB:
        if DB[0] == category:
            category_data = DB[1]
            for titles in category_data.keys():
                titlelist.append(titles)
    return titlelist

def kalaamdetails(category,title,type):
    try:
        global MasterDB
        for DB in MasterDB:
            if DB[0] == category:
                category_data = DB[1]
        for titles in category_data.keys():
            if title == titles:
                title_data = category_data[titles]
        if type == 'Audio':
            if len(title_data[0]) > 0:
                return title_data[0]
        elif type == 'PDF':
            if len(title_data[1]) > 0:
                return title_data[1]
        return "None"
    except:
        return "None"


def titlecount(category):
    global MasterDB
    for DB in MasterDB:
        if DB[0] == category:
            category_data = DB[1]
    return len(category_data.keys())

def audiocount(category):
    global MasterDB
    audiocounter = 0
    for DB in MasterDB:
        if DB[0] == category:
            category_data = DB[1]
    for titles in category_data.keys():
        audiocounter += len(category_data[titles][0])
    return audiocounter

def pdfcount(category):
    global MasterDB
    pdfcounter = 0
    for DB in MasterDB:
        if DB[0] == category:
            category_data = DB[1]
    for titles in category_data.keys():
        pdfcounter += len(category_data[titles][1])
    return pdfcounter

def sitemap_xml():
    global MasterDB
    outputdata = '<?xml version="1.0" encoding="UTF-8"?>\n'
    outputdata += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    outputdata += "\t<url>\n"
    outputdata += "\t\t<loc>http://www.marasiya.com/#/</loc>\n"
    outputdata += "\t\t<lastmod>"+date+"</lastmod>\n"
    outputdata += "\t\t<priority>1</priority>\n"
    outputdata += "\t</url>\n"
    for DB in MasterDB:
        outputdata += "\t<url>\n"
        outputdata += "\t\t<loc>http://www.marasiya.com/#/"+DB[0]+"</loc>\n"
        outputdata += "\t\t<lastmod>"+date+"</lastmod>\n"
        outputdata += "\t\t<priority>0.8</priority>\n"
        outputdata += "\t</url>\n"
    for DB in MasterDB:
        for Title in DB[1]:
            outputdata += "\t<url>\n"
            outputdata += "\t\t<loc>http://www.marasiya.com/#/" + DB[0] +"/"+Title.replace(" ","%20")+ "</loc>\n"
            outputdata += "\t\t<lastmod>" + date + "</lastmod>\n"
            outputdata += "\t\t<priority>0.6</priority>\n"
            outputdata += "\t</url>\n"
    outputdata += '</urlset>\n'
    sitemap = open("Site/sitemap.xml", "w", encoding="utf-8")
    sitemap.writelines(outputdata)


def databaseGenerator():
    database = ""
    database += "let database = ["
    categoryss = categorylist()
    for a in categoryss:
        category = a
        titles = titlelist(category)
        database += '{'
        database += 'category:"' + str(category) + '",'
        database += 'data:['
        for i in titles:
            database += '{'
            database += 'title:"' + str(i) + '",'
            audioinfo = kalaamdetails(category, i, "Audio")
            if audioinfo == "None":
                database += "audio:[],"
            else:
                database += "audio:["
                for k in audioinfo:
                    database += '{filename:"' + str(k[0]) + '",'
                    database += 'audioid:"' + str(k[1]) + '"},'
                database += "],"
            pdfinfo = kalaamdetails(category, i, "PDF")
            if pdfinfo == "None":
                database += "pdf:[],"
            else:
                database += "pdf:["
                for k in pdfinfo:
                    database += '{filename:"' + str(k[0]) + '",'
                    database += 'pdfid:"' + str(k[1]) + '"},'
                database += "],"
            database += "},"
        database += "],"
        database += "},"
    database += "]"
    return database

def titleDataGenerator():
    masterTitleCount = 0
    masterAudioCount = 0
    masterPDFCount = 0
    category = categorylist()
    outstring = "{"
    for i in category:
        masterTitleCount += titlecount(i)
        masterAudioCount += audiocount(i)
        masterPDFCount += pdfcount(i)
        outstring = outstring + (str(i) + "Title:" + str(titlecount(i)) + ",") + (str(i) + "Audio:" + str(audiocount(i)) + ",") + (str(i) + "PDF:" + str(pdfcount(i)) + ",")
    outstring = outstring + ("masterTitleCount:" + str(masterTitleCount) + ",") + ("masterAudioCount:" + str(masterAudioCount) + ",") + ("masterPDFCount:" + str(masterPDFCount) + ",")
    outstring = outstring + "}"
    updatedstring = ""
    for j in outstring:
        if j == '-':
            updatedstring += '_'
        else:
            updatedstring += j
    return updatedstring

static_JS_1 = """
const Navbar = Vue.component('navbar', {
    template:`
    <nav id="navbar" class="navbar navbar-expand-lg navbar-dark bg-black">
    <a class="navbar-brand" href="#">Marasiya.com</a>
    <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="true" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarSupportedContent">
      <ul class="navbar-nav mr-auto">
        <li class="nav-item"><router-link class="nav-link" to="/Marasiya">Marasiya</router-link></li>
        <li class="nav-item"><router-link class="nav-link" to="/Madeh">Madeh</router-link></li>
        <li class="nav-item"><router-link class="nav-link" to="/Rasa">Rasa</router-link></li>
        <li class="nav-item"><router-link class="nav-link" to="/Salaam">Salaam</router-link></li>
        <li class="nav-item"><router-link class="nav-link" to="/Manaqabat">Manaqabat</router-link></li>
        <li class="nav-item"><router-link class="nav-link" to="/Iltija">Iltija</router-link></li>
        <li class="nav-item"><router-link class="nav-link" to="/Nasihat">Nasihat</router-link></li>
        <li class="nav-item"><router-link class="nav-link" to="/Qasida">Qasida</router-link></li>
        <li class="nav-item"><router-link class="nav-link" to="/Naat">Naat</router-link></li>
        <li class="nav-item"><router-link class="nav-link" to="/Dua">Dua</router-link></li>
        <li class="nav-item"><router-link class="nav-link" to="/Quran-Chapters">Quran-Surat</router-link></li>
        <li class="nav-item"><router-link class="nav-link" to="/Quran-Juz">Quran-Juz</router-link></li>
        <li class="nav-item"><router-link class="nav-link" to="/Namaz">Namaz</router-link></li>
        <li class="nav-item"><router-link class="nav-link" to="/Misc">Misc</router-link></li>
      </ul>
    </div>
  </nav>`,
})

const Foot = Vue.component('foot', {
    template:`<footer class="bg-dark text-center text-white">Created by Moizali</footer>`,
})


const Home = Vue.component('home', {
    template: `
    <div><br>
        <p>Allah Syedna Mufaddal Saifudin Maula ne umar sharif ne sehat ane afiyat sathe ta roze qayamat tak daraz kare...</p>
        <p>This Site & App is designed for Dawoodi Bohra's.. With this site you can listen n download audio and read n download PDF of Marasiya, Madeh, Nasihat, Qasida, Salaam, Iltija, Manaqabat, Naat, Nazam, Dua, Matami Noha, Namaz Dua, Wuzu Dua, Quran's Surats and Many more... It contains approximately {{data.masterTitleCount}} Titles, {{data.masterAudioCount}} Audio files and {{data.masterPDFCount}} PDF and other text files</p>
        <p>List of content currently available on this website.</p>

        <li><router-link to="/Marasiya">مرثیہ | Marsiya</router-link></li>
        <div class="homesmall">Currently this section has {{data.MarasiyaTitle}} Titles, which includes {{data.MarasiyaAudio}} Audio files and {{data.MarasiyaPDF}} PDF files</div>

        <li><router-link to="/Madeh">مدح | Madeh</router-link></li>
        <div class="homesmall">Currently this section has {{data.MadehTitle}} Titles, which includes {{data.MadehAudio}} Audio files and {{data.MadehPDF}} PDF files.</div>

        <li><router-link to="/Rasa">Rasa - Syedna Mohammed Burhanuddin (R.A.)</router-link></li>
        <div class="homesmall">Currently this section has {{data.RasaTitle}} Titles, which includes {{data.RasaAudio}} Audio files and {{data.RasaPDF}} PDF files.</div>

        <li><router-link to="/Salaam">سلام | Salaam</router-link></li>
        <div class="homesmall">Currently this section has {{data.SalaamTitle}} Titles, which includes {{data.SalaamAudio}} Audio files and {{data.SalaamPDF}} PDF files.</div>

        <li><router-link to="/Manaqabat">مناقب | Manaqabat</router-link></li>
        <div class="homesmall">Currently this section has {{data.ManaqabatTitle}} Titles, which includes {{data.ManaqabatAudio}} Audio files and {{data.ManaqabatPDF}} PDF files.</div>

        <li><router-link to="/Iltija">التجا | Iltija</router-link></li>
        <div class="homesmall">Currently this section has {{data.IltijaTitle}} Titles, which includes {{data.IltijaAudio}} Audio files and {{data.IltijaPDF}} PDF files.</div>

        <li><router-link to="/Nasihat">نصيحة | Nasihat</router-link></li>
        <div class="homesmall">Currently this section has {{data.NasihatTitle}} Titles, which includes {{data.NasihatAudio}} Audio files and {{data.NasihatPDF}} PDF files.</div>

        <li><router-link to="/Qasida">قــصــائـد | Qasida</router-link></li>
        <div class="homesmall">Currently this section has {{data.QasidaTitle}} Titles, which includes {{data.QasidaAudio}} Audio files and {{data.QasidaPDF}} PDF files.</div>

        <li><router-link to="/Naat">نعت | Naat</router-link></li>
        <div class="homesmall">Currently this section has {{data.NaatTitle}} Titles, which includes {{data.NaatAudio}} Audio files and {{data.NaatPDF}} PDF files.</div>

        <li><router-link to="/Dua">دعاء | Dua</router-link></li>
        <div class="homesmall">Currently this section has {{data.DuaTitle}} Titles, which includes {{data.DuaAudio}} Audio files and {{data.DuaPDF}} PDF files.</div>

        <li><router-link to="/Quran-Chapters">القرآن الكريم | Quran Surat</router-link></li>
        <div class="homesmall">Currently this section has all {{data.Quran_ChaptersTitle}} Chapters, which includes {{data.Quran_ChaptersAudio}} Audio files and all {{data.Quran_ChaptersPDF}} Chapters available in text.</div>

        <li><router-link to="/Quran-Juz">القرآن الكريم | Quran Juz</router-link></li>
        <div class="homesmall">Currently this section has all {{data.Quran_JuzTitle}} Juz (Sipara), which includes {{data.Quran_JuzAudio}} Audio files and all {{data.Quran_JuzPDF}} Juz available in text.</div>

        <li><router-link to="/Namaz">وضؤ & نماز | Namaz and Wuzu </router-link></li>
        <div class="homesmall">Currently this section has {{data.NamazTitle}} Titles, which includes {{data.NamazAudio}} Audio files and {{data.NamazPDF}} dua's available in text.</div>

        <li><router-link to="/Misc">متفرقات | Miscellaneous </router-link></li>
        <div class="homesmall">This section includes content for which the category is not known. Currently this section has {{data.MiscTitle}} Titles, which includes {{data.MiscAudio}} Audio files and {{data.MiscPDF}} PDF files.</div>
        <br>
        <hr>
    </div>
    `,
    data: function() {
        return {
            data:"""

static_JS_2 = """
        }
    },
    mounted: async function() {
        document.querySelector('title').textContent = 'Home | Marasiya.com';
        
    },
})

const Kalaam = Vue.component('kalaam', {
    template: `
    <div><br>
        <div v-if="error == null && audioobject != null && pdfobject != null" >
            <div v-for="aud in audioobject">
                <h5>{{aud.filename}}</h5>
                <iframe :src=aud.audiolink width="350" height="60" allow="autoplay" ></iframe>
                <br>
                <a :href=aud.downloadlink target="_blank"><button class="button">Download Audio</button></a>
                <br><hr>
            </div>
            <div v-for="pdf in pdfobject">
                <iframe :src=pdf.pdflink width="100%" height="480" allow="autoplay"></iframe>
                <br>
                <a :href=pdf.downloadlink><button class="button">Download PDF</button></a>
                <br>
                <hr>
            </div>
        </div>
        <div v-else-if="error == null && audioobject != null && pdfobject == null" >
            <div v-for="aud in audioobject">
                <h5>{{aud.filename}}</h5>
                <iframe :src=aud.audiolink width="350" height="60" allow="autoplay" ></iframe>
                <br>
                <a :href=aud.downloadlink target="_blank"><button class="button">Download Audio</button></a>
                <br><hr>
            </div>
        </div>
        <div v-else-if="error == null && audioobject == null && pdfobject != null" >
            <div v-for="pdf in pdfobject">
                <iframe :src=pdf.pdflink width="100%" height="480" allow="autoplay"></iframe>
                <br>
                <a :href=pdf.downloadlink><button class="button">Download PDF</button></a>
                <br><hr><br>
            </div>
        </div>
        <div v-else-if="error == null && audioobject == null && pdfobject == null" >
        <h3> {{category}} </h3>
        No data found
        </div>
        <div v-else>
            This is not a valid url. redirecting to home.
        </div>
    </div>`,
    data: function() {
        return {
            category:null,
            categorylink:null,
            title:null,
            error:null,
            audioobject:null,
            pdfobject:null,
        }
    },
    mounted: async function() {
        this.category = this.$route.params.id;
        this.categorylink="/"+this.$route.params.id;
        this.title =  this.$route.params.ad;
        if(this.title == undefined){
            setTimeout(
                function() {
                    router.push("/")
                }, 2000);
        }
        else{
            let CurrentObject = null;
            for (let i=0;i < database.length;i++){
                if(database[i].category === this.category){
                    CurrentObject = database[i].data
                }
            }
            if (CurrentObject == null){
                this.error = "empty"
                setTimeout(
                    function() {
                        router.push("/")
                    }, 3000);
            }
            else {
                for(let j=0;j<CurrentObject.length;j++){
                    if (CurrentObject[j].title === this.title){;
                        if (CurrentObject[j].audio.length > 0){
                            tempaudioobject=[];
                            for(let audios=0;audios<CurrentObject[j].audio.length;audios++){
                                tempaudioobjectchild = {
                                                        filename:CurrentObject[j].audio[audios].filename,
                                                        audiolink:"https://drive.google.com/file/d/" + CurrentObject[j].audio[audios].audioid + "/preview",
                                                        downloadlink:"https://drive.google.com/uc?authuser=0&id=" + CurrentObject[j].audio[audios].audioid + "&export=download",
                                }
                                tempaudioobject.push(tempaudioobjectchild)
                            }
                            this.audioobject = tempaudioobject
                        }
                        if (CurrentObject[j].pdf.length > 0){
                            temppdfobject=[];
                            for(let pdfs=0;pdfs<CurrentObject[j].pdf.length;pdfs++){
                                temppdfobjectchild = {
                                                        filename:CurrentObject[j].pdf[pdfs].filename,
                                                        pdflink:"https://drive.google.com/file/d/" + CurrentObject[j].pdf[pdfs].pdfid + "/preview",
                                                        downloadlink:"https://drive.google.com/uc?authuser=0&id=" + CurrentObject[j].pdf[pdfs].pdfid + "&export=download",
                                }
                                temppdfobject.push(temppdfobjectchild)
                            }
                            this.pdfobject = temppdfobject;
                        }
                    }
                }
            }
            if (this.audioobject === null && this.pdfobject === null){
                var redirectval = this.category;
                setTimeout(
                    function() {
                        router.push("/"+redirectval)
                    }, 3000);
            }
        }
        document.querySelector('title').textContent = this.title + ' | ' + this.category + ' | ' + 'Marasiya.com';
        
        window.scrollTo(0, 0);
    },
})

const Dua = Vue.component('dua', {template: `<div><h3> {{componentname}} </h3><ol><li v-for="titleind in db"><router-link :to="{ path: titleind.path }">{{titleind.name}}</router-link></li></ol></div>`,
    data: function() {return {db: [],componentname:"Dua"}},
    mounted: async function() {rawdata = null;for (let i=0;i < database.length;i++){if(database[i].category === this.componentname){rawdata = database[i].data}}for(let j=0;j<rawdata.length;j++){tempobj = {name: rawdata[j].title,path: "/"+this.componentname+"/"+rawdata[j].title,};this.db.push(tempobj)}document.querySelector('title').textContent = this.componentname + ' | ' + 'Marasiya.com';},})

const Iltija = Vue.component('iltija', {template: `<div><h3> {{componentname}} </h3><ol><li v-for="titleind in db"><router-link :to="{ path: titleind.path }">{{titleind.name}}</router-link></li></ol><hr></div>`,
    data: function() {return {db: [],componentname:"Iltija"}},
    mounted: async function() {rawdata = null;for (let i=0;i < database.length;i++){if(database[i].category === this.componentname){rawdata = database[i].data}}for(let j=0;j<rawdata.length;j++){tempobj = {name: rawdata[j].title,path: "/"+this.componentname+"/"+rawdata[j].title,};this.db.push(tempobj)}document.querySelector('title').textContent = this.componentname + ' | ' + 'Marasiya.com';},})

const Madeh = Vue.component('madeh', {template: `<div><h3> {{componentname}} </h3><ol><li v-for="titleind in db"><router-link :to="{ path: titleind.path }">{{titleind.name}}</router-link></li></ol><hr></div>`,
    data: function() {return {db: [],componentname:"Madeh"}},
    mounted: async function() {rawdata = null;for (let i=0;i < database.length;i++){if(database[i].category === this.componentname){rawdata = database[i].data}}for(let j=0;j<rawdata.length;j++){tempobj = {name: rawdata[j].title,path: "/"+this.componentname+"/"+rawdata[j].title,};this.db.push(tempobj)}document.querySelector('title').textContent = this.componentname + ' | ' + 'Marasiya.com';},})

const Manaqabat = Vue.component('manaqabat', {template: `<div><h3> {{componentname}} </h3><ol><li v-for="titleind in db"><router-link :to="{ path: titleind.path }">{{titleind.name}}</router-link></li></ol><hr></div>`,
    data: function() {return {db: [],componentname:"Manaqabat"}},
    mounted: async function() {rawdata = null;for (let i=0;i < database.length;i++){if(database[i].category === this.componentname){rawdata = database[i].data}}for(let j=0;j<rawdata.length;j++){tempobj = {name: rawdata[j].title,path: "/"+this.componentname+"/"+rawdata[j].title,};this.db.push(tempobj)}document.querySelector('title').textContent = this.componentname + ' | ' + 'Marasiya.com';},})

const Marasiya = Vue.component('marasiya', {template: `<div><h3> {{componentname}} </h3><ol><li v-for="titleind in db"><router-link :to="{ path: titleind.path }">{{titleind.name}}</router-link></li></ol><hr></div>`,
    data: function() {return {db: [],componentname:"Marasiya"}},
    mounted: async function() {rawdata = null;for (let i=0;i < database.length;i++){if(database[i].category === this.componentname){rawdata = database[i].data}}for(let j=0;j<rawdata.length;j++){tempobj = {name: rawdata[j].title,path: "/"+this.componentname+"/"+rawdata[j].title,};this.db.push(tempobj)}document.querySelector('title').textContent = this.componentname + ' | ' + 'Marasiya.com';},})

const Misc = Vue.component('misc', {template: `<div><h3> {{componentname}} </h3><ol><li v-for="titleind in db"><router-link :to="{ path: titleind.path }">{{titleind.name}}</router-link></li></ol><hr></div>`,
    data: function() {return {db: [],componentname:"Misc"}},
    mounted: async function() {rawdata = null;for (let i=0;i < database.length;i++){if(database[i].category === this.componentname){rawdata = database[i].data}}for(let j=0;j<rawdata.length;j++){tempobj = {name: rawdata[j].title,path: "/"+this.componentname+"/"+rawdata[j].title,};this.db.push(tempobj)}document.querySelector('title').textContent = this.componentname + ' | ' + 'Marasiya.com';},})

const Naat = Vue.component('naat', {template: `<div><h3> {{componentname}} </h3><ol><li v-for="titleind in db"><router-link :to="{ path: titleind.path }">{{titleind.name}}</router-link></li></ol><hr></div>`,
    data: function() {return {db: [],componentname:"Naat"}},
    mounted: async function() {rawdata = null;for (let i=0;i < database.length;i++){if(database[i].category === this.componentname){rawdata = database[i].data}}for(let j=0;j<rawdata.length;j++){tempobj = {name: rawdata[j].title,path: "/"+this.componentname+"/"+rawdata[j].title,};this.db.push(tempobj)}document.querySelector('title').textContent = this.componentname + ' | ' + 'Marasiya.com';},})

const Namaz = Vue.component('namaz', {template: `<div><h3> {{componentname}} </h3><ol><li v-for="titleind in db"><router-link :to="{ path: titleind.path }">{{titleind.name}}</router-link></li></ol><hr></div>`,
    data: function() {return {db: [],componentname:"Namaz"}},
    mounted: async function() {rawdata = null;for (let i=0;i < database.length;i++){if(database[i].category === this.componentname){rawdata = database[i].data}}for(let j=0;j<rawdata.length;j++){tempobj = {name: rawdata[j].title,path: "/"+this.componentname+"/"+rawdata[j].title,};this.db.push(tempobj)}document.querySelector('title').textContent = this.componentname + ' | ' + 'Marasiya.com';},})

const Nasihat = Vue.component('nasihat', {template: `<div><h3> {{componentname}} </h3><ol><li v-for="titleind in db"><router-link :to="{ path: titleind.path }">{{titleind.name}}</router-link></li></ol><hr></div>`,
    data: function() {return {db: [],componentname:"Nasihat"}},
    mounted: async function() {rawdata = null;for (let i=0;i < database.length;i++){if(database[i].category === this.componentname){rawdata = database[i].data}}for(let j=0;j<rawdata.length;j++){tempobj = {name: rawdata[j].title,path: "/"+this.componentname+"/"+rawdata[j].title,};this.db.push(tempobj)}document.querySelector('title').textContent = this.componentname + ' | ' + 'Marasiya.com';},})

const Qasida = Vue.component('qasida', {template: `<div><h3> {{componentname}} </h3><ol><li v-for="titleind in db"><router-link :to="{ path: titleind.path }">{{titleind.name}}</router-link></li></ol><hr></div>`,
    data: function() {return {db: [],componentname:"Qasida"}},
    mounted: async function() {rawdata = null;for (let i=0;i < database.length;i++){if(database[i].category === this.componentname){rawdata = database[i].data}}for(let j=0;j<rawdata.length;j++){tempobj = {name: rawdata[j].title,path: "/"+this.componentname+"/"+rawdata[j].title,};this.db.push(tempobj)}document.querySelector('title').textContent = this.componentname + ' | ' + 'Marasiya.com';},})

const QuranChapters = Vue.component('quranchapters', {template: `<div><h3> {{componentname}} </h3><ol><li v-for="titleind in db"><router-link :to="{ path: titleind.path }">{{titleind.name}}</router-link></li></ol><hr></div>`,
    data: function() {return {db: [],componentname:"Quran-Chapters"}},
    mounted: async function() {rawdata = null;for (let i=0;i < database.length;i++){if(database[i].category === this.componentname){rawdata = database[i].data}}for(let j=0;j<rawdata.length;j++){tempobj = {name: rawdata[j].title,path: "/"+this.componentname+"/"+rawdata[j].title,};this.db.push(tempobj)}document.querySelector('title').textContent = this.componentname + ' | ' + 'Marasiya.com';},})

const QuranJuz = Vue.component('quranjuz', {template: `<div><h3> {{componentname}} </h3><ol><li v-for="titleind in db"><router-link :to="{ path: titleind.path }">{{titleind.name}}</router-link></li></ol><hr></div>`,
    data: function() {return {db: [],componentname:"Quran-Juz"}},
    mounted: async function() {rawdata = null;for (let i=0;i < database.length;i++){if(database[i].category === this.componentname){rawdata = database[i].data}}for(let j=0;j<rawdata.length;j++){tempobj = {name: rawdata[j].title,path: "/"+this.componentname+"/"+rawdata[j].title,};this.db.push(tempobj)}document.querySelector('title').textContent = this.componentname + ' | ' + 'Marasiya.com';},})

const Rasa = Vue.component('rasa', {template: `<div><h3> {{componentname}} </h3><ol><li v-for="titleind in db"><router-link :to="{ path: titleind.path }">{{titleind.name}}</router-link></li></ol><hr></div>`,
    data: function() {return {db: [],componentname:"Rasa"}},
    mounted: async function() {rawdata = null;for (let i=0;i < database.length;i++){if(database[i].category === this.componentname){rawdata = database[i].data}}for(let j=0;j<rawdata.length;j++){tempobj = {name: rawdata[j].title,path: "/"+this.componentname+"/"+rawdata[j].title,};this.db.push(tempobj)}document.querySelector('title').textContent = this.componentname + ' | ' + 'Marasiya.com';},})

const Salaam = Vue.component('salaam', {template: `<div><h3> {{componentname}} </h3><ol><li v-for="titleind in db"><router-link :to="{ path: titleind.path }">{{titleind.name}}</router-link></li></ol><hr></div>`,
    data: function() {return {db: [],componentname:"Salaam"}},
    mounted: async function() {rawdata = null;for (let i=0;i < database.length;i++){if(database[i].category === this.componentname){rawdata = database[i].data}}for(let j=0;j<rawdata.length;j++){tempobj = {name: rawdata[j].title,path: "/"+this.componentname+"/"+rawdata[j].title,};this.db.push(tempobj)}document.querySelector('title').textContent = this.componentname + ' | ' + 'Marasiya.com';},})

const NotFound = { template: '<p>Page not found</p>' }

const routes = [{
    path: '/',
    component: Home
}, {
    path: '/Dua',
    component: Dua
}, {
    path: '/Iltija',
    component: Iltija
}, {
    path: '/Madeh',
    component: Madeh
}, {
    path: '/Manaqabat',
    component: Manaqabat
}, {
    path: '/Marasiya',
    component: Marasiya
}, {
    path: '/Misc',
    component: Misc
}, {
    path: '/Naat',
    component: Naat
}, {
    path: '/Namaz',
    component: Namaz
}, {
    path: '/Nasihat',
    component: Nasihat
}, {
    path: '/Qasida',
    component: Qasida
}, {
    path: '/Quran-Chapters',
    component: QuranChapters
}, {
    path: '/Quran-Juz',
    component: QuranJuz
}, {
    path: '/Rasa',
    component: Rasa
}, {
    path: '/Salaam',
    component: Salaam
}, {
    path: '/:id?/:ad?',
    component: Kalaam
}, {
    path: '/*',
    component: NotFound
},
];
const router = new VueRouter({
  routes // short for `routes: routes`
})
var app = new Vue({
    el: '#app',
    router: router,
    mounted: async function() {
        document.getElementById("loading").innerHTML = ("");
    },
})

Description = 'Marasiya.com is a website for Dawoodi Bohras. With this site you can Listen n download audio & read n download PDF of '
for(index=0;index<database.length;index++){
    Description += database[index].category + ', '
    for(subindex=0;subindex<database[index].data.length;subindex++){
        Description += database[index].data[subindex].title + ', '
    }
    
}
document.querySelector('meta[name="description"]').content = Description"""

def update_app_js():
    ouputfile = open("Site/static/data.js","w",encoding="utf-8")
    ouputfile.writelines(databaseGenerator())
    ouputfile.writelines("\n")
    ouputfile.close()
    ouputfile = open("Site/static/app.js","w",encoding="utf-8")
    ouputfile.writelines(static_JS_1)
    ouputfile.writelines(titleDataGenerator())
    ouputfile.writelines(static_JS_2)
    ouputfile.close()

update_MasterDB()
sitemap_xml()
update_app_js()
print("All Steps Done")
