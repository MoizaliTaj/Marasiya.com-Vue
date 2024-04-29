
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
            data:{MarasiyaTitle:331,MarasiyaAudio:385,MarasiyaPDF:131,DuaTitle:47,DuaAudio:36,DuaPDF:38,IltijaTitle:15,IltijaAudio:17,IltijaPDF:2,MadehTitle:294,MadehAudio:325,MadehPDF:143,ManaqabatTitle:40,ManaqabatAudio:42,ManaqabatPDF:3,MiscTitle:49,MiscAudio:29,MiscPDF:34,NaatTitle:22,NaatAudio:27,NaatPDF:0,NamazTitle:24,NamazAudio:26,NamazPDF:16,NasihatTitle:29,NasihatAudio:31,NasihatPDF:12,QasidaTitle:55,QasidaAudio:67,QasidaPDF:16,Quran_ChaptersTitle:115,Quran_ChaptersAudio:114,Quran_ChaptersPDF:110,Quran_JuzTitle:30,Quran_JuzAudio:30,Quran_JuzPDF:30,RasaTitle:73,RasaAudio:77,RasaPDF:21,SalaamTitle:80,SalaamAudio:104,SalaamPDF:11,masterTitleCount:1204,masterAudioCount:1310,masterPDFCount:567,}
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
document.querySelector('meta[name="description"]').content = Description