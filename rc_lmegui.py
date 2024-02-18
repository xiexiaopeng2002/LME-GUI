# Resource object code (Python 3)
# Created by: object code
# Created by: The Resource Compiler for Qt version 6.6.1
# WARNING! All changes made in this file will be lost!

from PySide6 import QtCore

qt_resource_data = b"\
\x00\x01\xfc\x98\
(\
function(a){func\
tion j(a){try{re\
turn a?new windo\
w.ActiveXObject(\
\x22Microsoft.XMLHT\
TP\x22):new window.\
XMLHttpRequest}c\
atch(c){}}a.ajax\
Settings.xhr=voi\
d 0===window.Act\
iveXObject?j:fun\
ction(){return(t\
his.url==documen\
t.location||0==t\
his.url.indexOf(\
\x22http\x22)||!this.i\
sLocal)&&/^(get|\
post|head|put|de\
lete|options)$/i\
.test(this.type)\
&&j()||j(1)};a.a\
jaxTransport(\x22+s\
cript\x22,function(\
a){var c,b=docum\
ent.head||jQuery\
(\x22head\x22)[0]||doc\
ument.documentEl\
ement;return{sen\
d:function(d,k){\
c=document.creat\
eElement(\x22script\
\x22);a.scriptChars\
et&&\x0a(c.charset=\
a.scriptCharset)\
;c.src=a.url;c.o\
nload=c.onreadys\
tatechange=funct\
ion(a,b){if(b||!\
c.readyState||/l\
oaded|complete/.\
test(c.readyStat\
e))c.onload=c.on\
readystatechange\
=null,c.parentNo\
de&&c.parentNode\
.removeChild(c),\
c=null,b||k(200,\
\x22success\x22)};b.in\
sertBefore(c,b.f\
irstChild)},abor\
t:function(){if(\
c)c.onload(void \
0,!0)}}});a.exte\
nd(a.support,{ie\
cors:!!window.XD\
omainRequest});a\
.support.iecors?\
a.ajaxTransport(\
function(a){retu\
rn{send:function\
(c,b){var d=new \
window.XDomainRe\
quest;d.onload=f\
unction(){b(200,\
\x0a\x22OK\x22,{text:d.re\
sponseText},{\x22Co\
ntent-Type\x22:d.co\
ntentType})};a.x\
hrFields&&(d.one\
rror=a.xhrFields\
.error,d.ontimeo\
ut=a.xhrFields.t\
imeout);d.open(a\
.type,a.url);d.s\
end(a.hasContent\
&&a.data||null)}\
,abort:function(\
){xdr.abort()}}}\
):(a.ajaxSetup({\
accepts:{binary:\
\x22text/plain; cha\
rset=x-user-defi\
ned\x22},responseFi\
elds:{binary:\x22re\
sponse\x22}}),a.aja\
xTransport(\x22bina\
ry\x22,function(a){\
var c;return{sen\
d:function(b,d){\
var k=a.xhr();co\
nsole.log(\x22xhr.o\
pen binary async\
=\x22+a.async+\x22 url\
=\x22+a.url);k.open\
(a.type,a.url,a.\
async);\x0avar j=!1\
;try{k.hasOwnPro\
perty(\x22responseT\
ype\x22)&&(k.respon\
seType=\x22arraybuf\
fer\x22,j=!0)}catch\
(l){}try{!j&&k.o\
verrideMimeType&\
&k.overrideMimeT\
ype(\x22text/plain;\
 charset=x-user-\
defined\x22)}catch(\
e){}!a.crossDoma\
in&&!b[\x22X-Reques\
ted-With\x22]&&(b[\x22\
X-Requested-With\
\x22]=\x22XMLHttpReque\
st\x22);try{for(var\
 f in b)k.setReq\
uestHeader(f,b[f\
])}catch(h){}k.s\
end(a.hasContent\
&&a.data||null);\
c=function(){var\
 e=k.status,f=\x22\x22\
,h=k.getAllRespo\
nseHeaders(),b={\
};try{if(c&&4===\
k.readyState){c=\
void 0;try{b.tex\
t=\x22string\x22===typ\
eof k.responseTe\
xt?\x0ak.responseTe\
xt:null}catch(j)\
{}try{b.binary=k\
.response}catch(\
m){}try{f=k.stat\
usText}catch(l){\
f=\x22\x22}!e&&a.isLoc\
al&&!a.crossDoma\
in?e=b.text?200:\
404:1223===e&&(e\
=204);d(e,f,b,h)\
}}catch(t){alert\
(t),d(-1,t)}};a.\
async?4===k.read\
yState?setTimeou\
t(c):k.onreadyst\
atechange=c:c()}\
,abort:function(\
){}}}))})(jQuery\
);\x0a(function(a,j\
,g,c){function b\
(b,g){function m\
(e){a(l).each(fu\
nction(){self.Jm\
ol&&(0<=g.indexO\
f(\x22mouseup\x22)||0<\
=g.indexOf(\x22touc\
hend\x22))&&Jmol._s\
etMouseOwner(nul\
l);var h=a(this)\
;this!==e.target\
&&!h.has(e.targe\
t).length&&h.tri\
ggerHandler(g,[e\
.target,e])})}g=\
g||b+c;var l=a()\
,e=b+\x22.\x22+g+\x22-spe\
cial-event\x22;a.ev\
ent.special[g]={\
setup:function()\
{l=l.add(this);1\
===l.length&&a(j\
).bind(e,m)},tea\
rdown:function()\
{self.Jmol&&Jmol\
._setMouseOwner(\
null);l=l.not(th\
is);0===l.length\
&&a(j).unbind(e)\
},add:function(a\
){var e=\x0aa.handl\
er;a.handler=fun\
ction(a,f){a.tar\
get=f;e.apply(th\
is,arguments)}}}\
}a.map(g.split(\x22\
 \x22),function(a){\
b(a)});b(\x22focusi\
n\x22,\x22focus\x22+c);b(\
\x22focusout\x22,\x22blur\
\x22+c)})(jQuery,do\
cument,\x22click mo\
usemove mouseup \
touchmove touche\
nd\x22,\x22outjsmol\x22);\
\x22undefined\x22==typ\
eof jQuery&&aler\
t(\x22Note -- JSmol\
jQuery is requir\
ed for JSmol, bu\
t it's not defin\
ed.\x22);self.Jmol|\
|(Jmol={});\x0aJmol\
._version||(Jmol\
=function(a){var\
 j=function(a){r\
eturn{rear:a++,h\
eader:a++,main:a\
++,image:a++,fro\
nt:a++,fileOpene\
r:a++,coverImage\
:a++,dialog:a++,\
menu:a+9E4,conso\
le:a+91E3,consol\
eImage:a+91001,m\
onitorZIndex:a+9\
9999}},j={_versi\
on:\x22$Date: 2016-\
05-08 13:20:27 -\
0500 (Sun, 08 Ma\
y 2016) $\x22,_aler\
tNoBinary:!0,_al\
lowedJmolSize:[2\
5,2048,300],_app\
letCssClass:\x22\x22,_\
appletCssText:\x22\x22\
,_fileCache:null\
,_jarFile:null,_\
j2sPath:null,_us\
e:null,_j2sLoadM\
onitorOpacity:90\
,_applets:{},_as\
ynchronous:!0,_a\
jaxQueue:[],_per\
sistentMenu:!1,\x0a\
_getZOrders:j,_z\
:j(Jmol.z||9E3),\
_debugCode:!0,db\
:{_databasePrefi\
xes:\x22$=:\x22,_fileL\
oadScript:\x22;if (\
_loadScript = ''\
 && defaultLoadS\
cript == '' && _\
filetype == 'Pdb\
') { select prot\
ein or nucleic;c\
artoons Only;col\
or structure; se\
lect * };\x22,_nciL\
oadScript:\x22;n = \
({molecule=1}.le\
ngth < {molecule\
=2}.length ? 2 :\
 1); select mole\
cule=n;display s\
elected;center s\
elected;\x22,_pubCh\
emLoadScript:\x22\x22,\
_DirectDatabaseC\
alls:{\x22cactus.nc\
i.nih.gov\x22:null,\
\x22.x3dna.org\x22:nul\
l,\x22rruff.geo.ari\
zona.edu\x22:null,\x22\
.rcsb.org\x22:null,\
\x22ftp.wwpdb.org\x22:\
null,\x0a\x22pdbe.org\x22\
:null,\x22materials\
project.org\x22:nul\
l,\x22.ebi.ac.uk\x22:n\
ull,\x22pubchem.ncb\
i.nlm.nih.gov\x22:n\
ull,\x22http://www.\
nmrdb.org/tools/\
jmol/predict.php\
\x22:null,$:\x22https:\
//cactus.nci.nih\
.gov/chemical/st\
ructure/%FILENCI\
/file?format=sdf\
&get3d=True\x22,$$:\
\x22https://cactus.\
nci.nih.gov/chem\
ical/structure/%\
FILENCI/file?for\
mat=sdf\x22,\x22=\x22:\x22ht\
tp://files.rcsb.\
org/view/%FILE.p\
db\x22,\x22*\x22:\x22http://\
www.ebi.ac.uk/pd\
be/entry-files/d\
ownload/%FILE.ci\
f\x22,\x22==\x22:\x22http://\
www.rcsb.org/pdb\
/files/ligand/%F\
ILE.cif\x22,\x22:\x22:\x22ht\
tps://pubchem.nc\
bi.nlm.nih.gov/r\
est/pug/compound\
/%FILE/SDF?recor\
d_type=3d\x22},\x0a_re\
stQueryUrl:\x22http\
://www.rcsb.org/\
pdb/rest/search\x22\
,_restQueryXml:\x22\
<orgPdbQuery><qu\
eryType>org.pdb.\
query.simple.Adv\
ancedKeywordQuer\
y</queryType><de\
scription>Text S\
earch</descripti\
on><keywords>QUE\
RY</keywords></o\
rgPdbQuery>\x22,_re\
stReportUrl:\x22htt\
p://www.pdb.org/\
pdb/rest/customR\
eport?pdbids=IDL\
IST&customReport\
Columns=structur\
eId,structureTit\
le\x22},_debugAlert\
:!1,_document:a,\
_isXHTML:!1,_las\
tAppletID:null,_\
mousePageX:null,\
_mouseOwner:null\
,_serverUrl:\x22htt\
p://your.server.\
here/jsmol.php\x22,\
_syncId:(\x22\x22+Math\
.random()).subst\
ring(3),\x0a_touchi\
ng:!1,_XhtmlElem\
ent:null,_XhtmlA\
ppendChild:!1};a\
=a.location.href\
.toLowerCase();j\
._httpProto=0==a\
.indexOf(\x22https\x22\
)?\x22https://\x22:\x22ht\
tp://\x22;j._isFile\
=0==a.indexOf(\x22f\
ile:\x22);j._isFile\
&&$.ajaxSetup({m\
imeType:\x22text/pl\
ain\x22});j._ajaxTe\
stSite=j._httpPr\
oto+\x22google.com\x22\
;a=j._isFile||0=\
=a.indexOf(\x22http\
://localhost\x22)||\
0==a.indexOf(\x22ht\
tp://127.\x22);j._t\
racker=\x22http://\x22\
==j._httpProto&&\
!a&&\x22http://chem\
apps.stolaf.edu/\
jmol/JmolTracker\
.htm?id=UA-45940\
799-1\x22;j._isChro\
me=0<=navigator.\
userAgent.toLowe\
rCase().indexOf(\
\x22chrome\x22);\x0aj._is\
Safari=!j._isChr\
ome&&0<=navigato\
r.userAgent.toLo\
werCase().indexO\
f(\x22safari\x22);j._i\
sMsie=void 0!==w\
indow.ActiveXObj\
ect;j._isEdge=0<\
=navigator.userA\
gent.indexOf(\x22Ed\
ge/\x22);j._useData\
URI=!j._isSafari\
&&!j._isMsie&&!j\
._isEdge;window.\
requestAnimation\
Frame||(window.r\
equestAnimationF\
rame=window.setT\
imeout);for(var \
g in Jmol)j[g]=J\
mol[g];return j}\
(document,Jmol))\
;\x0a(function(a,j)\
{a.__$=j;j(docum\
ent).ready(funct\
ion(){a._documen\
t=null});a.$=fun\
ction(a,f){null=\
=a&&alert(f+argu\
ments.callee.cal\
ler.toString());\
return j(f?\x22#\x22+a\
._id+\x22_\x22+f:a)};a\
._$=function(a){\
return\x22string\x22==\
typeof a?j(\x22#\x22+a\
):a};a.$ajax=fun\
ction(e){a._ajax\
Call=e.url;e.cac\
he=\x22NO\x22!=e.cache\
;e.url=a._fixPro\
tocol(e.url);ret\
urn j.ajax(e)};a\
._fixProtocol=fu\
nction(a){return\
 0==a.indexOf(\x22h\
ttp://www.rcsb.o\
rg/pdb/files/\x22)&\
&0>a.indexOf(\x22/l\
igand/\x22)?\x22http:/\
/files.rcsb.org/\
view/\x22+a.substri\
ng(30).replace(/\
\x5c.gz/,\x22\x22):\x0a0==a.\
indexOf(\x22http://\
\x22)&&(0==a.indexO\
f(\x22http://pubche\
m\x22)||0==a.indexO\
f(\x22http://cactus\
\x22)||0==a.indexOf\
(\x22http://www.mat\
erialsproject\x22))\
?\x22https\x22+a.subst\
ring(4):a};a._ge\
tNCIInfo=functio\
n(e,f){return a.\
_getFileData(\x22ht\
tps://cactus.nci\
.nih.gov/chemica\
l/structure/\x22+e+\
\x22/\x22+(\x22name\x22==f?\x22\
names\x22:f))};a.$a\
ppEvent=function\
(e,f,h,b){e=a.$(\
e,f);e.off(h)&&b\
&&e.on(h,b)};a.$\
resize=function(\
a){return j(wind\
ow).resize(a)};a\
.$after=function\
(a,f){return j(a\
).after(f)};a.$a\
ppend=function(a\
,f){return j(a).\
append(f)};a.$bi\
nd=\x0afunction(a,f\
,h){return h?j(a\
).bind(f,h):j(a)\
.unbind(f)};a.$c\
losest=function(\
a,f){return j(a)\
.closest(f)};a.$\
get=function(a,f\
){return j(a).ge\
t(f)};a.$documen\
tOff=function(a,\
f){return j(docu\
ment).off(a,\x22#\x22+\
f)};a.$documentO\
n=function(a,f,h\
){return j(docum\
ent).on(a,\x22#\x22+f,\
h)};a.$getAncest\
orDiv=function(a\
,f){return j(\x22di\
v.\x22+f+\x22:has(#\x22+a\
+\x22)\x22)[0]};a.$sup\
portsIECrossDoma\
inScripting=func\
tion(){return j.\
support.iecors};\
a.$attr=function\
(e,f,h){return a\
._$(e).attr(f,h)\
};a.$css=functio\
n(e,f){return a.\
_$(e).css(f)};\x0aa\
.$find=function(\
e,f){return a._$\
(e).find(f)};a.$\
focus=function(e\
){return a._$(e)\
.focus()};a.$htm\
l=function(e,f){\
return a._$(e).h\
tml(f)};a.$offse\
t=function(e){re\
turn a._$(e).off\
set()};a.$window\
On=function(a,f)\
{return j(window\
).on(a,f)};a.$pr\
op=function(e,f,\
h){var b=a._$(e)\
;return 3==argum\
ents.length?b.pr\
op(f,h):b.prop(f\
)};a.$remove=fun\
ction(e){return \
a._$(e).remove()\
};a.$scrollTo=fu\
nction(e,f){var \
h=a._$(e);return\
 h.scrollTop(0>f\
?h[0].scrollHeig\
ht:f)};a.$setEna\
bled=function(e,\
f){return a._$(e\
).attr(\x22disabled\
\x22,\x0af?null:\x22disab\
led\x22)};a.$getSiz\
e=function(e){e=\
a._$(e);return[e\
.width(),e.heigh\
t()]};a.$setSize\
=function(e,f,h)\
{return a._$(e).\
width(f).height(\
h)};a.$is=functi\
on(e,f){return a\
._$(e).is(f)};a.\
$setVisible=func\
tion(e,f){var h=\
a._$(e);return f\
?h.show():h.hide\
()};a.$submit=fu\
nction(e){return\
 a._$(e).submit(\
)};a.$val=functi\
on(e,f){var h=a.\
_$(e);return 1==\
arguments.length\
?h.val():h.val(f\
)};a._clearVars=\
function(){delet\
e jQuery;delete \
j;delete a;delet\
e SwingControlle\
r;delete J;delet\
e JM;delete JS;d\
elete JSV;\x0adelet\
e JU;delete JV;d\
elete java;delet\
e javajs;delete \
Clazz;delete c$}\
;var g=document,\
c=window,b={};b.\
ua=navigator.use\
rAgent.toLowerCa\
se();var d;a:{d=\
[\x22linux\x22,\x22unix\x22,\
\x22mac\x22,\x22win\x22];for\
(var k=d.length;\
k--;)if(-1!=b.ua\
.indexOf(d[k])){\
d=d[k];break a}d\
=\x22unknown\x22}b.os=\
d;b.browser=func\
tion(){for(var a\
=b.ua,f=\x22konquer\
or webkit omniwe\
b opera webtv ic\
ab msie mozilla\x22\
.split(\x22 \x22),h=0;\
h<f.length;h++)i\
f(0<=a.indexOf(f\
[h]))return f[h]\
;return\x22unknown\x22\
};b.browserName=\
b.browser();b.br\
owserVersion=par\
seFloat(b.ua.sub\
string(b.ua.inde\
xOf(b.browserNam\
e)+\x0ab.browserNam\
e.length+1));b.s\
upportsXhr2=func\
tion(){return j.\
support.cors||j.\
support.iecors};\
b.allowDestroy=\x22\
msie\x22!=b.browser\
Name;b.allowHTML\
5=\x22msie\x22!=b.brow\
serName||0>navig\
ator.appVersion.\
indexOf(\x22MSIE 8\x22\
);b.getDefaultLa\
nguage=function(\
){return navigat\
or.language||nav\
igator.userLangu\
age||\x22en-US\x22};b.\
_webGLtest=0;b.s\
upportsWebGL=fun\
ction(){if(!a.fe\
atureDetection._\
webGLtest){var e\
;a.featureDetect\
ion._webGLtest=c\
.WebGLRenderingC\
ontext&&((e=g.cr\
eateElement(\x22can\
vas\x22)).getContex\
t(\x22webgl\x22)||e.ge\
tContext(\x22experi\
mental-webgl\x22))?\
\x0a1:-1}return 0<a\
.featureDetectio\
n._webGLtest};b.\
supportsLocaliza\
tion=function(){\
for(var a=g.getE\
lementsByTagName\
(\x22meta\x22),f=a.len\
gth;0<=--f;)if(0\
<=a[f].outerHTML\
.toLowerCase().i\
ndexOf(\x22utf-8\x22))\
return!0;return!\
1};b.supportsJav\
a=function(){a.f\
eatureDetection.\
_javaEnabled||(a\
.featureDetectio\
n._javaEnabled=a\
._isMsie?navigat\
or.javaEnabled()\
?1:-1:navigator.\
javaEnabled()&&(\
!navigator.mimeT\
ypes||navigator.\
mimeTypes[\x22appli\
cation/x-java-ap\
plet\x22])?1:-1);re\
turn 0<a.feature\
Detection._javaE\
nabled};b.compli\
antBrowser=\x0afunc\
tion(){var a=!!g\
.getElementById,\
f=b.os;if(\x22opera\
\x22==b.browserName\
&&7.54>=b.browse\
rVersion&&\x22mac\x22=\
=f||\x22webkit\x22==b.\
browserName&&125\
.12>b.browserVer\
sion||\x22msie\x22==b.\
browserName&&\x22ma\
c\x22==f||\x22konquero\
r\x22==b.browserNam\
e&&3.3>=b.browse\
rVersion)a=!1;re\
turn a};b.isFull\
yCompliant=funct\
ion(){return b.c\
ompliantBrowser(\
)&&b.supportsJav\
a()};b.useIEObje\
ct=\x22win\x22==b.os&&\
\x22msie\x22==b.browse\
rName&&5.5<=b.br\
owserVersion;b.u\
seHtml4Object=\x22m\
ozilla\x22==b.brows\
erName&&5<=b.bro\
wserVersion||\x22op\
era\x22==b.browserN\
ame&&8<=b.browse\
rVersion||\x0a\x22webk\
it\x22==b.browserNa\
me;b.hasFileRead\
er=c.File&&c.Fil\
eReader;a.featur\
eDetection=b;a._\
ajax=function(e)\
{if(!e.async)ret\
urn a.$ajax(e).r\
esponseText;a._a\
jaxQueue.push(e)\
;1==a._ajaxQueue\
.length&&a._ajax\
Done()};a._ajaxD\
one=function(){v\
ar e=a._ajaxQueu\
e.shift();e&&a.$\
ajax(e)};a._grab\
berOptions=[[\x22$\x22\
,\x22NCI(small mole\
cules)\x22],[\x22:\x22,\x22P\
ubChem(small mol\
ecules)\x22],[\x22=\x22,\x22\
RCSB(macromolecu\
les)\x22],[\x22*\x22,\x22PDB\
e(macromolecules\
)\x22]];a._getGrabb\
erOptions=functi\
on(e){if(0==a._g\
rabberOptions.le\
ngth)return\x22\x22;va\
r f='<input type\
=\x22text\x22 id=\x22ID_q\
uery\x22 onfocus=\x22j\
Query(this).sele\
ct()\x22 onkeypress\
=\x22if(13==event.w\
hich){Jmol._appl\
ets[\x5c'ID\x5c']._sea\
rch();return fal\
se}\x22 size=\x2232\x22 v\
alue=\x22\x22 />',\x0ah='\
<button id=\x22ID_s\
ubmit\x22 onclick=\x22\
Jmol._applets[\x5c'\
ID\x5c']._search()\x22\
>Search</button>\
</nobr>';1==a._g\
rabberOptions.le\
ngth?(f=\x22<nobr>\x22\
+f+'<span style=\
\x22display:none\x22>'\
,h=\x22</span>\x22+h):\
f+=\x22<br /><nobr>\
\x22;for(var f=f+'<\
select id=\x22ID_se\
lect\x22>',b=0;b<a.\
_grabberOptions.\
length;b++)var d\
=a._grabberOptio\
ns[b],f=f+('<opt\
ion value=\x22'+d[0\
]+'\x22 '+(0==b?\x22se\
lected\x22:\x22\x22)+\x22>\x22+\
d[1]+\x22</option>\x22\
);f=(f+\x22</select\
>\x22+h).replace(/I\
D/g,e._id);retur\
n\x22<br />\x22+f};a._\
getScriptForData\
base=function(e)\
{return\x22$\x22==e?a.\
db._nciLoadScrip\
t:\x0a\x22:\x22==e?a.db._\
pubChemLoadScrip\
t:a.db._fileLoad\
Script};a._setIn\
fo=function(a,f,\
h){var b=[],d=\x22\x22\
;if(0==h.indexOf\
(\x22ERROR\x22))d=h;el\
se switch(f){cas\
e \x22=\x22:f=h.split(\
\x22<dimStructure.s\
tructureId>\x22);b=\
[\x22<table>\x22];for(\
h=1;h<f.length;h\
++)b.push('<tr><\
td valign=top><a\
 href=\x22javascrip\
t:Jmol.search('+\
a._id+\x22,'=\x22+f[h]\
.substring(0,4)+\
\x22')\x5c\x22>\x22+f[h].sub\
string(0,4)+\x22</a\
></td>\x22),b.push(\
\x22<td>\x22+f[h].spli\
t(\x22Title>\x22)[1].s\
plit(\x22</\x22)[0]+\x22<\
/td></tr>\x22);b.pu\
sh(\x22</table>\x22);d\
=f.length-1+\x22 ma\
tches\x22;break;cas\
e \x22$\x22:case \x22:\x22:b\
reak;default:ret\
urn}a._infoHeade\
r=\x0ad;a._info=b.j\
oin(\x22\x22);a._showI\
nfo(!0)};a._load\
Success=function\
(e,f){f&&(a._aja\
xDone(),f(e))};a\
._loadError=func\
tion(e){a._ajaxD\
one();a.say(\x22Err\
or connecting to\
 server: \x22+a._aj\
axCall);null!=e&\
&e()};a._isDatab\
aseCall=function\
(e){return 0<=a.\
db._databasePref\
ixes.indexOf(e.s\
ubstring(0,1))};\
a._getDirectData\
baseCall=functio\
n(e,f){if(f&&!a.\
featureDetection\
.supportsXhr2())\
return e;var h=2\
,b=e.substring(0\
,h),d=a.db._Dire\
ctDatabaseCalls[\
b]||a.db._Direct\
DatabaseCalls[b=\
e.substring(0,--\
h)];d&&(\x22:\x22==b?(\
b=e.toLowerCase(\
),\x0aisNaN(parseIn\
t(e.substring(1)\
))?0==b.indexOf(\
\x22:smiles:\x22)?(d+=\
\x22?POST?smiles=\x22+\
e.substring(8),e\
=\x22smiles\x22):0==b.\
indexOf(\x22:cid:\x22)\
?e=\x22cid/\x22+e.subs\
tring(5):(0==b.i\
ndexOf(\x22:name:\x22)\
?e=e.substring(5\
):0==b.indexOf(\x22\
:cas:\x22)&&(e=e.su\
bstring(4)),e=\x22n\
ame/\x22+encodeURIC\
omponent(e.subst\
ring(h))):e=\x22cid\
/\x22+e.substring(1\
)):e=encodeURICo\
mponent(e.substr\
ing(h)),0<=e.ind\
exOf(\x22.mmtf\x22)?e=\
\x22http://mmtf.rcs\
b.org/full/\x22+e:0\
<=d.indexOf(\x22FIL\
ENCI\x22)?(e=e.repl\
ace(/\x5c%2F/g,\x22/\x22)\
,e=d.replace(/\x5c%\
FILENCI/,e)):e=d\
.replace(/\x5c%FILE\
/,e));return e};\
\x0aa._getRawDataFr\
omServer=functio\
n(e,f,h,b,d,c){e\
=\x22?call=getRawDa\
taFromDatabase&d\
atabase=\x22+e+(0<=\
f.indexOf(\x22?POST\
?\x22)?\x22?POST?\x22:\x22\x22)\
+\x22&query=\x22+encod\
eURIComponent(f)\
+(d?\x22&encoding=b\
ase64\x22:\x22\x22)+(c?\x22\x22\
:\x22&script=\x22+enco\
deURIComponent(a\
._getScriptForDa\
tabase(e)));retu\
rn a._contactSer\
ver(e,h,b)};a._c\
heckFileName=fun\
ction(e,f,h){a._\
isDatabaseCall(f\
)&&(h&&a._setQue\
ryTerm(e,f),f=a.\
_getDirectDataba\
seCall(f,!0),a._\
isDatabaseCall(f\
)&&(f=a._getDire\
ctDatabaseCall(f\
,!1),h&&(h[0]=!0\
)));return f};a.\
_checkCache=func\
tion(e,\x0af,h){if(\
e._cacheFiles&&a\
._fileCache&&!f.\
endsWith(\x22.js\x22))\
{if(e=a._fileCac\
he[f])return Sys\
tem.out.println(\
\x22using \x22+e.lengt\
h+\x22 bytes of cac\
hed data for \x22+f\
),h(e),null;h=fu\
nction(e,f){h(a.\
_fileCache[e]=f)\
}}return h};a._p\
layAudio=functio\
n(a){var f=docum\
ent.createElemen\
t(\x22audio\x22);f.con\
trols=\x22true\x22;f.s\
rc=a;f.play()};a\
._loadFileData=f\
unction(e,f,h,b)\
{var d=[];f=a._c\
heckFileName(e,f\
,d);h=a._checkCa\
che(e,f,h);d[0]?\
a._getRawDataFro\
mServer(\x22_\x22,f,h,\
b):(e={type:\x22GET\
\x22,dataType:\x22text\
\x22,url:f,async:a.\
_asynchronous,\x0as\
uccess:function(\
e){a._loadSucces\
s(e,h)},error:fu\
nction(){a._load\
Error(b)}},a._ch\
eckAjaxPost(e),a\
._ajax(e))};a._g\
etInfoFromDataba\
se=function(e,f,\
h){if(\x22====\x22==f)\
{var b=a.db._res\
tQueryXml.replac\
e(/QUERY/,h),b={\
dataType:\x22text\x22,\
type:\x22POST\x22,cont\
entType:\x22applica\
tion/x-www-form-\
urlencoded\x22,url:\
a.db._restQueryU\
rl,data:encodeUR\
IComponent(b)+\x22&\
req=browser\x22,suc\
cess:function(b)\
{a._ajaxDone();a\
._extractInfoFro\
mRCSB(e,f,h,b)},\
error:function()\
{a._loadError(nu\
ll)},async:a._as\
ynchronous};retu\
rn a._ajax(b)}h=\
\x22?call=getInfoFr\
omDatabase&datab\
ase=\x22+\x0af+\x22&query\
=\x22+encodeURIComp\
onent(h);return \
a._contactServer\
(h,function(h){a\
._setInfo(e,f,h)\
})};a._extractIn\
foFromRCSB=funct\
ion(e,f,h,b){var\
 d=b.length/5;if\
(0!=d&&4==h.leng\
th&&1!=d){h=h.to\
UpperCase();var \
c=b.indexOf(h);0\
<c&&0<=\x2212345678\
9\x22.indexOf(h.sub\
string(0,1))&&(b\
=h+\x22,\x22+b.substri\
ng(0,c)+b.substr\
ing(c+5));50<d&&\
(b=b.substring(0\
,250));b=b.repla\
ce(/\x5cn/g,\x22,\x22);b=\
a._restReportUrl\
.replace(/IDLIST\
/,b);a._loadFile\
Data(e,b,functio\
n(h){a._setInfo(\
e,f,h)})}};a._ch\
eckAjaxPost=func\
tion(a){var f=a.\
url.indexOf(\x22?PO\
ST?\x22);\x0a0<f&&(a.d\
ata=a.url.substr\
ing(f+6),a.url=a\
.url.substring(0\
,f),a.type=\x22POST\
\x22,a.contentType=\
\x22application/x-w\
ww-form-urlencod\
ed\x22)};a._contact\
Server=function(\
e,f,h){e={dataTy\
pe:\x22text\x22,type:\x22\
GET\x22,url:a._serv\
erUrl+e,success:\
function(e){a._l\
oadSuccess(e,f)}\
,error:function(\
){a._loadError(h\
)},async:f?a._as\
ynchronous:!1};a\
._checkAjaxPost(\
e);return a._aja\
x(e)};a._setQuer\
yTerm=function(e\
,f){if(f&&e._has\
Options&&\x22http:/\
/\x22!=f.substring(\
0,7)){if(a._isDa\
tabaseCall(f)){v\
ar h=f.substring\
(0,1);f=f.substr\
ing(1);f.substri\
ng(0,\x0a1)==h&&0<=\
\x22=$\x22.indexOf(h)&\
&(f=f.substring(\
1));var b=a._get\
Element(e,\x22selec\
t\x22);if(b&&b.opti\
ons)for(var d=0;\
d<b.options.leng\
th;d++)b[d].valu\
e==h&&(b[d].sele\
cted=!0)}a.$val(\
a.$(e,\x22query\x22),f\
)}};a._search=fu\
nction(e,f,h){1<\
arguments.length\
||(f=null);a._se\
tQueryTerm(e,f);\
f||(f=a.$val(a.$\
(e,\x22query\x22)));0=\
=f.indexOf(\x22!\x22)?\
e._script(f.subs\
tring(1)):(f&&(f\
=f.replace(/\x5c\x22/g\
,\x22\x22)),e._showInf\
o(!1),a._searchM\
ol(e,f,h,!0))};a\
._searchMol=func\
tion(e,f,h,b){va\
r d;a._isDatabas\
eCall(f)?(d=f.su\
bstring(0,1),f=f\
.substring(1)):\x0a\
d=e._hasOptions?\
a.$val(a.$(e,\x22se\
lect\x22)):\x22$\x22;\x22=\x22=\
=d&&3==f.length&\
&(f=\x22=\x22+f);var c\
=d+f;if(f&&!(0>c\
.indexOf(\x22?\x22)&&c\
==e._thisJmolMod\
el)){e._thisJmol\
Model=c;var g;b&\
&null!=e._viewSe\
t&&null!=(g=a.Vi\
ew.__findView(e.\
_viewSet,{chemID\
:c}))?a.View.__s\
etView(g,e,!1):(\
\x22$\x22==d||\x22:\x22==d?e\
._jmolFileType=\x22\
MOL\x22:\x22=\x22==d&&(e.\
_jmolFileType=\x22P\
DB\x22),e._searchDa\
tabase(f,d,h))}}\
;a._searchDataba\
se=function(e,f,\
h,b){e._showInfo\
(!1);return 0<=f\
.indexOf(\x22?\x22)?(a\
._getInfoFromDat\
abase(e,h,f.spli\
t(\x22?\x22)[0]),!0):a\
.db._DirectDatab\
aseCalls[h]?\x0a(e.\
_loadFile(h+f,b)\
,!0):!1};a._sync\
BinaryOK=\x22?\x22;a._\
canSyncBinary=fu\
nction(e){if(a._\
isAsync)return!0\
;if(self.VBArray\
)return a._syncB\
inaryOK=!1;if(\x22?\
\x22!=a._syncBinary\
OK)return a._syn\
cBinaryOK;a._syn\
cBinaryOK=!0;try\
{var f=new windo\
w.XMLHttpRequest\
;f.open(\x22text\x22,a\
._ajaxTestSite,!\
1);f.hasOwnPrope\
rty(\x22responseTyp\
e\x22)?f.responseTy\
pe=\x22arraybuffer\x22\
:f.overrideMimeT\
ype&&f.overrideM\
imeType(\x22text/pl\
ain; charset=x-u\
ser-defined\x22)}ca\
tch(h){return Sy\
stem.out.println\
(\x22JSmolCore.js: \
synchronous bina\
ry file transfer\
 is requested bu\
t not available\x22\
),\x0aa._alertNoBin\
ary&&!e&&alert(\x22\
JSmolCore.js: sy\
nchronous binary\
 file transfer i\
s requested but \
not available\x22),\
a._syncBinaryOK=\
!1}return!0};a._\
binaryTypes=\x22mmt\
f .gz .jpg .gif \
.png .zip .jmol \
.bin .smol .spar\
tan .mrc .map .c\
cp4 .dn6 .delphi\
 .omap .pse .dcd\
\x22.split(\x22 \x22);a._\
isBinaryUrl=func\
tion(e){for(var \
f=a._binaryTypes\
.length;0<=--f;)\
if(0<=e.indexOf(\
a._binaryTypes[f\
]))return!0;retu\
rn!1};a._getFile\
Data=function(e,\
f,h){var b=a._is\
BinaryUrl(e),d=0\
<=e.indexOf(\x22.gz\
\x22)&&0<=e.indexOf\
(\x22rcsb.org\x22);d&&\
(e=e.replace(/\x5c.\
gz/,\x0a\x22\x22),b=!1);v\
ar d=b&&!f&&!a._\
canSyncBinary(d)\
,c=0<=e.indexOf(\
\x22?POST?\x22);0==e.i\
ndexOf(\x22file:/\x22)\
&&0!=e.indexOf(\x22\
file:///\x22)&&(e=\x22\
file://\x22+e.subst\
ring(5));var g=0\
>e.indexOf(\x22://\x22\
)||0==e.indexOf(\
document.locatio\
n.protocol)&&0<=\
e.indexOf(docume\
nt.location.host\
),k=\x22https://\x22==\
a._httpProto&&0=\
=e.indexOf(\x22http\
://\x22),j=a._isDir\
ectCall(e);!j&&0\
<=e.indexOf(\x22?AL\
LOWSORIGIN?\x22)&&(\
j=!0,e=e.replace\
(/\x5c?ALLOWSORIGIN\
\x5c?/,\x22\x22));var m=!\
g&&a.$supportsIE\
CrossDomainScrip\
ting(),l=null;if\
(k||d||!g&&!j||!\
f&&m)l=a._getRaw\
DataFromServer(\x22\
_\x22,\x0ae,f,f,d,!0);\
else{e=e.replace\
(/file:\x5c/\x5c/\x5c/\x5c//\
,\x22file://\x22);var \
q={dataType:b?\x22b\
inary\x22:\x22text\x22,as\
ync:!!f};c?(q.ty\
pe=\x22POST\x22,q.url=\
e.split(\x22?POST?\x22\
)[0],q.data=e.sp\
lit(\x22?POST?\x22)[1]\
):(q.type=\x22GET\x22,\
q.url=e);f&&(q.s\
uccess=function(\
){f(a._xhrReturn\
(q.xhr))},q.erro\
r=function(){f(q\
.xhr.statusText)\
});q.xhr=a.$ajax\
(q);f||(l=a._xhr\
Return(q.xhr))}i\
f(!h)return l;nu\
ll==l&&(l=\x22\x22,b=!\
1);b&&(b=a._canS\
yncBinary(!0));r\
eturn b?a._strTo\
Bytes(l):JU.SB.n\
ewS(l)};a._xhrRe\
turn=function(a)\
{return!a.respon\
seText||self.Cla\
zz&&Clazz.instan\
ceOf(a.response,\
\x0aself.ArrayBuffe\
r)?a.response||a\
.statusText:a.re\
sponseText};a._i\
sDirectCall=func\
tion(e){if(0<=e.\
indexOf(\x22?ALLOWS\
ORIGIN?\x22))return\
!0;for(var f in \
a.db._DirectData\
baseCalls)if(0<=\
f.indexOf(\x22.\x22)&&\
0<=e.indexOf(f))\
return!0;return!\
1};a._cleanFileD\
ata=function(a){\
return 0<=a.inde\
xOf(\x22\x5cr\x22)&&0<=a.\
indexOf(\x22\x5cn\x22)?a.\
replace(/\x5cr\x5cn/g,\
\x22\x5cn\x22):0<=a.index\
Of(\x22\x5cr\x22)?a.repla\
ce(/\x5cr/g,\x22\x5cn\x22):a\
};a._getFileType\
=function(a){var\
 f=a.substring(0\
,1);if(\x22$\x22==f||\x22\
:\x22==f)return\x22MOL\
\x22;if(\x22=\x22==f)retu\
rn\x22=\x22==a.substri\
ng(1,2)?\x22LCIF\x22:\x22\
PDB\x22;a=\x0aa.split(\
\x22.\x22).pop().toUpp\
erCase();return \
a.substring(0,Ma\
th.min(a.length,\
3))};a._getZ=fun\
ction(e,f){retur\
n e&&e._z&&e._z[\
f]||a._z[f]};a._\
incrZ=function(e\
,f){return e&&e.\
_z&&++e._z[f]||+\
+a._z[f]};a._hid\
eLocalFileReader\
=function(e){e._\
localReader&&a.$\
setVisible(e._lo\
calReader,!1);e.\
_readingLocal=!1\
;a._setCursor(e,\
0)};a.loadFileFr\
omDialog=functio\
n(e){a._loadFile\
Asynchronously(n\
ull,e,null,null)\
};a._loadFileAsy\
nchronously=func\
tion(e,f,h,b){if\
(h&&0!=h.indexOf\
(\x22?\x22)){var d=h;h\
=a._checkFileNam\
e(f,h);var c=\x0afu\
nction(c){a._set\
Data(e,h,d,c,b,f\
)},c=a._checkCac\
he(f,h,c);0<=h.i\
ndexOf(\x22|\x22)&&(h=\
h.split(\x22|\x22)[0])\
;return null==c?\
null:a._getFileD\
ata(h,c)}if(!a.f\
eatureDetection.\
hasFileReader)re\
turn e?e.setData\
(msg,null,null,b\
,f):alert(msg);f\
._localReader||(\
c='<div id=\x22ID\x22 \
style=\x22z-index:'\
+a._getZ(f,\x22file\
Opener\x22)+';posit\
ion:absolute;bac\
kground:#E0E0E0;\
left:10px;top:10\
px\x22><div style=\x22\
margin:5px 5px 5\
px 5px;\x22><button\
 id=\x22ID_loadurl\x22\
>URL</button><in\
put type=\x22file\x22 \
id=\x22ID_files\x22 />\
<button id=\x22ID_l\
oadfile\x22>load</b\
utton><button id\
=\x22ID_cancel\x22>can\
cel</button></di\
v><div>',\x0aa.$aft\
er(\x22#\x22+f._id+\x22_a\
ppletdiv\x22,c.repl\
ace(/ID/g,f._id+\
\x22_localReader\x22))\
,f._localReader=\
a.$(f,\x22localRead\
er\x22));a.$appEven\
t(f,\x22localReader\
_loadurl\x22,\x22click\
\x22);a.$appEvent(f\
,\x22localReader_lo\
adurl\x22,\x22click\x22,f\
unction(){var e=\
prompt(\x22Enter a \
URL\x22);e&&(a._hid\
eLocalFileReader\
(f,0),a._setData\
(null,e,e,null,b\
,f))});a.$appEve\
nt(f,\x22localReade\
r_loadfile\x22,\x22cli\
ck\x22);a.$appEvent\
(f,\x22localReader_\
loadfile\x22,\x22click\
\x22,function(){var\
 h=a.$(f,\x22localR\
eader_files\x22)[0]\
.files[0],d=new \
FileReader;d.onl\
oadend=function(\
d){d.target.read\
yState==\x0aFileRea\
der.DONE&&(a._hi\
deLocalFileReade\
r(f,0),a._setDat\
a(e,h.name,h.nam\
e,d.target.resul\
t,b,f))};try{d.r\
eadAsArrayBuffer\
(h)}catch(c){ale\
rt(\x22You must sel\
ect a file first\
.\x22)}});a.$appEve\
nt(f,\x22localReade\
r_cancel\x22,\x22click\
\x22);a.$appEvent(f\
,\x22localReader_ca\
ncel\x22,\x22click\x22,fu\
nction(){a._hide\
LocalFileReader(\
f);e&&e.setData(\
\x22#CANCELED#\x22,nul\
l,null,b,f)});a.\
$setVisible(f._l\
ocalReader,!0);f\
._readingLocal=!\
0};a._setData=fu\
nction(e,f,h,b,d\
,c){b&&(b=a._str\
ToBytes(b));null\
!=b&&(null==e||0\
<=f.indexOf(\x22.jd\
x\x22))&&a.Cache.pu\
t(\x22cache://\x22+\x0af,\
b);null==e?c._ap\
plet.openFileAsy\
ncSpecial(null==\
b?f:\x22cache://\x22+f\
,1):e.setData(f,\
h,b,d)};a._doAja\
x=function(e,f,h\
){e=e.toString()\
;if(null!=h)retu\
rn a._saveFile(e\
,h);f&&(e+=\x22?POS\
T?\x22+f);return a.\
_getFileData(e,n\
ull,!0)};a._save\
File=function(e,\
f,h,b){if(a._loc\
alFileSaveFuncti\
on&&a._localFile\
SaveFunction(e,f\
))return\x22OK\x22;e=e\
.substring(e.las\
tIndexOf(\x22/\x22)+1)\
;h||(h=0<=e.inde\
xOf(\x22.pdf\x22)?\x22app\
lication/pdf\x22:0<\
=e.indexOf(\x22.png\
\x22)?\x22image/png\x22:0\
<=e.indexOf(\x22.gi\
f\x22)?\x22image/gif\x22:\
0<=e.indexOf(\x22.j\
pg\x22)?\x22image/jpg\x22\
:\x22\x22);\x0avar d=\x22str\
ing\x22==typeof f;d\
||(f=(JU?JU:J.ut\
il).Base64.getBa\
se64(f).toString\
());b||(b=d?\x22\x22:\x22\
base64\x22);(d=a._s\
erverUrl)&&0<=d.\
indexOf(\x22your.se\
rver\x22)&&(d=\x22\x22);a\
._useDataURI||!d\
?(b||(f=btoa(f))\
,b=document.crea\
teElement(\x22a\x22),b\
.href=\x22data:\x22+h+\
\x22;base64,\x22+f,b.t\
ype=h||\x22text/pla\
in\x22,b.download=e\
,b.target=\x22_blan\
k\x22,j(\x22body\x22).app\
end(b),b.click()\
,b.remove()):(a.\
_formdiv||(a.$af\
ter(\x22body\x22,'<div\
 id=\x22__jsmolform\
div__\x22 style=\x22di\
splay:none\x22>\x5ct\x5ct\
\x5ct\x5ct\x5ct\x5ct<form id\
=\x22__jsmolform__\x22\
 method=\x22post\x22 t\
arget=\x22_blank\x22 a\
ction=\x22\x22>\x5ct\x5ct\x5ct\x5c\
t\x5ct\x5ct<input name\
=\x22call\x22 value=\x22s\
aveFile\x22/>\x5ct\x5ct\x5ct\
\x5ct\x5ct\x5ct<input id=\
\x22__jsmolmimetype\
__\x22 name=\x22mimety\
pe\x22 value=\x22\x22/>\x5ct\
\x5ct\x5ct\x5ct\x5ct\x5ct<input\
 id=\x22__jsmolenco\
ding__\x22 name=\x22en\
coding\x22 value=\x22\x22\
/>\x5ct\x5ct\x5ct\x5ct\x5ct\x5ct<i\
nput id=\x22__jsmol\
filename__\x22 name\
=\x22filename\x22 valu\
e=\x22\x22/>\x5ct\x5ct\x5ct\x5ct\x5ct\
\x5ct<textarea id=\x22\
__jsmoldata__\x22 n\
ame=\x22data\x22></tex\
tarea>\x5ct\x5ct\x5ct\x5ct\x5ct\
\x5ct</form>\x5ct\x5ct\x5ct\x5c\
t\x5ct\x5ct</div>'),\x0aa\
._formdiv=\x22__jsm\
olform__\x22),a.$at\
tr(a._formdiv,\x22a\
ction\x22,d+\x22?\x22+(ne\
w Date).getMilli\
seconds()),a.$va\
l(\x22__jsmoldata__\
\x22,f),a.$val(\x22__j\
smolfilename__\x22,\
e),a.$val(\x22__jsm\
olmimetype__\x22,h)\
,a.$val(\x22__jsmol\
encoding__\x22,b),a\
.$submit(\x22__jsmo\
lform__\x22),a.$val\
(\x22__jsmoldata__\x22\
,\x22\x22),a.$val(\x22__j\
smolfilename__\x22,\
\x22\x22));return\x22OK\x22}\
;a._strToBytes=f\
unction(a){if(Cl\
azz.instanceOf(a\
,self.ArrayBuffe\
r))return Clazz.\
newByteArray(-1,\
a);for(var f=Cla\
zz.newByteArray(\
a.length,0),b=a.\
length;0<=--b;)f\
[b]=a.charCodeAt\
(b)&255;return f\
};a._setConsoleD\
iv=\x0afunction(a){\
self.Clazz&&Claz\
z.setConsoleDiv(\
a)};a._registerA\
pplet=function(e\
,f){return windo\
w[e]=a._applets[\
e]=a._applets[e+\
\x22__\x22+a._syncId+\x22\
__\x22]=f};a._ready\
Callback=functio\
n(e,f,b,d,c){e=e\
.split(\x22_object\x22\
)[0];var g=a._ap\
plets[e];if(b=b.\
booleanValue?b.b\
ooleanValue():b)\
g._appletPanel=c\
||d,g._applet=d;\
a._track(g._read\
yCallback(e,f,b)\
)};a._getWrapper\
=function(e,f){v\
ar b;if(f){var d\
=\x22\x22;if(e._coverI\
mage)var d=' onc\
lick=\x22Jmol.cover\
Applet(ID, false\
)\x22 title=\x22'+e._c\
overTitle+'\x22',c=\
'<image id=\x22ID_c\
overclickgo\x22 src\
=\x22'+\x0ae._makeLive\
Image+'\x22 style=\x22\
width:25px;heigh\
t:25px;position:\
absolute;bottom:\
10px;left:10px;z\
-index:'+a._getZ\
(e,\x22coverImage\x22)\
+';opacity:0.5;\x22\
'+d+\x22 />\x22,d='<di\
v id=\x22ID_coverdi\
v\x22 style=\x22backgr\
ound-color:red;z\
-index:'+a._getZ\
(e,\x22coverImage\x22)\
+';width:100%;he\
ight:100%;displa\
y:inline;positio\
n:absolute;top:0\
px;left:0px\x22><im\
age id=\x22ID_cover\
image\x22 src=\x22'+e.\
_coverImage+'\x22 s\
tyle=\x22width:100%\
;height:100%\x22'+d\
+\x22/>\x22+c+\x22</div>\x22\
;c=e._isJava?\x22\x22:\
'<image id=\x22ID_w\
aitimage\x22 src=\x22'\
+e._j2sPath+'/im\
g/cursor_wait.gi\
f\x22 style=\x22displa\
y:none;position:\
absolute;bottom:\
10px;left:10px;z\
-index:'+\x0aa._get\
Z(e,\x22coverImage\x22\
)+';\x22 />';b=a._a\
ppletCssText.rep\
lace(/\x5c'/g,'\x22');\
var g=e._getSpin\
ner&&e._getSpinn\
er();e._spinner=\
g=!g||\x22none\x22==g?\
\x22\x22:\x22background-i\
mage:url(\x22+g+\x22);\
 background-repe\
at:no-repeat; ba\
ckground-positio\
n:center;\x22;b=g+(\
0<=b.indexOf('st\
yle=\x22')?b.split(\
'style=\x22')[1]:'\x22\
 '+b);b='...<div\
 id=\x22ID_appletin\
fotablediv\x22 styl\
e=\x22width:Wpx;hei\
ght:Hpx;position\
:relative;font-s\
ize:14px;text-al\
ign:left\x22>IMG WA\
IT......<div id=\
\x22ID_appletdiv\x22 s\
tyle=\x22z-index:'+\
a._getZ(e,\x22heade\
r\x22)+\x22;width:100%\
;height:100%;pos\
ition:absolute;t\
op:0px;left:0px;\
\x22+\x0ab+\x22>\x22;var g=e\
._height,k=e._wi\
dth;if(\x22string\x22!\
==typeof g||0>g.\
indexOf(\x22%\x22))g+=\
\x22px\x22;if(\x22string\x22\
!==typeof k||0>k\
.indexOf(\x22%\x22))k+\
=\x22px\x22;b=b.replac\
e(/IMG/,d).repla\
ce(/WAIT/,c).rep\
lace(/Hpx/g,g).r\
eplace(/Wpx/g,k)\
}else b='......<\
/div>......<div \
id=\x22ID_2dappletd\
iv\x22 style=\x22posit\
ion:absolute;wid\
th:100%;height:1\
00%;overflow:hid\
den;display:none\
\x22></div>......<d\
iv id=\x22ID_infota\
blediv\x22 style=\x22w\
idth:100%;height\
:100%;position:a\
bsolute;top:0px;\
left:0px\x22>......\
...<div id=\x22ID_i\
nfoheaderdiv\x22 st\
yle=\x22height:20px\
;width:100%;back\
ground:yellow;di\
splay:none\x22><spa\
n id=\x22ID_infohea\
derspan\x22></span>\
<span id=\x22ID_inf\
ocheckboxspan\x22 s\
tyle=\x22position:a\
bsolute;text-ali\
gn:right;right:1\
px;\x22><a href=\x22ja\
vascript:Jmol.sh\
owInfo(ID,false)\
\x22>[x]</a></span>\
</div>.........<\
div id=\x22ID_infod\
iv\x22 style=\x22posit\
ion:absolute;top\
:20px;bottom:0px\
;width:100%;heig\
ht:100%;overflow\
:auto\x22></div>...\
...</div>...</di\
v>';\x0areturn b.re\
place(/\x5c.\x5c.\x5c./g,\
\x22\x22).replace(/[\x5cn\
\x5cr]/g,\x22\x22).replac\
e(/ID/g,e._id)};\
a._hideLoadingSp\
inner=function(e\
){e._spinner&&a.\
$css(a.$(e,\x22appl\
etdiv\x22),{\x22backgr\
ound-image\x22:\x22\x22})\
};a._documentWri\
te=function(e){i\
f(a._document){i\
f(a._isXHTML&&!a\
._XhtmlElement){\
var f=document.g\
etElementsByTagN\
ame(\x22script\x22);a.\
_XhtmlElement=f.\
item(f.length-1)\
;a._XhtmlAppendC\
hild=!1}a._Xhtml\
Element?a._domWr\
ite(e):a._docume\
nt.write(e)}retu\
rn e};a._domWrit\
e=function(e){fo\
r(var f=[0];f[0]\
<e.length;){var \
b=a._getDomEleme\
nt(e,f);if(!b)br\
eak;\x0aa._XhtmlApp\
endChild?a._Xhtm\
lElement.appendC\
hild(b):a._Xhtml\
Element.parentNo\
de.insertBefore(\
b,_jmol.XhtmlEle\
ment)}};a._getDo\
mElement=functio\
n(a,f){var b=doc\
ument.createElem\
ent(\x22span\x22);b.in\
nerHTML=a;f[0]=a\
.length;return b\
};a._setObject=f\
unction(e,f,b){e\
._id=f;e.__Info=\
{};b.z&&b.zIndex\
Base&&(a._z=a._g\
etZOrders(b.zInd\
exBase));for(var\
 d in b)e.__Info\
[d]=b[d];(e._z=b\
.z)||b.zIndexBas\
e&&(e._z=e.__Inf\
o.z=a._getZOrder\
s(b.zIndexBase))\
;e._width=b.widt\
h;e._height=b.he\
ight;e._noscript\
=!e._isJava&&b.n\
oscript;e._conso\
le=\x0ab.console;e.\
_cacheFiles=!!b.\
cacheFiles;e._vi\
ewSet=null==b.vi\
ewSet||e._isJava\
?null:\x22Set\x22+b.vi\
ewSet;null!=e._v\
iewSet&&(a.View.\
__init(e),e._cur\
rentView=null);!\
a._fileCache&&e.\
_cacheFiles&&(a.\
_fileCache={});e\
._console||(e._c\
onsole=e._id+\x22_i\
nfodiv\x22);\x22none\x22=\
=e._console&&(e.\
_console=null);e\
._color=b.color?\
b.color.replace(\
/0x/,\x22#\x22):\x22#FFFF\
FF\x22;e._disableIn\
itialConsole=b.d\
isableInitialCon\
sole;e._noMonito\
r=b.disableJ2SLo\
adMonitor;a._j2s\
Path&&(b.j2sPath\
=a._j2sPath);e._\
j2sPath=b.j2sPat\
h;e._coverImage=\
b.coverImage;\x0ae.\
_makeLiveImage=b\
.makeLiveImage||\
b.j2sPath+\x22/img/\
play_make_live.j\
pg\x22;e._isCovered\
=!!e._coverImage\
;e._deferApplet=\
b.deferApplet||e\
._isCovered&&e._\
isJava;e._deferU\
ncover=b.deferUn\
cover&&!e._isJav\
a;e._coverScript\
=b.coverScript;e\
._coverTitle=b.c\
overTitle;e._cov\
erTitle||(e._cov\
erTitle=e._defer\
Applet?\x22activate\
 3D model\x22:\x223D m\
odel is loading.\
..\x22);e._containe\
rWidth=e._width+\
(e._width==parse\
Float(e._width)?\
\x22px\x22:\x22\x22);e._cont\
ainerHeight=e._h\
eight+(e._height\
==parseFloat(e._\
height)?\x22px\x22:\x22\x22)\
;e._info=\x22\x22;e._i\
nfoHeader=\x0ae._jm\
olType+' \x22'+e._i\
d+'\x22';e._hasOpti\
ons=b.addSelecti\
onOptions;e._def\
aultModel=b.defa\
ultModel;e._read\
yScript=b.script\
?b.script:\x22\x22;e._\
readyFunction=b.\
readyFunction;e.\
_coverImage&&!e.\
_deferApplet&&(e\
._readyScript+=\x22\
;javascript \x22+f+\
\x22._displayCoverI\
mage(false)\x22);e.\
_src=b.src};a._a\
ddDefaultInfo=fu\
nction(e,f){for(\
var b in f)\x22unde\
fined\x22==typeof e\
[b]&&(e[b]=f[b])\
;a._use&&(e.use=\
a._use);0<=e.use\
.indexOf(\x22SIGNED\
\x22)&&(0>e.jarFile\
.indexOf(\x22Signed\
\x22)&&(e.jarFile=e\
.jarFile.replace\
(/Applet/,\x22Apple\
tSigned\x22)),e.use\
=\x0ae.use.replace(\
/SIGNED/,\x22JAVA\x22)\
,e.isSigned=!0)}\
;a._syncedApplet\
s=[];a._syncedCo\
mmands=[];a._syn\
cedReady=[];a._s\
yncReady=!1;a._i\
sJmolJSVSync=!1;\
a._setReady=func\
tion(e){a._synce\
dReady[e]=1;for(\
var f=0,b=0;b<a.\
_syncedApplets.l\
ength;b++){if(a.\
_syncedApplets[b\
]==e._id)a._sync\
edApplets[b]=e,a\
._syncedReady[b]\
=1;else if(!a._s\
yncedReady[b])co\
ntinue;f++}f==a.\
_syncedApplets.l\
ength&&a._setSyn\
cReady()};a._set\
Destroy=function\
(e){a.featureDet\
ection.allowDest\
roy&&a.$windowOn\
(\x22beforeunload\x22,\
function(){a._de\
stroy(e)})};\x0aa._\
destroy=function\
(e){try{e._apple\
tPanel&&e._apple\
tPanel.destroy()\
;e._applet=null;\
a._unsetMouse(e.\
_canvas);e._canv\
as=null;for(var \
b=0,h=0;h<a._syn\
cedApplets.lengt\
h;h++)a._syncedA\
pplets[h]==e&&(a\
._syncedApplets[\
h]=null),a._sync\
edApplets[h]&&b+\
+;0<b||a._clearV\
ars()}catch(d){}\
};a._setSyncRead\
y=function(){a._\
syncReady=!0;for\
(var e=\x22\x22,b=0;b<\
a._syncedApplets\
.length;b++)a._s\
yncedCommands[b]\
&&(e+=\x22Jmol.scri\
pt(Jmol._syncedA\
pplets[\x22+b+\x22], J\
mol._syncedComma\
nds[\x22+b+\x22]);\x22);s\
etTimeout(e,50)}\
;a._mySyncCallba\
ck=\x0afunction(e,b\
){app=a._applets\
[e];if(app._view\
Set)a.View.updat\
eFromSync(app,b)\
;else{if(!a._syn\
cReady||!a._isJm\
olJSVSync)return\
 1;for(var h=0;h\
<a._syncedApplet\
s.length;h++)0<=\
b.indexOf(a._syn\
cedApplets[h]._s\
yncKeyword)&&a._\
syncedApplets[h]\
._syncScript(b);\
return 0}};a._ge\
tElement=functio\
n(a,b){return do\
cument.getElemen\
tById(a._id+\x22_\x22+\
b)||{}};a._evalJ\
SON=function(a,b\
){a+=\x22\x22;if(!a)re\
turn[];if(\x22{\x22!=a\
.charAt(0))retur\
n 0<=a.indexOf(\x22\
 | \x22)&&(a=a.repl\
ace(/\x5c \x5c|\x5c /g,\x22\x5c\
n\x22)),a;var h=(ne\
w Function(\x22retu\
rn \x22+a))();\x0aretu\
rn!h?null:b&&voi\
d 0!=h[b]?h[b]:h\
};a._sortMessage\
s=function(a){fu\
nction b(a,e){re\
turn a[0]<e[0]?1\
:a[0]>e[0]?-1:0}\
if(!a||\x22object\x22!\
=typeof a)return\
[];for(var h=[],\
d=a.length-1;0<=\
d;d--)for(var c=\
0,g=a[d].length;\
c<g;c++)h[h.leng\
th]=a[d][c];if(0\
!=h.length)retur\
n h=h.sort(b)};a\
._setMouseOwner=\
function(e,b){nu\
ll==e||b?a._mous\
eOwner=e:a._mous\
eOwner==e&&(a._m\
ouseOwner=null)}\
;a._jsGetMouseMo\
difiers=function\
(a){var b=0;swit\
ch(a.button){cas\
e 0:b=16;break;c\
ase 1:b=8;break;\
case 2:b=4}a.shi\
ftKey&&(b+=1);a.\
altKey&&\x0a(b+=8);\
a.ctrlKey&&(b+=2\
);return b};a._j\
sGetXY=function(\
b,f){if(!b.apple\
t._ready||a._tou\
ching&&0>f.type.\
indexOf(\x22touch\x22)\
)return!1;var h=\
a.$offset(b.id),\
d,c=f.originalEv\
ent;f.pageX||(f.\
pageX=c.pageX);f\
.pageY||(f.pageY\
=c.pageY);a._mou\
sePageX=f.pageX;\
a._mousePageY=f.\
pageY;c.targetTo\
uches&&c.targetT\
ouches[0]?(d=c.t\
argetTouches[0].\
pageX-h.left,h=c\
.targetTouches[0\
].pageY-h.top):c\
.changedTouches?\
(d=c.changedTouc\
hes[0].pageX-h.l\
eft,h=c.changedT\
ouches[0].pageY-\
h.top):(d=f.page\
X-h.left,h=f.pag\
eY-h.top);return\
 void 0==\x0ad?null\
:[Math.round(d),\
Math.round(h),a.\
_jsGetMouseModif\
iers(f)]};a._set\
Cursor=function(\
b,f){if(!b._isJa\
va&&!b._readingL\
ocal){var h;swit\
ch(f){case 1:h=\x22\
crosshair\x22;break\
;case 3:h=\x22wait\x22\
;a.$setVisible(a\
.$(b,\x22waitimage\x22\
),!0);break;case\
 8:h=\x22ns-resize\x22\
;break;case 12:h\
=\x22grab\x22;break;ca\
se 13:h=\x22move\x22;b\
reak;default:a.$\
setVisible(a.$(b\
,\x22waitimage\x22),!1\
),h=\x22default\x22}b.\
_canvas.style.cu\
rsor=h}};a._gest\
ureUpdate=functi\
on(b,f){f.stopPr\
opagation();f.pr\
eventDefault();v\
ar h=f.originalE\
vent;switch(f.ty\
pe){case \x22touchs\
tart\x22:a._touchin\
g=\x0a!0;break;case\
 \x22touchend\x22:a._t\
ouching=!1}if(!h\
.touches||2!=h.t\
ouches.length)re\
turn!1;switch(f.\
type){case \x22touc\
hstart\x22:b._touch\
es=[[],[]];break\
;case \x22touchmove\
\x22:var d=a.$offse\
t(b.id),c=b._tou\
ches[0],g=b._tou\
ches[1];c.push([\
h.touches[0].pag\
eX-d.left,h.touc\
hes[0].pageY-d.t\
op]);g.push([h.t\
ouches[1].pageX-\
d.left,h.touches\
[1].pageY-d.top]\
);h=c.length;3<h\
&&(c.shift(),g.s\
hift());2<=h&&b.\
applet._processG\
esture(b._touche\
s)}return!0};a._\
jsSetMouse=funct\
ion(b){var f=fun\
ction(a){return!\
a.target||0<=(\x22\x22\
+a.target.classN\
ame).indexOf(\x22sw\
ingjs-ui\x22)};\x0aa.$\
bind(b,\x22mousedow\
n touchstart\x22,fu\
nction(h){if(f(h\
))return!0;a._se\
tMouseOwner(b,!0\
);h.stopPropagat\
ion();var d=h.ta\
rget[\x22data-UI\x22];\
(!d||!d.handleJS\
Event(b,501,h))&\
&h.preventDefaul\
t();b.isDragging\
=!0;if(\x22touchsta\
rt\x22==h.type&&a._\
gestureUpdate(b,\
h))return!!d;a._\
setConsoleDiv(b.\
applet._console)\
;var c=a._jsGetX\
Y(b,h);c&&(2!=h.\
button&&a.Swing.\
hideMenus(b.appl\
et),b.applet._pr\
ocessEvent(501,c\
));return!!d});a\
.$bind(b,\x22mouseu\
p touchend\x22,func\
tion(h){if(f(h))\
return!0;a._setM\
ouseOwner(null);\
h.stopPropagatio\
n();\x0avar d=h.tar\
get[\x22data-UI\x22];(\
!d||!d.handleJSE\
vent(b,502,h))&&\
h.preventDefault\
();b.isDragging=\
!1;if(\x22touchend\x22\
==h.type&&a._ges\
tureUpdate(b,h))\
return!!d;(h=a._\
jsGetXY(b,h))&&b\
.applet._process\
Event(502,h);ret\
urn!!d});a.$bind\
(b,\x22mousemove to\
uchmove\x22,functio\
n(h){if(f(h))ret\
urn!0;if(a._mous\
eOwner&&a._mouse\
Owner!=b&&a._mou\
seOwner.isDraggi\
ng){if(!a._mouse\
Owner.mouseMove)\
return!0;a._mous\
eOwner.mouseMove\
(h);return!1}ret\
urn a._drag(b,h)\
});a._drag=funct\
ion(b,e){e.stopP\
ropagation();e.p\
reventDefault();\
if(\x22touchmove\x22==\
\x0ae.type&&a._gest\
ureUpdate(b,e))r\
eturn!1;var f=a.\
_jsGetXY(b,e);if\
(!f)return!1;b.i\
sDragging||(f[2]\
=0);var d=e.targ\
et[\x22data-UI\x22];b.\
isdragging&&(!d|\
|d.handleJSEvent\
(b,506,e));b.app\
let._processEven\
t(b.isDragging?5\
06:503,f);return\
!!d};a.$bind(b,\x22\
DOMMouseScroll m\
ousewheel\x22,funct\
ion(h){if(f(h))r\
eturn!0;h.stopPr\
opagation();h.pr\
eventDefault();b\
.isDragging=!1;v\
ar d=h.originalE\
vent,d=d.detail?\
d.detail:(\x22mac\x22=\
=a.featureDetect\
ion.os?1:-1)*d.w\
heelDelta;h=a._j\
sGetMouseModifie\
rs(h);b.applet._\
processEvent(-1,\
[0>d?-1:\x0a1,0,h])\
;return!1});a.$b\
ind(b,\x22contextme\
nu\x22,function(){r\
eturn!1});a.$bin\
d(b,\x22mouseout\x22,f\
unction(h){if(f(\
h))return!0;a._m\
ouseOwner&&!a._m\
ouseOwner.mouseM\
ove&&a._setMouse\
Owner(null);b.ap\
plet._appletPane\
l&&b.applet._app\
letPanel.startHo\
verWatcher(!1);a\
._jsGetXY(b,h);r\
eturn!1});a.$bin\
d(b,\x22mouseenter\x22\
,function(h){if(\
f(h))return!0;b.\
applet._appletPa\
nel&&b.applet._a\
ppletPanel.start\
HoverWatcher(!0)\
;if(0===h.button\
s||0===h.which){\
b.isDragging=!1;\
h=a._jsGetXY(b,h\
);if(!h)return!1\
;b.applet._proce\
ssEvent(504,h);\x0a\
b.applet._proces\
sEvent(502,h);re\
turn!1}});a.$bin\
d(b,\x22mousemoveou\
tjsmol\x22,function\
(h,d,c){if(f(c))\
return!0;if(b==a\
._mouseOwner&&b.\
isDragging)retur\
n a._drag(b,c)})\
;b.applet._is2D&\
&a.$resize(funct\
ion(){b.applet&&\
b.applet._resize\
()});a.$bind(\x22bo\
dy\x22,\x22mouseup tou\
chend\x22,function(\
h){if(f(h))retur\
n!0;b.applet&&(b\
.isDragging=!1);\
a._setMouseOwner\
(null)})};a._jsU\
nsetMouse=functi\
on(b){b.applet=n\
ull;a.$bind(b,\x22m\
ousedown touchst\
art mousemove to\
uchmove mouseup \
touchend DOMMous\
eScroll mousewhe\
el contextmenu m\
ouseout mouseent\
er\x22,\x0anull);a._se\
tMouseOwner(null\
)};a.Swing={coun\
t:0,menuInitiali\
zed:0,menuCounte\
r:0,htDialogs:{}\
};var m=a.Swing;\
SwingController=\
m;m.setDraggable\
=function(b){b=b\
.prototype;b.set\
Container||(b.se\
tContainer=funct\
ion(b){this.cont\
ainer=b;b.obj=th\
is;this.ignoreMo\
use=this.isDragg\
ing=!1;var e=thi\
s;b.bind(\x22moused\
own touchstart\x22,\
function(b){if(e\
.ignoreMouse)ret\
urn e.ignoreMous\
e=!1,!0;a._setMo\
useOwner(e,!0);e\
.isDragging=!0;e\
.pageX=b.pageX;e\
.pageY=b.pageY;r\
eturn!1});b.bind\
(\x22mousemove touc\
hmove\x22,function(\
b){if(e.isDraggi\
ng&&\x0aa._mouseOwn\
er==e)return e.m\
ouseMove(b),!1})\
;b.bind(\x22mouseup\
 touchend\x22,funct\
ion(b){e.mouseUp\
(b);a._setMouseO\
wner(null)})},b.\
mouseUp=function\
(b){if(this.isDr\
agging&&a._mouse\
Owner==this)retu\
rn this.pageX0+=\
b.pageX-this.pag\
eX,this.pageY0+=\
b.pageY-this.pag\
eY,this.isDraggi\
ng=!1;a._setMous\
eOwner(null)},b.\
setPosition=func\
tion(){if(null==\
=a._mousePageX){\
var b=a.$offset(\
this.applet._id+\
\x22_\x22+(this.applet\
._is2D?\x22canvas2d\
\x22:\x22canvas\x22));a._\
mousePageX=b.lef\
t;a._mousePageY=\
b.top}this.pageX\
0=a._mousePageX;\
this.pageY0=\x0aa._\
mousePageY;this.\
container.css({t\
op:a._mousePageY\
+\x22px\x22,left:a._mo\
usePageX+\x22px\x22})}\
,b.mouseMove=fun\
ction(b){if(this\
.isDragging&&a._\
mouseOwner==this\
){this.timestamp\
=System.currentT\
imeMillis();var \
e=this.pageX0+(b\
.pageX-this.page\
X);b=this.pageY0\
+(b.pageY-this.p\
ageY);a._mousePa\
geX=e;a._mousePa\
geY=b;this.conta\
iner.css({top:b+\
\x22px\x22,left:e+\x22px\x22\
})}},b.dragBind=\
function(b){this\
.applet._ignoreM\
ouse=!b;this.con\
tainer.unbind(\x22m\
ousemoveoutjsmol\
\x22);this.containe\
r.unbind(\x22touchm\
oveoutjsmol\x22);th\
is.container.unb\
ind(\x22mouseupoutj\
smol\x22);\x0athis.con\
tainer.unbind(\x22t\
ouchendoutjsmol\x22\
);a._setMouseOwn\
er(null);if(b){v\
ar e=this;this.c\
ontainer.bind(\x22m\
ousemoveoutjsmol\
 touchmoveoutjsm\
ol\x22,function(a,b\
,f){e.mouseMove(\
f)});this.contai\
ner.bind(\x22mouseu\
poutjsmol touche\
ndoutjsmol\x22,func\
tion(a,b,f){e.mo\
useUp(f)})}})};m\
.JSDialog=functi\
on(){};m.setDrag\
gable(m.JSDialog\
);m.getScreenDim\
ensions=function\
(a){a.width=j(wi\
ndow).width();a.\
height=j(window)\
.height()};m.dis\
pose=function(b)\
{a.$remove(b.id+\
\x22_mover\x22);delete\
 m.htDialogs[b.i\
d];b.container.o\
bj.dragBind(!1)}\
;\x0am.register=fun\
ction(a,b){a.id=\
b+ ++m.count;m.h\
tDialogs[a.id]=a\
};m.setDialog=fu\
nction(b){a._set\
MouseOwner(null)\
;a.$remove(b.id)\
;var f=b.id+\x22_mo\
ver\x22,d=a._$(f),c\
;d[0]?(d.html(b.\
html),c=d[0].jd)\
:(a.$after(\x22body\
\x22,\x22<div id='\x22+f+\
\x22' style='positi\
on:absolute;left\
:0px;top:0px;'>\x22\
+b.html+\x22</div>\x22\
),c=new m.JSDial\
og,d=a._$(f),b.c\
ontainer=d,c.app\
let=b.manager.vw\
r.html5Applet,c.\
setContainer(d),\
c.dialog=b,c.set\
Position(),c.dra\
gBind(!0),d[0].j\
d=c);a.$bind(\x22#\x22\
+b.id+\x22 .JButton\
\x22,\x22mousedown tou\
chstart\x22,functio\
n(){c.ignoreMous\
e=\x0a!0});a.$bind(\
\x22#\x22+b.id+\x22 .JCom\
boBox\x22,\x22mousedow\
n touchstart\x22,fu\
nction(){c.ignor\
eMouse=!0});a.$b\
ind(\x22#\x22+b.id+\x22 .\
JCheckBox\x22,\x22mous\
edown touchstart\
\x22,function(){c.i\
gnoreMouse=!0});\
a.$bind(\x22#\x22+b.id\
+\x22 .JTextField\x22,\
\x22mousedown touch\
start\x22,function(\
){c.ignoreMouse=\
!0});a.$bind(\x22#\x22\
+b.id+\x22 .JTable\x22\
,\x22mousedown touc\
hstart\x22,function\
(){c.ignoreMouse\
=!0});a.$bind(\x22#\
\x22+b.id+\x22 .JScrol\
lPane\x22,\x22mousedow\
n touchstart\x22,fu\
nction(){c.ignor\
eMouse=!0});a.$b\
ind(\x22#\x22+b.id+\x22 .\
JEditorPane\x22,\x22mo\
usedown touchsta\
rt\x22,function(){c\
.ignoreMouse=\x0a!0\
})};m.setSelecte\
d=function(b){a.\
$prop(b.id,\x22chec\
ked\x22,!!b.selecte\
d)};m.setSelecte\
dIndex=function(\
b){a.$prop(b.id,\
\x22selectedIndex\x22,\
b.selectedIndex)\
};m.setText=func\
tion(b){a.$prop(\
b.id,\x22value\x22,b.t\
ext)};m.setVisib\
le=function(b){a\
.$setVisible(b.i\
d,b.visible)};m.\
setEnabled=funct\
ion(b){a.$setEna\
bled(b.id,b.enab\
led)};m.click=fu\
nction(b,f){var \
d=m.htDialogs[b.\
id];if(d){var c=\
d.toString();if(\
0<=c.indexOf(\x22JC\
heck\x22))d.selecte\
d=b.checked;else\
 if(0<=c.indexOf\
(\x22JCombo\x22))d.sel\
ectedIndex=b.sel\
ectedIndex;else \
if(null!=\x0ad.text\
&&(d.text=b.valu\
e,f&&13!=(f.char\
Code||f.keyCode)\
))return}c=m.htD\
ialogs[a.$getAnc\
estorDiv(b.id,\x22J\
Dialog\x22).id];c.m\
anager.actionPer\
formed(d?d.name:\
c.registryKey+\x22/\
\x22+b.id)};m.setFr\
ont=function(b){\
var f=b.manager.\
vwr.html5Applet;\
b.zIndex!=a._get\
Z(f,\x22dialog\x22)&&(\
b.zIndex=a._incr\
Z(f,\x22dialog\x22));b\
.container&&((b.\
container[0]||b.\
container).style\
.zIndex=b.zIndex\
)};m.hideMenus=f\
unction(a){if(a=\
a._menus)for(var\
 b in a)a[b].vis\
ible&&m.hideMenu\
(a[b])};m.window\
Closing=function\
(b){b=m.htDialog\
s[a.$getAncestor\
Div(b.id,\x0a\x22JDial\
og\x22).id];b.regis\
tryKey?b.manager\
.processWindowCl\
osing(b.registry\
Key):b.dispose()\
};a._track=funct\
ion(b){if(a._tra\
cker){try{var f=\
'<iframe style=\x22\
display:none\x22 wi\
dth=\x220\x22 height=\x22\
0\x22 frameborder=\x22\
0\x22 tabindex=\x22-1\x22\
 src=\x22'+(a._trac\
ker+\x22&applet=\x22+b\
._jmolType+\x22&ver\
sion=\x22+a._versio\
n+\x22&appver=\x22+a._\
__JmolVersion+\x22&\
url=\x22+encodeURIC\
omponent(documen\
t.location.href)\
)+'\x22></iframe>';\
a.$after(\x22body\x22,\
f)}catch(d){}del\
ete a._tracker}r\
eturn b};var l;a\
.getProfile=func\
tion(a){if(self.\
Clazz&&self.JSON\
)return l||Clazz\
._startProfiling\
(l=\x0a0==arguments\
.length||a),Claz\
z.getProfile()};\
a._getInChIKey=f\
unction(a,b){0<=\
b.indexOf(\x22MOL=\x22\
)&&b.split(\x22MOL=\
\x22)[1].split('\x22')\
};a._getAttr=fun\
ction(a,b){var d\
=a.indexOf(b+\x22=\x22\
);return 0<=d&&0\
<=(d=a.indexOf('\
\x22',d))?a.substri\
ng(d+1,a.indexOf\
('\x22',d+1)):null}\
;a.User={viewUpd\
atedCallback:nul\
l};a.View={count\
:0,applets:{},se\
ts:{}};(function\
(b){b.updateView\
=function(f,d){i\
f(null!=f._viewS\
et){d.chemID||(f\
._searchQuery=nu\
ll);d.data||(d.d\
ata=\x22N/A\x22);d.typ\
e=f._viewType;if\
(null==(f._curre\
ntView=b.__findV\
iew(f._viewSet,\x0a\
d)))f._currentVi\
ew=b.__createVie\
wSet(f._viewSet,\
d.chemID,d.viewI\
D||d.chemID);f._\
currentView[d.ty\
pe].data=d.data;\
f._currentView[d\
.type].smiles=f.\
_getSmiles();a.U\
ser.viewUpdatedC\
allback&&a.User.\
viewUpdatedCallb\
ack(f,\x22updateVie\
w\x22);b.__setView(\
f._currentView,f\
,!1)}};b.updateF\
romSync=function\
(f,d){f._updateM\
sg=d;var c=a._ge\
tAttr(d,\x22sourceI\
D\x22)||a._getAttr(\
d,\x22file\x22);if(c){\
var g=b.__findVi\
ew(f._viewSet,{v\
iewID:c});if(nul\
l==g)return a.up\
dateView(f,d);g!\
=f._currentView&\
&b.__setView(g,f\
,!0);var k=(c=a.\
_getAttr(d,\x0a\x22ato\
ms\x22))&&0<=d.inde\
xOf(\x22selectionha\
los ON\x22)?eval(\x22[\
\x22+c+\x22]\x22):[];setT\
imeout(function(\
){f._currentView\
==g&&b.updateAto\
mPick(f,k)},10);\
a.User.viewUpdat\
edCallback&&a.Us\
er.viewUpdatedCa\
llback(f,\x22update\
FromSync\x22)}};b.u\
pdateAtomPick=fu\
nction(b,e){var \
d=b._currentView\
;if(null!=d){for\
(var c in d)\x22inf\
o\x22!=c&&d[c].appl\
et!=b&&d[c].appl\
et._updateAtomPi\
ck(e);a.User.vie\
wUpdatedCallback\
&&a.User.viewUpd\
atedCallback(b,\x22\
updateAtomPick\x22)\
}};b.dumpViews=f\
unction(a){var d\
=b.sets[a];if(d)\
{var c=\x22View set\
 \x22+a+\x22:\x5cn\x22;a=b.a\
pplets[a];\x0afor(v\
ar g in a)c+=\x22\x5cn\
applet \x22+a[g]._i\
d+\x22 currentView=\
\x22+(a[g]._current\
View?a[g]._curre\
ntView.info.view\
ID:null);for(g=d\
.length;0<=--g;)\
{a=d[g];var c=c+\
(\x22\x5cn\x5cn<b>view=\x22+\
g+\x22 viewID=\x22+a.i\
nfo.viewID+\x22 che\
mID=\x22+a.info.che\
mID+\x22</b>\x5cn\x22),k,\
j;for(j in a)\x22in\
fo\x22!=j&&(c+=\x22\x5cnv\
iew=\x22+g+\x22 type=\x22\
+j+\x22 applet=\x22+((\
k=a[j]).applet?k\
.applet._id:null\
)+\x22 SMILES=\x22+k.s\
miles+\x22\x5cn atomMa\
p=\x22+JSON.stringi\
fy(k.atomMap)+\x22\x5c\
n data=\x5cn\x22+k.dat\
a+\x22\x5cn\x22)}return c\
}};b.__init=func\
tion(a){var d=a.\
_viewSet,c=b.app\
lets;c[d]||(c[d]\
={});c[d][a._vie\
wType]=\x0aa};b.__f\
indView=function\
(a,d){var c=b.se\
ts[a];null==c&&(\
c=b.sets[a]=[]);\
for(var g=c.leng\
th;0<=--g;){var \
k=c[g];if(d.view\
ID){if(k.info.vi\
ewID==d.viewID)r\
eturn k}else{if(\
null!=d.chemID&&\
d.chemID==k.info\
.chemID)return k\
;for(var j in k)\
if(\x22info\x22!=j&&(n\
ull!=d.data&&nul\
l!=k[j].data?d.d\
ata==k[j].data:d\
.type==j))return\
 k}}return null}\
;b.__createViewS\
et=function(f,d,\
c){b.count++;d={\
info:{chemID:d,v\
iewID:c||\x22model_\
\x22+b.count}};for(\
var g in a._appl\
ets)c=a._applets\
[g],c._viewSet==\
f&&(d[c._viewTyp\
e]={applet:c,\x0ada\
ta:null});b.sets\
[f].push(d);retu\
rn d};b.__setVie\
w=function(a,b,d\
){for(var e in a\
)if(\x22info\x22!=e){v\
ar c=a[e],g=c.ap\
plet,k=d||null!=\
g&&\x22<modified>\x22=\
=g._molData;if(!\
(null==g||g==b&&\
!k)){var j=null=\
=c.data,m=null!=\
g._currentView;g\
._currentView=a;\
if(!m||!(a[e].da\
ta==c.data&&!j&!\
k))if(g._loadMod\
elFromView(a),j)\
break}}}})(a.Vie\
w);a.Cache={file\
Cache:{}};a.Cach\
e.get=function(b\
){return a.Cache\
.fileCache[b]};a\
.Cache.put=funct\
ion(b,f){a.Cache\
.fileCache[b]=f}\
;a.Cache.setDrag\
Drop=function(b)\
{a.$appEvent(b,\x22\
appletdiv\x22,\x0a\x22dra\
gover\x22,function(\
a){a=a.originalE\
vent;a.stopPropa\
gation();a.preve\
ntDefault();a.da\
taTransfer.dropE\
ffect=\x22copy\x22});a\
.$appEvent(b,\x22ap\
pletdiv\x22,\x22drop\x22,\
function(f){var \
d=f.originalEven\
t;d.stopPropagat\
ion();d.preventD\
efault();var c=d\
.dataTransfer.fi\
les[0];if(null==\
c)try{c=\x22\x22+d.dat\
aTransfer.getDat\
a(\x22text\x22),(0==c.\
indexOf(\x22file:/\x22\
)||0==c.indexOf(\
\x22http:/\x22))&&b._s\
criptLoad(c)}cat\
ch(g){}else d=ne\
w FileReader,d.o\
nloadend=functio\
n(d){if(d.target\
.readyState==Fil\
eReader.DONE){va\
r g=\x22cache://DRO\
P_\x22+c.name;d=Cla\
zz.newByteArray(\
-1,\x0ad.target.res\
ult);g.endsWith(\
\x22.spt\x22)||b._appl\
etPanel.cacheFil\
eByName(\x22cache:/\
/DROP_*\x22,!1);\x22JS\
V\x22==b._viewType|\
|g.endsWith(\x22.jd\
x\x22)?a.Cache.put(\
g,d):b._appletPa\
nel.cachePut(g,d\
);(d=a._jsGetXY(\
b._canvas,f))&&(\
!b._appletPanel.\
setStatusDragDro\
pped||b._appletP\
anel.setStatusDr\
agDropped(0,d[0]\
,d[1],g))&&b._ap\
pletPanel.openFi\
leAsyncSpecial(g\
,1)}},d.readAsAr\
rayBuffer(c)})}}\
)(Jmol,jQuery);J\
mol._debugCode=!\
1;\x0a(function(a){\
a._isAsync=!1;a.\
_asyncCallbacks=\
{};a._coreFiles=\
[];var j=!1,g=[]\
,c=[],b=0,d=[],k\
=[],m=function(d\
){arguments.leng\
th||(d=!0);delet\
e b;for(var e;0<\
c.length&&\x22done\x22\
==(e=c[0])[4];)c\
.shift();if(0!=c\
.length)if(!a._i\
sAsync&&!d)setTi\
meout(m,10);else\
{e.push(\x22done\x22);\
var k=\x22JSmol exe\
c \x22+e[0]._id+\x22 \x22\
+e[3]+\x22 \x22+e[2];s\
elf.System&&Syst\
em.out.println(k\
);self.console&&\
console.log(k+\x22 \
-- OK\x22);g.push(k\
);e[1](e[0],e[2]\
)}},l=function(b\
){j?m():(j=!0,Lo\
adClazz(),b._noM\
onitor&&(Clazz._\
LoaderProgressMo\
nitor.showStatus\
=\x0afunction(){}),\
LoadClazz=null,b\
.__Info.uncompre\
ssed&&Clazz.load\
Class(),Clazz._L\
oader.onGlobalLo\
aded=function(){\
Clazz._LoaderPro\
gressMonitor.sho\
wStatus(\x22Applica\
tion loaded.\x22,!0\
);if(!a._debugCo\
de||!a.haveCore)\
a.haveCore=!0,m(\
)},Clazz._Loader\
.loadPackageClas\
spath(\x22java\x22,nul\
l,!0,m))},e=func\
tion(a,b){Clazz.\
_Loader.loadClas\
s(b,function(){m\
()})};a.showExec\
Log=function(){r\
eturn g.join(\x22\x5cn\
\x22)};a._addExec=f\
unction(a){a[1]|\
|(a[1]=e);var b=\
\x22JSmol load \x22+a[\
0]._id+\x22 \x22+a[3];\
self.console&&co\
nsole.log(b+\x22...\
\x22);g.push(b);\x0ac.\
push(a)};a._addC\
oreFile=function\
(b,e,c){b=b.toLo\
werCase().split(\
\x22.\x22)[0];if(!(0<=\
d.join(\x22\x22).index\
Of(b))){d.push(b\
);d.sort();a._co\
reFiles=[e+\x22/cor\
e/core\x22+d.join(\x22\
\x22)+\x22.z.js\x22];if(c\
&&(c=c.split(\x22 \x22\
)))for(b=0;b<c.l\
ength;b++)0>k.jo\
in(\x22\x22).indexOf(c\
[b])&&k.push(e+\x22\
/core/core\x22+c[b]\
+\x22.z.js\x22);for(b=\
0;b<k.length;b++\
)a._coreFiles.pu\
sh(k[b])}};a._Ca\
nvas2D=function(\
b,d,e,c){this._u\
niqueId=(\x22\x22+Math\
.random()).subst\
ring(3);this._id\
=b;this._is2D=!0\
;this._isJava=!1\
;this._jmolType=\
\x22Jmol._Canvas2D \
(\x22+e+\x22)\x22;this._i\
sLayered=\x0ad._isL\
ayered||!1;this.\
_isSwing=d._isSw\
ing||!1;this._is\
JSV=d._isJSV||!1\
;this._isAstex=d\
._isAstex||!1;th\
is._platform=d._\
platform||\x22\x22;if(\
c)return this;wi\
ndow[b]=this;thi\
s._createCanvas(\
b,d);if(!a._docu\
ment||this._defe\
rApplet)return t\
his;this._init()\
;return this};a.\
_setAppletParams\
=function(b,d,e,\
c){for(var g in \
e)if(!b||0<=b.in\
dexOf(\x22;\x22+g.toLo\
werCase()+\x22;\x22))n\
ull==e[g]||\x22lang\
uage\x22==g&&!a.fea\
tureDetection.su\
pportsLocalizati\
on()||(c?d.put(g\
,!0===e[g]?Boole\
an.TRUE:!1===e[g\
]?Boolean.FALSE:\
e[g]):d[g]=e[g])\
};\x0aa._jsSetProto\
type=function(d)\
{d._init=functio\
n(){this._setupJ\
S();this._showIn\
fo(!0);this._dis\
ableInitialConso\
le&&this._showIn\
fo(!1)};d._creat\
eCanvas=function\
(b,d,e){a._setOb\
ject(this,b,d);e\
&&(this._GLmol=e\
,this._GLmol.app\
let=this,this._G\
Lmol.id=this._id\
);e=a._getWrappe\
r(this,!0);this.\
_deferApplet||(a\
._document?(a._d\
ocumentWrite(e),\
this._newCanvas(\
!1),e=\x22\x22):(this.\
_deferApplet=!0,\
e+='<script type\
=\x22text/javascrip\
t\x22>'+b+\x22._cover(\
false)\x5cx3c/scrip\
t>\x22));e+=a._getW\
rapper(this,!1);\
d.addSelectionOp\
tions&&(e+=\x0aa._g\
etGrabberOptions\
(this));a._debug\
Alert&&!a._docum\
ent&&alert(e);th\
is._code=a._docu\
mentWrite(e)};d.\
_newCanvas=funct\
ion(a){this._is2\
D?this._createCa\
nvas2d(a):this._\
GLmol.create()};\
d._getHtml5Canva\
s=function(){ret\
urn this._canvas\
};d._getWidth=fu\
nction(){return \
this._canvas.wid\
th};d._getHeight\
=function(){retu\
rn this._canvas.\
height};d._getCo\
ntentLayer=funct\
ion(){return a.$\
(this,\x22contentLa\
yer\x22)[0]};d._rep\
aintNow=function\
(){a._repaint(th\
is,!1)};d._creat\
eCanvas2d=functi\
on(){var b=a.$(t\
his,\x22appletdiv\x22)\
;\x0atry{b[0].remov\
eChild(this._can\
vas),this._canva\
s.frontLayer&&b[\
0].removeChild(t\
his._canvas.fron\
tLayer),this._ca\
nvas.rearLayer&&\
b[0].removeChild\
(this._canvas.re\
arLayer),this._c\
anvas.contentLay\
er&&b[0].removeC\
hild(this._canva\
s.contentLayer),\
a._jsUnsetMouse(\
this._mouseInter\
face)}catch(d){}\
var e=Math.round\
(b.width()),f=Ma\
th.round(b.heigh\
t()),c=document.\
createElement(\x22c\
anvas\x22);c.applet\
=this;this._canv\
as=c;c.style.wid\
th=\x22100%\x22;c.styl\
e.height=\x22100%\x22;\
c.width=e;c.heig\
ht=f;c.id=this._\
id+\x22_canvas2d\x22;b\
.append(c);\x0aa._$\
(c.id).css({\x22z-i\
ndex\x22:a._getZ(th\
is,\x22main\x22)});if(\
this._isLayered)\
{var g=document.\
createElement(\x22d\
iv\x22);c.contentLa\
yer=g;g.id=this.\
_id+\x22_contentLay\
er\x22;b.append(g);\
a._$(g.id).css({\
zIndex:a._getZ(t\
his,\x22image\x22),pos\
ition:\x22absolute\x22\
,left:\x220px\x22,top:\
\x220px\x22,width:(thi\
s._isSwing?e:0)+\
\x22px\x22,height:(thi\
s._isSwing?f:0)+\
\x22px\x22,overflow:\x22h\
idden\x22});this._i\
sSwing?(b=docume\
nt.createElement\
(\x22div\x22),b.id=thi\
s._id+\x22_swingdiv\
\x22,a._$(this._id+\
\x22_appletinfotabl\
ediv\x22).append(b)\
,a._$(b.id).css(\
{zIndex:a._getZ(\
this,\x22rear\x22),pos\
ition:\x22absolute\x22\
,\x0aleft:\x220px\x22,top\
:\x220px\x22,width:e+\x22\
px\x22,height:f+\x22px\
\x22,overflow:\x22hidd\
en\x22}),this._mous\
eInterface=c.con\
tentLayer,c.cont\
entLayer.applet=\
this):this._mous\
eInterface=this.\
_getLayer(\x22front\
\x22,b,e,f,!1)}else\
 this._mouseInte\
rface=c;a._jsSet\
Mouse(this._mous\
eInterface)};d._\
getLayer=functio\
n(b,d,e,f,c){var\
 g=document.crea\
teElement(\x22canva\
s\x22);this._canvas\
[b+\x22Layer\x22]=g;g.\
style.width=\x22100\
%\x22;g.style.heigh\
t=\x22100%\x22;g.id=th\
is._id+\x22_\x22+b+\x22La\
yer\x22;g.width=e;g\
.height=f;d.appe\
nd(g);g.applet=t\
his;a._$(g.id).c\
ss({background:c\
?\x22rgb(0,0,0,1)\x22:\
\x0a\x22rgb(0,0,0,0.00\
1)\x22,\x22z-index\x22:a.\
_getZ(this,b),po\
sition:\x22absolute\
\x22,left:\x220px\x22,top\
:\x220px\x22,overflow:\
\x22hidden\x22});retur\
n g};d._setupJS=\
function(){windo\
w[\x22j2s.lib\x22]={ba\
se:this._j2sPath\
+\x22/\x22,alias:\x22.\x22,c\
onsole:this._con\
sole,monitorZInd\
ex:a._getZ(this,\
\x22monitorZIndex\x22)\
};0==c.length&&a\
._addExec([this,\
l,null,\x22loadClaz\
z\x22]);this._addCo\
reFiles();a._add\
Exec([this,this.\
__startAppletJS,\
null,\x22start appl\
et\x22]);this._isSi\
gned=!0;this._re\
ady=!1;this._app\
let=null;this._c\
anScript=functio\
n(){return!0};th\
is._savedOrienta\
tions=\x0a[];b&&cle\
arTimeout(b);b=s\
etTimeout(m,100)\
};d.__startApple\
tJS=function(b){\
0==a._version.in\
dexOf(\x22$Date: \x22)\
&&(a._version=(a\
._version.substr\
ing(7)+\x22 -\x22).spl\
it(\x22 -\x22)[0]+\x22 (J\
Smol/j2s)\x22);var \
d=Clazz._4Name(\x22\
java.util.Hashta\
ble\x22).newInstanc\
e();a._setApplet\
Params(b._availa\
bleParams,d,b.__\
Info,!0);d.put(\x22\
appletReadyCallb\
ack\x22,\x22Jmol._read\
yCallback\x22);d.pu\
t(\x22applet\x22,!0);d\
.put(\x22name\x22,b._i\
d);d.put(\x22syncId\
\x22,a._syncId);a._\
isAsync&&d.put(\x22\
async\x22,!0);b._co\
lor&&d.put(\x22bgco\
lor\x22,b._color);b\
._startupScript&\
&d.put(\x22script\x22,\
\x0ab._startupScrip\
t);a._syncedAppl\
ets.length&&d.pu\
t(\x22synccallback\x22\
,\x22Jmol._mySyncCa\
llback\x22);d.put(\x22\
signedApplet\x22,\x22t\
rue\x22);d.put(\x22pla\
tform\x22,b._platfo\
rm);b._is2D&&d.p\
ut(\x22display\x22,b._\
id+\x22_canvas2d\x22);\
d.put(\x22documentB\
ase\x22,document.lo\
cation.href);var\
 e=b._j2sPath+\x22/\
\x22;if(0>e.indexOf\
(\x22://\x22)){var f=d\
ocument.location\
.href.split(\x22#\x22)\
[0].split(\x22?\x22)[0\
].split(\x22/\x22);0==\
e.indexOf(\x22/\x22)?f\
=[f[0],e.substri\
ng(1)]:f[f.lengt\
h-1]=e;e=f.join(\
\x22/\x22)}d.put(\x22code\
Path\x22,e);a._regi\
sterApplet(b._id\
,b);try{b._newAp\
plet(d)}catch(c)\
{System.out.prin\
tln((a._isAsync?\
\x0a\x22normal async a\
bort from \x22:\x22\x22)+\
c);return}b._jsS\
etScreenDimensio\
ns();m()};d._res\
toreState||(d._r\
estoreState=func\
tion(){});d._jsS\
etScreenDimensio\
ns=function(){if\
(this._appletPan\
el){var b=a._get\
Element(this,thi\
s._is2D?\x22canvas2\
d\x22:\x22canvas\x22);thi\
s._appletPanel.s\
etScreenDimensio\
n(b.width,b.heig\
ht)}};d._show=fu\
nction(b){a.$set\
Visible(a.$(this\
,\x22appletdiv\x22),b)\
;b&&a._repaint(t\
his,!0)};d._canS\
cript=function()\
{return!0};d.equ\
als=function(a){\
return this==a};\
d.clone=function\
(){return this};\
d.hashCode=funct\
ion(){return par\
seInt(this._uniq\
ueId)};\x0ad._proce\
ssGesture=functi\
on(a){return thi\
s._appletPanel.p\
rocessTwoPointGe\
sture(a)};d._pro\
cessEvent=functi\
on(a,b){this._ap\
pletPanel.proces\
sMouseEvent(a,b[\
0],b[1],b[2],Sys\
tem.currentTimeM\
illis())};d._res\
ize=function(){v\
ar b=\x22__resizeTi\
meout_\x22+this._id\
;a[b]&&clearTime\
out(a[b]);var d=\
this;a[b]=setTim\
eout(function(){\
a._repaint(d,!0)\
;a[b]=null},100)\
};return d};a._r\
epaint=function(\
b,d){if(b&&b._ap\
pletPanel){var e\
=a.$(b,\x22appletdi\
v\x22),c=Math.round\
(e.width()),e=Ma\
th.round(e.heigh\
t());if(b._is2D&\
&(b._canvas.widt\
h!=\x0ac||b._canvas\
.height!=e))b._n\
ewCanvas(!0),b._\
appletPanel.setD\
isplay(b._canvas\
);b._appletPanel\
.setScreenDimens\
ion(c,e);c=funct\
ion(){b._appletP\
anel.paint?b._ap\
pletPanel.paint(\
null):b._appletP\
anel.update(null\
)};d?requestAnim\
ationFrame(c):c(\
)}};a._loadImage\
=function(b,d,e,\
c,g,k){var j=\x22ec\
ho_\x22+d+e+(c?\x22_\x22+\
c.length:\x22\x22),m=a\
._getHiddenCanva\
s(b.vwr.html5App\
let,j,0,0,!1,!0)\
;if(null==m){if(\
null==k){k=new I\
mage;if(null==c)\
return k.onload=\
function(){a._lo\
adImage(b,d,e,nu\
ll,g,k)},k.src=e\
,null;System.out\
.println(\x22Jsmol.\
js Jmol._loadIma\
ge using data UR\
I for \x22+\x0aj);k.sr\
c=\x22string\x22==type\
of c?c:\x22data:\x22+J\
U.Rdr.guessMimeT\
ypeForBytes(c)+\x22\
;base64,\x22+JU.Bas\
e64.getBase64(c)\
}var l=k.width,t\
=k.height;\x22webgl\
\x22==d&&(l/=2,t/=2\
);m=a._getHidden\
Canvas(b.vwr.htm\
l5Applet,j,l,t,!\
0,!1);m.imageWid\
th=l;m.imageHeig\
ht=t;m.id=j;m.im\
age=k;a._setCanv\
asImage(m,l,t)}e\
lse System.out.p\
rintln(\x22Jsmol.js\
 Jmol._loadImage\
 reading cached \
image for \x22+j);r\
eturn null==c?g(\
m,e):m};a._canva\
sCache={};a._get\
HiddenCanvas=fun\
ction(b,d,e,c,g,\
k){d=b._id+\x22_\x22+d\
;b=a._canvasCach\
e[d];if(k)return\
 b;if(g||!b||b.w\
idth!=\x0ae||b.heig\
ht!=c)b=document\
.createElement(\x22\
canvas\x22),b.width\
=b.style.width=e\
,b.height=b.styl\
e.height=c,b.id=\
d,a._canvasCache\
[d]=b;return b};\
a._setCanvasImag\
e=function(a,b,d\
){a.buf32=null;a\
.width=b;a.heigh\
t=d;a.getContext\
(\x222d\x22).drawImage\
(a.image,0,0,a.i\
mage.width,a.ima\
ge.height,0,0,b,\
d)};a._apply=fun\
ction(a,b){retur\
n a(b)}})(Jmol);\
\x0a(function(a,j){\
a._Applet=functi\
on(b,d,c){window\
[b]=this;this._j\
molType=\x22Jmol._A\
pplet\x22+(d.isSign\
ed?\x22 (signed)\x22:\x22\
\x22);this._viewTyp\
e=\x22Jmol\x22;this._i\
sJava=!0;this._s\
yncKeyword=\x22Sele\
ct:\x22;this._avail\
ableParams=\x22;pro\
gressbar;progres\
scolor;boxbgcolo\
r;boxfgcolor;all\
owjavascript;box\
message;\x5ct\x5ct\x5ct\x5ct\
\x5ct\x5ct\x5ct\x5ct\x5ct;messa\
gecallback;pickc\
allback;animfram\
ecallback;applet\
readycallback;at\
ommovedcallback;\
\x5ct\x5ct\x5ct\x5ct\x5ct\x5ct\x5ct\x5ct\
\x5ct;echocallback;\
evalcallback;hov\
ercallback;langu\
age;loadstructca\
llback;measureca\
llback;\x5ct\x5ct\x5ct\x5ct\x5c\
t\x5ct\x5ct\x5ct\x5ct;minimi\
zationcallback;r\
esizecallback;sc\
riptcallback;sta\
tusform;statuste\
xt;statustextare\
a;\x5ct\x5ct\x5ct\x5ct\x5ct\x5ct\x5ct\
\x5ct\x5ct;synccallbac\
k;usecommandthre\
ad;syncid;applet\
id;startupscript\
;menufile;\x22;\x0aif(\
c)return this;th\
is._isSigned=d.i\
sSigned;this._re\
adyFunction=d.re\
adyFunction;this\
._ready=!1;this.\
_isJava=!0;this.\
_isInfoVisible=!\
1;this._applet=n\
ull;this._memory\
Limit=d.memoryLi\
mit||512;this._c\
anScript=functio\
n(){return!0};th\
is._savedOrienta\
tions=[];this._i\
nitialize=functi\
on(b,c){var e=!1\
;a._jarFile&&(c=\
a._jarFile);if(t\
his._jarFile){va\
r f=this._jarFil\
e;0<=f.indexOf(\x22\
/\x22)?(alert(\x22This\
 web page URL is\
 requesting that\
 the applet used\
 be \x22+f+\x22. This \
is a possible se\
curity risk, par\
ticularly if the\
 applet is signe\
d, because signe\
d applets can re\
ad and write fil\
es on your local\
 machine or netw\
ork.\x22),\x0a\x22yes\x22==p\
rompt(\x22Do you wa\
nt to use applet\
 \x22+f+\x22? \x22,\x22yes o\
r no\x22)?(b=f.subs\
tring(0,f.lastIn\
dexOf(\x22/\x22)),c=f.\
substring(f.last\
IndexOf(\x22/\x22)+1))\
:e=!0):c=f;this_\
isSigned=d.isSig\
ned=0<=c.indexOf\
(\x22Signed\x22)}this.\
_jarPath=d.jarPa\
th=b||\x22.\x22;this._\
jarFile=d.jarFil\
e=\x22string\x22==type\
of c?c:(c?\x22JmolA\
ppletSigned\x22:\x22Jm\
olApplet\x22)+\x220.ja\
r\x22;e&&alert(\x22The\
 web page URL wa\
s ignored. Conti\
nuing using \x22+th\
is._jarFile+' in\
 directory \x22'+th\
is._jarPath+'\x22')\
;void 0==a.contr\
ols||a.controls.\
_onloadResetForm\
s()};this._creat\
e(b,d);return th\
is};\x0avar g=a._Ap\
plet,c=a._Applet\
.prototype;g._ge\
t=function(b,d,c\
){c||(c=!1);d||(\
d={});a._addDefa\
ultInfo(d,{color\
:\x22#FFFFFF\x22,width\
:300,height:300,\
addSelectionOpti\
ons:!1,serverURL\
:\x22http://your.se\
rver.here/jsmol.\
php\x22,defaultMode\
l:\x22\x22,script:null\
,src:null,readyF\
unction:null,use\
:\x22HTML5\x22,jarPath\
:\x22java\x22,jarFile:\
\x22JmolApplet0.jar\
\x22,isSigned:!1,j2\
sPath:\x22j2s\x22,cove\
rImage:null,make\
LiveImage:null,c\
overTitle:\x22\x22,cov\
erCommand:\x22\x22,def\
erApplet:!1,defe\
rUncover:!1,disa\
bleJ2SLoadMonito\
r:!1,disableInit\
ialConsole:!0,de\
bug:!1});a._debu\
gAlert=\x0ad.debug;\
d.serverURL&&(a.\
_serverUrl=d.ser\
verURL);for(var \
j=!1,l=null,e=d.\
use.toUpperCase(\
).split(\x22#\x22)[0].\
split(\x22 \x22),f=0;f\
<e.length;f++){s\
witch(e[f]){case\
 \x22JAVA\x22:j=!0;a.f\
eatureDetection.\
supportsJava()&&\
(l=new g(b,d,c))\
;break;case \x22WEB\
GL\x22:l=g._getCanv\
as(b,d,c,!0);bre\
ak;case \x22HTML5\x22:\
a.featureDetecti\
on.allowHTML5?l=\
g._getCanvas(b,d\
,c,!1):e.push(\x22J\
AVA\x22)}if(null!=l\
)break}null==l&&\
(c||!j?l={_jmolT\
ype:\x22none\x22}:j&&(\
l=new g(b,d)));r\
eturn c?l:a._reg\
isterApplet(b,l)\
};g._getCanvas=f\
unction(b,d,c,j)\
{d._isLayered=\x0a!\
1;d._platform=\x22J\
.awtjs2d.Platfor\
m\x22;return j&&a.f\
eatureDetection.\
supportsWebGL()?\
(a._Canvas3D.pro\
totype=a.GLmol.e\
xtendApplet(a._j\
sSetPrototype(ne\
w g(b,d,!0))),ne\
w a._Canvas3D(b,\
d,\x22Jmol\x22,c)):!j?\
(a._Canvas2D.pro\
totype=a._jsSetP\
rototype(new g(b\
,d,!0)),new a._C\
anvas2D(b,d,\x22Jmo\
l\x22,c)):null};g._\
noJavaMsg=\x22Eithe\
r you do not hav\
e Java applets e\
nabled in your w\
eb<br />browser \
or your browser \
is blocking this\
 applet.<br />\x5ct\
\x5ct\x5ctCheck the wa\
rning message fr\
om your browser \
and/or enable Ja\
va applets in<br\
 />\x5ct\x5ct\x5ctyour we\
b browser prefer\
ences, or instal\
l the Java Runti\
me Environment f\
rom <a href='htt\
p://www.java.com\
'>www.java.com</\
a>\x22;\x0ag._setCommo\
nMethods=functio\
n(a){a._showInfo\
=c._showInfo;a._\
search=c._search\
;a._getName=c._g\
etName;a._readyC\
allback=c._ready\
Callback};g._cre\
ateApplet=functi\
on(b,d,c){b._ini\
tialize(d.jarPat\
h,d.jarFile);var\
 m=b._jarFile;a.\
_isFile&&(m=m.re\
place(/0\x5c.jar/,\x22\
.jar\x22));var l=0<\
=b._containerWid\
th.indexOf(\x22px\x22)\
?b._containerWid\
th:\x22100%\x22,e=0<=b\
._containerHeigh\
t.indexOf(\x22px\x22)?\
b._containerHeig\
ht:\x22100%\x22,l=' st\
yle=\x22width:'+l+\x22\
;height:\x22+e+'\x22 '\
,e=\x22name='\x22+b._i\
d+\x22_object' id='\
\x22+b._id+\x22_object\
' \x5cn\x22+l+\x22\x5cn\x22;c.c\
odebase=b._jarPa\
th;\x0ac.codePath=c\
.codebase+\x22/\x22;if\
(0>c.codePath.in\
dexOf(\x22://\x22)){va\
r f=j.location.h\
ref.split(\x22#\x22)[0\
].split(\x22?\x22)[0].\
split(\x22/\x22);f[f.l\
ength-1]=c.codeP\
ath;c.codePath=f\
.join(\x22/\x22)}c.arc\
hive=m;c.mayscri\
pt=\x22true\x22;c.java\
_arguments=\x22-Xmx\
\x22+Math.round(d.m\
emoryLimit||b._m\
emoryLimit)+\x22m\x22;\
c.permissions=b.\
_isSigned?\x22all-p\
ermissions\x22:\x22san\
dbox\x22;c.document\
Location=j.locat\
ion.href;c.docum\
entBase=j.locati\
on.href.split(\x22#\
\x22)[0].split(\x22?\x22)\
[0];c.jarPath=d.\
jarPath;a._synce\
dApplets.length&\
&(c.synccallback\
=\x22Jmol._mySyncCa\
llback\x22);\x0ab._sta\
rtupScript&&(c.s\
cript=b._startup\
Script);var f=\x22\x5c\
n\x22,h;for(h in c)\
c[h]&&(f+=\x22  <pa\
ram name='\x22+h+\x22'\
 value='\x22+c[h]+\x22\
' />\x5cn\x22);f=a.fea\
tureDetection.us\
eIEObject||a.fea\
tureDetection.us\
eHtml4Object?\x22<o\
bject \x22+e+(a.fea\
tureDetection.us\
eIEObject?\x22 clas\
sid='clsid:8AD9C\
840-044E-11D1-B3\
E9-00805F499D93'\
 codebase='http:\
//java.sun.com/u\
pdate/1.6.0/jins\
tall-6u22-window\
s-i586.cab'>\x22:\x22 \
type='applicatio\
n/x-java-applet'\
>\x22)+f+\x22<p style=\
'background-colo\
r:yellow;\x22+l.spl\
it('\x22')[1]+\x22;tex\
t-align:center;v\
ertical-align:mi\
ddle;'>\x5cn\x22+\x0ag._n\
oJavaMsg+\x22</p></\
object>\x5cn\x22:\x22<app\
let \x22+e+\x22 code='\
\x22+c.code+\x22' code\
base='\x22+b._jarPa\
th+\x22' archive='\x22\
+m+\x22' mayscript=\
'true'>\x5cn\x22+f+\x22<t\
able bgcolor='ye\
llow'><tr><td al\
ign='center' val\
ign='middle' \x22+l\
+\x22>\x5cn\x22+g._noJava\
Msg+\x22</td></tr><\
/table></applet>\
\x5cn\x22;b._deferAppl\
et&&(b._javaCode\
=f,f=\x22\x22);f=a._ge\
tWrapper(b,!0)+f\
+a._getWrapper(b\
,!1)+(d.addSelec\
tionOptions?a._g\
etGrabberOptions\
(b):\x22\x22);a._debug\
Alert&&alert(f);\
b._code=a._docum\
entWrite(f)};c._\
newApplet=functi\
on(a){this._is2D\
||a.put(\x22script\x22\
,(a.get(\x22script\x22\
)||\x0a\x22\x22)+\x22;set mu\
ltipleBondSpacin\
g 0.35;\x22);this._\
viewerOptions=a;\
return new J.app\
letjs.Jmol(a)};c\
._addCoreFiles=f\
unction(){a._add\
CoreFile(\x22jmol\x22,\
this._j2sPath,th\
is.__Info.preloa\
dCore);this._is2\
D||a._addExec([t\
his,null,\x22J.expo\
rt.JSExporter\x22,\x22\
load JSExporter\x22\
]);a._debugCode&\
&a._addExec([thi\
s,null,\x22J.applet\
js.Jmol\x22,\x22load J\
mol\x22])};c._creat\
e=function(b,d){\
a._setObject(thi\
s,b,d);var c={sy\
ncId:a._syncId,p\
rogressbar:\x22true\
\x22,progresscolor:\
\x22blue\x22,boxbgcolo\
r:this._color||\x22\
black\x22,boxfgcolo\
r:\x22white\x22,boxmes\
sage:\x22Downloadin\
g JmolApplet ...\
\x22,\x0ascript:this._\
color?'backgroun\
d \x22'+this._color\
+'\x22':\x22\x22,code:\x22Jm\
olApplet.class\x22}\
;a._setAppletPar\
ams(this._availa\
bleParams,c,d);v\
ar j;d.inlineMod\
el?(j=d.inlineMo\
del,j=j.replace(\
/\x5cr|\x5cn|\x5cr\x5cn/g,0<\
=j.indexOf(\x22|\x22)?\
\x22\x5c\x5c/n\x22:\x22|\x22).repl\
ace(/'/g,\x22&#39;\x22\
),a._debugAlert&\
&alert(\x22inline m\
odel:\x5cn\x22+j)):j=\x22\
\x22;c.loadInline=j\
;c.appletReadyCa\
llback=\x22Jmol._re\
adyCallback\x22;a._\
syncedApplets.le\
ngth&&(c.synccal\
lback=\x22Jmol._myS\
yncCallback\x22);c.\
java_arguments=\x22\
-Xmx\x22+Math.round\
(d.memoryLimit||\
this._memoryLimi\
t)+\x22m\x22;this._ini\
tialize(d.jarPat\
h,\x0ad.jarFile);g.\
_createApplet(th\
is,d,c)};c._rest\
oreState=functio\
n(b,d){System.ou\
t.println(\x22\x5cn\x5cna\
synchronous rest\
ore state for \x22+\
b+\x22 \x22+d);var c=t\
his,g=c._applet&\
&c._applet.viewe\
r;switch(d){case\
 \x22setOptions\x22:re\
turn function(){\
c.__startAppletJ\
S(c)};case \x22rend\
er\x22:return funct\
ion(){setTimeout\
(function(){g.re\
fresh(2)},10)};d\
efault:switch(b)\
{case \x22J.shape.B\
alls\x22:case \x22J.sh\
ape.Sticks\x22:case\
 \x22J.shape.Frank\x22\
:return null}if(\
g&&g.isScriptExe\
cuting&&g.isScri\
ptExecuting()){i\
f(a._asyncCallba\
cks[b])return Sy\
stem.out.println\
(\x22...ignored\x22),\x0a\
1;var j=g.getEva\
lContextAndHoldQ\
ueue(g.eval),e=j\
.pc-1;j.asyncID=\
b;a._asyncCallba\
cks[b]=function(\
a){j.pc=a;System\
.out.println(\x22sc\
.asyncID=\x22+j.asy\
ncID+\x22 sc.pc = \x22\
+j.pc);g.eval.re\
sumeEval(j)};g.e\
val.pc=g.eval.pc\
End;System.out.p\
rintln(\x22setting \
resume for pc=\x22+\
j.pc+\x22 \x22+b+\x22 to \
\x22+a._asyncCallba\
cks[b]+\x22//\x22);ret\
urn function(){S\
ystem.out.printl\
n(\x22resuming \x22+b+\
\x22 \x22+a._asyncCall\
backs[b]);a._asy\
ncCallbacks[b](e\
)}}System.out.pr\
intln(b+\x22???????\
??????????????\x22+\
d);return functi\
on(){setTimeout(\
function(){g.ref\
resh(2)},\x0a10)}}}\
;c._readyCallbac\
k=function(b,d,c\
){if(c){a._setDe\
stroy(this);this\
._ready=!0;b=thi\
s._readyScript;t\
his._defaultMode\
l?a._search(this\
,this._defaultMo\
del,b?\x22;\x22+b:\x22\x22):\
b?this._script(b\
):this._src&&thi\
s._script('load \
\x22'+this._src+'\x22'\
);this._showInfo\
(!0);this._showI\
nfo(!1);a.Cache.\
setDragDrop(this\
);this._readyFun\
ction&&this._rea\
dyFunction(this)\
;a._setReady(thi\
s);if((b=this._2\
dapplet)&&b._isE\
mbedded&&b._read\
y&&b.__Info.visi\
ble)this._show2d\
(!0),this._show2\
d(!1),this._show\
2d(!0);a._hideLo\
adingSpinner(thi\
s)}};\x0ac._showInf\
o=function(b){b&\
&this._2dapplet&\
&this._2dapplet.\
_show(!1);a.$htm\
l(a.$(this,\x22info\
headerspan\x22),thi\
s._infoHeader);t\
his._info&&a.$ht\
ml(a.$(this,\x22inf\
odiv\x22),this._inf\
o);if(!this._isI\
nfoVisible!=!b){\
this._isInfoVisi\
ble=b;if(this._i\
sJava){var d=b?2\
:\x22100%\x22;a.$setSi\
ze(a.$(this,\x22app\
letdiv\x22),d,d)}a.\
$setVisible(a.$(\
this,\x22infotabled\
iv\x22),b);a.$setVi\
sible(a.$(this,\x22\
infoheaderdiv\x22),\
b);this._show(!b\
)}};c._show2d=fu\
nction(a){this._\
2dapplet._show2d\
(a);this._2dappl\
et._isEmbedded&&\
(this._showInfo(\
!1),this._show(!\
a),\x0athis._2dappl\
et.__showContain\
er(!0,!0))};c._g\
etSpinner=functi\
on(){return this\
.__Info.appletLo\
adingImage||this\
._j2sPath+\x22/img/\
JSmol_spinner.gi\
f\x22};c._getAtomCo\
rrelation=functi\
on(a){this._load\
MolData(a,\x22atomm\
ap = compare({1.\
1} {2.1} 'MAP' '\
H'); zap 2.1\x22,!0\
);a=this._evalua\
te(\x22atommap\x22);fo\
r(var d=this._ev\
aluate(\x22{*}.coun\
t\x22),c=[],g=[],j=\
0;j<a.length;j++\
){var e=a[j];c[e\
[0]+1]=e[1]-d+1;\
g[e[1]-d+1]=e[0]\
+1}return{fromJm\
ol:c,toJmol:g}};\
c._show=function\
(b){var d=!b?2:\x22\
100%\x22;a.$setSize\
(a.$(this,\x22objec\
t\x22),d,d);\x0athis._\
isJava||a.$setVi\
sible(a.$(this,\x22\
appletdiv\x22),b)};\
c._clearConsole=\
function(){this.\
_console==this._\
id+\x22_infodiv\x22&&(\
this.info=\x22\x22);se\
lf.Clazz&&(a._se\
tConsoleDiv(this\
._console),Clazz\
.Console.clear()\
)};c._addScript=\
function(a){this\
._readyScript||(\
this.readyScript\
=\x22\x22);this._ready\
Script&&(this._r\
eadyScript+=\x22;\x22)\
;this._readyScri\
pt+=a;return!0};\
c._script=functi\
on(b){if(!this._\
ready)return thi\
s._addScript(b);\
a._setConsoleDiv\
(this._console);\
a._hideLocalFile\
Reader(this);thi\
s._applet.script\
(b)};c._syncScri\
pt=\x0afunction(a){\
this._applet.syn\
cScript(a)};c._s\
criptCheck=funct\
ion(a){return th\
is._ready&&this.\
_applet.scriptCh\
eck(a)};c._scrip\
tWait=function(a\
,d){var c=this._\
scriptWaitAsArra\
y(a),g=\x22\x22;if(!d)\
for(var j=c.leng\
th;0<=--j;)for(v\
ar e=0,f=c[j].le\
ngth;e<f;e++)g+=\
c[j][e]+\x22\x5cn\x22;ret\
urn g};c._script\
Echo=function(a)\
{a=this._scriptW\
aitAsArray(a);fo\
r(var d=\x22\x22,c=a.l\
ength;0<=--c;)fo\
r(var g=a[c].len\
gth;0<=--g;)\x22scr\
iptEcho\x22==a[c][g\
][1]&&(d+=a[c][g\
][3]+\x22\x5cn\x22);retur\
n d.replace(/ \x5c|\
 /g,\x22\x5cn\x22)};c._sc\
riptMessage=func\
tion(a){a=\x0athis.\
_scriptWaitAsArr\
ay(a);for(var d=\
\x22\x22,c=a.length;0<\
=--c;)for(var g=\
a[c].length;0<=-\
-g;)\x22scriptStatu\
s\x22==a[c][g][1]&&\
(d+=a[c][g][3]+\x22\
\x5cn\x22);return d.re\
place(/ \x5c| /g,\x22\x5c\
n\x22)};c._scriptWa\
itOutput=functio\
n(a){var d=\x22\x22;tr\
y{a&&(d+=this._a\
pplet.scriptWait\
Output(a))}catch\
(c){}return d};c\
._scriptWaitAsAr\
ray=function(b){\
var d=\x22\x22;try{if(\
this._getStatus(\
\x22scriptEcho,scri\
ptMessage,script\
Status,scriptErr\
or\x22),b&&(d+=this\
._applet.scriptW\
ait(b),d=a._eval\
JSON(d,\x22jmolStat\
us\x22),\x22object\x22==t\
ypeof d))return \
d}catch(c){}retu\
rn[[d]]};\x0ac._get\
Status=function(\
b){return a._sor\
tMessages(this._\
getPropertyAsArr\
ay(\x22jmolStatus\x22,\
b))};c._getPrope\
rtyAsArray=funct\
ion(b,d){return \
a._evalJSON(this\
._getPropertyAsJ\
SON(b,d),b)};c._\
getPropertyAsStr\
ing=function(a,d\
){void 0==d&&(d=\
\x22\x22);return this.\
_applet.getPrope\
rtyAsString(a,d)\
+\x22\x22};c._getPrope\
rtyAsJSON=functi\
on(a,d){void 0==\
d&&(d=\x22\x22);try{re\
turn this._apple\
t.getPropertyAsJ\
SON(a,d)+\x22\x22}catc\
h(c){return\x22\x22}};\
c._getPropertyAs\
JavaObject=funct\
ion(a,d){void 0=\
=d&&(d=\x22\x22);retur\
n this._applet.g\
etProperty(a,d)}\
;\x0ac._evaluate=fu\
nction(a){null!=\
a||(a=\x22\x22);return\
 this._getProper\
tyAsArray(\x22varia\
bleInfo\x22,a)};c._\
evaluateDEPRECAT\
ED=function(a){a\
=\x22\x22+this._getPro\
pertyAsJavaObjec\
t(\x22evaluate\x22,a);\
var d=a.replace(\
/\x5c-*\x5cd+/,\x22\x22);if(\
\x22\x22==d&&!isNaN(pa\
rseInt(a)))retur\
n parseInt(a);d=\
a.replace(/\x5c-*\x5cd\
*\x5c.\x5cd*/,\x22\x22);retu\
rn\x22\x22==d&&!isNaN(\
parseFloat(a))?p\
arseFloat(a):a};\
c._saveOrientati\
on=function(a){r\
eturn this._save\
dOrientations[a]\
=this._getProper\
tyAsArray(\x22orien\
tationInfo\x22,\x22inf\
o\x22).moveTo};c._r\
estoreOrientatio\
n=function(a){a=\
this._savedOrien\
tations[a];\x0aretu\
rn!a||\x22\x22==a?a.re\
place(/1\x5c.0/,\x220\x22\
):this._scriptWa\
it(a)};c._restor\
eOrientationDela\
yed=function(a,d\
){1>arguments.le\
ngth&&(d=1);var \
c=this._savedOri\
entations[a];ret\
urn!c||\x22\x22==c?c.r\
eplace(/1\x5c.0/,d)\
:this._scriptWai\
t(c)};c._resizeA\
pplet=function(b\
){function d(b,d\
){var c=\x22\x22+b;ret\
urn 0==c.length?\
d?\x22\x22:a._allowedJ\
molSize[2]:c.ind\
exOf(\x22%\x22)==c.len\
gth-1?c:1>=(b=pa\
rseFloat(b))&&0<\
b?100*b+\x22%\x22:(isN\
aN(b=Math.floor(\
b))?a._allowedJm\
olSize[2]:b<a._a\
llowedJmolSize[0\
]?a._allowedJmol\
Size[0]:b>a._all\
owedJmolSize[1]?\
a._allowedJmolSi\
ze[1]:\x0ab)+(d?d:\x22\
\x22)}var c;\x22object\
\x22==typeof b&&nul\
l!=b?(c=b[0]||b.\
width,b=b[1]||b.\
height):c=b;c=[d\
(c,\x22px\x22),d(b,\x22px\
\x22)];b=a._getElem\
ent(this,\x22applet\
infotablediv\x22);b\
.style.width=c[0\
];b.style.height\
=c[1];this._cont\
ainerWidth=c[0];\
this._containerH\
eight=c[1];this.\
_is2D&&a._repain\
t(this,!0)};c._s\
earch=function(b\
,d){a._search(th\
is,b,d)};c._sear\
chDatabase=funct\
ion(b,d,c){if(th\
is._2dapplet&&th\
is._2dapplet._is\
Embedded&&!a.$(t\
his,\x22appletdiv:v\
isible\x22)[0])retu\
rn this._2dapple\
t._searchDatabas\
e(b,d,c);this._s\
howInfo(!1);\x0a0<=\
b.indexOf(\x22?\x22)?a\
._getInfoFromDat\
abase(this,d,b.s\
plit(\x22?\x22)[0]):(c\
||(c=a._getScrip\
tForDatabase(d))\
,b=d+b,this._cur\
rentView=null,th\
is._searchQuery=\
b,this._loadFile\
(b,c,b))};c._loa\
dFile=function(b\
,d,c){this._show\
Info(!1);d||(d=\x22\
\x22);this._thisJmo\
lModel=\x22\x22+Math.r\
andom();this._fi\
leName=b;if(!thi\
s._scriptLoad(b,\
d)){var g=this;a\
._loadFileData(t\
his,b,function(a\
){g.__loadModel(\
a,d,c)},function\
(){g.__loadModel\
(null)})}};c._sc\
riptLoad=functio\
n(a,d){d||(d=\x22\x22)\
;var c=this._isJ\
ava||!this._nosc\
ript;c&&this._sc\
ript(\x22zap;set ec\
ho middle center\
;echo Retrieving\
 data...\x22);\x0aif(!\
this._isSigned||\
null!=this._view\
Set)return!1;c?t\
his._script('loa\
d async \x22'+a+'\x22;\
'+d):this._apple\
t.openFile(a);th\
is._checkDeferre\
d(\x22\x22);return!0};\
c.__loadModel=fu\
nction(b,d,c){nu\
ll!=b&&(null!=th\
is._viewSet&&(d|\
|(d=\x22\x22),d+=\x22;if \
({*}.molecule.ma\
x > 1 || {*}.mod\
elindex.max > 0)\
{ delete molecul\
e > 1 or modelin\
dex > 0;x = getP\
roperty('extract\
Model',{*});load\
 inline @x};\x22),!\
d&&this._noscrip\
t?this._applet.l\
oadInlineString(\
b,\x22\x22,!1):this._l\
oadMolData(b,d,!\
1),null!=this._v\
iewSet&&a.View.u\
pdateView(this,{\
chemID:c,\x0adata:b\
}))};c._loadMolD\
ata=function(a,d\
,c){d||(d=\x22\x22);c=\
c?\x22append\x22:\x22mode\
l\x22;this._applet.\
scriptWait('load\
 DATA \x22'+c+'\x22'+a\
+'\x5cnEND \x22'+c+'\x22 \
;'+d)};c._loadMo\
delFromView=func\
tion(b){this._cu\
rrentView=b;var \
d=b.Jmol;null!=d\
.data?this.__loa\
dModel(d.data,nu\
ll,b.info.chemID\
):null!=b.info.c\
hemID?a._searchM\
ol(this,b.info.c\
hemID,null,!1):(\
d=b.JME)&&d.appl\
et._show2d(!1,th\
is)};c._updateVi\
ew=function(){nu\
ll!=this._viewSe\
t&&this._applet&\
&(chemID=\x22\x22+this\
._getPropertyAsJ\
avaObject(\x22varia\
bleInfo\x22,\x22script\
('show chemical \
inchiKey')\x22),\x0ach\
emID=36>chemID.l\
ength()?null:che\
mID.substring(36\
).split(\x22\x5cn\x22)[0]\
,a.View.updateVi\
ew(this,{chemID:\
chemID,data:\x22\x22+t\
his._getProperty\
AsJavaObject(\x22ev\
aluate\x22,\x22extract\
Model\x22,\x22{visible\
}\x22)}))};c._atomP\
ickedCallback=fu\
nction(b,d){if(!\
(0>d)){var c=[d+\
1];a.View.update\
AtomPick(this,c)\
;this._updateAto\
mPick(c)}};c._up\
dateAtomPick=fun\
ction(a){this._s\
cript(0==a.lengt\
h?\x22select none\x22:\
\x22select on visib\
le and (@\x22+a.joi\
n(\x22,@\x22)+\x22)\x22)};c.\
_isDeferred=func\
tion(){return!th\
is._canvas&&this\
._cover&&this._i\
sCovered&&this._\
deferApplet};\x0ac.\
_checkDeferred=f\
unction(a){retur\
n this._isDeferr\
ed()?(this._cove\
rScript=a,this._\
cover(!1),!0):!1\
};c._cover=funct\
ion(b){b||!this.\
_deferApplet?thi\
s._displayCoverI\
mage(b):(b=this.\
_coverScript?thi\
s._coverScript:\x22\
\x22,this._coverScr\
ipt=\x22\x22,this._def\
erUncover&&(b+=\x22\
;refresh;javascr\
ipt \x22+this._id+\x22\
._displayCoverIm\
age(false)\x22),thi\
s._script(b,!0),\
this._deferUncov\
er&&\x22activate 3D\
 model\x22==this._c\
overTitle&&(a._g\
etElement(this,\x22\
coverimage\x22).tit\
le=\x223D model is \
loading...\x22),thi\
s._isJava||this.\
_newCanvas(!1),t\
his._defaultMode\
l&&\x0aa._search(th\
is,this._default\
Model),this._sho\
wInfo(!1),this._\
deferUncover||th\
is._displayCover\
Image(!1),this._\
isJava&&a.$html(\
a.$(this,\x22applet\
div\x22),this._java\
Code),this._init\
&&this._init())}\
;c._displayCover\
Image=function(b\
){this._coverIma\
ge&&this._isCove\
red!=b&&(this._i\
sCovered=b,a._ge\
tElement(this,\x22c\
overdiv\x22).style.\
display=b?\x22block\
\x22:\x22none\x22)};c._ge\
tSmiles=function\
(){return this._\
evaluate(\x22{visib\
le}.find('SMILES\
')\x22)};c._getMol=\
function(){retur\
n this._evaluate\
(\x22getProperty('E\
xtractModel',{vi\
sible})\x22)};\x0ac._g\
etMol2D=function\
(){return this._\
evaluate(\x22script\
('select visible\
;show chemical s\
df')\x22)};a.jmolSm\
iles=function(a)\
{return a._getSm\
iles()}})(Jmol,d\
ocument);\x0a(funct\
ion(a){var j=a.c\
ontrols={_hasRes\
etForms:!1,_scri\
pts:[\x22\x22],_checkb\
oxMasters:{},_ch\
eckboxItems:{},_\
actions:{},_butt\
onCount:0,_check\
boxCount:0,_radi\
oGroupCount:0,_r\
adioCount:0,_lin\
kCount:0,_cmdCou\
nt:0,_menuCount:\
0,_previousOnloa\
dHandler:null,_c\
ontrol:null,_ele\
ment:null,_apple\
tCssClass:null,_\
appletCssText:\x22\x22\
,_buttonCssClass\
:null,_buttonCss\
Text:\x22\x22,_checkbo\
xCssClass:null,_\
checkboxCssText:\
\x22\x22,_radioCssClas\
s:null,_radioCss\
Text:\x22\x22,_linkCss\
Class:null,_link\
CssText:\x22\x22,_menu\
CssClass:null,_m\
enuCssText:\x22\x22};\x0a\
j._addScript=fun\
ction(a,c){var b\
=j._scripts.leng\
th;j._scripts[b]\
=[a,c];return b}\
;j._getIdForCont\
rol=function(a,c\
){return\x22string\x22\
==typeof a?a:!c|\
|!a._canScript||\
a._canScript(c)?\
a._id:null};j._r\
adio=function(a,\
c,b,d,k,m,l,e){v\
ar f=j._getIdFor\
Control(a,c);if(\
null==f)return n\
ull;++j._radioCo\
unt;void 0!=m&&n\
ull!=m||(m=\x22jmol\
RadioGroup\x22+(j._\
radioGroupCount-\
1));if(!c)return\
\x22\x22;void 0!=l&&nu\
ll!=l||(l=\x22jmolR\
adio\x22+(j._radioC\
ount-1));void 0!\
=b&&null!=b||(b=\
c.substring(0,32\
));k||(k=\x22\x22);a=\x22\
</span>\x22;j._acti\
ons[l]=\x0aj._addSc\
ript(f,c);c='<sp\
an id=\x22span_'+l+\
'\x22'+(e?' title=\x22\
'+e+'\x22':\x22\x22)+\x22><i\
nput name='\x22+m+\x22\
' id='\x22+l+\x22' typ\
e='radio' onclic\
k='Jmol.controls\
._click(this);re\
turn true;' onmo\
useover='Jmol.co\
ntrols._mouseOve\
r(this);return t\
rue;' onmouseout\
='Jmol.controls.\
_mouseOut()' \x22+(\
d?\x22checked='true\
' \x22:\x22\x22)+j._radio\
CssText+\x22 />\x22;0<\
=b.toLowerCase()\
.indexOf(\x22<td>\x22)\
&&(c+=a,a=\x22\x22);re\
turn c+('<label \
for=\x22'+l+'\x22>'+b+\
\x22</label>\x22+a+k)}\
;j._scriptExecut\
e=function(g,c){\
var b=a._applets\
[c[0]],d=c[1];if\
(\x22object\x22==typeo\
f d)d[0](g,d,\x0ab)\
;else\x22function\x22=\
=typeof d?d(b):a\
.script(b,d)};j.\
__checkScript=fu\
nction(a,c){var \
b=0<=c.value.ind\
exOf(\x22JSCONSOLE \
\x22)||\x22\x22===a._scri\
ptCheck(c.value)\
;c.style.color=b\
?\x22black\x22:\x22red\x22;r\
eturn b};j.__get\
Cmd=function(a,c\
){if(c._cmds&&c.\
_cmds.length){va\
r b=c._cmds[c._c\
mdpt=(c._cmdpt+c\
._cmds.length+a)\
%c._cmds.length]\
;setTimeout(func\
tion(){c.value=b\
},10);c._cmdadd=\
1;c._cmddir=a}};\
j._commandKeyPre\
ss=function(g,c,\
b){g=13==g?13:wi\
ndow.event?windo\
w.event.keyCode:\
g?g.keyCode||g.w\
hich:0;var d=doc\
ument.getElement\
ById(c),\x0ak=a._ap\
plets[b];switch(\
g){case 13:retur\
n c=d.value,j._s\
criptExecute(d,[\
b,c]),d._cmds||(\
d._cmds=[],d._cm\
ddir=0,d._cmdpt=\
-1,d._cmdadd=0),\
c&&0==d._cmdadd?\
(++d._cmdpt,d._c\
mds.splice(d._cm\
dpt,0,c),d._cmda\
dd=0,d._cmddir=0\
):d._cmdadd=0,d.\
value=\x22\x22,!1;case\
 27:return setTi\
meout(function()\
{d.value=\x22\x22},20)\
,!1;case 38:j.__\
getCmd(-1,d);bre\
ak;case 40:j.__g\
etCmd(1,d);break\
;default:d._cmda\
dd=0}setTimeout(\
function(){j.__c\
heckScript(k,d)}\
,20);return!0};j\
._click=function\
(a,c){j._element\
=a;1==arguments.\
length&&(c=j._ac\
tions[a.id]);\x0aj.\
_scriptExecute(a\
,j._scripts[c])}\
;j._menuSelected\
=function(a){var\
 c=a.value;if(vo\
id 0!=c)j._scrip\
tExecute(a,j._sc\
ripts[c]);else{c\
=a.length;if(\x22nu\
mber\x22==typeof c)\
for(var b=0;b<c;\
++b)if(a[b].sele\
cted){j._click(a\
[b],a[b].value);\
return}alert(\x22?Q\
ue? menu selecte\
d bug #8734\x22)}};\
j._cbNotifyMaste\
r=function(a){va\
r c=!0,b=!0,d=!1\
,k,m;for(m in a.\
chkGroup)k=a.chk\
Group[m],k.check\
ed?b=!1:c=!1,k.i\
ndeterminate&&(d\
=!0);k=a.chkMast\
er;c?k.checked=!\
0:b?k.checked=!1\
:d=!0;k.indeterm\
inate=d;(a=j._ch\
eckboxItems[k.id\
])&&\x0a(k=a.chkMas\
ter)&&j._cbNotif\
yMaster(j._check\
boxMasters[k.id]\
)};j._cbNotifyGr\
oup=function(a,c\
){for(var b in a\
.chkGroup){var d\
=a.chkGroup[b];d\
.checked!=c&&(d.\
checked=c,j._cbC\
lick(d));j._chec\
kboxMasters[d.id\
]&&j._cbNotifyGr\
oup(j._checkboxM\
asters[d.id],c)}\
};j._cbSetCheckb\
oxGroup=function\
(a,c,b){var d=a;\
\x22number\x22==typeof\
 d&&(d=\x22jmolChec\
kbox\x22+d);(a=docu\
ment.getElementB\
yId(d))||alert(\x22\
jmolSetCheckboxG\
roup: master che\
ckbox not found:\
 \x22+d);var k=j._c\
heckboxMasters[d\
]={};k.chkMaster\
=a;k.chkGroup={}\
;\x22string\x22==\x0atype\
of c?(c=b,d=1):d\
=0;for(a=d;a<c.l\
ength;a++)d=c[a]\
,\x22number\x22==typeo\
f d&&(d=\x22jmolChe\
ckbox\x22+d),(b=doc\
ument.getElement\
ById(d))||alert(\
\x22jmolSetCheckbox\
Group: group che\
ckbox not found:\
 \x22+d),k.chkGroup\
[d]=b,j._checkbo\
xItems[d]=k};j._\
cbClick=function\
(a){j._control=a\
;var c=j._action\
s[a.id][0],b=j._\
actions[a.id][1]\
;j._click(a,a.ch\
ecked?c:b);j._ch\
eckboxMasters[a.\
id]&&j._cbNotify\
Group(j._checkbo\
xMasters[a.id],a\
.checked);j._che\
ckboxItems[a.id]\
&&j._cbNotifyMas\
ter(j._checkboxI\
tems[a.id])};j._\
cbOver=function(\
a){var c=\x0aj._act\
ions[a.id][0],b=\
j._actions[a.id]\
[1];window.statu\
s=j._scripts[a.c\
hecked?b:c]};j._\
mouseOver=functi\
on(a,c){1==argum\
ents.length&&(c=\
j._actions[a.id]\
);window.status=\
j._scripts[c]};j\
._mouseOut=funct\
ion(){window.sta\
tus=\x22 \x22;return!0\
};j._onloadReset\
Forms=function()\
{j._hasResetForm\
s||(j._hasResetF\
orms=!0,j._previ\
ousOnloadHandler\
=window.onload,w\
indow.onload=fun\
ction(){if(0<j._\
buttonCount+j._c\
heckboxCount+j._\
menuCount+j._rad\
ioCount+j._radio\
GroupCount)for(v\
ar a=document.fo\
rms,c=a.length;0\
<=--c;)a[c].rese\
t();\x0aj._previous\
OnloadHandler&&j\
._previousOnload\
Handler()})};j._\
getButton=functi\
on(g,c,b,d,k){g=\
j._getIdForContr\
ol(g,c);if(null=\
=g)return\x22\x22;void\
 0!=d&&null!=d||\
(d=\x22jmolButton\x22+\
j._buttonCount);\
void 0!=b&&null!\
=b||(b=c.substri\
ng(0,32));++j._b\
uttonCount;j._ac\
tions[d]=j._addS\
cript(g,c);c='<s\
pan id=\x22span_'+d\
+'\x22'+(k?' title=\
\x22'+k+'\x22':\x22\x22)+\x22><\
input type='butt\
on' name='\x22+d+\x22'\
 id='\x22+d+\x22' valu\
e='\x22+b+\x22' onclic\
k='Jmol.controls\
._click(this)' o\
nmouseover='Jmol\
.controls._mouse\
Over(this);retur\
n true' onmouseo\
ut='Jmol.control\
s._mouseOut()' \x22\
+\x0aj._buttonCssTe\
xt+\x22 /></span>\x22;\
a._debugAlert&&a\
lert(c);return a\
._documentWrite(\
c)};j._getCheckb\
ox=function(g,c,\
b,d,k,m,l){var e\
=j._getIdForCont\
rol(g,c);null!=e\
&&(e=j._getIdFor\
Control(g,b));if\
(null==e)return\x22\
\x22;void 0!=m&&nul\
l!=m||(m=\x22jmolCh\
eckbox\x22+j._check\
boxCount);++j._c\
heckboxCount;if(\
void 0==c||null=\
=c||void 0==b||n\
ull==b)alert(\x22jm\
olCheckbox requi\
res two scripts\x22\
);else if(void 0\
==d||null==d)ale\
rt(\x22jmolCheckbox\
 requires a labe\
l\x22);else return \
j._actions[m]=[j\
._addScript(e,c)\
,j._addScript(e,\
b)],g=\x22</span>\x22,\
\x0ak='<span id=\x22sp\
an_'+m+'\x22'+(l?' \
title=\x22'+l+'\x22':\x22\
\x22)+\x22><input type\
='checkbox' name\
='\x22+m+\x22' id='\x22+m\
+\x22' onclick='Jmo\
l.controls._cbCl\
ick(this)' onmou\
seover='Jmol.con\
trols._cbOver(th\
is);return true'\
 onmouseout='Jmo\
l.controls._mous\
eOut()' \x22+(k?\x22ch\
ecked='true' \x22:\x22\
\x22)+j._checkboxCs\
sText+\x22 />\x22,0<=d\
.toLowerCase().i\
ndexOf(\x22<td>\x22)&&\
(k+=g,g=\x22\x22),k+='\
<label for=\x22'+m+\
'\x22>'+d+\x22</label>\
\x22+g,a._debugAler\
t&&alert(k),a._d\
ocumentWrite(k)}\
;j._getCommandIn\
put=function(g,c\
,b,d,k,m){g=j._g\
etIdForControl(g\
,\x22x\x22);if(null==g\
)return\x22\x22;\x0avoid \
0!=d&&null!=d||(\
d=\x22jmolCmd\x22+j._c\
mdCount);void 0!\
=c&&null!=c||(c=\
\x22Execute\x22);void \
0!=b&&!isNaN(b)|\
|(b=60);void 0!=\
m||(m=\x22help\x22);++\
j._cmdCount;c='<\
span id=\x22span_'+\
d+'\x22'+(k?' title\
=\x22'+k+'\x22':\x22\x22)+\x22>\
<input name='\x22+d\
+\x22' id='\x22+d+\x22' s\
ize='\x22+b+\x22' onke\
ydown='return Jm\
ol.controls._com\
mandKeyPress(eve\
nt,\x5c\x22\x22+d+'\x22,\x22'+g\
+\x22\x5c\x22)' value='\x22+\
m+\x22'/><input  ty\
pe='button' name\
='\x22+d+\x22Btn' id='\
\x22+d+\x22Btn' value \
= '\x22+c+\x22' onclic\
k='Jmol.controls\
._commandKeyPres\
s(13,\x5c\x22\x22+d+'\x22,\x22'\
+g+\x22\x5c\x22)' /></spa\
n>\x22;a._debugAler\
t&&alert(c);retu\
rn a._documentWr\
ite(c)};\x0aj._getL\
ink=function(g,c\
,b,d,k){g=j._get\
IdForControl(g,c\
);if(null==g)ret\
urn\x22\x22;void 0!=d&\
&null!=d||(d=\x22jm\
olLink\x22+j._linkC\
ount);void 0!=b&\
&null!=b||(b=c.s\
ubstring(0,32));\
++j._linkCount;c\
=j._addScript(g,\
c);b='<span id=\x22\
span_'+d+'\x22'+(k?\
' title=\x22'+k+'\x22'\
:\x22\x22)+\x22><a name='\
\x22+d+\x22' id='\x22+d+\x22\
' href='javascri\
pt:Jmol.controls\
._click(null,\x22+c\
+\x22);' onmouseove\
r='Jmol.controls\
._mouseOver(null\
,\x22+c+\x22);return t\
rue;' onmouseout\
='Jmol.controls.\
_mouseOut()' \x22+j\
._linkCssText+\x22>\
\x22+b+\x22</a></span>\
\x22;a._debugAlert&\
&alert(b);return\
 a._documentWrit\
e(b)};\x0aj._getMen\
u=function(g,c,b\
,d,k){var m=j._g\
etIdForControl(g\
,null);void 0!=d\
&&null!=d||(d=\x22j\
molMenu\x22+j._menu\
Count);++j._menu\
Count;m=typeof c\
;if(null!=m&&\x22ob\
ject\x22==m&&c.leng\
th){var l=c.leng\
th;\x22number\x22!=typ\
eof b||1==b?b=nu\
ll:0>b&&(b=l);b=\
'<span id=\x22span_\
'+d+'\x22'+(k?' tit\
le=\x22'+k+'\x22':\x22\x22)+\
\x22><select name='\
\x22+d+\x22' id='\x22+d+\x22\
' onChange='Jmol\
.controls._menuS\
elected(this)'\x22+\
(b?\x22 size='\x22+b+\x22\
' \x22:\x22\x22)+j._menuC\
ssText+\x22>\x22;for(d\
=0;d<l;++d){var \
e=c[d],m=typeof \
e,f=null,h=k=nul\
l;\x22object\x22==m&&n\
ull!=e?(f=e[0],k\
=e[1],h=e[2]):\x0af\
=k=e;m=j._getIdF\
orControl(g,f);i\
f(null==m)return\
\x22\x22;null==k&&(k=f\
);\x22#optgroup\x22==f\
?b+=\x22<optgroup l\
abel='\x22+k+\x22'>\x22:\x22\
#optgroupEnd\x22==f\
?b+=\x22</optgroup>\
\x22:(m=j._addScrip\
t(m,f),b+=\x22<opti\
on value='\x22+m+(h\
?\x22' selected='tr\
ue'>\x22:\x22'>\x22)+k+\x22<\
/option>\x22)}b+=\x22<\
/select></span>\x22\
;a._debugAlert&&\
alert(b);return \
a._documentWrite\
(b)}};j._getRadi\
o=function(g,c,b\
,d,k,m,l,e){0==j\
._radioGroupCoun\
t&&++j._radioGro\
upCount;m||(m=\x22j\
molRadioGroup\x22+(\
j._radioGroupCou\
nt-1));g=j._radi\
o(g,c,b,d,k,m,l?\
l:m+\x22_\x22+j._radio\
Count,e?e:0);if(\
null==\x0ag)return\x22\
\x22;a._debugAlert&\
&alert(g);return\
 a._documentWrit\
e(g)};j._getRadi\
oGroup=function(\
g,c,b,d,k,m){var\
 l=typeof c;if(\x22\
object\x22!=l||null\
==l||!c.length)a\
lert(\x22invalid ar\
rayOfRadioButton\
s\x22);else{void 0!\
=b&&null!=b||(b=\
\x22&#xa0; \x22);var e\
=c.length;++j._r\
adioGroupCount;d\
||(d=\x22jmolRadioG\
roup\x22+(j._radioG\
roupCount-1));fo\
r(var f=\x22<span i\
d='\x22+(k?k:d)+\x22'>\
\x22,h=0;h<e;++h){h\
==e-1&&(b=\x22\x22);va\
r r=c[h],l=typeo\
f r,L=null,f=\x22ob\
ject\x22==l?f+(L=j.\
_radio(g,r[0],r[\
1],r[2],b,d,3<r.\
length?r[3]:(k?k\
:d)+\x22_\x22+h,4<r.le\
ngth?r[4]:0,\x0am))\
:f+(L=j._radio(g\
,r,null,null,b,d\
,(k?k:d)+\x22_\x22+h,m\
));if(null==L)re\
turn\x22\x22}f+=\x22</spa\
n>\x22;a._debugAler\
t&&alert(f);retu\
rn a._documentWr\
ite(f)}}})(Jmol)\
;\x0a(function(a){v\
ar j=function(a)\
{a=\x22&\x22+a+\x22=\x22;ret\
urn decodeURI((\x22\
&\x22+document.loca\
tion.search.subs\
tring(1)+a).spli\
t(a)[1].split(\x22&\
\x22)[0])};a._j2sPa\
th=j(\x22_J2S\x22);a._\
jarFile=j(\x22_JAR\x22\
);a._use=j(\x22_USE\
\x22);a.getVersion=\
function(){retur\
n a._jmolInfo.ve\
rsion};a.getAppl\
et=function(g,c,\
b){return a._App\
let._get(g,c,b)}\
;a.getJMEApplet=\
function(g,c,b,d\
){return a._JMEA\
pplet._get(g,c,b\
,d)};a.getJSVApp\
let=function(g,c\
,b){return a._JS\
VApplet._get(g,c\
,b)};a.loadFile=\
function(a,c,b){\
a._loadFile(c,b)\
};a.script=funct\
ion(a,c){a._chec\
kDeferred(c)||\x0aa\
._script(c)};a.s\
criptCheck=funct\
ion(a,c){return \
a&&a._scriptChec\
k&&a._ready&&a._\
scriptCheck(c)};\
a.scriptWait=fun\
ction(a,c){retur\
n a._scriptWait(\
c)};a.scriptEcho\
=function(a,c){r\
eturn a._scriptE\
cho(c)};a.script\
Message=function\
(a,c){return a._\
scriptMessage(c)\
};a.scriptWaitOu\
tput=function(a,\
c){return a._scr\
iptWait(c)};a.sc\
riptWaitAsArray=\
function(a,c){re\
turn a._scriptWa\
itAsArray(c)};a.\
search=function(\
a,c,b){a._search\
(c,b)};a.evaluat\
eVar=function(a,\
c){return a._eva\
luate(c)};a.eval\
uate=function(a,\
c){return a._eva\
luateDEPRECATED(\
c)};\x0aa.getApplet\
Html=function(g,\
c){if(c){var b=a\
._document;a._do\
cument=null;g=a.\
getApplet(g,c);a\
._document=b}ret\
urn g._code};a.g\
etPropertyAsArra\
y=function(a,c,b\
){return a._getP\
ropertyAsArray(c\
,b)};a.getProper\
tyAsJavaObject=f\
unction(a,c,b){r\
eturn a._getProp\
ertyAsJavaObject\
(c,b)};a.getProp\
ertyAsJSON=funct\
ion(a,c,b){retur\
n a._getProperty\
AsJSON(c,b)};a.g\
etPropertyAsStri\
ng=function(a,c,\
b){return a._get\
PropertyAsString\
(c,b)};a.getStat\
us=function(a,c)\
{return a._getSt\
atus(c)};a.resiz\
eApplet=function\
(a,c){return a._\
resizeApplet(c)}\
;\x0aa.restoreOrien\
tation=function(\
a,c){return a._r\
estoreOrientatio\
n(c)};a.restoreO\
rientationDelaye\
d=function(a,c,b\
){return a._rest\
oreOrientationDe\
layed(c,b)};a.sa\
veOrientation=fu\
nction(a,c){retu\
rn a._saveOrient\
ation(c)};a.say=\
function(a){aler\
t(a)};a.clearCon\
sole=function(a)\
{a._clearConsole\
()};a.getInfo=fu\
nction(a){return\
 a._info};a.setI\
nfo=function(a,c\
,b){a._info=c;2<\
arguments.length\
&&a._showInfo(b)\
};a.showInfo=fun\
ction(a,c){a._sh\
owInfo(c)};a.sho\
w2d=function(a,c\
){a._show2d(c)};\
a.jmolBr=functio\
n(){return a._do\
cumentWrite(\x22<br\
 />\x22)};\x0aa.jmolBu\
tton=function(g,\
c,b,d,j){return \
a.controls._getB\
utton(g,c,b,d,j)\
};a.jmolCheckbox\
=function(g,c,b,\
d,j,m,l){return \
a.controls._getC\
heckbox(g,c,b,d,\
j,m,l)};a.jmolCo\
mmandInput=funct\
ion(g,c,b,d,j,m)\
{return a.contro\
ls._getCommandIn\
put(g,c,b,d,j,m)\
};a.jmolHtml=fun\
ction(g){return \
a._documentWrite\
(g)};a.jmolLink=\
function(g,c,b,d\
,j){return a.con\
trols._getLink(g\
,c,b,d,j)};a.jmo\
lMenu=function(g\
,c,b,d,j){return\
 a.controls._get\
Menu(g,c,b,d,j)}\
;a.jmolRadio=fun\
ction(g,c,b,d,j,\
m,l,e){return a.\
controls._getRad\
io(g,\x0ac,b,d,j,m,\
l,e)};a.jmolRadi\
oGroup=function(\
g,c,b,d,j,m){ret\
urn a.controls._\
getRadioGroup(g,\
c,b,d,j,m)};a.se\
tCheckboxGroup=f\
unction(g,c){a.c\
ontrols._cbSetCh\
eckboxGroup(g,c,\
arguments)};a.se\
tDocument=functi\
on(g){a._documen\
t=g};a.setXHTML=\
function(g){a._i\
sXHTML=!0;a._Xht\
mlElement=null;a\
._XhtmlAppendChi\
ld=!1;g&&(a._Xht\
mlElement=docume\
nt.getElementByI\
d(g),a._XhtmlApp\
endChild=!0)};a.\
setAppletCss=fun\
ction(g,c){null!\
=g&&(a._appletCs\
sClass=g);a._app\
letCssText=c?c+\x22\
 \x22:g?'class=\x22'+g\
+'\x22 ':\x22\x22};a.setB\
uttonCss=functio\
n(g,\x0ac){null!=g&\
&(a.controls._bu\
ttonCssClass=g);\
a.controls._butt\
onCssText=c?c+\x22 \
\x22:g?'class=\x22'+g+\
'\x22 ':\x22\x22};a.setCh\
eckboxCss=functi\
on(g,c){null!=g&\
&(a.controls._ch\
eckboxCssClass=g\
);a.controls._ch\
eckboxCssText=c?\
c+\x22 \x22:g?'class=\x22\
'+g+'\x22 ':\x22\x22};a.s\
etRadioCss=funct\
ion(g,c){null!=g\
&&(a.controls._r\
adioCssClass=g);\
a.controls._radi\
oCssText=c?c+\x22 \x22\
:g?'class=\x22'+g+'\
\x22 ':\x22\x22};a.setLin\
kCss=function(g,\
c){null!=g&&(a.c\
ontrols._linkCss\
Class=g);a.contr\
ols._linkCssText\
=c?c+\x22 \x22:g?'clas\
s=\x22'+g+'\x22 ':\x22\x22};\
a.setMenuCss=fun\
ction(g,c){null!\
=\x0ag&&(a.controls\
._menuCssClass=g\
);a.controls._me\
nuCssText=c?c+\x22 \
\x22:g?'class=\x22'+g+\
'\x22 ':\x22\x22};a.setAp\
pletSync=functio\
n(g,c,b){a._sync\
edApplets=g;a._s\
yncedCommands=c;\
a._syncedReady={\
};a._isJmolJSVSy\
nc=b};a.setGrabb\
erOptions=functi\
on(g){a._grabber\
Options=g};a.set\
AppletHtml=funct\
ion(g,c){g._code\
&&(a.$html(c,g._\
code),g._init&&!\
g._deferApplet&&\
g._init())};a.co\
verApplet=functi\
on(a,c){a._cover\
&&a._cover(c)};a\
.setFileCaching=\
function(g,c){g?\
g._cacheFiles=c:\
a.fileCache=c?{}\
:null};a.updateV\
iew=function(a,c\
,b){a._updateVie\
w(c,\x0ab)};a.getCh\
emicalInfo=funct\
ion(g,c,b){c||(c\
=\x22name\x22);\x22string\
\x22!=typeof g&&(g=\
g._getSmiles());\
return a._getNCI\
Info(g,c,b)};a.s\
aveImage=functio\
n(a){switch(a._v\
iewType){case \x22J\
mol\x22:a._script('\
write PNGJ \x22'+a.\
_id+'.png\x22');bre\
ak;case \x22JSV\x22:a.\
_script(\x22write P\
DF\x22);break;case \
\x22JME\x22:a._script(\
\x22print\x22)}}})(Jmo\
l);\x0aLoadClazz=fu\
nction(){c$=null\
;window[\x22j2s.cla\
zzloaded\x22]||(win\
dow[\x22j2s.clazzlo\
aded\x22]=!1);windo\
w[\x22j2s.clazzload\
ed\x22]||(window[\x22j\
2s.clazzloaded\x22]\
=!0,window[\x22j2s.\
object.native\x22]=\
!0,Clazz={_isQui\
et:!1,_debugging\
:!1},function(a,\
j){try{a._debugg\
ing=0<=document.\
location.href.in\
dexOf(\x22j2sdebug\x22\
)}catch(g){}var \
c=[\x22j2s.clazzloa\
ded\x22,\x22j2s.object\
.native\x22];a.setG\
lobal=function(a\
,b){c.push(a);wi\
ndow[a]=b};a.get\
Globals=function\
(){return c.sort\
().join(\x22\x5cn\x22)};a\
.setConsoleDiv=f\
unction(a){windo\
w[\x22j2s.lib\x22]&&(w\
indow[\x22j2s.lib\x22]\
.console=\x0aa)};va\
r b=null;a._star\
tProfiling=funct\
ion(a){b=a&&self\
.JSON?{}:null};N\
ullObject=functi\
on(){};a._suppor\
tsNativeObject=w\
indow[\x22j2s.objec\
t.native\x22];a._su\
pportsNativeObje\
ct?(a._O=functio\
n(){},a._O.__CLA\
SS_NAME__=\x22Objec\
t\x22,a._O.getClass\
=function(){retu\
rn a._O}):a._O=O\
bject;a.Console=\
{};a.dateToStrin\
g=Date.prototype\
.toString;a._has\
hCode=0;var d=a.\
_O.prototype;d.e\
quals=function(a\
){return this==a\
};d.hashCode=fun\
ction(){return t\
his._$hashcode||\
(this._$hashcode\
=++a._hashCode)}\
;d.getClass=func\
tion(){return a.\
getClass(this)};\
\x0ad.clone=functio\
n(){return a.clo\
ne(this)};a.clon\
e=function(a){va\
r b=new a.constr\
uctor,d;for(d in\
 a)b[d]=a[d];ret\
urn b};d.finaliz\
e=function(){};d\
.notify=function\
(){};d.notifyAll\
=function(){};d.\
wait=function(){\
};d.to$tring=Obj\
ect.prototype.to\
String;d.toStrin\
g=function(){ret\
urn this.__CLASS\
_NAME__?\x22[\x22+this\
.__CLASS_NAME__+\
\x22 object]\x22:this.\
to$tring.apply(t\
his,arguments)};\
a._extendedObjec\
tMethods=\x22equals\
 hashCode getCla\
ss clone finaliz\
e notify notifyA\
ll wait to$tring\
 toString\x22.split\
(\x22 \x22);a.extendJO\
=function(b,\x0ad){\
d&&(b.__CLASS_NA\
ME__=b.prototype\
.__CLASS_NAME__=\
d);if(a._support\
sNativeObject)fo\
r(var c=0;c<a._e\
xtendedObjectMet\
hods.length;c++)\
{var e=a._extend\
edObjectMethods[\
c];b.prototype[e\
]=a._O.prototype\
[e]}};a.extractC\
lassName=functio\
n(a){a=a.substri\
ng(1,a.length-1)\
;return 0<=a.ind\
exOf(\x22Array\x22)?\x22A\
rray\x22:0<=a.index\
Of(\x22object \x22)?a.\
substring(7):a};\
a.getClassName=f\
unction(b,d){if(\
null==b)return\x22N\
ullObject\x22;if(b \
instanceof a.Cas\
tedNull)return b\
.clazzName;switc\
h(typeof b){case\
 \x22number\x22:return\
\x22n\x22;case \x22boolea\
n\x22:return\x22b\x22;\x0aca\
se \x22string\x22:retu\
rn\x22String\x22;case \
\x22function\x22:if(b.\
__CLASS_NAME__)r\
eturn d?b.__CLAS\
S_NAME__:\x22Class\x22\
;var c=b.toStrin\
g(),e=c.indexOf(\
\x22function\x22);if(0\
>e)return\x22[\x22==c.\
charAt(0)?a.extr\
actClassName(c):\
c.replace(/[^a-z\
A-Z0-9]/g,\x22\x22);va\
r e=e+8,f=c.inde\
xOf(\x22(\x22,e);if(0>\
f)break;c=c.subs\
tring(e,f);if(0<\
=c.indexOf(\x22Arra\
y\x22))return\x22Array\
\x22;c=c.replace(/^\
\x5cs+/,\x22\x22).replace\
(/\x5cs+$/,\x22\x22);retu\
rn\x22anonymous\x22==c\
||\x22\x22==c?\x22Functio\
n\x22:c;case \x22objec\
t\x22:if(b.__CLASS_\
NAME__)return b.\
__CLASS_NAME__;i\
f(!b.constructor\
)break;if(!b.con\
structor.__CLASS\
_NAME__){if(b in\
stanceof\x0aNumber)\
return\x22Number\x22;i\
f(b instanceof B\
oolean)return\x22Bo\
olean\x22;if(b inst\
anceof Array||b.\
BYTES_PER_ELEMEN\
T)return\x22Array\x22;\
c=b.toString();i\
f(\x22[\x22==c.charAt(\
0))return a.extr\
actClassName(c)}\
return a.getClas\
sName(b.construc\
tor,!0)}return\x22O\
bject\x22};a.getCla\
ss=function(b){i\
f(!b)return a._O\
;if(\x22function\x22==\
typeof b)return \
b;if(b instanceo\
f a.CastedNull)b\
=b.clazzName;els\
e switch(typeof \
b){case \x22string\x22\
:return String;c\
ase \x22object\x22:if(\
!b.__CLASS_NAME_\
_)return b.const\
ructor||a._O;b=b\
.__CLASS_NAME__;\
break;default:re\
turn b.construct\
or}return a.eval\
Type(b,\x0a!0)};var\
 k=function(b,c)\
{for(var d=0;d<a\
.innerFunctionNa\
mes.length;d++)i\
f(c==a.innerFunc\
tionNames[d]&&a.\
_innerFunctions[\
c]===b[c])return\
!0;return!1},m=f\
unction(){};a.in\
heritArgs=new m;\
a.inheritClass=f\
unction(b,c,d){f\
or(var e in c)\x22b\
$\x22!=e&&(\x22prototy\
pe\x22!=e&&\x22superCl\
azz\x22!=e&&\x22__CLAS\
S_NAME__\x22!=e&&\x22i\
mplementz\x22!=e&&!\
k(c,e))&&(b[e]=c\
[e]);a.unloadedC\
lasses[a.getClas\
sName(b,!0)]||(b\
.prototype=d?d:c\
!==Number?new c(\
a.inheritArgs):n\
ew Number);b.sup\
erClazz=c;b.prot\
otype.__CLASS_NA\
ME__=b.__CLASS_N\
AME__};a.impleme\
ntOf=\x0afunction(a\
,b){if(2<=argume\
nts.length){a.im\
plementz||(a.imp\
lementz=[]);var \
c=a.implementz;i\
f(2==arguments.l\
ength)if(\x22functi\
on\x22==typeof b)c.\
push(b),l(a,b);e\
lse{if(b instanc\
eof Array)for(va\
r d=0;d<b.length\
;d++)c.push(b[d]\
),l(a,b[d])}else\
 for(d=1;d<argum\
ents.length;d++)\
c.push(arguments\
[d]),l(a,argumen\
ts[d])}};var l=f\
unction(a,b){for\
(var c in b)if(\x22\
b$\x22!=c&&\x22prototy\
pe\x22!=c&&\x22superCl\
azz\x22!=c&&\x22__CLAS\
S_NAME__\x22!=c&&\x22i\
mplementz\x22!=c&&(\
\x22function\x22!=type\
of b[c]||!k(b,c)\
))a[c]=a.prototy\
pe[c]=b[c]};a.ex\
tendInterface=\x0aa\
.implementOf;a.e\
qualsOrExtendsLe\
vel=function(b,c\
){if(b===c)retur\
n 0;if(b.impleme\
ntz)for(var d=b.\
implementz,e=0;e\
<d.length;e++){v\
ar f=a.equalsOrE\
xtendsLevel(d[e]\
,c);if(0<=f)retu\
rn f+1}return-1}\
;a.getInheritedL\
evel=function(b,\
c){if(b===c)retu\
rn 0;var d=\x22stri\
ng\x22==typeof b;if\
(d&&(\x22void\x22==b||\
\x22unknown\x22==b))re\
turn-1;var e=\x22st\
ring\x22==typeof c;\
if(e&&(\x22void\x22==c\
||\x22unknown\x22==c))\
return-1;if(b===\
(d?\x22NullObject\x22:\
NullObject))swit\
ch(c){case \x22n\x22:c\
ase \x22b\x22:return-1\
;case Number:cas\
e Boolean:case N\
ullObject:break;\
default:return 0\
}d&&\x0a(b=a.evalTy\
pe(b));e&&(c=a.e\
valType(c));if(!\
c||!b)return-1;d\
=0;for(e=b;e!==c\
&&10>d;){if(e.im\
plementz)for(var\
 f=e.implementz,\
g=0;g<f.length;g\
++){var j=a.equa\
lsOrExtendsLevel\
(f[g],c);if(0<=j\
)return d+j+1}e=\
e.superClazz;if(\
!e)return c===Ob\
ject||c===a._O?d\
+1.5:-1;d++}retu\
rn d};a.instance\
Of=function(b,c)\
{return null!=b&\
&c&&(b==c||b ins\
tanceof c||0<=a.\
getInheritedLeve\
l(a.getClassName\
(b),c))};a.super\
Call=function(b,\
c,d,e){var f=nul\
l,g=-1,j=b[d];if\
(j)if(j.claxxOwn\
er)j.claxxOwner!\
==c&&(f=j);else \
if(!j.stacks&&\x0a(\
!j.lastClaxxRef|\
|!j.lastClaxxRef\
.prototype[d]||!\
j.lastClaxxRef.p\
rototype[d].stac\
ks))f=j;else{var\
 h=j.stacks;h||(\
h=j.lastClaxxRef\
.prototype[d].st\
acks);for(g=h.le\
ngth;0<=--g;)if(\
c===h[g]){f=0<g?\
h[--g].prototype\
[d]:h[0].prototy\
pe[d][\x22\x5c\x5cunknown\
\x22];break}else if\
(0<a.getInherite\
dLevel(c,h[g])){\
f=h[g].prototype\
[d];break}}if(f)\
return 0==g&&\x22co\
nstruct\x22==d&&(c=\
j.stacks)&&(!c[0\
].superClazz&&c[\
0].con$truct)&&c\
[0].con$truct.ap\
ply(b,[]),f.appl\
y(b,e||[]);\x22cons\
truct\x22!=d&&(a.al\
ert([\x22j2slib\x22,\x22n\
o class found\x22,e\
.typeString]),\x0aV\
(b,c,d,a.getPara\
msType(e).typeSt\
ring))};a.superC\
onstructor=funct\
ion(b,c,d){a.sup\
erCall(b,c,\x22cons\
truct\x22,d);c.con$\
truct&&c.con$tru\
ct.apply(b,[])};\
a.CastedNull=fun\
ction(b){this.cl\
azzName=b?b inst\
anceof String?b:\
b instanceof Fun\
ction?a.getClass\
Name(b,!0):\x22\x22+b:\
\x22Object\x22;this.to\
String=function(\
){return null};t\
his.valueOf=func\
tion(){return nu\
ll}};a.castNullA\
s=function(b){re\
turn new a.Caste\
dNull(b)};a._ini\
tializingExcepti\
on=!1;a._calling\
StackTraces=[];v\
ar e=function(){\
this.toString=fu\
nction(){return\x22\
J2S MethodExcept\
ion\x22}},\x0af;try{nu\
ll.hello()}catch\
(h){if(d=functio\
n(a,b,c){c||(c=\x22\
[^\x5c\x5cs]+\x22);var d=\
a.indexOf(b);a=a\
.substring(0,d)+\
c+a.substring(d+\
b.length);return\
 RegExp(\x22^\x22+a+\x22$\
\x22)},/Opera[\x5c/\x5cs]\
(\x5cd+\x5c.\x5cd+)/.test\
(navigator.userA\
gent)){var d=h.m\
essage.indexOf(\x22\
:\x22),r=h.message.\
indexOf(\x22:\x22,d+2)\
,L=h.message.sub\
str(d+1,r-d-20);\
f=function(a){re\
turn-1!=a.messag\
e.indexOf(L)}}el\
se if(-1!=naviga\
tor.userAgent.to\
LowerCase().inde\
xOf(\x22webkit\x22)){v\
ar N=d(h.message\
,\x22hello\x22);f=func\
tion(a){return N\
.test(a.message)\
}}else N=d(h.mes\
sage,\x22$$o$$\x22),\x0af\
=function(a){ret\
urn N.test(a.mes\
sage)}}a.excepti\
onOf=function(b,\
c){if(b.__CLASS_\
NAME__)return a.\
instanceOf(b,c);\
b.getMessage||(b\
.getMessage=func\
tion(){return\x22\x22+\
b+(b.stack?\x22\x5cn\x22+\
b.stack:\x22\x22)});b.\
printStackTrace|\
|(b.printStackTr\
ace=function(){}\
);if(c==Error){i\
f(0>(\x22\x22+b).index\
Of(\x22Error\x22))retu\
rn!1;System.out.\
println(a.getSta\
ckTrace());retur\
n!0}return c==Ex\
ception||c==Thro\
wable||c==NullPo\
interException&&\
f(b)};a.getStack\
Trace=function(a\
){a||(a=25);var \
b=\x22\x5cn\x22,c=argumen\
ts.callee,d=0>a;\
d&&(a=-a);for(va\
r e=\x0a0;e<a&&(c=c\
.caller);e++){va\
r f=c.toString?c\
.toString().subs\
tring(0,c.toStri\
ng().indexOf(\x22{\x22\
)):\x22<native meth\
od>\x22,b=b+(e+\x22 \x22+\
(c.exName?(c.cla\
xxOwner?c.claxxO\
wner.__CLASS_NAM\
E__+\x22.\x22:\x22\x22)+c.ex\
Name+f.replace(/\
function /,\x22\x22):f\
)+\x22\x5cn\x22);if(c==c.\
caller){b+=\x22<rec\
ursing>\x5cn\x22;break\
}if(d)for(var f=\
c.arguments,g=0;\
g<f.length;g++){\
var j=\x22\x22+f[g];60\
<j.length&&(j=j.\
substring(0,60)+\
\x22...\x22);b+=\x22 args\
[\x22+g+\x22]=\x22+j.repl\
ace(/\x5cs+/g,\x22 \x22)+\
\x22\x5cn\x22}}return b};\
a.makeConstructo\
r=function(b,c,d\
){a.defineMethod\
(b,\x22construct\x22,c\
,d);b.con$truct&\
&\x0a(b.con$truct.i\
ndex=b.con$truct\
.stacks.length)}\
;a.overrideConst\
ructor=function(\
b,c,d){a.overrid\
eMethod(b,\x22const\
ruct\x22,c,d);b.con\
$truct&&(b.con$t\
ruct.index=b.con\
$truct.stacks.le\
ngth)};a.defineM\
ethod=function(c\
,d,f,g){f.exName\
=d;g=T(g);var j=\
c.prototype,h=j[\
d];a._Loader._ch\
eckLoad&&R(c,d,g\
);if(!h||h.claxx\
Owner===c&&h.fun\
Params==g)return\
 f.funParams=g,f\
.claxxOwner=c,f.\
exClazz=c,j[d]=f\
;var k=null,m=h.\
stacks;m||(m=[],\
k=h,h.claxxOwner\
&&(m[0]=k.claxxO\
wner));if(!h.sta\
cks||h.claxxRefe\
rence!==c){++q;h\
=function(){var \
c;\x0aa:{var d=argu\
ments.callee.cla\
xxReference,f=ar\
guments.callee.m\
ethodName;c=argu\
ments;fx=this[f]\
;var U=a.getPara\
msType(c);if(!fx\
)try{System.out.\
println(a.getSta\
ckTrace(5))}catc\
h(va){}if(b){var\
 g=d.__CLASS_NAM\
E__+\x22 \x22+f+\x22 \x22;0>\
t.indexOf(g)&&(t\
+=g+\x22\x5cn\x22);b[g]||\
(b[g]=0);b[g]++}\
if(fx.lastParams\
==U.typeString&&\
fx.lastClaxxRef=\
==d){if(U.hasCas\
tedNull){d=[];fo\
r(f=0;f<c.length\
;f++)d[f]=c[f]in\
stanceof a.Caste\
dNull?null:c[f]}\
else d=c;c=fx.la\
stMethod?fx.last\
Method.apply(thi\
s,d):null}else{f\
x.lastParams=U.t\
ypeString;\x0afx.la\
stClaxxRef=d;g=f\
x.stacks;g||(g=d\
.prototype[f].st\
acks);for(var j=\
!1,v=g.length;0<\
=--v;)if(j||g[v]\
===d){var h=g[v]\
.prototype[f],D=\
U,j=c,k=fx,m=[],\
G=!0,l=void 0;fo\
r(l in h)if(92==\
l.charCodeAt(0))\
{var B=l.substri\
ng(1).split(\x22\x5c\x5c\x22\
);B.length==D.le\
ngth&&m.push(B);\
G=!1}else if(G&&\
\x22funParams\x22==l&&\
h.funParams){l=h\
.funParams;B=l.s\
ubstring(1).spli\
t(\x22\x5c\x5c\x22);B.length\
==D.length&&(m[0\
]=B);break}if(!(\
l=0==m.length)){\
for(var l=D,B=[]\
,n=m.length,E=0;\
E<n;E++){for(var\
 p=[],sa=!0,r=m[\
E].length,q=0;q<\
r;q++)if(p[q]=a.\
getInheritedLeve\
l(l[q],\x0am[E][q])\
,0>p[q]){sa=!1;b\
reak}sa&&(p[l.le\
ngth]=E,B.push(p\
))}if(0==B.lengt\
h)m=null;else{n=\
B[0];for(E=1;E<B\
.length;E++){p=!\
0;for(q=0;q<l.le\
ngth;q++)if(n[q]\
<B[E][q]){p=!1;b\
reak}p&&(n=B[E])\
}m=m[n[l.length]\
].join(\x22\x5c\x5c\x22)}l=!\
m}if(l)j=new e;e\
lse{h=G?h:h[\x22\x5c\x5c\x22\
+m];G=null;if(D.\
hasCastedNull){G\
=[];for(D=0;D<j.\
length;D++)G[D]=\
j[D]instanceof a\
.CastedNull?null\
:j[D]}else G=j;k\
.lastMethod=h;j=\
h.apply(this,G)}\
if(!(j instanceo\
f e)){c=j;break \
a}j=!0}\x22construc\
t\x22!=f&&V(this,d,\
f,U.typeString);\
c=void 0}}return\
 c};h.methodName\
=\x0ad;h.claxxRefer\
ence=c;h=j[d]=h;\
d=[];for(j=0;j<m\
.length;j++)d[j]\
=m[j];h.stacks=d\
}m=h.stacks;0>S(\
m,c)&&m.push(c);\
k&&(k.claxxOwner\
===c?(h[k.funPar\
ams]=k,k.claxxOw\
ner=null,k.funPa\
rams=null):k.cla\
xxOwner||(h[\x22\x5c\x5cu\
nknown\x22]=k));f.e\
xClazz=c;h[g]=f;\
return h};duplic\
atedMethods={};v\
ar R=function(b,\
c,d){var e=b.pro\
totype[c];if(e&&\
(e.claxxOwner||e\
.claxxReference)\
===b)key=b.__CLA\
SS_NAME__+\x22.\x22+c+\
d,(b=duplicatedM\
ethods[key])?(c=\
\x22Warning! Duplic\
ate method found\
 for \x22+key,Syste\
m.out.println(c)\
,a.alert(c),dupl\
icatedMethods[ke\
y]=\x0ab+1):duplica\
tedMethods[key]=\
1};a.showDuplica\
tes=function(a){\
var b=\x22\x22,c=dupli\
catedMethods,d=0\
,e;for(e in c)1<\
c[e]&&(b+=c[e]+\x22\
\x5ct\x22+e+\x22\x5cn\x22,d++);\
b=\x22Duplicates: \x22\
+d+\x22\x5cn\x5cn\x22+b;Syst\
em.out.println(b\
);a||alert(b)};v\
ar S=function(a,\
b){if(a&&b)for(v\
ar c=a.length;0<\
=--c;)if(a[c]===\
b)return c;retur\
n-1},la=function\
(a,b){var c=S(a,\
b);if(0<=c){for(\
var d=a.length-1\
;c<d;c++)a[c]=a[\
c+1];a.length--;\
return!0}},T=fun\
ction(a){return \
a?a.replace(/~([\
NABSO])/g,functi\
on(a,b){switch(b\
){case \x22N\x22:retur\
n\x22n\x22;case \x22B\x22:re\
turn\x22b\x22;case \x22S\x22\
:return\x22String\x22;\
\x0acase \x22O\x22:return\
\x22Object\x22;case \x22A\
\x22:return\x22Array\x22}\
return\x22Unknown\x22}\
).replace(/\x5cs+/g\
,\x22\x22).replace(/^|\
,/g,\x22\x5c\x5c\x22).replac\
e(/\x5c$/g,\x22org.ecl\
ipse.s\x22):\x22\x5c\x5cvoid\
\x22};a.overrideMet\
hod=function(b,c\
,d,e){d.exName=c\
;e=T(e);a._Loade\
r._checkLoad&&R(\
b,c,e);d.funPara\
ms=e;d.claxxOwne\
r=b;return b.pro\
totype[c]=d};var\
 t=\x22\x22;a.getProfi\
le=function(){va\
r a=\x22\x22;if(b){var\
 a=[],c;for(c in\
 b){var d=\x22\x22+b[c\
];a.push(\x22      \
  \x22.substring(d.\
length)+d+\x22\x5ct\x22+c\
)}a=a.sort().rev\
erse().join(\x22\x5cr\x5c\
n\x22);b={}}return \
a};a.getParamsTy\
pe=function(b){v\
ar c=b.length;\x0as\
witch(c){case 0:\
var d=[\x22void\x22];d\
.typeString=\x22\x5c\x5cv\
oid\x22;return d;ca\
se 1:switch(type\
of obj){case \x22nu\
mber\x22:return d=[\
\x22n\x22],d.typeStrin\
g=\x22\x5c\x5cn\x22,d;case \x22\
boolean\x22:return \
d=[\x22b\x22],d.typeSt\
ring=\x22\x5c\x5cb\x22,d}}d=\
[];d.hasCastedNu\
ll=!1;if(b)for(v\
ar e=0;e<c;e++)d\
[e]=a.getClassNa\
me(b[e]),b[e]ins\
tanceof a.Casted\
Null&&(d.hasCast\
edNull=!0);d.typ\
eString=\x22\x5c\x5c\x22+d.j\
oin(\x22\x5c\x5c\x22);return\
 d};var q=0;a.al\
lPackage={};a.al\
lClasses={};a.la\
stPackageName=nu\
ll;a.lastPackage\
=null;a.unloaded\
Classes=[];a.dec\
larePackage=func\
tion(b){if(a.las\
tPackageName==\x0ab\
)return a.lastPa\
ckage;if(b&&b.le\
ngth){for(var c=\
b.split(/\x5c./),d=\
a.allPackage,e=0\
;e<c.length;e++)\
d[c[e]]||(d[c[e]\
]={__PKG_NAME__:\
d.__PKG_NAME__?d\
.__PKG_NAME__+\x22.\
\x22+c[e]:c[e]},0==\
e&&a.setGlobal(c\
[e],d[c[e]])),d=\
d[c[e]];a.lastPa\
ckageName=b;retu\
rn a.lastPackage\
=d}};a.evalType=\
function(b,c){va\
r d=b.lastIndexO\
f(\x22.\x22);if(-1!=d)\
{var e=b.substri\
ng(0,d),e=a.decl\
arePackage(e),d=\
b.substring(d+1)\
;return e[d]}if(\
c)return window[\
b];switch(b){cas\
e \x22string\x22:retur\
n String;case \x22n\
umber\x22:return Nu\
mber;case \x22objec\
t\x22:return a._O;\x0a\
case \x22boolean\x22:r\
eturn Boolean;ca\
se \x22function\x22:re\
turn Function;ca\
se \x22void\x22:case \x22\
undefined\x22:case \
\x22unknown\x22:return\
 b;case \x22NullObj\
ect\x22:return Null\
Object;default:r\
eturn window[b]}\
};a.defineType=f\
unction(b,c,d,e)\
{var f=a.unloade\
dClasses[b];f&&(\
c=f);f=b.lastInd\
exOf(\x22.\x22);if(-1!\
=f){var g=b.subs\
tring(0,f),g=a.d\
eclarePackage(g)\
,f=b.substring(f\
+1);if(g[f])retu\
rn g[f];g[f]=c}e\
lse{if(window[b]\
)return window[b\
];a.setGlobal(b,\
c)}a.decorateAsT\
ype(c,b,d,e);b=a\
._innerFunctions\
;c.defineMethod=\
b.defineMethod;c\
.defineStaticMet\
hod=\x0ab.defineSta\
ticMethod;c.make\
Constructor=b.ma\
keConstructor;re\
turn c};var X=!1\
;-1!=navigator.u\
serAgent.indexOf\
(\x22Safari\x22)&&(d=n\
avigator.userAge\
nt,r=d.indexOf(\x22\
Version/\x22),-1!=r\
&&(d=d.substring\
(r+8),X=4<=parse\
Float(d)));a.ins\
tantialize=funct\
ion(a,b){if(!b||\
!(1==b.length&&b\
[0]&&b[0]instanc\
eof m)){a instan\
ceof Number&&(a.\
valueOf=function\
(){return this})\
;if(X){for(var c\
=[],d=0;d<b.leng\
th;d++)c[d]=b[d]\
;b=c}(c=a.constr\
uct)?a.con$truct\
?a.getClass().su\
perClazz?c.claxx\
Owner&&c.claxxOw\
ner===a.getClass\
()||c.stacks&&\x0ac\
.stacks[c.stacks\
.length-1]==a.ge\
tClass()?c.apply\
(a,b):(c.claxxOw\
ner&&!c.claxxOwn\
er.superClazz&&c\
.claxxOwner.con$\
truct?c.claxxOwn\
er.con$truct.app\
ly(a,[]):c.stack\
s&&(1==c.stacks.\
length&&!c.stack\
s[0].superClazz)\
&&c.stacks[0].co\
n$truct.apply(a,\
[]),c.apply(a,b)\
,a.con$truct.app\
ly(a,[])):(a.con\
$truct.apply(a,[\
]),c.apply(a,b))\
:c.apply(a,b):a.\
con$truct&&a.con\
$truct.apply(a,[\
])}};a.innerFunc\
tionNames=\x22isIns\
tance equals has\
hCode getName ge\
tCanonicalName g\
etClassLoader ge\
tResource getRes\
ourceAsStream de\
fineMethod defin\
eStaticMethod ma\
keConstructor\x22.s\
plit(\x22 \x22);\x0aa._in\
nerFunctions={is\
Instance:functio\
n(b){return a.in\
stanceOf(b,this)\
},equals:functio\
n(a){return this\
===a},hashCode:f\
unction(){return\
 this.getName().\
hashCode()},toSt\
ring:function(){\
return\x22class \x22+t\
his.getName()},g\
etName:function(\
){return a.getCl\
assName(this,!0)\
},getCanonicalNa\
me:function(){re\
turn this.__CLAS\
S_NAME__},getCla\
ssLoader:functio\
n(){var b=this._\
_CLASS_NAME__,c=\
a._Loader.getCla\
sspathFor(b),d=c\
.lastIndexOf(b.r\
eplace(/\x5c./g,\x22/\x22\
)),c=-1!=d?c.sub\
string(0,d):a._L\
oader.getClasspa\
thFor(b,!0),b=a.\
_Loader.requireL\
oaderByBase(c);\x0a\
b.getResourceAsS\
tream=a._innerFu\
nctions.getResou\
rceAsStream;b.ge\
tResource=a._inn\
erFunctions.getR\
esource;return b\
},getResource:fu\
nction(a){return\
(a=this.getResou\
rceAsStream(a))?\
a.url:null},getR\
esourceAsStream:\
function(b){if(!\
b)return null;b=\
b.replace(/\x5c\x5c/g,\
\x22/\x22);var c=null,\
d=b,d=this.__CLA\
SS_NAME__;2==arg\
uments.length&&0\
!=b.indexOf(\x22/\x22)\
&&(b=\x22/\x22+b);if(0\
==b.indexOf(\x22/\x22)\
)if(2==arguments\
.length?(c=argum\
ents[1])||(c=a.b\
inaryFolders[0])\
:a._Loader&&(c=a\
._Loader.getClas\
spathFor(d,!0)),\
c){var c=c.repla\
ce(/\x5c\x5c/g,\x0a\x22/\x22),e\
=c.length,e=c.ch\
arAt(e-1);\x22/\x22!=e\
&&(c+=\x22/\x22);d=c+b\
.substring(1)}el\
se d=b.substring\
(1);else{if(this\
.base)c=this.bas\
e;else if(a._Loa\
der)if(c=a._Load\
er.getClasspathF\
or(d),e=c.lastIn\
dexOf(d.replace(\
/\x5c./g,\x22/\x22)),-1!=\
e)c=c.substring(\
0,e);else if(e=-\
1,c.indexOf(\x22.z.\
js\x22)==c.length-5\
&&-1!=(e=c.lastI\
ndexOf(\x22/\x22)))for\
(var c=c.substri\
ng(0,e+1),e=d.sp\
lit(/\x5c./),f=1;f<\
e.length;f++){fo\
r(var g=\x22/\x22,h=0;\
h<f;h++)g+=e[h]+\
\x22/\x22;if(g.length>\
c.length)break;i\
f(c.indexOf(g)==\
c.length-g.lengt\
h){c=c.substring\
(0,c.length-g.le\
ngth+\x0a1);break}}\
else c=a._Loader\
.getClasspathFor\
(d,!0);else(e=a.\
binaryFolders)&&\
e.length&&(c=e[0\
]);c||(c=\x22j2s/\x22)\
;c=c.replace(/\x5c\x5c\
/g,\x22/\x22);e=c.leng\
th;e=c.charAt(e-\
1);\x22/\x22!=e&&(c+=\x22\
/\x22);this.base?d=\
c+b:(e=d.lastInd\
exOf(\x22.\x22),d=-1==\
e||this.base?c+b\
:c+d.substring(0\
,e).replace(/\x5c./\
g,\x22/\x22)+\x22/\x22+b)}c=\
null;try{if(0>d.\
indexOf(\x22:/\x22)){v\
ar k=document.lo\
cation.href.spli\
t(\x22?\x22)[0].split(\
\x22/\x22);k[k.length-\
1]=d;d=k.join(\x22/\
\x22)}c=new java.ne\
t.URL(d)}catch(m\
){}k=null==c?nul\
l:j._getFileData\
(d.toString());i\
f(!k||\x22error\x22==k\
||0==k.indexOf(\x22\
[Exception\x22))ret\
urn null;\x0ak=(new\
 java.lang.Strin\
g(k)).getBytes()\
;k=new java.io.B\
ufferedInputStre\
am(new java.io.B\
yteArrayInputStr\
eam(k));k.url=c;\
return k},define\
Method:function(\
b,c,d){a.defineM\
ethod(this,b,c,d\
)},defineStaticM\
ethod:function(b\
,c,d){a.defineMe\
thod(this,b,c,d)\
;this[b]=this.pr\
ototype[b]},make\
Constructor:func\
tion(b,c){a.make\
Constructor(this\
,b,c)}};var Y=[]\
;a.pu$h=function\
(a){a||(a=self.c\
$);a&&Y.push(a)}\
;a.p0p=function(\
){return Y.pop()\
};a.decorateAsCl\
ass=function(b,c\
,d,e,f,g){var j=\
null;c&&(j=c.__P\
KG_NAME__,j||(j=\
\x0ac.__CLASS_NAME_\
_));var h=(j?j+\x22\
.\x22:\x22\x22)+d;a._Load\
er._classPending\
[h]&&(delete a._\
Loader._classPen\
ding[h],a._Loade\
r._classCountOK+\
+,a._Loader._cla\
ssCountPending--\
);a._Loader&&a._\
Loader._checkLoa\
d&&System.out.pr\
intln(\x22decoratin\
g class \x22+j+\x22.\x22+\
d);(j=a.unloaded\
Classes[h])&&(b=\
j);Z(b,c,d);g?a.\
inheritClass(b,e\
,g):e&&a.inherit\
Class(b,e);f&&a.\
implementOf(b,f)\
;return b};var Z\
=function(b,c,d)\
{var e;c?c.__PKG\
_NAME__?(e=c.__P\
KG_NAME__+\x22.\x22+d,\
c[d]=b,c===java.\
lang&&a.setGloba\
l(d,b)):(e=c.__C\
LASS_NAME__+\x22.\x22+\
d,c[d]=\x0ab):(e=d,\
a.setGlobal(d,b)\
);a.extendJO(b,e\
);c=a.innerFunct\
ionNames;for(d=0\
;d<c.length;d++)\
b[c[d]]=a._inner\
Functions[c[d]];\
a._Loader&&a._Lo\
ader.updateNodeF\
orFunctionDecora\
tion(e)};a.decla\
reInterface=func\
tion(b,c,d){var \
e=function(){};Z\
(e,b,c);d&&a.imp\
lementOf(e,d);re\
turn e};a.declar\
eType=function(b\
,c,d,e,f){return\
 a.decorateAsCla\
ss(function(){a.\
instantialize(th\
is,arguments)},b\
,c,d,e,f)};a.dec\
lareAnonymous=fu\
nction(b,c,d,e,f\
){return a.decor\
ateAsClass(funct\
ion(){a.prepareC\
allback(this,arg\
uments);a.instan\
tialize(this,\x0aar\
guments)},b,c,d,\
e,f)};a.decorate\
AsType=function(\
b,c,d,e,f,g){a.e\
xtendJO(b,c);b.e\
quals=a._innerFu\
nctions.equals;b\
.getName=a._inne\
rFunctions.getNa\
me;if(g)for(c=0;\
c<a.innerFunctio\
nNames.length;c+\
+)g=a.innerFunct\
ionNames[c],b[g]\
=a._innerFunctio\
ns[g];f?a.inheri\
tClass(b,d,f):d&\
&a.inheritClass(\
b,d);e&&a.implem\
entOf(b,e);retur\
n b};Number.prot\
otype._numberToS\
tring=Number.pro\
totype.toString;\
a.declarePackage\
(\x22java.io\x22);a.de\
clarePackage(\x22ja\
va.lang.annotati\
on\x22);a.declarePa\
ckage(\x22java.lang\
.instrument\x22);a.\
declarePackage(\x22\
java.lang.manage\
ment\x22);\x0aa.declar\
ePackage(\x22java.l\
ang.reflect\x22);a.\
declarePackage(\x22\
java.lang.ref\x22);\
java.lang.ref.re\
flect=java.lang.\
reflect;a.declar\
ePackage(\x22java.u\
til\x22);a.declareP\
ackage(\x22java.sec\
urity\x22);a.declar\
eInterface(java.\
io,\x22Closeable\x22);\
a.declareInterfa\
ce(java.io,\x22Data\
Input\x22);a.declar\
eInterface(java.\
io,\x22DataOutput\x22)\
;a.declareInterf\
ace(java.io,\x22Ext\
ernalizable\x22);a.\
declareInterface\
(java.io,\x22Flusha\
ble\x22);a.declareI\
nterface(java.io\
,\x22Serializable\x22)\
;a.declareInterf\
ace(java.lang,\x22I\
terable\x22);a.decl\
areInterface(jav\
a.lang,\x22CharSequ\
ence\x22);\x0aa.declar\
eInterface(java.\
lang,\x22Cloneable\x22\
);a.declareInter\
face(java.lang,\x22\
Appendable\x22);a.d\
eclareInterface(\
java.lang,\x22Compa\
rable\x22);a.declar\
eInterface(java.\
lang,\x22Runnable\x22)\
;a.declareInterf\
ace(java.util,\x22C\
omparator\x22);java\
.lang.ClassLoade\
r={__CLASS_NAME_\
_:\x22ClassLoader\x22}\
;var V=function(\
b,c,d,e){b=\x22\x22;e&\
&(b=e.substring(\
1).replace(/\x5c\x5c/g\
,\x22,\x22));c=(d&&\x22co\
nstruct\x22!=d?\x22Met\
hod\x22:\x22Constructo\
r\x22)+\x22 \x22+a.getCla\
ssName(c,!0)+\x22.\x22\
+d+\x22(\x22+b+\x22) is n\
ot found!\x22;throw\
 new java.lang.N\
oSuchMethodExcep\
tion(c);};a.prep\
areCallback=func\
tion(b,\x0ac){var d\
=c[0];if(b&&d&&d\
!==window){var e\
=a.getClassName(\
d,!0),f={};if(b.\
b$)for(var g in \
b.b$)f[g]=b.b$[g\
];b.b$=f;f[e]=d;\
for(e=a.getClass\
(d);e.superClazz\
;)e=e.superClazz\
,f[a.getClassNam\
e(e,!0)]=d;if(d=\
d.b$)for(g in d)\
f[g]=d[g]}for(f=\
0;f<c.length-1;f\
++)c[f]=c[f+1];c\
.length--};a.inn\
erTypeInstance=f\
unction(b,c,d){b\
||(b=arguments.c\
allee.caller);va\
r e;if(d||c.$fin\
als)if(e=new b(c\
,a.inheritArgs),\
d)if(c.f$){var f\
={},g;for(g in c\
.f$)f[g]=c.f$[g]\
;for(g in d)f[g]\
=d[g];e.f$=f}els\
e e.f$=d;else c.\
f$&&(e.f$=c.f$);\
\x0aelse switch(arg\
uments.length){c\
ase 3:return new\
 b(c);case 4:ret\
urn c.__CLASS_NA\
ME__==b.__CLASS_\
NAME__&&argument\
s[3]===a.inherit\
Args?c:new b(c,a\
rguments[3]);cas\
e 5:return new b\
(c,arguments[3],\
arguments[4]);ca\
se 6:return new \
b(c,arguments[3]\
,arguments[4],ar\
guments[5]);case\
 7:return new b(\
c,arguments[3],a\
rguments[4],argu\
ments[5],argumen\
ts[6]);case 8:re\
turn new b(c,arg\
uments[3],argume\
nts[4],arguments\
[5],arguments[6]\
,arguments[7]);c\
ase 9:return new\
 b(c,arguments[3\
],arguments[4],a\
rguments[5],argu\
ments[6],\x0aargume\
nts[7],arguments\
[8]);case 10:ret\
urn new b(c,argu\
ments[3],argumen\
ts[4],arguments[\
5],arguments[6],\
arguments[7],arg\
uments[8],argume\
nts[9]);default:\
e=new b(c,a.inhe\
ritArgs)}g=argum\
ents.length-3;fo\
r(f=Array(g);0<=\
--g;)f[g]=argume\
nts[g+3];a.insta\
ntialize(e,f);re\
turn e};a.cloneF\
inals=function()\
{for(var a={},b=\
arguments.length\
/2;0<=--b;)a[arg\
uments[b+b]]=arg\
uments[b+b+1];re\
turn a};a.isClas\
sDefined=a.isDef\
inedClass=functi\
on(b){if(!b)retu\
rn!1;if(a.allCla\
sses[b])return!0\
;for(var c=b.spl\
it(/\x5c./),d=null,\
\x0ae=0;e<c.length;\
e++)if(!(d=d?d[c\
[e]]:a.allPackag\
e[c[0]]))return!\
1;return d&&(a.a\
llClasses[b]=!0)\
};a.defineEnumCo\
nstant=function(\
a,b,c,d,e){e=e?n\
ew e:new a;e.$na\
me=b;e.$ordinal=\
c;d&&d.length&&e\
.construct.apply\
(e,d);a[b]=e;a.p\
rototype[b]=e;a[\
\x22$ values\x22]||(a[\
\x22$ values\x22]=[],a\
.values=function\
(){return this[\x22\
$ values\x22]});a[\x22\
$ values\x22].push(\
e);return e};a.f\
loatToInt=functi\
on(a){return isN\
aN(a)?0:0>a?Math\
.ceil(a):Math.fl\
oor(a)};a.floatT\
oByte=a.floatToS\
hort=a.floatToLo\
ng=a.floatToInt;\
a.doubleToByte=a\
.doubleToShort=\x0a\
a.doubleToLong=a\
.doubleToInt=a.f\
loatToInt;a.floa\
tToChar=function\
(a){return Strin\
g.fromCharCode(0\
>a?Math.ceil(a):\
Math.floor(a))};\
a.doubleToChar=a\
.floatToChar;var\
 aa=function(a,b\
){a||(a=0);if(\x22o\
bject\x22==typeof a\
)var c=a;else fo\
r(var c=Array(a)\
,d=0;d<a;d++)c[d\
]=0;c.BYTES_PER_\
ELEMENT=b>>3;c._\
fake=!0;return c\
},O=function(a,b\
){a||(a=0);b||(b\
=this.length);if\
(this._fake){var\
 c=new this.cons\
tructor(b-a);Sys\
tem.arraycopy(th\
is,a,c,0,b-a);re\
turn c}return ne\
w this.construct\
or(this.buffer.s\
lice(a*this.BYTE\
S_PER_ELEMENT,\x0ab\
*this.BYTES_PER_\
ELEMENT))};!0==(\
a.haveInt32=!!(s\
elf.Int32Array&&\
self.Int32Array!\
=Array))?Int32Ar\
ray.prototype.so\
rt||(Int32Array.\
prototype.sort=A\
rray.prototype.s\
ort):(Int32Array\
=function(a){ret\
urn aa(a,32)},In\
t32Array.prototy\
pe.sort=Array.pr\
ototype.sort,Int\
32Array.prototyp\
e.toString=funct\
ion(){return\x22[ob\
ject Int32Array]\
\x22});Int32Array.p\
rototype.slice||\
(Int32Array.prot\
otype.slice=func\
tion(){return O.\
apply(this,argum\
ents)});Int32Arr\
ay.prototype.clo\
ne=function(){va\
r a=this.slice()\
;a.BYTES_PER_ELE\
MENT=\x0a4;return a\
};!0==(a.haveFlo\
at64=!!(self.Flo\
at64Array&&self.\
Float64Array!=Ar\
ray))?Float64Arr\
ay.prototype.sor\
t||(Float64Array\
.prototype.sort=\
Array.prototype.\
sort):(Float64Ar\
ray=function(a){\
return aa(a,64)}\
,Float64Array.pr\
ototype.sort=Arr\
ay.prototype.sor\
t,Float64Array.p\
rototype.toStrin\
g=function(){ret\
urn\x22[object Floa\
t64Array]\x22});Flo\
at64Array.protot\
ype.slice||(Floa\
t64Array.prototy\
pe.slice=functio\
n(){return O.app\
ly(this,argument\
s)});Float64Arra\
y.prototype.clon\
e=function(){ret\
urn this.slice()\
};a.newArray=\x0afu\
nction(a,b,c,d){\
if(-1!=a||2==arg\
uments.length)re\
turn I(arguments\
,0);a=b.slice(c,\
d);a.BYTES_PER_E\
LEMENT=b.BYTES_P\
ER_ELEMENT;retur\
n a};var I=funct\
ion(a,b){var c=a\
[0];\x22string\x22==ty\
peof c&&(c=c.cha\
rCodeAt(0));var \
d=a.length-1,e=a\
[d];if(1<d){for(\
var e=Array(d),f\
=0;f<d;f++)e[f]=\
a[f+1];d=Array(c\
);for(f=0;f<c;f+\
+)d[f]=I(e,b);re\
turn d}0<b&&0>c&\
&(c=e);switch(b)\
{case 8:return d\
=new Int8Array(c\
),d.BYTES_PER_EL\
EMENT=1,d;case 3\
2:return d=new I\
nt32Array(c),d.B\
YTES_PER_ELEMENT\
=4,d;case 64:ret\
urn d=new Float6\
4Array(c),\x0ad.BYT\
ES_PER_ELEMENT=8\
,d;default:d=0>c\
?e:Array(c);d.BY\
TES_PER_ELEMENT=\
0;if(0<c&&null!=\
e)for(f=c;0<=--f\
;)d[f]=e;return \
d}};a.newByteArr\
ay=function(){re\
turn I(arguments\
,8)};a.newIntArr\
ay=function(){re\
turn I(arguments\
,32)};a.newFloat\
Array=function()\
{return I(argume\
nts,64)};a.newDo\
ubleArray=a.newF\
loatArray;a.newL\
ongArray=a.newSh\
ortArray=a.newIn\
tArray;a.newChar\
Array=a.newBoole\
anArray=a.newArr\
ay;!0==(a.haveIn\
t8=!!self.Int8Ar\
ray)?(Int8Array.\
prototype.sort||\
(Int8Array.proto\
type.sort=Array.\
prototype.sort),\
\x0aInt8Array.proto\
type.slice||(Int\
8Array.prototype\
.slice=function(\
){return O.apply\
(this,arguments)\
})):a.newByteArr\
ay=a.newIntArray\
;Int8Array.proto\
type.clone=funct\
ion(){var a=this\
.slice();a.BYTES\
_PER_ELEMENT=1;r\
eturn a};a.isAB=\
function(a){retu\
rn a&&\x22object\x22==\
typeof a&&1==a.B\
YTES_PER_ELEMENT\
};a.isAI=functio\
n(a){return a&&\x22\
object\x22==typeof \
a&&4==a.BYTES_PE\
R_ELEMENT};a.isA\
F=function(a){re\
turn a&&\x22object\x22\
==typeof a&&8==a\
.BYTES_PER_ELEME\
NT};a.isAS=funct\
ion(a){return a&\
&\x22object\x22==typeo\
f a&&a.construct\
or==Array&&\x0a(\x22st\
ring\x22==typeof a[\
0]||\x22undefined\x22=\
=typeof a[0])};a\
.isAII=function(\
b){return b&&\x22ob\
ject\x22==typeof b&\
&a.isAI(b[0])};a\
.isAFF=function(\
b){return b&&\x22ob\
ject\x22==typeof b&\
&a.isAF(b[0])};a\
.isAFFF=function\
(b){return b&&\x22o\
bject\x22==typeof b\
&&a.isAFF(b[0])}\
;a.isASS=functio\
n(b){return b&&\x22\
object\x22==typeof \
b&&a.isAS(b[0])}\
;a.isAFloat=func\
tion(b){return b\
&&\x22object\x22==type\
of b&&b.construc\
tor==Array&&a.in\
stanceOf(b[0],Fl\
oat)};a.isAP=fun\
ction(b){return \
b&&\x22JU.P3\x22==a.ge\
tClassName(b[0])\
};a.defineStatic\
s=function(a){fo\
r(var b=\x0aargumen\
ts.length,c=(b-1\
)/2;0<=--c;){var\
 d=arguments[--b\
],e=arguments[--\
b];a[e]=a.protot\
ype[e]=d}};a.pre\
pareFields=funct\
ion(a,b){var c=[\
];if(a.con$truct\
)for(var d=a.con\
$truct.stacks,e=\
0;e<d.length;e++\
)c[e]=d[e];d=a.c\
on$truct=functio\
n(){var a=argume\
nts.callee.stack\
s;if(a)for(var b\
=0;b<a.length;b+\
+)a[b].apply(thi\
s,[])};a.prototy\
pe.con$truct=d;c\
.push(b);a.con$t\
ruct.stacks=c;a.\
con$truct.index=\
0};a.checkPrivat\
eMethod=function\
(){me=arguments.\
callee.caller;ca\
ller=arguments.c\
allee.caller.cal\
ler;var b=\x22\x5c\x5c\x22+\x0a\
a.getParamsType(\
arguments[0]).jo\
in(\x22\x5c\x5c\x22);me.priv\
ateNote||(me.pri\
vateNote=\x22You ar\
e seeing this no\
te because the m\
ethod \x22+me.exNam\
e+b+\x22 in class \x22\
+me.exClazz.__CL\
ASS_NAME__+\x22 has\
 a superclass me\
thod by the same\
 name (possibly \
with the same pa\
rameters) that i\
s private and  t\
herefore might b\
e called imprope\
rly from this cl\
ass. If your  co\
de does not run \
properly, or you\
 want to make it\
 run faster, cha\
nge the name of \
this method to s\
omething else.\x22,\
System.out.print\
ln(me.privateNot\
e),alert(me.priv\
ateNote));\x0aretur\
n null};java.lan\
g.Object=a._O;a.\
_O.getName=a._in\
nerFunctions.get\
Name;java.lang.S\
ystem=System={pr\
ops:null,$props:\
{},arraycopy:fun\
ction(a,b,c,d,e)\
{if(a!==c||b>d)f\
or(;0<=--e;)c[d+\
+]=a[b++];else{d\
+=e;for(b+=e;0<=\
--e;)a[--d]=a[--\
b]}},currentTime\
Millis:function(\
){return(new Dat\
e).getTime()},gc\
:function(){},ge\
tProperties:func\
tion(){return Sy\
stem.props},getP\
roperty:function\
(a,b){if(System.\
props)return Sys\
tem.props.getPro\
perty(a,b);var c\
=System.$props[a\
];if(\x22undefined\x22\
!=typeof c)retur\
n c;if(0<a.index\
Of(\x22.\x22)){c=\x0anull\
;switch(a){case \
\x22java.version\x22:c\
ase \x22file.separa\
tor\x22:case \x22path.\
separator\x22:c=\x22/\x22\
;break;case \x22lin\
e.separator\x22:c=0\
<=navigator.user\
Agent.indexOf(\x22W\
indows\x22)?\x22\x5cr\x5cn\x22:\
\x22\x5cn\x22;break;case \
\x22os.name\x22:case \x22\
os.version\x22:c=na\
vigator.userAgen\
t}if(c)return Sy\
stem.$props[a]=c\
}return 1==argum\
ents.length?null\
:null==b?a:b},ge\
tSecurityManager\
:function(){retu\
rn null},setProp\
erties:function(\
a){System.props=\
a},lineSeparator\
:function(){retu\
rn\x22\x5cn\x22},setPrope\
rty:function(a,b\
){if(!System.pro\
ps)return System\
.$props[a]=b;Sys\
tem.props.setPro\
perty(a,\x0ab)}};Sy\
stem.identityHas\
hCode=function(b\
){return null==b\
?0:b._$hashcode|\
|(b._$hashcode=+\
+a._hashCode)};S\
ystem.out=new a.\
_O;System.out.__\
CLASS_NAME__=\x22ja\
va.io.PrintStrea\
m\x22;System.out.pr\
int=function(){}\
;System.out.prin\
tf=function(){};\
System.out.print\
ln=function(){};\
System.out.write\
=function(){};Sy\
stem.err=new a._\
O;System.err.__C\
LASS_NAME__=\x22jav\
a.io.PrintStream\
\x22;System.err.pri\
nt=function(){};\
System.err.print\
f=function(){};S\
ystem.err.printl\
n=function(){};S\
ystem.err.write=\
function(){};a.p\
opup=a.assert=\x0aa\
.log=a.error=win\
dow.alert;Thread\
=function(){};Th\
read.J2S_THREAD=\
Thread.prototype\
.J2S_THREAD=new \
Thread;Thread.cu\
rrentThread=Thre\
ad.prototype.cur\
rentThread=funct\
ion(){return thi\
s.J2S_THREAD};a.\
innerFunctionNam\
es=a.innerFuncti\
onNames.concat(\x22\
getSuperclass is\
AssignableFrom g\
etConstructor ge\
tDeclaredMethod \
getDeclaredMetho\
ds getMethod get\
Methods getModif\
iers newInstance\
\x22.split(\x22 \x22));a.\
_innerFunctions.\
getSuperclass=fu\
nction(){return \
this.superClazz}\
;a._innerFunctio\
ns.isAssignableF\
rom=function(b){\
return 0<=\x0aa.get\
InheritedLevel(b\
,this)};a._inner\
Functions.getCon\
structor=functio\
n(){return new j\
ava.lang.reflect\
.Constructor(thi\
s,[],[],java.lan\
g.reflect.Modifi\
er.PUBLIC)};a._i\
nnerFunctions.ge\
tDeclaredMethods\
=a._innerFunctio\
ns.getMethods=fu\
nction(){var a=[\
],b=this.prototy\
pe,c;for(c in b)\
\x22function\x22==type\
of b[c]&&!b[c]._\
_CLASS_NAME__&&a\
.push(new java.l\
ang.reflect.Meth\
od(this,c,[],jav\
a.lang.Void,[],j\
ava.lang.reflect\
.Modifier.PUBLIC\
));b=this;for(c \
in b)\x22function\x22=\
=typeof b[c]&&!b\
[c].__CLASS_NAME\
__&&a.push(new j\
ava.lang.reflect\
.Method(this,\x0ac,\
[],java.lang.Voi\
d,[],java.lang.r\
eflect.Modifier.\
PUBLIC|java.lang\
.reflect.Modifie\
r.STATIC));retur\
n a};a._innerFun\
ctions.getDeclar\
edMethod=a._inne\
rFunctions.getMe\
thod=function(a)\
{var b=this.prot\
otype,c;for(c in\
 b)if(a==c&&\x22fun\
ction\x22==typeof b\
[c]&&!b[c].__CLA\
SS_NAME__)return\
 new java.lang.r\
eflect.Method(th\
is,c,[],java.lan\
g.Void,[],java.l\
ang.reflect.Modi\
fier.PUBLIC);b=t\
his;for(c in b)i\
f(a==c&&\x22functio\
n\x22==typeof b[c]&\
&!b[c].__CLASS_N\
AME__)return new\
 java.lang.refle\
ct.Method(this,c\
,[],java.lang.Vo\
id,\x0a[],java.lang\
.reflect.Modifie\
r.PUBLIC|java.la\
ng.reflect.Modif\
ier.STATIC);retu\
rn null};a._inne\
rFunctions.getMo\
difiers=function\
(){return java.l\
ang.reflect.Modi\
fier.PUBLIC};a._\
innerFunctions.n\
ewInstance=funct\
ion(a){switch(nu\
ll==a?0:a.length\
){case 0:return \
new this;case 1:\
return new this(\
a[0]);case 2:ret\
urn new this(a[0\
],a[1]);case 3:r\
eturn new this(a\
[0],a[1],a[2]);c\
ase 4:return new\
 this(a[0],a[1],\
a[2],a[3]);defau\
lt:for(var b=\x22ne\
w \x22+this.__CLASS\
_NAME__+\x22(\x22,c=0;\
c<a.length;c++)b\
+=(0==c?\x22\x22:\x22,\x22)+\
\x22a[\x22+c+\x22]\x22;\x0aretu\
rn eval(b+\x22)\x22)}}\
;d=a.innerFuncti\
onNames;for(r=0;\
r<d.length;r++)a\
._O[d[r]]=a._inn\
erFunctions[d[r]\
],Array[d[r]]=a.\
_innerFunctions[\
d[r]];a._Loader=\
a.ClazzLoader=fu\
nction(){};var n\
=function(){this\
.parents=[];this\
.musts=[];this.o\
ptionals=[];this\
.onLoaded=this.p\
ath=this.name=th\
is.declaration=n\
ull;this.status=\
0;this.random=0.\
13412};(function\
(a,b){b._checkLo\
ad=j._checkLoad;\
b.updateNodeForF\
unctionDecoratio\
n=function(a){(a\
=C(a))&&a.status\
==n.STATUS_KNOWN\
&&window.setTime\
out(function(a){\
return function(\
){updateNode(a)}\
}(a),\x0a1)};n.prot\
otype.toString=f\
unction(){return\
 this.name||this\
.path||\x22ClazzNod\
e\x22};n.STATUS_UNK\
NOWN=0;n.STATUS_\
KNOWN=1;n.STATUS\
_CONTENT_LOADED=\
2;n.STATUS_MUSTS\
_LOADED=3;n.STAT\
US_DECLARED=4;n.\
STATUS_LOAD_COMP\
LETE=5;var c=[];\
b.requireLoaderB\
yBase=function(a\
){for(var d=0;d<\
c.length;d++)if(\
c[d].base==a)ret\
urn c[d];d=new b\
;d.base=a;c.push\
(d);return d};va\
r d=new n,e={},f\
=0,g=6,h=navigat\
or.userAgent.toL\
owerCase(),k=-1!\
=h.indexOf(\x22oper\
a\x22),m=-1!=h.inde\
xOf(\x22msie\x22)&&!k,\
l=-1!=h.indexOf(\
\x22gecko\x22);if(k&&(\
g=1,k=h.indexOf(\
\x22opera/\x22),\x0a-1!=k\
)){var p=9;try{p\
=parseFloat(h.su\
bString(k+6))}ca\
tch(r){}9.6<=p&&\
(g=6)}var t;self\
.Clazz&&a.isClas\
sDefined?isClass\
Defined=a.isClas\
sDefined:(t={},i\
sClassDefined=fu\
nction(a){return\
!0==t[a]});var u\
=function(a){if(\
!a||0==a.length)\
return[];for(var\
 b=null,c=0;c<a.\
length;c++)if(a[\
c]){if(\x22$\x22==a[c]\
.charAt(0))if(\x22.\
\x22==a[c].charAt(1\
)){if(!b)continu\
e;var d=b.lastIn\
dexOf(\x22.\x22);-1!=d\
&&(b=b.substring\
(0,d),a[c]=b+a[c\
].substring(1))}\
else a[c]=\x22org.e\
clipse.s\x22+a[c].s\
ubstring(1);b=a[\
c]}return a},x=[\
],w={},z=0;b.loa\
dPackageClasspat\
h=\x0afunction(a,c,\
d,e,f,g){f||(f=0\
);e||(e=null);g|\
|(g=0);var j=d&&\
w[\x22@\x22+a];if(0==f\
&&(d&&!w[\x22@java\x22\
]&&0!=a.indexOf(\
\x22java\x22)&&null!=w\
indow[\x22java.regi\
stered\x22]&&!w[\x22@j\
ava\x22])&&(b.loadP\
ackage(\x22java\x22,e?\
function(){b.loa\
dPackageClasspat\
h(a,c,d,e,1)}:nu\
ll),e))return;if\
(a instanceof Ar\
ray)if(u(a),e)g<\
a.length?b.loadP\
ackageClasspath(\
a[g],c,d,functio\
n(){b.loadPackag\
eClasspath(a,c,d\
,e,1,g+1)},1):e(\
);else for(j=0;j\
<a.length;j++)b.\
loadPackageClass\
path(a[j],c,d,nu\
ll);else{switch(\
a){case \x22java.*\x22\
:a=\x22java\x22;case \x22\
java\x22:c&&\x0a(f=\x22@n\
et.sf.j2s.ajax\x22,\
w[f]||(w[f]=c),f\
=\x22@net.sf.j2s\x22,w\
[f]||(w[f]=c));b\
reak;case \x22swt\x22:\
a=\x22org.eclipse.s\
wt\x22;break;case \x22\
ajax\x22:a=\x22net.sf.\
j2s.ajax\x22;break;\
case \x22j2s\x22:a=\x22ne\
t.sf.j2s\x22;break;\
default:a.lastIn\
dexOf(\x22.*\x22)==a.l\
ength-2&&(a=a.su\
bstring(0,a.leng\
th-2))}c&&(w[\x22@\x22\
+a]=c);d&&!j&&!w\
indow[a+\x22.regist\
ered\x22]?(z++,\x22jav\
a\x22==a&&(a=\x22core\x22\
),b.loadClass(a+\
\x22.package\x22,funct\
ion(){0==--z&&ta\
()},!0,!0,1)):e&\
&e()}};a.loadCla\
ss=function(c,d,\
e){self.Class||(\
Class=a,Class.fo\
rName=a._4Name,J\
avaObject=a._O);\
return c&&b.load\
Class(c,\x0ad,!0,e,\
1)};b.loadClass=\
function(c,f,g,j\
,h){h||(h=0);nul\
l==j&&(j=!1);if(\
\x22boolean\x22==typeo\
f f)return a.eva\
lType(c);null!=w\
indow[\x22java.regi\
stered\x22]&&!w[\x22@j\
ava\x22]&&b.loadPac\
kage(\x22java\x22);b.k\
eepOnLoading=!0;\
if(!g&&(z&&c.las\
tIndexOf(\x22.packa\
ge\x22)!=c.length-8\
||0!=c.indexOf(\x22\
java.\x22)&&!isClas\
sDefined(ba)))ma\
.push([c,f]),Sys\
tem.out.println(\
\x22loadclass-queui\
ng\x22+c+ba+\x22 \x22+isC\
lassDefined(ba))\
;else if((h=isCl\
assDefined(c))||\
A[\x22@\x22+c]){if(h&&\
f&&(g=C(c),!g||g\
.status>=n.STATU\
S_LOAD_COMPLETE)\
)j?window.setTim\
eout(f,25):f()}e\
lse{var k=\x0ab.get\
ClasspathFor(c);\
h=e[k];if(!h)for\
(j=x.length;0<=-\
-j;)if(x[j].path\
==k||x[j].name==\
c){h=!0;break}if\
(h){if(f&&(h=C(c\
)))if(h.onLoaded\
){if(f!=h.onLoad\
ed){var m=h.onLo\
aded,l=f;h.onLoa\
ded=function(){m\
();l()}}}else h.\
onLoaded=f}else{\
h=a.unloadedClas\
ses[c]&&C(c)||ne\
w n;h.name=c;h.p\
ath=k;h.isPackag\
e=k.lastIndexOf(\
\x22package.js\x22)==k\
.length-10;ga(k,\
c,h);h.onLoaded=\
f;h.status=n.STA\
TUS_KNOWN;c=!1;f\
or(j=x.length;0<\
=--j;)if(x[j].st\
atus!=n.STATUS_L\
OAD_COMPLETE){c=\
!0;break}if(h.is\
Package){for(j=x\
.length;0<=--j&&\
\x0a!x[j].isPackage\
;)x[j+1]=x[j];x[\
++j]=h}else c&&x\
.push(h);if(!c){\
var v=!1;f&&(v=H\
,H=!0);g&&(f=nul\
l);ca(d,h,!0);F(\
h,h.path,h.requi\
redBy,!1,f?funct\
ion(){H=v;f()}:n\
ull)}}}};b.loadP\
ackage=function(\
a,c){c||(c=null)\
;window[a+\x22.regi\
stered\x22]=!1;b.lo\
adPackageClasspa\
th(a,b.J2SLibBas\
e||(b.J2SLibBase\
=b.getJ2SLibBase\
()||\x22j2s/\x22),!0,c\
)};b.jarClasspat\
h=function(a,b){\
b instanceof Arr\
ay||(b=[b]);u(b)\
;for(var c=b.len\
gth;0<=--c;)w[\x22#\
\x22+b[c]]=a;w[\x22$\x22+\
a]=b};b.register\
Packages=functio\
n(c,d){for(var e\
=b.getClasspathF\
or(c+\x22.*\x22,\x0a!0),f\
=0;f<d.length;f+\
+)window.Clazz&&\
a.declarePackage\
(c+\x22.\x22+d[f]),b.l\
oadPackageClassp\
ath(c+\x22.\x22+d[f],e\
)};b.getClasspat\
hFor=function(c,\
d,e){var f=w[\x22#\x22\
+c];if(!f||d||e)\
{var g,j;if(f){i\
f(c=c.replace(/\x5c\
./g,\x22/\x22),0<=(j=f\
.lastIndexOf(c))\
||0<=(j=c.lastIn\
dexOf(\x22/\x22))&&0<=\
(j=f.lastIndexOf\
(c.substring(0,j\
))))g=f.substrin\
g(0,j)}else{for(\
j=c.length+2;0<=\
(j=c.lastIndexOf\
(\x22.\x22,j-2))&&!(g=\
w[\x22@\x22+c.substrin\
g(0,j)]););d||(c\
=c.replace(/\x5c./g\
,\x22/\x22))}null==g&&\
(g=window.Clazz&\
&a.binaryFolders\
&&a.binaryFolder\
s.length?a.binar\
yFolders[0]:\x0ab.b\
inaryFolders&&b.\
binaryFolders.le\
ngth?b.binaryFol\
ders[0]:\x22j2s\x22);f\
=(g.lastIndexOf(\
\x22/\x22)==g.length-1\
?g:g+\x22/\x22)+(d?\x22\x22:\
c.lastIndexOf(\x22/\
*\x22)==c.length-2?\
c.substring(0,j+\
1):c+(!e?\x22.js\x22:\x22\
.\x22!=e.charAt(0)?\
\x22.\x22+e:e))}return\
 f};b.ignore=fun\
ction(){var a=1=\
=arguments.lengt\
h&&arguments[0]i\
nstanceof Array?\
a=arguments[0]:n\
ull,b=a?a.length\
:arguments.lengt\
h;if(!a)for(var \
a=Array(b),c=0;c\
<b;c++)a[c]=argu\
ments[c];u(a);fo\
r(c=0;c<b;c++)A[\
\x22@\x22+a[c]]=1};b.o\
nScriptLoading=f\
unction(){};b.on\
ScriptLoaded=fun\
ction(){};b.onSc\
riptInitialized=\
\x0afunction(){};b.\
onScriptComplete\
d=function(){};b\
.onClassUnloaded\
=function(){};b.\
onGlobalLoaded=f\
unction(){};b.ke\
epOnLoading=!0;v\
ar y={},A={},K=f\
unction(c,d,e,f)\
{if(!f)try{eval(\
e+\x22;//# sourceUR\
L=\x22+c)}catch(g){\
if(a._isQuiet)re\
turn;c=\x22[Java2Sc\
ript] The requir\
ed class file \x5cn\
\x5cn\x22+c+(0==e.inde\
xOf(\x22[Exception\x22\
)&&e.indexOf(\x22da\
ta: no\x22)?\x22\x5cnwas \
not found.\x5cn\x22:\x22\x5c\
ncould not be lo\
aded. Script err\
or: \x22+g.message+\
\x22 \x5cn\x5cndata:\x5cn\x5cn\x22\
+e)+\x22\x5cn\x5cn\x22+a.get\
StackTrace();ale\
rt(c);a.alert(c)\
;throw g;}b.onSc\
riptLoaded(c,!1)\
;W(d)},\x0aL=functi\
on(a){return fun\
ction(){if(\x22inte\
ractive\x22!=a.read\
yState){try{a.pa\
rentNode&&a.pare\
ntNode.removeChi\
ld(a)}catch(b){}\
a=null}}},I=func\
tion(a){window[\x22\
j2s.script.debug\
ging\x22]||window.s\
etTimeout(L(a),1\
)};a._4Name=func\
tion(c,d,e){if(a\
.isClassDefined(\
c))return a.eval\
Type(c);d=j._isA\
sync&&d?d._resto\
reState(c,e):nul\
l;if(1==d)return\
 null;if(b.setLo\
adingMode(d?b.MO\
DE_SCRIPT:\x22xhr.s\
ync\x22))return b.l\
oadClass(c,d,!1,\
!0,1),null;b.loa\
dClass(c);return\
 a.evalType(c)};\
a.currentPath=\x22\x22\
;var F=function(\
c,d,g,h,k){a.cur\
rentPath=\x0ad;h&&a\
lert(\x22WHY>>\x22);h=\
e[d];e[d]=!0;la(\
x,d);ha=!0;ia=!1\
;b._checkLoad&&S\
ystem.out.printl\
n(\x22\x5ct\x22+d+(g?\x22\x5cn \
-- required by \x22\
+g:\x22\x22)+\x22  ajax=\x22\
+ha+\x22 async=\x22+ia\
);g=d;a._debuggi\
ng&&(d=d.replace\
(/\x5c.z\x5c.js/,\x22.js\x22\
));h||System.out\
.println(\x22loadSc\
ript \x22+d);b.onSc\
riptLoading(d);i\
f(ha&&!ia){var m\
=j._getFileData(\
d);try{K(d,g,m,h\
)}catch(l){alert\
(l+\x22 loading fil\
e \x22+d+\x22 \x22+c.name\
+\x22 \x22+a.getStackT\
race())}k&&k()}e\
lse c={dataType:\
\x22script\x22,async:!\
0,type:\x22GET\x22,url\
:d,success:M(d,!\
1,k),error:M(d,!\
0,k)},f++,h?setT\
imeout(c.success\
,\x0a0):j.$ajax(c)}\
,M=function(c,d,\
e){a.getStackTra\
ce();return func\
tion(){l&&this.t\
imeoutHandle&&(w\
indow.clearTimeo\
ut(this.timeoutH\
andle),this.time\
outHandle=null);\
0<f&&f--;this.on\
error=this.onloa\
d=null;d&&alert(\
\x22There was a pro\
blem loading \x22+c\
);b.onScriptLoad\
ed(c,!0);var a=t\
his,g;g=e?functi\
on(){I(a);W(c,e)\
}:function(){I(a\
);W(c)};0<=na?wi\
ndow.setTimeout(\
function(){W(c,g\
)},na):W(c,g)}},\
H=!0,N=!1,W=func\
tion(c,j){var h=\
y[\x22@\x22+c];if(h){v\
ar k,s=w[\x22$\x22+c];\
if(s)for(var l=0\
;l<s.length;l++)\
{var v=s[l];if(v\
!=h.name&&\x0a(k=C(\
v)))k.status<n.S\
TATUS_CONTENT_LO\
ADED&&(k.status=\
n.STATUS_CONTENT\
_LOADED,updateNo\
de(k));else{k=ne\
w n;k.name=v;var\
 p=w[\x22#\x22+v];p||(\
alert(v+\x22 J2S er\
ror in tryToLoad\
Next\x22),error(\x22Ja\
va2Script implem\
entation error! \
Please report th\
is bug!\x22));k.pat\
h=p;ga(k.path,v,\
k);k.status=n.ST\
ATUS_CONTENT_LOA\
DED;ca(d,k,!1);u\
pdateNode(k)}}if\
(h instanceof Ar\
ray)for(l=0;l<h.\
length;l++)h[l].\
status<n.STATUS_\
CONTENT_LOADED&&\
(h[l].status=n.S\
TATUS_CONTENT_LO\
ADED,updateNode(\
h[l]));else if(h\
.status<n.STATUS\
_CONTENT_LOADED)\
{k=\x0a!1;s=documen\
t.getElementsByT\
agName(\x22SCRIPT\x22)\
;for(l=0;l<s.len\
gth;l++)if(m){if\
(s[l].onreadysta\
techange&&s[l].o\
nreadystatechang\
e.path==h.path&&\
\x22interactive\x22==s\
[l].readyState){\
k=!0;break}}else\
 if(s[l].onload&\
&s[l].onload.pat\
h==h.path){k=!0;\
break}k||(h.stat\
us=n.STATUS_CONT\
ENT_LOADED,updat\
eNode(h))}if(b.k\
eepOnLoading){l=\
!0;if(k=oa(n.STA\
TUS_KNOWN))for(j\
a(k);f<g&&(k=oa(\
n.STATUS_KNOWN))\
;)ja(k);else if(\
0!=x.length)k=x.\
shift(),!e[k.pat\
h]||0!=x.length|\
|!H||k.musts.len\
gth||k.optionals\
.length?(ca(d,k,\
!0),F(k,k.path,\x0a\
k.requiredBy,!1)\
):H&&(H=!1);else\
 if(k=pa(n.STATU\
S_KNOWN))for(ja(\
k);f<g&&(k=pa(n.\
STATUS_KNOWN));)\
ja(k);else l=!1;\
if(!(l||0<f)){h=\
[oa,pa];s=null;f\
or(l=0;2>l;l++)f\
or(;k=h[l](n.STA\
TUS_CONTENT_LOAD\
ED);)1==l&&s===k\
&&(k.status=n.ST\
ATUS_LOAD_COMPLE\
TE),updateNode(k\
),s=k;for(;!(O=[\
],!Q(d,c)););for\
(l=0;2>l;l++)for\
(s=null;(k=h[l](\
n.STATUS_DECLARE\
D))&&s!==k;)upda\
teNode(s=k);s=[]\
;for(l=0;2>l;l++\
)for(;k=h[l](n.S\
TATUS_DECLARED);\
)s.push(k),k.sta\
tus=n.STATUS_LOA\
D_COMPLETE;if(s.\
length){for(l=0;\
l<s.length;l++)P\
(s[l]);\x0afor(l=0;\
l<s.length;l++)i\
f(h=s[l].onLoade\
d)s[l].onLoaded=\
null,h()}if(j)j(\
);else if(b._cla\
ssCountPending)f\
or(v in b._class\
Pending){if(k=C(\
v),System.out.pr\
intln(\x22class lef\
t pending \x22+v+\x22 \
\x22+k),k){updateNo\
de(k);break}}els\
e b._checkLoad&&\
(System.out.prin\
tln(\x22I think I'm\
 done: SAEM call\
 count: \x22+q),a.s\
howDuplicates(!0\
));b.onGlobalLoa\
ded()}}}},O=[],Q\
=function(a,c){v\
ar d=O,e=d.lengt\
h;d.push(a);for(\
var f=e;0<=--f&&\
!(d[f]===a&&d[f]\
.status>=n.STATU\
S_DECLARED););if\
(0<=f){if(b._che\
ckLoad){var g;Sy\
stem.out.println\
(\x22cycle found lo\
ading \x22+\x0ac+\x22 for\
 \x22+a)}for(;f<e;f\
++){var h=d[f];h\
.status=n.STATUS\
_LOAD_COMPLETE;P\
(h);for(g=0;g<h.\
parents.length;g\
++)updateNode(h.\
parents[g]);h.pa\
rents=[];var j=h\
.onLoaded;b._che\
ckLoad&&(g=\x22cycl\
e setting status\
 to LOAD_COMPLET\
E for \x22+h.name+(\
j?\x22 firing \x22+j.t\
oString():\x22\x22),Sy\
stem.out.println\
(g));j&&(h.onLoa\
ded=null,j())}d.\
length=0;return!\
0}h=[a.musts,a.o\
ptionals];for(g=\
0;2>g;g++){j=h[g\
];for(f=j.length\
;0<=--f;)if(j[f]\
.status==n.STATU\
S_DECLARED&&Q(j[\
f],c))return!0}d\
.length=e;return\
!1};b._classCoun\
tPending=0;b._cl\
assCountOK=\x0a0;b.\
_classPending={}\
;b.showPending=f\
unction(){var a=\
[],c;for(c in b.\
_classPending){v\
ar d=C(c);d?(a.p\
ush(d),System.ou\
t.println(R(\x22\x22,\x22\
\x22,d,\x22\x22,0))):aler\
t(\x22No node for \x22\
+c)}return a};va\
r R=function(a,b\
,c,d,e){b+=\x22--\x22+\
c.name;a+=b+\x22\x5cn\x22\
;if(5<e)return a\
+(d+\x22 ...\x5cn\x22);d+\
=\x22\x5ct\x22;a+=d+\x22stat\
us: \x22+c.status+\x22\
\x5cn\x22;if(c.parents\
&&c.parents.leng\
th&&c.parents[0]\
&&c.parents[0].n\
ame){a+=d+\x22paren\
ts: \x22+c.parents.\
length+\x22\x5cn\x22;for(\
var f=0;f<c.pare\
nts.length;f++)a\
=R(a,b,c.parents\
[f],d+\x22\x5ct\x22,e+1);\
a+=\x22\x5cn\x22}return a\
};updateNode=fun\
ction(a){if(!a.n\
ame||\x0aa.status>=\
n.STATUS_LOAD_CO\
MPLETE)P(a);else\
{var c=!0;if(a.m\
usts.length&&a.d\
eclaration)for(v\
ar d=a.musts.len\
gth,e=d;0<=--e;)\
{var f=a.musts[e\
];f.requiredBy=a\
;if(f.status<n.S\
TATUS_DECLARED&&\
isClassDefined(f\
.name)){var g=[]\
;f.status=n.STAT\
US_LOAD_COMPLETE\
;P(f);if(f.decla\
ration&&f.declar\
ation.clazzList)\
{for(var h=0,j=f\
.declaration.cla\
zzList,k=j.lengt\
h;h<k;h++){var l\
=C(j[h]);l&&(l.s\
tatus!=n.STATUS_\
LOAD_COMPLETE&&l\
!==f)&&(l.status\
=f.status,l.decl\
aration=null,P(l\
),l.onLoaded&&g.\
push(l))}f.decla\
ration=null}f.on\
Loaded&&\x0ag.push(\
f);for(h=0;h<g.l\
ength;h++)if(j=g\
[h].onLoaded)g[h\
].onLoaded=null,\
j()}else f.statu\
s==n.STATUS_CONT\
ENT_LOADED&&upda\
teNode(f),f.stat\
us<n.STATUS_DECL\
ARED&&(c=!1);a.m\
usts.length!=d&&\
(e=d=a.musts.len\
gth,c=!0)}if(c){\
if(a.status<n.ST\
ATUS_DECLARED){i\
f(e=a.declaratio\
n)e(),e.executed\
=!0;b._checkLoad\
&&b._classPendin\
g[a.name]&&(dele\
te b._classPendi\
ng[a.name],b._cl\
assCountOK,b._cl\
assCountPending-\
-);a.status=n.ST\
ATUS_DECLARED;t&\
&(t[a.name]=!0);\
b.onScriptInitia\
lized(a.path);if\
(a.declaration&&\
a.declaration.cl\
azzList){h=\x0a0;j=\
a.declaration.cl\
azzList;for(k=j.\
length;h<k;h++)i\
f((l=C(j[h]))&&l\
.status!=n.STATU\
S_DECLARED&&l!==\
a)l.status=n.STA\
TUS_DECLARED,t&&\
(t[l.name]=!0),b\
.onScriptInitial\
ized(l.path)}}c=\
n.STATUS_DECLARE\
D;if(0==a.option\
als.length&&0==a\
.musts.length||a\
.status>n.STATUS\
_KNOWN&&!a.decla\
ration||S(a.must\
s,n.STATUS_LOAD_\
COMPLETE)&&S(a.o\
ptionals,n.STATU\
S_LOAD_COMPLETE)\
){c=n.STATUS_LOA\
D_COMPLETE;if(!T\
(a,c))return!1;i\
f(a.declaration&\
&a.declaration.c\
lazzList){h=0;j=\
a.declaration.cl\
azzList;for(k=j.\
length;h<k;h++)i\
f((l=\x0aC(j[h]))&&\
l.status!=c&&l!=\
=a)if(l.declarat\
ion=null,!T(l,c)\
)return!1}}if(a.\
parents&&a.paren\
ts.length){for(e\
=0;e<a.parents.l\
ength;e++)h=a.pa\
rents[e],h.statu\
s<c&&updateNode(\
h,h.name);c==n.S\
TATUS_LOAD_COMPL\
ETE&&(a.parents=\
[])}}}};var S=fu\
nction(a,b){for(\
var c=a.length;0\
<=--c;)if(a[c].s\
tatus<b)return!1\
;return!0},T=fun\
ction(a,c){a.sta\
tus=c;b.onScript\
Completed(a.path\
);var d=a.onLoad\
ed;if(d&&(a.onLo\
aded=null,d(),!b\
.keepOnLoading))\
return!1;P(a);re\
turn!0},V={\x22r0.1\
3412\x22:1},X=funct\
ion(){for(;;){va\
r a=Math.random(\
),\x0ab=\x22r\x22+a;if(!V\
[b])return V[b]=\
1,d.random=a}},C\
=function(a){X()\
;return Y(a,d)},\
pa=function(a){X\
();return da(d,a\
)},oa=function(a\
){return aa(d,a)\
},Y=function(a,b\
){var c;return b\
.name==a?b:(c=Z(\
a,b.musts))||(c=\
Z(a,b.optionals)\
)?c:null},Z=func\
tion(a,b){for(va\
r c=d.random,e=b\
.length;0<=--e;)\
{var f=b[e];if(f\
.name==a||f.rand\
om!=c&&(f.random\
=c,f=Y(a,f)))ret\
urn f}return nul\
l},ka=function(a\
,b){return a.sta\
tus==b&&(b!=n.ST\
ATUS_KNOWN||!e[a\
.path])&&(b==n.S\
TATUS_DECLARED||\
!isClassDefined(\
a.name))},aa=fun\
ction(a,\x0ab){for(\
var c=a.musts.le\
ngth;0<=--c;){va\
r d=a.musts[c];i\
f(ka(d,b)||(d=aa\
(d,b)))return d}\
return ka(a,b)?a\
:null},da=functi\
on(a,b){var c;re\
turn(c=ea(a.must\
s,b))||(c=ea(a.o\
ptionals,b))||ka\
(c=a,b)?c:null},\
ea=function(a,b)\
{if(a)for(var c=\
d.random,e=0;e<a\
.length;e++){var\
 f=a[e];if(ka(f,\
b)||f.random!=c&\
&(f.random=c,f=d\
a(f,b)))return f\
}return null},qa\
=function(a,c,e,\
f){if(c instance\
of Array){u(c);f\
or(var g=0;g<c.l\
ength;g++)qa(a,c\
[g],e,f,c)}else{\
b._checkLoad&&!b\
._classPending[c\
]&&(b._classPend\
ing[c]=1,0==b._c\
lassCountPending\
++&&\x0a(b._classCo\
untOK=0),System.\
out.println(\x22Loa\
ding class \x22+c))\
;g=y[\x22#\x22+c];g||(\
g=(g=C(c))?g:new\
 n,g.name=c,g.pa\
th=w[\x22#\x22+c]||\x22un\
known\x22,ga(g.path\
,c,g),g.status=n\
.STATUS_KNOWN,ca\
(d,g,!1));fa(g,a\
,!0);5==argument\
s.length&&f&&(f.\
status=g.status,\
f.clazzList=argu\
ments[4]);if(g.d\
eclaration=f)g.s\
tatus=n.STATUS_C\
ONTENT_LOADED;fa\
(g,e,!1)}},fa=fu\
nction(a,b,c){if\
(b&&b.length){u(\
b);for(var d=0;d\
<b.length;d++){v\
ar e=b[d];if(e&&\
!isClassDefined(\
e)&&!A[\x22@\x22+e]){v\
ar f=C(e);f||(f=\
new n,f.name=e,f\
.status=n.STATUS\
_KNOWN);f.requir\
edBy=\x0aa;ca(a,f,c\
)}}}};window.Cla\
zz?a.load=qa:b.l\
oad=qa;var ga=fu\
nction(a,b,c){va\
r d=\x22@\x22+a;if(a=y\
[d])if(a instanc\
eof Array){for(v\
ar d=!1,e=0;e<a.\
length;e++)if(a[\
e].name==b){d=!0\
;break}d||a.push\
(c)}else y[d]=[a\
,c];else y[d]=c;\
y[\x22#\x22+b]=c},ja=f\
unction(a){var c\
=a.name;if(!isCl\
assDefined(c)&&!\
A[\x22@\x22+c]){var d=\
b.getClasspathFo\
r(c);a.path=d;ga\
(d,c,a);if(!e[d]\
)return F(a,d,a.\
requiredBy,!1),!\
0}return!1},ba=b\
.runtimeKeyClass\
=\x22java.lang.Stri\
ng\x22,ma=[];b.getJ\
2SLibBase=functi\
on(){var a=windo\
w[\x22j2s.lib\x22];ret\
urn a?a.base+\x0a(\x22\
.\x22==a.alias?\x22\x22:(\
a.alias?a.alias:\
a.version?a.vers\
ion:\x221.0.0\x22)+\x22/\x22\
):null};var ia=!\
0,ha=!1,na=-1;b.\
MODE_SCRIPT=4;b.\
MODE_XHR=2;b.MOD\
E_SYNC=1;b.setLo\
adingMode=functi\
on(a,c){var d=!0\
,e=!0;\x22string\x22==\
typeof a?(a=a.to\
LowerCase(),0<=a\
.indexOf(\x22script\
\x22)?e=!1:a.indexO\
f(\x22async\x22),d=!1)\
:a&b.MODE_SCRIPT\
?e=!1:d=!(a&b.MO\
DE_SYNC);ha=e;na\
=(ia=d)&&0<=c?c:\
-1;return d};var\
 ta=function(){i\
f(!z&&isClassDef\
ined(ba)){for(va\
r a=ma,c=0;c<a.l\
ength;c++)b.load\
Class(a[c][0],a[\
c][1]);ma=[]}};b\
.loadZJar=functi\
on(a,c){var d=nu\
ll,\x0ae=c instance\
of Array;e?c=c[c\
.length-1]:d=c==\
ba?ta:null;b.jar\
Classpath(a,e?c:\
[c]);b.loadClass\
(c,d,!0)};var ua\
={},ra=[],ca=fun\
ction(a,b,c){var\
 e=!1;c?(c=a.mus\
ts,b.requiredBy|\
|(b.requiredBy=a\
)):c=a.optionals\
;ua[b.name]||(ra\
.push(b),ua[b.na\
me]=b);for(var f\
=0;f<c.length;f+\
+)if(c[f].name==\
b.name){e=!0;bre\
ak}e||(c.push(b)\
,H&&(0!=b.name.i\
ndexOf(\x22java\x22)&&\
0!=b.name.indexO\
f(\x22net.sf.j2s.aj\
ax\x22))&&(N&&(H=!1\
),N=!0));a:{if(a\
.name&&a!=d&&a!=\
b)for(e=0;e<b.pa\
rents.length;e++\
)if(b.parents[e]\
.name==a.name)br\
eak a;b.parents.\
push(a)}},\x0aP=fun\
ction(a){var b=a\
.parents;if(b)fo\
r(var c=b.length\
;0<=--c;)la(b[c]\
.musts,a)||la(b[\
c].optionals,a)}\
;a.binaryFolders\
=b.binaryFolders\
=[b.getJ2SLibBas\
e()]})(a,a._Load\
er);a._LoaderPro\
gressMonitor={};\
var y=a._LoaderP\
rogressMonitor,F\
=null,K=0,u=null\
,Q=0;y.DEFAULT_O\
PACITY=j&&j._j2s\
LoadMonitorOpaci\
ty?j._j2sLoadMon\
itorOpacity:55;y\
.hideMonitor=fun\
ction(){u.style.\
display=\x22none\x22};\
y.showStatus=fun\
ction(a,b){if(!u\
){var c=document\
.createElement(\x22\
DIV\x22);c.id=\x22_Loa\
der-status\x22;c.st\
yle.cssText=\x22pos\
ition:absolute;b\
ottom:4px;left:4\
px;padding:2px 8\
px;z-index:\x22+\x0a(w\
indow[\x22j2s.lib\x22]\
.monitorZIndex||\
1E4)+\x22;backgroun\
d-color:#8e0000;\
color:yellow;fon\
t-family:Arial, \
sans-serif;font-\
size:10pt;white-\
space:nowrap;\x22;c\
.onmouseover=ra;\
u=c;document.bod\
y.appendChild(c)\
;da||(da=!0)}ea(\
u);if(null==a)b?\
M():y.hideMonito\
r();else{u.appen\
dChild(document.\
createTextNode(\x22\
\x22+a));\x22none\x22==u.\
style.display&&(\
u.style.display=\
\x22\x22);fa(y.DEFAULT\
_OPACITY);var d,\
c=navigator.user\
Agent;d=document\
.body;var e=d.pa\
rentNode,f=e.cli\
entHeight;d=d.sc\
rollTop+d.offset\
Top;var g=e.scro\
llTop+e.offsetTo\
p,c=\x0a0>c.indexOf\
(\x22Opera\x22)&&docum\
ent.all?0==f?d:g\
:0>c.indexOf(\x22Ge\
cko\x22)?f==e.offse\
tHeight&&f==e.sc\
rollHeight?d:g:d\
;Q!=c&&(Q=c,u.st\
yle.bottom=Q+4+\x22\
px\x22);b&&M()}};va\
r ea=function(a)\
{if(a)for(var b=\
a.childNodes.len\
gth;0<=--b;){var\
 c=a.childNodes[\
b];if(c){c.child\
Nodes&&c.childNo\
des.length&&ea(c\
);try{a.removeCh\
ild(c)}catch(d){\
}}}},fa=function\
(a){F&&a==y.DEFA\
ULT_OPACITY&&(wi\
ndow.clearTimeou\
t(F),F=null);K=a\
;navigator.userA\
gent.toLowerCase\
();u.style.filte\
r=\x22Alpha(Opacity\
=\x22+a+\x22)\x22;u.style\
.opacity=a/100},\
ra=function(){y.\
hideMonitor()},\x0a\
da=!1,M=function\
(){\x22none\x22!=u.sty\
le.display&&(K==\
y.DEFAULT_OPACIT\
Y?(F=window.setT\
imeout(function(\
){M()},750),K-=5\
):0<=K-10?(fa(K-\
10),F=window.set\
Timeout(function\
(){M()},40)):u.s\
tyle.display=\x22no\
ne\x22)},p=a.Consol\
e,z=System;p.max\
TotalLines=1E4;p\
.setMaxTotalLine\
s=function(a){p.\
maxTotalLines=0<\
a?a:999999};p.ma\
xLatency=40;p.se\
tMaxLatency=func\
tion(a){p.maxLat\
ency=0<a?a:40};p\
.pinning=!1;p.en\
ablePinning=func\
tion(a){p.pinnin\
g=a};p.linesCoun\
t=0;p.metLineBre\
ak=!1;p.createCo\
nsoleWindow=func\
tion(){var a=doc\
ument.createElem\
ent(\x22DIV\x22);\x0aa.st\
yle.cssText=\x22fon\
t-family:monospa\
ce, Arial, sans-\
serif;\x22;document\
.body.appendChil\
d(a);return a};v\
ar A=String.from\
CharCode(160),A=\
A+(A+A+A);p.cons\
oleOutput=functi\
on(a,b){var c=wi\
ndow[\x22j2s.lib\x22];\
(c=c&&c.console)\
&&\x22string\x22==type\
of c&&(c=documen\
t.getElementById\
(c));if(!c)retur\
n!1;if(p.linesCo\
unt>p.maxTotalLi\
nes){for(var d=0\
;d<p.linesCount-\
p.maxTotalLines;\
d++)c&&0<c.child\
Nodes.length&&c.\
removeChild(c.ch\
ildNodes[0]);p.l\
inesCount=p.maxT\
otalLines}var e=\
!1;a=(\x22undefined\
\x22==typeof a?\x22\x22:n\
ull==a?\x22null\x22:\x22\x22\
+\x0aa).replace(/\x5ct\
/g,A);if(0<a.len\
gth)switch(a.cha\
rAt(a.length-1))\
{case \x22\x5cn\x22:case \
\x22\x5cr\x22:a=1<a.lengt\
h?a.substring(0,\
a.length-(\x22\x5cr\x22==\
a.charAt(a.lengt\
h-2)?2:1)):\x22\x22,e=\
!0}var f=null;a=\
a.replace(/\x5ct/g,\
A);for(var f=a.s\
plit(/\x5cr\x5cn|\x5cr|\x5cn\
/g),d=0,g=f.leng\
th-1;d<=g;d++){v\
ar h=null;if(p.m\
etLineBreak||0==\
p.linesCount||1>\
c.childNodes.len\
gth)h=document.c\
reateElement(\x22DI\
V\x22),c.appendChil\
d(h),h.style.whi\
teSpace=\x22nowrap\x22\
,p.linesCount++;\
else try{h=c.chi\
ldNodes[c.childN\
odes.length-1]}c\
atch(j){h=docume\
nt.createElement\
(\x22DIV\x22),\x0ac.appen\
dChild(h),h.styl\
e.whiteSpace=\x22no\
wrap\x22,p.linesCou\
nt++}var k=docum\
ent.createElemen\
t(\x22SPAN\x22);h.appe\
ndChild(k);k.sty\
le.whiteSpace=\x22n\
owrap\x22;b&&(k.sty\
le.color=b);h=f[\
d];0==h.length&&\
(h=A);k.appendCh\
ild(document.cre\
ateTextNode(h));\
p.pinning||(c.sc\
rollTop+=100);p.\
metLineBreak=d!=\
g||e}d=c.parentN\
ode.className;!p\
.pinning&&(d&&-1\
!=d.indexOf(\x22com\
posite\x22))&&(c.pa\
rentNode.scrollT\
op=c.parentNode.\
scrollHeight);p.\
lastOutputTime=(\
new Date).getTim\
e()};p.clear=fun\
ction(){try{p.me\
tLineBreak=!0;va\
r a=window[\x22j2s.\
lib\x22],\x0ab=a&&a.co\
nsole;if(b&&(b=d\
ocument.getEleme\
ntById(b))){for(\
var c=b.childNod\
es,d=c.length;0<\
=--d;)b.removeCh\
ild(c[d]);p.line\
sCount=0}}catch(\
e){}};a.alert=fu\
nction(a){p.cons\
oleOutput(a+\x22\x5cr\x5c\
n\x22)};z.out.print\
=function(a){p.c\
onsoleOutput(a)}\
;z.out.println=f\
unction(a){p.con\
soleOutput(\x22unde\
fined\x22==typeof a\
?\x22\x5cr\x5cn\x22:null==a?\
\x22null\x5cr\x5cn\x22:a+\x22\x5cr\
\x5cn\x22)};z.out.writ\
e=function(a,b,c\
){z.out.print(St\
ring.instantiali\
ze(a).substring(\
b,b+c))};z.err._\
_CLASS_NAME__=\x22j\
ava.io.PrintStre\
am\x22;z.err.print=\
function(a){p.co\
nsoleOutput(a,\x0a\x22\
red\x22)};z.err.pri\
ntln=function(a)\
{p.consoleOutput\
(\x22undefined\x22==ty\
peof a?\x22\x5cr\x5cn\x22:nu\
ll==a?\x22null\x5cr\x5cn\x22\
:a+\x22\x5cr\x5cn\x22,\x22red\x22)\
};z.err.write=fu\
nction(a,b,c){z.\
err.print(String\
.instantialize(a\
).substring(b,b+\
c))}}(Clazz,Jmol\
))};Jmol.___Jmol\
Date=\x22$Date: 201\
6-06-27 01:32:19\
 -0400 (Mon, 27 \
Jun 2016) $\x22;Jmo\
l.___fullJmolPro\
perties=\x22src/org\
/jmol/viewer/Jmo\
l.properties\x22;Jm\
ol.___JmolVersio\
n=\x2214.7.0_2016.0\
6.27\x22;\x0a\
\x00\x02Z@\
(\
function(c,m){\x22o\
bject\x22===typeof \
module&&\x22object\x22\
===typeof module\
.exports?module.\
exports=c.docume\
nt?m(c,!0):funct\
ion(c){if(!c.doc\
ument)throw Erro\
r(\x22jQuery requir\
es a window with\
 a document\x22);re\
turn m(c)}:m(c)}\
)(\x22undefined\x22!==\
typeof window?wi\
ndow:this,functi\
on(c,m){function\
 h(a){var g=a.le\
ngth,k=d.type(a)\
;return\x22function\
\x22===k||d.isWindo\
w(a)?!1:1===a.no\
deType&&g?!0:\x22ar\
ray\x22===k||0===g|\
|\x22number\x22===type\
of g&&0<g&&g-1 i\
n a}function j(a\
,g,k){if(d.isFun\
ction(g))return \
d.grep(a,functio\
n(a,d){return!!g\
.call(a,\x0ad,a)!==\
k});if(g.nodeTyp\
e)return d.grep(\
a,function(a){re\
turn a===g!==k})\
;if(\x22string\x22===t\
ypeof g){if(Uc.t\
est(g))return d.\
filter(g,a,k);g=\
d.filter(g,a)}re\
turn d.grep(a,fu\
nction(a){return\
 0<=d.inArray(a,\
g)!==k})}functio\
n l(a,g){do a=a[\
g];while(a&&1!==\
a.nodeType);retu\
rn a}function r(\
){u.addEventList\
ener?(u.removeEv\
entListener(\x22DOM\
ContentLoaded\x22,p\
,!1),c.removeEve\
ntListener(\x22load\
\x22,p,!1)):(u.deta\
chEvent(\x22onready\
statechange\x22,p),\
c.detachEvent(\x22o\
nload\x22,p))}funct\
ion p(){if(u.add\
EventListener||\x22\
load\x22===event.ty\
pe||\x0a\x22complete\x22=\
==u.readyState)r\
(),d.ready()}fun\
ction v(a,g,k){i\
f(void 0===k&&1=\
==a.nodeType)if(\
k=\x22data-\x22+g.repl\
ace(Vc,\x22-$1\x22).to\
LowerCase(),k=a.\
getAttribute(k),\
\x22string\x22===typeo\
f k){try{k=\x22true\
\x22===k?!0:\x22false\x22\
===k?!1:\x22null\x22==\
=k?null:+k+\x22\x22===\
k?+k:Wc.test(k)?\
d.parseJSON(k):k\
}catch(q){}d.dat\
a(a,g,k)}else k=\
void 0;return k}\
function w(a){fo\
r(var g in a)if(\
!(\x22data\x22===g&&d.\
isEmptyObject(a[\
g]))&&\x22toJSON\x22!=\
=g)return!1;retu\
rn!0}function b(\
a,g,k,q){if(d.ac\
ceptData(a)){var\
 b=d.expando,c=a\
.nodeType,e=c?d.\
cache:a,f=\x0ac?a[b\
]:a[b]&&b;if(f&&\
e[f]&&(q||e[f].d\
ata)||!(void 0==\
=k&&\x22string\x22===t\
ypeof g)){f||(f=\
c?a[b]=V.pop()||\
d.guid++:b);e[f]\
||(e[f]=c?{}:{to\
JSON:d.noop});if\
(\x22object\x22===type\
of g||\x22function\x22\
===typeof g)q?e[\
f]=d.extend(e[f]\
,g):e[f].data=d.\
extend(e[f].data\
,g);a=e[f];q||(a\
.data||(a.data={\
}),a=a.data);voi\
d 0!==k&&(a[d.ca\
melCase(g)]=k);\x22\
string\x22===typeof\
 g?(k=a[g],null=\
=k&&(k=a[d.camel\
Case(g)])):k=a;r\
eturn k}}}functi\
on e(a,g,k){if(d\
.acceptData(a)){\
var q,b,c=a.node\
Type,e=c?d.cache\
:a,f=c?a[d.expan\
do]:d.expando;if\
(e[f]){if(g&&\x0a(q\
=k?e[f]:e[f].dat\
a)){d.isArray(g)\
?g=g.concat(d.ma\
p(g,d.camelCase)\
):g in q?g=[g]:(\
g=d.camelCase(g)\
,g=g in q?[g]:g.\
split(\x22 \x22));for(\
b=g.length;b--;)\
delete q[g[b]];i\
f(k?!w(q):!d.isE\
mptyObject(q))re\
turn}if(!k&&(del\
ete e[f].data,!w\
(e[f])))return;c\
?d.cleanData([a]\
,!0):s.deleteExp\
ando||e!=e.windo\
w?delete e[f]:e[\
f]=null}}}functi\
on f(){return!0}\
function n(){ret\
urn!1}function t\
(){try{return u.\
activeElement}ca\
tch(a){}}functio\
n B(a){var g=Rb.\
split(\x22|\x22);a=a.c\
reateDocumentFra\
gment();if(a.cre\
ateElement)for(;\
g.length;)a.crea\
teElement(g.pop(\
));\x0areturn a}fun\
ction E(a,g){var\
 k,q,b=0,c=typeo\
f a.getElementsB\
yTagName!==N?a.g\
etElementsByTagN\
ame(g||\x22*\x22):type\
of a.querySelect\
orAll!==N?a.quer\
ySelectorAll(g||\
\x22*\x22):void 0;if(!\
c){c=[];for(k=a.\
childNodes||a;nu\
ll!=(q=k[b]);b++\
)!g||d.nodeName(\
q,g)?c.push(q):d\
.merge(c,E(q,g))\
}return void 0==\
=g||g&&d.nodeNam\
e(a,g)?d.merge([\
a],c):c}function\
 Xc(a){ib.test(a\
.type)&&(a.defau\
ltChecked=a.chec\
ked)}function Sb\
(a,g){return d.n\
odeName(a,\x22table\
\x22)&&d.nodeName(1\
1!==g.nodeType?g\
:g.firstChild,\x22t\
r\x22)?a.getElement\
sByTagName(\x22tbod\
y\x22)[0]||\x0aa.appen\
dChild(a.ownerDo\
cument.createEle\
ment(\x22tbody\x22)):a\
}function jb(a){\
a.type=(null!==d\
.find.attr(a,\x22ty\
pe\x22))+\x22/\x22+a.type\
;return a}functi\
on xa(a){var g=Y\
c.exec(a.type);g\
?a.type=g[1]:a.r\
emoveAttribute(\x22\
type\x22);return a}\
function F(a,g){\
for(var k,q=0;nu\
ll!=(k=a[q]);q++\
)d._data(k,\x22glob\
alEval\x22,!g||d._d\
ata(g[q],\x22global\
Eval\x22))}function\
 Tb(a,g){if(1===\
g.nodeType&&d.ha\
sData(a)){var k,\
q,b;q=d._data(a)\
;var c=d._data(g\
,q),e=q.events;i\
f(e)for(k in del\
ete c.handle,c.e\
vents={},e){q=0;\
for(b=e[k].lengt\
h;q<b;q++)d.even\
t.add(g,\x0ak,e[k][\
q])}c.data&&(c.d\
ata=d.extend({},\
c.data))}}functi\
on Ub(a,g){var k\
=d(g.createEleme\
nt(a)).appendTo(\
g.body),q=c.getD\
efaultComputedSt\
yle?c.getDefault\
ComputedStyle(k[\
0]).display:d.cs\
s(k[0],\x22display\x22\
);k.detach();ret\
urn q}function V\
b(a){var g=u,k=W\
b[a];if(!k){k=Ub\
(a,g);if(\x22none\x22=\
==k||!k)ya=(ya||\
d(\x22<iframe frame\
border='0' width\
='0' height='0'/\
>\x22)).appendTo(g.\
documentElement)\
,g=(ya[0].conten\
tWindow||ya[0].c\
ontentDocument).\
document,g.write\
(),g.close(),k=U\
b(a,g),ya.detach\
();Wb[a]=k}retur\
n k}function Xb(\
a,\x0ag){return{get\
:function(){var \
k=a();if(null!=k\
)if(k)delete thi\
s.get;else retur\
n(this.get=g).ap\
ply(this,argumen\
ts)}}}function Y\
b(a,g){if(g in a\
)return g;for(va\
r k=g.charAt(0).\
toUpperCase()+g.\
slice(1),q=g,d=Z\
b.length;d--;)if\
(g=Zb[d]+k,g in \
a)return g;retur\
n q}function $b(\
a,g){for(var k,q\
,b,c=[],e=0,f=a.\
length;e<f;e++)i\
f(q=a[e],q.style\
)if(c[e]=d._data\
(q,\x22olddisplay\x22)\
,k=q.style.displ\
ay,g)!c[e]&&\x22non\
e\x22===k&&(q.style\
.display=\x22\x22),\x22\x22=\
==q.style.displa\
y&&za(q)&&(c[e]=\
d._data(q,\x22olddi\
splay\x22,Vb(q.node\
Name)));\x0aelse if\
(!c[e]&&(b=za(q)\
,k&&\x22none\x22!==k||\
!b))d._data(q,\x22o\
lddisplay\x22,b?k:d\
.css(q,\x22display\x22\
));for(e=0;e<f;e\
++)if(q=a[e],q.s\
tyle&&(!g||\x22none\
\x22===q.style.disp\
lay||\x22\x22===q.styl\
e.display))q.sty\
le.display=g?c[e\
]||\x22\x22:\x22none\x22;ret\
urn a}function a\
c(a,g,k){return(\
a=Zc.exec(g))?Ma\
th.max(0,a[1]-(k\
||0))+(a[2]||\x22px\
\x22):g}function bc\
(a,g,k,q,b){g=k=\
==(q?\x22border\x22:\x22c\
ontent\x22)?4:\x22widt\
h\x22===g?1:0;for(v\
ar c=0;4>g;g+=2)\
\x22margin\x22===k&&(c\
+=d.css(a,k+ga[g\
],!0,b)),q?(\x22con\
tent\x22===k&&(c-=d\
.css(a,\x22padding\x22\
+ga[g],!0,b)),\x22m\
argin\x22!==k&&(c-=\
\x0ad.css(a,\x22border\
\x22+ga[g]+\x22Width\x22,\
!0,b))):(c+=d.cs\
s(a,\x22padding\x22+ga\
[g],!0,b),\x22paddi\
ng\x22!==k&&(c+=d.c\
ss(a,\x22border\x22+ga\
[g]+\x22Width\x22,!0,b\
)));return c}fun\
ction cc(a,g,k){\
var q=!0,b=\x22widt\
h\x22===g?a.offsetW\
idth:a.offsetHei\
ght,c=ha(a),e=s.\
boxSizing()&&\x22bo\
rder-box\x22===d.cs\
s(a,\x22boxSizing\x22,\
!1,c);if(0>=b||n\
ull==b){b=ia(a,g\
,c);if(0>b||null\
==b)b=a.style[g]\
;if(Ia.test(b))r\
eturn b;q=e&&(s.\
boxSizingReliabl\
e()||b===a.style\
[g]);b=parseFloa\
t(b)||0}return b\
+bc(a,g,k||(e?\x22b\
order\x22:\x22content\x22\
),q,c)+\x22px\x22}func\
tion G(a,g,k,q,b\
){return new G.p\
rototype.init(a,\
\x0ag,k,q,b)}functi\
on dc(){setTimeo\
ut(function(){pa\
=void 0});return\
 pa=d.now()}func\
tion Ja(a,g){var\
 k,q={height:a},\
b=0;for(g=g?1:0;\
4>b;b+=2-g)k=ga[\
b],q[\x22margin\x22+k]\
=q[\x22padding\x22+k]=\
a;g&&(q.opacity=\
q.width=a);retur\
n q}function ec(\
a,g,k){for(var q\
,b=(Aa[g]||[]).c\
oncat(Aa[\x22*\x22]),d\
=0,c=b.length;d<\
c;d++)if(q=b[d].\
call(k,g,a))retu\
rn q}function fc\
(a,g,k){var q,b,\
c=0,e=Ka.length,\
f=d.Deferred().a\
lways(function()\
{delete h.elem})\
,h=function(){if\
(b)return!1;for(\
var g=pa||dc(),g\
=Math.max(0,n.st\
artTime+n.durati\
on-g),\x0ak=1-(g/n.\
duration||0),q=0\
,d=n.tweens.leng\
th;q<d;q++)n.twe\
ens[q].run(k);f.\
notifyWith(a,[n,\
k,g]);if(1>k&&d)\
return g;f.resol\
veWith(a,[n]);re\
turn!1},n=f.prom\
ise({elem:a,prop\
s:d.extend({},g)\
,opts:d.extend(!\
0,{specialEasing\
:{}},k),original\
Properties:g,ori\
ginalOptions:k,s\
tartTime:pa||dc(\
),duration:k.dur\
ation,tweens:[],\
createTween:func\
tion(g,k){var q=\
d.Tween(a,n.opts\
,g,k,n.opts.spec\
ialEasing[g]||n.\
opts.easing);n.t\
weens.push(q);re\
turn q},stop:fun\
ction(g){var k=0\
,q=g?n.tweens.le\
ngth:0;if(b)retu\
rn this;for(b=\x0a!\
0;k<q;k++)n.twee\
ns[k].run(1);g?f\
.resolveWith(a,[\
n,g]):f.rejectWi\
th(a,[n,g]);retu\
rn this}});g=n.p\
rops;k=n.opts.sp\
ecialEasing;var \
j,La,l,t;for(q i\
n g)if(j=d.camel\
Case(q),La=k[j],\
l=g[q],d.isArray\
(l)&&(La=l[1],l=\
g[q]=l[0]),q!==j\
&&(g[j]=l,delete\
 g[q]),(t=d.cssH\
ooks[j])&&\x22expan\
d\x22in t)for(q in \
l=t.expand(l),de\
lete g[j],l)q in\
 g||(g[q]=l[q],k\
[q]=La);else k[j\
]=La;for(;c<e;c+\
+)if(q=Ka[c].cal\
l(n,a,g,n.opts))\
return q;d.map(g\
,ec,n);d.isFunct\
ion(n.opts.start\
)&&n.opts.start.\
call(a,n);d.fx.t\
imer(d.extend(h,\
{elem:a,\x0aanim:n,\
queue:n.opts.que\
ue}));return n.p\
rogress(n.opts.p\
rogress).done(n.\
opts.done,n.opts\
.complete).fail(\
n.opts.fail).alw\
ays(n.opts.alway\
s)}function gc(a\
){return functio\
n(g,k){\x22string\x22!\
==typeof g&&(k=g\
,g=\x22*\x22);var q,b=\
0,c=g.toLowerCas\
e().match(T)||[]\
;if(d.isFunction\
(k))for(;q=c[b++\
];)\x22+\x22===q.charA\
t(0)?(q=q.slice(\
1)||\x22*\x22,(a[q]=a[\
q]||[]).unshift(\
k)):(a[q]=a[q]||\
[]).push(k)}}fun\
ction hc(a,g,k,q\
){function b(f){\
var h;c[f]=!0;d.\
each(a[f]||[],fu\
nction(a,d){var \
f=d(g,k,q);if(\x22s\
tring\x22===typeof \
f&&!e&&!c[f])ret\
urn g.dataTypes.\
unshift(f),\x0ab(f)\
,!1;if(e)return!\
(h=f)});return h\
}var c={},e=a===\
kb;return b(g.da\
taTypes[0])||!c[\
\x22*\x22]&&b(\x22*\x22)}fun\
ction lb(a,g){va\
r k,q,b=d.ajaxSe\
ttings.flatOptio\
ns||{};for(q in \
g)void 0!==g[q]&\
&((b[q]?a:k||(k=\
{}))[q]=g[q]);k&\
&d.extend(!0,a,k\
);return a}funct\
ion mb(a,g,k,q){\
var b;if(d.isArr\
ay(g))d.each(g,f\
unction(g,b){k||\
ad.test(a)?q(a,b\
):mb(a+\x22[\x22+(\x22obj\
ect\x22===typeof b?\
g:\x22\x22)+\x22]\x22,b,k,q)\
});else if(!k&&\x22\
object\x22===d.type\
(g))for(b in g)m\
b(a+\x22[\x22+b+\x22]\x22,g[\
b],k,q);else q(a\
,g)}function nb(\
a){try{return a?\
new c.ActiveXObj\
ect(\x22Microsoft.X\
MLHTTP\x22):\x0anew c.\
XMLHttpRequest}c\
atch(g){}}functi\
on ic(){try{retu\
rn new c.XMLHttp\
Request}catch(a)\
{}}function jc(a\
){return d.isWin\
dow(a)?a:9===a.n\
odeType?a.defaul\
tView||a.parentW\
indow:!1}var V=[\
],W=V.slice,kc=V\
.concat,ob=V.pus\
h,lc=V.indexOf,M\
a={},bd=Ma.toStr\
ing,qa=Ma.hasOwn\
Property,pb=\x22\x22.t\
rim,s={},d=funct\
ion(a,g){return \
new d.fn.init(a,\
g)},cd=/^[\x5cs\x5cuFE\
FF\x5cxA0]+|[\x5cs\x5cuFE\
FF\x5cxA0]+$/g,dd=/\
^-ms-/,ed=/-([\x5cd\
a-z])/gi,fd=func\
tion(a,g){return\
 g.toUpperCase()\
};d.fn=d.prototy\
pe={jquery:\x221.11\
.0\x22,constructor:\
d,selector:\x22\x22,le\
ngth:0,\x0atoArray:\
function(){retur\
n W.call(this)},\
get:function(a){\
return null!=a?0\
>a?this[a+this.l\
ength]:this[a]:W\
.call(this)},pus\
hStack:function(\
a){a=d.merge(thi\
s.constructor(),\
a);a.prevObject=\
this;a.context=t\
his.context;retu\
rn a},each:funct\
ion(a,g){return \
d.each(this,a,g)\
},map:function(a\
){return this.pu\
shStack(d.map(th\
is,function(g,k)\
{return a.call(g\
,k,g)}))},slice:\
function(){retur\
n this.pushStack\
(W.apply(this,ar\
guments))},first\
:function(){retu\
rn this.eq(0)},l\
ast:function(){r\
eturn this.eq(-1\
)},eq:function(a\
){var g=\x0athis.le\
ngth;a=+a+(0>a?g\
:0);return this.\
pushStack(0<=a&&\
a<g?[this[a]]:[]\
)},end:function(\
){return this.pr\
evObject||this.c\
onstructor(null)\
},push:ob,sort:V\
.sort,splice:V.s\
plice};d.extend=\
d.fn.extend=func\
tion(){var a,g,k\
,b,c,e=arguments\
[0]||{},f=1,h=ar\
guments.length,n\
=!1;\x22boolean\x22===\
typeof e&&(n=e,e\
=arguments[f]||{\
},f++);\x22object\x22!\
==typeof e&&!d.i\
sFunction(e)&&(e\
={});f===h&&(e=t\
his,f--);for(;f<\
h;f++)if(null!=(\
c=arguments[f]))\
for(b in c)a=e[b\
],k=c[b],e!==k&&\
(n&&k&&(d.isPlai\
nObject(k)||(g=d\
.isArray(k)))?\x0a(\
g?(g=!1,a=a&&d.i\
sArray(a)?a:[]):\
a=a&&d.isPlainOb\
ject(a)?a:{},e[b\
]=d.extend(n,a,k\
)):void 0!==k&&(\
e[b]=k));return \
e};d.extend({exp\
ando:\x22jQuery\x22+(\x22\
1.11.0\x22+Math.ran\
dom()).replace(/\
\x5cD/g,\x22\x22),isReady\
:!0,error:functi\
on(a){throw Erro\
r(a);},noop:func\
tion(){},isFunct\
ion:function(a){\
return\x22function\x22\
===d.type(a)},is\
Array:Array.isAr\
ray||function(a)\
{return\x22array\x22==\
=d.type(a)},isWi\
ndow:function(a)\
{return null!=a&\
&a==a.window},is\
Numeric:function\
(a){return 0<=a-\
parseFloat(a)},i\
sEmptyObject:fun\
ction(a){for(var\
 g in a)return!1\
;\x0areturn!0},isPl\
ainObject:functi\
on(a){var g;if(!\
a||\x22object\x22!==d.\
type(a)||a.nodeT\
ype||d.isWindow(\
a))return!1;try{\
if(a.constructor\
&&!qa.call(a,\x22co\
nstructor\x22)&&!qa\
.call(a.construc\
tor.prototype,\x22i\
sPrototypeOf\x22))r\
eturn!1}catch(k)\
{return!1}if(s.o\
wnLast)for(g in \
a)return qa.call\
(a,g);for(g in a\
);return void 0=\
==g||qa.call(a,g\
)},type:function\
(a){return null=\
=a?a+\x22\x22:\x22object\x22\
===typeof a||\x22fu\
nction\x22===typeof\
 a?Ma[bd.call(a)\
]||\x22object\x22:type\
of a},globalEval\
:function(a){a&&\
d.trim(a)&&(c.ex\
ecScript||functi\
on(a){c.eval.cal\
l(c,\x0aa)})(a)},ca\
melCase:function\
(a){return a.rep\
lace(dd,\x22ms-\x22).r\
eplace(ed,fd)},n\
odeName:function\
(a,g){return a.n\
odeName&&a.nodeN\
ame.toLowerCase(\
)===g.toLowerCas\
e()},each:functi\
on(a,g,k){var b,\
d=0,c=a.length;b\
=h(a);if(k)if(b)\
for(;d<c&&!(b=g.\
apply(a[d],k),!1\
===b);d++);else \
for(d in a){if(b\
=g.apply(a[d],k)\
,!1===b)break}el\
se if(b)for(;d<c\
&&!(b=g.call(a[d\
],d,a[d]),!1===b\
);d++);else for(\
d in a)if(b=g.ca\
ll(a[d],d,a[d]),\
!1===b)break;ret\
urn a},trim:pb&&\
!pb.call(\x22\x5cufeff\
\x5cu00a0\x22)?functio\
n(a){return null\
==a?\x22\x22:pb.call(a\
)}:\x0afunction(a){\
return null==a?\x22\
\x22:(a+\x22\x22).replace\
(cd,\x22\x22)},makeArr\
ay:function(a,g)\
{var k=g||[];nul\
l!=a&&(h(Object(\
a))?d.merge(k,\x22s\
tring\x22===typeof \
a?[a]:a):ob.call\
(k,a));return k}\
,inArray:functio\
n(a,g,k){var b;i\
f(g){if(lc)retur\
n lc.call(g,a,k)\
;b=g.length;for(\
k=k?0>k?Math.max\
(0,b+k):k:0;k<b;\
k++)if(k in g&&g\
[k]===a)return k\
}return-1},merge\
:function(a,g){f\
or(var k=+g.leng\
th,b=0,d=a.lengt\
h;b<k;)a[d++]=g[\
b++];if(k!==k)fo\
r(;void 0!==g[b]\
;)a[d++]=g[b++];\
a.length=d;retur\
n a},grep:functi\
on(a,g,k){for(va\
r b=[],d=\x0a0,c=a.\
length,e=!k;d<c;\
d++)k=!g(a[d],d)\
,k!==e&&b.push(a\
[d]);return b},m\
ap:function(a,g,\
k){var b,d=0,c=a\
.length,e=[];if(\
h(a))for(;d<c;d+\
+)b=g(a[d],d,k),\
null!=b&&e.push(\
b);else for(d in\
 a)b=g(a[d],d,k)\
,null!=b&&e.push\
(b);return kc.ap\
ply([],e)},guid:\
1,proxy:function\
(a,g){var k,b;\x22s\
tring\x22===typeof \
g&&(b=a[g],g=a,a\
=b);if(d.isFunct\
ion(a))return k=\
W.call(arguments\
,2),b=function()\
{return a.apply(\
g||this,k.concat\
(W.call(argument\
s)))},b.guid=a.g\
uid=a.guid||d.gu\
id++,b},now:func\
tion(){return+ne\
w Date},support:\
s});\x0ad.each(\x22Boo\
lean Number Stri\
ng Function Arra\
y Date RegExp Ob\
ject Error\x22.spli\
t(\x22 \x22),function(\
a,g){Ma[\x22[object\
 \x22+g+\x22]\x22]=g.toLo\
werCase()});var \
qb=c,z=function(\
a,g,k,b){var d,c\
,e,f,h;(g?g.owne\
rDocument||g:O)!\
==H&&X(g);g=g||H\
;k=k||[];if(!a||\
\x22string\x22!==typeo\
f a)return k;if(\
1!==(f=g.nodeTyp\
e)&&9!==f)return\
[];if(S&&!b){if(\
d=gd.exec(a))if(\
e=d[1])if(9===f)\
if((c=g.getEleme\
ntById(e))&&c.pa\
rentNode){if(c.i\
d===e)return k.p\
ush(c),k}else re\
turn k;else{if(g\
.ownerDocument&&\
(c=g.ownerDocume\
nt.getElementByI\
d(e))&&Ba(g,\x0ac)&\
&c.id===e)return\
 k.push(c),k}els\
e{if(d[2])return\
 Y.apply(k,g.get\
ElementsByTagNam\
e(a)),k;if((e=d[\
3])&&x.getElemen\
tsByClassName&&g\
.getElementsByCl\
assName)return Y\
.apply(k,g.getEl\
ementsByClassNam\
e(e)),k}if(x.qsa\
&&(!I||!I.test(a\
))){c=d=C;e=g;h=\
9===f&&a;if(1===\
f&&\x22object\x22!==g.\
nodeName.toLower\
Case()){f=Na(a);\
(d=g.getAttribut\
e(\x22id\x22))?c=d.rep\
lace(hd,\x22\x5c\x5c$&\x22):\
g.setAttribute(\x22\
id\x22,c);c=\x22[id='\x22\
+c+\x22'] \x22;for(e=f\
.length;e--;)f[e\
]=c+Oa(f[e]);e=r\
b.test(a)&&sb(g.\
parentNode)||g;h\
=f.join(\x22,\x22)}if(\
h)try{return Y.a\
pply(k,\x0ae.queryS\
electorAll(h)),k\
}catch(n){}final\
ly{d||g.removeAt\
tribute(\x22id\x22)}}}\
var j;a:{a=a.rep\
lace(Pa,\x22$1\x22);c=\
Na(a);if(!b&&1==\
=c.length){d=c[0\
]=c[0].slice(0);\
if(2<d.length&&\x22\
ID\x22===(j=d[0]).t\
ype&&x.getById&&\
9===g.nodeType&&\
S&&y.relative[d[\
1].type]){g=(y.f\
ind.ID(j.matches\
[0].replace(Z,aa\
),g)||[])[0];if(\
!g){j=k;break a}\
a=a.slice(d.shif\
t().value.length\
)}for(f=Qa.needs\
Context.test(a)?\
0:d.length;f--;)\
{j=d[f];if(y.rel\
ative[e=j.type])\
break;if(e=y.fin\
d[e])if(b=e(j.ma\
tches[0].replace\
(Z,aa),rb.test(d\
[0].type)&&sb(g.\
parentNode)||\x0ag)\
){d.splice(f,1);\
a=b.length&&Oa(d\
);if(!a){Y.apply\
(k,b);j=k;break \
a}break}}}tb(a,c\
)(b,g,!S,k,rb.te\
st(a)&&sb(g.pare\
ntNode)||g);j=k}\
return j},ub=fun\
ction(){function\
 a(k,b){g.push(k\
+\x22 \x22)>y.cacheLen\
gth&&delete a[g.\
shift()];return \
a[k+\x22 \x22]=b}var g\
=[];return a},P=\
function(a){a[C]\
=!0;return a},Q=\
function(a){var \
g=H.createElemen\
t(\x22div\x22);try{ret\
urn!!a(g)}catch(\
k){return!1}fina\
lly{g.parentNode\
&&g.parentNode.r\
emoveChild(g)}},\
vb=function(a,g)\
{for(var k=a.spl\
it(\x22|\x22),b=a.leng\
th;b--;)y.attrHa\
ndle[k[b]]=g},nc\
=function(a,\x0ag){\
var k=g&&a,b=k&&\
1===a.nodeType&&\
1===g.nodeType&&\
(~g.sourceIndex|\
|mc)-(~a.sourceI\
ndex||mc);if(b)r\
eturn b;if(k)for\
(;k=k.nextSiblin\
g;)if(k===g)retu\
rn-1;return a?1:\
-1},id=function(\
a){return functi\
on(g){return\x22inp\
ut\x22===g.nodeName\
.toLowerCase()&&\
g.type===a}},jd=\
function(a){retu\
rn function(g){v\
ar k=g.nodeName.\
toLowerCase();re\
turn(\x22input\x22===k\
||\x22button\x22===k)&\
&g.type===a}},ja\
=function(a){ret\
urn P(function(g\
){g=+g;return P(\
function(k,b){fo\
r(var d,c=a([],k\
.length,g),e=c.l\
ength;e--;)if(k[\
d=c[e]])k[d]=!(b\
[d]=\x0ak[d])})})},\
sb=function(a){r\
eturn a&&typeof \
a.getElementsByT\
agName!==ra&&a},\
oc=function(){},\
Na=function(a,g)\
{var k,b,d,c,e,f\
,h;if(e=pc[a+\x22 \x22\
])return g?0:e.s\
lice(0);e=a;f=[]\
;for(h=y.preFilt\
er;e;){if(!k||(b\
=kd.exec(e)))b&&\
(e=e.slice(b[0].\
length)||e),f.pu\
sh(d=[]);k=!1;if\
(b=ld.exec(e))k=\
b.shift(),d.push\
({value:k,type:b\
[0].replace(Pa,\x22\
 \x22)}),e=e.slice(\
k.length);for(c \
in y.filter)if((\
b=Qa[c].exec(e))\
&&(!h[c]||(b=h[c\
](b))))k=b.shift\
(),d.push({value\
:k,type:c,matche\
s:b}),e=e.slice(\
k.length);if(!k)\
break}return g?\x0a\
e.length:e?z.err\
or(a):pc(a,f).sl\
ice(0)},Oa=funct\
ion(a){for(var g\
=0,k=a.length,b=\
\x22\x22;g<k;g++)b+=a[\
g].value;return \
b},wb=function(a\
,g,k){var b=g.di\
r,d=k&&\x22parentNo\
de\x22===b,c=md++;r\
eturn g.first?fu\
nction(g,k,c){fo\
r(;g=g[b];)if(1=\
==g.nodeType||d)\
return a(g,k,c)}\
:function(g,k,e)\
{var f,h,n=[R,c]\
;if(e)for(;g=g[b\
];){if((1===g.no\
deType||d)&&a(g,\
k,e))return!0}el\
se for(;g=g[b];)\
if(1===g.nodeTyp\
e||d){h=g[C]||(g\
[C]={});if((f=h[\
b])&&f[0]===R&&f\
[1]===c)return n\
[2]=f[2];h[b]=n;\
if(n[2]=a(g,k,e)\
)return!0}}},xb=\
function(a){retu\
rn 1<\x0aa.length?f\
unction(g,k,b){f\
or(var d=a.lengt\
h;d--;)if(!a[d](\
g,k,b))return!1;\
return!0}:a[0]},\
Ra=function(a,g,\
k,b,d){for(var c\
,e=[],f=0,h=a.le\
ngth,n=null!=g;f\
<h;f++)if(c=a[f]\
)if(!k||k(c,b,d)\
)e.push(c),n&&g.\
push(f);return e\
},yb=function(a,\
g,k,b,d,c){b&&!b\
[C]&&(b=yb(b));d\
&&!d[C]&&(d=yb(d\
,c));return P(fu\
nction(c,e,f,M){\
var h,n,j=[],l=[\
],t=e.length,r;i\
f(!(r=c)){r=g||\x22\
*\x22;for(var m=f.n\
odeType?[f]:f,p=\
[],B=0,s=m.lengt\
h;B<s;B++)z(r,m[\
B],p);r=p}r=a&&(\
c||!g)?Ra(r,j,a,\
f,M):r;m=k?d||(c\
?a:t||b)?[]:e:r;\
k&&k(r,m,f,\x0aM);i\
f(b){h=Ra(m,l);b\
(h,[],f,M);for(f\
=h.length;f--;)i\
f(n=h[f])m[l[f]]\
=!(r[l[f]]=n)}if\
(c){if(d||a){if(\
d){h=[];for(f=m.\
length;f--;)if(n\
=m[f])h.push(r[f\
]=n);d(null,m=[]\
,h,M)}for(f=m.le\
ngth;f--;)if((n=\
m[f])&&-1<(h=d?k\
a.call(c,n):j[f]\
))c[h]=!(e[h]=n)\
}}else m=Ra(m===\
e?m.splice(t,m.l\
ength):m),d?d(nu\
ll,e,m,M):Y.appl\
y(e,m)})},zb=fun\
ction(a){var g,k\
,b,d=a.length,c=\
y.relative[a[0].\
type];k=c||y.rel\
ative[\x22 \x22];for(v\
ar e=c?1:0,f=wb(\
function(a){retu\
rn a===g},k,!0),\
h=wb(function(a)\
{return-1<ka.cal\
l(g,a)},k,!0),n=\
[function(a,\x0ak,b\
){return!c&&(b||\
k!==Sa)||((g=k).\
nodeType?f(a,k,b\
):h(a,k,b))}];e<\
d;e++)if(k=y.rel\
ative[a[e].type]\
)n=[wb(xb(n),k)]\
;else{k=y.filter\
[a[e].type].appl\
y(null,a[e].matc\
hes);if(k[C]){fo\
r(b=++e;b<d&&!y.\
relative[a[b].ty\
pe];b++);return \
yb(1<e&&xb(n),1<\
e&&Oa(a.slice(0,\
e-1).concat({val\
ue:\x22 \x22===a[e-2].\
type?\x22*\x22:\x22\x22})).r\
eplace(Pa,\x22$1\x22),\
k,e<b&&zb(a.slic\
e(e,b)),b<d&&zb(\
a=a.slice(b)),b<\
d&&Oa(a))}n.push\
(k)}return xb(n)\
},sa,x,y,Ta,qc,t\
b,Sa,ba,ta,X,H,U\
,S,I,la,Ua,Ba,C=\
\x22sizzle\x22+-new Da\
te,O=qb.document\
,R=0,md=0,rc=ub(\
),\x0apc=ub(),sc=ub\
(),Ab=function(a\
,g){a===g&&(ta=!\
0);return 0},ra=\
\x22undefined\x22,mc=-\
2147483648,nd={}\
.hasOwnProperty,\
ca=[],od=ca.pop,\
pd=ca.push,Y=ca.\
push,tc=ca.slice\
,ka=ca.indexOf||\
function(a){for(\
var g=0,k=this.l\
ength;g<k;g++)if\
(this[g]===a)ret\
urn g;return-1},\
uc=\x22(?:\x5c\x5c\x5c\x5c.|[\x5c\x5c\
w-]|[^\x5c\x5cx00-\x5c\x5cxa\
0])+\x22.replace(\x22w\
\x22,\x22w#\x22),vc=\x22\x5c\x5c[[\
\x5c\x5cx20\x5c\x5ct\x5c\x5cr\x5c\x5cn\x5c\x5c\
f]*((?:\x5c\x5c\x5c\x5c.|[\x5c\x5c\
w-]|[^\x5c\x5cx00-\x5c\x5cxa\
0])+)[\x5c\x5cx20\x5c\x5ct\x5c\x5c\
r\x5c\x5cn\x5c\x5cf]*(?:([*^\
$|!~]?=)[\x5c\x5cx20\x5c\x5c\
t\x5c\x5cr\x5c\x5cn\x5c\x5cf]*(?:(\
['\x5c\x22])((?:\x5c\x5c\x5c\x5c.|\
[^\x5c\x5c\x5c\x5c])*?)\x5c\x5c3|(\
\x22+uc+\x22)|)|)[\x5c\x5cx2\
0\x5c\x5ct\x5c\x5cr\x5c\x5cn\x5c\x5cf]*\x5c\
\x5c]\x22,Bb=\x22:((?:\x5c\x5c\x5c\
\x5c.|[\x5c\x5cw-]|[^\x5c\x5cx0\
0-\x5c\x5cxa0])+)(?:\x5c\x5c\
(((['\x5c\x22])((?:\x5c\x5c\x5c\
\x5c.|[^\x5c\x5c\x5c\x5c])*?)\x5c\x5c\
3|((?:\x5c\x5c\x5c\x5c.|[^\x5c\x5c\
\x5c\x5c()[\x5c\x5c]]|\x22+\x0avc.\
replace(3,8)+\x22)*\
)|.*)\x5c\x5c)|)\x22,Pa=R\
egExp(\x22^[\x5c\x5cx20\x5c\x5c\
t\x5c\x5cr\x5c\x5cn\x5c\x5cf]+|((?\
:^|[^\x5c\x5c\x5c\x5c])(?:\x5c\x5c\
\x5c\x5c.)*)[\x5c\x5cx20\x5c\x5ct\x5c\
\x5cr\x5c\x5cn\x5c\x5cf]+$\x22,\x22g\x22\
),kd=/^[\x5cx20\x5ct\x5cr\
\x5cn\x5cf]*,[\x5cx20\x5ct\x5cr\
\x5cn\x5cf]*/,ld=/^[\x5cx\
20\x5ct\x5cr\x5cn\x5cf]*([>+\
~]|[\x5cx20\x5ct\x5cr\x5cn\x5cf\
])[\x5cx20\x5ct\x5cr\x5cn\x5cf]\
*/,qd=RegExp(\x22=[\
\x5c\x5cx20\x5c\x5ct\x5c\x5cr\x5c\x5cn\x5c\x5c\
f]*([^\x5c\x5c]'\x5c\x22]*?)\
[\x5c\x5cx20\x5c\x5ct\x5c\x5cr\x5c\x5cn\x5c\
\x5cf]*\x5c\x5c]\x22,\x22g\x22),rd\
=RegExp(Bb),sd=R\
egExp(\x22^\x22+uc+\x22$\x22\
),Qa={ID:/^#((?:\
\x5c\x5c.|[\x5cw-]|[^\x5cx00\
-\x5cxa0])+)/,CLASS\
:/^\x5c.((?:\x5c\x5c.|[\x5cw\
-]|[^\x5cx00-\x5cxa0])\
+)/,TAG:RegExp(\x22\
^(\x22+\x22(?:\x5c\x5c\x5c\x5c.|[\x5c\
\x5cw-]|[^\x5c\x5cx00-\x5c\x5cx\
a0])+\x22.replace(\x22\
w\x22,\x22w*\x22)+\x22)\x22),AT\
TR:RegExp(\x22^\x22+vc\
),\x0aPSEUDO:RegExp\
(\x22^\x22+Bb),CHILD:R\
egExp(\x22^:(only|f\
irst|last|nth|nt\
h-last)-(child|o\
f-type)(?:\x5c\x5c([\x5c\x5c\
x20\x5c\x5ct\x5c\x5cr\x5c\x5cn\x5c\x5cf]\
*(even|odd|(([+-\
]|)(\x5c\x5cd*)n|)[\x5c\x5cx\
20\x5c\x5ct\x5c\x5cr\x5c\x5cn\x5c\x5cf]*\
(?:([+-]|)[\x5c\x5cx20\
\x5c\x5ct\x5c\x5cr\x5c\x5cn\x5c\x5cf]*(\x5c\
\x5cd+)|))[\x5c\x5cx20\x5c\x5ct\
\x5c\x5cr\x5c\x5cn\x5c\x5cf]*\x5c\x5c)|)\
\x22,\x22i\x22),bool:RegE\
xp(\x22^(?:checked|\
selected|async|a\
utofocus|autopla\
y|controls|defer\
|disabled|hidden\
|ismap|loop|mult\
iple|open|readon\
ly|required|scop\
ed)$\x22,\x22i\x22),needs\
Context:RegExp(\x22\
^[\x5c\x5cx20\x5c\x5ct\x5c\x5cr\x5c\x5cn\
\x5c\x5cf]*[>+~]|:(eve\
n|odd|eq|gt|lt|n\
th|first|last)(?\
:\x5c\x5c([\x5c\x5cx20\x5c\x5ct\x5c\x5cr\
\x5c\x5cn\x5c\x5cf]*((?:-\x5c\x5cd\
)?\x5c\x5cd*)[\x5c\x5cx20\x5c\x5ct\
\x5c\x5cr\x5c\x5cn\x5c\x5cf]*\x5c\x5c)|)\
(?=[^-]|$)\x22,\x0a\x22i\x22\
)},td=/^(?:input\
|select|textarea\
|button)$/i,ud=/\
^h\x5cd$/i,Ca=/^[^{\
]+\x5c{\x5cs*\x5c[native \
\x5cw/,gd=/^(?:#([\x5c\
w-]+)|(\x5cw+)|\x5c.([\
\x5cw-]+))$/,rb=/[+\
~]/,hd=/'|\x5c\x5c/g,Z\
=RegExp(\x22\x5c\x5c\x5c\x5c([\x5c\
\x5cda-f]{1,6}[\x5c\x5cx2\
0\x5c\x5ct\x5c\x5cr\x5c\x5cn\x5c\x5cf]?|\
([\x5c\x5cx20\x5c\x5ct\x5c\x5cr\x5c\x5cn\
\x5c\x5cf])|.)\x22,\x22ig\x22),\
aa=function(a,g,\
k){a=\x220x\x22+g-6553\
6;return a!==a||\
k?g:0>a?String.f\
romCharCode(a+65\
536):String.from\
CharCode(a>>10|5\
5296,a&1023|5632\
0)};try{Y.apply(\
ca=tc.call(O.chi\
ldNodes),O.child\
Nodes),ca[O.chil\
dNodes.length].n\
odeType}catch(ae\
){Y={apply:ca.le\
ngth?function(a,\
g){pd.apply(a,tc\
.call(g))}:\x0afunc\
tion(a,g){for(va\
r k=a.length,b=0\
;a[k++]=g[b++];)\
;a.length=k-1}}}\
x=z.support={};q\
c=z.isXML=functi\
on(a){return(a=a\
&&(a.ownerDocume\
nt||a).documentE\
lement)?\x22HTML\x22!=\
=a.nodeName:!1};\
X=z.setDocument=\
function(a){var \
g=a?a.ownerDocum\
ent||a:O;a=g.def\
aultView;if(g===\
H||9!==g.nodeTyp\
e||!g.documentEl\
ement)return H;H\
=g;U=g.documentE\
lement;S=!qc(g);\
a&&a!==a.top&&(a\
.addEventListene\
r?a.addEventList\
ener(\x22unload\x22,fu\
nction(){X()},!1\
):a.attachEvent&\
&a.attachEvent(\x22\
onunload\x22,functi\
on(){X()}));x.at\
tributes=Q(funct\
ion(a){a.classNa\
me=\x0a\x22i\x22;return!a\
.getAttribute(\x22c\
lassName\x22)});x.g\
etElementsByTagN\
ame=Q(function(a\
){a.appendChild(\
g.createComment(\
\x22\x22));return!a.ge\
tElementsByTagNa\
me(\x22*\x22).length})\
;x.getElementsBy\
ClassName=Ca.tes\
t(g.getElementsB\
yClassName)&&Q(f\
unction(a){a.inn\
erHTML=\x22<div cla\
ss='a'></div><di\
v class='a i'></\
div>\x22;a.firstChi\
ld.className=\x22i\x22\
;return 2===a.ge\
tElementsByClass\
Name(\x22i\x22).length\
});x.getById=Q(f\
unction(a){U.app\
endChild(a).id=C\
;return!g.getEle\
mentsByName||!g.\
getElementsByNam\
e(C).length});x.\
getById?(y.find.\
ID=function(a,\x0ag\
){if(typeof g.ge\
tElementById!==r\
a&&S){var b=g.ge\
tElementById(a);\
return b&&b.pare\
ntNode?[b]:[]}},\
y.filter.ID=func\
tion(a){var g=a.\
replace(Z,aa);re\
turn function(a)\
{return a.getAtt\
ribute(\x22id\x22)===g\
}}):(delete y.fi\
nd.ID,y.filter.I\
D=function(a){va\
r g=a.replace(Z,\
aa);return funct\
ion(a){return(a=\
typeof a.getAttr\
ibuteNode!==ra&&\
a.getAttributeNo\
de(\x22id\x22))&&a.val\
ue===g}});y.find\
.TAG=x.getElemen\
tsByTagName?func\
tion(a,g){if(typ\
eof g.getElement\
sByTagName!==ra)\
return g.getElem\
entsByTagName(a)\
}:function(a,g){\
var b,\x0ad=[],c=0,\
e=g.getElementsB\
yTagName(a);if(\x22\
*\x22===a){for(;b=e\
[c++];)1===b.nod\
eType&&d.push(b)\
;return d}return\
 e};y.find.CLASS\
=x.getElementsBy\
ClassName&&funct\
ion(a,g){if(type\
of g.getElements\
ByClassName!==ra\
&&S)return g.get\
ElementsByClassN\
ame(a)};la=[];I=\
[];if(x.qsa=Ca.t\
est(g.querySelec\
torAll))Q(functi\
on(a){a.innerHTM\
L=\x22<select t=''>\
<option selected\
=''></option></s\
elect>\x22;a.queryS\
electorAll(\x22[t^=\
'']\x22).length&&I.\
push(\x22[*^$]=[\x5c\x5cx\
20\x5c\x5ct\x5c\x5cr\x5c\x5cn\x5c\x5cf]*\
(?:''|\x5c\x22\x5c\x22)\x22);a.\
querySelectorAll\
(\x22[selected]\x22).l\
ength||I.push(\x22\x5c\
\x5c[[\x5c\x5cx20\x5c\x5ct\x5c\x5cr\x5c\x5c\
n\x5c\x5cf]*(?:value|c\
hecked|selected|\
async|autofocus|\
autoplay|control\
s|defer|disabled\
|hidden|ismap|lo\
op|multiple|open\
|readonly|requir\
ed|scoped)\x22);\x0aa.\
querySelectorAll\
(\x22:checked\x22).len\
gth||I.push(\x22:ch\
ecked\x22)}),Q(func\
tion(a){var b=g.\
createElement(\x22i\
nput\x22);b.setAttr\
ibute(\x22type\x22,\x22hi\
dden\x22);a.appendC\
hild(b).setAttri\
bute(\x22name\x22,\x22D\x22)\
;a.querySelector\
All(\x22[name=d]\x22).\
length&&I.push(\x22\
name[\x5c\x5cx20\x5c\x5ct\x5c\x5cr\
\x5c\x5cn\x5c\x5cf]*[*^$|!~]\
?=\x22);a.querySele\
ctorAll(\x22:enable\
d\x22).length||I.pu\
sh(\x22:enabled\x22,\x22:\
disabled\x22);a.que\
rySelectorAll(\x22*\
,:x\x22);I.push(\x22,.\
*:\x22)});(x.matche\
sSelector=Ca.tes\
t(Ua=U.webkitMat\
chesSelector||U.\
mozMatchesSelect\
or||U.oMatchesSe\
lector||U.msMatc\
hesSelector))&&Q\
(function(a){x.d\
isconnectedMatch\
=\x0aUa.call(a,\x22div\
\x22);Ua.call(a,\x22[s\
!='']:x\x22);la.pus\
h(\x22!=\x22,Bb)});I=I\
.length&&RegExp(\
I.join(\x22|\x22));la=\
la.length&&RegEx\
p(la.join(\x22|\x22));\
Ba=(a=Ca.test(U.\
compareDocumentP\
osition))||Ca.te\
st(U.contains)?f\
unction(a,g){var\
 b=9===a.nodeTyp\
e?a.documentElem\
ent:a,d=g&&g.par\
entNode;return a\
===d||!(!d||!(1=\
==d.nodeType&&(b\
.contains?b.cont\
ains(d):a.compar\
eDocumentPositio\
n&&a.compareDocu\
mentPosition(d)&\
16)))}:function(\
a,g){if(g)for(;g\
=g.parentNode;)i\
f(g===a)return!0\
;return!1};Ab=a?\
function(a,b){if\
(a===b)return ta\
=!0,0;var d=\x0a!a.\
compareDocumentP\
osition-!b.compa\
reDocumentPositi\
on;if(d)return d\
;d=(a.ownerDocum\
ent||a)===(b.own\
erDocument||b)?a\
.compareDocument\
Position(b):1;re\
turn d&1||!x.sor\
tDetached&&b.com\
pareDocumentPosi\
tion(a)===d?a===\
g||a.ownerDocume\
nt===O&&Ba(O,a)?\
-1:b===g||b.owne\
rDocument===O&&B\
a(O,b)?1:ba?ka.c\
all(ba,a)-ka.cal\
l(ba,b):0:d&4?-1\
:1}:function(a,b\
){if(a===b)retur\
n ta=!0,0;var d,\
c=0;d=a.parentNo\
de;var e=b.paren\
tNode,f=[a],h=[b\
];if(!d||!e)retu\
rn a===g?-1:b===\
g?1:d?-1:e?1:ba?\
ka.call(ba,a)-ka\
.call(ba,b):0;if\
(d===\x0ae)return n\
c(a,b);for(d=a;d\
=d.parentNode;)f\
.unshift(d);for(\
d=b;d=d.parentNo\
de;)h.unshift(d)\
;for(;f[c]===h[c\
];)c++;return c?\
nc(f[c],h[c]):f[\
c]===O?-1:h[c]==\
=O?1:0};return g\
};z.matches=func\
tion(a,g){return\
 z(a,null,null,g\
)};z.matchesSele\
ctor=function(a,\
g){(a.ownerDocum\
ent||a)!==H&&X(a\
);g=g.replace(qd\
,\x22='$1']\x22);if(x.\
matchesSelector&\
&S&&(!la||!la.te\
st(g))&&(!I||!I.\
test(g)))try{var\
 k=Ua.call(a,g);\
if(k||x.disconne\
ctedMatch||a.doc\
ument&&11!==a.do\
cument.nodeType)\
return k}catch(b\
){}return 0<z(g,\
H,null,[a]).leng\
th};\x0az.contains=\
function(a,g){(a\
.ownerDocument||\
a)!==H&&X(a);ret\
urn Ba(a,g)};z.a\
ttr=function(a,g\
){(a.ownerDocume\
nt||a)!==H&&X(a)\
;var k=y.attrHan\
dle[g.toLowerCas\
e()],k=k&&nd.cal\
l(y.attrHandle,g\
.toLowerCase())?\
k(a,g,!S):void 0\
;return void 0!=\
=k?k:x.attribute\
s||!S?a.getAttri\
bute(g):(k=a.get\
AttributeNode(g)\
)&&k.specified?k\
.value:null};z.e\
rror=function(a)\
{throw Error(\x22Sy\
ntax error, unre\
cognized express\
ion: \x22+a);};z.un\
iqueSort=functio\
n(a){var g,k=[],\
b=0,d=0;ta=!x.de\
tectDuplicates;b\
a=!x.sortStable&\
&a.slice(0);\x0aa.s\
ort(Ab);if(ta){f\
or(;g=a[d++];)g=\
==a[d]&&(b=k.pus\
h(d));for(;b--;)\
a.splice(k[b],1)\
}ba=null;return \
a};Ta=z.getText=\
function(a){var \
g,k=\x22\x22,b=0;if(g=\
a.nodeType)if(1=\
==g||9===g||11==\
=g){if(\x22string\x22=\
==typeof a.textC\
ontent)return a.\
textContent;for(\
a=a.firstChild;a\
;a=a.nextSibling\
)k+=Ta(a)}else{i\
f(3===g||4===g)r\
eturn a.nodeValu\
e}else for(;g=a[\
b++];)k+=Ta(g);r\
eturn k};y=z.sel\
ectors={cacheLen\
gth:50,createPse\
udo:P,match:Qa,a\
ttrHandle:{},fin\
d:{},relative:{\x22\
>\x22:{dir:\x22parentN\
ode\x22,first:!0},\x22\
 \x22:{dir:\x22parentN\
ode\x22},\x0a\x22+\x22:{dir:\
\x22previousSibling\
\x22,first:!0},\x22~\x22:\
{dir:\x22previousSi\
bling\x22}},preFilt\
er:{ATTR:functio\
n(a){a[1]=a[1].r\
eplace(Z,aa);a[3\
]=(a[4]||a[5]||\x22\
\x22).replace(Z,aa)\
;\x22~=\x22===a[2]&&(a\
[3]=\x22 \x22+a[3]+\x22 \x22\
);return a.slice\
(0,4)},CHILD:fun\
ction(a){a[1]=a[\
1].toLowerCase()\
;\x22nth\x22===a[1].sl\
ice(0,3)?(a[3]||\
z.error(a[0]),a[\
4]=+(a[4]?a[5]+(\
a[6]||1):2*(\x22eve\
n\x22===a[3]||\x22odd\x22\
===a[3])),a[5]=+\
(a[7]+a[8]||\x22odd\
\x22===a[3])):a[3]&\
&z.error(a[0]);r\
eturn a},PSEUDO:\
function(a){var \
g,k=!a[5]&&a[2];\
if(Qa.CHILD.test\
(a[0]))return nu\
ll;if(a[3]&&\x0avoi\
d 0!==a[4])a[2]=\
a[4];else if(k&&\
rd.test(k)&&(g=N\
a(k,!0))&&(g=k.i\
ndexOf(\x22)\x22,k.len\
gth-g)-k.length)\
)a[0]=a[0].slice\
(0,g),a[2]=k.sli\
ce(0,g);return a\
.slice(0,3)}},fi\
lter:{TAG:functi\
on(a){var g=a.re\
place(Z,aa).toLo\
werCase();return\
\x22*\x22===a?function\
(){return!0}:fun\
ction(a){return \
a.nodeName&&a.no\
deName.toLowerCa\
se()===g}},CLASS\
:function(a){var\
 g=rc[a+\x22 \x22];ret\
urn g||(g=RegExp\
(\x22(^|[\x5c\x5cx20\x5c\x5ct\x5c\x5c\
r\x5c\x5cn\x5c\x5cf])\x22+a+\x22([\
\x5c\x5cx20\x5c\x5ct\x5c\x5cr\x5c\x5cn\x5c\x5c\
f]|$)\x22))&&rc(a,f\
unction(a){retur\
n g.test(\x22string\
\x22===typeof a.cla\
ssName&&a.classN\
ame||\x0atypeof a.g\
etAttribute!==ra\
&&a.getAttribute\
(\x22class\x22)||\x22\x22)})\
},ATTR:function(\
a,g,k){return fu\
nction(b){b=z.at\
tr(b,a);if(null=\
=b)return\x22!=\x22===\
g;if(!g)return!0\
;b+=\x22\x22;return\x22=\x22\
===g?b===k:\x22!=\x22=\
==g?b!==k:\x22^=\x22==\
=g?k&&0===b.inde\
xOf(k):\x22*=\x22===g?\
k&&-1<b.indexOf(\
k):\x22$=\x22===g?k&&b\
.slice(-k.length\
)===k:\x22~=\x22===g?-\
1<(\x22 \x22+b+\x22 \x22).in\
dexOf(k):\x22|=\x22===\
g?b===k||b.slice\
(0,k.length+1)==\
=k+\x22-\x22:!1}},CHIL\
D:function(a,g,k\
,b,d){var c=\x22nth\
\x22!==a.slice(0,3)\
,e=\x22last\x22!==a.sl\
ice(-4),f=\x22of-ty\
pe\x22===g;return 1\
===b&&0===d?func\
tion(a){return!!\
a.parentNode}:\x0af\
unction(g,k,h){v\
ar n,j,l,t,r;k=c\
!==e?\x22nextSiblin\
g\x22:\x22previousSibl\
ing\x22;var m=g.par\
entNode,p=f&&g.n\
odeName.toLowerC\
ase();h=!h&&!f;i\
f(m){if(c){for(;\
k;){for(j=g;j=j[\
k];)if(f?j.nodeN\
ame.toLowerCase(\
)===p:1===j.node\
Type)return!1;r=\
k=\x22only\x22===a&&!r\
&&\x22nextSibling\x22}\
return!0}r=[e?m.\
firstChild:m.las\
tChild];if(e&&h)\
{h=m[C]||(m[C]={\
});n=h[a]||[];t=\
n[0]===R&&n[1];l\
=n[0]===R&&n[2];\
for(j=t&&m.child\
Nodes[t];j=++t&&\
j&&j[k]||(l=t=0)\
||r.pop();)if(1=\
==j.nodeType&&++\
l&&j===g){h[a]=[\
R,t,l];break}}el\
se if(h&&(n=(g[C\
]||(g[C]=\x0a{}))[a\
])&&n[0]===R)l=n\
[1];else for(;j=\
++t&&j&&j[k]||(l\
=t=0)||r.pop();)\
if((f?j.nodeName\
.toLowerCase()==\
=p:1===j.nodeTyp\
e)&&++l)if(h&&((\
j[C]||(j[C]={}))\
[a]=[R,l]),j===g\
)break;l-=d;retu\
rn l===b||0===l%\
b&&0<=l/b}}},PSE\
UDO:function(a,g\
){var k,b=y.pseu\
dos[a]||y.setFil\
ters[a.toLowerCa\
se()]||z.error(\x22\
unsupported pseu\
do: \x22+a);return \
b[C]?b(g):1<b.le\
ngth?(k=[a,a,\x22\x22,\
g],y.setFilters.\
hasOwnProperty(a\
.toLowerCase())?\
P(function(a,k){\
for(var d,c=b(a,\
g),e=c.length;e-\
-;)d=ka.call(a,c\
[e]),a[d]=!(k[d]\
=c[e])}):functio\
n(a){return b(a,\
\x0a0,k)}):b}},pseu\
dos:{not:P(funct\
ion(a){var g=[],\
k=[],b=tb(a.repl\
ace(Pa,\x22$1\x22));re\
turn b[C]?P(func\
tion(a,g,k,d){d=\
b(a,null,d,[]);f\
or(var c=a.lengt\
h;c--;)if(k=d[c]\
)a[c]=!(g[c]=k)}\
):function(a,d,c\
){g[0]=a;b(g,nul\
l,c,k);return!k.\
pop()}}),has:P(f\
unction(a){retur\
n function(g){re\
turn 0<z(a,g).le\
ngth}}),contains\
:P(function(a){r\
eturn function(g\
){return-1<(g.te\
xtContent||g.inn\
erText||Ta(g)).i\
ndexOf(a)}}),lan\
g:P(function(a){\
sd.test(a||\x22\x22)||\
z.error(\x22unsuppo\
rted lang: \x22+a);\
a=a.replace(Z,aa\
).toLowerCase();\
return function(\
g){var k;\x0ado if(\
k=S?g.lang:g.get\
Attribute(\x22xml:l\
ang\x22)||g.getAttr\
ibute(\x22lang\x22))re\
turn k=k.toLower\
Case(),k===a||0=\
==k.indexOf(a+\x22-\
\x22);while((g=g.pa\
rentNode)&&1===g\
.nodeType);retur\
n!1}}),target:fu\
nction(a){var g=\
qb.location&&qb.\
location.hash;re\
turn g&&g.slice(\
1)===a.id},root:\
function(a){retu\
rn a===U},focus:\
function(a){retu\
rn a===H.activeE\
lement&&(!H.hasF\
ocus||H.hasFocus\
())&&!(!a.type&&\
!a.href&&!~a.tab\
Index)},enabled:\
function(a){retu\
rn!1===a.disable\
d},disabled:func\
tion(a){return!0\
===a.disabled},c\
hecked:function(\
a){var g=\x0aa.node\
Name.toLowerCase\
();return\x22input\x22\
===g&&!!a.checke\
d||\x22option\x22===g&\
&!!a.selected},s\
elected:function\
(a){a.parentNode\
&&a.parentNode.s\
electedIndex;ret\
urn!0===a.select\
ed},empty:functi\
on(a){for(a=a.fi\
rstChild;a;a=a.n\
extSibling)if(6>\
a.nodeType)retur\
n!1;return!0},pa\
rent:function(a)\
{return!y.pseudo\
s.empty(a)},head\
er:function(a){r\
eturn ud.test(a.\
nodeName)},input\
:function(a){ret\
urn td.test(a.no\
deName)},button:\
function(a){var \
g=a.nodeName.toL\
owerCase();retur\
n\x22input\x22===g&&\x22b\
utton\x22===a.type|\
|\x22button\x22===g},\x0a\
text:function(a)\
{var g;return\x22in\
put\x22===a.nodeNam\
e.toLowerCase()&\
&\x22text\x22===a.type\
&&(null==(g=a.ge\
tAttribute(\x22type\
\x22))||\x22text\x22===g.\
toLowerCase())},\
first:ja(functio\
n(){return[0]}),\
last:ja(function\
(a,g){return[g-1\
]}),eq:ja(functi\
on(a,g,k){return\
[0>k?k+g:k]}),ev\
en:ja(function(a\
,g){for(var k=0;\
k<g;k+=2)a.push(\
k);return a}),od\
d:ja(function(a,\
g){for(var k=1;k\
<g;k+=2)a.push(k\
);return a}),lt:\
ja(function(a,g,\
k){for(g=0>k?k+g\
:k;0<=--g;)a.pus\
h(g);return a}),\
gt:ja(function(a\
,g,k){for(k=0>k?\
k+g:k;++k<g;)a.p\
ush(k);\x0areturn a\
})}};y.pseudos.n\
th=y.pseudos.eq;\
for(sa in{radio:\
!0,checkbox:!0,f\
ile:!0,password:\
!0,image:!0})y.p\
seudos[sa]=id(sa\
);for(sa in{subm\
it:!0,reset:!0})\
y.pseudos[sa]=jd\
(sa);oc.prototyp\
e=y.filters=y.ps\
eudos;y.setFilte\
rs=new oc;tb=z.c\
ompile=function(\
a,g){var k,b=[],\
d=[],c=sc[a+\x22 \x22]\
;if(!c){g||(g=Na\
(a));for(k=g.len\
gth;k--;)c=zb(g[\
k]),c[C]?b.push(\
c):d.push(c);var\
 e=0<b.length,f=\
0<d.length;k=fun\
ction(a,g,k,c,M)\
{var h,n,j,l=0,t\
=\x220\x22,r=a&&[],m=[\
],p=Sa,B=a||f&&y\
.find.TAG(\x22*\x22,M)\
,s=R+=null==p?1:\
Math.random()||\x0a\
0.1,E=B.length;f\
or(M&&(Sa=g!==H&\
&g);t!==E&&null!\
=(h=B[t]);t++){i\
f(f&&h){for(n=0;\
j=d[n++];)if(j(h\
,g,k)){c.push(h)\
;break}M&&(R=s)}\
e&&((h=!j&&h)&&l\
--,a&&r.push(h))\
}l+=t;if(e&&t!==\
l){for(n=0;j=b[n\
++];)j(r,m,g,k);\
if(a){if(0<l)for\
(;t--;)!r[t]&&!m\
[t]&&(m[t]=od.ca\
ll(c));m=Ra(m)}Y\
.apply(c,m);M&&(\
!a&&0<m.length&&\
1<l+b.length)&&z\
.uniqueSort(c)}M\
&&(R=s,Sa=p);ret\
urn r};k=e?P(k):\
k;c=sc(a,k)}retu\
rn c};x.sortStab\
le=C.split(\x22\x22).s\
ort(Ab).join(\x22\x22)\
===C;x.detectDup\
licates=!!ta;X()\
;x.sortDetached=\
Q(function(a){re\
turn a.compareDo\
cumentPosition(H\
.createElement(\x22\
div\x22))&\x0a1});Q(fu\
nction(a){a.inne\
rHTML=\x22<a href='\
#'></a>\x22;return\x22\
#\x22===a.firstChil\
d.getAttribute(\x22\
href\x22)})||vb(\x22ty\
pe|href|height|w\
idth\x22,function(a\
,g,k){if(!k)retu\
rn a.getAttribut\
e(g,\x22type\x22===g.t\
oLowerCase()?1:2\
)});(!x.attribut\
es||!Q(function(\
a){a.innerHTML=\x22\
<input/>\x22;a.firs\
tChild.setAttrib\
ute(\x22value\x22,\x22\x22);\
return\x22\x22===a.fir\
stChild.getAttri\
bute(\x22value\x22)}))\
&&vb(\x22value\x22,fun\
ction(a,g,k){if(\
!k&&\x22input\x22===a.\
nodeName.toLower\
Case())return a.\
defaultValue});Q\
(function(a){ret\
urn null==a.getA\
ttribute(\x22disabl\
ed\x22)})||vb(\x22chec\
ked|selected|asy\
nc|autofocus|aut\
oplay|controls|d\
efer|disabled|hi\
dden|ismap|loop|\
multiple|open|re\
adonly|required|\
scoped\x22,\x0afunctio\
n(a,g,k){var b;i\
f(!k)return!0===\
a[g]?g.toLowerCa\
se():(b=a.getAtt\
ributeNode(g))&&\
b.specified?b.va\
lue:null});d.fin\
d=z;d.expr=z.sel\
ectors;d.expr[\x22:\
\x22]=d.expr.pseudo\
s;d.unique=z.uni\
queSort;d.text=z\
.getText;d.isXML\
Doc=z.isXML;d.co\
ntains=z.contain\
s;var wc=d.expr.\
match.needsConte\
xt,xc=/^<(\x5cw+)\x5cs\
*\x5c/?>(?:<\x5c/\x5c1>|)\
$/,Uc=/^.[^:#\x5c[\x5c\
.,]*$/;d.filter=\
function(a,g,k){\
var b=g[0];k&&(a\
=\x22:not(\x22+a+\x22)\x22);\
return 1===g.len\
gth&&1===b.nodeT\
ype?d.find.match\
esSelector(b,a)?\
[b]:[]:d.find.ma\
tches(a,d.grep(g\
,function(a){ret\
urn 1===\x0aa.nodeT\
ype}))};d.fn.ext\
end({find:functi\
on(a){var g,k=[]\
,b=this,c=b.leng\
th;if(\x22string\x22!=\
=typeof a)return\
 this.pushStack(\
d(a).filter(func\
tion(){for(g=0;g\
<c;g++)if(d.cont\
ains(b[g],this))\
return!0}));for(\
g=0;g<c;g++)d.fi\
nd(a,b[g],k);k=t\
his.pushStack(1<\
c?d.unique(k):k)\
;k.selector=this\
.selector?this.s\
elector+\x22 \x22+a:a;\
return k},filter\
:function(a){ret\
urn this.pushSta\
ck(j(this,a||[],\
!1))},not:functi\
on(a){return thi\
s.pushStack(j(th\
is,a||[],!0))},i\
s:function(a){re\
turn!!j(this,\x22st\
ring\x22===typeof a\
&&wc.test(a)?d(a\
):\x0aa||[],!1).len\
gth}});var Da,u=\
c.document,vd=/^\
(?:\x5cs*(<[\x5cw\x5cW]+>\
)[^>]*|#([\x5cw-]*)\
)$/;(d.fn.init=f\
unction(a,g){var\
 k,b;if(!a)retur\
n this;if(\x22strin\
g\x22===typeof a){i\
f((k=\x22<\x22===a.cha\
rAt(0)&&\x22>\x22===a.\
charAt(a.length-\
1)&&3<=a.length?\
[null,a,null]:vd\
.exec(a))&&(k[1]\
||!g)){if(k[1]){\
if(g=g instanceo\
f d?g[0]:g,d.mer\
ge(this,d.parseH\
TML(k[1],g&&g.no\
deType?g.ownerDo\
cument||g:u,!0))\
,xc.test(k[1])&&\
d.isPlainObject(\
g))for(k in g)if\
(d.isFunction(th\
is[k]))this[k](g\
[k]);else this.a\
ttr(k,g[k])}else\
{if((b=u.getElem\
entById(k[2]))&&\
\x0ab.parentNode){i\
f(b.id!==k[2])re\
turn Da.find(a);\
this.length=1;th\
is[0]=b}this.con\
text=u;this.sele\
ctor=a}return th\
is}return!g||g.j\
query?(g||Da).fi\
nd(a):this.const\
ructor(g).find(a\
)}if(a.nodeType)\
return this.cont\
ext=this[0]=a,th\
is.length=1,this\
;if(d.isFunction\
(a))return\x22undef\
ined\x22!==typeof D\
a.ready?Da.ready\
(a):a(d);void 0!\
==a.selector&&(t\
his.selector=a.s\
elector,this.con\
text=a.context);\
return d.makeArr\
ay(a,this)}).pro\
totype=d.fn;Da=d\
(u);var wd=/^(?:\
parents|prev(?:U\
ntil|All))/,xd={\
children:!0,cont\
ents:!0,\x0anext:!0\
,prev:!0};d.exte\
nd({dir:function\
(a,g,k){var b=[]\
;for(a=a[g];a&&9\
!==a.nodeType&&(\
void 0===k||1!==\
a.nodeType||!d(a\
).is(k));)1===a.\
nodeType&&b.push\
(a),a=a[g];retur\
n b},sibling:fun\
ction(a,g){for(v\
ar k=[];a;a=a.ne\
xtSibling)1===a.\
nodeType&&a!==g&\
&k.push(a);retur\
n k}});d.fn.exte\
nd({has:function\
(a){var g,k=d(a,\
this),b=k.length\
;return this.fil\
ter(function(){f\
or(g=0;g<b;g++)i\
f(d.contains(thi\
s,k[g]))return!0\
})},closest:func\
tion(a,g){for(va\
r k,b=0,c=this.l\
ength,e=[],f=wc.\
test(a)||\x22string\
\x22!==typeof a?d(a\
,\x0ag||this.contex\
t):0;b<c;b++)for\
(k=this[b];k&&k!\
==g;k=k.parentNo\
de)if(11>k.nodeT\
ype&&(f?-1<f.ind\
ex(k):1===k.node\
Type&&d.find.mat\
chesSelector(k,a\
))){e.push(k);br\
eak}return this.\
pushStack(1<e.le\
ngth?d.unique(e)\
:e)},index:funct\
ion(a){return!a?\
this[0]&&this[0]\
.parentNode?this\
.first().prevAll\
().length:-1:\x22st\
ring\x22===typeof a\
?d.inArray(this[\
0],d(a)):d.inArr\
ay(a.jquery?a[0]\
:a,this)},add:fu\
nction(a,g){retu\
rn this.pushStac\
k(d.unique(d.mer\
ge(this.get(),d(\
a,g))))},addBack\
:function(a){ret\
urn this.add(nul\
l==a?this.prevOb\
ject:\x0athis.prevO\
bject.filter(a))\
}});d.each({pare\
nt:function(a){r\
eturn(a=a.parent\
Node)&&11!==a.no\
deType?a:null},p\
arents:function(\
a){return d.dir(\
a,\x22parentNode\x22)}\
,parentsUntil:fu\
nction(a,g,k){re\
turn d.dir(a,\x22pa\
rentNode\x22,k)},ne\
xt:function(a){r\
eturn l(a,\x22nextS\
ibling\x22)},prev:f\
unction(a){retur\
n l(a,\x22previousS\
ibling\x22)},nextAl\
l:function(a){re\
turn d.dir(a,\x22ne\
xtSibling\x22)},pre\
vAll:function(a)\
{return d.dir(a,\
\x22previousSibling\
\x22)},nextUntil:fu\
nction(a,g,k){re\
turn d.dir(a,\x22ne\
xtSibling\x22,k)},p\
revUntil:functio\
n(a,g,k){return \
d.dir(a,\x0a\x22previo\
usSibling\x22,k)},s\
iblings:function\
(a){return d.sib\
ling((a.parentNo\
de||{}).firstChi\
ld,a)},children:\
function(a){retu\
rn d.sibling(a.f\
irstChild)},cont\
ents:function(a)\
{return d.nodeNa\
me(a,\x22iframe\x22)?a\
.contentDocument\
||a.contentWindo\
w.document:d.mer\
ge([],a.childNod\
es)}},function(a\
,g){d.fn[a]=func\
tion(k,b){var c=\
d.map(this,g,k);\
\x22Until\x22!==a.slic\
e(-5)&&(b=k);b&&\
\x22string\x22===typeo\
f b&&(c=d.filter\
(b,c));1<this.le\
ngth&&(xd[a]||(c\
=d.unique(c)),wd\
.test(a)&&(c=c.r\
everse()));retur\
n this.pushStack\
(c)}});var T=/\x5cS\
+/g,\x0ayc={};d.Cal\
lbacks=function(\
a){var g;if(\x22str\
ing\x22===typeof a)\
{if(!(g=yc[a])){\
g=a;var k=yc[g]=\
{};d.each(g.matc\
h(T)||[],functio\
n(a,g){k[g]=!0})\
;g=k}}else g=d.e\
xtend({},a);a=g;\
var b,c,e,f,h,n,\
j=[],l=!a.once&&\
[],t=function(g)\
{c=a.memory&&g;e\
=!0;h=n||0;n=0;f\
=j.length;for(b=\
!0;j&&h<f;h++)if\
(!1===j[h].apply\
(g[0],g[1])&&a.s\
topOnFalse){c=!1\
;break}b=!1;j&&(\
l?l.length&&t(l.\
shift()):c?j=[]:\
m.disable())},m=\
{add:function(){\
if(j){var g=j.le\
ngth;(function $\
c(g){d.each(g,fu\
nction(g,b){var \
k=d.type(b);\x22fun\
ction\x22===k?\x0a(!a.\
unique||!m.has(b\
))&&j.push(b):b&\
&(b.length&&\x22str\
ing\x22!==k)&&$c(b)\
})})(arguments);\
b?f=j.length:c&&\
(n=g,t(c))}retur\
n this},remove:f\
unction(){j&&d.e\
ach(arguments,fu\
nction(a,g){for(\
var k;-1<(k=d.in\
Array(g,j,k));)j\
.splice(k,1),b&&\
(k<=f&&f--,k<=h&\
&h--)});return t\
his},has:functio\
n(a){return a?-1\
<d.inArray(a,j):\
!(!j||!j.length)\
},empty:function\
(){j=[];f=0;retu\
rn this},disable\
:function(){j=l=\
c=void 0;return \
this},disabled:f\
unction(){return\
!j},lock:functio\
n(){l=void 0;c||\
m.disable();retu\
rn this},locked:\
function(){retur\
n!l},\x0afireWith:f\
unction(a,g){if(\
j&&(!e||l))g=g||\
[],g=[a,g.slice?\
g.slice():g],b?l\
.push(g):t(g);re\
turn this},fire:\
function(){m.fir\
eWith(this,argum\
ents);return thi\
s},fired:functio\
n(){return!!e}};\
return m};d.exte\
nd({Deferred:fun\
ction(a){var g=[\
[\x22resolve\x22,\x22done\
\x22,d.Callbacks(\x22o\
nce memory\x22),\x22re\
solved\x22],[\x22rejec\
t\x22,\x22fail\x22,d.Call\
backs(\x22once memo\
ry\x22),\x22rejected\x22]\
,[\x22notify\x22,\x22prog\
ress\x22,d.Callback\
s(\x22memory\x22)]],b=\
\x22pending\x22,c={sta\
te:function(){re\
turn b},always:f\
unction(){e.done\
(arguments).fail\
(arguments);retu\
rn this},then:fu\
nction(){var a=\x0a\
arguments;return\
 d.Deferred(func\
tion(b){d.each(g\
,function(g,k){v\
ar f=d.isFunctio\
n(a[g])&&a[g];e[\
k[1]](function()\
{var a=f&&f.appl\
y(this,arguments\
);if(a&&d.isFunc\
tion(a.promise))\
a.promise().done\
(b.resolve).fail\
(b.reject).progr\
ess(b.notify);el\
se b[k[0]+\x22With\x22\
](this===c?b.pro\
mise():this,f?[a\
]:arguments)})})\
;a=null}).promis\
e()},promise:fun\
ction(a){return \
null!=a?d.extend\
(a,c):c}},e={};c\
.pipe=c.then;d.e\
ach(g,function(a\
,d){var f=d[2],h\
=d[3];c[d[1]]=f.\
add;h&&f.add(fun\
ction(){b=h},g[a\
^1][2].disable,g\
[2][2].lock);\x0ae[\
d[0]]=function()\
{e[d[0]+\x22With\x22](\
this===e?c:this,\
arguments);retur\
n this};e[d[0]+\x22\
With\x22]=f.fireWit\
h});c.promise(e)\
;a&&a.call(e,e);\
return e},when:f\
unction(a){var g\
=0,b=W.call(argu\
ments),c=b.lengt\
h,e=1!==c||a&&d.\
isFunction(a.pro\
mise)?c:0,f=1===\
e?a:d.Deferred()\
,h=function(a,g,\
b){return functi\
on(k){g[a]=this;\
b[a]=1<arguments\
.length?W.call(a\
rguments):k;b===\
n?f.notifyWith(g\
,b):--e||f.resol\
veWith(g,b)}},n,\
j,l;if(1<c){n=Ar\
ray(c);j=Array(c\
);for(l=Array(c)\
;g<c;g++)b[g]&&d\
.isFunction(b[g]\
.promise)?b[g].p\
romise().done(h(\
g,\x0al,b)).fail(f.\
reject).progress\
(h(g,j,n)):--e}e\
||f.resolveWith(\
l,b);return f.pr\
omise()}});var V\
a;d.fn.ready=fun\
ction(a){d.ready\
.promise().done(\
a);return this};\
d.extend({isRead\
y:!1,readyWait:1\
,holdReady:funct\
ion(a){a?d.ready\
Wait++:d.ready(!\
0)},ready:functi\
on(a){if(!(!0===\
a?--d.readyWait:\
d.isReady)){if(!\
u.body)return se\
tTimeout(d.ready\
);d.isReady=!0;!\
0!==a&&0<--d.rea\
dyWait||(Va.reso\
lveWith(u,[d]),d\
.fn.trigger&&d(u\
).trigger(\x22ready\
\x22).off(\x22ready\x22))\
}}});d.ready.pro\
mise=function(a)\
{if(!Va)if(Va=d.\
Deferred(),\x0a\x22com\
plete\x22===u.ready\
State)setTimeout\
(d.ready);else i\
f(u.addEventList\
ener)u.addEventL\
istener(\x22DOMCont\
entLoaded\x22,p,!1)\
,c.addEventListe\
ner(\x22load\x22,p,!1)\
;else{u.attachEv\
ent(\x22onreadystat\
echange\x22,p);c.at\
tachEvent(\x22onloa\
d\x22,p);var g=!1;t\
ry{g=null==c.fra\
meElement&&u.doc\
umentElement}cat\
ch(b){}g&&g.doSc\
roll&&function K\
(){if(!d.isReady\
){try{g.doScroll\
(\x22left\x22)}catch(a\
){return setTime\
out(K,50)}r();d.\
ready()}}()}retu\
rn Va.promise(a)\
};var N=\x22undefin\
ed\x22,zc;for(zc in\
 d(s))break;s.ow\
nLast=\x220\x22!==zc;s\
.inlineBlockNeed\
sLayout=\x0a!1;d(fu\
nction(){var a,g\
,b=u.getElements\
ByTagName(\x22body\x22\
)[0];if(b){a=u.c\
reateElement(\x22di\
v\x22);a.style.cssT\
ext=\x22border:0;wi\
dth:0;height:0;p\
osition:absolute\
;top:0;left:-999\
9px;margin-top:1\
px\x22;g=u.createEl\
ement(\x22div\x22);b.a\
ppendChild(a).ap\
pendChild(g);if(\
typeof g.style.z\
oom!==N&&(g.styl\
e.cssText=\x22borde\
r:0;margin:0;wid\
th:1px;padding:1\
px;display:inlin\
e;zoom:1\x22,s.inli\
neBlockNeedsLayo\
ut=3===g.offsetW\
idth))b.style.zo\
om=1;b.removeChi\
ld(a)}});var yd=\
u.createElement(\
\x22div\x22);if(null==\
s.deleteExpando)\
{s.deleteExpando\
=\x0a!0;try{delete \
yd.test}catch(be\
){s.deleteExpand\
o=!1}}d.acceptDa\
ta=function(a){v\
ar g=d.noData[(a\
.nodeName+\x22 \x22).t\
oLowerCase()],b=\
+a.nodeType||1;r\
eturn 1!==b&&9!=\
=b?!1:!g||!0!==g\
&&a.getAttribute\
(\x22classid\x22)===g}\
;var Wc=/^(?:\x5c{[\
\x5cw\x5cW]*\x5c}|\x5c[[\x5cw\x5cW\
]*\x5c])$/,Vc=/([A-\
Z])/g;d.extend({\
cache:{},noData:\
{\x22applet \x22:!0,\x22e\
mbed \x22:!0,\x22objec\
t \x22:\x22clsid:D27CD\
B6E-AE6D-11cf-96\
B8-444553540000\x22\
},hasData:functi\
on(a){a=a.nodeTy\
pe?d.cache[a[d.e\
xpando]]:a[d.exp\
ando];return!!a&\
&!w(a)},data:fun\
ction(a,g,k){ret\
urn b(a,g,k)},re\
moveData:functio\
n(a,\x0ag){return e\
(a,g)},_data:fun\
ction(a,g,k){ret\
urn b(a,g,k,!0)}\
,_removeData:fun\
ction(a,g){retur\
n e(a,g,!0)}});d\
.fn.extend({data\
:function(a,g){v\
ar b,c,e,f=this[\
0],h=f&&f.attrib\
utes;if(void 0==\
=a){if(this.leng\
th&&(e=d.data(f)\
,1===f.nodeType&\
&!d._data(f,\x22par\
sedAttrs\x22))){for\
(b=h.length;b--;\
)c=h[b].name,0==\
=c.indexOf(\x22data\
-\x22)&&(c=d.camelC\
ase(c.slice(5)),\
v(f,c,e[c]));d._\
data(f,\x22parsedAt\
trs\x22,!0)}return \
e}return\x22object\x22\
===typeof a?this\
.each(function()\
{d.data(this,a)}\
):1<arguments.le\
ngth?this.each(f\
unction(){d.data\
(this,\x0aa,g)}):f?\
v(f,a,d.data(f,a\
)):void 0},remov\
eData:function(a\
){return this.ea\
ch(function(){d.\
removeData(this,\
a)})}});d.extend\
({queue:function\
(a,g,b){var c;if\
(a)return g=(g||\
\x22fx\x22)+\x22queue\x22,c=\
d._data(a,g),b&&\
(!c||d.isArray(b\
)?c=d._data(a,g,\
d.makeArray(b)):\
c.push(b)),c||[]\
},dequeue:functi\
on(a,g){g=g||\x22fx\
\x22;var b=d.queue(\
a,g),c=b.length,\
e=b.shift(),f=d.\
_queueHooks(a,g)\
,h=function(){d.\
dequeue(a,g)};\x22i\
nprogress\x22===e&&\
(e=b.shift(),c--\
);e&&(\x22fx\x22===g&&\
b.unshift(\x22inpro\
gress\x22),delete f\
.stop,e.call(a,h\
,f));!c&&f&&\x0af.e\
mpty.fire()},_qu\
eueHooks:functio\
n(a,g){var b=g+\x22\
queueHooks\x22;retu\
rn d._data(a,b)|\
|d._data(a,b,{em\
pty:d.Callbacks(\
\x22once memory\x22).a\
dd(function(){d.\
_removeData(a,g+\
\x22queue\x22);d._remo\
veData(a,b)})})}\
});d.fn.extend({\
queue:function(a\
,g){var b=2;\x22str\
ing\x22!==typeof a&\
&(g=a,a=\x22fx\x22,b--\
);return argumen\
ts.length<b?d.qu\
eue(this[0],a):v\
oid 0===g?this:t\
his.each(functio\
n(){var b=d.queu\
e(this,a,g);d._q\
ueueHooks(this,a\
);\x22fx\x22===a&&\x22inp\
rogress\x22!==b[0]&\
&d.dequeue(this,\
a)})},dequeue:fu\
nction(a){return\
 this.each(funct\
ion(){d.dequeue(\
this,\x0aa)})},clea\
rQueue:function(\
a){return this.q\
ueue(a||\x22fx\x22,[])\
},promise:functi\
on(a,g){var b,c=\
1,e=d.Deferred()\
,f=this,h=this.l\
ength,n=function\
(){--c||e.resolv\
eWith(f,[f])};\x22s\
tring\x22!==typeof \
a&&(g=a,a=void 0\
);for(a=a||\x22fx\x22;\
h--;)if((b=d._da\
ta(f[h],a+\x22queue\
Hooks\x22))&&b.empt\
y)c++,b.empty.ad\
d(n);n();return \
e.promise(g)}});\
var Wa=/[+-]?(?:\
\x5cd*\x5c.|)\x5cd+(?:[eE\
][+-]?\x5cd+|)/.sou\
rce,ga=[\x22Top\x22,\x22R\
ight\x22,\x22Bottom\x22,\x22\
Left\x22],za=functi\
on(a,g){a=g||a;r\
eturn\x22none\x22===d.\
css(a,\x22display\x22)\
||!d.contains(a.\
ownerDocument,a)\
},ma=d.access=\x0af\
unction(a,g,b,c,\
e,f,h){var n=0,j\
=a.length,l=null\
==b;if(\x22object\x22=\
==d.type(b))for(\
n in e=!0,b)d.ac\
cess(a,g,n,b[n],\
!0,f,h);else if(\
void 0!==c&&(e=!\
0,d.isFunction(c\
)||(h=!0),l&&(h?\
(g.call(a,c),g=n\
ull):(l=g,g=func\
tion(a,g,b){retu\
rn l.call(d(a),b\
)})),g))for(;n<j\
;n++)g(a[n],b,h?\
c:c.call(a[n],n,\
g(a[n],b)));retu\
rn e?a:l?g.call(\
a):j?g(a[0],b):f\
},ib=/^(?:checkb\
ox|radio)$/i,Cb=\
u.createDocument\
Fragment(),D=u.c\
reateElement(\x22di\
v\x22),Ea=u.createE\
lement(\x22input\x22);\
D.setAttribute(\x22\
className\x22,\x22t\x22);\
D.innerHTML=\x22  <\
link/><table></t\
able><a href='/a\
'>a</a>\x22;\x0as.lead\
ingWhitespace=3=\
==D.firstChild.n\
odeType;s.tbody=\
!D.getElementsBy\
TagName(\x22tbody\x22)\
.length;s.htmlSe\
rialize=!!D.getE\
lementsByTagName\
(\x22link\x22).length;\
s.html5Clone=\x22<:\
nav></:nav>\x22!==u\
.createElement(\x22\
nav\x22).cloneNode(\
!0).outerHTML;Ea\
.type=\x22checkbox\x22\
;Ea.checked=!0;C\
b.appendChild(Ea\
);s.appendChecke\
d=Ea.checked;D.i\
nnerHTML=\x22<texta\
rea>x</textarea>\
\x22;s.noCloneCheck\
ed=!!D.cloneNode\
(!0).lastChild.d\
efaultValue;Cb.a\
ppendChild(D);D.\
innerHTML=\x22<inpu\
t type='radio' c\
hecked='checked'\
 name='t'/>\x22;s.c\
heckClone=D.clon\
eNode(!0).cloneN\
ode(!0).lastChil\
d.checked;\x0as.noC\
loneEvent=!0;D.a\
ttachEvent&&(D.a\
ttachEvent(\x22oncl\
ick\x22,function(){\
s.noCloneEvent=!\
1}),D.cloneNode(\
!0).click());if(\
null==s.deleteEx\
pando){s.deleteE\
xpando=!0;try{de\
lete D.test}catc\
h(ce){s.deleteEx\
pando=!1}}var Cb\
=D=Ea=null,Xa,Ya\
,Ac=u.createElem\
ent(\x22div\x22);for(X\
a in{submit:!0,c\
hange:!0,focusin\
:!0})if(Ya=\x22on\x22+\
Xa,!(s[Xa+\x22Bubbl\
es\x22]=Ya in c))Ac\
.setAttribute(Ya\
,\x22t\x22),s[Xa+\x22Bubb\
les\x22]=!1===Ac.at\
tributes[Ya].exp\
ando;var Db=/^(?\
:input|select|te\
xtarea)$/i,zd=/^\
key/,Ad=/^(?:mou\
se|contextmenu)|\
click/,Bc=/^(?:f\
ocusinfocus|focu\
soutblur)$/,\x0aCc=\
/^([^.]*)(?:\x5c.(.\
+)|)$/;d.event={\
global:{},add:fu\
nction(a,g,b,c,e\
){var f,h,n,j,l,\
t,m,r,p;if(n=d._\
data(a)){b.handl\
er&&(j=b,b=j.han\
dler,e=j.selecto\
r);b.guid||(b.gu\
id=d.guid++);if(\
!(h=n.events))h=\
n.events={};if(!\
(l=n.handle))l=n\
.handle=function\
(a){return typeo\
f d!==N&&(!a||d.\
event.triggered!\
==a.type)?d.even\
t.dispatch.apply\
(l.elem,argument\
s):void 0},l.ele\
m=a;g=(g||\x22\x22).ma\
tch(T)||[\x22\x22];for\
(n=g.length;n--;\
)if(f=Cc.exec(g[\
n])||[],r=t=f[1]\
,p=(f[2]||\x22\x22).sp\
lit(\x22.\x22).sort(),\
r){f=d.event.spe\
cial[r]||{};r=(e\
?f.delegateType:\
\x0af.bindType)||r;\
f=d.event.specia\
l[r]||{};t=d.ext\
end({type:r,orig\
Type:t,data:c,ha\
ndler:b,guid:b.g\
uid,selector:e,n\
eedsContext:e&&d\
.expr.match.need\
sContext.test(e)\
,namespace:p.joi\
n(\x22.\x22)},j);if(!(\
m=h[r]))if(m=h[r\
]=[],m.delegateC\
ount=0,!f.setup|\
|!1===f.setup.ca\
ll(a,c,p,l))a.ad\
dEventListener?a\
.addEventListene\
r(r,l,!1):a.atta\
chEvent&&a.attac\
hEvent(\x22on\x22+r,l)\
;f.add&&(f.add.c\
all(a,t),t.handl\
er.guid||(t.hand\
ler.guid=b.guid)\
);e?m.splice(m.d\
elegateCount++,0\
,t):m.push(t);d.\
event.global[r]=\
!0}a=null}},remo\
ve:function(a,\x0ag\
,b,c,e){var f,h,\
n,j,l,t,m,r,p,B,\
s,E=d.hasData(a)\
&&d._data(a);if(\
E&&(t=E.events))\
{g=(g||\x22\x22).match\
(T)||[\x22\x22];for(l=\
g.length;l--;)if\
(n=Cc.exec(g[l])\
||[],p=s=n[1],B=\
(n[2]||\x22\x22).split\
(\x22.\x22).sort(),p){\
m=d.event.specia\
l[p]||{};p=(c?m.\
delegateType:m.b\
indType)||p;r=t[\
p]||[];n=n[2]&&R\
egExp(\x22(^|\x5c\x5c.)\x22+\
B.join(\x22\x5c\x5c.(?:.*\
\x5c\x5c.|)\x22)+\x22(\x5c\x5c.|$)\
\x22);for(j=f=r.len\
gth;f--;)if(h=r[\
f],(e||s===h.ori\
gType)&&(!b||b.g\
uid===h.guid)&&(\
!n||n.test(h.nam\
espace))&&(!c||c\
===h.selector||\x22\
**\x22===c&&h.selec\
tor))r.splice(f,\
1),h.selector&&r\
.delegateCount--\
,\x0am.remove&&m.re\
move.call(a,h);j\
&&!r.length&&((!\
m.teardown||!1==\
=m.teardown.call\
(a,B,E.handle))&\
&d.removeEvent(a\
,p,E.handle),del\
ete t[p])}else f\
or(p in t)d.even\
t.remove(a,p+g[l\
],b,c,!0);d.isEm\
ptyObject(t)&&(d\
elete E.handle,d\
._removeData(a,\x22\
events\x22))}},trig\
ger:function(a,g\
,b,e){var f,h,n,\
j,l,t,m=[b||u],r\
=qa.call(a,\x22type\
\x22)?a.type:a;l=qa\
.call(a,\x22namespa\
ce\x22)?a.namespace\
.split(\x22.\x22):[];n\
=f=b=b||u;if(!(3\
===b.nodeType||8\
===b.nodeType)&&\
!Bc.test(r+d.eve\
nt.triggered))if\
(0<=r.indexOf(\x22.\
\x22)&&(l=r.split(\x22\
.\x22),r=l.shift(),\
\x0al.sort()),h=0>r\
.indexOf(\x22:\x22)&&\x22\
on\x22+r,a=a[d.expa\
ndo]?a:new d.Eve\
nt(r,\x22object\x22===\
typeof a&&a),a.i\
sTrigger=e?2:3,a\
.namespace=l.joi\
n(\x22.\x22),a.namespa\
ce_re=a.namespac\
e?RegExp(\x22(^|\x5c\x5c.\
)\x22+l.join(\x22\x5c\x5c.(?\
:.*\x5c\x5c.|)\x22)+\x22(\x5c\x5c.\
|$)\x22):null,a.res\
ult=void 0,a.tar\
get||(a.target=b\
),g=null==g?[a]:\
d.makeArray(g,[a\
]),l=d.event.spe\
cial[r]||{},e||!\
(l.trigger&&!1==\
=l.trigger.apply\
(b,g))){if(!e&&!\
l.noBubble&&!d.i\
sWindow(b)){j=l.\
delegateType||r;\
Bc.test(j+r)||(n\
=n.parentNode);f\
or(;n;n=n.parent\
Node)m.push(n),f\
=n;if(f===(b.own\
erDocument||\x0au))\
m.push(f.default\
View||f.parentWi\
ndow||c)}for(t=0\
;(n=m[t++])&&!a.\
isPropagationSto\
pped();)if(a.typ\
e=1<t?j:l.bindTy\
pe||r,(f=(d._dat\
a(n,\x22events\x22)||{\
})[a.type]&&d._d\
ata(n,\x22handle\x22))\
&&f.apply(n,g),(\
f=h&&n[h])&&f.ap\
ply&&d.acceptDat\
a(n))a.result=f.\
apply(n,g),!1===\
a.result&&a.prev\
entDefault();a.t\
ype=r;if(!e&&!a.\
isDefaultPrevent\
ed()&&(!l._defau\
lt||!1===l._defa\
ult.apply(m.pop(\
),g))&&d.acceptD\
ata(b)&&h&&b[r]&\
&!d.isWindow(b))\
{(f=b[h])&&(b[h]\
=null);d.event.t\
riggered=r;try{b\
[r]()}catch(p){}\
d.event.triggere\
d=\x0avoid 0;f&&(b[\
h]=f)}return a.r\
esult}},dispatch\
:function(a){a=d\
.event.fix(a);va\
r g,b,c,e,f=[],h\
=W.call(argument\
s);g=(d._data(th\
is,\x22events\x22)||{}\
)[a.type]||[];va\
r n=d.event.spec\
ial[a.type]||{};\
h[0]=a;a.delegat\
eTarget=this;if(\
!(n.preDispatch&\
&!1===n.preDispa\
tch.call(this,a)\
)){f=d.event.han\
dlers.call(this,\
a,g);for(g=0;(c=\
f[g++])&&!a.isPr\
opagationStopped\
();){a.currentTa\
rget=c.elem;for(\
e=0;(b=c.handler\
s[e++])&&!a.isIm\
mediatePropagati\
onStopped();)if(\
!a.namespace_re|\
|a.namespace_re.\
test(b.namespace\
))if(a.handleObj\
=\x0ab,a.data=b.dat\
a,b=((d.event.sp\
ecial[b.origType\
]||{}).handle||b\
.handler).apply(\
c.elem,h),void 0\
!==b&&!1===(a.re\
sult=b))a.preven\
tDefault(),a.sto\
pPropagation()}n\
.postDispatch&&n\
.postDispatch.ca\
ll(this,a);retur\
n a.result}},han\
dlers:function(a\
,g){var b,c,e,f,\
h=[],n=g.delegat\
eCount,j=a.targe\
t;if(n&&j.nodeTy\
pe&&(!a.button||\
\x22click\x22!==a.type\
))for(;j!=this;j\
=j.parentNode||t\
his)if(1===j.nod\
eType&&(!0!==j.d\
isabled||\x22click\x22\
!==a.type)){e=[]\
;for(f=0;f<n;f++\
)c=g[f],b=c.sele\
ctor+\x22 \x22,void 0=\
==e[b]&&(e[b]=c.\
needsContext?\x0a0<\
=d(b,this).index\
(j):d.find(b,thi\
s,null,[j]).leng\
th),e[b]&&e.push\
(c);e.length&&h.\
push({elem:j,han\
dlers:e})}n<g.le\
ngth&&h.push({el\
em:this,handlers\
:g.slice(n)});re\
turn h},fix:func\
tion(a){if(a[d.e\
xpando])return a\
;var g,b,c;g=a.t\
ype;var e=a,f=th\
is.fixHooks[g];f\
||(this.fixHooks\
[g]=f=Ad.test(g)\
?this.mouseHooks\
:zd.test(g)?this\
.keyHooks:{});c=\
f.props?this.pro\
ps.concat(f.prop\
s):this.props;a=\
new d.Event(e);f\
or(g=c.length;g-\
-;)b=c[g],a[b]=e\
[b];a.target||(a\
.target=e.srcEle\
ment||u);3===a.t\
arget.nodeType&&\
(a.target=\x0aa.tar\
get.parentNode);\
a.metaKey=!!a.me\
taKey;return f.f\
ilter?f.filter(a\
,e):a},props:\x22al\
tKey bubbles can\
celable ctrlKey \
currentTarget ev\
entPhase metaKey\
 relatedTarget s\
hiftKey target t\
imeStamp view wh\
ich\x22.split(\x22 \x22),\
fixHooks:{},keyH\
ooks:{props:[\x22ch\
ar\x22,\x22charCode\x22,\x22\
key\x22,\x22keyCode\x22],\
filter:function(\
a,g){null==a.whi\
ch&&(a.which=nul\
l!=g.charCode?g.\
charCode:g.keyCo\
de);return a}},m\
ouseHooks:{props\
:\x22button buttons\
 clientX clientY\
 fromElement off\
setX offsetY pag\
eX pageY screenX\
 screenY toEleme\
nt\x22.split(\x22 \x22),f\
ilter:function(a\
,\x0ag){var b,d,c=g\
.button,e=g.from\
Element;null==a.\
pageX&&null!=g.c\
lientX&&(b=a.tar\
get.ownerDocumen\
t||u,d=b.documen\
tElement,b=b.bod\
y,a.pageX=g.clie\
ntX+(d&&d.scroll\
Left||b&&b.scrol\
lLeft||0)-(d&&d.\
clientLeft||b&&b\
.clientLeft||0),\
a.pageY=g.client\
Y+(d&&d.scrollTo\
p||b&&b.scrollTo\
p||0)-(d&&d.clie\
ntTop||b&&b.clie\
ntTop||0));!a.re\
latedTarget&&e&&\
(a.relatedTarget\
=e===a.target?g.\
toElement:e);!a.\
which&&void 0!==\
c&&(a.which=c&1?\
1:c&2?3:c&4?2:0)\
;return a}},spec\
ial:{load:{noBub\
ble:!0},focus:{t\
rigger:function(\
){if(this!==\x0at()\
&&this.focus)try\
{return this.foc\
us(),!1}catch(a)\
{}},delegateType\
:\x22focusin\x22},blur\
:{trigger:functi\
on(){if(this===t\
()&&this.blur)re\
turn this.blur()\
,!1},delegateTyp\
e:\x22focusout\x22},cl\
ick:{trigger:fun\
ction(){if(d.nod\
eName(this,\x22inpu\
t\x22)&&\x22checkbox\x22=\
==this.type&&thi\
s.click)return t\
his.click(),!1},\
_default:functio\
n(a){return d.no\
deName(a.target,\
\x22a\x22)}},beforeunl\
oad:{postDispatc\
h:function(a){vo\
id 0!==a.result&\
&(a.originalEven\
t.returnValue=a.\
result)}}},simul\
ate:function(a,g\
,b,c){a=d.extend\
(new d.Event,b,{\
type:a,\x0aisSimula\
ted:!0,originalE\
vent:{}});c?d.ev\
ent.trigger(a,nu\
ll,g):d.event.di\
spatch.call(g,a)\
;a.isDefaultPrev\
ented()&&b.preve\
ntDefault()}};d.\
removeEvent=u.re\
moveEventListene\
r?function(a,g,b\
){a.removeEventL\
istener&&a.remov\
eEventListener(g\
,b,!1)}:function\
(a,g,b){g=\x22on\x22+g\
;a.detachEvent&&\
(typeof a[g]===N\
&&(a[g]=null),a.\
detachEvent(g,b)\
)};d.Event=funct\
ion(a,g){if(!(th\
is instanceof d.\
Event))return ne\
w d.Event(a,g);a\
&&a.type?(this.o\
riginalEvent=a,t\
his.type=a.type,\
this.isDefaultPr\
evented=a.defaul\
tPrevented||void\
 0===\x0aa.defaultP\
revented&&(!1===\
a.returnValue||a\
.getPreventDefau\
lt&&a.getPrevent\
Default())?f:n):\
this.type=a;g&&d\
.extend(this,g);\
this.timeStamp=a\
&&a.timeStamp||d\
.now();this[d.ex\
pando]=!0};d.Eve\
nt.prototype={is\
DefaultPrevented\
:n,isPropagation\
Stopped:n,isImme\
diatePropagation\
Stopped:n,preven\
tDefault:functio\
n(){var a=this.o\
riginalEvent;thi\
s.isDefaultPreve\
nted=f;a&&(a.pre\
ventDefault?a.pr\
eventDefault():a\
.returnValue=!1)\
},stopPropagatio\
n:function(){var\
 a=this.original\
Event;this.isPro\
pagationStopped=\
f;a&&(a.stopProp\
agation&&\x0aa.stop\
Propagation(),a.\
cancelBubble=!0)\
},stopImmediateP\
ropagation:funct\
ion(){this.isImm\
ediatePropagatio\
nStopped=f;this.\
stopPropagation(\
)}};d.each({mous\
eenter:\x22mouseove\
r\x22,mouseleave:\x22m\
ouseout\x22},functi\
on(a,g){d.event.\
special[a]={dele\
gateType:g,bindT\
ype:g,handle:fun\
ction(a){var b,c\
=a.relatedTarget\
,e=a.handleObj;i\
f(!c||c!==this&&\
!d.contains(this\
,c))a.type=e.ori\
gType,b=e.handle\
r.apply(this,arg\
uments),a.type=g\
;return b}}});s.\
submitBubbles||(\
d.event.special.\
submit={setup:fu\
nction(){if(d.no\
deName(this,\x22for\
m\x22))return!1;\x0ad.\
event.add(this,\x22\
click._submit ke\
ypress._submit\x22,\
function(a){a=a.\
target;if((a=d.n\
odeName(a,\x22input\
\x22)||d.nodeName(a\
,\x22button\x22)?a.for\
m:void 0)&&!d._d\
ata(a,\x22submitBub\
bles\x22))d.event.a\
dd(a,\x22submit._su\
bmit\x22,function(a\
){a._submit_bubb\
le=!0}),d._data(\
a,\x22submitBubbles\
\x22,!0)})},postDis\
patch:function(a\
){a._submit_bubb\
le&&(delete a._s\
ubmit_bubble,thi\
s.parentNode&&!a\
.isTrigger&&d.ev\
ent.simulate(\x22su\
bmit\x22,this.paren\
tNode,a,!0))},te\
ardown:function(\
){if(d.nodeName(\
this,\x22form\x22))ret\
urn!1;d.event.re\
move(this,\x22._sub\
mit\x22)}});\x0as.chan\
geBubbles||(d.ev\
ent.special.chan\
ge={setup:functi\
on(){if(Db.test(\
this.nodeName)){\
if(\x22checkbox\x22===\
this.type||\x22radi\
o\x22===this.type)d\
.event.add(this,\
\x22propertychange.\
_change\x22,functio\
n(a){\x22checked\x22==\
=a.originalEvent\
.propertyName&&(\
this._just_chang\
ed=!0)}),d.event\
.add(this,\x22click\
._change\x22,functi\
on(a){this._just\
_changed&&!a.isT\
rigger&&(this._j\
ust_changed=!1);\
d.event.simulate\
(\x22change\x22,this,a\
,!0)});return!1}\
d.event.add(this\
,\x22beforeactivate\
._change\x22,functi\
on(a){a=a.target\
;Db.test(a.nodeN\
ame)&&!d._data(a\
,\x0a\x22changeBubbles\
\x22)&&(d.event.add\
(a,\x22change._chan\
ge\x22,function(a){\
this.parentNode&\
&(!a.isSimulated\
&&!a.isTrigger)&\
&d.event.simulat\
e(\x22change\x22,this.\
parentNode,a,!0)\
}),d._data(a,\x22ch\
angeBubbles\x22,!0)\
)})},handle:func\
tion(a){var g=a.\
target;if(this!=\
=g||a.isSimulate\
d||a.isTrigger||\
\x22radio\x22!==g.type\
&&\x22checkbox\x22!==g\
.type)return a.h\
andleObj.handler\
.apply(this,argu\
ments)},teardown\
:function(){d.ev\
ent.remove(this,\
\x22._change\x22);retu\
rn!Db.test(this.\
nodeName)}});s.f\
ocusinBubbles||d\
.each({focus:\x22fo\
cusin\x22,blur:\x22foc\
usout\x22},\x0afunctio\
n(a,g){var b=fun\
ction(a){d.event\
.simulate(g,a.ta\
rget,d.event.fix\
(a),!0)};d.event\
.special[g]={set\
up:function(){va\
r c=this.ownerDo\
cument||this,e=d\
._data(c,g);e||c\
.addEventListene\
r(a,b,!0);d._dat\
a(c,g,(e||0)+1)}\
,teardown:functi\
on(){var c=this.\
ownerDocument||t\
his,e=d._data(c,\
g)-1;e?d._data(c\
,g,e):(c.removeE\
ventListener(a,b\
,!0),d._removeDa\
ta(c,g))}}});d.f\
n.extend({on:fun\
ction(a,g,b,c,e)\
{var f,h;if(\x22obj\
ect\x22===typeof a)\
{\x22string\x22!==type\
of g&&(b=b||g,g=\
void 0);for(f in\
 a)this.on(f,g,b\
,a[f],e);return \
this}null==\x0ab&&n\
ull==c?(c=g,b=g=\
void 0):null==c&\
&(\x22string\x22===typ\
eof g?(c=b,b=voi\
d 0):(c=b,b=g,g=\
void 0));if(!1==\
=c)c=n;else if(!\
c)return this;1=\
==e&&(h=c,c=func\
tion(a){d().off(\
a);return h.appl\
y(this,arguments\
)},c.guid=h.guid\
||(h.guid=d.guid\
++));return this\
.each(function()\
{d.event.add(thi\
s,a,c,b,g)})},on\
e:function(a,g,b\
,d){return this.\
on(a,g,b,d,1)},o\
ff:function(a,g,\
b){var c;if(a&&a\
.preventDefault&\
&a.handleObj)ret\
urn c=a.handleOb\
j,d(a.delegateTa\
rget).off(c.name\
space?c.origType\
+\x22.\x22+c.namespace\
:c.origType,c.se\
lector,\x0ac.handle\
r),this;if(\x22obje\
ct\x22===typeof a){\
for(c in a)this.\
off(c,g,a[c]);re\
turn this}if(!1=\
==g||\x22function\x22=\
==typeof g)b=g,g\
=void 0;!1===b&&\
(b=n);return thi\
s.each(function(\
){d.event.remove\
(this,a,b,g)})},\
trigger:function\
(a,g){return thi\
s.each(function(\
){d.event.trigge\
r(a,g,this)})},t\
riggerHandler:fu\
nction(a,g){var \
b=this[0];if(b)r\
eturn d.event.tr\
igger(a,g,b,!0)}\
});var Rb=\x22abbr|\
article|aside|au\
dio|bdi|canvas|d\
ata|datalist|det\
ails|figcaption|\
figure|footer|he\
ader|hgroup|mark\
|meter|nav|outpu\
t|progress|secti\
on|summary|time|\
video\x22,\x0aBd=/ jQu\
ery\x5cd+=\x22(?:null|\
\x5cd+)\x22/g,Dc=RegEx\
p(\x22<(?:\x22+Rb+\x22)[\x5c\
\x5cs/>]\x22,\x22i\x22),Eb=/\
^\x5cs+/,Ec=/<(?!ar\
ea|br|col|embed|\
hr|img|input|lin\
k|meta|param)(([\
\x5cw:]+)[^>]*)\x5c/>/\
gi,Fc=/<([\x5cw:]+)\
/,Gc=/<tbody/i,C\
d=/<|&#?\x5cw+;/,Dd\
=/<(?:script|sty\
le|link)/i,Ed=/c\
hecked\x5cs*(?:[^=]\
|=\x5cs*.checked.)/\
i,Hc=/^$|\x5c/(?:ja\
va|ecma)script/i\
,Yc=/^true\x5c/(.*)\
/,Fd=/^\x5cs*<!(?:\x5c\
[CDATA\x5c[|--)|(?:\
\x5c]\x5c]|--)>\x5cs*$/g,\
L={option:[1,\x22<s\
elect multiple='\
multiple'>\x22,\x22</s\
elect>\x22],legend:\
[1,\x22<fieldset>\x22,\
\x22</fieldset>\x22],a\
rea:[1,\x22<map>\x22,\x22\
</map>\x22],param:[\
1,\x22<object>\x22,\x0a\x22<\
/object>\x22],thead\
:[1,\x22<table>\x22,\x22<\
/table>\x22],tr:[2,\
\x22<table><tbody>\x22\
,\x22</tbody></tabl\
e>\x22],col:[2,\x22<ta\
ble><tbody></tbo\
dy><colgroup>\x22,\x22\
</colgroup></tab\
le>\x22],td:[3,\x22<ta\
ble><tbody><tr>\x22\
,\x22</tr></tbody><\
/table>\x22],_defau\
lt:s.htmlSeriali\
ze?[0,\x22\x22,\x22\x22]:[1,\
\x22X<div>\x22,\x22</div>\
\x22]},Fb=B(u).appe\
ndChild(u.create\
Element(\x22div\x22));\
L.optgroup=L.opt\
ion;L.tbody=L.tf\
oot=L.colgroup=L\
.caption=L.thead\
;L.th=L.td;d.ext\
end({clone:funct\
ion(a,g,b){var c\
,e,f,h,n,j=d.con\
tains(a.ownerDoc\
ument,a);s.html5\
Clone||d.isXMLDo\
c(a)||!Dc.test(\x22\
<\x22+\x0aa.nodeName+\x22\
>\x22)?f=a.cloneNod\
e(!0):(Fb.innerH\
TML=a.outerHTML,\
Fb.removeChild(f\
=Fb.firstChild))\
;if((!s.noCloneE\
vent||!s.noClone\
Checked)&&(1===a\
.nodeType||11===\
a.nodeType)&&!d.\
isXMLDoc(a)){c=E\
(f);n=E(a);for(h\
=0;null!=(e=n[h]\
);++h)if(c[h]){v\
ar l=c[h],t=void\
 0,r=void 0,m=vo\
id 0;if(1===l.no\
deType){t=l.node\
Name.toLowerCase\
();if(!s.noClone\
Event&&l[d.expan\
do]){m=d._data(l\
);for(r in m.eve\
nts)d.removeEven\
t(l,r,m.handle);\
l.removeAttribut\
e(d.expando)}if(\
\x22script\x22===t&&l.\
text!==e.text)jb\
(l).text=e.text,\
xa(l);else if(\x22o\
bject\x22===\x0at)l.pa\
rentNode&&(l.out\
erHTML=e.outerHT\
ML),s.html5Clone\
&&(e.innerHTML&&\
!d.trim(l.innerH\
TML))&&(l.innerH\
TML=e.innerHTML)\
;else if(\x22input\x22\
===t&&ib.test(e.\
type))l.defaultC\
hecked=l.checked\
=e.checked,l.val\
ue!==e.value&&(l\
.value=e.value);\
else if(\x22option\x22\
===t)l.defaultSe\
lected=l.selecte\
d=e.defaultSelec\
ted;else if(\x22inp\
ut\x22===t||\x22textar\
ea\x22===t)l.defaul\
tValue=e.default\
Value}}}if(g)if(\
b){n=n||E(a);c=c\
||E(f);for(h=0;n\
ull!=(e=n[h]);h+\
+)Tb(e,c[h])}els\
e Tb(a,f);c=E(f,\
\x22script\x22);0<c.le\
ngth&&F(c,!j&&E(\
a,\x22script\x22));ret\
urn f},\x0abuildFra\
gment:function(a\
,g,b,c){for(var \
e,f,h,n,j,l,t=a.\
length,r=B(g),m=\
[],p=0;p<t;p++)i\
f((f=a[p])||0===\
f)if(\x22object\x22===\
d.type(f))d.merg\
e(m,f.nodeType?[\
f]:f);else if(Cd\
.test(f)){h=h||r\
.appendChild(g.c\
reateElement(\x22di\
v\x22));n=(Fc.exec(\
f)||[\x22\x22,\x22\x22])[1].\
toLowerCase();l=\
L[n]||L._default\
;h.innerHTML=l[1\
]+f.replace(Ec,\x22\
<$1></$2>\x22)+l[2]\
;for(e=l[0];e--;\
)h=h.lastChild;!\
s.leadingWhitesp\
ace&&Eb.test(f)&\
&m.push(g.create\
TextNode(Eb.exec\
(f)[0]));if(!s.t\
body)for(e=(f=\x22t\
able\x22===n&&!Gc.t\
est(f)?h.firstCh\
ild:\x22<table>\x22===\
\x0al[1]&&!Gc.test(\
f)?h:0)&&f.child\
Nodes.length;e--\
;)d.nodeName(j=f\
.childNodes[e],\x22\
tbody\x22)&&!j.chil\
dNodes.length&&f\
.removeChild(j);\
d.merge(m,h.chil\
dNodes);for(h.te\
xtContent=\x22\x22;h.f\
irstChild;)h.rem\
oveChild(h.first\
Child);h=r.lastC\
hild}else m.push\
(g.createTextNod\
e(f));h&&r.remov\
eChild(h);s.appe\
ndChecked||d.gre\
p(E(m,\x22input\x22),X\
c);for(p=0;f=m[p\
++];)if(!(c&&-1!\
==d.inArray(f,c)\
)&&(a=d.contains\
(f.ownerDocument\
,f),h=E(r.append\
Child(f),\x22script\
\x22),a&&F(h),b))fo\
r(e=0;f=h[e++];)\
Hc.test(f.type||\
\x22\x22)&&b.push(f);r\
eturn r},\x0acleanD\
ata:function(a,g\
){for(var b,c,e,\
f,h=0,n=d.expand\
o,j=d.cache,l=s.\
deleteExpando,t=\
d.event.special;\
null!=(b=a[h]);h\
++)if(g||d.accep\
tData(b))if(f=(e\
=b[n])&&j[e]){if\
(f.events)for(c \
in f.events)t[c]\
?d.event.remove(\
b,c):d.removeEve\
nt(b,c,f.handle)\
;j[e]&&(delete j\
[e],l?delete b[n\
]:typeof b.remov\
eAttribute!==N?b\
.removeAttribute\
(n):b[n]=null,V.\
push(e))}}});d.f\
n.extend({text:f\
unction(a){retur\
n ma(this,functi\
on(a){return voi\
d 0===a?d.text(t\
his):this.empty(\
).append((this[0\
]&&this[0].owner\
Document||u).cre\
ateTextNode(a))}\
,\x0anull,a,argumen\
ts.length)},appe\
nd:function(){re\
turn this.domMan\
ip(arguments,fun\
ction(a){(1===th\
is.nodeType||11=\
==this.nodeType|\
|9===this.nodeTy\
pe)&&Sb(this,a).\
appendChild(a)})\
},prepend:functi\
on(){return this\
.domManip(argume\
nts,function(a){\
if(1===this.node\
Type||11===this.\
nodeType||9===th\
is.nodeType){var\
 g=Sb(this,a);g.\
insertBefore(a,g\
.firstChild)}})}\
,before:function\
(){return this.d\
omManip(argument\
s,function(a){th\
is.parentNode&&t\
his.parentNode.i\
nsertBefore(a,th\
is)})},after:fun\
ction(){return t\
his.domManip(arg\
uments,\x0afunction\
(a){this.parentN\
ode&&this.parent\
Node.insertBefor\
e(a,this.nextSib\
ling)})},remove:\
function(a,g){fo\
r(var b,c=a?d.fi\
lter(a,this):thi\
s,e=0;null!=(b=c\
[e]);e++)!g&&1==\
=b.nodeType&&d.c\
leanData(E(b)),b\
.parentNode&&(g&\
&d.contains(b.ow\
nerDocument,b)&&\
F(E(b,\x22script\x22))\
,b.parentNode.re\
moveChild(b));re\
turn this},empty\
:function(){for(\
var a,g=0;null!=\
(a=this[g]);g++)\
{for(1===a.nodeT\
ype&&d.cleanData\
(E(a,!1));a.firs\
tChild;)a.remove\
Child(a.firstChi\
ld);a.options&&d\
.nodeName(a,\x22sel\
ect\x22)&&(a.option\
s.length=0)}retu\
rn this},\x0aclone:\
function(a,g){a=\
null==a?!1:a;g=n\
ull==g?a:g;retur\
n this.map(funct\
ion(){return d.c\
lone(this,a,g)})\
},html:function(\
a){return ma(thi\
s,function(a){va\
r b=this[0]||{},\
c=0,e=this.lengt\
h;if(void 0===a)\
return 1===b.nod\
eType?b.innerHTM\
L.replace(Bd,\x22\x22)\
:void 0;if(\x22stri\
ng\x22===typeof a&&\
!Dd.test(a)&&(s.\
htmlSerialize||!\
Dc.test(a))&&(s.\
leadingWhitespac\
e||!Eb.test(a))&\
&!L[(Fc.exec(a)|\
|[\x22\x22,\x22\x22])[1].toL\
owerCase()]){a=a\
.replace(Ec,\x22<$1\
></$2>\x22);try{for\
(;c<e;c++)b=this\
[c]||{},1===b.no\
deType&&(d.clean\
Data(E(b,!1)),b.\
innerHTML=\x0aa);b=\
0}catch(f){}}b&&\
this.empty().app\
end(a)},null,a,a\
rguments.length)\
},replaceWith:fu\
nction(){var a=a\
rguments[0];this\
.domManip(argume\
nts,function(g){\
a=this.parentNod\
e;d.cleanData(E(\
this));a&&a.repl\
aceChild(g,this)\
});return a&&(a.\
length||a.nodeTy\
pe)?this:this.re\
move()},detach:f\
unction(a){retur\
n this.remove(a,\
!0)},domManip:fu\
nction(a,g){a=kc\
.apply([],a);var\
 b,c,e,f,h=0,n=t\
his.length,j=thi\
s,l=n-1,t=a[0],r\
=d.isFunction(t)\
;if(r||1<n&&\x22str\
ing\x22===typeof t&\
&!s.checkClone&&\
Ed.test(t))retur\
n this.each(func\
tion(b){var c=\x0aj\
.eq(b);r&&(a[0]=\
t.call(this,b,c.\
html()));c.domMa\
nip(a,g)});if(n&\
&(f=d.buildFragm\
ent(a,this[0].ow\
nerDocument,!1,t\
his),b=f.firstCh\
ild,1===f.childN\
odes.length&&(f=\
b),b)){e=d.map(E\
(f,\x22script\x22),jb)\
;for(c=e.length;\
h<n;h++)b=f,h!==\
l&&(b=d.clone(b,\
!0,!0),c&&d.merg\
e(e,E(b,\x22script\x22\
))),g.call(this[\
h],b,h);if(c){f=\
e[e.length-1].ow\
nerDocument;d.ma\
p(e,xa);for(h=0;\
h<c;h++)if(b=e[h\
],Hc.test(b.type\
||\x22\x22)&&!d._data(\
b,\x22globalEval\x22)&\
&d.contains(f,b)\
)b.src?d._evalUr\
l&&d._evalUrl(b.\
src):d.globalEva\
l((b.text||b.tex\
tContent||\x0ab.inn\
erHTML||\x22\x22).repl\
ace(Fd,\x22\x22))}f=b=\
null}return this\
}});d.each({appe\
ndTo:\x22append\x22,pr\
ependTo:\x22prepend\
\x22,insertBefore:\x22\
before\x22,insertAf\
ter:\x22after\x22,repl\
aceAll:\x22replaceW\
ith\x22},function(a\
,g){d.fn[a]=func\
tion(a){for(var \
b=0,c=[],e=d(a),\
f=e.length-1;b<=\
f;b++)a=b===f?th\
is:this.clone(!0\
),d(e[b])[g](a),\
ob.apply(c,a.get\
());return this.\
pushStack(c)}});\
var ya,Wb={},Fa,\
Za,ua=u.createEl\
ement(\x22div\x22);ua.\
innerHTML=\x22  <li\
nk/><table></tab\
le><a href='/a'>\
a</a><input type\
='checkbox'/>\x22;F\
a=ua.getElements\
ByTagName(\x22a\x22)[0\
];\x0aFa.style.cssT\
ext=\x22float:left;\
opacity:.5\x22;s.op\
acity=/^0.5/.tes\
t(Fa.style.opaci\
ty);s.cssFloat=!\
!Fa.style.cssFlo\
at;ua.style.back\
groundClip=\x22cont\
ent-box\x22;ua.clon\
eNode(!0).style.\
backgroundClip=\x22\
\x22;s.clearCloneSt\
yle=\x22content-box\
\x22===ua.style.bac\
kgroundClip;Fa=u\
a=null;s.shrinkW\
rapBlocks=functi\
on(){var a,g,b;i\
f(null==Za){a=u.\
getElementsByTag\
Name(\x22body\x22)[0];\
if(!a)return;g=u\
.createElement(\x22\
div\x22);b=u.create\
Element(\x22div\x22);a\
.appendChild(g).\
appendChild(b);Z\
a=!1;typeof b.st\
yle.zoom!==N&&(b\
.style.cssText=\x22\
-webkit-box-sizi\
ng:content-box;-\
moz-box-sizing:c\
ontent-box;box-s\
izing:content-bo\
x;display:block;\
padding:0;margin\
:0;border:0;widt\
h:1px;padding:1p\
x;zoom:1\x22,\x0ab.inn\
erHTML=\x22<div></d\
iv>\x22,b.firstChil\
d.style.width=\x225\
px\x22,Za=3!==b.off\
setWidth);a.remo\
veChild(g)}retur\
n Za};var Ic=/^m\
argin/,Ia=RegExp\
(\x22^(\x22+Wa+\x22)(?!px\
)[a-z%]+$\x22,\x22i\x22),\
ha,ia,Gd=/^(top|\
right|bottom|lef\
t)$/;c.getComput\
edStyle?(ha=func\
tion(a){return a\
.ownerDocument.d\
efaultView.getCo\
mputedStyle(a,nu\
ll)},ia=function\
(a,g,b){var c,e,\
f=a.style;e=(b=b\
||ha(a))?b.getPr\
opertyValue(g)||\
b[g]:void 0;b&&(\
\x22\x22===e&&!d.conta\
ins(a.ownerDocum\
ent,a)&&(e=d.sty\
le(a,g)),Ia.test\
(e)&&Ic.test(g)&\
&(a=f.width,g=f.\
minWidth,c=f.max\
Width,\x0af.minWidt\
h=f.maxWidth=f.w\
idth=e,e=b.width\
,f.width=a,f.min\
Width=g,f.maxWid\
th=c));return vo\
id 0===e?e:e+\x22\x22}\
):u.documentElem\
ent.currentStyle\
&&(ha=function(a\
){return a.curre\
ntStyle},ia=func\
tion(a,g,b){var \
c,d,e,f=a.style;\
e=(b=b||ha(a))?b\
[g]:void 0;null=\
=e&&(f&&f[g])&&(\
e=f[g]);if(Ia.te\
st(e)&&!Gd.test(\
g)){b=f.left;if(\
d=(c=a.runtimeSt\
yle)&&c.left)c.l\
eft=a.currentSty\
le.left;f.left=\x22\
fontSize\x22===g?\x221\
em\x22:e;e=f.pixelL\
eft+\x22px\x22;f.left=\
b;d&&(c.left=d)}\
return void 0===\
e?e:e+\x22\x22||\x22auto\x22\
});var Ib=functi\
on(){var a,b,\x0ae=\
u.getElementsByT\
agName(\x22body\x22)[0\
];e&&(a=u.create\
Element(\x22div\x22),b\
=u.createElement\
(\x22div\x22),a.style.\
cssText=Gb,e.app\
endChild(a).appe\
ndChild(b),b.sty\
le.cssText=\x22-web\
kit-box-sizing:b\
order-box;-moz-b\
ox-sizing:border\
-box;box-sizing:\
border-box;posit\
ion:absolute;dis\
play:block;paddi\
ng:1px;border:1p\
x;width:4px;marg\
in-top:1%;top:1%\
\x22,d.swap(e,null!\
=e.style.zoom?{z\
oom:1}:{},functi\
on(){Hb=4===b.of\
fsetWidth}),$a=!\
0,ab=!1,bb=!0,c.\
getComputedStyle\
&&(ab=\x221%\x22!==(c.\
getComputedStyle\
(b,null)||{}).to\
p,$a=\x224px\x22===(c.\
getComputedStyle\
(b,\x0anull)||{widt\
h:\x224px\x22}).width)\
,e.removeChild(a\
),b=e=null)},Ga,\
cb,Hb,$a,ab,bb,v\
a=u.createElemen\
t(\x22div\x22),Gb=\x22bor\
der:0;width:0;he\
ight:0;position:\
absolute;top:0;l\
eft:-9999px\x22;va.\
innerHTML=\x22  <li\
nk/><table></tab\
le><a href='/a'>\
a</a><input type\
='checkbox'/>\x22;G\
a=va.getElements\
ByTagName(\x22a\x22)[0\
];Ga.style.cssTe\
xt=\x22float:left;o\
pacity:.5\x22;s.opa\
city=/^0.5/.test\
(Ga.style.opacit\
y);s.cssFloat=!!\
Ga.style.cssFloa\
t;va.style.backg\
roundClip=\x22conte\
nt-box\x22;va.clone\
Node(!0).style.b\
ackgroundClip=\x22\x22\
;s.clearCloneSty\
le=\x22content-box\x22\
===\x0ava.style.bac\
kgroundClip;Ga=v\
a=null;d.extend(\
s,{reliableHidde\
nOffsets:functio\
n(){if(null!=cb)\
return cb;var a,\
b,c;b=u.createEl\
ement(\x22div\x22);var\
 d=u.getElements\
ByTagName(\x22body\x22\
)[0];if(d)return\
 b.setAttribute(\
\x22className\x22,\x22t\x22)\
,b.innerHTML=\x22  \
<link/><table></\
table><a href='/\
a'>a</a><input t\
ype='checkbox'/>\
\x22,a=u.createElem\
ent(\x22div\x22),a.sty\
le.cssText=Gb,d.\
appendChild(a).a\
ppendChild(b),b.\
innerHTML=\x22<tabl\
e><tr><td></td><\
td>t</td></tr></\
table>\x22,b=b.getE\
lementsByTagName\
(\x22td\x22),b[0].styl\
e.cssText=\x22paddi\
ng:0;margin:0;bo\
rder:0;display:n\
one\x22,\x0ac=0===b[0]\
.offsetHeight,b[\
0].style.display\
=\x22\x22,b[1].style.d\
isplay=\x22none\x22,cb\
=c&&0===b[0].off\
setHeight,d.remo\
veChild(a),cb},b\
oxSizing:functio\
n(){null==Hb&&Ib\
();return Hb},bo\
xSizingReliable:\
function(){null=\
=$a&&Ib();return\
 $a},pixelPositi\
on:function(){nu\
ll==ab&&Ib();ret\
urn ab},reliable\
MarginRight:func\
tion(){var a,b,d\
,e;if(null==bb&&\
c.getComputedSty\
le){a=u.getEleme\
ntsByTagName(\x22bo\
dy\x22)[0];if(!a)re\
turn;b=u.createE\
lement(\x22div\x22);d=\
u.createElement(\
\x22div\x22);b.style.c\
ssText=Gb;a.appe\
ndChild(b).appen\
dChild(d);e=\x0ad.a\
ppendChild(u.cre\
ateElement(\x22div\x22\
));e.style.cssTe\
xt=d.style.cssTe\
xt=\x22-webkit-box-\
sizing:content-b\
ox;-moz-box-sizi\
ng:content-box;b\
ox-sizing:conten\
t-box;display:bl\
ock;padding:0;ma\
rgin:0;border:0\x22\
;e.style.marginR\
ight=e.style.wid\
th=\x220\x22;d.style.w\
idth=\x221px\x22;bb=!p\
arseFloat((c.get\
ComputedStyle(e,\
null)||{}).margi\
nRight);a.remove\
Child(b)}return \
bb}});d.swap=fun\
ction(a,b,c,d){v\
ar e,f={};for(e \
in b)f[e]=a.styl\
e[e],a.style[e]=\
b[e];c=c.apply(a\
,d||[]);for(e in\
 b)a.style[e]=f[\
e];return c};var\
 Jb=/alpha\x5c([^)]\
*\x5c)/i,\x0aHd=/opaci\
ty\x5cs*=\x5cs*([^)]*)\
/,Id=/^(none|tab\
le(?!-c[ea]).+)/\
,Zc=RegExp(\x22^(\x22+\
Wa+\x22)(.*)$\x22,\x22i\x22)\
,Jd=RegExp(\x22^([+\
-])=(\x22+Wa+\x22)\x22,\x22i\
\x22),Kd={position:\
\x22absolute\x22,visib\
ility:\x22hidden\x22,d\
isplay:\x22block\x22},\
Jc={letterSpacin\
g:0,fontWeight:4\
00},Zb=[\x22Webkit\x22\
,\x22O\x22,\x22Moz\x22,\x22ms\x22]\
;d.extend({cssHo\
oks:{opacity:{ge\
t:function(a,b){\
if(b){var c=ia(a\
,\x22opacity\x22);retu\
rn\x22\x22===c?\x221\x22:c}}\
}},cssNumber:{co\
lumnCount:!0,fil\
lOpacity:!0,font\
Weight:!0,lineHe\
ight:!0,opacity:\
!0,order:!0,orph\
ans:!0,widows:!0\
,zIndex:!0,zoom:\
!0},cssProps:{\x22f\
loat\x22:s.cssFloat\
?\x0a\x22cssFloat\x22:\x22st\
yleFloat\x22},style\
:function(a,b,c,\
e){if(a&&!(3===a\
.nodeType||8===a\
.nodeType||!a.st\
yle)){var f,h,n,\
j=d.camelCase(b)\
,l=a.style;b=d.c\
ssProps[j]||(d.c\
ssProps[j]=Yb(l,\
j));n=d.cssHooks\
[b]||d.cssHooks[\
j];if(void 0!==c\
){h=typeof c;if(\
\x22string\x22===h&&(f\
=Jd.exec(c)))c=(\
f[1]+1)*f[2]+par\
seFloat(d.css(a,\
b)),h=\x22number\x22;i\
f(!(null==c||c!=\
=c))if(\x22number\x22=\
==h&&!d.cssNumbe\
r[j]&&(c+=\x22px\x22),\
!s.clearCloneSty\
le&&(\x22\x22===c&&0==\
=b.indexOf(\x22back\
ground\x22))&&(l[b]\
=\x22inherit\x22),!n||\
!(\x22set\x22in n)||vo\
id 0!==(c=n.set(\
a,c,e)))try{l[b]\
=\x0a\x22\x22,l[b]=c}catc\
h(t){}}else retu\
rn n&&\x22get\x22in n&\
&void 0!==(f=n.g\
et(a,!1,e))?f:l[\
b]}},css:functio\
n(a,b,c,e){var f\
,h;h=d.camelCase\
(b);b=d.cssProps\
[h]||(d.cssProps\
[h]=Yb(a.style,h\
));(h=d.cssHooks\
[b]||d.cssHooks[\
h])&&\x22get\x22in h&&\
(f=h.get(a,!0,c)\
);void 0===f&&(f\
=ia(a,b,e));\x22nor\
mal\x22===f&&b in J\
c&&(f=Jc[b]);ret\
urn\x22\x22===c||c?(a=\
parseFloat(f),!0\
===c||d.isNumeri\
c(a)?a||0:f):f}}\
);d.each([\x22heigh\
t\x22,\x22width\x22],func\
tion(a,b){d.cssH\
ooks[b]={get:fun\
ction(a,c,e){if(\
c)return 0===a.o\
ffsetWidth&&Id.t\
est(d.css(a,\x22dis\
play\x22))?\x0ad.swap(\
a,Kd,function(){\
return cc(a,b,e)\
}):cc(a,b,e)},se\
t:function(a,c,e\
){var f=e&&ha(a)\
;return ac(a,c,e\
?bc(a,b,e,s.boxS\
izing()&&\x22border\
-box\x22===d.css(a,\
\x22boxSizing\x22,!1,f\
),f):0)}}});s.op\
acity||(d.cssHoo\
ks.opacity={get:\
function(a,b){re\
turn Hd.test((b&\
&a.currentStyle?\
a.currentStyle.f\
ilter:a.style.fi\
lter)||\x22\x22)?0.01*\
parseFloat(RegEx\
p.$1)+\x22\x22:b?\x221\x22:\x22\
\x22},set:function(\
a,b){var c=a.sty\
le,e=a.currentSt\
yle,f=d.isNumeri\
c(b)?\x22alpha(opac\
ity=\x22+100*b+\x22)\x22:\
\x22\x22,h=e&&e.filter\
||c.filter||\x22\x22;c\
.zoom=1;if((1<=b\
||\x22\x22===b)&&\x22\x22===\
\x0ad.trim(h.replac\
e(Jb,\x22\x22))&&c.rem\
oveAttribute)if(\
c.removeAttribut\
e(\x22filter\x22),\x22\x22==\
=b||e&&!e.filter\
)return;c.filter\
=Jb.test(h)?h.re\
place(Jb,f):h+\x22 \
\x22+f}});d.cssHook\
s.marginRight=Xb\
(s.reliableMargi\
nRight,function(\
a,b){if(b)return\
 d.swap(a,{displ\
ay:\x22inline-block\
\x22},ia,[a,\x22margin\
Right\x22])});d.eac\
h({margin:\x22\x22,pad\
ding:\x22\x22,border:\x22\
Width\x22},function\
(a,b){d.cssHooks\
[a+b]={expand:fu\
nction(c){var d=\
0,e={};for(c=\x22st\
ring\x22===typeof c\
?c.split(\x22 \x22):[c\
];4>d;d++)e[a+ga\
[d]+b]=c[d]||c[d\
-2]||c[0];return\
 e}};Ic.test(a)|\
|(d.cssHooks[a+\x0a\
b].set=ac)});d.f\
n.extend({css:fu\
nction(a,b){retu\
rn ma(this,funct\
ion(a,b,g){var c\
,e={},f=0;if(d.i\
sArray(b)){g=ha(\
a);for(c=b.lengt\
h;f<c;f++)e[b[f]\
]=d.css(a,b[f],!\
1,g);return e}re\
turn void 0!==g?\
d.style(a,b,g):d\
.css(a,b)},a,b,1\
<arguments.lengt\
h)},show:functio\
n(){return $b(th\
is,!0)},hide:fun\
ction(){return $\
b(this)},toggle:\
function(a){retu\
rn\x22boolean\x22===ty\
peof a?a?this.sh\
ow():this.hide()\
:this.each(funct\
ion(){za(this)?d\
(this).show():d(\
this).hide()})}}\
);d.Tween=G;G.pr\
ototype={constru\
ctor:G,init:func\
tion(a,\x0ab,c,e,f,\
h){this.elem=a;t\
his.prop=c;this.\
easing=f||\x22swing\
\x22;this.options=b\
;this.start=this\
.now=this.cur();\
this.end=e;this.\
unit=h||(d.cssNu\
mber[c]?\x22\x22:\x22px\x22)\
},cur:function()\
{var a=G.propHoo\
ks[this.prop];re\
turn a&&a.get?a.\
get(this):G.prop\
Hooks._default.g\
et(this)},run:fu\
nction(a){var b,\
c=G.propHooks[th\
is.prop];this.po\
s=this.options.d\
uration?b=d.easi\
ng[this.easing](\
a,this.options.d\
uration*a,0,1,th\
is.options.durat\
ion):b=a;this.no\
w=(this.end-this\
.start)*b+this.s\
tart;this.option\
s.step&&this.opt\
ions.step.call(t\
his.elem,\x0athis.n\
ow,this);c&&c.se\
t?c.set(this):G.\
propHooks._defau\
lt.set(this);ret\
urn this}};G.pro\
totype.init.prot\
otype=G.prototyp\
e;G.propHooks={_\
default:{get:fun\
ction(a){if(null\
!=a.elem[a.prop]\
&&(!a.elem.style\
||null==a.elem.s\
tyle[a.prop]))re\
turn a.elem[a.pr\
op];a=d.css(a.el\
em,a.prop,\x22\x22);re\
turn!a||\x22auto\x22==\
=a?0:a},set:func\
tion(a){if(d.fx.\
step[a.prop])d.f\
x.step[a.prop](a\
);else a.elem.st\
yle&&(null!=a.el\
em.style[d.cssPr\
ops[a.prop]]||d.\
cssHooks[a.prop]\
)?d.style(a.elem\
,a.prop,a.now+a.\
unit):a.elem[a.p\
rop]=a.now}}};G.\
propHooks.scroll\
Top=\x0aG.propHooks\
.scrollLeft={set\
:function(a){a.e\
lem.nodeType&&a.\
elem.parentNode&\
&(a.elem[a.prop]\
=a.now)}};d.easi\
ng={linear:funct\
ion(a){return a}\
,swing:function(\
a){return 0.5-Ma\
th.cos(a*Math.PI\
)/2}};d.fx=G.pro\
totype.init;d.fx\
.step={};var pa,\
db,Ld=/^(?:toggl\
e|show|hide)$/,K\
c=RegExp(\x22^(?:([\
+-])=|)(\x22+Wa+\x22)(\
[a-z%]*)$\x22,\x22i\x22),\
Md=/queueHooks$/\
,Ka=[function(a,\
b,c){var e,f,h,n\
,j,l,t=this,r={}\
,m=a.style,p=a.n\
odeType&&za(a),B\
=d._data(a,\x22fxsh\
ow\x22);c.queue||(n\
=d._queueHooks(a\
,\x22fx\x22),null==n.u\
nqueued&&(n.unqu\
eued=0,j=n.empty\
.fire,\x0an.empty.f\
ire=function(){n\
.unqueued||j()})\
,n.unqueued++,t.\
always(function(\
){t.always(funct\
ion(){n.unqueued\
--;d.queue(a,\x22fx\
\x22).length||n.emp\
ty.fire()})}));i\
f(1===a.nodeType\
&&(\x22height\x22in b|\
|\x22width\x22in b))c.\
overflow=[m.over\
flow,m.overflowX\
,m.overflowY],f=\
d.css(a,\x22display\
\x22),l=Vb(a.nodeNa\
me),\x22none\x22===f&&\
(f=l),\x22inline\x22==\
=f&&\x22none\x22===d.c\
ss(a,\x22float\x22)&&(\
!s.inlineBlockNe\
edsLayout||\x22inli\
ne\x22===l?m.displa\
y=\x22inline-block\x22\
:m.zoom=1);c.ove\
rflow&&(m.overfl\
ow=\x22hidden\x22,s.sh\
rinkWrapBlocks()\
||t.always(funct\
ion(){m.overflow\
=\x0ac.overflow[0];\
m.overflowX=c.ov\
erflow[1];m.over\
flowY=c.overflow\
[2]}));for(e in \
b)if(f=b[e],Ld.e\
xec(f)){delete b\
[e];h=h||\x22toggle\
\x22===f;if(f===(p?\
\x22hide\x22:\x22show\x22))i\
f(\x22show\x22===f&&B&\
&void 0!==B[e])p\
=!0;else continu\
e;r[e]=B&&B[e]||\
d.style(a,e)}if(\
!d.isEmptyObject\
(r))for(e in B?\x22\
hidden\x22in B&&(p=\
B.hidden):B=d._d\
ata(a,\x22fxshow\x22,{\
}),h&&(B.hidden=\
!p),p?d(a).show(\
):t.done(functio\
n(){d(a).hide()}\
),t.done(functio\
n(){var b;d._rem\
oveData(a,\x22fxsho\
w\x22);for(b in r)d\
.style(a,b,r[b])\
}),r)b=ec(p?B[e]\
:0,e,t),e in B||\
(B[e]=b.start,\x0ap\
&&(b.end=b.start\
,b.start=\x22width\x22\
===e||\x22height\x22==\
=e?1:0))}],Aa={\x22\
*\x22:[function(a,b\
){var c=this.cre\
ateTween(a,b),e=\
c.cur(),f=Kc.exe\
c(b),h=f&&f[3]||\
(d.cssNumber[a]?\
\x22\x22:\x22px\x22),n=(d.cs\
sNumber[a]||\x22px\x22\
!==h&&+e)&&Kc.ex\
ec(d.css(c.elem,\
a)),j=1,l=20;if(\
n&&n[3]!==h){h=h\
||n[3];f=f||[];n\
=+e||1;do j=j||\x22\
.5\x22,n/=j,d.style\
(c.elem,a,n+h);w\
hile(j!==(j=c.cu\
r()/e)&&1!==j&&-\
-l)}f&&(n=c.star\
t=+n||+e||0,c.un\
it=h,c.end=f[1]?\
n+(f[1]+1)*f[2]:\
+f[2]);return c}\
]};d.Animation=d\
.extend(fc,{twee\
ner:function(a,b\
){d.isFunction(a\
)?(b=\x0aa,a=[\x22*\x22])\
:a=a.split(\x22 \x22);\
for(var c,e=0,f=\
a.length;e<f;e++\
)c=a[e],Aa[c]=Aa\
[c]||[],Aa[c].un\
shift(b)},prefil\
ter:function(a,b\
){b?Ka.unshift(a\
):Ka.push(a)}});\
d.speed=function\
(a,b,c){var e=a&\
&\x22object\x22===type\
of a?d.extend({}\
,a):{complete:c|\
|!c&&b||d.isFunc\
tion(a)&&a,durat\
ion:a,easing:c&&\
b||b&&!d.isFunct\
ion(b)&&b};e.dur\
ation=d.fx.off?0\
:\x22number\x22===type\
of e.duration?e.\
duration:e.durat\
ion in d.fx.spee\
ds?d.fx.speeds[e\
.duration]:d.fx.\
speeds._default;\
if(null==e.queue\
||!0===e.queue)e\
.queue=\x22fx\x22;e.ol\
d=e.complete;\x0ae.\
complete=functio\
n(){d.isFunction\
(e.old)&&e.old.c\
all(this);e.queu\
e&&d.dequeue(thi\
s,e.queue)};retu\
rn e};d.fn.exten\
d({fadeTo:functi\
on(a,b,c,d){retu\
rn this.filter(z\
a).css(\x22opacity\x22\
,0).show().end()\
.animate({opacit\
y:b},a,c,d)},ani\
mate:function(a,\
b,c,e){var f=d.i\
sEmptyObject(a),\
h=d.speed(b,c,e)\
;b=function(){va\
r b=fc(this,d.ex\
tend({},a),h);(f\
||d._data(this,\x22\
finish\x22))&&b.sto\
p(!0)};b.finish=\
b;return f||!1==\
=h.queue?this.ea\
ch(b):this.queue\
(h.queue,b)},sto\
p:function(a,b,c\
){var e=function\
(a){var b=a.stop\
;delete a.stop;\x0a\
b(c)};\x22string\x22!=\
=typeof a&&(c=b,\
b=a,a=void 0);b&\
&!1!==a&&this.qu\
eue(a||\x22fx\x22,[]);\
return this.each\
(function(){var \
b=!0,g=null!=a&&\
a+\x22queueHooks\x22,f\
=d.timers,h=d._d\
ata(this);if(g)h\
[g]&&h[g].stop&&\
e(h[g]);else for\
(g in h)h[g]&&(h\
[g].stop&&Md.tes\
t(g))&&e(h[g]);f\
or(g=f.length;g-\
-;)if(f[g].elem=\
==this&&(null==a\
||f[g].queue===a\
))f[g].anim.stop\
(c),b=!1,f.splic\
e(g,1);(b||!c)&&\
d.dequeue(this,a\
)})},finish:func\
tion(a){!1!==a&&\
(a=a||\x22fx\x22);retu\
rn this.each(fun\
ction(){var b,c=\
d._data(this),e=\
c[a+\x22queue\x22];b=c\
[a+\x22queueHooks\x22]\
;\x0avar f=d.timers\
,h=e?e.length:0;\
c.finish=!0;d.qu\
eue(this,a,[]);b\
&&b.stop&&b.stop\
.call(this,!0);f\
or(b=f.length;b-\
-;)f[b].elem===t\
his&&f[b].queue=\
==a&&(f[b].anim.\
stop(!0),f.splic\
e(b,1));for(b=0;\
b<h;b++)e[b]&&e[\
b].finish&&e[b].\
finish.call(this\
);delete c.finis\
h})}});d.each([\x22\
toggle\x22,\x22show\x22,\x22\
hide\x22],function(\
a,b){var c=d.fn[\
b];d.fn[b]=funct\
ion(a,d,e){retur\
n null==a||\x22bool\
ean\x22===typeof a?\
c.apply(this,arg\
uments):this.ani\
mate(Ja(b,!0),a,\
d,e)}});d.each({\
slideDown:Ja(\x22sh\
ow\x22),slideUp:Ja(\
\x22hide\x22),slideTog\
gle:Ja(\x22toggle\x22)\
,\x0afadeIn:{opacit\
y:\x22show\x22},fadeOu\
t:{opacity:\x22hide\
\x22},fadeToggle:{o\
pacity:\x22toggle\x22}\
},function(a,b){\
d.fn[a]=function\
(a,c,d){return t\
his.animate(b,a,\
c,d)}});d.timers\
=[];d.fx.tick=fu\
nction(){var a,b\
=d.timers,c=0;fo\
r(pa=d.now();c<b\
.length;c++)a=b[\
c],!a()&&b[c]===\
a&&b.splice(c--,\
1);b.length||d.f\
x.stop();pa=void\
 0};d.fx.timer=f\
unction(a){d.tim\
ers.push(a);a()?\
d.fx.start():d.t\
imers.pop()};d.f\
x.interval=13;d.\
fx.start=functio\
n(){db||(db=setI\
nterval(d.fx.tic\
k,d.fx.interval)\
)};d.fx.stop=fun\
ction(){clearInt\
erval(db);\x0adb=nu\
ll};d.fx.speeds=\
{slow:600,fast:2\
00,_default:400}\
;d.fn.delay=func\
tion(a,b){a=d.fx\
?d.fx.speeds[a]|\
|a:a;return this\
.queue(b||\x22fx\x22,f\
unction(b,g){var\
 c=setTimeout(b,\
a);g.stop=functi\
on(){clearTimeou\
t(c)}})};var eb,\
da,Kb,Lb,Ha=u.cr\
eateElement(\x22div\
\x22);Ha.setAttribu\
te(\x22className\x22,\x22\
t\x22);Ha.innerHTML\
=\x22  <link/><tabl\
e></table><a hre\
f='/a'>a</a><inp\
ut type='checkbo\
x'/>\x22;eb=Ha.getE\
lementsByTagName\
(\x22a\x22)[0];Kb=u.cr\
eateElement(\x22sel\
ect\x22);Lb=Kb.appe\
ndChild(u.create\
Element(\x22option\x22\
));da=Ha.getElem\
entsByTagName(\x22i\
nput\x22)[0];\x0aeb.st\
yle.cssText=\x22top\
:1px\x22;s.getSetAt\
tribute=\x22t\x22!==Ha\
.className;s.sty\
le=/top/.test(eb\
.getAttribute(\x22s\
tyle\x22));s.hrefNo\
rmalized=\x22/a\x22===\
eb.getAttribute(\
\x22href\x22);s.checkO\
n=!!da.value;s.o\
ptSelected=Lb.se\
lected;s.enctype\
=!!u.createEleme\
nt(\x22form\x22).encty\
pe;Kb.disabled=!\
0;s.optDisabled=\
!Lb.disabled;da=\
u.createElement(\
\x22input\x22);da.setA\
ttribute(\x22value\x22\
,\x22\x22);s.input=\x22\x22=\
==da.getAttribut\
e(\x22value\x22);da.va\
lue=\x22t\x22;da.setAt\
tribute(\x22type\x22,\x22\
radio\x22);s.radioV\
alue=\x22t\x22===da.va\
lue;var Nd=/\x5cr/g\
;d.fn.extend({va\
l:function(a){va\
r b,\x0ac,e,f=this[\
0];if(arguments.\
length)return e=\
d.isFunction(a),\
this.each(functi\
on(c){if(1===thi\
s.nodeType&&(c=e\
?a.call(this,c,d\
(this).val()):a,\
null==c?c=\x22\x22:\x22nu\
mber\x22===typeof c\
?c+=\x22\x22:d.isArray\
(c)&&(c=d.map(c,\
function(a){retu\
rn null==a?\x22\x22:a+\
\x22\x22})),b=d.valHoo\
ks[this.type]||d\
.valHooks[this.n\
odeName.toLowerC\
ase()],!b||!(\x22se\
t\x22in b)||void 0=\
==b.set(this,c,\x22\
value\x22)))this.va\
lue=c});if(f){if\
((b=d.valHooks[f\
.type]||d.valHoo\
ks[f.nodeName.to\
LowerCase()])&&\x22\
get\x22in b&&void 0\
!==(c=b.get(f,\x22v\
alue\x22)))return c\
;c=f.value;\x0aretu\
rn\x22string\x22===typ\
eof c?c.replace(\
Nd,\x22\x22):null==c?\x22\
\x22:c}}});d.extend\
({valHooks:{opti\
on:{get:function\
(a){var b=d.find\
.attr(a,\x22value\x22)\
;return null!=b?\
b:d.text(a)}},se\
lect:{get:functi\
on(a){for(var b,\
c=a.options,e=a.\
selectedIndex,f=\
(a=\x22select-one\x22=\
==a.type||0>e)?n\
ull:[],h=a?e+1:c\
.length,n=0>e?h:\
a?e:0;n<h;n++)if\
(b=c[n],(b.selec\
ted||n===e)&&(s.\
optDisabled?!b.d\
isabled:null===b\
.getAttribute(\x22d\
isabled\x22))&&(!b.\
parentNode.disab\
led||!d.nodeName\
(b.parentNode,\x22o\
ptgroup\x22))){b=d(\
b).val();if(a)re\
turn b;f.push(b)\
}return f},\x0aset:\
function(a,b){fo\
r(var c,e,f=a.op\
tions,h=d.makeAr\
ray(b),n=f.lengt\
h;n--;)if(e=f[n]\
,0<=d.inArray(d.\
valHooks.option.\
get(e),h))try{e.\
selected=c=!0}ca\
tch(j){e.scrollH\
eight}else e.sel\
ected=!1;c||(a.s\
electedIndex=-1)\
;return f}}}});d\
.each([\x22radio\x22,\x22\
checkbox\x22],funct\
ion(){d.valHooks\
[this]={set:func\
tion(a,b){if(d.i\
sArray(b))return\
 a.checked=0<=d.\
inArray(d(a).val\
(),b)}};s.checkO\
n||(d.valHooks[t\
his].get=functio\
n(a){return null\
===a.getAttribut\
e(\x22value\x22)?\x22on\x22:\
a.value})});var \
wa,Lc,ea=d.expr.\
attrHandle,Mb=/^\
(?:checked|selec\
ted)$/i,\x0ana=s.ge\
tSetAttribute,fb\
=s.input;d.fn.ex\
tend({attr:funct\
ion(a,b){return \
ma(this,d.attr,a\
,b,1<arguments.l\
ength)},removeAt\
tr:function(a){r\
eturn this.each(\
function(){d.rem\
oveAttr(this,a)}\
)}});d.extend({a\
ttr:function(a,b\
,c){var e,f,h=a.\
nodeType;if(a&&!\
(3===h||8===h||2\
===h)){if(typeof\
 a.getAttribute=\
==N)return d.pro\
p(a,b,c);if(1!==\
h||!d.isXMLDoc(a\
))b=b.toLowerCas\
e(),e=d.attrHook\
s[b]||(d.expr.ma\
tch.bool.test(b)\
?Lc:wa);if(void \
0!==c)if(null===\
c)d.removeAttr(a\
,b);else{if(e&&\x22\
set\x22in e&&void 0\
!==(f=e.set(a,\x0ac\
,b)))return f;a.\
setAttribute(b,c\
+\x22\x22);return c}el\
se{if(e&&\x22get\x22in\
 e&&null!==(f=e.\
get(a,b)))return\
 f;f=d.find.attr\
(a,b);return nul\
l==f?void 0:f}}}\
,removeAttr:func\
tion(a,b){var c,\
e,f=0,h=b&&b.mat\
ch(T);if(h&&1===\
a.nodeType)for(;\
c=h[f++];)e=d.pr\
opFix[c]||c,d.ex\
pr.match.bool.te\
st(c)?fb&&na||!M\
b.test(c)?a[e]=!\
1:a[d.camelCase(\
\x22default-\x22+c)]=a\
[e]=!1:d.attr(a,\
c,\x22\x22),a.removeAt\
tribute(na?c:e)}\
,attrHooks:{type\
:{set:function(a\
,b){if(!s.radioV\
alue&&\x22radio\x22===\
b&&d.nodeName(a,\
\x22input\x22)){var c=\
a.value;a.setAtt\
ribute(\x22type\x22,\x0ab\
);c&&(a.value=c)\
;return b}}}}});\
Lc={set:function\
(a,b,c){!1===b?d\
.removeAttr(a,c)\
:fb&&na||!Mb.tes\
t(c)?a.setAttrib\
ute(!na&&d.propF\
ix[c]||c,c):a[d.\
camelCase(\x22defau\
lt-\x22+c)]=a[c]=!0\
;return c}};d.ea\
ch(d.expr.match.\
bool.source.matc\
h(/\x5cw+/g),functi\
on(a,b){var c=ea\
[b]||d.find.attr\
;ea[b]=fb&&na||!\
Mb.test(b)?funct\
ion(a,b,g){var d\
,e;g||(e=ea[b],e\
a[b]=d,d=null!=c\
(a,b,g)?b.toLowe\
rCase():null,ea[\
b]=e);return d}:\
function(a,b,c){\
if(!c)return a[d\
.camelCase(\x22defa\
ult-\x22+b)]?b.toLo\
werCase():null}}\
);if(!fb||!na)d.\
attrHooks.value=\
\x0a{set:function(a\
,b,c){if(d.nodeN\
ame(a,\x22input\x22))a\
.defaultValue=b;\
else return wa&&\
wa.set(a,b,c)}};\
na||(wa={set:fun\
ction(a,b,c){var\
 d=a.getAttribut\
eNode(c);d||a.se\
tAttributeNode(d\
=a.ownerDocument\
.createAttribute\
(c));d.value=b+=\
\x22\x22;if(\x22value\x22===\
c||b===a.getAttr\
ibute(c))return \
b}},ea.id=ea.nam\
e=ea.coords=func\
tion(a,b,c){var \
d;if(!c)return(d\
=a.getAttributeN\
ode(b))&&\x22\x22!==d.\
value?d.value:nu\
ll},d.valHooks.b\
utton={get:funct\
ion(a,b){var c=a\
.getAttributeNod\
e(b);if(c&&c.spe\
cified)return c.\
value},set:wa.se\
t},d.attrHooks.c\
ontenteditable=\x0a\
{set:function(a,\
b,c){wa.set(a,\x22\x22\
===b?!1:b,c)}},d\
.each([\x22width\x22,\x22\
height\x22],functio\
n(a,b){d.attrHoo\
ks[b]={set:funct\
ion(a,c){if(\x22\x22==\
=c)return a.setA\
ttribute(b,\x22auto\
\x22),c}}}));s.styl\
e||(d.attrHooks.\
style={get:funct\
ion(a){return a.\
style.cssText||v\
oid 0},set:funct\
ion(a,b){return \
a.style.cssText=\
b+\x22\x22}});var Od=/\
^(?:input|select\
|textarea|button\
|object)$/i,Pd=/\
^(?:a|area)$/i;d\
.fn.extend({prop\
:function(a,b){r\
eturn ma(this,d.\
prop,a,b,1<argum\
ents.length)},re\
moveProp:functio\
n(a){a=d.propFix\
[a]||a;return th\
is.each(function\
(){try{this[a]=\x0a\
void 0,delete th\
is[a]}catch(b){}\
})}});d.extend({\
propFix:{\x22for\x22:\x22\
htmlFor\x22,\x22class\x22\
:\x22className\x22},pr\
op:function(a,b,\
c){var e,f,h;h=a\
.nodeType;if(a&&\
!(3===h||8===h||\
2===h)){if(h=1!=\
=h||!d.isXMLDoc(\
a))b=d.propFix[b\
]||b,f=d.propHoo\
ks[b];return voi\
d 0!==c?f&&\x22set\x22\
in f&&void 0!==(\
e=f.set(a,c,b))?\
e:a[b]=c:f&&\x22get\
\x22in f&&null!==(e\
=f.get(a,b))?e:a\
[b]}},propHooks:\
{tabIndex:{get:f\
unction(a){var b\
=d.find.attr(a,\x22\
tabindex\x22);retur\
n b?parseInt(b,1\
0):Od.test(a.nod\
eName)||Pd.test(\
a.nodeName)&&a.h\
ref?0:-1}}}});s.\
hrefNormalized||\
\x0ad.each([\x22href\x22,\
\x22src\x22],function(\
a,b){d.propHooks\
[b]={get:functio\
n(a){return a.ge\
tAttribute(b,4)}\
}});s.optSelecte\
d||(d.propHooks.\
selected={get:fu\
nction(a){if(a=a\
.parentNode)a.se\
lectedIndex,a.pa\
rentNode&&a.pare\
ntNode.selectedI\
ndex;return null\
}});d.each(\x22tabI\
ndex readOnly ma\
xLength cellSpac\
ing cellPadding \
rowSpan colSpan \
useMap frameBord\
er contentEditab\
le\x22.split(\x22 \x22),f\
unction(){d.prop\
Fix[this.toLower\
Case()]=this});s\
.enctype||(d.pro\
pFix.enctype=\x22en\
coding\x22);var Nb=\
/[\x5ct\x5cr\x5cn\x5cf]/g;d.\
fn.extend({addCl\
ass:function(a){\
var b,\x0ac,e,f,h,n\
=0,j=this.length\
;b=\x22string\x22===ty\
peof a&&a;if(d.i\
sFunction(a))ret\
urn this.each(fu\
nction(b){d(this\
).addClass(a.cal\
l(this,b,this.cl\
assName))});if(b\
)for(b=(a||\x22\x22).m\
atch(T)||[];n<j;\
n++)if(c=this[n]\
,e=1===c.nodeTyp\
e&&(c.className?\
(\x22 \x22+c.className\
+\x22 \x22).replace(Nb\
,\x22 \x22):\x22 \x22)){for(\
h=0;f=b[h++];)0>\
e.indexOf(\x22 \x22+f+\
\x22 \x22)&&(e+=f+\x22 \x22)\
;e=d.trim(e);c.c\
lassName!==e&&(c\
.className=e)}re\
turn this},remov\
eClass:function(\
a){var b,c,e,f,h\
,n=0,j=this.leng\
th;b=0===argumen\
ts.length||\x22stri\
ng\x22===typeof a&&\
a;if(d.isFunctio\
n(a))return this\
.each(function(b\
){d(this).remove\
Class(a.call(thi\
s,\x0ab,this.classN\
ame))});if(b)for\
(b=(a||\x22\x22).match\
(T)||[];n<j;n++)\
if(c=this[n],e=1\
===c.nodeType&&(\
c.className?(\x22 \x22\
+c.className+\x22 \x22\
).replace(Nb,\x22 \x22\
):\x22\x22)){for(h=0;f\
=b[h++];)for(;0<\
=e.indexOf(\x22 \x22+f\
+\x22 \x22);)e=e.repla\
ce(\x22 \x22+f+\x22 \x22,\x22 \x22\
);e=a?d.trim(e):\
\x22\x22;c.className!=\
=e&&(c.className\
=e)}return this}\
,toggleClass:fun\
ction(a,b){var c\
=typeof a;return\
\x22boolean\x22===type\
of b&&\x22string\x22==\
=c?b?this.addCla\
ss(a):this.remov\
eClass(a):d.isFu\
nction(a)?this.e\
ach(function(c){\
d(this).toggleCl\
ass(a.call(this,\
c,this.className\
,b),b)}):\x0athis.e\
ach(function(){i\
f(\x22string\x22===c)f\
or(var b,g=0,e=d\
(this),f=a.match\
(T)||[];b=f[g++]\
;)e.hasClass(b)?\
e.removeClass(b)\
:e.addClass(b);e\
lse if(c===N||\x22b\
oolean\x22===c)this\
.className&&d._d\
ata(this,\x22__clas\
sName__\x22,this.cl\
assName),this.cl\
assName=this.cla\
ssName||!1===a?\x22\
\x22:d._data(this,\x22\
__className__\x22)|\
|\x22\x22})},hasClass:\
function(a){a=\x22 \
\x22+a+\x22 \x22;for(var \
b=0,c=this.lengt\
h;b<c;b++)if(1==\
=this[b].nodeTyp\
e&&0<=(\x22 \x22+this[\
b].className+\x22 \x22\
).replace(Nb,\x22 \x22\
).indexOf(a))ret\
urn!0;return!1}}\
);d.each(\x22blur f\
ocus focusin foc\
usout load resiz\
e scroll unload \
click dblclick m\
ousedown mouseup\
 mousemove mouse\
over mouseout mo\
useenter mousele\
ave change selec\
t submit keydown\
 keypress keyup \
error contextmen\
u\x22.split(\x22 \x22),\x0af\
unction(a,b){d.f\
n[b]=function(a,\
c){return 0<argu\
ments.length?thi\
s.on(b,null,a,c)\
:this.trigger(b)\
}});d.fn.extend(\
{hover:function(\
a,b){return this\
.mouseenter(a).m\
ouseleave(b||a)}\
,bind:function(a\
,b,c){return thi\
s.on(a,null,b,c)\
},unbind:functio\
n(a,b){return th\
is.off(a,null,b)\
},delegate:funct\
ion(a,b,c,e){ret\
urn this.on(b,a,\
c,e)},undelegate\
:function(a,b,c)\
{return 1===argu\
ments.length?thi\
s.off(a,\x22**\x22):th\
is.off(b,a||\x22**\x22\
,c)}});var Ob=d.\
now(),Pb=/\x5c?/,Qd\
=/(,)|(\x5c[|{)|(}|\
])|\x22(?:[^\x22\x5c\x5c\x5cr\x5cn\
]|\x5c\x5c[\x22\x5c\x5c\x5c/bfnrt]\
|\x5c\x5cu[\x5cda-fA-F]{4\
})*\x22\x5cs*:?|true|f\
alse|null|-?(?!0\
\x5cd)\x5cd+(?:\x5c.\x5cd+|)\
(?:[eE][+-]?\x5cd+|\
)/g;\x0ad.parseJSON\
=function(a){if(\
c.JSON&&c.JSON.p\
arse)return c.JS\
ON.parse(a+\x22\x22);v\
ar b,e=null,f=d.\
trim(a+\x22\x22);retur\
n f&&!d.trim(f.r\
eplace(Qd,functi\
on(a,c,d,f){b&&c\
&&(e=0);if(0===e\
)return a;b=d||c\
;e+=!f-!d;return\
\x22\x22}))?Function(\x22\
return \x22+f)():d.\
error(\x22Invalid J\
SON: \x22+a)};d.par\
seXML=function(a\
){var b,e;if(!a|\
|\x22string\x22!==type\
of a)return null\
;try{c.DOMParser\
?(e=new DOMParse\
r,b=e.parseFromS\
tring(a,\x22text/xm\
l\x22)):(b=new Acti\
veXObject(\x22Micro\
soft.XMLDOM\x22),b.\
async=\x22false\x22,b.\
loadXML(a))}catc\
h(f){b=void 0}(!\
b||!b.documentEl\
ement||\x0ab.getEle\
mentsByTagName(\x22\
parsererror\x22).le\
ngth)&&d.error(\x22\
Invalid XML: \x22+a\
);return b};var \
oa,fa,Rd=/#.*$/,\
Mc=/([?&])_=[^&]\
*/,Sd=/^(.*?):[ \
\x5ct]*([^\x5cr\x5cn]*)\x5cr\
?$/mg,Td=/^(?:GE\
T|HEAD)$/,Ud=/^\x5c\
/\x5c//,Nc=/^([\x5cw.+\
-]+:)(?:\x5c/\x5c/(?:[\
^\x5c/?#]*@|)([^\x5c/?\
#:]*)(?::(\x5cd+)|)\
|)/,Oc={},kb={},\
Pc=\x22*/\x22.concat(\x22\
*\x22);try{fa=locat\
ion.href}catch(d\
e){fa=u.createEl\
ement(\x22a\x22),fa.hr\
ef=\x22\x22,fa=fa.href\
}oa=Nc.exec(fa.t\
oLowerCase())||[\
];d.extend({acti\
ve:0,lastModifie\
d:{},etag:{},aja\
xSettings:{url:f\
a,type:\x22GET\x22,isL\
ocal:/^(?:about|\
app|app-storage|\
.+-extension|fil\
e|res|widget):$/\
.test(oa[1]),\x0agl\
obal:!0,processD\
ata:!0,async:!0,\
contentType:\x22app\
lication/x-www-f\
orm-urlencoded; \
charset=UTF-8\x22,a\
ccepts:{\x22*\x22:Pc,t\
ext:\x22text/plain\x22\
,html:\x22text/html\
\x22,xml:\x22applicati\
on/xml, text/xml\
\x22,json:\x22applicat\
ion/json, text/j\
avascript\x22},cont\
ents:{xml:/xml/,\
html:/html/,json\
:/json/},respons\
eFields:{xml:\x22re\
sponseXML\x22,text:\
\x22responseText\x22,j\
son:\x22responseJSO\
N\x22},converters:{\
\x22* text\x22:String,\
\x22text html\x22:!0,\x22\
text json\x22:d.par\
seJSON,\x22text xml\
\x22:d.parseXML},fl\
atOptions:{url:!\
0,context:!0}},a\
jaxSetup:functio\
n(a,b){return b?\
lb(lb(a,\x0ad.ajaxS\
ettings),b):lb(d\
.ajaxSettings,a)\
},ajaxPrefilter:\
gc(Oc),ajaxTrans\
port:gc(kb),ajax\
:function(a,b){f\
unction c(a,b,g,\
e){var f,k,r,q;q\
=b;if(2!==y){y=2\
;j&&clearTimeout\
(j);t=void 0;n=e\
||\x22\x22;A.readyStat\
e=0<a?4:0;e=200<\
=a&&300>a||304==\
=a;if(g){r=m;for\
(var u=A,K,w,z,x\
,C=r.contents,F=\
r.dataTypes;\x22*\x22=\
==F[0];)F.shift(\
),void 0===w&&(w\
=r.mimeType||u.g\
etResponseHeader\
(\x22Content-Type\x22)\
);if(w)for(x in \
C)if(C[x]&&C[x].\
test(w)){F.unshi\
ft(x);break}if(F\
[0]in g)z=F[0];e\
lse{for(x in g){\
if(!F[0]||r.conv\
erters[x+\x22 \x22+F[0\
]]){z=\x0ax;break}K\
||(K=x)}z=z||K}z\
?(z!==F[0]&&F.un\
shift(z),r=g[z])\
:r=void 0}a:{g=m\
;K=r;w=A;z=e;var\
 H,D,G,u={},C=g.\
dataTypes.slice(\
);if(C[1])for(D \
in g.converters)\
u[D.toLowerCase(\
)]=g.converters[\
D];for(x=C.shift\
();x;)if(g.respo\
nseFields[x]&&(w\
[g.responseField\
s[x]]=K),!G&&(z&\
&g.dataFilter)&&\
(K=g.dataFilter(\
K,g.dataType)),G\
=x,x=C.shift())i\
f(\x22*\x22===x)x=G;el\
se if(\x22*\x22!==G&&G\
!==x){D=u[G+\x22 \x22+\
x]||u[\x22* \x22+x];if\
(!D)for(H in u)i\
f(r=H.split(\x22 \x22)\
,r[1]===x&&(D=u[\
G+\x22 \x22+r[0]]||u[\x22\
* \x22+r[0]])){!0==\
=D?D=u[H]:!0!==u\
[H]&&(x=r[0],\x0aC.\
unshift(r[1]));b\
reak}if(!0!==D)i\
f(D&&g[\x22throws\x22]\
)K=D(K);else try\
{K=D(K)}catch(I)\
{r={state:\x22parse\
rerror\x22,error:D?\
I:\x22No conversion\
 from \x22+G+\x22 to \x22\
+x};break a}}r={\
state:\x22success\x22,\
data:K}}if(e)m.i\
fModified&&((q=A\
.getResponseHead\
er(\x22Last-Modifie\
d\x22))&&(d.lastMod\
ified[h]=q),(q=A\
.getResponseHead\
er(\x22etag\x22))&&(d.\
etag[h]=q)),204=\
==a||\x22HEAD\x22===m.\
type?q=\x22noconten\
t\x22:304===a?q=\x22no\
tmodified\x22:(q=r.\
state,f=r.data,k\
=r.error,e=!k);e\
lse if(k=q,a||!q\
)q=\x22error\x22,0>a&&\
(a=0);A.status=a\
;A.statusText=(b\
||q)+\x22\x22;e?s.reso\
lveWith(p,\x0a[f,q,\
A]):s.rejectWith\
(p,[A,q,k]);A.st\
atusCode(v);v=vo\
id 0;l&&B.trigge\
r(e?\x22ajaxSuccess\
\x22:\x22ajaxError\x22,[A\
,m,e?f:k]);E.fir\
eWith(p,[A,q]);l\
&&(B.trigger(\x22aj\
axComplete\x22,[A,m\
]),--d.active||d\
.event.trigger(\x22\
ajaxStop\x22))}}\x22ob\
ject\x22===typeof a\
&&(b=a,a=void 0)\
;b=b||{};var e,f\
,h,n,j,l,t,r,m=d\
.ajaxSetup({},b)\
,p=m.context||m,\
B=m.context&&(p.\
nodeType||p.jque\
ry)?d(p):d.event\
,s=d.Deferred(),\
E=d.Callbacks(\x22o\
nce memory\x22),v=m\
.statusCode||{},\
u={},w={},y=0,z=\
\x22canceled\x22,A={re\
adyState:0,getRe\
sponseHeader:fun\
ction(a){var b;i\
f(2===\x0ay){if(!r)\
for(r={};b=Sd.ex\
ec(n);)r[b[1].to\
LowerCase()]=b[2\
];b=r[a.toLowerC\
ase()]}return nu\
ll==b?null:b},ge\
tAllResponseHead\
ers:function(){r\
eturn 2===y?n:nu\
ll},setRequestHe\
ader:function(a,\
b){var c=a.toLow\
erCase();y||(a=w\
[c]=w[c]||a,u[a]\
=b);return this}\
,overrideMimeTyp\
e:function(a){y|\
|(m.mimeType=a);\
return this},sta\
tusCode:function\
(a){var b;if(a)i\
f(2>y)for(b in a\
)v[b]=[v[b],a[b]\
];else A.always(\
a[A.status]);ret\
urn this},abort:\
function(a){a=a|\
|z;t&&t.abort(a)\
;c(0,a);return t\
his}};s.promise(\
A).complete=\x0aE.a\
dd;A.success=A.d\
one;A.error=A.fa\
il;m.url=((a||m.\
url||fa)+\x22\x22).rep\
lace(Rd,\x22\x22).repl\
ace(Ud,oa[1]+\x22//\
\x22);m.type=b.meth\
od||b.type||m.me\
thod||m.type;m.d\
ataTypes=d.trim(\
m.dataType||\x22*\x22)\
.toLowerCase().m\
atch(T)||[\x22\x22];nu\
ll==m.crossDomai\
n&&(e=Nc.exec(m.\
url.toLowerCase(\
)),m.crossDomain\
=!(!e||!(e[1]!==\
oa[1]||e[2]!==oa\
[2]||(e[3]||(\x22ht\
tp:\x22===e[1]?\x2280\x22\
:\x22443\x22))!==(oa[3\
]||(\x22http:\x22===oa\
[1]?\x2280\x22:\x22443\x22))\
)));m.data&&(m.p\
rocessData&&\x22str\
ing\x22!==typeof m.\
data)&&(m.data=d\
.param(m.data,m.\
traditional));hc\
(Oc,m,b,A);if(2=\
==\x0ay)return A;(l\
=m.global)&&0===\
d.active++&&d.ev\
ent.trigger(\x22aja\
xStart\x22);m.type=\
m.type.toUpperCa\
se();m.hasConten\
t=!Td.test(m.typ\
e);h=m.url;m.has\
Content||(m.data\
&&(h=m.url+=(Pb.\
test(h)?\x22&\x22:\x22?\x22)\
+m.data,delete m\
.data),!1===m.ca\
che&&(m.url=Mc.t\
est(h)?h.replace\
(Mc,\x22$1_=\x22+Ob++)\
:h+(Pb.test(h)?\x22\
&\x22:\x22?\x22)+\x22_=\x22+Ob+\
+));m.ifModified\
&&(d.lastModifie\
d[h]&&A.setReque\
stHeader(\x22If-Mod\
ified-Since\x22,d.l\
astModified[h]),\
d.etag[h]&&A.set\
RequestHeader(\x22I\
f-None-Match\x22,d.\
etag[h]));(m.dat\
a&&m.hasContent&\
&!1!==m.contentT\
ype||b.contentTy\
pe)&&\x0aA.setReque\
stHeader(\x22Conten\
t-Type\x22,m.conten\
tType);A.setRequ\
estHeader(\x22Accep\
t\x22,m.dataTypes[0\
]&&m.accepts[m.d\
ataTypes[0]]?m.a\
ccepts[m.dataTyp\
es[0]]+(\x22*\x22!==m.\
dataTypes[0]?\x22, \
\x22+Pc+\x22; q=0.01\x22:\
\x22\x22):m.accepts[\x22*\
\x22]);for(f in m.h\
eaders)A.setRequ\
estHeader(f,m.he\
aders[f]);if(m.b\
eforeSend&&(!1==\
=m.beforeSend.ca\
ll(p,A,m)||2===y\
))return A.abort\
();z=\x22abort\x22;for\
(f in{success:1,\
error:1,complete\
:1})A[f](m[f]);i\
f(t=hc(kb,m,b,A)\
){A.readyState=1\
;l&&B.trigger(\x22a\
jaxSend\x22,[A,m]);\
m.async&&0<m.tim\
eout&&(j=setTime\
out(function(){A\
.abort(\x22timeout\x22\
)},\x0am.timeout));\
try{y=1,t.send(u\
,c)}catch(x){if(\
2>y)c(-1,x);else\
 throw x;}}else \
c(-1,\x22No Transpo\
rt\x22);return A},g\
etJSON:function(\
a,b,c){return d.\
get(a,b,c,\x22json\x22\
)},getScript:fun\
ction(a,b){retur\
n d.get(a,void 0\
,b,\x22script\x22)}});\
d.each([\x22get\x22,\x22p\
ost\x22],function(a\
,b){d[b]=functio\
n(a,c,e,f){d.isF\
unction(c)&&(f=f\
||e,e=c,c=void 0\
);return d.ajax(\
{url:a,type:b,da\
taType:f,data:c,\
success:e})}});d\
.each(\x22ajaxStart\
 ajaxStop ajaxCo\
mplete ajaxError\
 ajaxSuccess aja\
xSend\x22.split(\x22 \x22\
),function(a,b){\
d.fn[b]=function\
(a){return this.\
on(b,\x0aa)}});d._e\
valUrl=function(\
a){return d.ajax\
({url:a,type:\x22GE\
T\x22,dataType:\x22scr\
ipt\x22,async:!1,gl\
obal:!1,\x22throws\x22\
:!0})};d.fn.exte\
nd({wrapAll:func\
tion(a){if(d.isF\
unction(a))retur\
n this.each(func\
tion(b){d(this).\
wrapAll(a.call(t\
his,b))});if(thi\
s[0]){var b=d(a,\
this[0].ownerDoc\
ument).eq(0).clo\
ne(!0);this[0].p\
arentNode&&b.ins\
ertBefore(this[0\
]);b.map(functio\
n(){for(var a=th\
is;a.firstChild&\
&1===a.firstChil\
d.nodeType;)a=a.\
firstChild;retur\
n a}).append(thi\
s)}return this},\
wrapInner:functi\
on(a){return d.i\
sFunction(a)?\x0ath\
is.each(function\
(b){d(this).wrap\
Inner(a.call(thi\
s,b))}):this.eac\
h(function(){var\
 b=d(this),c=b.c\
ontents();c.leng\
th?c.wrapAll(a):\
b.append(a)})},w\
rap:function(a){\
var b=d.isFuncti\
on(a);return thi\
s.each(function(\
c){d(this).wrapA\
ll(b?a.call(this\
,c):a)})},unwrap\
:function(){retu\
rn this.parent()\
.each(function()\
{d.nodeName(this\
,\x22body\x22)||d(this\
).replaceWith(th\
is.childNodes)})\
.end()}});d.expr\
.filters.hidden=\
function(a){retu\
rn 0>=a.offsetWi\
dth&&0>=a.offset\
Height||!s.relia\
bleHiddenOffsets\
()&&\x22none\x22===(a.\
style&&\x0aa.style.\
display||d.css(a\
,\x22display\x22))};d.\
expr.filters.vis\
ible=function(a)\
{return!d.expr.f\
ilters.hidden(a)\
};var Vd=/%20/g,\
ad=/\x5c[\x5c]$/,Qc=/\x5c\
r?\x5cn/g,Wd=/^(?:s\
ubmit|button|ima\
ge|reset|file)$/\
i,Xd=/^(?:input|\
select|textarea|\
keygen)/i;d.para\
m=function(a,b){\
var c,e=[],f=fun\
ction(a,b){b=d.i\
sFunction(b)?b()\
:null==b?\x22\x22:b;e[\
e.length]=encode\
URIComponent(a)+\
\x22=\x22+encodeURICom\
ponent(b)};void \
0===b&&(b=d.ajax\
Settings&&d.ajax\
Settings.traditi\
onal);if(d.isArr\
ay(a)||a.jquery&\
&!d.isPlainObjec\
t(a))d.each(a,fu\
nction(){f(this.\
name,\x0athis.value\
)});else for(c i\
n a)mb(c,a[c],b,\
f);return e.join\
(\x22&\x22).replace(Vd\
,\x22+\x22)};d.fn.exte\
nd({serialize:fu\
nction(){return \
d.param(this.ser\
ializeArray())},\
serializeArray:f\
unction(){return\
 this.map(functi\
on(){var a=d.pro\
p(this,\x22elements\
\x22);return a?d.ma\
keArray(a):this}\
).filter(functio\
n(){var a=this.t\
ype;return this.\
name&&!d(this).i\
s(\x22:disabled\x22)&&\
Xd.test(this.nod\
eName)&&!Wd.test\
(a)&&(this.check\
ed||!ib.test(a))\
}).map(function(\
a,b){var c=d(thi\
s).val();return \
null==c?null:d.i\
sArray(c)?d.map(\
c,function(a){re\
turn{name:b.name\
,\x0avalue:a.replac\
e(Qc,\x22\x5cr\x5cn\x22)}}):\
{name:b.name,val\
ue:c.replace(Qc,\
\x22\x5cr\x5cn\x22)}}).get()\
}});d.ajaxSettin\
gs.xhr=void 0!==\
c.ActiveXObject?\
function(){var a\
;if(!(a=!this.is\
Local&&/^(get|po\
st|head|put|dele\
te|options)$/i.t\
est(this.type)&&\
ic()))a:{try{a=n\
ew c.ActiveXObje\
ct(\x22Microsoft.XM\
LHTTP\x22);break a}\
catch(b){}a=void\
 0}return a}:ic;\
d.ajaxSettings.x\
hr=void 0===c.Ac\
tiveXObject?nb:f\
unction(){return\
(this.url==u.loc\
ation||0==this.u\
rl.indexOf(\x22http\
\x22)||!this.isLoca\
l)&&/^(get|post|\
head|put|delete|\
options)$/i.test\
(this.type)&&\x0anb\
()||nb(1)};var Y\
d=0,gb={},hb=d.a\
jaxSettings.xhr(\
);if(c.ActiveXOb\
ject)d(c).on(\x22un\
load\x22,function()\
{for(var a in gb\
)gb[a](void 0,!0\
)});s.cors=!!hb&\
&\x22withCredential\
s\x22in hb;(hb=s.aj\
ax=!!hb)&&d.ajax\
Transport(functi\
on(a){if(!a.cros\
sDomain||s.cors)\
{var b;return{se\
nd:function(c,e)\
{var f,h=a.xhr()\
,n=++Yd;console.\
log(\x22xhr.open as\
ync=\x22+a.async+\x22 \
url=\x22+a.url);h.o\
pen(a.type,a.url\
,a.async,a.usern\
ame,a.password);\
if(a.xhrFields)f\
or(f in a.xhrFie\
lds)h[f]=a.xhrFi\
elds[f];a.mimeTy\
pe&&h.overrideMi\
meType&&h.overri\
deMimeType(a.mim\
eType);\x0a!a.cross\
Domain&&!c[\x22X-Re\
quested-With\x22]&&\
(c[\x22X-Requested-\
With\x22]=\x22XMLHttpR\
equest\x22);for(f i\
n c)void 0!==c[f\
]&&h.setRequestH\
eader(f,c[f]+\x22\x22)\
;h.send(a.hasCon\
tent&&a.data||nu\
ll);b=function(c\
,f){var k,j,l;if\
(b&&(f||4===h.re\
adyState))if(del\
ete gb[n],b=void\
 0,h.onreadystat\
echange=d.noop,f\
)4!==h.readyStat\
e&&h.abort();els\
e{l={};k=h.statu\
s;\x22string\x22===typ\
eof h.responseTe\
xt&&(l.text=h.re\
sponseText);try{\
j=h.statusText}c\
atch(m){j=\x22\x22}!k&\
&a.isLocal&&!a.c\
rossDomain?k=l.t\
ext?200:404:1223\
===k&&(k=204)}l&\
&e(k,j,l,h.getAl\
lResponseHeaders\
())};\x0aa.async?4=\
==h.readyState?s\
etTimeout(b):h.o\
nreadystatechang\
e=gb[n]=b:b()},a\
bort:function(){\
b&&b(void 0,!0)}\
}}});d.ajaxSetup\
({accepts:{scrip\
t:\x22text/javascri\
pt, application/\
javascript, appl\
ication/ecmascri\
pt, application/\
x-ecmascript\x22},c\
ontents:{script:\
/(?:java|ecma)sc\
ript/},converter\
s:{\x22text script\x22\
:function(a){d.g\
lobalEval(a);ret\
urn a}}});d.ajax\
Prefilter(\x22scrip\
t\x22,function(a){v\
oid 0===a.cache&\
&(a.cache=!1);a.\
crossDomain&&(a.\
type=\x22GET\x22,a.glo\
bal=!1)});d.ajax\
Transport(\x22scrip\
t\x22,function(a){i\
f(a.crossDomain)\
{var b,\x0ac=u.head\
||d(\x22head\x22)[0]||\
u.documentElemen\
t;return{send:fu\
nction(e,d){b=u.\
createElement(\x22s\
cript\x22);b.async=\
!0;a.scriptChars\
et&&(b.charset=a\
.scriptCharset);\
b.src=a.url;b.on\
load=b.onreadyst\
atechange=functi\
on(a,c){if(c||!b\
.readyState||/lo\
aded|complete/.t\
est(b.readyState\
))b.onload=b.onr\
eadystatechange=\
null,b.parentNod\
e&&b.parentNode.\
removeChild(b),b\
=null,c||d(200,\x22\
success\x22)};c.ins\
ertBefore(b,c.fi\
rstChild)},abort\
:function(){if(b\
)b.onload(void 0\
,!0)}}}});var Rc\
=[],Qb=/(=)\x5c?(?=\
&|$)|\x5c?\x5c?/;d.aja\
xSetup({jsonp:\x22c\
allback\x22,\x0ajsonpC\
allback:function\
(){var a=Rc.pop(\
)||d.expando+\x22_\x22\
+Ob++;this[a]=!0\
;return a}});d.a\
jaxPrefilter(\x22js\
on jsonp\x22,functi\
on(a,b,e){var f,\
h,n,j=!1!==a.jso\
np&&(Qb.test(a.u\
rl)?\x22url\x22:\x22strin\
g\x22===typeof a.da\
ta&&!(a.contentT\
ype||\x22\x22).indexOf\
(\x22application/x-\
www-form-urlenco\
ded\x22)&&Qb.test(a\
.data)&&\x22data\x22);\
if(j||\x22jsonp\x22===\
a.dataTypes[0])r\
eturn f=a.jsonpC\
allback=d.isFunc\
tion(a.jsonpCall\
back)?a.jsonpCal\
lback():a.jsonpC\
allback,j?a[j]=a\
[j].replace(Qb,\x22\
$1\x22+f):!1!==a.js\
onp&&(a.url+=(Pb\
.test(a.url)?\x22&\x22\
:\x22?\x22)+a.jsonp+\x22=\
\x22+\x0af),a.converte\
rs[\x22script json\x22\
]=function(){n||\
d.error(f+\x22 was \
not called\x22);ret\
urn n[0]},a.data\
Types[0]=\x22json\x22,\
h=c[f],c[f]=func\
tion(){n=argumen\
ts},e.always(fun\
ction(){c[f]=h;a\
[f]&&(a.jsonpCal\
lback=b.jsonpCal\
lback,Rc.push(f)\
);n&&d.isFunctio\
n(h)&&h(n[0]);n=\
h=void 0}),\x22scri\
pt\x22});d.parseHTM\
L=function(a,b,c\
){if(!a||\x22string\
\x22!==typeof a)ret\
urn null;\x22boolea\
n\x22===typeof b&&(\
c=b,b=!1);b=b||u\
;var e=xc.exec(a\
);c=!c&&[];if(e)\
return[b.createE\
lement(e[1])];e=\
d.buildFragment(\
[a],b,c);c&&c.le\
ngth&&d(c).remov\
e();return d.mer\
ge([],\x0ae.childNo\
des)};var Sc=d.f\
n.load;d.fn.load\
=function(a,b,c)\
{if(\x22string\x22!==t\
ypeof a&&Sc)retu\
rn Sc.apply(this\
,arguments);var \
e,f,h,n=this,j=a\
.indexOf(\x22 \x22);0<\
=j&&(e=a.slice(j\
,a.length),a=a.s\
lice(0,j));d.isF\
unction(b)?(c=b,\
b=void 0):b&&\x22ob\
ject\x22===typeof b\
&&(h=\x22POST\x22);0<n\
.length&&d.ajax(\
{url:a,type:h,da\
taType:\x22html\x22,da\
ta:b}).done(func\
tion(a){f=argume\
nts;n.html(e?d(\x22\
<div>\x22).append(d\
.parseHTML(a)).f\
ind(e):a)}).comp\
lete(c&&function\
(a,b){n.each(c,f\
||[a.responseTex\
t,b,a])});return\
 this};d.expr.fi\
lters.animated=\x0a\
function(a){retu\
rn d.grep(d.time\
rs,function(b){r\
eturn a===b.elem\
}).length};var T\
c=c.document.doc\
umentElement;d.o\
ffset={setOffset\
:function(a,b,c)\
{var e,f,h,n=d.c\
ss(a,\x22position\x22)\
,j=d(a),l={};\x22st\
atic\x22===n&&(a.st\
yle.position=\x22re\
lative\x22);h=j.off\
set();f=d.css(a,\
\x22top\x22);e=d.css(a\
,\x22left\x22);(\x22absol\
ute\x22===n||\x22fixed\
\x22===n)&&-1<d.inA\
rray(\x22auto\x22,[f,e\
])?(e=j.position\
(),f=e.top,e=e.l\
eft):(f=parseFlo\
at(f)||0,e=parse\
Float(e)||0);d.i\
sFunction(b)&&(b\
=b.call(a,c,h));\
null!=b.top&&(l.\
top=b.top-h.top+\
f);null!=b.left&\
&(l.left=\x0ab.left\
-h.left+e);\x22usin\
g\x22in b?b.using.c\
all(a,l):j.css(l\
)}};d.fn.extend(\
{offset:function\
(a){if(arguments\
.length)return v\
oid 0===a?this:t\
his.each(functio\
n(b){d.offset.se\
tOffset(this,a,b\
)});var b,c,e={t\
op:0,left:0},f=(\
c=this[0])&&c.ow\
nerDocument;if(f\
){b=f.documentEl\
ement;if(!d.cont\
ains(b,c))return\
 e;typeof c.getB\
oundingClientRec\
t!==N&&(e=c.getB\
oundingClientRec\
t());c=jc(f);ret\
urn{top:e.top+(c\
.pageYOffset||b.\
scrollTop)-(b.cl\
ientTop||0),left\
:e.left+(c.pageX\
Offset||b.scroll\
Left)-(b.clientL\
eft||0)}}},posit\
ion:function(){i\
f(this[0]){var a\
,\x0ab,c={top:0,lef\
t:0},e=this[0];\x22\
fixed\x22===d.css(e\
,\x22position\x22)?b=e\
.getBoundingClie\
ntRect():(a=this\
.offsetParent(),\
b=this.offset(),\
d.nodeName(a[0],\
\x22html\x22)||(c=a.of\
fset()),c.top+=d\
.css(a[0],\x22borde\
rTopWidth\x22,!0),c\
.left+=d.css(a[0\
],\x22borderLeftWid\
th\x22,!0));return{\
top:b.top-c.top-\
d.css(e,\x22marginT\
op\x22,!0),left:b.l\
eft-c.left-d.css\
(e,\x22marginLeft\x22,\
!0)}}},offsetPar\
ent:function(){r\
eturn this.map(f\
unction(){for(va\
r a=this.offsetP\
arent||Tc;a&&!d.\
nodeName(a,\x22html\
\x22)&&\x22static\x22===d\
.css(a,\x22position\
\x22);)a=a.offsetPa\
rent;return a||\x0a\
Tc})}});d.each({\
scrollLeft:\x22page\
XOffset\x22,scrollT\
op:\x22pageYOffset\x22\
},function(a,b){\
var c=/Y/.test(b\
);d.fn[a]=functi\
on(e){return ma(\
this,function(a,\
e,f){var h=jc(a)\
;if(void 0===f)r\
eturn h?b in h?h\
[b]:h.document.d\
ocumentElement[e\
]:a[e];h?h.scrol\
lTo(!c?f:d(h).sc\
rollLeft(),c?f:d\
(h).scrollTop())\
:a[e]=f},a,e,arg\
uments.length,nu\
ll)}});d.each([\x22\
top\x22,\x22left\x22],fun\
ction(a,b){d.css\
Hooks[b]=Xb(s.pi\
xelPosition,func\
tion(a,c){if(c)r\
eturn c=ia(a,b),\
Ia.test(c)?d(a).\
position()[b]+\x22p\
x\x22:c})});d.each(\
{Height:\x22height\x22\
,Width:\x22width\x22},\
\x0afunction(a,b){d\
.each({padding:\x22\
inner\x22+a,content\
:b,\x22\x22:\x22outer\x22+a}\
,function(c,e){d\
.fn[e]=function(\
e,f){var h=argum\
ents.length&&(c|\
|\x22boolean\x22!==typ\
eof e),n=c||(!0=\
==e||!0===f?\x22mar\
gin\x22:\x22border\x22);r\
eturn ma(this,fu\
nction(b,c,e){re\
turn d.isWindow(\
b)?b.document.do\
cumentElement[\x22c\
lient\x22+a]:9===b.\
nodeType?(c=b.do\
cumentElement,Ma\
th.max(b.body[\x22s\
croll\x22+a],c[\x22scr\
oll\x22+a],b.body[\x22\
offset\x22+a],c[\x22of\
fset\x22+a],c[\x22clie\
nt\x22+a])):void 0=\
==e?d.css(b,c,n)\
:d.style(b,c,e,n\
)},b,h?e:void 0,\
h,null)}})});d.f\
n.size=function(\
){return this.le\
ngth};\x0ad.fn.andS\
elf=d.fn.addBack\
;\x22function\x22===ty\
peof define&&def\
ine.amd&&define(\
\x22jquery\x22,[],func\
tion(){return d}\
);var Zd=c.jQuer\
y,$d=c.$;d.noCon\
flict=function(a\
){c.$===d&&(c.$=\
$d);a&&c.jQuery=\
==d&&(c.jQuery=Z\
d);return d};typ\
eof m===N&&(c.jQ\
uery=c.$=d);retu\
rn d});\x0a(functio\
n(c){function m(\
c){try{return c?\
new window.Activ\
eXObject(\x22Micros\
oft.XMLHTTP\x22):ne\
w window.XMLHttp\
Request}catch(j)\
{}}c.ajaxSetting\
s.xhr=void 0===w\
indow.ActiveXObj\
ect?m:function()\
{return(this.url\
==document.locat\
ion||0==this.url\
.indexOf(\x22http\x22)\
||!this.isLocal)\
&&/^(get|post|he\
ad|put|delete|op\
tions)$/i.test(t\
his.type)&&m()||\
m(1)};c.ajaxTran\
sport(\x22+script\x22,\
function(c){var \
j,l=document.hea\
d||jQuery(\x22head\x22\
)[0]||document.d\
ocumentElement;r\
eturn{send:funct\
ion(m,p){j=docum\
ent.createElemen\
t(\x22script\x22);c.sc\
riptCharset&&\x0a(j\
.charset=c.scrip\
tCharset);j.src=\
c.url;j.onload=j\
.onreadystatecha\
nge=function(c,h\
){if(h||!j.ready\
State||/loaded|c\
omplete/.test(j.\
readyState))j.on\
load=j.onreadyst\
atechange=null,j\
.parentNode&&j.p\
arentNode.remove\
Child(j),j=null,\
h||p(200,\x22succes\
s\x22)};l.insertBef\
ore(j,l.firstChi\
ld)},abort:funct\
ion(){if(j)j.onl\
oad(void 0,!0)}}\
});c.extend(c.su\
pport,{iecors:!!\
window.XDomainRe\
quest});c.suppor\
t.iecors?c.ajaxT\
ransport(functio\
n(c){return{send\
:function(j,l){v\
ar m=new window.\
XDomainRequest;m\
.onload=function\
(){l(200,\x0a\x22OK\x22,{\
text:m.responseT\
ext},{\x22Content-T\
ype\x22:m.contentTy\
pe})};c.xhrField\
s&&(m.onerror=c.\
xhrFields.error,\
m.ontimeout=c.xh\
rFields.timeout)\
;m.open(c.type,c\
.url);m.send(c.h\
asContent&&c.dat\
a||null)},abort:\
function(){xdr.a\
bort()}}}):(c.aj\
axSetup({accepts\
:{binary:\x22text/p\
lain; charset=x-\
user-defined\x22},r\
esponseFields:{b\
inary:\x22response\x22\
}}),c.ajaxTransp\
ort(\x22binary\x22,fun\
ction(c){var j;r\
eturn{send:funct\
ion(l,m){var p=c\
.xhr();console.l\
og(\x22xhr.open bin\
ary async=\x22+c.as\
ync+\x22 url=\x22+c.ur\
l);p.open(c.type\
,c.url,c.async);\
\x0avar v=!1;try{p.\
hasOwnProperty(\x22\
responseType\x22)&&\
(p.responseType=\
\x22arraybuffer\x22,v=\
!0)}catch(w){}tr\
y{!v&&p.override\
MimeType&&p.over\
rideMimeType(\x22te\
xt/plain; charse\
t=x-user-defined\
\x22)}catch(b){}!c.\
crossDomain&&!l[\
\x22X-Requested-Wit\
h\x22]&&(l[\x22X-Reque\
sted-With\x22]=\x22XML\
HttpRequest\x22);tr\
y{for(var e in l\
)p.setRequestHea\
der(e,l[e])}catc\
h(f){}p.send(c.h\
asContent&&c.dat\
a||null);j=funct\
ion(){var b=p.st\
atus,e=\x22\x22,f=p.ge\
tAllResponseHead\
ers(),l={};try{i\
f(j&&4===p.ready\
State){j=void 0;\
try{l.text=\x22stri\
ng\x22===typeof p.r\
esponseText?\x0ap.r\
esponseText:null\
}catch(v){}try{l\
.binary=p.respon\
se}catch(w){}try\
{e=p.statusText}\
catch(jb){e=\x22\x22}!\
b&&c.isLocal&&!c\
.crossDomain?b=l\
.text?200:404:12\
23===b&&(b=204);\
m(b,e,l,f)}}catc\
h(xa){alert(xa),\
m(-1,xa)}};c.asy\
nc?4===p.readySt\
ate?setTimeout(j\
):p.onreadystate\
change=j:j()},ab\
ort:function(){}\
}}))})(jQuery);\x0a\
(function(c,m,h,\
j){function l(h,\
l){function v(b)\
{c(w).each(funct\
ion(){self.Jmol&\
&(0<=l.indexOf(\x22\
mouseup\x22)||0<=l.\
indexOf(\x22touchen\
d\x22))&&Jmol._setM\
ouseOwner(null);\
var f=c(this);th\
is!==b.target&&!\
f.has(b.target).\
length&&f.trigge\
rHandler(l,[b.ta\
rget,b])})}l=l||\
h+j;var w=c(),b=\
h+\x22.\x22+l+\x22-specia\
l-event\x22;c.event\
.special[l]={set\
up:function(){w=\
w.add(this);1===\
w.length&&c(m).b\
ind(b,v)},teardo\
wn:function(){se\
lf.Jmol&&Jmol._s\
etMouseOwner(nul\
l);w=w.not(this)\
;0===w.length&&c\
(m).unbind(b)},a\
dd:function(b){v\
ar c=\x0ab.handler;\
b.handler=functi\
on(b,e){b.target\
=e;c.apply(this,\
arguments)}}}}c.\
map(h.split(\x22 \x22)\
,function(c){l(c\
)});l(\x22focusin\x22,\
\x22focus\x22+j);l(\x22fo\
cusout\x22,\x22blur\x22+j\
)})(jQuery,docum\
ent,\x22click mouse\
move mouseup tou\
chmove touchend\x22\
,\x22outjsmol\x22);\x22un\
defined\x22==typeof\
 jQuery&&alert(\x22\
Note -- JSmoljQu\
ery is required \
for JSmol, but i\
t's not defined.\
\x22);self.Jmol||(J\
mol={});\x0aJmol._v\
ersion||(Jmol=fu\
nction(c){var m=\
function(c){retu\
rn{rear:c++,head\
er:c++,main:c++,\
image:c++,front:\
c++,fileOpener:c\
++,coverImage:c+\
+,dialog:c++,men\
u:c+9E4,console:\
c+91E3,consoleIm\
age:c+91001,moni\
torZIndex:c+9999\
9}},m={_version:\
\x22$Date: 2016-05-\
08 13:20:27 -050\
0 (Sun, 08 May 2\
016) $\x22,_alertNo\
Binary:!0,_allow\
edJmolSize:[25,2\
048,300],_applet\
CssClass:\x22\x22,_app\
letCssText:\x22\x22,_f\
ileCache:null,_j\
arFile:null,_j2s\
Path:null,_use:n\
ull,_j2sLoadMoni\
torOpacity:90,_a\
pplets:{},_async\
hronous:!0,_ajax\
Queue:[],_persis\
tentMenu:!1,\x0a_ge\
tZOrders:m,_z:m(\
Jmol.z||9E3),_de\
bugCode:!0,db:{_\
databasePrefixes\
:\x22$=:\x22,_fileLoad\
Script:\x22;if (_lo\
adScript = '' &&\
 defaultLoadScri\
pt == '' && _fil\
etype == 'Pdb') \
{ select protein\
 or nucleic;cart\
oons Only;color \
structure; selec\
t * };\x22,_nciLoad\
Script:\x22;n = ({m\
olecule=1}.lengt\
h < {molecule=2}\
.length ? 2 : 1)\
; select molecul\
e=n;display sele\
cted;center sele\
cted;\x22,_pubChemL\
oadScript:\x22\x22,_Di\
rectDatabaseCall\
s:{\x22cactus.nci.n\
ih.gov\x22:null,\x22.x\
3dna.org\x22:null,\x22\
rruff.geo.arizon\
a.edu\x22:null,\x22.rc\
sb.org\x22:null,\x22ft\
p.wwpdb.org\x22:nul\
l,\x0a\x22pdbe.org\x22:nu\
ll,\x22materialspro\
ject.org\x22:null,\x22\
.ebi.ac.uk\x22:null\
,\x22pubchem.ncbi.n\
lm.nih.gov\x22:null\
,\x22http://www.nmr\
db.org/tools/jmo\
l/predict.php\x22:n\
ull,$:\x22https://c\
actus.nci.nih.go\
v/chemical/struc\
ture/%FILENCI/fi\
le?format=sdf&ge\
t3d=True\x22,$$:\x22ht\
tps://cactus.nci\
.nih.gov/chemica\
l/structure/%FIL\
ENCI/file?format\
=sdf\x22,\x22=\x22:\x22http:\
//files.rcsb.org\
/view/%FILE.pdb\x22\
,\x22*\x22:\x22http://www\
.ebi.ac.uk/pdbe/\
entry-files/down\
load/%FILE.cif\x22,\
\x22==\x22:\x22http://www\
.rcsb.org/pdb/fi\
les/ligand/%FILE\
.cif\x22,\x22:\x22:\x22https\
://pubchem.ncbi.\
nlm.nih.gov/rest\
/pug/compound/%F\
ILE/SDF?record_t\
ype=3d\x22},\x0a_restQ\
ueryUrl:\x22http://\
www.rcsb.org/pdb\
/rest/search\x22,_r\
estQueryXml:\x22<or\
gPdbQuery><query\
Type>org.pdb.que\
ry.simple.Advanc\
edKeywordQuery</\
queryType><descr\
iption>Text Sear\
ch</description>\
<keywords>QUERY<\
/keywords></orgP\
dbQuery>\x22,_restR\
eportUrl:\x22http:/\
/www.pdb.org/pdb\
/rest/customRepo\
rt?pdbids=IDLIST\
&customReportCol\
umns=structureId\
,structureTitle\x22\
},_debugAlert:!1\
,_document:c,_is\
XHTML:!1,_lastAp\
pletID:null,_mou\
sePageX:null,_mo\
useOwner:null,_s\
erverUrl:\x22http:/\
/your.server.her\
e/jsmol.php\x22,_sy\
ncId:(\x22\x22+Math.ra\
ndom()).substrin\
g(3),\x0a_touching:\
!1,_XhtmlElement\
:null,_XhtmlAppe\
ndChild:!1};c=c.\
location.href.to\
LowerCase();m._h\
ttpProto=0==c.in\
dexOf(\x22https\x22)?\x22\
https://\x22:\x22http:\
//\x22;m._isFile=0=\
=c.indexOf(\x22file\
:\x22);m._isFile&&$\
.ajaxSetup({mime\
Type:\x22text/plain\
\x22});m._ajaxTestS\
ite=m._httpProto\
+\x22google.com\x22;c=\
m._isFile||0==c.\
indexOf(\x22http://\
localhost\x22)||0==\
c.indexOf(\x22http:\
//127.\x22);m._trac\
ker=\x22http://\x22==m\
._httpProto&&!c&\
&\x22http://chemapp\
s.stolaf.edu/jmo\
l/JmolTracker.ht\
m?id=UA-45940799\
-1\x22;m._isChrome=\
0<=navigator.use\
rAgent.toLowerCa\
se().indexOf(\x22ch\
rome\x22);\x0am._isSaf\
ari=!m._isChrome\
&&0<=navigator.u\
serAgent.toLower\
Case().indexOf(\x22\
safari\x22);m._isMs\
ie=void 0!==wind\
ow.ActiveXObject\
;m._isEdge=0<=na\
vigator.userAgen\
t.indexOf(\x22Edge/\
\x22);m._useDataURI\
=!m._isSafari&&!\
m._isMsie&&!m._i\
sEdge;window.req\
uestAnimationFra\
me||(window.requ\
estAnimationFram\
e=window.setTime\
out);for(var h i\
n Jmol)m[h]=Jmol\
[h];return m}(do\
cument,Jmol));\x0a(\
function(c,m){c.\
__$=m;m(document\
).ready(function\
(){c._document=n\
ull});c.$=functi\
on(b,c){null==b&\
&alert(c+argumen\
ts.callee.caller\
.toString());ret\
urn m(c?\x22#\x22+b._i\
d+\x22_\x22+c:b)};c._$\
=function(b){ret\
urn\x22string\x22==typ\
eof b?m(\x22#\x22+b):b\
};c.$ajax=functi\
on(b){c._ajaxCal\
l=b.url;b.cache=\
\x22NO\x22!=b.cache;b.\
url=c._fixProtoc\
ol(b.url);return\
 m.ajax(b)};c._f\
ixProtocol=funct\
ion(b){return 0=\
=b.indexOf(\x22http\
://www.rcsb.org/\
pdb/files/\x22)&&0>\
b.indexOf(\x22/liga\
nd/\x22)?\x22http://fi\
les.rcsb.org/vie\
w/\x22+b.substring(\
30).replace(/\x5c.g\
z/,\x22\x22):\x0a0==b.ind\
exOf(\x22http://\x22)&\
&(0==b.indexOf(\x22\
http://pubchem\x22)\
||0==b.indexOf(\x22\
http://cactus\x22)|\
|0==b.indexOf(\x22h\
ttp://www.materi\
alsproject\x22))?\x22h\
ttps\x22+b.substrin\
g(4):b};c._getNC\
IInfo=function(b\
,e){return c._ge\
tFileData(\x22https\
://cactus.nci.ni\
h.gov/chemical/s\
tructure/\x22+b+\x22/\x22\
+(\x22name\x22==e?\x22nam\
es\x22:e))};c.$appE\
vent=function(b,\
e,f,h){b=c.$(b,e\
);b.off(f)&&h&&b\
.on(f,h)};c.$res\
ize=function(b){\
return m(window)\
.resize(b)};c.$a\
fter=function(b,\
c){return m(b).a\
fter(c)};c.$appe\
nd=function(b,c)\
{return m(b).app\
end(c)};c.$bind=\
\x0afunction(b,c,f)\
{return f?m(b).b\
ind(c,f):m(b).un\
bind(c)};c.$clos\
est=function(b,c\
){return m(b).cl\
osest(c)};c.$get\
=function(b,c){r\
eturn m(b).get(c\
)};c.$documentOf\
f=function(b,c){\
return m(documen\
t).off(b,\x22#\x22+c)}\
;c.$documentOn=f\
unction(b,c,f){r\
eturn m(document\
).on(b,\x22#\x22+c,f)}\
;c.$getAncestorD\
iv=function(b,c)\
{return m(\x22div.\x22\
+c+\x22:has(#\x22+b+\x22)\
\x22)[0]};c.$suppor\
tsIECrossDomainS\
cripting=functio\
n(){return m.sup\
port.iecors};c.$\
attr=function(b,\
e,f){return c._$\
(b).attr(e,f)};c\
.$css=function(b\
,e){return c._$(\
b).css(e)};\x0ac.$f\
ind=function(b,e\
){return c._$(b)\
.find(e)};c.$foc\
us=function(b){r\
eturn c._$(b).fo\
cus()};c.$html=f\
unction(b,e){ret\
urn c._$(b).html\
(e)};c.$offset=f\
unction(b){retur\
n c._$(b).offset\
()};c.$windowOn=\
function(b,c){re\
turn m(window).o\
n(b,c)};c.$prop=\
function(b,e,f){\
var h=c._$(b);re\
turn 3==argument\
s.length?h.prop(\
e,f):h.prop(e)};\
c.$remove=functi\
on(b){return c._\
$(b).remove()};c\
.$scrollTo=funct\
ion(b,e){var f=c\
._$(b);return f.\
scrollTop(0>e?f[\
0].scrollHeight:\
e)};c.$setEnable\
d=function(b,e){\
return c._$(b).a\
ttr(\x22disabled\x22,\x0a\
e?null:\x22disabled\
\x22)};c.$getSize=f\
unction(b){b=c._\
$(b);return[b.wi\
dth(),b.height()\
]};c.$setSize=fu\
nction(b,e,f){re\
turn c._$(b).wid\
th(e).height(f)}\
;c.$is=function(\
b,e){return c._$\
(b).is(e)};c.$se\
tVisible=functio\
n(b,e){var f=c._\
$(b);return e?f.\
show():f.hide()}\
;c.$submit=funct\
ion(b){return c.\
_$(b).submit()};\
c.$val=function(\
b,e){var f=c._$(\
b);return 1==arg\
uments.length?f.\
val():f.val(e)};\
c._clearVars=fun\
ction(){delete j\
Query;delete m;d\
elete c;delete S\
wingController;d\
elete J;delete J\
M;delete JS;dele\
te JSV;\x0adelete J\
U;delete JV;dele\
te java;delete j\
avajs;delete Cla\
zz;delete c$};va\
r h=document,j=w\
indow,l={};l.ua=\
navigator.userAg\
ent.toLowerCase(\
);var r;a:{r=[\x22l\
inux\x22,\x22unix\x22,\x22ma\
c\x22,\x22win\x22];for(va\
r p=r.length;p--\
;)if(-1!=l.ua.in\
dexOf(r[p])){r=r\
[p];break a}r=\x22u\
nknown\x22}l.os=r;l\
.browser=functio\
n(){for(var b=l.\
ua,c=\x22konqueror \
webkit omniweb o\
pera webtv icab \
msie mozilla\x22.sp\
lit(\x22 \x22),f=0;f<c\
.length;f++)if(0\
<=b.indexOf(c[f]\
))return c[f];re\
turn\x22unknown\x22};l\
.browserName=l.b\
rowser();l.brows\
erVersion=parseF\
loat(l.ua.substr\
ing(l.ua.indexOf\
(l.browserName)+\
\x0al.browserName.l\
ength+1));l.supp\
ortsXhr2=functio\
n(){return m.sup\
port.cors||m.sup\
port.iecors};l.a\
llowDestroy=\x22msi\
e\x22!=l.browserNam\
e;l.allowHTML5=\x22\
msie\x22!=l.browser\
Name||0>navigato\
r.appVersion.ind\
exOf(\x22MSIE 8\x22);l\
.getDefaultLangu\
age=function(){r\
eturn navigator.\
language||naviga\
tor.userLanguage\
||\x22en-US\x22};l._we\
bGLtest=0;l.supp\
ortsWebGL=functi\
on(){if(!c.featu\
reDetection._web\
GLtest){var b;c.\
featureDetection\
._webGLtest=j.We\
bGLRenderingCont\
ext&&((b=h.creat\
eElement(\x22canvas\
\x22)).getContext(\x22\
webgl\x22)||b.getCo\
ntext(\x22experimen\
tal-webgl\x22))?\x0a1:\
-1}return 0<c.fe\
atureDetection._\
webGLtest};l.sup\
portsLocalizatio\
n=function(){for\
(var b=h.getElem\
entsByTagName(\x22m\
eta\x22),c=b.length\
;0<=--c;)if(0<=b\
[c].outerHTML.to\
LowerCase().inde\
xOf(\x22utf-8\x22))ret\
urn!0;return!1};\
l.supportsJava=f\
unction(){c.feat\
ureDetection._ja\
vaEnabled||(c.fe\
atureDetection._\
javaEnabled=c._i\
sMsie?navigator.\
javaEnabled()?1:\
-1:navigator.jav\
aEnabled()&&(!na\
vigator.mimeType\
s||navigator.mim\
eTypes[\x22applicat\
ion/x-java-apple\
t\x22])?1:-1);retur\
n 0<c.featureDet\
ection._javaEnab\
led};l.compliant\
Browser=\x0afunctio\
n(){var b=!!h.ge\
tElementById,c=l\
.os;if(\x22opera\x22==\
l.browserName&&7\
.54>=l.browserVe\
rsion&&\x22mac\x22==c|\
|\x22webkit\x22==l.bro\
wserName&&125.12\
>l.browserVersio\
n||\x22msie\x22==l.bro\
wserName&&\x22mac\x22=\
=c||\x22konqueror\x22=\
=l.browserName&&\
3.3>=l.browserVe\
rsion)b=!1;retur\
n b};l.isFullyCo\
mpliant=function\
(){return l.comp\
liantBrowser()&&\
l.supportsJava()\
};l.useIEObject=\
\x22win\x22==l.os&&\x22ms\
ie\x22==l.browserNa\
me&&5.5<=l.brows\
erVersion;l.useH\
tml4Object=\x22mozi\
lla\x22==l.browserN\
ame&&5<=l.browse\
rVersion||\x22opera\
\x22==l.browserName\
&&8<=l.browserVe\
rsion||\x0a\x22webkit\x22\
==l.browserName;\
l.hasFileReader=\
j.File&&j.FileRe\
ader;c.featureDe\
tection=l;c._aja\
x=function(b){if\
(!b.async)return\
 c.$ajax(b).resp\
onseText;c._ajax\
Queue.push(b);1=\
=c._ajaxQueue.le\
ngth&&c._ajaxDon\
e()};c._ajaxDone\
=function(){var \
b=c._ajaxQueue.s\
hift();b&&c.$aja\
x(b)};c._grabber\
Options=[[\x22$\x22,\x22N\
CI(small molecul\
es)\x22],[\x22:\x22,\x22PubC\
hem(small molecu\
les)\x22],[\x22=\x22,\x22RCS\
B(macromolecules\
)\x22],[\x22*\x22,\x22PDBe(m\
acromolecules)\x22]\
];c._getGrabberO\
ptions=function(\
b){if(0==c._grab\
berOptions.lengt\
h)return\x22\x22;var e\
='<input type=\x22t\
ext\x22 id=\x22ID_quer\
y\x22 onfocus=\x22jQue\
ry(this).select(\
)\x22 onkeypress=\x22i\
f(13==event.whic\
h){Jmol._applets\
[\x5c'ID\x5c']._search\
();return false}\
\x22 size=\x2232\x22 valu\
e=\x22\x22 />',\x0af='<bu\
tton id=\x22ID_subm\
it\x22 onclick=\x22Jmo\
l._applets[\x5c'ID\x5c\
']._search()\x22>Se\
arch</button></n\
obr>';1==c._grab\
berOptions.lengt\
h?(e=\x22<nobr>\x22+e+\
'<span style=\x22di\
splay:none\x22>',f=\
\x22</span>\x22+f):e+=\
\x22<br /><nobr>\x22;f\
or(var e=e+'<sel\
ect id=\x22ID_selec\
t\x22>',h=0;h<c._gr\
abberOptions.len\
gth;h++)var j=c.\
_grabberOptions[\
h],e=e+('<option\
 value=\x22'+j[0]+'\
\x22 '+(0==h?\x22selec\
ted\x22:\x22\x22)+\x22>\x22+j[1\
]+\x22</option>\x22);e\
=(e+\x22</select>\x22+\
f).replace(/ID/g\
,b._id);return\x22<\
br />\x22+e};c._get\
ScriptForDatabas\
e=function(b){re\
turn\x22$\x22==b?c.db.\
_nciLoadScript:\x0a\
\x22:\x22==b?c.db._pub\
ChemLoadScript:c\
.db._fileLoadScr\
ipt};c._setInfo=\
function(b,c,f){\
var h=[],j=\x22\x22;if\
(0==f.indexOf(\x22E\
RROR\x22))j=f;else \
switch(c){case \x22\
=\x22:c=f.split(\x22<d\
imStructure.stru\
ctureId>\x22);h=[\x22<\
table>\x22];for(f=1\
;f<c.length;f++)\
h.push('<tr><td \
valign=top><a hr\
ef=\x22javascript:J\
mol.search('+b._\
id+\x22,'=\x22+c[f].su\
bstring(0,4)+\x22')\
\x5c\x22>\x22+c[f].substr\
ing(0,4)+\x22</a></\
td>\x22),h.push(\x22<t\
d>\x22+c[f].split(\x22\
Title>\x22)[1].spli\
t(\x22</\x22)[0]+\x22</td\
></tr>\x22);h.push(\
\x22</table>\x22);j=c.\
length-1+\x22 match\
es\x22;break;case \x22\
$\x22:case \x22:\x22:brea\
k;default:return\
}b._infoHeader=\x0a\
j;b._info=h.join\
(\x22\x22);b._showInfo\
(!0)};c._loadSuc\
cess=function(b,\
e){e&&(c._ajaxDo\
ne(),e(b))};c._l\
oadError=functio\
n(b){c._ajaxDone\
();c.say(\x22Error \
connecting to se\
rver: \x22+c._ajaxC\
all);null!=b&&b(\
)};c._isDatabase\
Call=function(b)\
{return 0<=c.db.\
_databasePrefixe\
s.indexOf(b.subs\
tring(0,1))};c._\
getDirectDatabas\
eCall=function(b\
,e){if(e&&!c.fea\
tureDetection.su\
pportsXhr2())ret\
urn b;var f=2,h=\
b.substring(0,f)\
,j=c.db._DirectD\
atabaseCalls[h]|\
|c.db._DirectDat\
abaseCalls[h=b.s\
ubstring(0,--f)]\
;j&&(\x22:\x22==h?(h=b\
.toLowerCase(),\x0a\
isNaN(parseInt(b\
.substring(1)))?\
0==h.indexOf(\x22:s\
miles:\x22)?(j+=\x22?P\
OST?smiles=\x22+b.s\
ubstring(8),b=\x22s\
miles\x22):0==h.ind\
exOf(\x22:cid:\x22)?b=\
\x22cid/\x22+b.substri\
ng(5):(0==h.inde\
xOf(\x22:name:\x22)?b=\
b.substring(5):0\
==h.indexOf(\x22:ca\
s:\x22)&&(b=b.subst\
ring(4)),b=\x22name\
/\x22+encodeURIComp\
onent(b.substrin\
g(f))):b=\x22cid/\x22+\
b.substring(1)):\
b=encodeURICompo\
nent(b.substring\
(f)),0<=b.indexO\
f(\x22.mmtf\x22)?b=\x22ht\
tp://mmtf.rcsb.o\
rg/full/\x22+b:0<=j\
.indexOf(\x22FILENC\
I\x22)?(b=b.replace\
(/\x5c%2F/g,\x22/\x22),b=\
j.replace(/\x5c%FIL\
ENCI/,b)):b=j.re\
place(/\x5c%FILE/,b\
));return b};\x0ac.\
_getRawDataFromS\
erver=function(b\
,e,f,h,j,l){b=\x22?\
call=getRawDataF\
romDatabase&data\
base=\x22+b+(0<=e.i\
ndexOf(\x22?POST?\x22)\
?\x22?POST?\x22:\x22\x22)+\x22&\
query=\x22+encodeUR\
IComponent(e)+(j\
?\x22&encoding=base\
64\x22:\x22\x22)+(l?\x22\x22:\x22&\
script=\x22+encodeU\
RIComponent(c._g\
etScriptForDatab\
ase(b)));return \
c._contactServer\
(b,f,h)};c._chec\
kFileName=functi\
on(b,e,f){c._isD\
atabaseCall(e)&&\
(f&&c._setQueryT\
erm(b,e),e=c._ge\
tDirectDatabaseC\
all(e,!0),c._isD\
atabaseCall(e)&&\
(e=c._getDirectD\
atabaseCall(e,!1\
),f&&(f[0]=!0)))\
;return e};c._ch\
eckCache=functio\
n(b,\x0ae,f){if(b._\
cacheFiles&&c._f\
ileCache&&!e.end\
sWith(\x22.js\x22)){if\
(b=c._fileCache[\
e])return System\
.out.println(\x22us\
ing \x22+b.length+\x22\
 bytes of cached\
 data for \x22+e),f\
(b),null;f=funct\
ion(b,e){f(c._fi\
leCache[b]=e)}}r\
eturn f};c._play\
Audio=function(b\
){var c=document\
.createElement(\x22\
audio\x22);c.contro\
ls=\x22true\x22;c.src=\
b;c.play()};c._l\
oadFileData=func\
tion(b,e,f,h){va\
r j=[];e=c._chec\
kFileName(b,e,j)\
;f=c._checkCache\
(b,e,f);j[0]?c._\
getRawDataFromSe\
rver(\x22_\x22,e,f,h):\
(b={type:\x22GET\x22,d\
ataType:\x22text\x22,u\
rl:e,async:c._as\
ynchronous,\x0asucc\
ess:function(b){\
c._loadSuccess(b\
,f)},error:funct\
ion(){c._loadErr\
or(h)}},c._check\
AjaxPost(b),c._a\
jax(b))};c._getI\
nfoFromDatabase=\
function(b,e,f){\
if(\x22====\x22==e){va\
r h=c.db._restQu\
eryXml.replace(/\
QUERY/,f),h={dat\
aType:\x22text\x22,typ\
e:\x22POST\x22,content\
Type:\x22applicatio\
n/x-www-form-url\
encoded\x22,url:c.d\
b._restQueryUrl,\
data:encodeURICo\
mponent(h)+\x22&req\
=browser\x22,succes\
s:function(h){c.\
_ajaxDone();c._e\
xtractInfoFromRC\
SB(b,e,f,h)},err\
or:function(){c.\
_loadError(null)\
},async:c._async\
hronous};return \
c._ajax(h)}f=\x22?c\
all=getInfoFromD\
atabase&database\
=\x22+\x0ae+\x22&query=\x22+\
encodeURICompone\
nt(f);return c._\
contactServer(f,\
function(f){c._s\
etInfo(b,e,f)})}\
;c._extractInfoF\
romRCSB=function\
(b,e,f,h){var j=\
h.length/5;if(0!\
=j&&4==f.length&\
&1!=j){f=f.toUpp\
erCase();var l=h\
.indexOf(f);0<l&\
&0<=\x22123456789\x22.\
indexOf(f.substr\
ing(0,1))&&(h=f+\
\x22,\x22+h.substring(\
0,l)+h.substring\
(l+5));50<j&&(h=\
h.substring(0,25\
0));h=h.replace(\
/\x5cn/g,\x22,\x22);h=c._\
restReportUrl.re\
place(/IDLIST/,h\
);c._loadFileDat\
a(b,h,function(f\
){c._setInfo(b,e\
,f)})}};c._check\
AjaxPost=functio\
n(b){var c=b.url\
.indexOf(\x22?POST?\
\x22);\x0a0<c&&(b.data\
=b.url.substring\
(c+6),b.url=b.ur\
l.substring(0,c)\
,b.type=\x22POST\x22,b\
.contentType=\x22ap\
plication/x-www-\
form-urlencoded\x22\
)};c._contactSer\
ver=function(b,e\
,f){b={dataType:\
\x22text\x22,type:\x22GET\
\x22,url:c._serverU\
rl+b,success:fun\
ction(b){c._load\
Success(b,e)},er\
ror:function(){c\
._loadError(f)},\
async:e?c._async\
hronous:!1};c._c\
heckAjaxPost(b);\
return c._ajax(b\
)};c._setQueryTe\
rm=function(b,e)\
{if(e&&b._hasOpt\
ions&&\x22http://\x22!\
=e.substring(0,7\
)){if(c._isDatab\
aseCall(e)){var \
f=e.substring(0,\
1);e=e.substring\
(1);e.substring(\
0,\x0a1)==f&&0<=\x22=$\
\x22.indexOf(f)&&(e\
=e.substring(1))\
;var h=c._getEle\
ment(b,\x22select\x22)\
;if(h&&h.options\
)for(var j=0;j<h\
.options.length;\
j++)h[j].value==\
f&&(h[j].selecte\
d=!0)}c.$val(c.$\
(b,\x22query\x22),e)}}\
;c._search=funct\
ion(b,e,f){1<arg\
uments.length||(\
e=null);c._setQu\
eryTerm(b,e);e||\
(e=c.$val(c.$(b,\
\x22query\x22)));0==e.\
indexOf(\x22!\x22)?b._\
script(e.substri\
ng(1)):(e&&(e=e.\
replace(/\x5c\x22/g,\x22\x22\
)),b._showInfo(!\
1),c._searchMol(\
b,e,f,!0))};c._s\
earchMol=functio\
n(b,e,f,h){var j\
;c._isDatabaseCa\
ll(e)?(j=e.subst\
ring(0,1),e=e.su\
bstring(1)):\x0aj=b\
._hasOptions?c.$\
val(c.$(b,\x22selec\
t\x22)):\x22$\x22;\x22=\x22==j&\
&3==e.length&&(e\
=\x22=\x22+e);var l=j+\
e;if(e&&!(0>l.in\
dexOf(\x22?\x22)&&l==b\
._thisJmolModel)\
){b._thisJmolMod\
el=l;var m;h&&nu\
ll!=b._viewSet&&\
null!=(m=c.View.\
__findView(b._vi\
ewSet,{chemID:l}\
))?c.View.__setV\
iew(m,b,!1):(\x22$\x22\
==j||\x22:\x22==j?b._j\
molFileType=\x22MOL\
\x22:\x22=\x22==j&&(b._jm\
olFileType=\x22PDB\x22\
),b._searchDatab\
ase(e,j,f))}};c.\
_searchDatabase=\
function(b,e,f,h\
){b._showInfo(!1\
);return 0<=e.in\
dexOf(\x22?\x22)?(c._g\
etInfoFromDataba\
se(b,f,e.split(\x22\
?\x22)[0]),!0):c.db\
._DirectDatabase\
Calls[f]?\x0a(b._lo\
adFile(f+e,h),!0\
):!1};c._syncBin\
aryOK=\x22?\x22;c._can\
SyncBinary=funct\
ion(b){if(c._isA\
sync)return!0;if\
(self.VBArray)re\
turn c._syncBina\
ryOK=!1;if(\x22?\x22!=\
c._syncBinaryOK)\
return c._syncBi\
naryOK;c._syncBi\
naryOK=!0;try{va\
r e=new window.X\
MLHttpRequest;e.\
open(\x22text\x22,c._a\
jaxTestSite,!1);\
e.hasOwnProperty\
(\x22responseType\x22)\
?e.responseType=\
\x22arraybuffer\x22:e.\
overrideMimeType\
&&e.overrideMime\
Type(\x22text/plain\
; charset=x-user\
-defined\x22)}catch\
(f){return Syste\
m.out.println(\x22J\
SmolCore.js: syn\
chronous binary \
file transfer is\
 requested but n\
ot available\x22),\x0a\
c._alertNoBinary\
&&!b&&alert(\x22JSm\
olCore.js: synch\
ronous binary fi\
le transfer is r\
equested but not\
 available\x22),c._\
syncBinaryOK=!1}\
return!0};c._bin\
aryTypes=\x22mmtf .\
gz .jpg .gif .pn\
g .zip .jmol .bi\
n .smol .spartan\
 .mrc .map .ccp4\
 .dn6 .delphi .o\
map .pse .dcd\x22.s\
plit(\x22 \x22);c._isB\
inaryUrl=functio\
n(b){for(var e=c\
._binaryTypes.le\
ngth;0<=--e;)if(\
0<=b.indexOf(c._\
binaryTypes[e]))\
return!0;return!\
1};c._getFileDat\
a=function(b,e,f\
){var h=c._isBin\
aryUrl(b),j=0<=b\
.indexOf(\x22.gz\x22)&\
&0<=b.indexOf(\x22r\
csb.org\x22);j&&(b=\
b.replace(/\x5c.gz/\
,\x0a\x22\x22),h=!1);var \
j=h&&!e&&!c._can\
SyncBinary(j),l=\
0<=b.indexOf(\x22?P\
OST?\x22);0==b.inde\
xOf(\x22file:/\x22)&&0\
!=b.indexOf(\x22fil\
e:///\x22)&&(b=\x22fil\
e://\x22+b.substrin\
g(5));var m=0>b.\
indexOf(\x22://\x22)||\
0==b.indexOf(doc\
ument.location.p\
rotocol)&&0<=b.i\
ndexOf(document.\
location.host),r\
=\x22https://\x22==c._\
httpProto&&0==b.\
indexOf(\x22http://\
\x22),p=c._isDirect\
Call(b);!p&&0<=b\
.indexOf(\x22?ALLOW\
SORIGIN?\x22)&&(p=!\
0,b=b.replace(/\x5c\
?ALLOWSORIGIN\x5c?/\
,\x22\x22));var v=!m&&\
c.$supportsIECro\
ssDomainScriptin\
g(),w=null;if(r|\
|j||!m&&!p||!e&&\
v)w=c._getRawDat\
aFromServer(\x22_\x22,\
\x0ab,e,e,j,!0);els\
e{b=b.replace(/f\
ile:\x5c/\x5c/\x5c/\x5c//,\x22f\
ile://\x22);var F={\
dataType:h?\x22bina\
ry\x22:\x22text\x22,async\
:!!e};l?(F.type=\
\x22POST\x22,F.url=b.s\
plit(\x22?POST?\x22)[0\
],F.data=b.split\
(\x22?POST?\x22)[1]):(\
F.type=\x22GET\x22,F.u\
rl=b);e&&(F.succ\
ess=function(){e\
(c._xhrReturn(F.\
xhr))},F.error=f\
unction(){e(F.xh\
r.statusText)});\
F.xhr=c.$ajax(F)\
;e||(w=c._xhrRet\
urn(F.xhr))}if(!\
f)return w;null=\
=w&&(w=\x22\x22,h=!1);\
h&&(h=c._canSync\
Binary(!0));retu\
rn h?c._strToByt\
es(w):JU.SB.newS\
(w)};c._xhrRetur\
n=function(b){re\
turn!b.responseT\
ext||self.Clazz&\
&Clazz.instanceO\
f(b.response,\x0ase\
lf.ArrayBuffer)?\
b.response||b.st\
atusText:b.respo\
nseText};c._isDi\
rectCall=functio\
n(b){if(0<=b.ind\
exOf(\x22?ALLOWSORI\
GIN?\x22))return!0;\
for(var e in c.d\
b._DirectDatabas\
eCalls)if(0<=e.i\
ndexOf(\x22.\x22)&&0<=\
b.indexOf(e))ret\
urn!0;return!1};\
c._cleanFileData\
=function(b){ret\
urn 0<=b.indexOf\
(\x22\x5cr\x22)&&0<=b.ind\
exOf(\x22\x5cn\x22)?b.rep\
lace(/\x5cr\x5cn/g,\x22\x5cn\
\x22):0<=b.indexOf(\
\x22\x5cr\x22)?b.replace(\
/\x5cr/g,\x22\x5cn\x22):b};c\
._getFileType=fu\
nction(b){var c=\
b.substring(0,1)\
;if(\x22$\x22==c||\x22:\x22=\
=c)return\x22MOL\x22;i\
f(\x22=\x22==c)return\x22\
=\x22==b.substring(\
1,2)?\x22LCIF\x22:\x22PDB\
\x22;b=\x0ab.split(\x22.\x22\
).pop().toUpperC\
ase();return b.s\
ubstring(0,Math.\
min(b.length,3))\
};c._getZ=functi\
on(b,e){return b\
&&b._z&&b._z[e]|\
|c._z[e]};c._inc\
rZ=function(b,e)\
{return b&&b._z&\
&++b._z[e]||++c.\
_z[e]};c._hideLo\
calFileReader=fu\
nction(b){b._loc\
alReader&&c.$set\
Visible(b._local\
Reader,!1);b._re\
adingLocal=!1;c.\
_setCursor(b,0)}\
;c.loadFileFromD\
ialog=function(b\
){c._loadFileAsy\
nchronously(null\
,b,null,null)};c\
._loadFileAsynch\
ronously=functio\
n(b,e,f,h){if(f&\
&0!=f.indexOf(\x22?\
\x22)){var j=f;f=c.\
_checkFileName(e\
,f);var l=\x0afunct\
ion(l){c._setDat\
a(b,f,j,l,h,e)},\
l=c._checkCache(\
e,f,l);0<=f.inde\
xOf(\x22|\x22)&&(f=f.s\
plit(\x22|\x22)[0]);re\
turn null==l?nul\
l:c._getFileData\
(f,l)}if(!c.feat\
ureDetection.has\
FileReader)retur\
n b?b.setData(ms\
g,null,null,h,e)\
:alert(msg);e._l\
ocalReader||(l='\
<div id=\x22ID\x22 sty\
le=\x22z-index:'+c.\
_getZ(e,\x22fileOpe\
ner\x22)+';position\
:absolute;backgr\
ound:#E0E0E0;lef\
t:10px;top:10px\x22\
><div style=\x22mar\
gin:5px 5px 5px \
5px;\x22><button id\
=\x22ID_loadurl\x22>UR\
L</button><input\
 type=\x22file\x22 id=\
\x22ID_files\x22 /><bu\
tton id=\x22ID_load\
file\x22>load</butt\
on><button id=\x22I\
D_cancel\x22>cancel\
</button></div><\
div>',\x0ac.$after(\
\x22#\x22+e._id+\x22_appl\
etdiv\x22,l.replace\
(/ID/g,e._id+\x22_l\
ocalReader\x22)),e.\
_localReader=c.$\
(e,\x22localReader\x22\
));c.$appEvent(e\
,\x22localReader_lo\
adurl\x22,\x22click\x22);\
c.$appEvent(e,\x22l\
ocalReader_loadu\
rl\x22,\x22click\x22,func\
tion(){var b=pro\
mpt(\x22Enter a URL\
\x22);b&&(c._hideLo\
calFileReader(e,\
0),c._setData(nu\
ll,b,b,null,h,e)\
)});c.$appEvent(\
e,\x22localReader_l\
oadfile\x22,\x22click\x22\
);c.$appEvent(e,\
\x22localReader_loa\
dfile\x22,\x22click\x22,f\
unction(){var f=\
c.$(e,\x22localRead\
er_files\x22)[0].fi\
les[0],j=new Fil\
eReader;j.onload\
end=function(j){\
j.target.readySt\
ate==\x0aFileReader\
.DONE&&(c._hideL\
ocalFileReader(e\
,0),c._setData(b\
,f.name,f.name,j\
.target.result,h\
,e))};try{j.read\
AsArrayBuffer(f)\
}catch(l){alert(\
\x22You must select\
 a file first.\x22)\
}});c.$appEvent(\
e,\x22localReader_c\
ancel\x22,\x22click\x22);\
c.$appEvent(e,\x22l\
ocalReader_cance\
l\x22,\x22click\x22,funct\
ion(){c._hideLoc\
alFileReader(e);\
b&&b.setData(\x22#C\
ANCELED#\x22,null,n\
ull,h,e)});c.$se\
tVisible(e._loca\
lReader,!0);e._r\
eadingLocal=!0};\
c._setData=funct\
ion(b,e,f,h,j,l)\
{h&&(h=c._strToB\
ytes(h));null!=h\
&&(null==b||0<=e\
.indexOf(\x22.jdx\x22)\
)&&c.Cache.put(\x22\
cache://\x22+\x0ae,h);\
null==b?l._apple\
t.openFileAsyncS\
pecial(null==h?e\
:\x22cache://\x22+e,1)\
:b.setData(e,f,h\
,j)};c._doAjax=f\
unction(b,e,f){b\
=b.toString();if\
(null!=f)return \
c._saveFile(b,f)\
;e&&(b+=\x22?POST?\x22\
+e);return c._ge\
tFileData(b,null\
,!0)};c._saveFil\
e=function(b,e,f\
,h){if(c._localF\
ileSaveFunction&\
&c._localFileSav\
eFunction(b,e))r\
eturn\x22OK\x22;b=b.su\
bstring(b.lastIn\
dexOf(\x22/\x22)+1);f|\
|(f=0<=b.indexOf\
(\x22.pdf\x22)?\x22applic\
ation/pdf\x22:0<=b.\
indexOf(\x22.png\x22)?\
\x22image/png\x22:0<=b\
.indexOf(\x22.gif\x22)\
?\x22image/gif\x22:0<=\
b.indexOf(\x22.jpg\x22\
)?\x22image/jpg\x22:\x22\x22\
);\x0avar j=\x22string\
\x22==typeof e;j||(\
e=(JU?JU:J.util)\
.Base64.getBase6\
4(e).toString())\
;h||(h=j?\x22\x22:\x22bas\
e64\x22);(j=c._serv\
erUrl)&&0<=j.ind\
exOf(\x22your.serve\
r\x22)&&(j=\x22\x22);c._u\
seDataURI||!j?(h\
||(e=btoa(e)),h=\
document.createE\
lement(\x22a\x22),h.hr\
ef=\x22data:\x22+f+\x22;b\
ase64,\x22+e,h.type\
=f||\x22text/plain\x22\
,h.download=b,h.\
target=\x22_blank\x22,\
m(\x22body\x22).append\
(h),h.click(),h.\
remove()):(c._fo\
rmdiv||(c.$after\
(\x22body\x22,'<div id\
=\x22__jsmolformdiv\
__\x22 style=\x22displ\
ay:none\x22>\x5ct\x5ct\x5ct\x5c\
t\x5ct\x5ct<form id=\x22_\
_jsmolform__\x22 me\
thod=\x22post\x22 targ\
et=\x22_blank\x22 acti\
on=\x22\x22>\x5ct\x5ct\x5ct\x5ct\x5ct\
\x5ct<input name=\x22c\
all\x22 value=\x22save\
File\x22/>\x5ct\x5ct\x5ct\x5ct\x5c\
t\x5ct<input id=\x22__\
jsmolmimetype__\x22\
 name=\x22mimetype\x22\
 value=\x22\x22/>\x5ct\x5ct\x5c\
t\x5ct\x5ct\x5ct<input id\
=\x22__jsmolencodin\
g__\x22 name=\x22encod\
ing\x22 value=\x22\x22/>\x5c\
t\x5ct\x5ct\x5ct\x5ct\x5ct<inpu\
t id=\x22__jsmolfil\
ename__\x22 name=\x22f\
ilename\x22 value=\x22\
\x22/>\x5ct\x5ct\x5ct\x5ct\x5ct\x5ct<\
textarea id=\x22__j\
smoldata__\x22 name\
=\x22data\x22></textar\
ea>\x5ct\x5ct\x5ct\x5ct\x5ct\x5ct<\
/form>\x5ct\x5ct\x5ct\x5ct\x5ct\
\x5ct</div>'),\x0ac._f\
ormdiv=\x22__jsmolf\
orm__\x22),c.$attr(\
c._formdiv,\x22acti\
on\x22,j+\x22?\x22+(new D\
ate).getMillisec\
onds()),c.$val(\x22\
__jsmoldata__\x22,e\
),c.$val(\x22__jsmo\
lfilename__\x22,b),\
c.$val(\x22__jsmolm\
imetype__\x22,f),c.\
$val(\x22__jsmolenc\
oding__\x22,h),c.$s\
ubmit(\x22__jsmolfo\
rm__\x22),c.$val(\x22_\
_jsmoldata__\x22,\x22\x22\
),c.$val(\x22__jsmo\
lfilename__\x22,\x22\x22)\
);return\x22OK\x22};c.\
_strToBytes=func\
tion(b){if(Clazz\
.instanceOf(b,se\
lf.ArrayBuffer))\
return Clazz.new\
ByteArray(-1,b);\
for(var c=Clazz.\
newByteArray(b.l\
ength,0),f=b.len\
gth;0<=--f;)c[f]\
=b.charCodeAt(f)\
&255;return c};c\
._setConsoleDiv=\
\x0afunction(b){sel\
f.Clazz&&Clazz.s\
etConsoleDiv(b)}\
;c._registerAppl\
et=function(b,e)\
{return window[b\
]=c._applets[b]=\
c._applets[b+\x22__\
\x22+c._syncId+\x22__\x22\
]=e};c._readyCal\
lback=function(b\
,e,f,h,j){b=b.sp\
lit(\x22_object\x22)[0\
];var l=c._apple\
ts[b];if(f=f.boo\
leanValue?f.bool\
eanValue():f)l._\
appletPanel=j||h\
,l._applet=h;c._\
track(l._readyCa\
llback(b,e,f))};\
c._getWrapper=fu\
nction(b,e){var \
f;if(e){var h=\x22\x22\
;if(b._coverImag\
e)var h=' onclic\
k=\x22Jmol.coverApp\
let(ID, false)\x22 \
title=\x22'+b._cove\
rTitle+'\x22',j='<i\
mage id=\x22ID_cove\
rclickgo\x22 src=\x22'\
+\x0ab._makeLiveIma\
ge+'\x22 style=\x22wid\
th:25px;height:2\
5px;position:abs\
olute;bottom:10p\
x;left:10px;z-in\
dex:'+c._getZ(b,\
\x22coverImage\x22)+';\
opacity:0.5;\x22'+h\
+\x22 />\x22,h='<div i\
d=\x22ID_coverdiv\x22 \
style=\x22backgroun\
d-color:red;z-in\
dex:'+c._getZ(b,\
\x22coverImage\x22)+';\
width:100%;heigh\
t:100%;display:i\
nline;position:a\
bsolute;top:0px;\
left:0px\x22><image\
 id=\x22ID_coverima\
ge\x22 src=\x22'+b._co\
verImage+'\x22 styl\
e=\x22width:100%;he\
ight:100%\x22'+h+\x22/\
>\x22+j+\x22</div>\x22;j=\
b._isJava?\x22\x22:'<i\
mage id=\x22ID_wait\
image\x22 src=\x22'+b.\
_j2sPath+'/img/c\
ursor_wait.gif\x22 \
style=\x22display:n\
one;position:abs\
olute;bottom:10p\
x;left:10px;z-in\
dex:'+\x0ac._getZ(b\
,\x22coverImage\x22)+'\
;\x22 />';f=c._appl\
etCssText.replac\
e(/\x5c'/g,'\x22');var\
 l=b._getSpinner\
&&b._getSpinner(\
);b._spinner=l=!\
l||\x22none\x22==l?\x22\x22:\
\x22background-imag\
e:url(\x22+l+\x22); ba\
ckground-repeat:\
no-repeat; backg\
round-position:c\
enter;\x22;f=l+(0<=\
f.indexOf('style\
=\x22')?f.split('st\
yle=\x22')[1]:'\x22 '+\
f);f='...<div id\
=\x22ID_appletinfot\
ablediv\x22 style=\x22\
width:Wpx;height\
:Hpx;position:re\
lative;font-size\
:14px;text-align\
:left\x22>IMG WAIT.\
.....<div id=\x22ID\
_appletdiv\x22 styl\
e=\x22z-index:'+c._\
getZ(b,\x22header\x22)\
+\x22;width:100%;he\
ight:100%;positi\
on:absolute;top:\
0px;left:0px;\x22+\x0a\
f+\x22>\x22;var l=b._h\
eight,m=b._width\
;if(\x22string\x22!==t\
ypeof l||0>l.ind\
exOf(\x22%\x22))l+=\x22px\
\x22;if(\x22string\x22!==\
typeof m||0>m.in\
dexOf(\x22%\x22))m+=\x22p\
x\x22;f=f.replace(/\
IMG/,h).replace(\
/WAIT/,j).replac\
e(/Hpx/g,l).repl\
ace(/Wpx/g,m)}el\
se f='......</di\
v>......<div id=\
\x22ID_2dappletdiv\x22\
 style=\x22position\
:absolute;width:\
100%;height:100%\
;overflow:hidden\
;display:none\x22><\
/div>......<div \
id=\x22ID_infotable\
div\x22 style=\x22widt\
h:100%;height:10\
0%;position:abso\
lute;top:0px;lef\
t:0px\x22>.........\
<div id=\x22ID_info\
headerdiv\x22 style\
=\x22height:20px;wi\
dth:100%;backgro\
und:yellow;displ\
ay:none\x22><span i\
d=\x22ID_infoheader\
span\x22></span><sp\
an id=\x22ID_infoch\
eckboxspan\x22 styl\
e=\x22position:abso\
lute;text-align:\
right;right:1px;\
\x22><a href=\x22javas\
cript:Jmol.showI\
nfo(ID,false)\x22>[\
x]</a></span></d\
iv>.........<div\
 id=\x22ID_infodiv\x22\
 style=\x22position\
:absolute;top:20\
px;bottom:0px;wi\
dth:100%;height:\
100%;overflow:au\
to\x22></div>......\
</div>...</div>'\
;\x0areturn f.repla\
ce(/\x5c.\x5c.\x5c./g,\x22\x22)\
.replace(/[\x5cn\x5cr]\
/g,\x22\x22).replace(/\
ID/g,b._id)};c._\
hideLoadingSpinn\
er=function(b){b\
._spinner&&c.$cs\
s(c.$(b,\x22appletd\
iv\x22),{\x22backgroun\
d-image\x22:\x22\x22})};c\
._documentWrite=\
function(b){if(c\
._document){if(c\
._isXHTML&&!c._X\
htmlElement){var\
 e=document.getE\
lementsByTagName\
(\x22script\x22);c._Xh\
tmlElement=e.ite\
m(e.length-1);c.\
_XhtmlAppendChil\
d=!1}c._XhtmlEle\
ment?c._domWrite\
(b):c._document.\
write(b)}return \
b};c._domWrite=f\
unction(b){for(v\
ar e=[0];e[0]<b.\
length;){var f=c\
._getDomElement(\
b,e);if(!f)break\
;\x0ac._XhtmlAppend\
Child?c._XhtmlEl\
ement.appendChil\
d(f):c._XhtmlEle\
ment.parentNode.\
insertBefore(f,_\
jmol.XhtmlElemen\
t)}};c._getDomEl\
ement=function(b\
,c){var f=docume\
nt.createElement\
(\x22span\x22);f.inner\
HTML=b;c[0]=b.le\
ngth;return f};c\
._setObject=func\
tion(b,e,f){b._i\
d=e;b.__Info={};\
f.z&&f.zIndexBas\
e&&(c._z=c._getZ\
Orders(f.zIndexB\
ase));for(var h \
in f)b.__Info[h]\
=f[h];(b._z=f.z)\
||f.zIndexBase&&\
(b._z=b.__Info.z\
=c._getZOrders(f\
.zIndexBase));b.\
_width=f.width;b\
._height=f.heigh\
t;b._noscript=!b\
._isJava&&f.nosc\
ript;b._console=\
\x0af.console;b._ca\
cheFiles=!!f.cac\
heFiles;b._viewS\
et=null==f.viewS\
et||b._isJava?nu\
ll:\x22Set\x22+f.viewS\
et;null!=b._view\
Set&&(c.View.__i\
nit(b),b._curren\
tView=null);!c._\
fileCache&&b._ca\
cheFiles&&(c._fi\
leCache={});b._c\
onsole||(b._cons\
ole=b._id+\x22_info\
div\x22);\x22none\x22==b.\
_console&&(b._co\
nsole=null);b._c\
olor=f.color?f.c\
olor.replace(/0x\
/,\x22#\x22):\x22#FFFFFF\x22\
;b._disableIniti\
alConsole=f.disa\
bleInitialConsol\
e;b._noMonitor=f\
.disableJ2SLoadM\
onitor;c._j2sPat\
h&&(f.j2sPath=c.\
_j2sPath);b._j2s\
Path=f.j2sPath;b\
._coverImage=f.c\
overImage;\x0ab._ma\
keLiveImage=f.ma\
keLiveImage||f.j\
2sPath+\x22/img/pla\
y_make_live.jpg\x22\
;b._isCovered=!!\
b._coverImage;b.\
_deferApplet=f.d\
eferApplet||b._i\
sCovered&&b._isJ\
ava;b._deferUnco\
ver=f.deferUncov\
er&&!b._isJava;b\
._coverScript=f.\
coverScript;b._c\
overTitle=f.cove\
rTitle;b._coverT\
itle||(b._coverT\
itle=b._deferApp\
let?\x22activate 3D\
 model\x22:\x223D mode\
l is loading...\x22\
);b._containerWi\
dth=b._width+(b.\
_width==parseFlo\
at(b._width)?\x22px\
\x22:\x22\x22);b._contain\
erHeight=b._heig\
ht+(b._height==p\
arseFloat(b._hei\
ght)?\x22px\x22:\x22\x22);b.\
_info=\x22\x22;b._info\
Header=\x0ab._jmolT\
ype+' \x22'+b._id+'\
\x22';b._hasOptions\
=f.addSelectionO\
ptions;b._defaul\
tModel=f.default\
Model;b._readySc\
ript=f.script?f.\
script:\x22\x22;b._rea\
dyFunction=f.rea\
dyFunction;b._co\
verImage&&!b._de\
ferApplet&&(b._r\
eadyScript+=\x22;ja\
vascript \x22+e+\x22._\
displayCoverImag\
e(false)\x22);b._sr\
c=f.src};c._addD\
efaultInfo=funct\
ion(b,e){for(var\
 f in e)\x22undefin\
ed\x22==typeof b[f]\
&&(b[f]=e[f]);c.\
_use&&(b.use=c._\
use);0<=b.use.in\
dexOf(\x22SIGNED\x22)&\
&(0>b.jarFile.in\
dexOf(\x22Signed\x22)&\
&(b.jarFile=b.ja\
rFile.replace(/A\
pplet/,\x22AppletSi\
gned\x22)),b.use=\x0ab\
.use.replace(/SI\
GNED/,\x22JAVA\x22),b.\
isSigned=!0)};c.\
_syncedApplets=[\
];c._syncedComma\
nds=[];c._synced\
Ready=[];c._sync\
Ready=!1;c._isJm\
olJSVSync=!1;c._\
setReady=functio\
n(b){c._syncedRe\
ady[b]=1;for(var\
 e=0,f=0;f<c._sy\
ncedApplets.leng\
th;f++){if(c._sy\
ncedApplets[f]==\
b._id)c._syncedA\
pplets[f]=b,c._s\
yncedReady[f]=1;\
else if(!c._sync\
edReady[f])conti\
nue;e++}e==c._sy\
ncedApplets.leng\
th&&c._setSyncRe\
ady()};c._setDes\
troy=function(b)\
{c.featureDetect\
ion.allowDestroy\
&&c.$windowOn(\x22b\
eforeunload\x22,fun\
ction(){c._destr\
oy(b)})};\x0ac._des\
troy=function(b)\
{try{b._appletPa\
nel&&b._appletPa\
nel.destroy();b.\
_applet=null;c._\
unsetMouse(b._ca\
nvas);b._canvas=\
null;for(var e=0\
,f=0;f<c._synced\
Applets.length;f\
++)c._syncedAppl\
ets[f]==b&&(c._s\
yncedApplets[f]=\
null),c._syncedA\
pplets[f]&&e++;0\
<e||c._clearVars\
()}catch(h){}};c\
._setSyncReady=f\
unction(){c._syn\
cReady=!0;for(va\
r b=\x22\x22,e=0;e<c._\
syncedApplets.le\
ngth;e++)c._sync\
edCommands[e]&&(\
b+=\x22Jmol.script(\
Jmol._syncedAppl\
ets[\x22+e+\x22], Jmol\
._syncedCommands\
[\x22+e+\x22]);\x22);setT\
imeout(b,50)};c.\
_mySyncCallback=\
\x0afunction(b,e){a\
pp=c._applets[b]\
;if(app._viewSet\
)c.View.updateFr\
omSync(app,e);el\
se{if(!c._syncRe\
ady||!c._isJmolJ\
SVSync)return 1;\
for(var f=0;f<c.\
_syncedApplets.l\
ength;f++)0<=e.i\
ndexOf(c._synced\
Applets[f]._sync\
Keyword)&&c._syn\
cedApplets[f]._s\
yncScript(e);ret\
urn 0}};c._getEl\
ement=function(b\
,c){return docum\
ent.getElementBy\
Id(b._id+\x22_\x22+c)|\
|{}};c._evalJSON\
=function(b,c){b\
+=\x22\x22;if(!b)retur\
n[];if(\x22{\x22!=b.ch\
arAt(0))return 0\
<=b.indexOf(\x22 | \
\x22)&&(b=b.replace\
(/\x5c \x5c|\x5c /g,\x22\x5cn\x22)\
),b;var f=(new F\
unction(\x22return \
\x22+b))();\x0areturn!\
f?null:c&&void 0\
!=f[c]?f[c]:f};c\
._sortMessages=f\
unction(b){funct\
ion c(b,e){retur\
n b[0]<e[0]?1:b[\
0]>e[0]?-1:0}if(\
!b||\x22object\x22!=ty\
peof b)return[];\
for(var f=[],h=b\
.length-1;0<=h;h\
--)for(var j=0,l\
=b[h].length;j<l\
;j++)f[f.length]\
=b[h][j];if(0!=f\
.length)return f\
=f.sort(c)};c._s\
etMouseOwner=fun\
ction(b,e){null=\
=b||e?c._mouseOw\
ner=b:c._mouseOw\
ner==b&&(c._mous\
eOwner=null)};c.\
_jsGetMouseModif\
iers=function(b)\
{var c=0;switch(\
b.button){case 0\
:c=16;break;case\
 1:c=8;break;cas\
e 2:c=4}b.shiftK\
ey&&(c+=1);b.alt\
Key&&\x0a(c+=8);b.c\
trlKey&&(c+=2);r\
eturn c};c._jsGe\
tXY=function(b,e\
){if(!b.applet._\
ready||c._touchi\
ng&&0>e.type.ind\
exOf(\x22touch\x22))re\
turn!1;var f=c.$\
offset(b.id),h,j\
=e.originalEvent\
;e.pageX||(e.pag\
eX=j.pageX);e.pa\
geY||(e.pageY=j.\
pageY);c._mouseP\
ageX=e.pageX;c._\
mousePageY=e.pag\
eY;j.targetTouch\
es&&j.targetTouc\
hes[0]?(h=j.targ\
etTouches[0].pag\
eX-f.left,f=j.ta\
rgetTouches[0].p\
ageY-f.top):j.ch\
angedTouches?(h=\
j.changedTouches\
[0].pageX-f.left\
,f=j.changedTouc\
hes[0].pageY-f.t\
op):(h=e.pageX-f\
.left,f=e.pageY-\
f.top);return vo\
id 0==\x0ah?null:[M\
ath.round(h),Mat\
h.round(f),c._js\
GetMouseModifier\
s(e)]};c._setCur\
sor=function(b,e\
){if(!b._isJava&\
&!b._readingLoca\
l){var f;switch(\
e){case 1:f=\x22cro\
sshair\x22;break;ca\
se 3:f=\x22wait\x22;c.\
$setVisible(c.$(\
b,\x22waitimage\x22),!\
0);break;case 8:\
f=\x22ns-resize\x22;br\
eak;case 12:f=\x22g\
rab\x22;break;case \
13:f=\x22move\x22;brea\
k;default:c.$set\
Visible(c.$(b,\x22w\
aitimage\x22),!1),f\
=\x22default\x22}b._ca\
nvas.style.curso\
r=f}};c._gesture\
Update=function(\
b,e){e.stopPropa\
gation();e.preve\
ntDefault();var \
f=e.originalEven\
t;switch(e.type)\
{case \x22touchstar\
t\x22:c._touching=\x0a\
!0;break;case \x22t\
ouchend\x22:c._touc\
hing=!1}if(!f.to\
uches||2!=f.touc\
hes.length)retur\
n!1;switch(e.typ\
e){case \x22touchst\
art\x22:b._touches=\
[[],[]];break;ca\
se \x22touchmove\x22:v\
ar h=c.$offset(b\
.id),j=b._touche\
s[0],l=b._touche\
s[1];j.push([f.t\
ouches[0].pageX-\
h.left,f.touches\
[0].pageY-h.top]\
);l.push([f.touc\
hes[1].pageX-h.l\
eft,f.touches[1]\
.pageY-h.top]);f\
=j.length;3<f&&(\
j.shift(),l.shif\
t());2<=f&&b.app\
let._processGest\
ure(b._touches)}\
return!0};c._jsS\
etMouse=function\
(b){var e=functi\
on(b){return!b.t\
arget||0<=(\x22\x22+b.\
target.className\
).indexOf(\x22swing\
js-ui\x22)};\x0ac.$bin\
d(b,\x22mousedown t\
ouchstart\x22,funct\
ion(f){if(e(f))r\
eturn!0;c._setMo\
useOwner(b,!0);f\
.stopPropagation\
();var h=f.targe\
t[\x22data-UI\x22];(!h\
||!h.handleJSEve\
nt(b,501,f))&&f.\
preventDefault()\
;b.isDragging=!0\
;if(\x22touchstart\x22\
==f.type&&c._ges\
tureUpdate(b,f))\
return!!h;c._set\
ConsoleDiv(b.app\
let._console);va\
r j=c._jsGetXY(b\
,f);j&&(2!=f.but\
ton&&c.Swing.hid\
eMenus(b.applet)\
,b.applet._proce\
ssEvent(501,j));\
return!!h});c.$b\
ind(b,\x22mouseup t\
ouchend\x22,functio\
n(f){if(e(f))ret\
urn!0;c._setMous\
eOwner(null);f.s\
topPropagation()\
;\x0avar h=f.target\
[\x22data-UI\x22];(!h|\
|!h.handleJSEven\
t(b,502,f))&&f.p\
reventDefault();\
b.isDragging=!1;\
if(\x22touchend\x22==f\
.type&&c._gestur\
eUpdate(b,f))ret\
urn!!h;(f=c._jsG\
etXY(b,f))&&b.ap\
plet._processEve\
nt(502,f);return\
!!h});c.$bind(b,\
\x22mousemove touch\
move\x22,function(f\
){if(e(f))return\
!0;if(c._mouseOw\
ner&&c._mouseOwn\
er!=b&&c._mouseO\
wner.isDragging)\
{if(!c._mouseOwn\
er.mouseMove)ret\
urn!0;c._mouseOw\
ner.mouseMove(f)\
;return!1}return\
 c._drag(b,f)});\
c._drag=function\
(b,e){e.stopProp\
agation();e.prev\
entDefault();if(\
\x22touchmove\x22==\x0ae.\
type&&c._gesture\
Update(b,e))retu\
rn!1;var h=c._js\
GetXY(b,e);if(!h\
)return!1;b.isDr\
agging||(h[2]=0)\
;var j=e.target[\
\x22data-UI\x22];b.isd\
ragging&&(!j||j.\
handleJSEvent(b,\
506,e));b.applet\
._processEvent(b\
.isDragging?506:\
503,h);return!!j\
};c.$bind(b,\x22DOM\
MouseScroll mous\
ewheel\x22,function\
(f){if(e(f))retu\
rn!0;f.stopPropa\
gation();f.preve\
ntDefault();b.is\
Dragging=!1;var \
h=f.originalEven\
t,h=h.detail?h.d\
etail:(\x22mac\x22==c.\
featureDetection\
.os?1:-1)*h.whee\
lDelta;f=c._jsGe\
tMouseModifiers(\
f);b.applet._pro\
cessEvent(-1,[0>\
h?-1:\x0a1,0,f]);re\
turn!1});c.$bind\
(b,\x22contextmenu\x22\
,function(){retu\
rn!1});c.$bind(b\
,\x22mouseout\x22,func\
tion(f){if(e(f))\
return!0;c._mous\
eOwner&&!c._mous\
eOwner.mouseMove\
&&c._setMouseOwn\
er(null);b.apple\
t._appletPanel&&\
b.applet._applet\
Panel.startHover\
Watcher(!1);c._j\
sGetXY(b,f);retu\
rn!1});c.$bind(b\
,\x22mouseenter\x22,fu\
nction(f){if(e(f\
))return!0;b.app\
let._appletPanel\
&&b.applet._appl\
etPanel.startHov\
erWatcher(!0);if\
(0===f.buttons||\
0===f.which){b.i\
sDragging=!1;f=c\
._jsGetXY(b,f);i\
f(!f)return!1;b.\
applet._processE\
vent(504,f);\x0ab.a\
pplet._processEv\
ent(502,f);retur\
n!1}});c.$bind(b\
,\x22mousemoveoutjs\
mol\x22,function(f,\
h,j){if(e(j))ret\
urn!0;if(b==c._m\
ouseOwner&&b.isD\
ragging)return c\
._drag(b,j)});b.\
applet._is2D&&c.\
$resize(function\
(){b.applet&&b.a\
pplet._resize()}\
);c.$bind(\x22body\x22\
,\x22mouseup touche\
nd\x22,function(f){\
if(e(f))return!0\
;b.applet&&(b.is\
Dragging=!1);c._\
setMouseOwner(nu\
ll)})};c._jsUnse\
tMouse=function(\
b){b.applet=null\
;c.$bind(b,\x22mous\
edown touchstart\
 mousemove touch\
move mouseup tou\
chend DOMMouseSc\
roll mousewheel \
contextmenu mous\
eout mouseenter\x22\
,\x0anull);c._setMo\
useOwner(null)};\
c.Swing={count:0\
,menuInitialized\
:0,menuCounter:0\
,htDialogs:{}};v\
ar v=c.Swing;Swi\
ngController=v;v\
.setDraggable=fu\
nction(b){b=b.pr\
ototype;b.setCon\
tainer||(b.setCo\
ntainer=function\
(b){this.contain\
er=b;b.obj=this;\
this.ignoreMouse\
=this.isDragging\
=!1;var f=this;b\
.bind(\x22mousedown\
 touchstart\x22,fun\
ction(b){if(f.ig\
noreMouse)return\
 f.ignoreMouse=!\
1,!0;c._setMouse\
Owner(f,!0);f.is\
Dragging=!0;f.pa\
geX=b.pageX;f.pa\
geY=b.pageY;retu\
rn!1});b.bind(\x22m\
ousemove touchmo\
ve\x22,function(b){\
if(f.isDragging&\
&\x0ac._mouseOwner=\
=f)return f.mous\
eMove(b),!1});b.\
bind(\x22mouseup to\
uchend\x22,function\
(b){f.mouseUp(b)\
;c._setMouseOwne\
r(null)})},b.mou\
seUp=function(b)\
{if(this.isDragg\
ing&&c._mouseOwn\
er==this)return \
this.pageX0+=b.p\
ageX-this.pageX,\
this.pageY0+=b.p\
ageY-this.pageY,\
this.isDragging=\
!1;c._setMouseOw\
ner(null)},b.set\
Position=functio\
n(){if(null===c.\
_mousePageX){var\
 b=c.$offset(thi\
s.applet._id+\x22_\x22\
+(this.applet._i\
s2D?\x22canvas2d\x22:\x22\
canvas\x22));c._mou\
sePageX=b.left;c\
._mousePageY=b.t\
op}this.pageX0=c\
._mousePageX;thi\
s.pageY0=\x0ac._mou\
sePageY;this.con\
tainer.css({top:\
c._mousePageY+\x22p\
x\x22,left:c._mouse\
PageX+\x22px\x22})},b.\
mouseMove=functi\
on(b){if(this.is\
Dragging&&c._mou\
seOwner==this){t\
his.timestamp=Sy\
stem.currentTime\
Millis();var f=t\
his.pageX0+(b.pa\
geX-this.pageX);\
b=this.pageY0+(b\
.pageY-this.page\
Y);c._mousePageX\
=f;c._mousePageY\
=b;this.containe\
r.css({top:b+\x22px\
\x22,left:f+\x22px\x22})}\
},b.dragBind=fun\
ction(b){this.ap\
plet._ignoreMous\
e=!b;this.contai\
ner.unbind(\x22mous\
emoveoutjsmol\x22);\
this.container.u\
nbind(\x22touchmove\
outjsmol\x22);this.\
container.unbind\
(\x22mouseupoutjsmo\
l\x22);\x0athis.contai\
ner.unbind(\x22touc\
hendoutjsmol\x22);c\
._setMouseOwner(\
null);if(b){var \
f=this;this.cont\
ainer.bind(\x22mous\
emoveoutjsmol to\
uchmoveoutjsmol\x22\
,function(b,c,e)\
{f.mouseMove(e)}\
);this.container\
.bind(\x22mouseupou\
tjsmol touchendo\
utjsmol\x22,functio\
n(b,c,e){f.mouse\
Up(e)})}})};v.JS\
Dialog=function(\
){};v.setDraggab\
le(v.JSDialog);v\
.getScreenDimens\
ions=function(b)\
{b.width=m(windo\
w).width();b.hei\
ght=m(window).he\
ight()};v.dispos\
e=function(b){c.\
$remove(b.id+\x22_m\
over\x22);delete v.\
htDialogs[b.id];\
b.container.obj.\
dragBind(!1)};\x0av\
.register=functi\
on(b,c){b.id=c+ \
++v.count;v.htDi\
alogs[b.id]=b};v\
.setDialog=funct\
ion(b){c._setMou\
seOwner(null);c.\
$remove(b.id);va\
r e=b.id+\x22_mover\
\x22,f=c._$(e),h;f[\
0]?(f.html(b.htm\
l),h=f[0].jd):(c\
.$after(\x22body\x22,\x22\
<div id='\x22+e+\x22' \
style='position:\
absolute;left:0p\
x;top:0px;'>\x22+b.\
html+\x22</div>\x22),h\
=new v.JSDialog,\
f=c._$(e),b.cont\
ainer=f,h.applet\
=b.manager.vwr.h\
tml5Applet,h.set\
Container(f),h.d\
ialog=b,h.setPos\
ition(),h.dragBi\
nd(!0),f[0].jd=h\
);c.$bind(\x22#\x22+b.\
id+\x22 .JButton\x22,\x22\
mousedown touchs\
tart\x22,function()\
{h.ignoreMouse=\x0a\
!0});c.$bind(\x22#\x22\
+b.id+\x22 .JComboB\
ox\x22,\x22mousedown t\
ouchstart\x22,funct\
ion(){h.ignoreMo\
use=!0});c.$bind\
(\x22#\x22+b.id+\x22 .JCh\
eckBox\x22,\x22mousedo\
wn touchstart\x22,f\
unction(){h.igno\
reMouse=!0});c.$\
bind(\x22#\x22+b.id+\x22 \
.JTextField\x22,\x22mo\
usedown touchsta\
rt\x22,function(){h\
.ignoreMouse=!0}\
);c.$bind(\x22#\x22+b.\
id+\x22 .JTable\x22,\x22m\
ousedown touchst\
art\x22,function(){\
h.ignoreMouse=!0\
});c.$bind(\x22#\x22+b\
.id+\x22 .JScrollPa\
ne\x22,\x22mousedown t\
ouchstart\x22,funct\
ion(){h.ignoreMo\
use=!0});c.$bind\
(\x22#\x22+b.id+\x22 .JEd\
itorPane\x22,\x22mouse\
down touchstart\x22\
,function(){h.ig\
noreMouse=\x0a!0})}\
;v.setSelected=f\
unction(b){c.$pr\
op(b.id,\x22checked\
\x22,!!b.selected)}\
;v.setSelectedIn\
dex=function(b){\
c.$prop(b.id,\x22se\
lectedIndex\x22,b.s\
electedIndex)};v\
.setText=functio\
n(b){c.$prop(b.i\
d,\x22value\x22,b.text\
)};v.setVisible=\
function(b){c.$s\
etVisible(b.id,b\
.visible)};v.set\
Enabled=function\
(b){c.$setEnable\
d(b.id,b.enabled\
)};v.click=funct\
ion(b,e){var f=v\
.htDialogs[b.id]\
;if(f){var h=f.t\
oString();if(0<=\
h.indexOf(\x22JChec\
k\x22))f.selected=b\
.checked;else if\
(0<=h.indexOf(\x22J\
Combo\x22))f.select\
edIndex=b.select\
edIndex;else if(\
null!=\x0af.text&&(\
f.text=b.value,e\
&&13!=(e.charCod\
e||e.keyCode)))r\
eturn}h=v.htDial\
ogs[c.$getAncest\
orDiv(b.id,\x22JDia\
log\x22).id];h.mana\
ger.actionPerfor\
med(f?f.name:h.r\
egistryKey+\x22/\x22+b\
.id)};v.setFront\
=function(b){var\
 e=b.manager.vwr\
.html5Applet;b.z\
Index!=c._getZ(e\
,\x22dialog\x22)&&(b.z\
Index=c._incrZ(e\
,\x22dialog\x22));b.co\
ntainer&&((b.con\
tainer[0]||b.con\
tainer).style.zI\
ndex=b.zIndex)};\
v.hideMenus=func\
tion(b){if(b=b._\
menus)for(var c \
in b)b[c].visibl\
e&&v.hideMenu(b[\
c])};v.windowClo\
sing=function(b)\
{b=v.htDialogs[c\
.$getAncestorDiv\
(b.id,\x0a\x22JDialog\x22\
).id];b.registry\
Key?b.manager.pr\
ocessWindowClosi\
ng(b.registryKey\
):b.dispose()};c\
._track=function\
(b){if(c._tracke\
r){try{var e='<i\
frame style=\x22dis\
play:none\x22 width\
=\x220\x22 height=\x220\x22 \
frameborder=\x220\x22 \
tabindex=\x22-1\x22 sr\
c=\x22'+(c._tracker\
+\x22&applet=\x22+b._j\
molType+\x22&versio\
n=\x22+c._version+\x22\
&appver=\x22+c.___J\
molVersion+\x22&url\
=\x22+encodeURIComp\
onent(document.l\
ocation.href))+'\
\x22></iframe>';c.$\
after(\x22body\x22,e)}\
catch(f){}delete\
 c._tracker}retu\
rn b};var w;c.ge\
tProfile=functio\
n(b){if(self.Cla\
zz&&self.JSON)re\
turn w||Clazz._s\
tartProfiling(w=\
\x0a0==arguments.le\
ngth||b),Clazz.g\
etProfile()};c._\
getInChIKey=func\
tion(b,c){0<=c.i\
ndexOf(\x22MOL=\x22)&&\
c.split(\x22MOL=\x22)[\
1].split('\x22')};c\
._getAttr=functi\
on(b,c){var f=b.\
indexOf(c+\x22=\x22);r\
eturn 0<=f&&0<=(\
f=b.indexOf('\x22',\
f))?b.substring(\
f+1,b.indexOf('\x22\
',f+1)):null};c.\
User={viewUpdate\
dCallback:null};\
c.View={count:0,\
applets:{},sets:\
{}};(function(b)\
{b.updateView=fu\
nction(e,f){if(n\
ull!=e._viewSet)\
{f.chemID||(e._s\
earchQuery=null)\
;f.data||(f.data\
=\x22N/A\x22);f.type=e\
._viewType;if(nu\
ll==(e._currentV\
iew=b.__findView\
(e._viewSet,\x0af))\
)e._currentView=\
b.__createViewSe\
t(e._viewSet,f.c\
hemID,f.viewID||\
f.chemID);e._cur\
rentView[f.type]\
.data=f.data;e._\
currentView[f.ty\
pe].smiles=e._ge\
tSmiles();c.User\
.viewUpdatedCall\
back&&c.User.vie\
wUpdatedCallback\
(e,\x22updateView\x22)\
;b.__setView(e._\
currentView,e,!1\
)}};b.updateFrom\
Sync=function(e,\
f){e._updateMsg=\
f;var h=c._getAt\
tr(f,\x22sourceID\x22)\
||c._getAttr(f,\x22\
file\x22);if(h){var\
 j=b.__findView(\
e._viewSet,{view\
ID:h});if(null==\
j)return c.updat\
eView(e,f);j!=e.\
_currentView&&b.\
__setView(j,e,!0\
);var l=(h=c._ge\
tAttr(f,\x0a\x22atoms\x22\
))&&0<=f.indexOf\
(\x22selectionhalos\
 ON\x22)?eval(\x22[\x22+h\
+\x22]\x22):[];setTime\
out(function(){e\
._currentView==j\
&&b.updateAtomPi\
ck(e,l)},10);c.U\
ser.viewUpdatedC\
allback&&c.User.\
viewUpdatedCallb\
ack(e,\x22updateFro\
mSync\x22)}};b.upda\
teAtomPick=funct\
ion(b,f){var h=b\
._currentView;if\
(null!=h){for(va\
r j in h)\x22info\x22!\
=j&&h[j].applet!\
=b&&h[j].applet.\
_updateAtomPick(\
f);c.User.viewUp\
datedCallback&&c\
.User.viewUpdate\
dCallback(b,\x22upd\
ateAtomPick\x22)}};\
b.dumpViews=func\
tion(c){var f=b.\
sets[c];if(f){va\
r h=\x22View set \x22+\
c+\x22:\x5cn\x22;c=b.appl\
ets[c];\x0afor(var \
j in c)h+=\x22\x5cnapp\
let \x22+c[j]._id+\x22\
 currentView=\x22+(\
c[j]._currentVie\
w?c[j]._currentV\
iew.info.viewID:\
null);for(j=f.le\
ngth;0<=--j;){c=\
f[j];var h=h+(\x22\x5c\
n\x5cn<b>view=\x22+j+\x22\
 viewID=\x22+c.info\
.viewID+\x22 chemID\
=\x22+c.info.chemID\
+\x22</b>\x5cn\x22),l,m;f\
or(m in c)\x22info\x22\
!=m&&(h+=\x22\x5cnview\
=\x22+j+\x22 type=\x22+m+\
\x22 applet=\x22+((l=c\
[m]).applet?l.ap\
plet._id:null)+\x22\
 SMILES=\x22+l.smil\
es+\x22\x5cn atomMap=\x22\
+JSON.stringify(\
l.atomMap)+\x22\x5cn d\
ata=\x5cn\x22+l.data+\x22\
\x5cn\x22)}return h}};\
b.__init=functio\
n(c){var f=c._vi\
ewSet,h=b.applet\
s;h[f]||(h[f]={}\
);h[f][c._viewTy\
pe]=\x0ac};b.__find\
View=function(c,\
f){var h=b.sets[\
c];null==h&&(h=b\
.sets[c]=[]);for\
(var j=h.length;\
0<=--j;){var l=h\
[j];if(f.viewID)\
{if(l.info.viewI\
D==f.viewID)retu\
rn l}else{if(nul\
l!=f.chemID&&f.c\
hemID==l.info.ch\
emID)return l;fo\
r(var m in l)if(\
\x22info\x22!=m&&(null\
!=f.data&&null!=\
l[m].data?f.data\
==l[m].data:f.ty\
pe==m))return l}\
}return null};b.\
__createViewSet=\
function(e,f,h){\
b.count++;f={inf\
o:{chemID:f,view\
ID:h||\x22model_\x22+b\
.count}};for(var\
 j in c._applets\
)h=c._applets[j]\
,h._viewSet==e&&\
(f[h._viewType]=\
{applet:h,\x0adata:\
null});b.sets[e]\
.push(f);return \
f};b.__setView=f\
unction(b,c,h){f\
or(var j in b)if\
(\x22info\x22!=j){var \
l=b[j],m=l.apple\
t,r=h||null!=m&&\
\x22<modified>\x22==m.\
_molData;if(!(nu\
ll==m||m==c&&!r)\
){var p=null==l.\
data,v=null!=m._\
currentView;m._c\
urrentView=b;if(\
!v||!(b[j].data=\
=l.data&&!p&!r))\
if(m._loadModelF\
romView(b),p)bre\
ak}}}})(c.View);\
c.Cache={fileCac\
he:{}};c.Cache.g\
et=function(b){r\
eturn c.Cache.fi\
leCache[b]};c.Ca\
che.put=function\
(b,e){c.Cache.fi\
leCache[b]=e};c.\
Cache.setDragDro\
p=function(b){c.\
$appEvent(b,\x22app\
letdiv\x22,\x0a\x22dragov\
er\x22,function(b){\
b=b.originalEven\
t;b.stopPropagat\
ion();b.preventD\
efault();b.dataT\
ransfer.dropEffe\
ct=\x22copy\x22});c.$a\
ppEvent(b,\x22apple\
tdiv\x22,\x22drop\x22,fun\
ction(e){var f=e\
.originalEvent;f\
.stopPropagation\
();f.preventDefa\
ult();var h=f.da\
taTransfer.files\
[0];if(null==h)t\
ry{h=\x22\x22+f.dataTr\
ansfer.getData(\x22\
text\x22),(0==h.ind\
exOf(\x22file:/\x22)||\
0==h.indexOf(\x22ht\
tp:/\x22))&&b._scri\
ptLoad(h)}catch(\
j){}else f=new F\
ileReader,f.onlo\
adend=function(f\
){if(f.target.re\
adyState==FileRe\
ader.DONE){var j\
=\x22cache://DROP_\x22\
+h.name;f=Clazz.\
newByteArray(-1,\
\x0af.target.result\
);j.endsWith(\x22.s\
pt\x22)||b._appletP\
anel.cacheFileBy\
Name(\x22cache://DR\
OP_*\x22,!1);\x22JSV\x22=\
=b._viewType||j.\
endsWith(\x22.jdx\x22)\
?c.Cache.put(j,f\
):b._appletPanel\
.cachePut(j,f);(\
f=c._jsGetXY(b._\
canvas,e))&&(!b.\
_appletPanel.set\
StatusDragDroppe\
d||b._appletPane\
l.setStatusDragD\
ropped(0,f[0],f[\
1],j))&&b._apple\
tPanel.openFileA\
syncSpecial(j,1)\
}},f.readAsArray\
Buffer(h)})}})(J\
mol,jQuery);Jmol\
._debugCode=!1;J\
mol._grabberOpti\
ons=[[\x22$\x22,\x22NCI(s\
mall molecules)\x22\
],[\x22:\x22,\x22PubChem(\
small molecules)\
\x22]];Jmol.say=fun\
ction(c){alert(c\
)};\x0aJmol._TMAppl\
et=function(c,m,\
h){this._uniqueI\
d=(\x22\x22+Math.rando\
m()).substring(3\
);this._id=c;thi\
s._is2D=!0;this.\
_isJava=!1;this.\
_ready=!0;this._\
mouseDown=!1;thi\
s._jmolType=\x22Jmo\
l._Canvas2D (Twi\
rlyMol)\x22;if(h)re\
turn this;this._\
createCanvas(c,m\
);return this};\x0a\
Jmol._TMApplet._\
getApplet=functi\
on(c,m,h){if(!Jm\
ol.featureDetect\
ion.allowHTML5)r\
eturn null;h||(h\
=!1);m||(m={});J\
mol._addDefaultI\
nfo(m,{color:\x22#F\
FFFFF\x22,width:300\
,height:300,addS\
electionOptions:\
!1,serverURL:\x22ht\
tp://your.server\
.here/jsmol.php\x22\
,defaultModel:\x22\x22\
,readyFunction:n\
ull,use:\x22HTML5\x22,\
bondWidth:5,shad\
eAtoms:!1,zoomSc\
aling:1.5,pinchS\
caling:2,mouseDr\
agFactor:0.5,tou\
chDragFactor:0.1\
5,multipleBondSp\
acing:4,spinRate\
X:0,spinRateY:0.\
5,spinFPS:20,spi\
n:!1,noscript:!0\
,debug:!1});m=ne\
w Jmol._TMApplet\
(c,m,\x0ah);return \
h?m:Jmol._regist\
erApplet(c,m)};J\
mol.getTMApplet=\
Jmol._TMApplet._\
getApplet;\x0a(func\
tion(c){c._CPK=\x22\
#FF1493 #FFFFFF \
#D9FFFF #CC80FF \
#C2FF00 #FFB5B5 \
#909090 #3050F8 \
#FF0D0D #90E050 \
#B3E3F5 #AB5CF2 \
#8AFF00 #BFA6A6 \
#F0C8A0 #FF8000 \
#FFFF30 #1FF01F \
#80D1E3 #8F40D4 \
#3DFF00 #E6E6E6 \
#BFC2C7 #A6A6AB \
#8A99C7 #9C7AC7 \
#E06633 #F090A0 \
#50D050 #C88033 \
#7D80B0 #C28F8F \
#668F8F #BD80E3 \
#FFA100 #A62929 \
#5CB8D1 #702EB0 \
#00FF00 #94FFFF \
#94E0E0 #73C2C9 \
#54B5B5 #3B9E9E \
#248F8F #0A7D8C \
#006985 #C0C0C0 \
#FFD98F #A67573 \
#668080 #9E63B5 \
#D47A00 #940094 \
#429EB0 #57178F \
#00C900\x22.split(\x22\
 \x22);c._elem=\x22X H\
 He Li Be B C N \
O F Ne Na Mg Al \
Si P S Cl Ar K C\
a Sc Ti V Cr Mn \
Fe Co Ni Cu Zn G\
a Ge As Se Br Kr\
 Rb Sr Y Zr Nb M\
o Tc Ru Rh Pd Ag\
 Cd In Sn Sb Te \
I Xe Cs Ba La Ce\
 Pr Nd Pm Sm Eu \
Gd Tb Dy Ho Er T\
m Yb Lu Hf Ta W \
Re Os Ir Pt Au H\
g Tl Pb Bi Po At\
 Rn Fr Ra Ac Th \
Pa U Np Pu Am Cm\
 Bk Cf Es\x22.split\
(\x22 \x22);\x0ac._elemNo\
={};var m=c.prot\
otype;m.spin=fun\
ction(c){this.__\
Info.spin=c;this\
._spin(c)};m._sp\
in=function(c){t\
his._spinThread&\
&clearTimeout(th\
is._spinThread);\
if(0==this.spinF\
PS||0==this.spin\
RateX&&0==this.s\
pinRateY)c=!1;if\
(c){var j=this;c\
=1E3/this.spinFP\
S;this._mouseDow\
n||(this._rotate\
(this.spinRateY,\
this.spinRateX),\
this._draw());th\
is._spinThread=s\
etTimeout(functi\
on(){j._spin(!0)\
},c)}};m._initPa\
rams=function(){\
this.zoom=this._\
_Info.defaultZoo\
m||100;this.doSp\
in=this.__Info.s\
pin||!1;this.cen\
ter2D=[this._can\
vas.width/\x0a2,thi\
s._canvas.height\
/2,0];this._getC\
enterAndRadius()\
;this.rotation=n\
ew c.M3;this.sha\
deAtoms=!1;this.\
_setParams()};m.\
_setParams=funct\
ion(){this.bondW\
idth=this.__Info\
.bondWidth||5;th\
is.zoomScaling=t\
his.__Info.zoomS\
caling||1.5;this\
.pinchScaling=th\
is.__Info.pinchS\
caling||1;this.m\
ouseDragFactor=t\
his.__Info.mouse\
DragFactor||0.5;\
this.touchDragFa\
ctor=this.__Info\
.touchDragFactor\
||0.15;this.mult\
ipleBondSpacing=\
this.__Info.mult\
ipleBondSpacing|\
|4;this.spinRate\
X=this.__Info.sp\
inRateX||0;this.\
spinRateY=this._\
_Info.spinRateY|\
|\x0a0;this.spinFPS\
=this.__Info.spi\
nFPS||0;var c=th\
is.shadeAtoms;(t\
his.shadeAtoms=t\
his.__Info.shade\
Atoms||!1)&&!c&&\
this._setAtomSha\
des()};m._setAto\
mShades=function\
(){if(this.atoms\
)for(var c=this.\
atoms.length;0<=\
--c;)this.atoms[\
c].color50=this.\
_getColor(this.a\
toms[c].color,0.\
5)};m._createCan\
vas=function(c,j\
){Jmol._setObjec\
t(this,c,j);this\
._color=this._co\
lor.replace(/0x/\
,\x22#\x22);var l=Jmol\
._getWrapper(thi\
s,!0);Jmol._docu\
ment?(Jmol._docu\
mentWrite(l),thi\
s._createCanvas2\
d(!1),l=\x22\x22):l+='\
<script type=\x22te\
xt/javascript\x22>'\
+\x0ac+\x22._createCan\
vas2d(false)\x5cx3c\
/script>\x22;l+=Jmo\
l._getWrapper(th\
is,!1);j.addSele\
ctionOptions&&(l\
+=Jmol._getGrabb\
erOptions(this,\x22\
\x22));Jmol._debugA\
lert&&!Jmol._doc\
ument&&alert(l);\
this._code=Jmol.\
_documentWrite(l\
)};m._createCanv\
as2d=function(c)\
{var j=document.\
createElement(\x22c\
anvas\x22),l=Jmol.$\
(this,\x22appletdiv\
\x22);c&&(l[0].remo\
veChild(this._ca\
nvas),Jmol._jsUn\
setMouse(this._c\
anvas));c=Math.r\
ound(l.width());\
var m=Math.round\
(l.height());j.a\
pplet=this;this.\
_canvas=j;j.styl\
e.width=\x22100%\x22;j\
.style.height=\x221\
00%\x22;j.width=\x0ac;\
j.height=m;j.id=\
this._id+\x22_canva\
s2d\x22;l.append(j)\
;setTimeout(this\
._id+\x22._start()\x22\
,10)};m._start=f\
unction(){Jmol._\
jsSetMouse(this.\
_canvas);this._d\
efaultModel?Jmol\
._search(this,th\
is._defaultModel\
,this._readyScri\
pt?this._readySc\
ript:\x22\x22):this._s\
rc&&this._loadFi\
le(this._src);th\
is._showInfo(!0)\
;this._showInfo(\
!1)};m._search=f\
unction(c,j){Jmo\
l._search(this,c\
,j)};m._searchDa\
tabase=function(\
c,j,l){this._sho\
wInfo(!1);0<=c.i\
ndexOf(\x22?\x22)?Jmol\
._getInfoFromDat\
abase(this,j,c.s\
plit(\x22?\x22)[0]):th\
is._loadFile(j+c\
,l)};\x0am.__loadMo\
del=function(c){\
this._spin(!1);\x22\
''\x22==c&&(c=this.\
_mol);c?(this._p\
arse(c),this._in\
itParams(),this.\
_draw(),this._sh\
owInfo(!1),this.\
doSpin&&this._sp\
in(!0)):alert(\x22N\
o model data.\x22)}\
;m._showInfo=fun\
ction(c){Jmol.$h\
tml(Jmol.$(this,\
\x22infoheaderspan\x22\
),this._infoHead\
er);this._info&&\
Jmol.$html(Jmol.\
$(this,\x22infodiv\x22\
),this._info);!t\
his._isInfoVisib\
le!=!c&&(this._i\
sInfoVisible=c,J\
mol.$setVisible(\
Jmol.$(this,\x22inf\
otablediv\x22),c),J\
mol.$setVisible(\
Jmol.$(this,\x22inf\
oheaderdiv\x22),c),\
this._show(!c))}\
;m._show=functio\
n(c){Jmol.$setVi\
sible(Jmol.$(thi\
s,\x0a\x22appletdiv\x22),\
c);c&&this._draw\
()};m._resize=fu\
nction(){var c=\x22\
__resizeTimeout_\
\x22+this._id;Jmol[\
c]&&clearTimeout\
(Jmol[c]);var j=\
this;Jmol[c]=set\
Timeout(function\
(){j._draw();Jmo\
l[c]=null},100)}\
;m._canScript=fu\
nction(){return!\
0};m._script=fun\
ction(c){for(var\
 j=c.split(\x22;\x22),\
l=0;l<j.length;l\
++)c=j[l].trim()\
,\x22image\x22==c?wind\
ow.open(this._ca\
nvas.toDataURL(\x22\
image/png\x22)):0==\
c.indexOf(\x22load \
\x22)?this._loadFil\
e(c.substring(5)\
.trim()):0==c.in\
dexOf(\x22spin \x22)&&\
this.spin(0>c.to\
LowerCase().inde\
xOf(\x22off\x22))};m._\
loadFile=\x0afuncti\
on(c){this._show\
Info(!1);this._t\
hisJmolModel=c;v\
ar j=this;Jmol._\
loadFileData(thi\
s,c,function(c){\
j.__loadModel(c)\
})};m._processEv\
ent=function(c,j\
){switch(c){case\
 502:case 503:th\
is._mouseDown=!1\
;default:return;\
case 501:this._m\
ouseX=j[0];this.\
_mouseY=j[1];thi\
s._mouseDown=!0;\
return;case 506:\
var l=j[0]-this.\
_mouseX,m=j[1]-t\
his._mouseY,l=0>\
l?-1:0<l?1:0,m=0\
>m?-1:0<m?1:0;sw\
itch(j[2]){case \
17:this._zoomBy(\
m);break;case 24\
:this.center2D[0\
]+=l;this.center\
2D[1]+=m;break;d\
efault:this._rot\
ate(l,m)}this._m\
ouseX=\x0aj[0];this\
._mouseY=j[1];br\
eak;case -1:this\
._zoomBy(j[1])}t\
his._draw()};m._\
processGesture=f\
unction(h){if(!(\
2>h[0].length)){\
var j=h[0],l=h[1\
],m=j[0],p=j[l.l\
ength-1];h=m[0];\
var v=p[0],m=m[1\
],p=p[1],w=[v-h,\
p-m,0],b=c._leng\
th(w),e=l[0],f=l\
[l.length-1],l=e\
[0],n=f[0],e=e[1\
],f=f[1],t=[n-l,\
f-e,0],B=c._leng\
th(t);3>b||3>B||\
(c._scale(w,1/b)\
,c._scale(t,1/B)\
,w=c._dot(w,t),0\
.8<w?(h=Math.rou\
nd(v-j[j.length-\
2][0]),j=Math.ro\
und(p-j[j.length\
-2][1]),this.cen\
ter2D[0]+=h,this\
.center2D[1]+=j)\
:-0.8>w&&(w=[l-h\
,e-m,0],t=[n-\x0av,\
f-p,0],j=c._leng\
th(t)-c._length(\
w),this.zoom+=(0\
>j?-1:1)*this.pi\
nchScaling),this\
._draw())}};m._z\
oomBy=function(c\
){this.zoom+=c*t\
his.zoomScaling;\
5>this.zoom&&(th\
is.zoom=5);500<t\
his.zoom&&(this.\
zoom=500)};m._ge\
tRotationScaling\
=function(){retu\
rn[1/Math.max(th\
is._canvas.width\
,500)*this.mouse\
DragFactor*c.deg\
_per_radian,1/Ma\
th.max(this._can\
vas.height,500)*\
this.mouseDragFa\
ctor*c.deg_per_r\
adian]};m._rotat\
e=function(h,j){\
var l=this._getR\
otationScaling()\
;j&&(c._m3.rotX(\
j*l[1]),this.rot\
ation.mul(c._m3)\
);h&&\x0a(c._m3.rot\
Y(h*l[0]),this.r\
otation.mul(c._m\
3))};m._getCente\
rAndRadius=funct\
ion(){Math.min(t\
his._canvas.widt\
h,this._canvas.h\
eight);for(var h\
=[999999,999999,\
999999],j=[-9999\
99,-999999,-9999\
99],l=this.atoms\
.length;0<=--l;)\
for(var m=3;0<=-\
-m;){var p=this.\
atoms[l].xyz[m];\
p<h[m]&&(h[m]=p)\
;p>j[m]&&(j[m]=p\
)}p=[0,0,0];for(\
m=3;0<=--m;)p[m]\
=(j[m]+h[m])/2;h\
=0;for(l=this.at\
oms.length;0<=--\
l;)j=this.atoms[\
l],j=c._distance\
(j.xyz,p)+(1==j.\
elemNo?1:1.5),j>\
h&&(h=j);this.ce\
nter=p;this.mode\
lRadius=0==h?10:\
h};m._setScreenC\
oords=\x0afunction(\
){for(var c=this\
.center,j=this.r\
otation,l=this.c\
enter2D,m=Math.m\
in(this._canvas.\
width,this._canv\
as.height)/2/thi\
s.modelRadius*th\
is.zoom/100,p=th\
is.atoms.length;\
0<=--p;){var v=t\
his.atoms[p];thi\
s._transform(v.x\
yz,v.sxyz,c,j,m,\
l);v.srad=m*v.ra\
dius}for(p=this.\
bonds.length;0<=\
--p;)v=this.bond\
s[p],this._trans\
form(v.xyz,v.sxy\
z,c,j,m,l),this.\
_transform(v.pts\
[0],v.spts[0],c,\
j,m,l),this._tra\
nsform(v.pts[1],\
v.spts[1],c,j,m,\
l)};m._transform\
=function(h,j,l,\
m,p,v){for(var w\
=c._temp1,b=c._t\
emp2,e=3;0<=\x0a--e\
;)w[e]=(h[e]-l[e\
])*p;m.transform\
(w,b);b[1]=-b[1]\
;b[2]=-b[2];for(\
e=3;0<=--e;)j[e]\
=b[e]+v[e]};m._p\
arse=function(c)\
{this._parseSDF(\
c)};m._parseSDF=\
function(h){this\
._mol=h;if(!c._e\
lemNo.H)for(var \
j=c._elem.length\
;0<=--j;)c._elem\
No[c._elem[j]]=j\
;h=h.split(\x22\x5cn\x22)\
;var l=3,m=h[l++\
];this.nAtoms=pa\
rseFloat(m.subst\
ring(0,3));this.\
nBonds=parseFloa\
t(m.substring(3,\
6));this.atoms=A\
rray(this.nAtoms\
);this.bonds=Arr\
ay(this.nBonds);\
this.elements=Ar\
ray(this.nAtoms+\
this.nBonds);for\
(var p=0,v,w,b,j\
=0;j<this.nAtoms\
;j++){m=\x0ah[l++];\
v=parseFloat(m.s\
ubstring(0,10));\
w=parseFloat(m.s\
ubstring(10,20))\
;b=parseFloat(m.\
substring(20,30)\
);var m=m.substr\
ing(31,34).repla\
ce(/\x5cs+/g,\x22\x22),m=\
c._elemNo[m]||0,\
e=1==m?0.23:0.35\
,f=c._CPK[m]||c.\
_CPK[0];this.ele\
ments[p++]=this.\
atoms[j]={type:0\
,elemNo:m,xyz:[v\
,w,b],sxyz:[0,0,\
0],radius:e,colo\
r:f,color50:f}}f\
or(j=0;j<this.nB\
onds;j++){m=h[l+\
+];v=this.atoms[\
parseFloat(m.sub\
string(0,3))-1];\
w=this.atoms[par\
seFloat(m.substr\
ing(3,6))-1];b=M\
ath.abs(parseFlo\
at(m.substring(6\
,9)));switch(b){\
case 4:case 5:ca\
se 6:case 8:b=\x0a1\
;break;case 7:b=\
2}m=c._getPointA\
long(v.xyz,w.xyz\
,0.5);f=c._dista\
nce(v.xyz,m);e=v\
.radius<f?c._get\
PointAlong(v.xyz\
,m,v.radius/f):[\
0,0,99999];f=w.r\
adius<f?c._getPo\
intAlong(w.xyz,m\
,w.radius/f):[0,\
0,99999];this.el\
ements[p++]=this\
.bonds[j]={type:\
1,atoms:[v,w],xy\
z:m,pts:[e,f],sx\
yz:[0,0,0],spts:\
[[0,0,0],[0,0,0]\
],order:b,color:\
0}}};m._getColor\
=function(c,j){\x22\
#FFFFFF\x22==c&&(c=\
\x22#D0D0D0\x22);var l\
=parseInt(\x220x\x22+c\
.substring(1),16\
),m=l>>16&255,p=\
l>>8&255,l=l&255\
;255!=m&&(m+=Mat\
h.floor((255-m)*\
j));255!=p&&(p+=\
Math.floor((255-\
\x0ap)*j));255!=l&&\
(l+=Math.floor((\
255-l)*j));m=\x2200\
0000\x22+(m<<16|p<<\
8|l).toString(16\
);return\x22#\x22+m.su\
bstring(m.length\
-6,m.length)};m.\
_draw=function()\
{if(this.atoms){\
this._setParams(\
);this._setScree\
nCoords();var h=\
this.elements;h.\
sort(c._zorder);\
var j=this._canv\
as.getContext(\x222\
d\x22);j.fillStyle=\
this._color;j.fi\
llRect(0,0,this.\
_canvas.width,th\
is._canvas.heigh\
t);for(var l=h.l\
ength;0<=--l;){v\
ar m=h[l];0==m.t\
ype?this._drawAt\
om(j,m):this._dr\
awBond(j,m)}}};m\
._drawAtom=funct\
ion(h,j){h.begin\
Path();if(this.s\
hadeAtoms){var l\
=\x0aj.srad/4,l=h.c\
reateRadialGradi\
ent(j.sxyz[0]-l,\
j.sxyz[1]-l,l,j.\
sxyz[0],j.sxyz[1\
],j.srad);l.addC\
olorStop(0,j.col\
or50);l.addColor\
Stop(1,\x22#FFFFFF\x22\
==j.color?\x22#D0D0\
D0\x22:j.color);h.f\
illStyle=l;h.arc\
(j.sxyz[0],j.sxy\
z[1],j.srad,0,c.\
_pi2);h.fill()}e\
lse h.fillStyle=\
j.color,h.arc(j.\
sxyz[0],j.sxyz[1\
],j.srad,0,c._pi\
2),h.fill(),h.st\
rokeStyle=\x22#0000\
00\x22,h.lineWidth=\
1,h.stroke()};m.\
_drawBond=functi\
on(c,j){99999!=j\
.pts[0][2]&&this\
._drawBondLines(\
c,j,j.spts[0],j.\
atoms[0].color);\
99999!=j.pts[1][\
2]&&this._drawBo\
ndLines(c,\x0aj,j.s\
pts[1],j.atoms[1\
].color)};m._dra\
wBondLines=funct\
ion(h,j,l,m){var\
 p=c._temp;p.wid\
th=this.bondWidt\
h;p.color=j.colo\
r?j.color:m;if(1\
==j.order)p.pt1=\
l,p.pt2=j.sxyz,t\
his._drawLine(h,\
p);else{p.pt1=c.\
_temp1;p.pt2=c._\
temp2;p.pta=l;p.\
ptb=j.sxyz;p.dx=\
p.ptb[0]-p.pta[0\
];p.dy=p.ptb[1]-\
p.pta[1];p.mag2d\
=Math.round(Math\
.sqrt(p.dx*p.dx+\
p.dy*p.dy));p.bo\
ndOrder=j.order;\
for(this._resetA\
xisCoordinates(p\
);0<p.bondOrder;\
)this._drawLine(\
h,p),p.bondOrder\
--,this._stepAxi\
sCoordinates(p)}\
};m._drawLine=fu\
nction(c,j){c.be\
ginPath();\x0ac.str\
okeStyle=j.color\
;c.moveTo(j.pt1[\
0],j.pt1[1]);c.l\
ineTo(j.pt2[0],j\
.pt2[1]);c.lineW\
idth=j.width;c.s\
troke()};m._rese\
tAxisCoordinates\
=function(c){var\
 j=c.mag2d>>3;1!\
=this.multipleBo\
ndSpacing&&(j*=t\
his.multipleBond\
Spacing);j=c.wid\
th+j;c.dxStep=Ma\
th.round(j*c.dy/\
c.mag2d);c.dySte\
p=Math.round(j*-\
c.dx/c.mag2d);c.\
pt1[0]=c.pta[0];\
c.pt1[1]=c.pta[1\
];c.pt2[0]=c.ptb\
[0];c.pt2[1]=c.p\
tb[1];j=c.bondOr\
der-1;c.pt1[0]-=\
Math.round(c.dxS\
tep*j/2);c.pt1[1\
]-=Math.round(c.\
dyStep*j/2);c.pt\
2[0]-=Math.round\
(c.dxStep*j/2);c\
.pt2[1]-=\x0aMath.r\
ound(c.dyStep*j/\
2)};m._stepAxisC\
oordinates=funct\
ion(c){c.pt1[0]+\
=c.dxStep;c.pt1[\
1]+=c.dyStep;c.p\
t2[0]+=c.dxStep;\
c.pt2[1]+=c.dySt\
ep};c._distance=\
function(c,j){fo\
r(var l=0,m=3;0<\
=--m;)var p=c[m]\
-j[m],l=l+p*p;re\
turn Math.sqrt(l\
)};c._dot=functi\
on(c,j){for(var \
l=0,m=3;0<=--m;)\
l+=c[m]*j[m];ret\
urn l};c._setPt=\
function(c,j){fo\
r(var l=3;0<=--l\
;)j[l]=c[l];retu\
rn j};c._scale=f\
unction(c,j){for\
(var l=3;0<=--l;\
)c[l]*=j};c._len\
gth=function(c){\
for(var j=0,l=3;\
0<=--l;)j+=c[l]*\
c[l];return Math\
.sqrt(j)};c._get\
PointAlong=\x0afunc\
tion(c,j,l){retu\
rn[(j[0]-c[0])*l\
+c[0],(j[1]-c[1]\
)*l+c[1],(j[2]-c\
[2])*l+c[2]]};c.\
_zorder=function\
(c,j){var l=c.sx\
yz[2],m=j.sxyz[2\
];return l<m?-1:\
l>m?1:0};c.M3=fu\
nction(){this.m0\
0=1;this.m10=thi\
s.m02=this.m01=0\
;this.m11=1;this\
.m21=this.m20=th\
is.m12=0;this.m2\
2=1};c.M3.protot\
ype.set=function\
(c,j,l,m,p,v,w,b\
,e){this.m00=c;t\
his.m01=j;this.m\
02=l;this.m10=m;\
this.m11=p;this.\
m12=v;this.m20=w\
;this.m21=b;this\
.m22=e};c.M3.pro\
totype.transform\
=function(c,j){j\
[0]=this.m00*c[0\
]+this.m01*c[1]+\
this.m02*c[2];j[\
1]=\x0athis.m10*c[0\
]+this.m11*c[1]+\
this.m12*c[2];j[\
2]=this.m20*c[0]\
+this.m21*c[1]+t\
his.m22*c[2]};c.\
M3.prototype.rot\
X=function(c){va\
r j=Math.cos(c);\
c=Math.sin(c);th\
is.m00=1;this.m1\
0=this.m02=this.\
m01=0;this.m11=j\
;this.m12=-c;thi\
s.m20=0;this.m21\
=c;this.m22=j};c\
.M3.prototype.ro\
tY=function(c){v\
ar j=Math.cos(c)\
;c=Math.sin(c);t\
his.m00=j;this.m\
01=0;this.m02=c;\
this.m10=0;this.\
m11=1;this.m12=0\
;this.m20=-c;thi\
s.m21=0;this.m22\
=j};c.M3.prototy\
pe.mul=function(\
c){this.set(c.m0\
0*this.m00+c.m01\
*this.m10+c.m02*\
this.m20,\x0ac.m00*\
this.m01+c.m01*t\
his.m11+c.m02*th\
is.m21,c.m00*thi\
s.m02+c.m01*this\
.m12+c.m02*this.\
m22,c.m10*this.m\
00+c.m11*this.m1\
0+c.m12*this.m20\
,c.m10*this.m01+\
c.m11*this.m11+c\
.m12*this.m21,c.\
m10*this.m02+c.m\
11*this.m12+c.m1\
2*this.m22,c.m20\
*this.m00+c.m21*\
this.m10+c.m22*t\
his.m20,c.m20*th\
is.m01+c.m21*thi\
s.m11+c.m22*this\
.m21,c.m20*this.\
m02+c.m21*this.m\
12+c.m22*this.m2\
2)};c._pi2=2*Mat\
h.PI;c.deg_per_r\
adian=180/Math.P\
I;c._z3=[0,0,0];\
c._temp1=[0,0,0]\
;c._temp2=[0,0,0\
];c._temp={};c._\
m3=new c.M3})(Jm\
ol._TMApplet);\x0a\
\x00\x03y\x81\
(\
function(a,m){\x22o\
bject\x22===typeof \
module&&\x22object\x22\
===typeof module\
.exports?module.\
exports=a.docume\
nt?m(a,!0):funct\
ion(a){if(!a.doc\
ument)throw Erro\
r(\x22jQuery requir\
es a window with\
 a document\x22);re\
turn m(a)}:m(a)}\
)(\x22undefined\x22!==\
typeof window?wi\
ndow:this,functi\
on(a,m){function\
 k(f){var w=f.le\
ngth,a=g.type(f)\
;return\x22function\
\x22===a||g.isWindo\
w(f)?!1:1===f.no\
deType&&w?!0:\x22ar\
ray\x22===a||0===w|\
|\x22number\x22===type\
of w&&0<w&&w-1 i\
n f}function h(f\
,w,a){if(g.isFun\
ction(w))return \
g.grep(f,functio\
n(f,g){return!!w\
.call(f,\x0ag,f)!==\
a});if(w.nodeTyp\
e)return g.grep(\
f,function(f){re\
turn f===w!==a})\
;if(\x22string\x22===t\
ypeof w){if(Vc.t\
est(w))return g.\
filter(w,f,a);w=\
g.filter(w,f)}re\
turn g.grep(f,fu\
nction(f){return\
 0<=g.inArray(f,\
w)!==a})}functio\
n e(f,w){do f=f[\
w];while(f&&1!==\
f.nodeType);retu\
rn f}function l(\
){y.addEventList\
ener?(y.removeEv\
entListener(\x22DOM\
ContentLoaded\x22,q\
,!1),a.removeEve\
ntListener(\x22load\
\x22,q,!1)):(y.deta\
chEvent(\x22onready\
statechange\x22,q),\
a.detachEvent(\x22o\
nload\x22,q))}funct\
ion q(){if(y.add\
EventListener||\x22\
load\x22===event.ty\
pe||\x0a\x22complete\x22=\
==y.readyState)l\
(),g.ready()}fun\
ction s(f,w,a){i\
f(void 0===a&&1=\
==f.nodeType)if(\
a=\x22data-\x22+w.repl\
ace(Wc,\x22-$1\x22).to\
LowerCase(),a=f.\
getAttribute(a),\
\x22string\x22===typeo\
f a){try{a=\x22true\
\x22===a?!0:\x22false\x22\
===a?!1:\x22null\x22==\
=a?null:+a+\x22\x22===\
a?+a:Xc.test(a)?\
g.parseJSON(a):a\
}catch(A){}g.dat\
a(f,w,a)}else a=\
void 0;return a}\
function u(f){fo\
r(var a in f)if(\
!(\x22data\x22===a&&g.\
isEmptyObject(f[\
a]))&&\x22toJSON\x22!=\
=a)return!1;retu\
rn!0}function b(\
f,a,p,A){if(g.ac\
ceptData(f)){var\
 b=g.expando,c=f\
.nodeType,d=c?g.\
cache:f,n=\x0ac?f[b\
]:f[b]&&b;if(n&&\
d[n]&&(A||d[n].d\
ata)||!(void 0==\
=p&&\x22string\x22===t\
ypeof a)){n||(n=\
c?f[b]=j.pop()||\
g.guid++:b);d[n]\
||(d[n]=c?{}:{to\
JSON:g.noop});if\
(\x22object\x22===type\
of a||\x22function\x22\
===typeof a)A?d[\
n]=g.extend(d[n]\
,a):d[n].data=g.\
extend(d[n].data\
,a);f=d[n];A||(f\
.data||(f.data={\
}),f=f.data);voi\
d 0!==p&&(f[g.ca\
melCase(a)]=p);\x22\
string\x22===typeof\
 a?(p=f[a],null=\
=p&&(p=f[g.camel\
Case(a)])):p=f;r\
eturn p}}}functi\
on c(f,a,p){if(g\
.acceptData(f)){\
var A,b,c=f.node\
Type,j=c?g.cache\
:f,d=c?f[g.expan\
do]:g.expando;if\
(j[d]){if(a&&\x0a(A\
=p?j[d]:j[d].dat\
a)){g.isArray(a)\
?a=a.concat(g.ma\
p(a,g.camelCase)\
):a in A?a=[a]:(\
a=g.camelCase(a)\
,a=a in A?[a]:a.\
split(\x22 \x22));for(\
b=a.length;b--;)\
delete A[a[b]];i\
f(p?!u(A):!g.isE\
mptyObject(A))re\
turn}if(!p&&(del\
ete j[d].data,!u\
(j[d])))return;c\
?g.cleanData([f]\
,!0):v.deleteExp\
ando||j!=j.windo\
w?delete j[d]:j[\
d]=null}}}functi\
on d(){return!0}\
function t(){ret\
urn!1}function F\
(){try{return y.\
activeElement}ca\
tch(f){}}functio\
n C(f){var a=mc.\
split(\x22|\x22);f=f.c\
reateDocumentFra\
gment();if(f.cre\
ateElement)for(;\
a.length;)f.crea\
teElement(a.pop(\
));\x0areturn f}fun\
ction K(f,a){var\
 p,A,b=0,c=typeo\
f f.getElementsB\
yTagName!==ka?f.\
getElementsByTag\
Name(a||\x22*\x22):typ\
eof f.querySelec\
torAll!==ka?f.qu\
erySelectorAll(a\
||\x22*\x22):void 0;if\
(!c){c=[];for(p=\
f.childNodes||f;\
null!=(A=p[b]);b\
++)!a||g.nodeNam\
e(A,a)?c.push(A)\
:g.merge(c,K(A,a\
))}return void 0\
===a||a&&g.nodeN\
ame(f,a)?g.merge\
([f],c):c}functi\
on rb(f){Mb.test\
(f.type)&&(f.def\
aultChecked=f.ch\
ecked)}function \
Ya(f,a){return g\
.nodeName(f,\x22tab\
le\x22)&&g.nodeName\
(11!==a.nodeType\
?a:a.firstChild,\
\x22tr\x22)?f.getEleme\
ntsByTagName(\x22tb\
ody\x22)[0]||\x0af.app\
endChild(f.owner\
Document.createE\
lement(\x22tbody\x22))\
:f}function Ea(f\
){f.type=(null!=\
=g.find.attr(f,\x22\
type\x22))+\x22/\x22+f.ty\
pe;return f}func\
tion U(f){var a=\
Yc.exec(f.type);\
a?f.type=a[1]:f.\
removeAttribute(\
\x22type\x22);return f\
}function P(f,a)\
{for(var p,A=0;n\
ull!=(p=f[A]);A+\
+)g._data(p,\x22glo\
balEval\x22,!a||g._\
data(a[A],\x22globa\
lEval\x22))}functio\
n Fa(f,a){if(1==\
=a.nodeType&&g.h\
asData(f)){var p\
,A,b;A=g._data(f\
);var c=g._data(\
a,A),j=A.events;\
if(j)for(p in de\
lete c.handle,c.\
events={},j){A=0\
;for(b=j[p].leng\
th;A<b;A++)g.eve\
nt.add(a,\x0ap,j[p]\
[A])}c.data&&(c.\
data=g.extend({}\
,c.data))}}funct\
ion Pa(f,w){var \
p=g(w.createElem\
ent(f)).appendTo\
(w.body),A=a.get\
DefaultComputedS\
tyle?a.getDefaul\
tComputedStyle(p\
[0]).display:g.c\
ss(p[0],\x22display\
\x22);p.detach();re\
turn A}function \
db(f){var a=y,p=\
nc[f];if(!p){p=P\
a(f,a);if(\x22none\x22\
===p||!p)eb=(eb|\
|g(\x22<iframe fram\
eborder='0' widt\
h='0' height='0'\
/>\x22)).appendTo(a\
.documentElement\
),a=(eb[0].conte\
ntWindow||eb[0].\
contentDocument)\
.document,a.writ\
e(),a.close(),p=\
Pa(f,a),eb.detac\
h();nc[f]=p}retu\
rn p}function fb\
(f,\x0aa){return{ge\
t:function(){var\
 p=f();if(null!=\
p)if(p)delete th\
is.get;else retu\
rn(this.get=a).a\
pply(this,argume\
nts)}}}function \
gb(f,a){if(a in \
f)return a;for(v\
ar p=a.charAt(0)\
.toUpperCase()+a\
.slice(1),A=a,b=\
oc.length;b--;)i\
f(a=oc[b]+p,a in\
 f)return a;retu\
rn A}function va\
(f,a){for(var p,\
A,b,c=[],j=0,d=f\
.length;j<d;j++)\
if(A=f[j],A.styl\
e)if(c[j]=g._dat\
a(A,\x22olddisplay\x22\
),p=A.style.disp\
lay,a)!c[j]&&\x22no\
ne\x22===p&&(A.styl\
e.display=\x22\x22),\x22\x22\
===A.style.displ\
ay&&hb(A)&&(c[j]\
=g._data(A,\x22oldd\
isplay\x22,db(A.nod\
eName)));\x0aelse i\
f(!c[j]&&(b=hb(A\
),p&&\x22none\x22!==p|\
|!b))g._data(A,\x22\
olddisplay\x22,b?p:\
g.css(A,\x22display\
\x22));for(j=0;j<d;\
j++)if(A=f[j],A.\
style&&(!a||\x22non\
e\x22===A.style.dis\
play||\x22\x22===A.sty\
le.display))A.st\
yle.display=a?c[\
j]||\x22\x22:\x22none\x22;re\
turn f}function \
la(f,a,p){return\
(f=Zc.exec(a))?M\
ath.max(0,f[1]-(\
p||0))+(f[2]||\x22p\
x\x22):a}function x\
(f,a,p,b,c){a=p=\
==(b?\x22border\x22:\x22c\
ontent\x22)?4:\x22widt\
h\x22===a?1:0;for(v\
ar j=0;4>a;a+=2)\
\x22margin\x22===p&&(j\
+=g.css(f,p+Qa[a\
],!0,c)),b?(\x22con\
tent\x22===p&&(j-=g\
.css(f,\x22padding\x22\
+Qa[a],!0,c)),\x22m\
argin\x22!==p&&(j-=\
\x0ag.css(f,\x22border\
\x22+Qa[a]+\x22Width\x22,\
!0,c))):(j+=g.cs\
s(f,\x22padding\x22+Qa\
[a],!0,c),\x22paddi\
ng\x22!==p&&(j+=g.c\
ss(f,\x22border\x22+Qa\
[a]+\x22Width\x22,!0,c\
)));return j}fun\
ction Z(f,a,p){v\
ar b=!0,c=\x22width\
\x22===a?f.offsetWi\
dth:f.offsetHeig\
ht,j=Ra(f),d=v.b\
oxSizing()&&\x22bor\
der-box\x22===g.css\
(f,\x22boxSizing\x22,!\
1,j);if(0>=c||nu\
ll==c){c=Sa(f,a,\
j);if(0>c||null=\
=c)c=f.style[a];\
if(sb.test(c))re\
turn c;b=d&&(v.b\
oxSizingReliable\
()||c===f.style[\
a]);c=parseFloat\
(c)||0}return c+\
x(f,a,p||(d?\x22bor\
der\x22:\x22content\x22),\
b,j)+\x22px\x22}functi\
on L(f,a,p,b,g){\
return new L.pro\
totype.init(f,\x0aa\
,p,b,g)}function\
 fa(){setTimeout\
(function(){Za=v\
oid 0});return Z\
a=g.now()}functi\
on O(f,a){var p,\
b={height:f},g=0\
;for(a=a?1:0;4>g\
;g+=2-a)p=Qa[g],\
b[\x22margin\x22+p]=b[\
\x22padding\x22+p]=f;a\
&&(b.opacity=b.w\
idth=f);return b\
}function wa(f,a\
,p){for(var b,g=\
(ib[a]||[]).conc\
at(ib[\x22*\x22]),c=0,\
j=g.length;c<j;c\
++)if(b=g[c].cal\
l(p,a,f))return \
b}function jb(f,\
a,p){var b,c,j=0\
,d=tb.length,n=g\
.Deferred().alwa\
ys(function(){de\
lete e.elem}),e=\
function(){if(c)\
return!1;for(var\
 a=Za||fa(),a=Ma\
th.max(0,r.start\
Time+r.duration-\
a),w=\x0a1-(a/r.dur\
ation||0),p=0,b=\
r.tweens.length;\
p<b;p++)r.tweens\
[p].run(w);n.not\
ifyWith(f,[r,w,a\
]);if(1>w&&b)ret\
urn a;n.resolveW\
ith(f,[r]);retur\
n!1},r=n.promise\
({elem:f,props:g\
.extend({},a),op\
ts:g.extend(!0,{\
specialEasing:{}\
},p),originalPro\
perties:a,origin\
alOptions:p,star\
tTime:Za||fa(),d\
uration:p.durati\
on,tweens:[],cre\
ateTween:functio\
n(a,w){var p=g.T\
ween(f,r.opts,a,\
w,r.opts.special\
Easing[a]||r.opt\
s.easing);r.twee\
ns.push(p);retur\
n p},stop:functi\
on(a){var w=0,p=\
a?r.tweens.lengt\
h:0;if(c)return \
this;for(c=\x0a!0;w\
<p;w++)r.tweens[\
w].run(1);a?n.re\
solveWith(f,[r,a\
]):n.rejectWith(\
f,[r,a]);return \
this}});a=r.prop\
s;p=r.opts.speci\
alEasing;var h,t\
,l,k;for(b in a)\
if(h=g.camelCase\
(b),t=p[h],l=a[b\
],g.isArray(l)&&\
(t=l[1],l=a[b]=l\
[0]),b!==h&&(a[h\
]=l,delete a[b])\
,(k=g.cssHooks[h\
])&&\x22expand\x22in k\
)for(b in l=k.ex\
pand(l),delete a\
[h],l)b in a||(a\
[b]=l[b],p[b]=t)\
;else p[h]=t;for\
(;j<d;j++)if(b=t\
b[j].call(r,f,a,\
r.opts))return b\
;g.map(a,wa,r);g\
.isFunction(r.op\
ts.start)&&r.opt\
s.start.call(f,r\
);g.fx.timer(g.e\
xtend(e,{elem:f,\
anim:r,\x0aqueue:r.\
opts.queue}));re\
turn r.progress(\
r.opts.progress)\
.done(r.opts.don\
e,r.opts.complet\
e).fail(r.opts.f\
ail).always(r.op\
ts.always)}funct\
ion kb(f){return\
 function(a,p){\x22\
string\x22!==typeof\
 a&&(p=a,a=\x22*\x22);\
var b,c=0,j=a.to\
LowerCase().matc\
h(xa)||[];if(g.i\
sFunction(p))for\
(;b=j[c++];)\x22+\x22=\
==b.charAt(0)?(b\
=b.slice(1)||\x22*\x22\
,(f[b]=f[b]||[])\
.unshift(p)):(f[\
b]=f[b]||[]).pus\
h(p)}}function u\
b(f,a,p,b){funct\
ion c(n){var e;j\
[n]=!0;g.each(f[\
n]||[],function(\
f,g){var n=g(a,p\
,b);if(\x22string\x22=\
==typeof n&&!d&&\
!j[n])return a.d\
ataTypes.unshift\
(n),\x0ac(n),!1;if(\
d)return!(e=n)})\
;return e}var j=\
{},d=f===Nb;retu\
rn c(a.dataTypes\
[0])||!j[\x22*\x22]&&c\
(\x22*\x22)}function y\
a(f,a){var p,b,c\
=g.ajaxSettings.\
flatOptions||{};\
for(b in a)void \
0!==a[b]&&((c[b]\
?f:p||(p={}))[b]\
=a[b]);p&&g.exte\
nd(!0,f,p);retur\
n f}function ma(\
f,a,p,b){var c;i\
f(g.isArray(a))g\
.each(a,function\
(a,w){p||ad.test\
(f)?b(f,w):ma(f+\
\x22[\x22+(\x22object\x22===\
typeof w?a:\x22\x22)+\x22\
]\x22,w,p,b)});else\
 if(!p&&\x22object\x22\
===g.type(a))for\
(c in a)ma(f+\x22[\x22\
+c+\x22]\x22,a[c],p,b)\
;else b(f,a)}fun\
ction D(f){try{r\
eturn f?new a.Ac\
tiveXObject(\x22Mic\
rosoft.XMLHTTP\x22)\
:\x0anew a.XMLHttpR\
equest}catch(w){\
}}function aa(){\
try{return new a\
.XMLHttpRequest}\
catch(f){}}funct\
ion V(f){return \
g.isWindow(f)?f:\
9===f.nodeType?f\
.defaultView||f.\
parentWindow:!1}\
var j=[],n=j.sli\
ce,r=j.concat,z=\
j.push,G=j.index\
Of,Q={},bd=Q.toS\
tring,za=Q.hasOw\
nProperty,Ob=\x22\x22.\
trim,v={},g=func\
tion(f,a){return\
 new g.fn.init(f\
,a)},cd=/^[\x5cs\x5cuF\
EFF\x5cxA0]+|[\x5cs\x5cuF\
EFF\x5cxA0]+$/g,dd=\
/^-ms-/,ed=/-([\x5c\
da-z])/gi,fd=fun\
ction(f,a){retur\
n a.toUpperCase(\
)};g.fn=g.protot\
ype={jquery:\x221.1\
1.0\x22,constructor\
:g,selector:\x22\x22,l\
ength:0,\x0atoArray\
:function(){retu\
rn n.call(this)}\
,get:function(f)\
{return null!=f?\
0>f?this[f+this.\
length]:this[f]:\
n.call(this)},pu\
shStack:function\
(f){f=g.merge(th\
is.constructor()\
,f);f.prevObject\
=this;f.context=\
this.context;ret\
urn f},each:func\
tion(f,a){return\
 g.each(this,f,a\
)},map:function(\
f){return this.p\
ushStack(g.map(t\
his,function(a,p\
){return f.call(\
a,p,a)}))},slice\
:function(){retu\
rn this.pushStac\
k(n.apply(this,a\
rguments))},firs\
t:function(){ret\
urn this.eq(0)},\
last:function(){\
return this.eq(-\
1)},eq:function(\
f){var a=\x0athis.l\
ength;f=+f+(0>f?\
a:0);return this\
.pushStack(0<=f&\
&f<a?[this[f]]:[\
])},end:function\
(){return this.p\
revObject||this.\
constructor(null\
)},push:z,sort:j\
.sort,splice:j.s\
plice};g.extend=\
g.fn.extend=func\
tion(){var f,a,p\
,b,c,j=arguments\
[0]||{},d=1,n=ar\
guments.length,e\
=!1;\x22boolean\x22===\
typeof j&&(e=j,j\
=arguments[d]||{\
},d++);\x22object\x22!\
==typeof j&&!g.i\
sFunction(j)&&(j\
={});d===n&&(j=t\
his,d--);for(;d<\
n;d++)if(null!=(\
c=arguments[d]))\
for(b in c)f=j[b\
],p=c[b],j!==p&&\
(e&&p&&(g.isPlai\
nObject(p)||(a=g\
.isArray(p)))?(a\
?\x0a(a=!1,f=f&&g.i\
sArray(f)?f:[]):\
f=f&&g.isPlainOb\
ject(f)?f:{},j[b\
]=g.extend(e,f,p\
)):void 0!==p&&(\
j[b]=p));return \
j};g.extend({exp\
ando:\x22jQuery\x22+(\x22\
1.11.0\x22+Math.ran\
dom()).replace(/\
\x5cD/g,\x22\x22),isReady\
:!0,error:functi\
on(f){throw Erro\
r(f);},noop:func\
tion(){},isFunct\
ion:function(f){\
return\x22function\x22\
===g.type(f)},is\
Array:Array.isAr\
ray||function(f)\
{return\x22array\x22==\
=g.type(f)},isWi\
ndow:function(f)\
{return null!=f&\
&f==f.window},is\
Numeric:function\
(f){return 0<=f-\
parseFloat(f)},i\
sEmptyObject:fun\
ction(f){for(var\
 a in f)return!1\
;\x0areturn!0},isPl\
ainObject:functi\
on(f){var a;if(!\
f||\x22object\x22!==g.\
type(f)||f.nodeT\
ype||g.isWindow(\
f))return!1;try{\
if(f.constructor\
&&!za.call(f,\x22co\
nstructor\x22)&&!za\
.call(f.construc\
tor.prototype,\x22i\
sPrototypeOf\x22))r\
eturn!1}catch(p)\
{return!1}if(v.o\
wnLast)for(a in \
f)return za.call\
(f,a);for(a in f\
);return void 0=\
==a||za.call(f,a\
)},type:function\
(f){return null=\
=f?f+\x22\x22:\x22object\x22\
===typeof f||\x22fu\
nction\x22===typeof\
 f?Q[bd.call(f)]\
||\x22object\x22:typeo\
f f},globalEval:\
function(f){f&&g\
.trim(f)&&(a.exe\
cScript||functio\
n(f){a.eval.call\
(a,\x0af)})(f)},cam\
elCase:function(\
f){return f.repl\
ace(dd,\x22ms-\x22).re\
place(ed,fd)},no\
deName:function(\
f,a){return f.no\
deName&&f.nodeNa\
me.toLowerCase()\
===a.toLowerCase\
()},each:functio\
n(f,a,p){var b,g\
=0,c=f.length;b=\
k(f);if(p)if(b)f\
or(;g<c&&!(b=a.a\
pply(f[g],p),!1=\
==b);g++);else f\
or(g in f){if(b=\
a.apply(f[g],p),\
!1===b)break}els\
e if(b)for(;g<c&\
&!(b=a.call(f[g]\
,g,f[g]),!1===b)\
;g++);else for(g\
 in f)if(b=a.cal\
l(f[g],g,f[g]),!\
1===b)break;retu\
rn f},trim:Ob&&!\
Ob.call(\x22\x5cufeff\x5c\
u00a0\x22)?function\
(f){return null=\
=f?\x22\x22:Ob.call(f)\
}:\x0afunction(f){r\
eturn null==f?\x22\x22\
:(f+\x22\x22).replace(\
cd,\x22\x22)},makeArra\
y:function(f,a){\
var p=a||[];null\
!=f&&(k(Object(f\
))?g.merge(p,\x22st\
ring\x22===typeof f\
?[f]:f):z.call(p\
,f));return p},i\
nArray:function(\
f,a,p){var b;if(\
a){if(G)return G\
.call(a,f,p);b=a\
.length;for(p=p?\
0>p?Math.max(0,b\
+p):p:0;p<b;p++)\
if(p in a&&a[p]=\
==f)return p}ret\
urn-1},merge:fun\
ction(f,a){for(v\
ar p=+a.length,b\
=0,g=f.length;b<\
p;)f[g++]=a[b++]\
;if(p!==p)for(;v\
oid 0!==a[b];)f[\
g++]=a[b++];f.le\
ngth=g;return f}\
,grep:function(f\
,a,p){for(var b=\
[],g=0,c=\x0af.leng\
th,j=!p;g<c;g++)\
p=!a(f[g],g),p!=\
=j&&b.push(f[g])\
;return b},map:f\
unction(f,a,p){v\
ar b,g=0,c=f.len\
gth,j=[];if(k(f)\
)for(;g<c;g++)b=\
a(f[g],g,p),null\
!=b&&j.push(b);e\
lse for(g in f)b\
=a(f[g],g,p),nul\
l!=b&&j.push(b);\
return r.apply([\
],j)},guid:1,pro\
xy:function(f,a)\
{var p,b;\x22string\
\x22===typeof a&&(b\
=f[a],a=f,f=b);i\
f(g.isFunction(f\
))return p=n.cal\
l(arguments,2),b\
=function(){retu\
rn f.apply(a||th\
is,p.concat(n.ca\
ll(arguments)))}\
,b.guid=f.guid=f\
.guid||g.guid++,\
b},now:function(\
){return+new Dat\
e},support:v});\x0a\
g.each(\x22Boolean \
Number String Fu\
nction Array Dat\
e RegExp Object \
Error\x22.split(\x22 \x22\
),function(f,a){\
Q[\x22[object \x22+a+\x22\
]\x22]=a.toLowerCas\
e()});var Pb=a,E\
=function(f,a,p,\
b){var g,c,j,d,n\
;(a?a.ownerDocum\
ent||a:W)!==R&&n\
a(a);a=a||R;p=p|\
|[];if(!f||\x22stri\
ng\x22!==typeof f)r\
eturn p;if(1!==(\
d=a.nodeType)&&9\
!==d)return[];if\
(X&&!b){if(g=gd.\
exec(f))if(j=g[1\
])if(9===d)if((c\
=a.getElementByI\
d(j))&&c.parentN\
ode){if(c.id===j\
)return p.push(c\
),p}else return \
p;else{if(a.owne\
rDocument&&(c=a.\
ownerDocument.ge\
tElementById(j))\
&&ra(a,\x0ac)&&c.id\
===j)return p.pu\
sh(c),p}else{if(\
g[2])return Ga.a\
pply(p,a.getElem\
entsByTagName(f)\
),p;if((j=g[3])&\
&I.getElementsBy\
ClassName&&a.get\
ElementsByClassN\
ame)return Ga.ap\
ply(p,a.getEleme\
ntsByClassName(j\
)),p}if(I.qsa&&(\
!S||!S.test(f)))\
{c=g=M;j=a;n=9==\
=d&&f;if(1===d&&\
\x22object\x22!==a.nod\
eName.toLowerCas\
e()){d=sa(f);(g=\
a.getAttribute(\x22\
id\x22))?c=g.replac\
e(hd,\x22\x5c\x5c$&\x22):a.s\
etAttribute(\x22id\x22\
,c);c=\x22[id='\x22+c+\
\x22'] \x22;for(j=d.le\
ngth;j--;)d[j]=c\
+vb(d[j]);j=Qb.t\
est(f)&&ga(a.par\
entNode)||a;n=d.\
join(\x22,\x22)}if(n)t\
ry{return Ga.app\
ly(p,\x0aj.querySel\
ectorAll(n)),p}c\
atch(e){}finally\
{g||a.removeAttr\
ibute(\x22id\x22)}}}va\
r r;a:{f=f.repla\
ce(wb,\x22$1\x22);c=sa\
(f);if(!b&&1===c\
.length){g=c[0]=\
c[0].slice(0);if\
(2<g.length&&\x22ID\
\x22===(r=g[0]).typ\
e&&I.getById&&9=\
==a.nodeType&&X&\
&H.relative[g[1]\
.type]){a=(H.fin\
d.ID(r.matches[0\
].replace(Ha,Ia)\
,a)||[])[0];if(!\
a){r=p;break a}f\
=f.slice(g.shift\
().value.length)\
}for(d=xb.needsC\
ontext.test(f)?0\
:g.length;d--;){\
r=g[d];if(H.rela\
tive[j=r.type])b\
reak;if(j=H.find\
[j])if(b=j(r.mat\
ches[0].replace(\
Ha,Ia),Qb.test(g\
[0].type)&&\x0aga(a\
.parentNode)||a)\
){g.splice(d,1);\
f=b.length&&vb(g\
);if(!f){Ga.appl\
y(p,b);r=p;break\
 a}break}}}$a(f,\
c)(b,a,!X,p,Qb.t\
est(f)&&ga(a.par\
entNode)||a);r=p\
}return r},Rb=fu\
nction(){functio\
n f(p,b){a.push(\
p+\x22 \x22)>H.cacheLe\
ngth&&delete f[a\
.shift()];return\
 f[p+\x22 \x22]=b}var \
a=[];return f},o\
a=function(f){f[\
M]=!0;return f},\
pa=function(f){v\
ar a=R.createEle\
ment(\x22div\x22);try{\
return!!f(a)}cat\
ch(p){return!1}f\
inally{a.parentN\
ode&&a.parentNod\
e.removeChild(a)\
}},Sb=function(f\
,a){for(var p=f.\
split(\x22|\x22),b=f.l\
ength;b--;)H.att\
rHandle[p[b]]=\x0aa\
},pc=function(f,\
a){var p=a&&f,b=\
p&&1===f.nodeTyp\
e&&1===a.nodeTyp\
e&&(~a.sourceInd\
ex||ha)-(~f.sour\
ceIndex||ha);if(\
b)return b;if(p)\
for(;p=p.nextSib\
ling;)if(p===a)r\
eturn-1;return f\
?1:-1},id=functi\
on(f){return fun\
ction(a){return\x22\
input\x22===a.nodeN\
ame.toLowerCase(\
)&&a.type===f}},\
jd=function(f){r\
eturn function(a\
){var p=a.nodeNa\
me.toLowerCase()\
;return(\x22input\x22=\
==p||\x22button\x22===\
p)&&a.type===f}}\
,ta=function(f){\
return oa(functi\
on(a){a=+a;retur\
n oa(function(p,\
b){for(var g,c=f\
([],p.length,a),\
j=c.length;j--;)\
if(p[g=\x0ac[j]])p[\
g]=!(b[g]=p[g])}\
)})},ga=function\
(f){return f&&ty\
peof f.getElemen\
tsByTagName!==T&\
&f},qc=function(\
){},sa=function(\
f,a){var p,b,g,c\
,j,d,n;if(j=Ja[f\
+\x22 \x22])return a?0\
:j.slice(0);j=f;\
d=[];for(n=H.pre\
Filter;j;){if(!p\
||(b=kd.exec(j))\
)b&&(j=j.slice(b\
[0].length)||j),\
d.push(g=[]);p=!\
1;if(b=ld.exec(j\
))p=b.shift(),g.\
push({value:p,ty\
pe:b[0].replace(\
wb,\x22 \x22)}),j=j.sl\
ice(p.length);fo\
r(c in H.filter)\
if((b=xb[c].exec\
(j))&&(!n[c]||(b\
=n[c](b))))p=b.s\
hift(),g.push({v\
alue:p,type:c,ma\
tches:b}),j=j.sl\
ice(p.length);\x0ai\
f(!p)break}retur\
n a?j.length:j?E\
.error(f):Ja(f,d\
).slice(0)},vb=f\
unction(f){for(v\
ar a=0,p=f.lengt\
h,b=\x22\x22;a<p;a++)b\
+=f[a].value;ret\
urn b},Tb=functi\
on(f,a,p){var b=\
a.dir,g=p&&\x22pare\
ntNode\x22===b,c=md\
++;return a.firs\
t?function(a,p,w\
){for(;a=a[b];)i\
f(1===a.nodeType\
||g)return f(a,p\
,w)}:function(a,\
p,w){var j,d,n=[\
ba,c];if(w)for(;\
a=a[b];){if((1==\
=a.nodeType||g)&\
&f(a,p,w))return\
!0}else for(;a=a\
[b];)if(1===a.no\
deType||g){d=a[M\
]||(a[M]={});if(\
(j=d[b])&&j[0]==\
=ba&&j[1]===c)re\
turn n[2]=j[2];d\
[b]=n;if(n[2]=f(\
a,p,\x0aw))return!0\
}}},Ub=function(\
f){return 1<f.le\
ngth?function(a,\
p,b){for(var g=f\
.length;g--;)if(\
!f[g](a,p,b))ret\
urn!1;return!0}:\
f[0]},Ta=functio\
n(f,a,p,b,g){for\
(var c,j=[],d=0,\
n=f.length,e=nul\
l!=a;d<n;d++)if(\
c=f[d])if(!p||p(\
c,b,g))j.push(c)\
,e&&a.push(d);re\
turn j},Vb=funct\
ion(f,a,p,b,g,c)\
{b&&!b[M]&&(b=Vb\
(b));g&&!g[M]&&(\
g=Vb(g,c));retur\
n oa(function(c,\
j,d,n){var e,r,e\
a=[],l=[],h=j.le\
ngth,t;if(!(t=c)\
){t=a||\x22*\x22;for(v\
ar k=d.nodeType?\
[d]:d,B=[],z=0,T\
=k.length;z<T;z+\
+)E(t,k[z],B);t=\
B}t=f&&(c||!a)?T\
a(t,ea,f,d,\x0an):t\
;k=p?g||(c?f:h||\
b)?[]:j:t;p&&p(t\
,k,d,n);if(b){e=\
Ta(k,l);b(e,[],d\
,n);for(d=e.leng\
th;d--;)if(r=e[d\
])k[l[d]]=!(t[l[\
d]]=r)}if(c){if(\
g||f){if(g){e=[]\
;for(d=k.length;\
d--;)if(r=k[d])e\
.push(t[d]=r);g(\
null,k=[],e,n)}f\
or(d=k.length;d-\
-;)if((r=k[d])&&\
-1<(e=g?Ua.call(\
c,r):ea[d]))c[e]\
=!(j[e]=r)}}else\
 k=Ta(k===j?k.sp\
lice(h,k.length)\
:k),g?g(null,j,k\
,n):Ga.apply(j,k\
)})},Wb=function\
(f){var a,p,b,g=\
f.length,c=H.rel\
ative[f[0].type]\
;p=c||H.relative\
[\x22 \x22];for(var j=\
c?1:0,d=Tb(funct\
ion(f){return f=\
==a},p,!0),n=Tb(\
function(f){retu\
rn-1<\x0aUa.call(a,\
f)},p,!0),e=[fun\
ction(f,p,b){ret\
urn!c&&(b||p!==A\
a)||((a=p).nodeT\
ype?d(f,p,b):n(f\
,p,b))}];j<g;j++\
)if(p=H.relative\
[f[j].type])e=[T\
b(Ub(e),p)];else\
{p=H.filter[f[j]\
.type].apply(nul\
l,f[j].matches);\
if(p[M]){for(b=+\
+j;b<g&&!H.relat\
ive[f[b].type];b\
++);return Vb(1<\
j&&Ub(e),1<j&&vb\
(f.slice(0,j-1).\
concat({value:\x22 \
\x22===f[j-2].type?\
\x22*\x22:\x22\x22})).replac\
e(wb,\x22$1\x22),p,j<b\
&&Wb(f.slice(j,b\
)),b<g&&Wb(f=f.s\
lice(b)),b<g&&vb\
(f))}e.push(p)}r\
eturn Ub(e)},Ba,\
I,H,Ka,rc,$a,Aa,\
qa,Ca,na,R,ia,X,\
S,ca,La,ra,M=\x22si\
zzle\x22+-new Date,\
\x0aW=Pb.document,b\
a=0,md=0,sc=Rb()\
,Ja=Rb(),Da=Rb()\
,B=function(f,a)\
{f===a&&(Ca=!0);\
return 0},T=\x22und\
efined\x22,ha=-2147\
483648,da={}.has\
OwnProperty,N=[]\
,ua=N.pop,nd=N.p\
ush,Ga=N.push,tc\
=N.slice,Ua=N.in\
dexOf||function(\
f){for(var a=0,p\
=this.length;a<p\
;a++)if(this[a]=\
==f)return a;ret\
urn-1},uc=\x22(?:\x5c\x5c\
\x5c\x5c.|[\x5c\x5cw-]|[^\x5c\x5cx\
00-\x5c\x5cxa0])+\x22.rep\
lace(\x22w\x22,\x22w#\x22),v\
c=\x22\x5c\x5c[[\x5c\x5cx20\x5c\x5ct\x5c\
\x5cr\x5c\x5cn\x5c\x5cf]*((?:\x5c\x5c\
\x5c\x5c.|[\x5c\x5cw-]|[^\x5c\x5cx\
00-\x5c\x5cxa0])+)[\x5c\x5cx\
20\x5c\x5ct\x5c\x5cr\x5c\x5cn\x5c\x5cf]*\
(?:([*^$|!~]?=)[\
\x5c\x5cx20\x5c\x5ct\x5c\x5cr\x5c\x5cn\x5c\x5c\
f]*(?:(['\x5c\x22])((?\
:\x5c\x5c\x5c\x5c.|[^\x5c\x5c\x5c\x5c])*\
?)\x5c\x5c3|(\x22+uc+\x22)|)\
|)[\x5c\x5cx20\x5c\x5ct\x5c\x5cr\x5c\x5c\
n\x5c\x5cf]*\x5c\x5c]\x22,\x0aXb=\x22\
:((?:\x5c\x5c\x5c\x5c.|[\x5c\x5cw-\
]|[^\x5c\x5cx00-\x5c\x5cxa0]\
)+)(?:\x5c\x5c(((['\x5c\x22]\
)((?:\x5c\x5c\x5c\x5c.|[^\x5c\x5c\x5c\
\x5c])*?)\x5c\x5c3|((?:\x5c\x5c\
\x5c\x5c.|[^\x5c\x5c\x5c\x5c()[\x5c\x5c]\
]|\x22+vc.replace(3\
,8)+\x22)*)|.*)\x5c\x5c)|\
)\x22,wb=RegExp(\x22^[\
\x5c\x5cx20\x5c\x5ct\x5c\x5cr\x5c\x5cn\x5c\x5c\
f]+|((?:^|[^\x5c\x5c\x5c\x5c\
])(?:\x5c\x5c\x5c\x5c.)*)[\x5c\x5c\
x20\x5c\x5ct\x5c\x5cr\x5c\x5cn\x5c\x5cf]\
+$\x22,\x22g\x22),kd=/^[\x5c\
x20\x5ct\x5cr\x5cn\x5cf]*,[\x5c\
x20\x5ct\x5cr\x5cn\x5cf]*/,l\
d=/^[\x5cx20\x5ct\x5cr\x5cn\x5c\
f]*([>+~]|[\x5cx20\x5c\
t\x5cr\x5cn\x5cf])[\x5cx20\x5ct\
\x5cr\x5cn\x5cf]*/,od=Reg\
Exp(\x22=[\x5c\x5cx20\x5c\x5ct\x5c\
\x5cr\x5c\x5cn\x5c\x5cf]*([^\x5c\x5c]\
'\x5c\x22]*?)[\x5c\x5cx20\x5c\x5ct\
\x5c\x5cr\x5c\x5cn\x5c\x5cf]*\x5c\x5c]\x22,\
\x22g\x22),pd=RegExp(X\
b),qd=RegExp(\x22^\x22\
+uc+\x22$\x22),xb={ID:\
/^#((?:\x5c\x5c.|[\x5cw-]\
|[^\x5cx00-\x5cxa0])+)\
/,CLASS:/^\x5c.((?:\
\x5c\x5c.|[\x5cw-]|[^\x5cx00\
-\x5cxa0])+)/,\x0aTAG:\
RegExp(\x22^(\x22+\x22(?:\
\x5c\x5c\x5c\x5c.|[\x5c\x5cw-]|[^\x5c\
\x5cx00-\x5c\x5cxa0])+\x22.r\
eplace(\x22w\x22,\x22w*\x22)\
+\x22)\x22),ATTR:RegEx\
p(\x22^\x22+vc),PSEUDO\
:RegExp(\x22^\x22+Xb),\
CHILD:RegExp(\x22^:\
(only|first|last\
|nth|nth-last)-(\
child|of-type)(?\
:\x5c\x5c([\x5c\x5cx20\x5c\x5ct\x5c\x5cr\
\x5c\x5cn\x5c\x5cf]*(even|od\
d|(([+-]|)(\x5c\x5cd*)\
n|)[\x5c\x5cx20\x5c\x5ct\x5c\x5cr\x5c\
\x5cn\x5c\x5cf]*(?:([+-]|\
)[\x5c\x5cx20\x5c\x5ct\x5c\x5cr\x5c\x5cn\
\x5c\x5cf]*(\x5c\x5cd+)|))[\x5c\
\x5cx20\x5c\x5ct\x5c\x5cr\x5c\x5cn\x5c\x5cf\
]*\x5c\x5c)|)\x22,\x22i\x22),bo\
ol:RegExp(\x22^(?:c\
hecked|selected|\
async|autofocus|\
autoplay|control\
s|defer|disabled\
|hidden|ismap|lo\
op|multiple|open\
|readonly|requir\
ed|scoped)$\x22,\x22i\x22\
),needsContext:R\
egExp(\x22^[\x5c\x5cx20\x5c\x5c\
t\x5c\x5cr\x5c\x5cn\x5c\x5cf]*[>+~\
]|:(even|odd|eq|\
gt|lt|nth|first|\
last)(?:\x5c\x5c([\x5c\x5cx2\
0\x5c\x5ct\x5c\x5cr\x5c\x5cn\x5c\x5cf]*(\
(?:-\x5c\x5cd)?\x5c\x5cd*)[\x5c\
\x5cx20\x5c\x5ct\x5c\x5cr\x5c\x5cn\x5c\x5cf\
]*\x5c\x5c)|)(?=[^-]|$\
)\x22,\x0a\x22i\x22)},rd=/^(\
?:input|select|t\
extarea|button)$\
/i,sd=/^h\x5cd$/i,l\
b=/^[^{]+\x5c{\x5cs*\x5c[\
native \x5cw/,gd=/^\
(?:#([\x5cw-]+)|(\x5cw\
+)|\x5c.([\x5cw-]+))$/\
,Qb=/[+~]/,hd=/'\
|\x5c\x5c/g,Ha=RegExp(\
\x22\x5c\x5c\x5c\x5c([\x5c\x5cda-f]{1\
,6}[\x5c\x5cx20\x5c\x5ct\x5c\x5cr\x5c\
\x5cn\x5c\x5cf]?|([\x5c\x5cx20\x5c\
\x5ct\x5c\x5cr\x5c\x5cn\x5c\x5cf])|.)\
\x22,\x22ig\x22),Ia=funct\
ion(f,a,p){f=\x220x\
\x22+a-65536;return\
 f!==f||p?a:0>f?\
String.fromCharC\
ode(f+65536):Str\
ing.fromCharCode\
(f>>10|55296,f&1\
023|56320)};try{\
Ga.apply(N=tc.ca\
ll(W.childNodes)\
,W.childNodes),N\
[W.childNodes.le\
ngth].nodeType}c\
atch(Zd){Ga={app\
ly:N.length?func\
tion(f,a){nd.app\
ly(f,tc.call(a))\
}:\x0afunction(f,a)\
{for(var p=f.len\
gth,b=0;f[p++]=a\
[b++];);f.length\
=p-1}}}I=E.suppo\
rt={};rc=E.isXML\
=function(f){ret\
urn(f=f&&(f.owne\
rDocument||f).do\
cumentElement)?\x22\
HTML\x22!==f.nodeNa\
me:!1};na=E.setD\
ocument=function\
(f){var a=f?f.ow\
nerDocument||f:W\
;f=a.defaultView\
;if(a===R||9!==a\
.nodeType||!a.do\
cumentElement)re\
turn R;R=a;ia=a.\
documentElement;\
X=!rc(a);f&&f!==\
f.top&&(f.addEve\
ntListener?f.add\
EventListener(\x22u\
nload\x22,function(\
){na()},!1):f.at\
tachEvent&&f.att\
achEvent(\x22onunlo\
ad\x22,function(){n\
a()}));I.attribu\
tes=pa(function(\
f){f.className=\x0a\
\x22i\x22;return!f.get\
Attribute(\x22class\
Name\x22)});I.getEl\
ementsByTagName=\
pa(function(f){f\
.appendChild(a.c\
reateComment(\x22\x22)\
);return!f.getEl\
ementsByTagName(\
\x22*\x22).length});I.\
getElementsByCla\
ssName=lb.test(a\
.getElementsByCl\
assName)&&pa(fun\
ction(f){f.inner\
HTML=\x22<div class\
='a'></div><div \
class='a i'></di\
v>\x22;f.firstChild\
.className=\x22i\x22;r\
eturn 2===f.getE\
lementsByClassNa\
me(\x22i\x22).length})\
;I.getById=pa(fu\
nction(f){ia.app\
endChild(f).id=M\
;return!a.getEle\
mentsByName||!a.\
getElementsByNam\
e(M).length});I.\
getById?(H.find.\
ID=function(f,\x0aa\
){if(typeof a.ge\
tElementById!==T\
&&X){var b=a.get\
ElementById(f);r\
eturn b&&b.paren\
tNode?[b]:[]}},H\
.filter.ID=funct\
ion(f){var a=f.r\
eplace(Ha,Ia);re\
turn function(f)\
{return f.getAtt\
ribute(\x22id\x22)===a\
}}):(delete H.fi\
nd.ID,H.filter.I\
D=function(f){va\
r a=f.replace(Ha\
,Ia);return func\
tion(f){return(f\
=typeof f.getAtt\
ributeNode!==T&&\
f.getAttributeNo\
de(\x22id\x22))&&f.val\
ue===a}});H.find\
.TAG=I.getElemen\
tsByTagName?func\
tion(f,a){if(typ\
eof a.getElement\
sByTagName!==T)r\
eturn a.getEleme\
ntsByTagName(f)}\
:function(f,a){v\
ar b,\x0aw=[],g=0,j\
=a.getElementsBy\
TagName(f);if(\x22*\
\x22===f){for(;b=j[\
g++];)1===b.node\
Type&&w.push(b);\
return w}return \
j};H.find.CLASS=\
I.getElementsByC\
lassName&&functi\
on(f,a){if(typeo\
f a.getElementsB\
yClassName!==T&&\
X)return a.getEl\
ementsByClassNam\
e(f)};ca=[];S=[]\
;if(I.qsa=lb.tes\
t(a.querySelecto\
rAll))pa(functio\
n(f){f.innerHTML\
=\x22<select t=''><\
option selected=\
''></option></se\
lect>\x22;f.querySe\
lectorAll(\x22[t^='\
']\x22).length&&S.p\
ush(\x22[*^$]=[\x5c\x5cx2\
0\x5c\x5ct\x5c\x5cr\x5c\x5cn\x5c\x5cf]*(\
?:''|\x5c\x22\x5c\x22)\x22);f.q\
uerySelectorAll(\
\x22[selected]\x22).le\
ngth||S.push(\x22\x5c\x5c\
[[\x5c\x5cx20\x5c\x5ct\x5c\x5cr\x5c\x5cn\
\x5c\x5cf]*(?:value|ch\
ecked|selected|a\
sync|autofocus|a\
utoplay|controls\
|defer|disabled|\
hidden|ismap|loo\
p|multiple|open|\
readonly|require\
d|scoped)\x22);\x0af.q\
uerySelectorAll(\
\x22:checked\x22).leng\
th||S.push(\x22:che\
cked\x22)}),pa(func\
tion(f){var b=a.\
createElement(\x22i\
nput\x22);b.setAttr\
ibute(\x22type\x22,\x22hi\
dden\x22);f.appendC\
hild(b).setAttri\
bute(\x22name\x22,\x22D\x22)\
;f.querySelector\
All(\x22[name=d]\x22).\
length&&S.push(\x22\
name[\x5c\x5cx20\x5c\x5ct\x5c\x5cr\
\x5c\x5cn\x5c\x5cf]*[*^$|!~]\
?=\x22);f.querySele\
ctorAll(\x22:enable\
d\x22).length||S.pu\
sh(\x22:enabled\x22,\x22:\
disabled\x22);f.que\
rySelectorAll(\x22*\
,:x\x22);S.push(\x22,.\
*:\x22)});(I.matche\
sSelector=lb.tes\
t(La=ia.webkitMa\
tchesSelector||i\
a.mozMatchesSele\
ctor||ia.oMatche\
sSelector||ia.ms\
MatchesSelector)\
)&&\x0apa(function(\
f){I.disconnecte\
dMatch=La.call(f\
,\x22div\x22);La.call(\
f,\x22[s!='']:x\x22);c\
a.push(\x22!=\x22,Xb)}\
);S=S.length&&Re\
gExp(S.join(\x22|\x22)\
);ca=ca.length&&\
RegExp(ca.join(\x22\
|\x22));ra=(f=lb.te\
st(ia.compareDoc\
umentPosition))|\
|lb.test(ia.cont\
ains)?function(f\
,a){var b=9===f.\
nodeType?f.docum\
entElement:f,w=a\
&&a.parentNode;r\
eturn f===w||!(!\
w||!(1===w.nodeT\
ype&&(b.contains\
?b.contains(w):f\
.compareDocument\
Position&&f.comp\
areDocumentPosit\
ion(w)&16)))}:fu\
nction(f,a){if(a\
)for(;a=a.parent\
Node;)if(a===f)r\
eturn!0;return!1\
};B=f?function(f\
,\x0ab){if(f===b)re\
turn Ca=!0,0;var\
 g=!f.compareDoc\
umentPosition-!b\
.compareDocument\
Position;if(g)re\
turn g;g=(f.owne\
rDocument||f)===\
(b.ownerDocument\
||b)?f.compareDo\
cumentPosition(b\
):1;return g&1||\
!I.sortDetached&\
&b.compareDocume\
ntPosition(f)===\
g?f===a||f.owner\
Document===W&&ra\
(W,f)?-1:b===a||\
b.ownerDocument=\
==W&&ra(W,b)?1:q\
a?Ua.call(qa,f)-\
Ua.call(qa,b):0:\
g&4?-1:1}:functi\
on(f,b){if(f===b\
)return Ca=!0,0;\
var g,j=0;g=f.pa\
rentNode;var c=b\
.parentNode,d=[f\
],n=[b];if(!g||!\
c)return f===a?-\
1:b===a?1:g?-1:c\
?1:qa?Ua.call(qa\
,\x0af)-Ua.call(qa,\
b):0;if(g===c)re\
turn pc(f,b);for\
(g=f;g=g.parentN\
ode;)d.unshift(g\
);for(g=b;g=g.pa\
rentNode;)n.unsh\
ift(g);for(;d[j]\
===n[j];)j++;ret\
urn j?pc(d[j],n[\
j]):d[j]===W?-1:\
n[j]===W?1:0};re\
turn a};E.matche\
s=function(f,a){\
return E(f,null,\
null,a)};E.match\
esSelector=funct\
ion(f,a){(f.owne\
rDocument||f)!==\
R&&na(f);a=a.rep\
lace(od,\x22='$1']\x22\
);if(I.matchesSe\
lector&&X&&(!ca|\
|!ca.test(a))&&(\
!S||!S.test(a)))\
try{var b=La.cal\
l(f,a);if(b||I.d\
isconnectedMatch\
||f.document&&11\
!==f.document.no\
deType)return b}\
catch(g){}return\
 0<\x0aE(a,R,null,[\
f]).length};E.co\
ntains=function(\
f,a){(f.ownerDoc\
ument||f)!==R&&n\
a(f);return ra(f\
,a)};E.attr=func\
tion(f,a){(f.own\
erDocument||f)!=\
=R&&na(f);var b=\
H.attrHandle[a.t\
oLowerCase()],b=\
b&&da.call(H.att\
rHandle,a.toLowe\
rCase())?b(f,a,!\
X):void 0;return\
 void 0!==b?b:I.\
attributes||!X?f\
.getAttribute(a)\
:(b=f.getAttribu\
teNode(a))&&b.sp\
ecified?b.value:\
null};E.error=fu\
nction(f){throw \
Error(\x22Syntax er\
ror, unrecognize\
d expression: \x22+\
f);};E.uniqueSor\
t=function(f){va\
r a,b=[],g=0,j=0\
;Ca=!I.detectDup\
licates;qa=\x0a!I.s\
ortStable&&f.sli\
ce(0);f.sort(B);\
if(Ca){for(;a=f[\
j++];)a===f[j]&&\
(g=b.push(j));fo\
r(;g--;)f.splice\
(b[g],1)}qa=null\
;return f};Ka=E.\
getText=function\
(f){var a,b=\x22\x22,g\
=0;if(a=f.nodeTy\
pe)if(1===a||9==\
=a||11===a){if(\x22\
string\x22===typeof\
 f.textContent)r\
eturn f.textCont\
ent;for(f=f.firs\
tChild;f;f=f.nex\
tSibling)b+=Ka(f\
)}else{if(3===a|\
|4===a)return f.\
nodeValue}else f\
or(;a=f[g++];)b+\
=Ka(a);return b}\
;H=E.selectors={\
cacheLength:50,c\
reatePseudo:oa,m\
atch:xb,attrHand\
le:{},find:{},re\
lative:{\x22>\x22:{dir\
:\x22parentNode\x22,fi\
rst:!0},\x0a\x22 \x22:{di\
r:\x22parentNode\x22},\
\x22+\x22:{dir:\x22previo\
usSibling\x22,first\
:!0},\x22~\x22:{dir:\x22p\
reviousSibling\x22}\
},preFilter:{ATT\
R:function(f){f[\
1]=f[1].replace(\
Ha,Ia);f[3]=(f[4\
]||f[5]||\x22\x22).rep\
lace(Ha,Ia);\x22~=\x22\
===f[2]&&(f[3]=\x22\
 \x22+f[3]+\x22 \x22);ret\
urn f.slice(0,4)\
},CHILD:function\
(f){f[1]=f[1].to\
LowerCase();\x22nth\
\x22===f[1].slice(0\
,3)?(f[3]||E.err\
or(f[0]),f[4]=+(\
f[4]?f[5]+(f[6]|\
|1):2*(\x22even\x22===\
f[3]||\x22odd\x22===f[\
3])),f[5]=+(f[7]\
+f[8]||\x22odd\x22===f\
[3])):f[3]&&E.er\
ror(f[0]);return\
 f},PSEUDO:funct\
ion(f){var a,b=!\
f[5]&&f[2];if(xb\
.CHILD.test(f[0]\
))return null;\x0ai\
f(f[3]&&void 0!=\
=f[4])f[2]=f[4];\
else if(b&&pd.te\
st(b)&&(a=sa(b,!\
0))&&(a=b.indexO\
f(\x22)\x22,b.length-a\
)-b.length))f[0]\
=f[0].slice(0,a)\
,f[2]=b.slice(0,\
a);return f.slic\
e(0,3)}},filter:\
{TAG:function(f)\
{var a=f.replace\
(Ha,Ia).toLowerC\
ase();return\x22*\x22=\
==f?function(){r\
eturn!0}:functio\
n(f){return f.no\
deName&&f.nodeNa\
me.toLowerCase()\
===a}},CLASS:fun\
ction(f){var a=s\
c[f+\x22 \x22];return \
a||(a=RegExp(\x22(^\
|[\x5c\x5cx20\x5c\x5ct\x5c\x5cr\x5c\x5cn\
\x5c\x5cf])\x22+f+\x22([\x5c\x5cx2\
0\x5c\x5ct\x5c\x5cr\x5c\x5cn\x5c\x5cf]|$\
)\x22))&&sc(f,funct\
ion(f){return a.\
test(\x22string\x22===\
typeof f.classNa\
me&&\x0af.className\
||typeof f.getAt\
tribute!==T&&f.g\
etAttribute(\x22cla\
ss\x22)||\x22\x22)})},ATT\
R:function(f,a,b\
){return functio\
n(g){g=E.attr(g,\
f);if(null==g)re\
turn\x22!=\x22===a;if(\
!a)return!0;g+=\x22\
\x22;return\x22=\x22===a?\
g===b:\x22!=\x22===a?g\
!==b:\x22^=\x22===a?b&\
&0===g.indexOf(b\
):\x22*=\x22===a?b&&-1\
<g.indexOf(b):\x22$\
=\x22===a?b&&g.slic\
e(-b.length)===b\
:\x22~=\x22===a?-1<(\x22 \
\x22+g+\x22 \x22).indexOf\
(b):\x22|=\x22===a?g==\
=b||g.slice(0,b.\
length+1)===b+\x22-\
\x22:!1}},CHILD:fun\
ction(f,a,b,g,j)\
{var c=\x22nth\x22!==f\
.slice(0,3),d=\x22l\
ast\x22!==f.slice(-\
4),n=\x22of-type\x22==\
=a;return 1===g&\
&0===j?function(\
f){return!!f.par\
entNode}:\x0afuncti\
on(a,b,p){var w,\
e,r,k,t;b=c!==d?\
\x22nextSibling\x22:\x22p\
reviousSibling\x22;\
var l=a.parentNo\
de,h=n&&a.nodeNa\
me.toLowerCase()\
;p=!p&&!n;if(l){\
if(c){for(;b;){f\
or(e=a;e=e[b];)i\
f(n?e.nodeName.t\
oLowerCase()===h\
:1===e.nodeType)\
return!1;t=b=\x22on\
ly\x22===f&&!t&&\x22ne\
xtSibling\x22}retur\
n!0}t=[d?l.first\
Child:l.lastChil\
d];if(d&&p){p=l[\
M]||(l[M]={});w=\
p[f]||[];k=w[0]=\
==ba&&w[1];r=w[0\
]===ba&&w[2];for\
(e=k&&l.childNod\
es[k];e=++k&&e&&\
e[b]||(r=k=0)||t\
.pop();)if(1===e\
.nodeType&&++r&&\
e===a){p[f]=[ba,\
k,r];break}}else\
 if(p&&(w=(a[M]|\
|\x0a(a[M]={}))[f])\
&&w[0]===ba)r=w[\
1];else for(;e=+\
+k&&e&&e[b]||(r=\
k=0)||t.pop();)i\
f((n?e.nodeName.\
toLowerCase()===\
h:1===e.nodeType\
)&&++r)if(p&&((e\
[M]||(e[M]={}))[\
f]=[ba,r]),e===a\
)break;r-=j;retu\
rn r===g||0===r%\
g&&0<=r/g}}},PSE\
UDO:function(f,a\
){var b,g=H.pseu\
dos[f]||H.setFil\
ters[f.toLowerCa\
se()]||E.error(\x22\
unsupported pseu\
do: \x22+f);return \
g[M]?g(a):1<g.le\
ngth?(b=[f,f,\x22\x22,\
a],H.setFilters.\
hasOwnProperty(f\
.toLowerCase())?\
oa(function(f,b)\
{for(var p,j=g(f\
,a),c=j.length;c\
--;)p=Ua.call(f,\
j[c]),f[p]=!(b[p\
]=j[c])}):\x0afunct\
ion(f){return g(\
f,0,b)}):g}},pse\
udos:{not:oa(fun\
ction(f){var a=[\
],b=[],g=$a(f.re\
place(wb,\x22$1\x22));\
return g[M]?oa(f\
unction(f,a,b,p)\
{p=g(f,null,p,[]\
);for(var w=f.le\
ngth;w--;)if(b=p\
[w])f[w]=!(a[w]=\
b)}):function(f,\
j,c){a[0]=f;g(a,\
null,c,b);return\
!b.pop()}}),has:\
oa(function(f){r\
eturn function(a\
){return 0<E(f,a\
).length}}),cont\
ains:oa(function\
(f){return funct\
ion(a){return-1<\
(a.textContent||\
a.innerText||Ka(\
a)).indexOf(f)}}\
),lang:oa(functi\
on(f){qd.test(f|\
|\x22\x22)||E.error(\x22u\
nsupported lang:\
 \x22+f);f=f.replac\
e(Ha,\x0aIa).toLowe\
rCase();return f\
unction(a){var b\
;do if(b=X?a.lan\
g:a.getAttribute\
(\x22xml:lang\x22)||a.\
getAttribute(\x22la\
ng\x22))return b=b.\
toLowerCase(),b=\
==f||0===b.index\
Of(f+\x22-\x22);while(\
(a=a.parentNode)\
&&1===a.nodeType\
);return!1}}),ta\
rget:function(f)\
{var a=Pb.locati\
on&&Pb.location.\
hash;return a&&a\
.slice(1)===f.id\
},root:function(\
f){return f===ia\
},focus:function\
(f){return f===R\
.activeElement&&\
(!R.hasFocus||R.\
hasFocus())&&!(!\
f.type&&!f.href&\
&!~f.tabIndex)},\
enabled:function\
(f){return!1===f\
.disabled},disab\
led:function(f){\
return!0===\x0af.di\
sabled},checked:\
function(f){var \
a=f.nodeName.toL\
owerCase();retur\
n\x22input\x22===a&&!!\
f.checked||\x22opti\
on\x22===a&&!!f.sel\
ected},selected:\
function(f){f.pa\
rentNode&&f.pare\
ntNode.selectedI\
ndex;return!0===\
f.selected},empt\
y:function(f){fo\
r(f=f.firstChild\
;f;f=f.nextSibli\
ng)if(6>f.nodeTy\
pe)return!1;retu\
rn!0},parent:fun\
ction(f){return!\
H.pseudos.empty(\
f)},header:funct\
ion(f){return sd\
.test(f.nodeName\
)},input:functio\
n(f){return rd.t\
est(f.nodeName)}\
,button:function\
(f){var a=f.node\
Name.toLowerCase\
();return\x22input\x22\
===\x0aa&&\x22button\x22=\
==f.type||\x22butto\
n\x22===a},text:fun\
ction(f){var a;r\
eturn\x22input\x22===f\
.nodeName.toLowe\
rCase()&&\x22text\x22=\
==f.type&&(null=\
=(a=f.getAttribu\
te(\x22type\x22))||\x22te\
xt\x22===a.toLowerC\
ase())},first:ta\
(function(){retu\
rn[0]}),last:ta(\
function(f,a){re\
turn[a-1]}),eq:t\
a(function(f,a,b\
){return[0>b?b+a\
:b]}),even:ta(fu\
nction(f,a){for(\
var b=0;b<a;b+=2\
)f.push(b);retur\
n f}),odd:ta(fun\
ction(f,a){for(v\
ar b=1;b<a;b+=2)\
f.push(b);return\
 f}),lt:ta(funct\
ion(f,a,b){for(a\
=0>b?b+a:b;0<=--\
a;)f.push(a);ret\
urn f}),gt:ta(fu\
nction(f,\x0aa,b){f\
or(b=0>b?b+a:b;+\
+b<a;)f.push(b);\
return f})}};H.p\
seudos.nth=H.pse\
udos.eq;for(Ba i\
n{radio:!0,check\
box:!0,file:!0,p\
assword:!0,image\
:!0})H.pseudos[B\
a]=id(Ba);for(Ba\
 in{submit:!0,re\
set:!0})H.pseudo\
s[Ba]=jd(Ba);qc.\
prototype=H.filt\
ers=H.pseudos;H.\
setFilters=new q\
c;$a=E.compile=f\
unction(f,a){var\
 b,g=[],j=[],c=D\
a[f+\x22 \x22];if(!c){\
a||(a=sa(f));for\
(b=a.length;b--;\
)c=Wb(a[b]),c[M]\
?g.push(c):j.pus\
h(c);var d=0<g.l\
ength,n=0<j.leng\
th;b=function(f,\
a,b,p,w){var c,e\
,r,k=0,ea=\x220\x22,t=\
f&&[],l=[],h=Aa,\
B=f||n&&H.find.T\
AG(\x22*\x22,\x0aw),z=ba+\
=null==h?1:Math.\
random()||0.1,T=\
B.length;for(w&&\
(Aa=a!==R&&a);ea\
!==T&&null!=(c=B\
[ea]);ea++){if(n\
&&c){for(e=0;r=j\
[e++];)if(r(c,a,\
b)){p.push(c);br\
eak}w&&(ba=z)}d&\
&((c=!r&&c)&&k--\
,f&&t.push(c))}k\
+=ea;if(d&&ea!==\
k){for(e=0;r=g[e\
++];)r(t,l,a,b);\
if(f){if(0<k)for\
(;ea--;)!t[ea]&&\
!l[ea]&&(l[ea]=u\
a.call(p));l=Ta(\
l)}Ga.apply(p,l)\
;w&&(!f&&0<l.len\
gth&&1<k+g.lengt\
h)&&E.uniqueSort\
(p)}w&&(ba=z,Aa=\
h);return t};b=d\
?oa(b):b;c=Da(f,\
b)}return c};I.s\
ortStable=M.spli\
t(\x22\x22).sort(B).jo\
in(\x22\x22)===M;I.det\
ectDuplicates=\x0a!\
!Ca;na();I.sortD\
etached=pa(funct\
ion(f){return f.\
compareDocumentP\
osition(R.create\
Element(\x22div\x22))&\
1});pa(function(\
f){f.innerHTML=\x22\
<a href='#'></a>\
\x22;return\x22#\x22===f.\
firstChild.getAt\
tribute(\x22href\x22)}\
)||Sb(\x22type|href\
|height|width\x22,f\
unction(f,a,b){i\
f(!b)return f.ge\
tAttribute(a,\x22ty\
pe\x22===a.toLowerC\
ase()?1:2)});(!I\
.attributes||!pa\
(function(f){f.i\
nnerHTML=\x22<input\
/>\x22;f.firstChild\
.setAttribute(\x22v\
alue\x22,\x22\x22);return\
\x22\x22===f.firstChil\
d.getAttribute(\x22\
value\x22)}))&&Sb(\x22\
value\x22,function(\
f,a,b){if(!b&&\x22i\
nput\x22===f.nodeNa\
me.toLowerCase()\
)return f.defaul\
tValue});\x0apa(fun\
ction(f){return \
null==f.getAttri\
bute(\x22disabled\x22)\
})||Sb(\x22checked|\
selected|async|a\
utofocus|autopla\
y|controls|defer\
|disabled|hidden\
|ismap|loop|mult\
iple|open|readon\
ly|required|scop\
ed\x22,function(f,a\
,b){var g;if(!b)\
return!0===f[a]?\
a.toLowerCase():\
(g=f.getAttribut\
eNode(a))&&g.spe\
cified?g.value:n\
ull});g.find=E;g\
.expr=E.selector\
s;g.expr[\x22:\x22]=g.\
expr.pseudos;g.u\
nique=E.uniqueSo\
rt;g.text=E.getT\
ext;g.isXMLDoc=E\
.isXML;g.contain\
s=E.contains;var\
 wc=g.expr.match\
.needsContext,xc\
=/^<(\x5cw+)\x5cs*\x5c/?>\
(?:<\x5c/\x5c1>|)$/,Vc\
=\x0a/^.[^:#\x5c[\x5c.,]*\
$/;g.filter=func\
tion(f,a,b){var \
j=a[0];b&&(f=\x22:n\
ot(\x22+f+\x22)\x22);retu\
rn 1===a.length&\
&1===j.nodeType?\
g.find.matchesSe\
lector(j,f)?[j]:\
[]:g.find.matche\
s(f,g.grep(a,fun\
ction(f){return \
1===f.nodeType})\
)};g.fn.extend({\
find:function(f)\
{var a,b=[],j=th\
is,c=j.length;if\
(\x22string\x22!==type\
of f)return this\
.pushStack(g(f).\
filter(function(\
){for(a=0;a<c;a+\
+)if(g.contains(\
j[a],this))retur\
n!0}));for(a=0;a\
<c;a++)g.find(f,\
j[a],b);b=this.p\
ushStack(1<c?g.u\
nique(b):b);b.se\
lector=this.sele\
ctor?this.select\
or+\x22 \x22+\x0af:f;retu\
rn b},filter:fun\
ction(f){return \
this.pushStack(h\
(this,f||[],!1))\
},not:function(f\
){return this.pu\
shStack(h(this,f\
||[],!0))},is:fu\
nction(f){return\
!!h(this,\x22string\
\x22===typeof f&&wc\
.test(f)?g(f):f|\
|[],!1).length}}\
);var mb,y=a.doc\
ument,td=/^(?:\x5cs\
*(<[\x5cw\x5cW]+>)[^>]\
*|#([\x5cw-]*))$/;(\
g.fn.init=functi\
on(f,a){var b,j;\
if(!f)return thi\
s;if(\x22string\x22===\
typeof f){if((b=\
\x22<\x22===f.charAt(0\
)&&\x22>\x22===f.charA\
t(f.length-1)&&3\
<=f.length?[null\
,f,null]:td.exec\
(f))&&(b[1]||!a)\
){if(b[1]){if(a=\
a instanceof g?a\
[0]:a,g.merge(th\
is,\x0ag.parseHTML(\
b[1],a&&a.nodeTy\
pe?a.ownerDocume\
nt||a:y,!0)),xc.\
test(b[1])&&g.is\
PlainObject(a))f\
or(b in a)if(g.i\
sFunction(this[b\
]))this[b](a[b])\
;else this.attr(\
b,a[b])}else{if(\
(j=y.getElementB\
yId(b[2]))&&j.pa\
rentNode){if(j.i\
d!==b[2])return \
mb.find(f);this.\
length=1;this[0]\
=j}this.context=\
y;this.selector=\
f}return this}re\
turn!a||a.jquery\
?(a||mb).find(f)\
:this.constructo\
r(a).find(f)}if(\
f.nodeType)retur\
n this.context=t\
his[0]=f,this.le\
ngth=1,this;if(g\
.isFunction(f))r\
eturn\x22undefined\x22\
!==typeof mb.rea\
dy?mb.ready(f):\x0a\
f(g);void 0!==f.\
selector&&(this.\
selector=f.selec\
tor,this.context\
=f.context);retu\
rn g.makeArray(f\
,this)}).prototy\
pe=g.fn;mb=g(y);\
var ud=/^(?:pare\
nts|prev(?:Until\
|All))/,vd={chil\
dren:!0,contents\
:!0,next:!0,prev\
:!0};g.extend({d\
ir:function(f,a,\
b){var j=[];for(\
f=f[a];f&&9!==f.\
nodeType&&(void \
0===b||1!==f.nod\
eType||!g(f).is(\
b));)1===f.nodeT\
ype&&j.push(f),f\
=f[a];return j},\
sibling:function\
(f,a){for(var b=\
[];f;f=f.nextSib\
ling)1===f.nodeT\
ype&&f!==a&&b.pu\
sh(f);return b}}\
);g.fn.extend({h\
as:function(f){v\
ar a,\x0ab=g(f,this\
),j=b.length;ret\
urn this.filter(\
function(){for(a\
=0;a<j;a++)if(g.\
contains(this,b[\
a]))return!0})},\
closest:function\
(f,a){for(var b,\
j=0,c=this.lengt\
h,d=[],n=wc.test\
(f)||\x22string\x22!==\
typeof f?g(f,a||\
this.context):0;\
j<c;j++)for(b=th\
is[j];b&&b!==a;b\
=b.parentNode)if\
(11>b.nodeType&&\
(n?-1<n.index(b)\
:1===b.nodeType&\
&g.find.matchesS\
elector(b,f))){d\
.push(b);break}r\
eturn this.pushS\
tack(1<d.length?\
g.unique(d):d)},\
index:function(f\
){return!f?this[\
0]&&this[0].pare\
ntNode?this.firs\
t().prevAll().le\
ngth:-1:\x22string\x22\
===\x0atypeof f?g.i\
nArray(this[0],g\
(f)):g.inArray(f\
.jquery?f[0]:f,t\
his)},add:functi\
on(f,a){return t\
his.pushStack(g.\
unique(g.merge(t\
his.get(),g(f,a)\
)))},addBack:fun\
ction(f){return \
this.add(null==f\
?this.prevObject\
:this.prevObject\
.filter(f))}});g\
.each({parent:fu\
nction(f){return\
(f=f.parentNode)\
&&11!==f.nodeTyp\
e?f:null},parent\
s:function(f){re\
turn g.dir(f,\x22pa\
rentNode\x22)},pare\
ntsUntil:functio\
n(f,a,b){return \
g.dir(f,\x22parentN\
ode\x22,b)},next:fu\
nction(f){return\
 e(f,\x22nextSiblin\
g\x22)},prev:functi\
on(f){return e(f\
,\x22previousSiblin\
g\x22)},\x0anextAll:fu\
nction(f){return\
 g.dir(f,\x22nextSi\
bling\x22)},prevAll\
:function(f){ret\
urn g.dir(f,\x22pre\
viousSibling\x22)},\
nextUntil:functi\
on(f,a,b){return\
 g.dir(f,\x22nextSi\
bling\x22,b)},prevU\
ntil:function(f,\
a,b){return g.di\
r(f,\x22previousSib\
ling\x22,b)},siblin\
gs:function(f){r\
eturn g.sibling(\
(f.parentNode||{\
}).firstChild,f)\
},children:funct\
ion(f){return g.\
sibling(f.firstC\
hild)},contents:\
function(f){retu\
rn g.nodeName(f,\
\x22iframe\x22)?f.cont\
entDocument||f.c\
ontentWindow.doc\
ument:g.merge([]\
,f.childNodes)}}\
,function(f,a){g\
.fn[f]=function(\
b,\x0aj){var c=g.ma\
p(this,a,b);\x22Unt\
il\x22!==f.slice(-5\
)&&(j=b);j&&\x22str\
ing\x22===typeof j&\
&(c=g.filter(j,c\
));1<this.length\
&&(vd[f]||(c=g.u\
nique(c)),ud.tes\
t(f)&&(c=c.rever\
se()));return th\
is.pushStack(c)}\
});var xa=/\x5cS+/g\
,yc={};g.Callbac\
ks=function(f){v\
ar a;if(\x22string\x22\
===typeof f){if(\
!(a=yc[f])){a=f;\
var b=yc[a]={};g\
.each(a.match(xa\
)||[],function(f\
,a){b[a]=!0});a=\
b}}else a=g.exte\
nd({},f);f=a;var\
 j,c,d,n,e,r,k=[\
],l=!f.once&&[],\
t=function(a){c=\
f.memory&&a;d=!0\
;e=r||0;r=0;n=k.\
length;for(j=!0;\
k&&e<n;e++)if(!1\
===k[e].apply(a[\
0],\x0aa[1])&&f.sto\
pOnFalse){c=!1;b\
reak}j=!1;k&&(l?\
l.length&&t(l.sh\
ift()):c?k=[]:h.\
disable())},h={a\
dd:function(){if\
(k){var a=k.leng\
th;(function $c(\
a){g.each(a,func\
tion(a,b){var p=\
g.type(b);\x22funct\
ion\x22===p?(!f.uni\
que||!h.has(b))&\
&k.push(b):b&&(b\
.length&&\x22string\
\x22!==p)&&$c(b)})}\
)(arguments);j?n\
=k.length:c&&(r=\
a,t(c))}return t\
his},remove:func\
tion(){k&&g.each\
(arguments,funct\
ion(f,a){for(var\
 b;-1<(b=g.inArr\
ay(a,k,b));)k.sp\
lice(b,1),j&&(b<\
=n&&n--,b<=e&&e-\
-)});return this\
},has:function(f\
){return f?-1<g.\
inArray(f,\x0ak):!(\
!k||!k.length)},\
empty:function()\
{k=[];n=0;return\
 this},disable:f\
unction(){k=l=c=\
void 0;return th\
is},disabled:fun\
ction(){return!k\
},lock:function(\
){l=void 0;c||h.\
disable();return\
 this},locked:fu\
nction(){return!\
l},fireWith:func\
tion(f,a){if(k&&\
(!d||l))a=a||[],\
a=[f,a.slice?a.s\
lice():a],j?l.pu\
sh(a):t(a);retur\
n this},fire:fun\
ction(){h.fireWi\
th(this,argument\
s);return this},\
fired:function()\
{return!!d}};ret\
urn h};g.extend(\
{Deferred:functi\
on(f){var a=[[\x22r\
esolve\x22,\x22done\x22,g\
.Callbacks(\x22once\
 memory\x22),\x22resol\
ved\x22],\x0a[\x22reject\x22\
,\x22fail\x22,g.Callba\
cks(\x22once memory\
\x22),\x22rejected\x22],[\
\x22notify\x22,\x22progre\
ss\x22,g.Callbacks(\
\x22memory\x22)]],b=\x22p\
ending\x22,j={state\
:function(){retu\
rn b},always:fun\
ction(){c.done(a\
rguments).fail(a\
rguments);return\
 this},then:func\
tion(){var f=arg\
uments;return g.\
Deferred(functio\
n(b){g.each(a,fu\
nction(a,p){var \
w=g.isFunction(f\
[a])&&f[a];c[p[1\
]](function(){va\
r f=w&&w.apply(t\
his,arguments);i\
f(f&&g.isFunctio\
n(f.promise))f.p\
romise().done(b.\
resolve).fail(b.\
reject).progress\
(b.notify);else \
b[p[0]+\x22With\x22](t\
his===j?b.promis\
e():\x0athis,w?[f]:\
arguments)})});f\
=null}).promise(\
)},promise:funct\
ion(f){return nu\
ll!=f?g.extend(f\
,j):j}},c={};j.p\
ipe=j.then;g.eac\
h(a,function(f,g\
){var d=g[2],n=g\
[3];j[g[1]]=d.ad\
d;n&&d.add(funct\
ion(){b=n},a[f^1\
][2].disable,a[2\
][2].lock);c[g[0\
]]=function(){c[\
g[0]+\x22With\x22](thi\
s===c?j:this,arg\
uments);return t\
his};c[g[0]+\x22Wit\
h\x22]=d.fireWith})\
;j.promise(c);f&\
&f.call(c,c);ret\
urn c},when:func\
tion(f){var a=0,\
b=n.call(argumen\
ts),j=b.length,c\
=1!==j||f&&g.isF\
unction(f.promis\
e)?j:0,d=1===c?f\
:g.Deferred(),e=\
function(f,\x0aa,b)\
{return function\
(g){a[f]=this;b[\
f]=1<arguments.l\
ength?n.call(arg\
uments):g;b===r?\
d.notifyWith(a,b\
):--c||d.resolve\
With(a,b)}},r,k,\
l;if(1<j){r=Arra\
y(j);k=Array(j);\
for(l=Array(j);a\
<j;a++)b[a]&&g.i\
sFunction(b[a].p\
romise)?b[a].pro\
mise().done(e(a,\
l,b)).fail(d.rej\
ect).progress(e(\
a,k,r)):--c}c||d\
.resolveWith(l,b\
);return d.promi\
se()}});var yb;g\
.fn.ready=functi\
on(f){g.ready.pr\
omise().done(f);\
return this};g.e\
xtend({isReady:!\
1,readyWait:1,ho\
ldReady:function\
(f){f?g.readyWai\
t++:g.ready(!0)}\
,ready:function(\
f){if(!(!0===\x0af?\
--g.readyWait:g.\
isReady)){if(!y.\
body)return setT\
imeout(g.ready);\
g.isReady=!0;!0!\
==f&&0<--g.ready\
Wait||(yb.resolv\
eWith(y,[g]),g.f\
n.trigger&&g(y).\
trigger(\x22ready\x22)\
.off(\x22ready\x22))}}\
});g.ready.promi\
se=function(f){i\
f(!yb)if(yb=g.De\
ferred(),\x22comple\
te\x22===y.readySta\
te)setTimeout(g.\
ready);else if(y\
.addEventListene\
r)y.addEventList\
ener(\x22DOMContent\
Loaded\x22,q,!1),a.\
addEventListener\
(\x22load\x22,q,!1);el\
se{y.attachEvent\
(\x22onreadystatech\
ange\x22,q);a.attac\
hEvent(\x22onload\x22,\
q);var b=!1;try{\
b=null==a.frameE\
lement&&y.docume\
ntElement}catch(\
j){}b&&\x0ab.doScro\
ll&&function Uc(\
){if(!g.isReady)\
{try{b.doScroll(\
\x22left\x22)}catch(f)\
{return setTimeo\
ut(Uc,50)}l();g.\
ready()}}()}retu\
rn yb.promise(f)\
};var ka=\x22undefi\
ned\x22,zc;for(zc i\
n g(v))break;v.o\
wnLast=\x220\x22!==zc;\
v.inlineBlockNee\
dsLayout=!1;g(fu\
nction(){var f,a\
,b=y.getElements\
ByTagName(\x22body\x22\
)[0];if(b){f=y.c\
reateElement(\x22di\
v\x22);f.style.cssT\
ext=\x22border:0;wi\
dth:0;height:0;p\
osition:absolute\
;top:0;left:-999\
9px;margin-top:1\
px\x22;a=y.createEl\
ement(\x22div\x22);b.a\
ppendChild(f).ap\
pendChild(a);if(\
typeof a.style.z\
oom!==ka&&(a.sty\
le.cssText=\x0a\x22bor\
der:0;margin:0;w\
idth:1px;padding\
:1px;display:inl\
ine;zoom:1\x22,v.in\
lineBlockNeedsLa\
yout=3===a.offse\
tWidth))b.style.\
zoom=1;b.removeC\
hild(f)}});var w\
d=y.createElemen\
t(\x22div\x22);if(null\
==v.deleteExpand\
o){v.deleteExpan\
do=!0;try{delete\
 wd.test}catch($\
d){v.deleteExpan\
do=!1}}g.acceptD\
ata=function(f){\
var a=g.noData[(\
f.nodeName+\x22 \x22).\
toLowerCase()],b\
=+f.nodeType||1;\
return 1!==b&&9!\
==b?!1:!a||!0!==\
a&&f.getAttribut\
e(\x22classid\x22)===a\
};var Xc=/^(?:\x5c{\
[\x5cw\x5cW]*\x5c}|\x5c[[\x5cw\x5c\
W]*\x5c])$/,Wc=/([A\
-Z])/g;g.extend(\
{cache:{},noData\
:{\x22applet \x22:!0,\x0a\
\x22embed \x22:!0,\x22obj\
ect \x22:\x22clsid:D27\
CDB6E-AE6D-11cf-\
96B8-44455354000\
0\x22},hasData:func\
tion(f){f=f.node\
Type?g.cache[f[g\
.expando]]:f[g.e\
xpando];return!!\
f&&!u(f)},data:f\
unction(f,a,g){r\
eturn b(f,a,g)},\
removeData:funct\
ion(f,a){return \
c(f,a)},_data:fu\
nction(f,a,g){re\
turn b(f,a,g,!0)\
},_removeData:fu\
nction(f,a){retu\
rn c(f,a,!0)}});\
g.fn.extend({dat\
a:function(f,a){\
var b,j,c,d=this\
[0],n=d&&d.attri\
butes;if(void 0=\
==f){if(this.len\
gth&&(c=g.data(d\
),1===d.nodeType\
&&!g._data(d,\x22pa\
rsedAttrs\x22))){fo\
r(b=n.length;b--\
;)j=n[b].name,\x0a0\
===j.indexOf(\x22da\
ta-\x22)&&(j=g.came\
lCase(j.slice(5)\
),s(d,j,c[j]));g\
._data(d,\x22parsed\
Attrs\x22,!0)}retur\
n c}return\x22objec\
t\x22===typeof f?th\
is.each(function\
(){g.data(this,f\
)}):1<arguments.\
length?this.each\
(function(){g.da\
ta(this,f,a)}):d\
?s(d,f,g.data(d,\
f)):void 0},remo\
veData:function(\
f){return this.e\
ach(function(){g\
.removeData(this\
,f)})}});g.exten\
d({queue:functio\
n(f,a,b){var j;i\
f(f)return a=(a|\
|\x22fx\x22)+\x22queue\x22,j\
=g._data(f,a),b&\
&(!j||g.isArray(\
b)?j=g._data(f,a\
,g.makeArray(b))\
:j.push(b)),j||[\
]},dequeue:funct\
ion(f,\x0aa){a=a||\x22\
fx\x22;var b=g.queu\
e(f,a),j=b.lengt\
h,c=b.shift(),d=\
g._queueHooks(f,\
a),n=function(){\
g.dequeue(f,a)};\
\x22inprogress\x22===c\
&&(c=b.shift(),j\
--);c&&(\x22fx\x22===a\
&&b.unshift(\x22inp\
rogress\x22),delete\
 d.stop,c.call(f\
,n,d));!j&&d&&d.\
empty.fire()},_q\
ueueHooks:functi\
on(f,a){var b=a+\
\x22queueHooks\x22;ret\
urn g._data(f,b)\
||g._data(f,b,{e\
mpty:g.Callbacks\
(\x22once memory\x22).\
add(function(){g\
._removeData(f,a\
+\x22queue\x22);g._rem\
oveData(f,b)})})\
}});g.fn.extend(\
{queue:function(\
f,a){var b=2;\x22st\
ring\x22!==typeof f\
&&(a=f,f=\x22fx\x22,b-\
-);return argume\
nts.length<\x0ab?g.\
queue(this[0],f)\
:void 0===a?this\
:this.each(funct\
ion(){var b=g.qu\
eue(this,f,a);g.\
_queueHooks(this\
,f);\x22fx\x22===f&&\x22i\
nprogress\x22!==b[0\
]&&g.dequeue(thi\
s,f)})},dequeue:\
function(f){retu\
rn this.each(fun\
ction(){g.dequeu\
e(this,f)})},cle\
arQueue:function\
(f){return this.\
queue(f||\x22fx\x22,[]\
)},promise:funct\
ion(f,a){var b,j\
=1,c=g.Deferred(\
),d=this,n=this.\
length,e=functio\
n(){--j||c.resol\
veWith(d,[d])};\x22\
string\x22!==typeof\
 f&&(a=f,f=void \
0);for(f=f||\x22fx\x22\
;n--;)if((b=g._d\
ata(d[n],f+\x22queu\
eHooks\x22))&&b.emp\
ty)j++,b.empty.a\
dd(e);\x0ae();retur\
n c.promise(a)}}\
);var zb=/[+-]?(\
?:\x5cd*\x5c.|)\x5cd+(?:[\
eE][+-]?\x5cd+|)/.s\
ource,Qa=[\x22Top\x22,\
\x22Right\x22,\x22Bottom\x22\
,\x22Left\x22],hb=func\
tion(f,a){f=a||f\
;return\x22none\x22===\
g.css(f,\x22display\
\x22)||!g.contains(\
f.ownerDocument,\
f)},Va=g.access=\
function(f,a,b,j\
,c,d,n){var e=0,\
r=f.length,k=nul\
l==b;if(\x22object\x22\
===g.type(b))for\
(e in c=!0,b)g.a\
ccess(f,a,e,b[e]\
,!0,d,n);else if\
(void 0!==j&&(c=\
!0,g.isFunction(\
j)||(n=!0),k&&(n\
?(a.call(f,j),a=\
null):(k=a,a=fun\
ction(a,f,b){ret\
urn k.call(g(a),\
b)})),a))for(;e<\
r;e++)a(f[e],b,n\
?j:j.call(f[e],\x0a\
e,a(f[e],b)));re\
turn c?f:k?a.cal\
l(f):r?a(f[0],b)\
:d},Mb=/^(?:chec\
kbox|radio)$/i,Y\
b=y.createDocume\
ntFragment(),Y=y\
.createElement(\x22\
div\x22),nb=y.creat\
eElement(\x22input\x22\
);Y.setAttribute\
(\x22className\x22,\x22t\x22\
);Y.innerHTML=\x22 \
 <link/><table><\
/table><a href='\
/a'>a</a>\x22;v.lea\
dingWhitespace=3\
===Y.firstChild.\
nodeType;v.tbody\
=!Y.getElementsB\
yTagName(\x22tbody\x22\
).length;v.htmlS\
erialize=!!Y.get\
ElementsByTagNam\
e(\x22link\x22).length\
;v.html5Clone=\x22<\
:nav></:nav>\x22!==\
y.createElement(\
\x22nav\x22).cloneNode\
(!0).outerHTML;n\
b.type=\x22checkbox\
\x22;nb.checked=\x0a!0\
;Yb.appendChild(\
nb);v.appendChec\
ked=nb.checked;Y\
.innerHTML=\x22<tex\
tarea>x</textare\
a>\x22;v.noCloneChe\
cked=!!Y.cloneNo\
de(!0).lastChild\
.defaultValue;Yb\
.appendChild(Y);\
Y.innerHTML=\x22<in\
put type='radio'\
 checked='checke\
d' name='t'/>\x22;v\
.checkClone=Y.cl\
oneNode(!0).clon\
eNode(!0).lastCh\
ild.checked;v.no\
CloneEvent=!0;Y.\
attachEvent&&(Y.\
attachEvent(\x22onc\
lick\x22,function()\
{v.noCloneEvent=\
!1}),Y.cloneNode\
(!0).click());if\
(null==v.deleteE\
xpando){v.delete\
Expando=!0;try{d\
elete Y.test}cat\
ch(ae){v.deleteE\
xpando=!1}}var Y\
b=Y=\x0anb=null,Ab,\
Bb,Ac=y.createEl\
ement(\x22div\x22);for\
(Ab in{submit:!0\
,change:!0,focus\
in:!0})if(Bb=\x22on\
\x22+Ab,!(v[Ab+\x22Bub\
bles\x22]=Bb in a))\
Ac.setAttribute(\
Bb,\x22t\x22),v[Ab+\x22Bu\
bbles\x22]=!1===Ac.\
attributes[Bb].e\
xpando;var Zb=/^\
(?:input|select|\
textarea)$/i,xd=\
/^key/,yd=/^(?:m\
ouse|contextmenu\
)|click/,Bc=/^(?\
:focusinfocus|fo\
cusoutblur)$/,Cc\
=/^([^.]*)(?:\x5c.(\
.+)|)$/;g.event=\
{global:{},add:f\
unction(a,b,j,c,\
d){var n,e,r,k,l\
,t,h,B,z;if(r=g.\
_data(a)){j.hand\
ler&&(k=j,j=k.ha\
ndler,d=k.select\
or);j.guid||(j.g\
uid=g.guid++);if\
(!(e=r.events))e\
=\x0ar.events={};if\
(!(l=r.handle))l\
=r.handle=functi\
on(a){return typ\
eof g!==ka&&(!a|\
|g.event.trigger\
ed!==a.type)?g.e\
vent.dispatch.ap\
ply(l.elem,argum\
ents):void 0},l.\
elem=a;b=(b||\x22\x22)\
.match(xa)||[\x22\x22]\
;for(r=b.length;\
r--;)if(n=Cc.exe\
c(b[r])||[],B=t=\
n[1],z=(n[2]||\x22\x22\
).split(\x22.\x22).sor\
t(),B){n=g.event\
.special[B]||{};\
B=(d?n.delegateT\
ype:n.bindType)|\
|B;n=g.event.spe\
cial[B]||{};t=g.\
extend({type:B,o\
rigType:t,data:c\
,handler:j,guid:\
j.guid,selector:\
d,needsContext:d\
&&g.expr.match.n\
eedsContext.test\
(d),namespace:z.\
join(\x22.\x22)},\x0ak);i\
f(!(h=e[B]))if(h\
=e[B]=[],h.deleg\
ateCount=0,!n.se\
tup||!1===n.setu\
p.call(a,c,z,l))\
a.addEventListen\
er?a.addEventLis\
tener(B,l,!1):a.\
attachEvent&&a.a\
ttachEvent(\x22on\x22+\
B,l);n.add&&(n.a\
dd.call(a,t),t.h\
andler.guid||(t.\
handler.guid=j.g\
uid));d?h.splice\
(h.delegateCount\
++,0,t):h.push(t\
);g.event.global\
[B]=!0}a=null}},\
remove:function(\
a,b,j,c,d){var n\
,e,r,k,l,t,h,B,z\
,T,q,m=g.hasData\
(a)&&g._data(a);\
if(m&&(t=m.event\
s)){b=(b||\x22\x22).ma\
tch(xa)||[\x22\x22];fo\
r(l=b.length;l--\
;)if(r=Cc.exec(b\
[l])||[],z=q=r[1\
],T=(r[2]||\x22\x22).s\
plit(\x22.\x22).sort()\
,\x0az){h=g.event.s\
pecial[z]||{};z=\
(c?h.delegateTyp\
e:h.bindType)||z\
;B=t[z]||[];r=r[\
2]&&RegExp(\x22(^|\x5c\
\x5c.)\x22+T.join(\x22\x5c\x5c.\
(?:.*\x5c\x5c.|)\x22)+\x22(\x5c\
\x5c.|$)\x22);for(k=n=\
B.length;n--;)if\
(e=B[n],(d||q===\
e.origType)&&(!j\
||j.guid===e.gui\
d)&&(!r||r.test(\
e.namespace))&&(\
!c||c===e.select\
or||\x22**\x22===c&&e.\
selector))B.spli\
ce(n,1),e.select\
or&&B.delegateCo\
unt--,h.remove&&\
h.remove.call(a,\
e);k&&!B.length&\
&((!h.teardown||\
!1===h.teardown.\
call(a,T,m.handl\
e))&&g.removeEve\
nt(a,z,m.handle)\
,delete t[z])}el\
se for(z in t)g.\
event.remove(a,z\
+b[l],j,\x0ac,!0);g\
.isEmptyObject(t\
)&&(delete m.han\
dle,g._removeDat\
a(a,\x22events\x22))}}\
,trigger:functio\
n(f,b,j,c){var d\
,n,e,r,k,l,t=[j|\
|y],h=za.call(f,\
\x22type\x22)?f.type:f\
;k=za.call(f,\x22na\
mespace\x22)?f.name\
space.split(\x22.\x22)\
:[];e=d=j=j||y;i\
f(!(3===j.nodeTy\
pe||8===j.nodeTy\
pe)&&!Bc.test(h+\
g.event.triggere\
d))if(0<=h.index\
Of(\x22.\x22)&&(k=h.sp\
lit(\x22.\x22),h=k.shi\
ft(),k.sort()),n\
=0>h.indexOf(\x22:\x22\
)&&\x22on\x22+h,f=f[g.\
expando]?f:new g\
.Event(h,\x22object\
\x22===typeof f&&f)\
,f.isTrigger=c?2\
:3,f.namespace=k\
.join(\x22.\x22),f.nam\
espace_re=f.name\
space?RegExp(\x22(^\
|\x5c\x5c.)\x22+\x0ak.join(\x22\
\x5c\x5c.(?:.*\x5c\x5c.|)\x22)+\
\x22(\x5c\x5c.|$)\x22):null,\
f.result=void 0,\
f.target||(f.tar\
get=j),b=null==b\
?[f]:g.makeArray\
(b,[f]),k=g.even\
t.special[h]||{}\
,c||!(k.trigger&\
&!1===k.trigger.\
apply(j,b))){if(\
!c&&!k.noBubble&\
&!g.isWindow(j))\
{r=k.delegateTyp\
e||h;Bc.test(r+h\
)||(e=e.parentNo\
de);for(;e;e=e.p\
arentNode)t.push\
(e),d=e;if(d===(\
j.ownerDocument|\
|y))t.push(d.def\
aultView||d.pare\
ntWindow||a)}for\
(l=0;(e=t[l++])&\
&!f.isPropagatio\
nStopped();)if(f\
.type=1<l?r:k.bi\
ndType||h,(d=(g.\
_data(e,\x22events\x22\
)||{})[f.type]&&\
g._data(e,\x22handl\
e\x22))&&\x0ad.apply(e\
,b),(d=n&&e[n])&\
&d.apply&&g.acce\
ptData(e))f.resu\
lt=d.apply(e,b),\
!1===f.result&&f\
.preventDefault(\
);f.type=h;if(!c\
&&!f.isDefaultPr\
evented()&&(!k._\
default||!1===k.\
_default.apply(t\
.pop(),b))&&g.ac\
ceptData(j)&&n&&\
j[h]&&!g.isWindo\
w(j)){(d=j[n])&&\
(j[n]=null);g.ev\
ent.triggered=h;\
try{j[h]()}catch\
(B){}g.event.tri\
ggered=void 0;d&\
&(j[n]=d)}return\
 f.result}},disp\
atch:function(a)\
{a=g.event.fix(a\
);var b,j,c,d,e=\
[],r=n.call(argu\
ments);b=(g._dat\
a(this,\x22events\x22)\
||{})[a.type]||[\
];var k=g.event.\
special[a.type]|\
|\x0a{};r[0]=a;a.de\
legateTarget=thi\
s;if(!(k.preDisp\
atch&&!1===k.pre\
Dispatch.call(th\
is,a))){e=g.even\
t.handlers.call(\
this,a,b);for(b=\
0;(c=e[b++])&&!a\
.isPropagationSt\
opped();){a.curr\
entTarget=c.elem\
;for(d=0;(j=c.ha\
ndlers[d++])&&!a\
.isImmediateProp\
agationStopped()\
;)if(!a.namespac\
e_re||a.namespac\
e_re.test(j.name\
space))if(a.hand\
leObj=j,a.data=j\
.data,j=((g.even\
t.special[j.orig\
Type]||{}).handl\
e||j.handler).ap\
ply(c.elem,r),vo\
id 0!==j&&!1===(\
a.result=j))a.pr\
eventDefault(),a\
.stopPropagation\
()}k.postDispatc\
h&&k.postDispatc\
h.call(this,\x0aa);\
return a.result}\
},handlers:funct\
ion(a,b){var j,c\
,d,n,e=[],r=b.de\
legateCount,k=a.\
target;if(r&&k.n\
odeType&&(!a.but\
ton||\x22click\x22!==a\
.type))for(;k!=t\
his;k=k.parentNo\
de||this)if(1===\
k.nodeType&&(!0!\
==k.disabled||\x22c\
lick\x22!==a.type))\
{d=[];for(n=0;n<\
r;n++)c=b[n],j=c\
.selector+\x22 \x22,vo\
id 0===d[j]&&(d[\
j]=c.needsContex\
t?0<=g(j,this).i\
ndex(k):g.find(j\
,this,null,[k]).\
length),d[j]&&d.\
push(c);d.length\
&&e.push({elem:k\
,handlers:d})}r<\
b.length&&e.push\
({elem:this,hand\
lers:b.slice(r)}\
);return e},fix:\
function(a){if(a\
[g.expando])retu\
rn a;\x0avar b,j,c;\
b=a.type;var d=a\
,n=this.fixHooks\
[b];n||(this.fix\
Hooks[b]=n=yd.te\
st(b)?this.mouse\
Hooks:xd.test(b)\
?this.keyHooks:{\
});c=n.props?thi\
s.props.concat(n\
.props):this.pro\
ps;a=new g.Event\
(d);for(b=c.leng\
th;b--;)j=c[b],a\
[j]=d[j];a.targe\
t||(a.target=d.s\
rcElement||y);3=\
==a.target.nodeT\
ype&&(a.target=a\
.target.parentNo\
de);a.metaKey=!!\
a.metaKey;return\
 n.filter?n.filt\
er(a,d):a},props\
:\x22altKey bubbles\
 cancelable ctrl\
Key currentTarge\
t eventPhase met\
aKey relatedTarg\
et shiftKey targ\
et timeStamp vie\
w which\x22.split(\x22\
 \x22),\x0afixHooks:{}\
,keyHooks:{props\
:[\x22char\x22,\x22charCo\
de\x22,\x22key\x22,\x22keyCo\
de\x22],filter:func\
tion(a,b){null==\
a.which&&(a.whic\
h=null!=b.charCo\
de?b.charCode:b.\
keyCode);return \
a}},mouseHooks:{\
props:\x22button bu\
ttons clientX cl\
ientY fromElemen\
t offsetX offset\
Y pageX pageY sc\
reenX screenY to\
Element\x22.split(\x22\
 \x22),filter:funct\
ion(a,b){var g,j\
,c=b.button,d=b.\
fromElement;null\
==a.pageX&&null!\
=b.clientX&&(g=a\
.target.ownerDoc\
ument||y,j=g.doc\
umentElement,g=g\
.body,a.pageX=b.\
clientX+(j&&j.sc\
rollLeft||g&&g.s\
crollLeft||0)-(j\
&&j.clientLeft||\
\x0ag&&g.clientLeft\
||0),a.pageY=b.c\
lientY+(j&&j.scr\
ollTop||g&&g.scr\
ollTop||0)-(j&&j\
.clientTop||g&&g\
.clientTop||0));\
!a.relatedTarget\
&&d&&(a.relatedT\
arget=d===a.targ\
et?b.toElement:d\
);!a.which&&void\
 0!==c&&(a.which\
=c&1?1:c&2?3:c&4\
?2:0);return a}}\
,special:{load:{\
noBubble:!0},foc\
us:{trigger:func\
tion(){if(this!=\
=F()&&this.focus\
)try{return this\
.focus(),!1}catc\
h(a){}},delegate\
Type:\x22focusin\x22},\
blur:{trigger:fu\
nction(){if(this\
===F()&&this.blu\
r)return this.bl\
ur(),!1},delegat\
eType:\x22focusout\x22\
},click:{trigger\
:function(){if(g\
.nodeName(this,\x0a\
\x22input\x22)&&\x22check\
box\x22===this.type\
&&this.click)ret\
urn this.click()\
,!1},_default:fu\
nction(a){return\
 g.nodeName(a.ta\
rget,\x22a\x22)}},befo\
reunload:{postDi\
spatch:function(\
a){void 0!==a.re\
sult&&(a.origina\
lEvent.returnVal\
ue=a.result)}}},\
simulate:functio\
n(a,b,j,c){a=g.e\
xtend(new g.Even\
t,j,{type:a,isSi\
mulated:!0,origi\
nalEvent:{}});c?\
g.event.trigger(\
a,null,b):g.even\
t.dispatch.call(\
b,a);a.isDefault\
Prevented()&&j.p\
reventDefault()}\
};g.removeEvent=\
y.removeEventLis\
tener?function(a\
,b,g){a.removeEv\
entListener&&a.r\
emoveEventListen\
er(b,\x0ag,!1)}:fun\
ction(a,b,g){b=\x22\
on\x22+b;a.detachEv\
ent&&(typeof a[b\
]===ka&&(a[b]=nu\
ll),a.detachEven\
t(b,g))};g.Event\
=function(a,b){i\
f(!(this instanc\
eof g.Event))ret\
urn new g.Event(\
a,b);a&&a.type?(\
this.originalEve\
nt=a,this.type=a\
.type,this.isDef\
aultPrevented=a.\
defaultPrevented\
||void 0===a.def\
aultPrevented&&(\
!1===a.returnVal\
ue||a.getPrevent\
Default&&a.getPr\
eventDefault())?\
d:t):this.type=a\
;b&&g.extend(thi\
s,b);this.timeSt\
amp=a&&a.timeSta\
mp||g.now();this\
[g.expando]=!0};\
g.Event.prototyp\
e={isDefaultPrev\
ented:t,isPropag\
ationStopped:t,\x0a\
isImmediatePropa\
gationStopped:t,\
preventDefault:f\
unction(){var a=\
this.originalEve\
nt;this.isDefaul\
tPrevented=d;a&&\
(a.preventDefaul\
t?a.preventDefau\
lt():a.returnVal\
ue=!1)},stopProp\
agation:function\
(){var a=this.or\
iginalEvent;this\
.isPropagationSt\
opped=d;a&&(a.st\
opPropagation&&a\
.stopPropagation\
(),a.cancelBubbl\
e=!0)},stopImmed\
iatePropagation:\
function(){this.\
isImmediatePropa\
gationStopped=d;\
this.stopPropaga\
tion()}};g.each(\
{mouseenter:\x22mou\
seover\x22,mouselea\
ve:\x22mouseout\x22},f\
unction(a,b){g.e\
vent.special[a]=\
{delegateType:b,\
\x0abindType:b,hand\
le:function(a){v\
ar f,j=a.related\
Target,c=a.handl\
eObj;if(!j||j!==\
this&&!g.contain\
s(this,j))a.type\
=c.origType,f=c.\
handler.apply(th\
is,arguments),a.\
type=b;return f}\
}});v.submitBubb\
les||(g.event.sp\
ecial.submit={se\
tup:function(){i\
f(g.nodeName(thi\
s,\x22form\x22))return\
!1;g.event.add(t\
his,\x22click._subm\
it keypress._sub\
mit\x22,function(a)\
{a=a.target;if((\
a=g.nodeName(a,\x22\
input\x22)||g.nodeN\
ame(a,\x22button\x22)?\
a.form:void 0)&&\
!g._data(a,\x22subm\
itBubbles\x22))g.ev\
ent.add(a,\x22submi\
t._submit\x22,funct\
ion(a){a._submit\
_bubble=\x0a!0}),g.\
_data(a,\x22submitB\
ubbles\x22,!0)})},p\
ostDispatch:func\
tion(a){a._submi\
t_bubble&&(delet\
e a._submit_bubb\
le,this.parentNo\
de&&!a.isTrigger\
&&g.event.simula\
te(\x22submit\x22,this\
.parentNode,a,!0\
))},teardown:fun\
ction(){if(g.nod\
eName(this,\x22form\
\x22))return!1;g.ev\
ent.remove(this,\
\x22._submit\x22)}});v\
.changeBubbles||\
(g.event.special\
.change={setup:f\
unction(){if(Zb.\
test(this.nodeNa\
me)){if(\x22checkbo\
x\x22===this.type||\
\x22radio\x22===this.t\
ype)g.event.add(\
this,\x22propertych\
ange._change\x22,fu\
nction(a){\x22check\
ed\x22===a.original\
Event.propertyNa\
me&&\x0a(this._just\
_changed=!0)}),g\
.event.add(this,\
\x22click._change\x22,\
function(a){this\
._just_changed&&\
!a.isTrigger&&(t\
his._just_change\
d=!1);g.event.si\
mulate(\x22change\x22,\
this,a,!0)});ret\
urn!1}g.event.ad\
d(this,\x22beforeac\
tivate._change\x22,\
function(a){a=a.\
target;Zb.test(a\
.nodeName)&&!g._\
data(a,\x22changeBu\
bbles\x22)&&(g.even\
t.add(a,\x22change.\
_change\x22,functio\
n(a){this.parent\
Node&&(!a.isSimu\
lated&&!a.isTrig\
ger)&&g.event.si\
mulate(\x22change\x22,\
this.parentNode,\
a,!0)}),g._data(\
a,\x22changeBubbles\
\x22,!0))})},handle\
:function(a){var\
 b=a.target;\x0aif(\
this!==b||a.isSi\
mulated||a.isTri\
gger||\x22radio\x22!==\
b.type&&\x22checkbo\
x\x22!==b.type)retu\
rn a.handleObj.h\
andler.apply(thi\
s,arguments)},te\
ardown:function(\
){g.event.remove\
(this,\x22._change\x22\
);return!Zb.test\
(this.nodeName)}\
});v.focusinBubb\
les||g.each({foc\
us:\x22focusin\x22,blu\
r:\x22focusout\x22},fu\
nction(a,b){var \
j=function(a){g.\
event.simulate(b\
,a.target,g.even\
t.fix(a),!0)};g.\
event.special[b]\
={setup:function\
(){var c=this.ow\
nerDocument||thi\
s,d=g._data(c,b)\
;d||c.addEventLi\
stener(a,j,!0);g\
._data(c,b,(d||0\
)+1)},teardown:f\
unction(){var c=\
\x0athis.ownerDocum\
ent||this,d=g._d\
ata(c,b)-1;d?g._\
data(c,b,d):(c.r\
emoveEventListen\
er(a,j,!0),g._re\
moveData(c,b))}}\
});g.fn.extend({\
on:function(a,b,\
j,c,d){var n,e;i\
f(\x22object\x22===typ\
eof a){\x22string\x22!\
==typeof b&&(j=j\
||b,b=void 0);fo\
r(n in a)this.on\
(n,b,j,a[n],d);r\
eturn this}null=\
=j&&null==c?(c=b\
,j=b=void 0):nul\
l==c&&(\x22string\x22=\
==typeof b?(c=j,\
j=void 0):(c=j,j\
=b,b=void 0));if\
(!1===c)c=t;else\
 if(!c)return th\
is;1===d&&(e=c,c\
=function(a){g()\
.off(a);return e\
.apply(this,argu\
ments)},c.guid=e\
.guid||(e.guid=g\
.guid++));\x0aretur\
n this.each(func\
tion(){g.event.a\
dd(this,a,c,j,b)\
})},one:function\
(a,b,g,j){return\
 this.on(a,b,g,j\
,1)},off:functio\
n(a,b,j){var c;i\
f(a&&a.preventDe\
fault&&a.handleO\
bj)return c=a.ha\
ndleObj,g(a.dele\
gateTarget).off(\
c.namespace?c.or\
igType+\x22.\x22+c.nam\
espace:c.origTyp\
e,c.selector,c.h\
andler),this;if(\
\x22object\x22===typeo\
f a){for(c in a)\
this.off(c,b,a[c\
]);return this}i\
f(!1===b||\x22funct\
ion\x22===typeof b)\
j=b,b=void 0;!1=\
==j&&(j=t);retur\
n this.each(func\
tion(){g.event.r\
emove(this,a,j,b\
)})},trigger:fun\
ction(a,b){retur\
n this.each(func\
tion(){g.event.t\
rigger(a,\x0ab,this\
)})},triggerHand\
ler:function(a,b\
){var j=this[0];\
if(j)return g.ev\
ent.trigger(a,b,\
j,!0)}});var mc=\
\x22abbr|article|as\
ide|audio|bdi|ca\
nvas|data|datali\
st|details|figca\
ption|figure|foo\
ter|header|hgrou\
p|mark|meter|nav\
|output|progress\
|section|summary\
|time|video\x22,zd=\
/ jQuery\x5cd+=\x22(?:\
null|\x5cd+)\x22/g,Dc=\
RegExp(\x22<(?:\x22+mc\
+\x22)[\x5c\x5cs/>]\x22,\x22i\x22)\
,$b=/^\x5cs+/,Ec=/<\
(?!area|br|col|e\
mbed|hr|img|inpu\
t|link|meta|para\
m)(([\x5cw:]+)[^>]*\
)\x5c/>/gi,Fc=/<([\x5c\
w:]+)/,Gc=/<tbod\
y/i,Ad=/<|&#?\x5cw+\
;/,Bd=/<(?:scrip\
t|style|link)/i,\
Cd=/checked\x5cs*(?\
:[^=]|=\x5cs*.check\
ed.)/i,\x0aHc=/^$|\x5c\
/(?:java|ecma)sc\
ript/i,Yc=/^true\
\x5c/(.*)/,Dd=/^\x5cs*\
<!(?:\x5c[CDATA\x5c[|-\
-)|(?:\x5c]\x5c]|--)>\x5c\
s*$/g,ja={option\
:[1,\x22<select mul\
tiple='multiple'\
>\x22,\x22</select>\x22],\
legend:[1,\x22<fiel\
dset>\x22,\x22</fields\
et>\x22],area:[1,\x22<\
map>\x22,\x22</map>\x22],\
param:[1,\x22<objec\
t>\x22,\x22</object>\x22]\
,thead:[1,\x22<tabl\
e>\x22,\x22</table>\x22],\
tr:[2,\x22<table><t\
body>\x22,\x22</tbody>\
</table>\x22],col:[\
2,\x22<table><tbody\
></tbody><colgro\
up>\x22,\x22</colgroup\
></table>\x22],td:[\
3,\x22<table><tbody\
><tr>\x22,\x22</tr></t\
body></table>\x22],\
_default:v.htmlS\
erialize?[0,\x22\x22,\x22\
\x22]:[1,\x22X<div>\x22,\x22\
</div>\x22]},ac=\x0aC(\
y).appendChild(y\
.createElement(\x22\
div\x22));ja.optgro\
up=ja.option;ja.\
tbody=ja.tfoot=j\
a.colgroup=ja.ca\
ption=ja.thead;j\
a.th=ja.td;g.ext\
end({clone:funct\
ion(a,b,j){var c\
,d,n,e,r,k=g.con\
tains(a.ownerDoc\
ument,a);v.html5\
Clone||g.isXMLDo\
c(a)||!Dc.test(\x22\
<\x22+a.nodeName+\x22>\
\x22)?n=a.cloneNode\
(!0):(ac.innerHT\
ML=a.outerHTML,a\
c.removeChild(n=\
ac.firstChild));\
if((!v.noCloneEv\
ent||!v.noCloneC\
hecked)&&(1===a.\
nodeType||11===a\
.nodeType)&&!g.i\
sXMLDoc(a)){c=K(\
n);r=K(a);for(e=\
0;null!=(d=r[e])\
;++e)if(c[e]){va\
r l=c[e],h=void \
0,t=\x0avoid 0,B=vo\
id 0;if(1===l.no\
deType){h=l.node\
Name.toLowerCase\
();if(!v.noClone\
Event&&l[g.expan\
do]){B=g._data(l\
);for(t in B.eve\
nts)g.removeEven\
t(l,t,B.handle);\
l.removeAttribut\
e(g.expando)}if(\
\x22script\x22===h&&l.\
text!==d.text)Ea\
(l).text=d.text,\
U(l);else if(\x22ob\
ject\x22===h)l.pare\
ntNode&&(l.outer\
HTML=d.outerHTML\
),v.html5Clone&&\
(d.innerHTML&&!g\
.trim(l.innerHTM\
L))&&(l.innerHTM\
L=d.innerHTML);e\
lse if(\x22input\x22==\
=h&&Mb.test(d.ty\
pe))l.defaultChe\
cked=l.checked=d\
.checked,l.value\
!==d.value&&(l.v\
alue=d.value);el\
se if(\x22option\x22==\
=\x0ah)l.defaultSel\
ected=l.selected\
=d.defaultSelect\
ed;else if(\x22inpu\
t\x22===h||\x22textare\
a\x22===h)l.default\
Value=d.defaultV\
alue}}}if(b)if(j\
){r=r||K(a);c=c|\
|K(n);for(e=0;nu\
ll!=(d=r[e]);e++\
)Fa(d,c[e])}else\
 Fa(a,n);c=K(n,\x22\
script\x22);0<c.len\
gth&&P(c,!k&&K(a\
,\x22script\x22));retu\
rn n},buildFragm\
ent:function(a,b\
,j,c){for(var d,\
n,e,r,k,l,h=a.le\
ngth,t=C(b),B=[]\
,z=0;z<h;z++)if(\
(n=a[z])||0===n)\
if(\x22object\x22===g.\
type(n))g.merge(\
B,n.nodeType?[n]\
:n);else if(Ad.t\
est(n)){e=e||t.a\
ppendChild(b.cre\
ateElement(\x22div\x22\
));r=(Fc.exec(n)\
||[\x22\x22,\x22\x22])[1].to\
LowerCase();\x0al=j\
a[r]||ja._defaul\
t;e.innerHTML=l[\
1]+n.replace(Ec,\
\x22<$1></$2>\x22)+l[2\
];for(d=l[0];d--\
;)e=e.lastChild;\
!v.leadingWhites\
pace&&$b.test(n)\
&&B.push(b.creat\
eTextNode($b.exe\
c(n)[0]));if(!v.\
tbody)for(d=(n=\x22\
table\x22===r&&!Gc.\
test(n)?e.firstC\
hild:\x22<table>\x22==\
=l[1]&&!Gc.test(\
n)?e:0)&&n.child\
Nodes.length;d--\
;)g.nodeName(k=n\
.childNodes[d],\x22\
tbody\x22)&&!k.chil\
dNodes.length&&n\
.removeChild(k);\
g.merge(B,e.chil\
dNodes);for(e.te\
xtContent=\x22\x22;e.f\
irstChild;)e.rem\
oveChild(e.first\
Child);e=t.lastC\
hild}else B.push\
(b.createTextNod\
e(n));\x0ae&&t.remo\
veChild(e);v.app\
endChecked||g.gr\
ep(K(B,\x22input\x22),\
rb);for(z=0;n=B[\
z++];)if(!(c&&-1\
!==g.inArray(n,c\
))&&(a=g.contain\
s(n.ownerDocumen\
t,n),e=K(t.appen\
dChild(n),\x22scrip\
t\x22),a&&P(e),j))f\
or(d=0;n=e[d++];\
)Hc.test(n.type|\
|\x22\x22)&&j.push(n);\
return t},cleanD\
ata:function(a,b\
){for(var c,d,n,\
e,r=0,k=g.expand\
o,l=g.cache,h=v.\
deleteExpando,t=\
g.event.special;\
null!=(c=a[r]);r\
++)if(b||g.accep\
tData(c))if(e=(n\
=c[k])&&l[n]){if\
(e.events)for(d \
in e.events)t[d]\
?g.event.remove(\
c,d):g.removeEve\
nt(c,d,e.handle)\
;l[n]&&(delete l\
[n],\x0ah?delete c[\
k]:typeof c.remo\
veAttribute!==ka\
?c.removeAttribu\
te(k):c[k]=null,\
j.push(n))}}});g\
.fn.extend({text\
:function(a){ret\
urn Va(this,func\
tion(a){return v\
oid 0===a?g.text\
(this):this.empt\
y().append((this\
[0]&&this[0].own\
erDocument||y).c\
reateTextNode(a)\
)},null,a,argume\
nts.length)},app\
end:function(){r\
eturn this.domMa\
nip(arguments,fu\
nction(a){(1===t\
his.nodeType||11\
===this.nodeType\
||9===this.nodeT\
ype)&&Ya(this,a)\
.appendChild(a)}\
)},prepend:funct\
ion(){return thi\
s.domManip(argum\
ents,function(a)\
{if(1===this.nod\
eType||\x0a11===thi\
s.nodeType||9===\
this.nodeType){v\
ar b=Ya(this,a);\
b.insertBefore(a\
,b.firstChild)}}\
)},before:functi\
on(){return this\
.domManip(argume\
nts,function(a){\
this.parentNode&\
&this.parentNode\
.insertBefore(a,\
this)})},after:f\
unction(){return\
 this.domManip(a\
rguments,functio\
n(a){this.parent\
Node&&this.paren\
tNode.insertBefo\
re(a,this.nextSi\
bling)})},remove\
:function(a,b){f\
or(var j,c=a?g.f\
ilter(a,this):th\
is,d=0;null!=(j=\
c[d]);d++)!b&&1=\
==j.nodeType&&g.\
cleanData(K(j)),\
j.parentNode&&(b\
&&g.contains(j.o\
wnerDocument,\x0aj)\
&&P(K(j,\x22script\x22\
)),j.parentNode.\
removeChild(j));\
return this},emp\
ty:function(){fo\
r(var a,b=0;null\
!=(a=this[b]);b+\
+){for(1===a.nod\
eType&&g.cleanDa\
ta(K(a,!1));a.fi\
rstChild;)a.remo\
veChild(a.firstC\
hild);a.options&\
&g.nodeName(a,\x22s\
elect\x22)&&(a.opti\
ons.length=0)}re\
turn this},clone\
:function(a,b){a\
=null==a?!1:a;b=\
null==b?a:b;retu\
rn this.map(func\
tion(){return g.\
clone(this,a,b)}\
)},html:function\
(a){return Va(th\
is,function(a){v\
ar f=this[0]||{}\
,b=0,j=this.leng\
th;if(void 0===a\
)return 1===f.no\
deType?f.innerHT\
ML.replace(zd,\x0a\x22\
\x22):void 0;if(\x22st\
ring\x22===typeof a\
&&!Bd.test(a)&&(\
v.htmlSerialize|\
|!Dc.test(a))&&(\
v.leadingWhitesp\
ace||!$b.test(a)\
)&&!ja[(Fc.exec(\
a)||[\x22\x22,\x22\x22])[1].\
toLowerCase()]){\
a=a.replace(Ec,\x22\
<$1></$2>\x22);try{\
for(;b<j;b++)f=t\
his[b]||{},1===f\
.nodeType&&(g.cl\
eanData(K(f,!1))\
,f.innerHTML=a);\
f=0}catch(c){}}f\
&&this.empty().a\
ppend(a)},null,a\
,arguments.lengt\
h)},replaceWith:\
function(){var a\
=arguments[0];th\
is.domManip(argu\
ments,function(b\
){a=this.parentN\
ode;g.cleanData(\
K(this));a&&a.re\
placeChild(b,thi\
s)});return a&&(\
a.length||\x0aa.nod\
eType)?this:this\
.remove()},detac\
h:function(a){re\
turn this.remove\
(a,!0)},domManip\
:function(a,b){a\
=r.apply([],a);v\
ar j,c,d,n,e=0,k\
=this.length,l=t\
his,h=k-1,t=a[0]\
,B=g.isFunction(\
t);if(B||1<k&&\x22s\
tring\x22===typeof \
t&&!v.checkClone\
&&Cd.test(t))ret\
urn this.each(fu\
nction(j){var g=\
l.eq(j);B&&(a[0]\
=t.call(this,j,g\
.html()));g.domM\
anip(a,b)});if(k\
&&(n=g.buildFrag\
ment(a,this[0].o\
wnerDocument,!1,\
this),j=n.firstC\
hild,1===n.child\
Nodes.length&&(n\
=j),j)){d=g.map(\
K(n,\x22script\x22),Ea\
);for(c=d.length\
;e<k;e++)j=n,e!=\
=\x0ah&&(j=g.clone(\
j,!0,!0),c&&g.me\
rge(d,K(j,\x22scrip\
t\x22))),b.call(thi\
s[e],j,e);if(c){\
n=d[d.length-1].\
ownerDocument;g.\
map(d,U);for(e=0\
;e<c;e++)if(j=d[\
e],Hc.test(j.typ\
e||\x22\x22)&&!g._data\
(j,\x22globalEval\x22)\
&&g.contains(n,j\
))j.src?g._evalU\
rl&&g._evalUrl(j\
.src):g.globalEv\
al((j.text||j.te\
xtContent||j.inn\
erHTML||\x22\x22).repl\
ace(Dd,\x22\x22))}n=j=\
null}return this\
}});g.each({appe\
ndTo:\x22append\x22,pr\
ependTo:\x22prepend\
\x22,insertBefore:\x22\
before\x22,insertAf\
ter:\x22after\x22,repl\
aceAll:\x22replaceW\
ith\x22},function(a\
,b){g.fn[a]=func\
tion(a){for(var \
f=0,j=[],\x0ac=g(a)\
,d=c.length-1;f<\
=d;f++)a=f===d?t\
his:this.clone(!\
0),g(c[f])[b](a)\
,z.apply(j,a.get\
());return this.\
pushStack(j)}});\
var eb,nc={},ob,\
Cb,ab=y.createEl\
ement(\x22div\x22);ab.\
innerHTML=\x22  <li\
nk/><table></tab\
le><a href='/a'>\
a</a><input type\
='checkbox'/>\x22;o\
b=ab.getElements\
ByTagName(\x22a\x22)[0\
];ob.style.cssTe\
xt=\x22float:left;o\
pacity:.5\x22;v.opa\
city=/^0.5/.test\
(ob.style.opacit\
y);v.cssFloat=!!\
ob.style.cssFloa\
t;ab.style.backg\
roundClip=\x22conte\
nt-box\x22;ab.clone\
Node(!0).style.b\
ackgroundClip=\x22\x22\
;v.clearCloneSty\
le=\x22content-box\x22\
===\x0aab.style.bac\
kgroundClip;ob=a\
b=null;v.shrinkW\
rapBlocks=functi\
on(){var a,b,j;i\
f(null==Cb){a=y.\
getElementsByTag\
Name(\x22body\x22)[0];\
if(!a)return;b=y\
.createElement(\x22\
div\x22);j=y.create\
Element(\x22div\x22);a\
.appendChild(b).\
appendChild(j);C\
b=!1;typeof j.st\
yle.zoom!==ka&&(\
j.style.cssText=\
\x22-webkit-box-siz\
ing:content-box;\
-moz-box-sizing:\
content-box;box-\
sizing:content-b\
ox;display:block\
;padding:0;margi\
n:0;border:0;wid\
th:1px;padding:1\
px;zoom:1\x22,j.inn\
erHTML=\x22<div></d\
iv>\x22,j.firstChil\
d.style.width=\x225\
px\x22,Cb=3!==j.off\
setWidth);\x0aa.rem\
oveChild(b)}retu\
rn Cb};var Ic=/^\
margin/,sb=RegEx\
p(\x22^(\x22+zb+\x22)(?!p\
x)[a-z%]+$\x22,\x22i\x22)\
,Ra,Sa,Ed=/^(top\
|right|bottom|le\
ft)$/;a.getCompu\
tedStyle?(Ra=fun\
ction(a){return \
a.ownerDocument.\
defaultView.getC\
omputedStyle(a,n\
ull)},Sa=functio\
n(a,b,j){var c,d\
,n=a.style;d=(j=\
j||Ra(a))?j.getP\
ropertyValue(b)|\
|j[b]:void 0;j&&\
(\x22\x22===d&&!g.cont\
ains(a.ownerDocu\
ment,a)&&(d=g.st\
yle(a,b)),sb.tes\
t(d)&&Ic.test(b)\
&&(a=n.width,b=n\
.minWidth,c=n.ma\
xWidth,n.minWidt\
h=n.maxWidth=n.w\
idth=d,d=j.width\
,n.width=a,n.min\
Width=b,n.maxWid\
th=\x0ac));return v\
oid 0===d?d:d+\x22\x22\
}):y.documentEle\
ment.currentStyl\
e&&(Ra=function(\
a){return a.curr\
entStyle},Sa=fun\
ction(a,b,j){var\
 g,c,d,n=a.style\
;d=(j=j||Ra(a))?\
j[b]:void 0;null\
==d&&(n&&n[b])&&\
(d=n[b]);if(sb.t\
est(d)&&!Ed.test\
(b)){j=n.left;if\
(c=(g=a.runtimeS\
tyle)&&g.left)g.\
left=a.currentSt\
yle.left;n.left=\
\x22fontSize\x22===b?\x22\
1em\x22:d;d=n.pixel\
Left+\x22px\x22;n.left\
=j;c&&(g.left=c)\
}return void 0==\
=d?d:d+\x22\x22||\x22auto\
\x22});var dc=funct\
ion(){var f,b,j=\
y.getElementsByT\
agName(\x22body\x22)[0\
];j&&(f=y.create\
Element(\x22div\x22),b\
=y.createElement\
(\x22div\x22),\x0af.style\
.cssText=bc,j.ap\
pendChild(f).app\
endChild(b),b.st\
yle.cssText=\x22-we\
bkit-box-sizing:\
border-box;-moz-\
box-sizing:borde\
r-box;box-sizing\
:border-box;posi\
tion:absolute;di\
splay:block;padd\
ing:1px;border:1\
px;width:4px;mar\
gin-top:1%;top:1\
%\x22,g.swap(j,null\
!=j.style.zoom?{\
zoom:1}:{},funct\
ion(){cc=4===b.o\
ffsetWidth}),Db=\
!0,Eb=!1,Fb=!0,a\
.getComputedStyl\
e&&(Eb=\x221%\x22!==(a\
.getComputedStyl\
e(b,null)||{}).t\
op,Db=\x224px\x22===(a\
.getComputedStyl\
e(b,null)||{widt\
h:\x224px\x22}).width)\
,j.removeChild(f\
),b=j=null)},pb,\
Gb,cc,Db,Eb,Fb,\x0a\
bb=y.createEleme\
nt(\x22div\x22),bc=\x22bo\
rder:0;width:0;h\
eight:0;position\
:absolute;top:0;\
left:-9999px\x22;bb\
.innerHTML=\x22  <l\
ink/><table></ta\
ble><a href='/a'\
>a</a><input typ\
e='checkbox'/>\x22;\
pb=bb.getElement\
sByTagName(\x22a\x22)[\
0];pb.style.cssT\
ext=\x22float:left;\
opacity:.5\x22;v.op\
acity=/^0.5/.tes\
t(pb.style.opaci\
ty);v.cssFloat=!\
!pb.style.cssFlo\
at;bb.style.back\
groundClip=\x22cont\
ent-box\x22;bb.clon\
eNode(!0).style.\
backgroundClip=\x22\
\x22;v.clearCloneSt\
yle=\x22content-box\
\x22===bb.style.bac\
kgroundClip;pb=b\
b=null;g.extend(\
v,{reliableHidde\
nOffsets:functio\
n(){if(null!=\x0aGb\
)return Gb;var a\
,b,j;b=y.createE\
lement(\x22div\x22);va\
r g=y.getElement\
sByTagName(\x22body\
\x22)[0];if(g)retur\
n b.setAttribute\
(\x22className\x22,\x22t\x22\
),b.innerHTML=\x22 \
 <link/><table><\
/table><a href='\
/a'>a</a><input \
type='checkbox'/\
>\x22,a=y.createEle\
ment(\x22div\x22),a.st\
yle.cssText=bc,g\
.appendChild(a).\
appendChild(b),b\
.innerHTML=\x22<tab\
le><tr><td></td>\
<td>t</td></tr><\
/table>\x22,b=b.get\
ElementsByTagNam\
e(\x22td\x22),b[0].sty\
le.cssText=\x22padd\
ing:0;margin:0;b\
order:0;display:\
none\x22,j=0===b[0]\
.offsetHeight,b[\
0].style.display\
=\x22\x22,b[1].style.d\
isplay=\x0a\x22none\x22,G\
b=j&&0===b[0].of\
fsetHeight,g.rem\
oveChild(a),Gb},\
boxSizing:functi\
on(){null==cc&&d\
c();return cc},b\
oxSizingReliable\
:function(){null\
==Db&&dc();retur\
n Db},pixelPosit\
ion:function(){n\
ull==Eb&&dc();re\
turn Eb},reliabl\
eMarginRight:fun\
ction(){var f,b,\
j,g;if(null==Fb&\
&a.getComputedSt\
yle){f=y.getElem\
entsByTagName(\x22b\
ody\x22)[0];if(!f)r\
eturn;b=y.create\
Element(\x22div\x22);j\
=y.createElement\
(\x22div\x22);b.style.\
cssText=bc;f.app\
endChild(b).appe\
ndChild(j);g=j.a\
ppendChild(y.cre\
ateElement(\x22div\x22\
));g.style.cssTe\
xt=j.style.cssTe\
xt=\x0a\x22-webkit-box\
-sizing:content-\
box;-moz-box-siz\
ing:content-box;\
box-sizing:conte\
nt-box;display:b\
lock;padding:0;m\
argin:0;border:0\
\x22;g.style.margin\
Right=g.style.wi\
dth=\x220\x22;j.style.\
width=\x221px\x22;Fb=!\
parseFloat((a.ge\
tComputedStyle(g\
,null)||{}).marg\
inRight);f.remov\
eChild(b)}return\
 Fb}});g.swap=fu\
nction(a,b,j,g){\
var c,d={};for(c\
 in b)d[c]=a.sty\
le[c],a.style[c]\
=b[c];j=j.apply(\
a,g||[]);for(c i\
n b)a.style[c]=d\
[c];return j};va\
r ec=/alpha\x5c([^)\
]*\x5c)/i,Fd=/opaci\
ty\x5cs*=\x5cs*([^)]*)\
/,Gd=/^(none|tab\
le(?!-c[ea]).+)/\
,Zc=RegExp(\x22^(\x22+\
\x0azb+\x22)(.*)$\x22,\x22i\x22\
),Hd=RegExp(\x22^([\
+-])=(\x22+zb+\x22)\x22,\x22\
i\x22),Id={position\
:\x22absolute\x22,visi\
bility:\x22hidden\x22,\
display:\x22block\x22}\
,Jc={letterSpaci\
ng:0,fontWeight:\
400},oc=[\x22Webkit\
\x22,\x22O\x22,\x22Moz\x22,\x22ms\x22\
];g.extend({cssH\
ooks:{opacity:{g\
et:function(a,b)\
{if(b){var j=Sa(\
a,\x22opacity\x22);ret\
urn\x22\x22===j?\x221\x22:j}\
}}},cssNumber:{c\
olumnCount:!0,fi\
llOpacity:!0,fon\
tWeight:!0,lineH\
eight:!0,opacity\
:!0,order:!0,orp\
hans:!0,widows:!\
0,zIndex:!0,zoom\
:!0},cssProps:{\x22\
float\x22:v.cssFloa\
t?\x22cssFloat\x22:\x22st\
yleFloat\x22},style\
:function(a,b,j,\
c){if(a&&!(3===a\
.nodeType||\x0a8===\
a.nodeType||!a.s\
tyle)){var d,n,e\
,r=g.camelCase(b\
),k=a.style;b=g.\
cssProps[r]||(g.\
cssProps[r]=gb(k\
,r));e=g.cssHook\
s[b]||g.cssHooks\
[r];if(void 0!==\
j){n=typeof j;if\
(\x22string\x22===n&&(\
d=Hd.exec(j)))j=\
(d[1]+1)*d[2]+pa\
rseFloat(g.css(a\
,b)),n=\x22number\x22;\
if(!(null==j||j!\
==j))if(\x22number\x22\
===n&&!g.cssNumb\
er[r]&&(j+=\x22px\x22)\
,!v.clearCloneSt\
yle&&(\x22\x22===j&&0=\
==b.indexOf(\x22bac\
kground\x22))&&(k[b\
]=\x22inherit\x22),!e|\
|!(\x22set\x22in e)||v\
oid 0!==(j=e.set\
(a,j,c)))try{k[b\
]=\x22\x22,k[b]=j}catc\
h(l){}}else retu\
rn e&&\x22get\x22in e&\
&void 0!==(d=e.g\
et(a,\x0a!1,c))?d:k\
[b]}},css:functi\
on(a,b,j,c){var \
d,n;n=g.camelCas\
e(b);b=g.cssProp\
s[n]||(g.cssProp\
s[n]=gb(a.style,\
n));(n=g.cssHook\
s[b]||g.cssHooks\
[n])&&\x22get\x22in n&\
&(d=n.get(a,!0,j\
));void 0===d&&(\
d=Sa(a,b,c));\x22no\
rmal\x22===d&&b in \
Jc&&(d=Jc[b]);re\
turn\x22\x22===j||j?(a\
=parseFloat(d),!\
0===j||g.isNumer\
ic(a)?a||0:d):d}\
});g.each([\x22heig\
ht\x22,\x22width\x22],fun\
ction(a,b){g.css\
Hooks[b]={get:fu\
nction(a,f,j){if\
(f)return 0===a.\
offsetWidth&&Gd.\
test(g.css(a,\x22di\
splay\x22))?g.swap(\
a,Id,function(){\
return Z(a,b,j)}\
):Z(a,b,j)},set:\
function(a,\x0af,j)\
{var c=j&&Ra(a);\
return la(a,f,j?\
x(a,b,j,v.boxSiz\
ing()&&\x22border-b\
ox\x22===g.css(a,\x22b\
oxSizing\x22,!1,c),\
c):0)}}});v.opac\
ity||(g.cssHooks\
.opacity={get:fu\
nction(a,b){retu\
rn Fd.test((b&&a\
.currentStyle?a.\
currentStyle.fil\
ter:a.style.filt\
er)||\x22\x22)?0.01*pa\
rseFloat(RegExp.\
$1)+\x22\x22:b?\x221\x22:\x22\x22}\
,set:function(a,\
b){var j=a.style\
,c=a.currentStyl\
e,d=g.isNumeric(\
b)?\x22alpha(opacit\
y=\x22+100*b+\x22)\x22:\x22\x22\
,n=c&&c.filter||\
j.filter||\x22\x22;j.z\
oom=1;if((1<=b||\
\x22\x22===b)&&\x22\x22===g.\
trim(n.replace(e\
c,\x22\x22))&&j.remove\
Attribute)if(j.r\
emoveAttribute(\x22\
filter\x22),\x0a\x22\x22===b\
||c&&!c.filter)r\
eturn;j.filter=e\
c.test(n)?n.repl\
ace(ec,d):n+\x22 \x22+\
d}});g.cssHooks.\
marginRight=fb(v\
.reliableMarginR\
ight,function(a,\
b){if(b)return g\
.swap(a,{display\
:\x22inline-block\x22}\
,Sa,[a,\x22marginRi\
ght\x22])});g.each(\
{margin:\x22\x22,paddi\
ng:\x22\x22,border:\x22Wi\
dth\x22},function(a\
,b){g.cssHooks[a\
+b]={expand:func\
tion(j){var g=0,\
c={};for(j=\x22stri\
ng\x22===typeof j?j\
.split(\x22 \x22):[j];\
4>g;g++)c[a+Qa[g\
]+b]=j[g]||j[g-2\
]||j[0];return c\
}};Ic.test(a)||(\
g.cssHooks[a+b].\
set=la)});g.fn.e\
xtend({css:funct\
ion(a,b){return \
Va(this,function\
(a,\x0af,b){var j,c\
={},d=0;if(g.isA\
rray(f)){b=Ra(a)\
;for(j=f.length;\
d<j;d++)c[f[d]]=\
g.css(a,f[d],!1,\
b);return c}retu\
rn void 0!==b?g.\
style(a,f,b):g.c\
ss(a,f)},a,b,1<a\
rguments.length)\
},show:function(\
){return va(this\
,!0)},hide:funct\
ion(){return va(\
this)},toggle:fu\
nction(a){return\
\x22boolean\x22===type\
of a?a?this.show\
():this.hide():t\
his.each(functio\
n(){hb(this)?g(t\
his).show():g(th\
is).hide()})}});\
g.Tween=L;L.prot\
otype={construct\
or:L,init:functi\
on(a,b,j,c,d,n){\
this.elem=a;this\
.prop=j;this.eas\
ing=d||\x22swing\x22;t\
his.options=\x0ab;t\
his.start=this.n\
ow=this.cur();th\
is.end=c;this.un\
it=n||(g.cssNumb\
er[j]?\x22\x22:\x22px\x22)},\
cur:function(){v\
ar a=L.propHooks\
[this.prop];retu\
rn a&&a.get?a.ge\
t(this):L.propHo\
oks._default.get\
(this)},run:func\
tion(a){var b,j=\
L.propHooks[this\
.prop];this.pos=\
this.options.dur\
ation?b=g.easing\
[this.easing](a,\
this.options.dur\
ation*a,0,1,this\
.options.duratio\
n):b=a;this.now=\
(this.end-this.s\
tart)*b+this.sta\
rt;this.options.\
step&&this.optio\
ns.step.call(thi\
s.elem,this.now,\
this);j&&j.set?j\
.set(this):L.pro\
pHooks._default.\
set(this);\x0aretur\
n this}};L.proto\
type.init.protot\
ype=L.prototype;\
L.propHooks={_de\
fault:{get:funct\
ion(a){if(null!=\
a.elem[a.prop]&&\
(!a.elem.style||\
null==a.elem.sty\
le[a.prop]))retu\
rn a.elem[a.prop\
];a=g.css(a.elem\
,a.prop,\x22\x22);retu\
rn!a||\x22auto\x22===a\
?0:a},set:functi\
on(a){if(g.fx.st\
ep[a.prop])g.fx.\
step[a.prop](a);\
else a.elem.styl\
e&&(null!=a.elem\
.style[g.cssProp\
s[a.prop]]||g.cs\
sHooks[a.prop])?\
g.style(a.elem,a\
.prop,a.now+a.un\
it):a.elem[a.pro\
p]=a.now}}};L.pr\
opHooks.scrollTo\
p=L.propHooks.sc\
rollLeft={set:fu\
nction(a){a.elem\
.nodeType&&\x0aa.el\
em.parentNode&&(\
a.elem[a.prop]=a\
.now)}};g.easing\
={linear:functio\
n(a){return a},s\
wing:function(a)\
{return 0.5-Math\
.cos(a*Math.PI)/\
2}};g.fx=L.proto\
type.init;g.fx.s\
tep={};var Za,Hb\
,Jd=/^(?:toggle|\
show|hide)$/,Kc=\
RegExp(\x22^(?:([+-\
])=|)(\x22+zb+\x22)([a\
-z%]*)$\x22,\x22i\x22),Kd\
=/queueHooks$/,t\
b=[function(a,b,\
j){var c,d,n,e,r\
,k,l=this,h={},t\
=a.style,B=a.nod\
eType&&hb(a),z=g\
._data(a,\x22fxshow\
\x22);j.queue||(e=g\
._queueHooks(a,\x22\
fx\x22),null==e.unq\
ueued&&(e.unqueu\
ed=0,r=e.empty.f\
ire,e.empty.fire\
=function(){e.un\
queued||r()}),e.\
unqueued++,\x0al.al\
ways(function(){\
l.always(functio\
n(){e.unqueued--\
;g.queue(a,\x22fx\x22)\
.length||e.empty\
.fire()})}));if(\
1===a.nodeType&&\
(\x22height\x22in b||\x22\
width\x22in b))j.ov\
erflow=[t.overfl\
ow,t.overflowX,t\
.overflowY],d=g.\
css(a,\x22display\x22)\
,k=db(a.nodeName\
),\x22none\x22===d&&(d\
=k),\x22inline\x22===d\
&&\x22none\x22===g.css\
(a,\x22float\x22)&&(!v\
.inlineBlockNeed\
sLayout||\x22inline\
\x22===k?t.display=\
\x22inline-block\x22:t\
.zoom=1);j.overf\
low&&(t.overflow\
=\x22hidden\x22,v.shri\
nkWrapBlocks()||\
l.always(functio\
n(){t.overflow=j\
.overflow[0];t.o\
verflowX=j.overf\
low[1];t.overflo\
wY=\x0aj.overflow[2\
]}));for(c in b)\
if(d=b[c],Jd.exe\
c(d)){delete b[c\
];n=n||\x22toggle\x22=\
==d;if(d===(B?\x22h\
ide\x22:\x22show\x22))if(\
\x22show\x22===d&&z&&v\
oid 0!==z[c])B=!\
0;else continue;\
h[c]=z&&z[c]||g.\
style(a,c)}if(!g\
.isEmptyObject(h\
))for(c in z?\x22hi\
dden\x22in z&&(B=z.\
hidden):z=g._dat\
a(a,\x22fxshow\x22,{})\
,n&&(z.hidden=!B\
),B?g(a).show():\
l.done(function(\
){g(a).hide()}),\
l.done(function(\
){var b;g._remov\
eData(a,\x22fxshow\x22\
);for(b in h)g.s\
tyle(a,b,h[b])})\
,h)b=wa(B?z[c]:0\
,c,l),c in z||(z\
[c]=b.start,B&&(\
b.end=b.start,b.\
start=\x22width\x22===\
c||\x22height\x22===\x0ac\
?1:0))}],ib={\x22*\x22\
:[function(a,b){\
var j=this.creat\
eTween(a,b),c=j.\
cur(),d=Kc.exec(\
b),n=d&&d[3]||(g\
.cssNumber[a]?\x22\x22\
:\x22px\x22),e=(g.cssN\
umber[a]||\x22px\x22!=\
=n&&+c)&&Kc.exec\
(g.css(j.elem,a)\
),r=1,k=20;if(e&\
&e[3]!==n){n=n||\
e[3];d=d||[];e=+\
c||1;do r=r||\x22.5\
\x22,e/=r,g.style(j\
.elem,a,e+n);whi\
le(r!==(r=j.cur(\
)/c)&&1!==r&&--k\
)}d&&(e=j.start=\
+e||+c||0,j.unit\
=n,j.end=d[1]?e+\
(d[1]+1)*d[2]:+d\
[2]);return j}]}\
;g.Animation=g.e\
xtend(jb,{tweene\
r:function(a,b){\
g.isFunction(a)?\
(b=a,a=[\x22*\x22]):a=\
a.split(\x22 \x22);for\
(var j,c=0,d=a.l\
ength;c<\x0ad;c++)j\
=a[c],ib[j]=ib[j\
]||[],ib[j].unsh\
ift(b)},prefilte\
r:function(a,b){\
b?tb.unshift(a):\
tb.push(a)}});g.\
speed=function(a\
,b,j){var c=a&&\x22\
object\x22===typeof\
 a?g.extend({},a\
):{complete:j||!\
j&&b||g.isFuncti\
on(a)&&a,duratio\
n:a,easing:j&&b|\
|b&&!g.isFunctio\
n(b)&&b};c.durat\
ion=g.fx.off?0:\x22\
number\x22===typeof\
 c.duration?c.du\
ration:c.duratio\
n in g.fx.speeds\
?g.fx.speeds[c.d\
uration]:g.fx.sp\
eeds._default;if\
(null==c.queue||\
!0===c.queue)c.q\
ueue=\x22fx\x22;c.old=\
c.complete;c.com\
plete=function()\
{g.isFunction(c.\
old)&&c.old.call\
(this);\x0ac.queue&\
&g.dequeue(this,\
c.queue)};return\
 c};g.fn.extend(\
{fadeTo:function\
(a,b,j,c){return\
 this.filter(hb)\
.css(\x22opacity\x22,0\
).show().end().a\
nimate({opacity:\
b},a,j,c)},anima\
te:function(a,b,\
j,c){var d=g.isE\
mptyObject(a),n=\
g.speed(b,j,c);b\
=function(){var \
b=jb(this,g.exte\
nd({},a),n);(d||\
g._data(this,\x22fi\
nish\x22))&&b.stop(\
!0)};b.finish=b;\
return d||!1===n\
.queue?this.each\
(b):this.queue(n\
.queue,b)},stop:\
function(a,b,j){\
var c=function(a\
){var b=a.stop;d\
elete a.stop;b(j\
)};\x22string\x22!==ty\
peof a&&(j=b,b=a\
,a=void 0);b&&\x0a!\
1!==a&&this.queu\
e(a||\x22fx\x22,[]);re\
turn this.each(f\
unction(){var b=\
!0,d=null!=a&&a+\
\x22queueHooks\x22,n=g\
.timers,e=g._dat\
a(this);if(d)e[d\
]&&e[d].stop&&c(\
e[d]);else for(d\
 in e)e[d]&&(e[d\
].stop&&Kd.test(\
d))&&c(e[d]);for\
(d=n.length;d--;\
)if(n[d].elem===\
this&&(null==a||\
n[d].queue===a))\
n[d].anim.stop(j\
),b=!1,n.splice(\
d,1);(b||!j)&&g.\
dequeue(this,a)}\
)},finish:functi\
on(a){!1!==a&&(a\
=a||\x22fx\x22);return\
 this.each(funct\
ion(){var b,j=g.\
_data(this),c=j[\
a+\x22queue\x22];b=j[a\
+\x22queueHooks\x22];v\
ar d=g.timers,n=\
c?c.length:0;j.f\
inish=\x0a!0;g.queu\
e(this,a,[]);b&&\
b.stop&&b.stop.c\
all(this,!0);for\
(b=d.length;b--;\
)d[b].elem===thi\
s&&d[b].queue===\
a&&(d[b].anim.st\
op(!0),d.splice(\
b,1));for(b=0;b<\
n;b++)c[b]&&c[b]\
.finish&&c[b].fi\
nish.call(this);\
delete j.finish}\
)}});g.each([\x22to\
ggle\x22,\x22show\x22,\x22hi\
de\x22],function(a,\
b){var j=g.fn[b]\
;g.fn[b]=functio\
n(a,f,c){return \
null==a||\x22boolea\
n\x22===typeof a?j.\
apply(this,argum\
ents):this.anima\
te(O(b,!0),a,f,c\
)}});g.each({sli\
deDown:O(\x22show\x22)\
,slideUp:O(\x22hide\
\x22),slideToggle:O\
(\x22toggle\x22),fadeI\
n:{opacity:\x22show\
\x22},fadeOut:{opac\
ity:\x22hide\x22},\x0afad\
eToggle:{opacity\
:\x22toggle\x22}},func\
tion(a,b){g.fn[a\
]=function(a,f,j\
){return this.an\
imate(b,a,f,j)}}\
);g.timers=[];g.\
fx.tick=function\
(){var a,b=g.tim\
ers,j=0;for(Za=g\
.now();j<b.lengt\
h;j++)a=b[j],!a(\
)&&b[j]===a&&b.s\
plice(j--,1);b.l\
ength||g.fx.stop\
();Za=void 0};g.\
fx.timer=functio\
n(a){g.timers.pu\
sh(a);a()?g.fx.s\
tart():g.timers.\
pop()};g.fx.inte\
rval=13;g.fx.sta\
rt=function(){Hb\
||(Hb=setInterva\
l(g.fx.tick,g.fx\
.interval))};g.f\
x.stop=function(\
){clearInterval(\
Hb);Hb=null};g.f\
x.speeds={slow:6\
00,fast:200,_def\
ault:400};\x0ag.fn.\
delay=function(a\
,b){a=g.fx?g.fx.\
speeds[a]||a:a;r\
eturn this.queue\
(b||\x22fx\x22,functio\
n(b,j){var c=set\
Timeout(b,a);j.s\
top=function(){c\
learTimeout(c)}}\
)};var Ib,Ma,fc,\
gc,qb=y.createEl\
ement(\x22div\x22);qb.\
setAttribute(\x22cl\
assName\x22,\x22t\x22);qb\
.innerHTML=\x22  <l\
ink/><table></ta\
ble><a href='/a'\
>a</a><input typ\
e='checkbox'/>\x22;\
Ib=qb.getElement\
sByTagName(\x22a\x22)[\
0];fc=y.createEl\
ement(\x22select\x22);\
gc=fc.appendChil\
d(y.createElemen\
t(\x22option\x22));Ma=\
qb.getElementsBy\
TagName(\x22input\x22)\
[0];Ib.style.css\
Text=\x22top:1px\x22;v\
.getSetAttribute\
=\x0a\x22t\x22!==qb.class\
Name;v.style=/to\
p/.test(Ib.getAt\
tribute(\x22style\x22)\
);v.hrefNormaliz\
ed=\x22/a\x22===Ib.get\
Attribute(\x22href\x22\
);v.checkOn=!!Ma\
.value;v.optSele\
cted=gc.selected\
;v.enctype=!!y.c\
reateElement(\x22fo\
rm\x22).enctype;fc.\
disabled=!0;v.op\
tDisabled=!gc.di\
sabled;Ma=y.crea\
teElement(\x22input\
\x22);Ma.setAttribu\
te(\x22value\x22,\x22\x22);v\
.input=\x22\x22===Ma.g\
etAttribute(\x22val\
ue\x22);Ma.value=\x22t\
\x22;Ma.setAttribut\
e(\x22type\x22,\x22radio\x22\
);v.radioValue=\x22\
t\x22===Ma.value;va\
r Ld=/\x5cr/g;g.fn.\
extend({val:func\
tion(a){var b,j,\
c,d=this[0];if(a\
rguments.length)\
return c=\x0ag.isFu\
nction(a),this.e\
ach(function(j){\
if(1===this.node\
Type&&(j=c?a.cal\
l(this,j,g(this)\
.val()):a,null==\
j?j=\x22\x22:\x22number\x22=\
==typeof j?j+=\x22\x22\
:g.isArray(j)&&(\
j=g.map(j,functi\
on(a){return nul\
l==a?\x22\x22:a+\x22\x22})),\
b=g.valHooks[thi\
s.type]||g.valHo\
oks[this.nodeNam\
e.toLowerCase()]\
,!b||!(\x22set\x22in b\
)||void 0===b.se\
t(this,j,\x22value\x22\
)))this.value=j}\
);if(d){if((b=g.\
valHooks[d.type]\
||g.valHooks[d.n\
odeName.toLowerC\
ase()])&&\x22get\x22in\
 b&&void 0!==(j=\
b.get(d,\x22value\x22)\
))return j;j=d.v\
alue;return\x22stri\
ng\x22===typeof j?j\
.replace(Ld,\x22\x22):\
\x0anull==j?\x22\x22:j}}}\
);g.extend({valH\
ooks:{option:{ge\
t:function(a){va\
r b=g.find.attr(\
a,\x22value\x22);retur\
n null!=b?b:g.te\
xt(a)}},select:{\
get:function(a){\
for(var b,j=a.op\
tions,c=a.select\
edIndex,d=(a=\x22se\
lect-one\x22===a.ty\
pe||0>c)?null:[]\
,n=a?c+1:j.lengt\
h,e=0>c?n:a?c:0;\
e<n;e++)if(b=j[e\
],(b.selected||e\
===c)&&(v.optDis\
abled?!b.disable\
d:null===b.getAt\
tribute(\x22disable\
d\x22))&&(!b.parent\
Node.disabled||!\
g.nodeName(b.par\
entNode,\x22optgrou\
p\x22))){b=g(b).val\
();if(a)return b\
;d.push(b)}retur\
n d},set:functio\
n(a,b){for(var j\
,c,d=a.options,\x0a\
n=g.makeArray(b)\
,e=d.length;e--;\
)if(c=d[e],0<=g.\
inArray(g.valHoo\
ks.option.get(c)\
,n))try{c.select\
ed=j=!0}catch(r)\
{c.scrollHeight}\
else c.selected=\
!1;j||(a.selecte\
dIndex=-1);retur\
n d}}}});g.each(\
[\x22radio\x22,\x22checkb\
ox\x22],function(){\
g.valHooks[this]\
={set:function(a\
,b){if(g.isArray\
(b))return a.che\
cked=0<=g.inArra\
y(g(a).val(),b)}\
};v.checkOn||(g.\
valHooks[this].g\
et=function(a){r\
eturn null===a.g\
etAttribute(\x22val\
ue\x22)?\x22on\x22:a.valu\
e})});var cb,Lc,\
Na=g.expr.attrHa\
ndle,hc=/^(?:che\
cked|selected)$/\
i,Wa=v.getSetAtt\
ribute,\x0aJb=v.inp\
ut;g.fn.extend({\
attr:function(a,\
b){return Va(thi\
s,g.attr,a,b,1<a\
rguments.length)\
},removeAttr:fun\
ction(a){return \
this.each(functi\
on(){g.removeAtt\
r(this,a)})}});g\
.extend({attr:fu\
nction(a,b,j){va\
r c,d,n=a.nodeTy\
pe;if(a&&!(3===n\
||8===n||2===n))\
{if(typeof a.get\
Attribute===ka)r\
eturn g.prop(a,b\
,j);if(1!==n||!g\
.isXMLDoc(a))b=b\
.toLowerCase(),c\
=g.attrHooks[b]|\
|(g.expr.match.b\
ool.test(b)?Lc:c\
b);if(void 0!==j\
)if(null===j)g.r\
emoveAttr(a,b);e\
lse{if(c&&\x22set\x22i\
n c&&void 0!==(d\
=c.set(a,j,b)))r\
eturn d;a.setAtt\
ribute(b,\x0aj+\x22\x22);\
return j}else{if\
(c&&\x22get\x22in c&&n\
ull!==(d=c.get(a\
,b)))return d;d=\
g.find.attr(a,b)\
;return null==d?\
void 0:d}}},remo\
veAttr:function(\
a,b){var j,c,d=0\
,n=b&&b.match(xa\
);if(n&&1===a.no\
deType)for(;j=n[\
d++];)c=g.propFi\
x[j]||j,g.expr.m\
atch.bool.test(j\
)?Jb&&Wa||!hc.te\
st(j)?a[c]=!1:a[\
g.camelCase(\x22def\
ault-\x22+j)]=a[c]=\
!1:g.attr(a,j,\x22\x22\
),a.removeAttrib\
ute(Wa?j:c)},att\
rHooks:{type:{se\
t:function(a,b){\
if(!v.radioValue\
&&\x22radio\x22===b&&g\
.nodeName(a,\x22inp\
ut\x22)){var j=a.va\
lue;a.setAttribu\
te(\x22type\x22,b);j&&\
(a.value=j);retu\
rn b}}}}});\x0aLc={\
set:function(a,b\
,j){!1===b?g.rem\
oveAttr(a,j):Jb&\
&Wa||!hc.test(j)\
?a.setAttribute(\
!Wa&&g.propFix[j\
]||j,j):a[g.came\
lCase(\x22default-\x22\
+j)]=a[j]=!0;ret\
urn j}};g.each(g\
.expr.match.bool\
.source.match(/\x5c\
w+/g),function(a\
,b){var j=Na[b]|\
|g.find.attr;Na[\
b]=Jb&&Wa||!hc.t\
est(b)?function(\
a,b,f){var c,g;f\
||(g=Na[b],Na[b]\
=c,c=null!=j(a,b\
,f)?b.toLowerCas\
e():null,Na[b]=g\
);return c}:func\
tion(a,b,f){if(!\
f)return a[g.cam\
elCase(\x22default-\
\x22+b)]?b.toLowerC\
ase():null}});if\
(!Jb||!Wa)g.attr\
Hooks.value={set\
:function(a,b,j)\
{if(g.nodeName(a\
,\x0a\x22input\x22))a.def\
aultValue=b;else\
 return cb&&cb.s\
et(a,b,j)}};Wa||\
(cb={set:functio\
n(a,b,j){var c=a\
.getAttributeNod\
e(j);c||a.setAtt\
ributeNode(c=a.o\
wnerDocument.cre\
ateAttribute(j))\
;c.value=b+=\x22\x22;i\
f(\x22value\x22===j||b\
===a.getAttribut\
e(j))return b}},\
Na.id=Na.name=Na\
.coords=function\
(a,b,j){var c;if\
(!j)return(c=a.g\
etAttributeNode(\
b))&&\x22\x22!==c.valu\
e?c.value:null},\
g.valHooks.butto\
n={get:function(\
a,b){var j=a.get\
AttributeNode(b)\
;if(j&&j.specifi\
ed)return j.valu\
e},set:cb.set},g\
.attrHooks.conte\
nteditable={set:\
function(a,\x0ab,j)\
{cb.set(a,\x22\x22===b\
?!1:b,j)}},g.eac\
h([\x22width\x22,\x22heig\
ht\x22],function(a,\
b){g.attrHooks[b\
]={set:function(\
a,f){if(\x22\x22===f)r\
eturn a.setAttri\
bute(b,\x22auto\x22),f\
}}}));v.style||(\
g.attrHooks.styl\
e={get:function(\
a){return a.styl\
e.cssText||void \
0},set:function(\
a,b){return a.st\
yle.cssText=b+\x22\x22\
}});var Md=/^(?:\
input|select|tex\
tarea|button|obj\
ect)$/i,Nd=/^(?:\
a|area)$/i;g.fn.\
extend({prop:fun\
ction(a,b){retur\
n Va(this,g.prop\
,a,b,1<arguments\
.length)},remove\
Prop:function(a)\
{a=g.propFix[a]|\
|a;return this.e\
ach(function(){t\
ry{this[a]=\x0avoid\
 0,delete this[a\
]}catch(b){}})}}\
);g.extend({prop\
Fix:{\x22for\x22:\x22html\
For\x22,\x22class\x22:\x22cl\
assName\x22},prop:f\
unction(a,b,j){v\
ar c,d,n;n=a.nod\
eType;if(a&&!(3=\
==n||8===n||2===\
n)){if(n=1!==n||\
!g.isXMLDoc(a))b\
=g.propFix[b]||b\
,d=g.propHooks[b\
];return void 0!\
==j?d&&\x22set\x22in d\
&&void 0!==(c=d.\
set(a,j,b))?c:a[\
b]=j:d&&\x22get\x22in \
d&&null!==(c=d.g\
et(a,b))?c:a[b]}\
},propHooks:{tab\
Index:{get:funct\
ion(a){var b=g.f\
ind.attr(a,\x22tabi\
ndex\x22);return b?\
parseInt(b,10):M\
d.test(a.nodeNam\
e)||Nd.test(a.no\
deName)&&a.href?\
0:-1}}}});v.href\
Normalized||\x0ag.e\
ach([\x22href\x22,\x22src\
\x22],function(a,b)\
{g.propHooks[b]=\
{get:function(a)\
{return a.getAtt\
ribute(b,4)}}});\
v.optSelected||(\
g.propHooks.sele\
cted={get:functi\
on(a){if(a=a.par\
entNode)a.select\
edIndex,a.parent\
Node&&a.parentNo\
de.selectedIndex\
;return null}});\
g.each(\x22tabIndex\
 readOnly maxLen\
gth cellSpacing \
cellPadding rowS\
pan colSpan useM\
ap frameBorder c\
ontentEditable\x22.\
split(\x22 \x22),funct\
ion(){g.propFix[\
this.toLowerCase\
()]=this});v.enc\
type||(g.propFix\
.enctype=\x22encodi\
ng\x22);var ic=/[\x5ct\
\x5cr\x5cn\x5cf]/g;g.fn.e\
xtend({addClass:\
function(a){var \
b,\x0aj,c,d,n,e=0,r\
=this.length;b=\x22\
string\x22===typeof\
 a&&a;if(g.isFun\
ction(a))return \
this.each(functi\
on(b){g(this).ad\
dClass(a.call(th\
is,b,this.classN\
ame))});if(b)for\
(b=(a||\x22\x22).match\
(xa)||[];e<r;e++\
)if(j=this[e],c=\
1===j.nodeType&&\
(j.className?(\x22 \
\x22+j.className+\x22 \
\x22).replace(ic,\x22 \
\x22):\x22 \x22)){for(n=0\
;d=b[n++];)0>c.i\
ndexOf(\x22 \x22+d+\x22 \x22\
)&&(c+=d+\x22 \x22);c=\
g.trim(c);j.clas\
sName!==c&&(j.cl\
assName=c)}retur\
n this},removeCl\
ass:function(a){\
var b,j,c,d,n,e=\
0,r=this.length;\
b=0===arguments.\
length||\x22string\x22\
===typeof a&&a;i\
f(g.isFunction(a\
))return this.ea\
ch(function(b){g\
(this).removeCla\
ss(a.call(this,\x0a\
b,this.className\
))});if(b)for(b=\
(a||\x22\x22).match(xa\
)||[];e<r;e++)if\
(j=this[e],c=1==\
=j.nodeType&&(j.\
className?(\x22 \x22+j\
.className+\x22 \x22).\
replace(ic,\x22 \x22):\
\x22\x22)){for(n=0;d=b\
[n++];)for(;0<=c\
.indexOf(\x22 \x22+d+\x22\
 \x22);)c=c.replace\
(\x22 \x22+d+\x22 \x22,\x22 \x22);\
c=a?g.trim(c):\x22\x22\
;j.className!==c\
&&(j.className=c\
)}return this},t\
oggleClass:funct\
ion(a,b){var j=t\
ypeof a;return\x22b\
oolean\x22===typeof\
 b&&\x22string\x22===j\
?b?this.addClass\
(a):this.removeC\
lass(a):g.isFunc\
tion(a)?this.eac\
h(function(j){g(\
this).toggleClas\
s(a.call(this,j,\
this.className,b\
),b)}):\x0athis.eac\
h(function(){if(\
\x22string\x22===j)for\
(var b,c=0,d=g(t\
his),n=a.match(x\
a)||[];b=n[c++];\
)d.hasClass(b)?d\
.removeClass(b):\
d.addClass(b);el\
se if(j===ka||\x22b\
oolean\x22===j)this\
.className&&g._d\
ata(this,\x22__clas\
sName__\x22,this.cl\
assName),this.cl\
assName=this.cla\
ssName||!1===a?\x22\
\x22:g._data(this,\x22\
__className__\x22)|\
|\x22\x22})},hasClass:\
function(a){a=\x22 \
\x22+a+\x22 \x22;for(var \
b=0,j=this.lengt\
h;b<j;b++)if(1==\
=this[b].nodeTyp\
e&&0<=(\x22 \x22+this[\
b].className+\x22 \x22\
).replace(ic,\x22 \x22\
).indexOf(a))ret\
urn!0;return!1}}\
);g.each(\x22blur f\
ocus focusin foc\
usout load resiz\
e scroll unload \
click dblclick m\
ousedown mouseup\
 mousemove mouse\
over mouseout mo\
useenter mousele\
ave change selec\
t submit keydown\
 keypress keyup \
error contextmen\
u\x22.split(\x22 \x22),\x0af\
unction(a,b){g.f\
n[b]=function(a,\
f){return 0<argu\
ments.length?thi\
s.on(b,null,a,f)\
:this.trigger(b)\
}});g.fn.extend(\
{hover:function(\
a,b){return this\
.mouseenter(a).m\
ouseleave(b||a)}\
,bind:function(a\
,b,j){return thi\
s.on(a,null,b,j)\
},unbind:functio\
n(a,b){return th\
is.off(a,null,b)\
},delegate:funct\
ion(a,b,j,c){ret\
urn this.on(b,a,\
j,c)},undelegate\
:function(a,b,j)\
{return 1===argu\
ments.length?thi\
s.off(a,\x22**\x22):th\
is.off(b,a||\x22**\x22\
,j)}});var jc=g.\
now(),kc=/\x5c?/,Od\
=/(,)|(\x5c[|{)|(}|\
])|\x22(?:[^\x22\x5c\x5c\x5cr\x5cn\
]|\x5c\x5c[\x22\x5c\x5c\x5c/bfnrt]\
|\x5c\x5cu[\x5cda-fA-F]{4\
})*\x22\x5cs*:?|true|f\
alse|null|-?(?!0\
\x5cd)\x5cd+(?:\x5c.\x5cd+|)\
(?:[eE][+-]?\x5cd+|\
)/g;\x0ag.parseJSON\
=function(b){if(\
a.JSON&&a.JSON.p\
arse)return a.JS\
ON.parse(b+\x22\x22);v\
ar j,c=null,d=g.\
trim(b+\x22\x22);retur\
n d&&!g.trim(d.r\
eplace(Od,functi\
on(a,b,f,g){j&&b\
&&(c=0);if(0===c\
)return a;j=f||b\
;c+=!g-!f;return\
\x22\x22}))?Function(\x22\
return \x22+d)():g.\
error(\x22Invalid J\
SON: \x22+b)};g.par\
seXML=function(b\
){var j,c;if(!b|\
|\x22string\x22!==type\
of b)return null\
;try{a.DOMParser\
?(c=new DOMParse\
r,j=c.parseFromS\
tring(b,\x22text/xm\
l\x22)):(j=new Acti\
veXObject(\x22Micro\
soft.XMLDOM\x22),j.\
async=\x22false\x22,j.\
loadXML(b))}catc\
h(d){j=void 0}(!\
j||!j.documentEl\
ement||\x0aj.getEle\
mentsByTagName(\x22\
parsererror\x22).le\
ngth)&&g.error(\x22\
Invalid XML: \x22+b\
);return j};var \
Xa,Oa,Pd=/#.*$/,\
Mc=/([?&])_=[^&]\
*/,Qd=/^(.*?):[ \
\x5ct]*([^\x5cr\x5cn]*)\x5cr\
?$/mg,Rd=/^(?:GE\
T|HEAD)$/,Sd=/^\x5c\
/\x5c//,Nc=/^([\x5cw.+\
-]+:)(?:\x5c/\x5c/(?:[\
^\x5c/?#]*@|)([^\x5c/?\
#:]*)(?::(\x5cd+)|)\
|)/,Oc={},Nb={},\
Pc=\x22*/\x22.concat(\x22\
*\x22);try{Oa=locat\
ion.href}catch(b\
e){Oa=y.createEl\
ement(\x22a\x22),Oa.hr\
ef=\x22\x22,Oa=Oa.href\
}Xa=Nc.exec(Oa.t\
oLowerCase())||[\
];g.extend({acti\
ve:0,lastModifie\
d:{},etag:{},aja\
xSettings:{url:O\
a,type:\x22GET\x22,isL\
ocal:/^(?:about|\
app|app-storage|\
.+-extension|fil\
e|res|widget):$/\
.test(Xa[1]),\x0agl\
obal:!0,processD\
ata:!0,async:!0,\
contentType:\x22app\
lication/x-www-f\
orm-urlencoded; \
charset=UTF-8\x22,a\
ccepts:{\x22*\x22:Pc,t\
ext:\x22text/plain\x22\
,html:\x22text/html\
\x22,xml:\x22applicati\
on/xml, text/xml\
\x22,json:\x22applicat\
ion/json, text/j\
avascript\x22},cont\
ents:{xml:/xml/,\
html:/html/,json\
:/json/},respons\
eFields:{xml:\x22re\
sponseXML\x22,text:\
\x22responseText\x22,j\
son:\x22responseJSO\
N\x22},converters:{\
\x22* text\x22:String,\
\x22text html\x22:!0,\x22\
text json\x22:g.par\
seJSON,\x22text xml\
\x22:g.parseXML},fl\
atOptions:{url:!\
0,context:!0}},a\
jaxSetup:functio\
n(a,b){return b?\
ya(ya(a,\x0ag.ajaxS\
ettings),b):ya(g\
.ajaxSettings,a)\
},ajaxPrefilter:\
kb(Oc),ajaxTrans\
port:kb(Nb),ajax\
:function(a,b){f\
unction j(a,b,f,\
c){var d,t,p,F;F\
=b;if(2!==da){da\
=2;r&&clearTimeo\
ut(r);l=void 0;e\
=c||\x22\x22;s.readySt\
ate=0<a?4:0;c=20\
0<=a&&300>a||304\
===a;if(f){p=h;f\
or(var w=s,N,ha,\
G,C,Q=p.contents\
,A=p.dataTypes;\x22\
*\x22===A[0];)A.shi\
ft(),void 0===ha\
&&(ha=p.mimeType\
||w.getResponseH\
eader(\x22Content-T\
ype\x22));if(ha)for\
(C in Q)if(Q[C]&\
&Q[C].test(ha)){\
A.unshift(C);bre\
ak}if(A[0]in f)G\
=A[0];else{for(C\
 in f){if(!A[0]|\
|p.converters[C+\
\x0a\x22 \x22+A[0]]){G=C;\
break}N||(N=C)}G\
=G||N}G?(G!==A[0\
]&&A.unshift(G),\
p=f[G]):p=void 0\
}a:{f=h;N=p;ha=s\
;G=c;var K,v,ua,\
w={},Q=f.dataTyp\
es.slice();if(Q[\
1])for(v in f.co\
nverters)w[v.toL\
owerCase()]=f.co\
nverters[v];for(\
C=Q.shift();C;)i\
f(f.responseFiel\
ds[C]&&(ha[f.res\
ponseFields[C]]=\
N),!ua&&(G&&f.da\
taFilter)&&(N=f.\
dataFilter(N,f.d\
ataType)),ua=C,C\
=Q.shift())if(\x22*\
\x22===C)C=ua;else \
if(\x22*\x22!==ua&&ua!\
==C){v=w[ua+\x22 \x22+\
C]||w[\x22* \x22+C];if\
(!v)for(K in w)i\
f(p=K.split(\x22 \x22)\
,p[1]===C&&(v=w[\
ua+\x22 \x22+p[0]]||w[\
\x22* \x22+p[0]])){!0=\
==v?v=\x0aw[K]:!0!=\
=w[K]&&(C=p[0],Q\
.unshift(p[1]));\
break}if(!0!==v)\
if(v&&f[\x22throws\x22\
])N=v(N);else tr\
y{N=v(N)}catch(u\
){p={state:\x22pars\
ererror\x22,error:v\
?u:\x22No conversio\
n from \x22+ua+\x22 to\
 \x22+C};break a}}p\
={state:\x22success\
\x22,data:N}}if(c)h\
.ifModified&&((F\
=s.getResponseHe\
ader(\x22Last-Modif\
ied\x22))&&(g.lastM\
odified[n]=F),(F\
=s.getResponseHe\
ader(\x22etag\x22))&&(\
g.etag[n]=F)),20\
4===a||\x22HEAD\x22===\
h.type?F=\x22nocont\
ent\x22:304===a?F=\x22\
notmodified\x22:(F=\
p.state,d=p.data\
,t=p.error,c=!t)\
;else if(t=F,a||\
!F)F=\x22error\x22,0>a\
&&(a=0);s.status\
=a;s.statusText=\
\x0a(b||F)+\x22\x22;c?T.r\
esolveWith(B,[d,\
F,s]):T.rejectWi\
th(B,[s,F,t]);s.\
statusCode(m);m=\
void 0;k&&z.trig\
ger(c?\x22ajaxSucce\
ss\x22:\x22ajaxError\x22,\
[s,h,c?d:t]);q.f\
ireWith(B,[s,F])\
;k&&(z.trigger(\x22\
ajaxComplete\x22,[s\
,h]),--g.active|\
|g.event.trigger\
(\x22ajaxStop\x22))}}\x22\
object\x22===typeof\
 a&&(b=a,a=void \
0);b=b||{};var c\
,d,n,e,r,k,l,t,h\
=g.ajaxSetup({},\
b),B=h.context||\
h,z=h.context&&(\
B.nodeType||B.jq\
uery)?g(B):g.eve\
nt,T=g.Deferred(\
),q=g.Callbacks(\
\x22once memory\x22),m\
=h.statusCode||{\
},F={},N={},da=0\
,ha=\x22canceled\x22,s\
={readyState:0,g\
etResponseHeader\
:function(a){var\
 b;\x0aif(2===da){i\
f(!t)for(t={};b=\
Qd.exec(e);)t[b[\
1].toLowerCase()\
]=b[2];b=t[a.toL\
owerCase()]}retu\
rn null==b?null:\
b},getAllRespons\
eHeaders:functio\
n(){return 2===d\
a?e:null},setReq\
uestHeader:funct\
ion(a,b){var f=a\
.toLowerCase();d\
a||(a=N[f]=N[f]|\
|a,F[a]=b);retur\
n this},override\
MimeType:functio\
n(a){da||(h.mime\
Type=a);return t\
his},statusCode:\
function(a){var \
b;if(a)if(2>da)f\
or(b in a)m[b]=[\
m[b],a[b]];else \
s.always(a[s.sta\
tus]);return thi\
s},abort:functio\
n(a){a=a||ha;l&&\
l.abort(a);j(0,a\
);return this}};\
T.promise(s).com\
plete=\x0aq.add;s.s\
uccess=s.done;s.\
error=s.fail;h.u\
rl=((a||h.url||O\
a)+\x22\x22).replace(P\
d,\x22\x22).replace(Sd\
,Xa[1]+\x22//\x22);h.t\
ype=b.method||b.\
type||h.method||\
h.type;h.dataTyp\
es=g.trim(h.data\
Type||\x22*\x22).toLow\
erCase().match(x\
a)||[\x22\x22];null==h\
.crossDomain&&(c\
=Nc.exec(h.url.t\
oLowerCase()),h.\
crossDomain=!(!c\
||!(c[1]!==Xa[1]\
||c[2]!==Xa[2]||\
(c[3]||(\x22http:\x22=\
==c[1]?\x2280\x22:\x22443\
\x22))!==(Xa[3]||(\x22\
http:\x22===Xa[1]?\x22\
80\x22:\x22443\x22)))));h\
.data&&(h.proces\
sData&&\x22string\x22!\
==typeof h.data)\
&&(h.data=g.para\
m(h.data,h.tradi\
tional));ub(Oc,h\
,b,s);if(2===\x0ada\
)return s;(k=h.g\
lobal)&&0===g.ac\
tive++&&g.event.\
trigger(\x22ajaxSta\
rt\x22);h.type=h.ty\
pe.toUpperCase()\
;h.hasContent=!R\
d.test(h.type);n\
=h.url;h.hasCont\
ent||(h.data&&(n\
=h.url+=(kc.test\
(n)?\x22&\x22:\x22?\x22)+h.d\
ata,delete h.dat\
a),!1===h.cache&\
&(h.url=Mc.test(\
n)?n.replace(Mc,\
\x22$1_=\x22+jc++):n+(\
kc.test(n)?\x22&\x22:\x22\
?\x22)+\x22_=\x22+jc++));\
h.ifModified&&(g\
.lastModified[n]\
&&s.setRequestHe\
ader(\x22If-Modifie\
d-Since\x22,g.lastM\
odified[n]),g.et\
ag[n]&&s.setRequ\
estHeader(\x22If-No\
ne-Match\x22,g.etag\
[n]));(h.data&&h\
.hasContent&&!1!\
==h.contentType|\
|b.contentType)&\
&\x0as.setRequestHe\
ader(\x22Content-Ty\
pe\x22,h.contentTyp\
e);s.setRequestH\
eader(\x22Accept\x22,h\
.dataTypes[0]&&h\
.accepts[h.dataT\
ypes[0]]?h.accep\
ts[h.dataTypes[0\
]]+(\x22*\x22!==h.data\
Types[0]?\x22, \x22+Pc\
+\x22; q=0.01\x22:\x22\x22):\
h.accepts[\x22*\x22]);\
for(d in h.heade\
rs)s.setRequestH\
eader(d,h.header\
s[d]);if(h.befor\
eSend&&(!1===h.b\
eforeSend.call(B\
,s,h)||2===da))r\
eturn s.abort();\
ha=\x22abort\x22;for(d\
 in{success:1,er\
ror:1,complete:1\
})s[d](h[d]);if(\
l=ub(Nb,h,b,s)){\
s.readyState=1;k\
&&z.trigger(\x22aja\
xSend\x22,[s,h]);h.\
async&&0<h.timeo\
ut&&(r=setTimeou\
t(function(){s.a\
bort(\x22timeout\x22)}\
,\x0ah.timeout));tr\
y{da=1,l.send(F,\
j)}catch(G){if(2\
>da)j(-1,G);else\
 throw G;}}else \
j(-1,\x22No Transpo\
rt\x22);return s},g\
etJSON:function(\
a,b,j){return g.\
get(a,b,j,\x22json\x22\
)},getScript:fun\
ction(a,b){retur\
n g.get(a,void 0\
,b,\x22script\x22)}});\
g.each([\x22get\x22,\x22p\
ost\x22],function(a\
,b){g[b]=functio\
n(a,f,j,c){g.isF\
unction(f)&&(c=c\
||j,j=f,f=void 0\
);return g.ajax(\
{url:a,type:b,da\
taType:c,data:f,\
success:j})}});g\
.each(\x22ajaxStart\
 ajaxStop ajaxCo\
mplete ajaxError\
 ajaxSuccess aja\
xSend\x22.split(\x22 \x22\
),function(a,b){\
g.fn[b]=function\
(a){return this.\
on(b,\x0aa)}});g._e\
valUrl=function(\
a){return g.ajax\
({url:a,type:\x22GE\
T\x22,dataType:\x22scr\
ipt\x22,async:!1,gl\
obal:!1,\x22throws\x22\
:!0})};g.fn.exte\
nd({wrapAll:func\
tion(a){if(g.isF\
unction(a))retur\
n this.each(func\
tion(b){g(this).\
wrapAll(a.call(t\
his,b))});if(thi\
s[0]){var b=g(a,\
this[0].ownerDoc\
ument).eq(0).clo\
ne(!0);this[0].p\
arentNode&&b.ins\
ertBefore(this[0\
]);b.map(functio\
n(){for(var a=th\
is;a.firstChild&\
&1===a.firstChil\
d.nodeType;)a=a.\
firstChild;retur\
n a}).append(thi\
s)}return this},\
wrapInner:functi\
on(a){return g.i\
sFunction(a)?\x0ath\
is.each(function\
(b){g(this).wrap\
Inner(a.call(thi\
s,b))}):this.eac\
h(function(){var\
 b=g(this),j=b.c\
ontents();j.leng\
th?j.wrapAll(a):\
b.append(a)})},w\
rap:function(a){\
var b=g.isFuncti\
on(a);return thi\
s.each(function(\
j){g(this).wrapA\
ll(b?a.call(this\
,j):a)})},unwrap\
:function(){retu\
rn this.parent()\
.each(function()\
{g.nodeName(this\
,\x22body\x22)||g(this\
).replaceWith(th\
is.childNodes)})\
.end()}});g.expr\
.filters.hidden=\
function(a){retu\
rn 0>=a.offsetWi\
dth&&0>=a.offset\
Height||!v.relia\
bleHiddenOffsets\
()&&\x22none\x22===(a.\
style&&\x0aa.style.\
display||g.css(a\
,\x22display\x22))};g.\
expr.filters.vis\
ible=function(a)\
{return!g.expr.f\
ilters.hidden(a)\
};var Td=/%20/g,\
ad=/\x5c[\x5c]$/,Qc=/\x5c\
r?\x5cn/g,Ud=/^(?:s\
ubmit|button|ima\
ge|reset|file)$/\
i,Vd=/^(?:input|\
select|textarea|\
keygen)/i;g.para\
m=function(a,b){\
var j,c=[],d=fun\
ction(a,b){b=g.i\
sFunction(b)?b()\
:null==b?\x22\x22:b;c[\
c.length]=encode\
URIComponent(a)+\
\x22=\x22+encodeURICom\
ponent(b)};void \
0===b&&(b=g.ajax\
Settings&&g.ajax\
Settings.traditi\
onal);if(g.isArr\
ay(a)||a.jquery&\
&!g.isPlainObjec\
t(a))g.each(a,fu\
nction(){d(this.\
name,\x0athis.value\
)});else for(j i\
n a)ma(j,a[j],b,\
d);return c.join\
(\x22&\x22).replace(Td\
,\x22+\x22)};g.fn.exte\
nd({serialize:fu\
nction(){return \
g.param(this.ser\
ializeArray())},\
serializeArray:f\
unction(){return\
 this.map(functi\
on(){var a=g.pro\
p(this,\x22elements\
\x22);return a?g.ma\
keArray(a):this}\
).filter(functio\
n(){var a=this.t\
ype;return this.\
name&&!g(this).i\
s(\x22:disabled\x22)&&\
Vd.test(this.nod\
eName)&&!Ud.test\
(a)&&(this.check\
ed||!Mb.test(a))\
}).map(function(\
a,b){var j=g(thi\
s).val();return \
null==j?null:g.i\
sArray(j)?g.map(\
j,function(a){re\
turn{name:b.name\
,\x0avalue:a.replac\
e(Qc,\x22\x5cr\x5cn\x22)}}):\
{name:b.name,val\
ue:j.replace(Qc,\
\x22\x5cr\x5cn\x22)}}).get()\
}});g.ajaxSettin\
gs.xhr=void 0!==\
a.ActiveXObject?\
function(){var b\
;if(!(b=!this.is\
Local&&/^(get|po\
st|head|put|dele\
te|options)$/i.t\
est(this.type)&&\
aa()))a:{try{b=n\
ew a.ActiveXObje\
ct(\x22Microsoft.XM\
LHTTP\x22);break a}\
catch(j){}b=void\
 0}return b}:aa;\
g.ajaxSettings.x\
hr=void 0===a.Ac\
tiveXObject?D:fu\
nction(){return(\
this.url==y.loca\
tion||0==this.ur\
l.indexOf(\x22http\x22\
)||!this.isLocal\
)&&/^(get|post|h\
ead|put|delete|o\
ptions)$/i.test(\
this.type)&&\x0aD()\
||D(1)};var Wd=0\
,Kb={},Lb=g.ajax\
Settings.xhr();i\
f(a.ActiveXObjec\
t)g(a).on(\x22unloa\
d\x22,function(){fo\
r(var a in Kb)Kb\
[a](void 0,!0)})\
;v.cors=!!Lb&&\x22w\
ithCredentials\x22i\
n Lb;(Lb=v.ajax=\
!!Lb)&&g.ajaxTra\
nsport(function(\
a){if(!a.crossDo\
main||v.cors){va\
r b;return{send:\
function(j,c){va\
r d,n=a.xhr(),e=\
++Wd;console.log\
(\x22xhr.open async\
=\x22+a.async+\x22 url\
=\x22+a.url);n.open\
(a.type,a.url,a.\
async,a.username\
,a.password);if(\
a.xhrFields)for(\
d in a.xhrFields\
)n[d]=a.xhrField\
s[d];a.mimeType&\
&n.overrideMimeT\
ype&&n.overrideM\
imeType(a.mimeTy\
pe);\x0a!a.crossDom\
ain&&!j[\x22X-Reque\
sted-With\x22]&&(j[\
\x22X-Requested-Wit\
h\x22]=\x22XMLHttpRequ\
est\x22);for(d in j\
)void 0!==j[d]&&\
n.setRequestHead\
er(d,j[d]+\x22\x22);n.\
send(a.hasConten\
t&&a.data||null)\
;b=function(j,d)\
{var r,h,k;if(b&\
&(d||4===n.ready\
State))if(delete\
 Kb[e],b=void 0,\
n.onreadystatech\
ange=g.noop,d)4!\
==n.readyState&&\
n.abort();else{k\
={};r=n.status;\x22\
string\x22===typeof\
 n.responseText&\
&(k.text=n.respo\
nseText);try{h=n\
.statusText}catc\
h(l){h=\x22\x22}!r&&a.\
isLocal&&!a.cros\
sDomain?r=k.text\
?200:404:1223===\
r&&(r=204)}k&&c(\
r,h,k,n.getAllRe\
sponseHeaders())\
};\x0aa.async?4===n\
.readyState?setT\
imeout(b):n.onre\
adystatechange=K\
b[e]=b:b()},abor\
t:function(){b&&\
b(void 0,!0)}}}}\
);g.ajaxSetup({a\
ccepts:{script:\x22\
text/javascript,\
 application/jav\
ascript, applica\
tion/ecmascript,\
 application/x-e\
cmascript\x22},cont\
ents:{script:/(?\
:java|ecma)scrip\
t/},converters:{\
\x22text script\x22:fu\
nction(a){g.glob\
alEval(a);return\
 a}}});g.ajaxPre\
filter(\x22script\x22,\
function(a){void\
 0===a.cache&&(a\
.cache=!1);a.cro\
ssDomain&&(a.typ\
e=\x22GET\x22,a.global\
=!1)});g.ajaxTra\
nsport(\x22script\x22,\
function(a){if(a\
.crossDomain){va\
r b,\x0aj=y.head||g\
(\x22head\x22)[0]||y.d\
ocumentElement;r\
eturn{send:funct\
ion(c,g){b=y.cre\
ateElement(\x22scri\
pt\x22);b.async=!0;\
a.scriptCharset&\
&(b.charset=a.sc\
riptCharset);b.s\
rc=a.url;b.onloa\
d=b.onreadystate\
change=function(\
a,j){if(j||!b.re\
adyState||/loade\
d|complete/.test\
(b.readyState))b\
.onload=b.onread\
ystatechange=nul\
l,b.parentNode&&\
b.parentNode.rem\
oveChild(b),b=nu\
ll,j||g(200,\x22suc\
cess\x22)};j.insert\
Before(b,j.first\
Child)},abort:fu\
nction(){if(b)b.\
onload(void 0,!0\
)}}}});var Rc=[]\
,lc=/(=)\x5c?(?=&|$\
)|\x5c?\x5c?/;g.ajaxSe\
tup({jsonp:\x22call\
back\x22,\x0ajsonpCall\
back:function(){\
var a=Rc.pop()||\
g.expando+\x22_\x22+jc\
++;this[a]=!0;re\
turn a}});g.ajax\
Prefilter(\x22json \
jsonp\x22,function(\
b,j,c){var d,n,e\
,r=!1!==b.jsonp&\
&(lc.test(b.url)\
?\x22url\x22:\x22string\x22=\
==typeof b.data&\
&!(b.contentType\
||\x22\x22).indexOf(\x22a\
pplication/x-www\
-form-urlencoded\
\x22)&&lc.test(b.da\
ta)&&\x22data\x22);if(\
r||\x22jsonp\x22===b.d\
ataTypes[0])retu\
rn d=b.jsonpCall\
back=g.isFunctio\
n(b.jsonpCallbac\
k)?b.jsonpCallba\
ck():b.jsonpCall\
back,r?b[r]=b[r]\
.replace(lc,\x22$1\x22\
+d):!1!==b.jsonp\
&&(b.url+=(kc.te\
st(b.url)?\x22&\x22:\x22?\
\x22)+b.jsonp+\x22=\x22+\x0a\
d),b.converters[\
\x22script json\x22]=f\
unction(){e||g.e\
rror(d+\x22 was not\
 called\x22);return\
 e[0]},b.dataTyp\
es[0]=\x22json\x22,n=a\
[d],a[d]=functio\
n(){e=arguments}\
,c.always(functi\
on(){a[d]=n;b[d]\
&&(b.jsonpCallba\
ck=j.jsonpCallba\
ck,Rc.push(d));e\
&&g.isFunction(n\
)&&n(e[0]);e=n=v\
oid 0}),\x22script\x22\
});g.parseHTML=f\
unction(a,b,j){i\
f(!a||\x22string\x22!=\
=typeof a)return\
 null;\x22boolean\x22=\
==typeof b&&(j=b\
,b=!1);b=b||y;va\
r c=xc.exec(a);j\
=!j&&[];if(c)ret\
urn[b.createElem\
ent(c[1])];c=g.b\
uildFragment([a]\
,b,j);j&&j.lengt\
h&&g(j).remove()\
;return g.merge(\
[],\x0ac.childNodes\
)};var Sc=g.fn.l\
oad;g.fn.load=fu\
nction(a,b,j){if\
(\x22string\x22!==type\
of a&&Sc)return \
Sc.apply(this,ar\
guments);var c,d\
,n,e=this,r=a.in\
dexOf(\x22 \x22);0<=r&\
&(c=a.slice(r,a.\
length),a=a.slic\
e(0,r));g.isFunc\
tion(b)?(j=b,b=v\
oid 0):b&&\x22objec\
t\x22===typeof b&&(\
n=\x22POST\x22);0<e.le\
ngth&&g.ajax({ur\
l:a,type:n,dataT\
ype:\x22html\x22,data:\
b}).done(functio\
n(a){d=arguments\
;e.html(c?g(\x22<di\
v>\x22).append(g.pa\
rseHTML(a)).find\
(c):a)}).complet\
e(j&&function(a,\
b){e.each(j,d||[\
a.responseText,b\
,a])});return th\
is};g.expr.filte\
rs.animated=\x0afun\
ction(a){return \
g.grep(g.timers,\
function(b){retu\
rn a===b.elem}).\
length};var Tc=a\
.document.docume\
ntElement;g.offs\
et={setOffset:fu\
nction(a,b,j){va\
r c,d,n,e=g.css(\
a,\x22position\x22),r=\
g(a),h={};\x22stati\
c\x22===e&&(a.style\
.position=\x22relat\
ive\x22);n=r.offset\
();d=g.css(a,\x22to\
p\x22);c=g.css(a,\x22l\
eft\x22);(\x22absolute\
\x22===e||\x22fixed\x22==\
=e)&&-1<g.inArra\
y(\x22auto\x22,[d,c])?\
(c=r.position(),\
d=c.top,c=c.left\
):(d=parseFloat(\
d)||0,c=parseFlo\
at(c)||0);g.isFu\
nction(b)&&(b=b.\
call(a,j,n));nul\
l!=b.top&&(h.top\
=b.top-n.top+d);\
null!=b.left&&(h\
.left=\x0ab.left-n.\
left+c);\x22using\x22i\
n b?b.using.call\
(a,h):r.css(h)}}\
;g.fn.extend({of\
fset:function(a)\
{if(arguments.le\
ngth)return void\
 0===a?this:this\
.each(function(b\
){g.offset.setOf\
fset(this,a,b)})\
;var b,j,c={top:\
0,left:0},d=(j=t\
his[0])&&j.owner\
Document;if(d){b\
=d.documentEleme\
nt;if(!g.contain\
s(b,j))return c;\
typeof j.getBoun\
dingClientRect!=\
=ka&&(c=j.getBou\
ndingClientRect(\
));j=V(d);return\
{top:c.top+(j.pa\
geYOffset||b.scr\
ollTop)-(b.clien\
tTop||0),left:c.\
left+(j.pageXOff\
set||b.scrollLef\
t)-(b.clientLeft\
||0)}}},position\
:function(){if(t\
his[0]){var a,\x0ab\
,j={top:0,left:0\
},c=this[0];\x22fix\
ed\x22===g.css(c,\x22p\
osition\x22)?b=c.ge\
tBoundingClientR\
ect():(a=this.of\
fsetParent(),b=t\
his.offset(),g.n\
odeName(a[0],\x22ht\
ml\x22)||(j=a.offse\
t()),j.top+=g.cs\
s(a[0],\x22borderTo\
pWidth\x22,!0),j.le\
ft+=g.css(a[0],\x22\
borderLeftWidth\x22\
,!0));return{top\
:b.top-j.top-g.c\
ss(c,\x22marginTop\x22\
,!0),left:b.left\
-j.left-g.css(c,\
\x22marginLeft\x22,!0)\
}}},offsetParent\
:function(){retu\
rn this.map(func\
tion(){for(var a\
=this.offsetPare\
nt||Tc;a&&!g.nod\
eName(a,\x22html\x22)&\
&\x22static\x22===g.cs\
s(a,\x22position\x22);\
)a=a.offsetParen\
t;return a||\x0aTc}\
)}});g.each({scr\
ollLeft:\x22pageXOf\
fset\x22,scrollTop:\
\x22pageYOffset\x22},f\
unction(a,b){var\
 j=/Y/.test(b);g\
.fn[a]=function(\
c){return Va(thi\
s,function(a,c,f\
){var d=V(a);if(\
void 0===f)retur\
n d?b in d?d[b]:\
d.document.docum\
entElement[c]:a[\
c];d?d.scrollTo(\
!j?f:g(d).scroll\
Left(),j?f:g(d).\
scrollTop()):a[c\
]=f},a,c,argumen\
ts.length,null)}\
});g.each([\x22top\x22\
,\x22left\x22],functio\
n(a,b){g.cssHook\
s[b]=fb(v.pixelP\
osition,function\
(a,j){if(j)retur\
n j=Sa(a,b),sb.t\
est(j)?g(a).posi\
tion()[b]+\x22px\x22:j\
})});g.each({Hei\
ght:\x22height\x22,Wid\
th:\x22width\x22},\x0afun\
ction(a,b){g.eac\
h({padding:\x22inne\
r\x22+a,content:b,\x22\
\x22:\x22outer\x22+a},fun\
ction(j,c){g.fn[\
c]=function(c,d)\
{var n=arguments\
.length&&(j||\x22bo\
olean\x22!==typeof \
c),e=j||(!0===c|\
|!0===d?\x22margin\x22\
:\x22border\x22);retur\
n Va(this,functi\
on(b,j,c){return\
 g.isWindow(b)?b\
.document.docume\
ntElement[\x22clien\
t\x22+a]:9===b.node\
Type?(j=b.docume\
ntElement,Math.m\
ax(b.body[\x22scrol\
l\x22+a],j[\x22scroll\x22\
+a],b.body[\x22offs\
et\x22+a],j[\x22offset\
\x22+a],j[\x22client\x22+\
a])):void 0===c?\
g.css(b,j,e):g.s\
tyle(b,j,c,e)},b\
,n?c:void 0,n,nu\
ll)}})});g.fn.si\
ze=function(){re\
turn this.length\
};\x0ag.fn.andSelf=\
g.fn.addBack;\x22fu\
nction\x22===typeof\
 define&&define.\
amd&&define(\x22jqu\
ery\x22,[],function\
(){return g});va\
r Xd=a.jQuery,Yd\
=a.$;g.noConflic\
t=function(b){a.\
$===g&&(a.$=Yd);\
b&&a.jQuery===g&\
&(a.jQuery=Xd);r\
eturn g};typeof \
m===ka&&(a.jQuer\
y=a.$=g);return \
g});\x0a(function(a\
){function m(a){\
try{return a?new\
 window.ActiveXO\
bject(\x22Microsoft\
.XMLHTTP\x22):new w\
indow.XMLHttpReq\
uest}catch(h){}}\
a.ajaxSettings.x\
hr=void 0===wind\
ow.ActiveXObject\
?m:function(){re\
turn(this.url==d\
ocument.location\
||0==this.url.in\
dexOf(\x22http\x22)||!\
this.isLocal)&&/\
^(get|post|head|\
put|delete|optio\
ns)$/i.test(this\
.type)&&m()||m(1\
)};a.ajaxTranspo\
rt(\x22+script\x22,fun\
ction(a){var h,e\
=document.head||\
jQuery(\x22head\x22)[0\
]||document.docu\
mentElement;retu\
rn{send:function\
(l,q){h=document\
.createElement(\x22\
script\x22);a.scrip\
tCharset&&\x0a(h.ch\
arset=a.scriptCh\
arset);h.src=a.u\
rl;h.onload=h.on\
readystatechange\
=function(a,e){i\
f(e||!h.readySta\
te||/loaded|comp\
lete/.test(h.rea\
dyState))h.onloa\
d=h.onreadystate\
change=null,h.pa\
rentNode&&h.pare\
ntNode.removeChi\
ld(h),h=null,e||\
q(200,\x22success\x22)\
};e.insertBefore\
(h,e.firstChild)\
},abort:function\
(){if(h)h.onload\
(void 0,!0)}}});\
a.extend(a.suppo\
rt,{iecors:!!win\
dow.XDomainReque\
st});a.support.i\
ecors?a.ajaxTran\
sport(function(a\
){return{send:fu\
nction(h,e){var \
l=new window.XDo\
mainRequest;l.on\
load=function(){\
e(200,\x0a\x22OK\x22,{tex\
t:l.responseText\
},{\x22Content-Type\
\x22:l.contentType}\
)};a.xhrFields&&\
(l.onerror=a.xhr\
Fields.error,l.o\
ntimeout=a.xhrFi\
elds.timeout);l.\
open(a.type,a.ur\
l);l.send(a.hasC\
ontent&&a.data||\
null)},abort:fun\
ction(){xdr.abor\
t()}}}):(a.ajaxS\
etup({accepts:{b\
inary:\x22text/plai\
n; charset=x-use\
r-defined\x22},resp\
onseFields:{bina\
ry:\x22response\x22}})\
,a.ajaxTransport\
(\x22binary\x22,functi\
on(a){var h;retu\
rn{send:function\
(e,l){var q=a.xh\
r();console.log(\
\x22xhr.open binary\
 async=\x22+a.async\
+\x22 url=\x22+a.url);\
q.open(a.type,a.\
url,a.async);\x0ava\
r m=!1;try{q.has\
OwnProperty(\x22res\
ponseType\x22)&&(q.\
responseType=\x22ar\
raybuffer\x22,m=!0)\
}catch(u){}try{!\
m&&q.overrideMim\
eType&&q.overrid\
eMimeType(\x22text/\
plain; charset=x\
-user-defined\x22)}\
catch(b){}!a.cro\
ssDomain&&!e[\x22X-\
Requested-With\x22]\
&&(e[\x22X-Requeste\
d-With\x22]=\x22XMLHtt\
pRequest\x22);try{f\
or(var c in e)q.\
setRequestHeader\
(c,e[c])}catch(d\
){}q.send(a.hasC\
ontent&&a.data||\
null);h=function\
(){var b=q.statu\
s,c=\x22\x22,d=q.getAl\
lResponseHeaders\
(),e={};try{if(h\
&&4===q.readySta\
te){h=void 0;try\
{e.text=\x22string\x22\
===typeof q.resp\
onseText?\x0aq.resp\
onseText:null}ca\
tch(m){}try{e.bi\
nary=q.response}\
catch(s){}try{c=\
q.statusText}cat\
ch(u){c=\x22\x22}!b&&a\
.isLocal&&!a.cro\
ssDomain?b=e.tex\
t?200:404:1223==\
=b&&(b=204);l(b,\
c,e,d)}}catch(U)\
{alert(U),l(-1,U\
)}};a.async?4===\
q.readyState?set\
Timeout(h):q.onr\
eadystatechange=\
h:h()},abort:fun\
ction(){}}}))})(\
jQuery);\x0a(functi\
on(a,m,k,h){func\
tion e(e,k){func\
tion s(b){a(u).e\
ach(function(){s\
elf.Jmol&&(0<=k.\
indexOf(\x22mouseup\
\x22)||0<=k.indexOf\
(\x22touchend\x22))&&J\
mol._setMouseOwn\
er(null);var d=a\
(this);this!==b.\
target&&!d.has(b\
.target).length&\
&d.triggerHandle\
r(k,[b.target,b]\
)})}k=k||e+h;var\
 u=a(),b=e+\x22.\x22+k\
+\x22-special-event\
\x22;a.event.specia\
l[k]={setup:func\
tion(){u=u.add(t\
his);1===u.lengt\
h&&a(m).bind(b,s\
)},teardown:func\
tion(){self.Jmol\
&&Jmol._setMouse\
Owner(null);u=u.\
not(this);0===u.\
length&&a(m).unb\
ind(b)},add:func\
tion(a){var b=\x0aa\
.handler;a.handl\
er=function(a,c)\
{a.target=c;b.ap\
ply(this,argumen\
ts)}}}}a.map(k.s\
plit(\x22 \x22),functi\
on(a){e(a)});e(\x22\
focusin\x22,\x22focus\x22\
+h);e(\x22focusout\x22\
,\x22blur\x22+h)})(jQu\
ery,document,\x22cl\
ick mousemove mo\
useup touchmove \
touchend\x22,\x22outjs\
mol\x22);\x22undefined\
\x22==typeof jQuery\
&&alert(\x22Note --\
 JSmoljQuery is \
required for JSm\
ol, but it's not\
 defined.\x22);self\
.Jmol||(Jmol={})\
;\x0aJmol._version|\
|(Jmol=function(\
a){var m=functio\
n(a){return{rear\
:a++,header:a++,\
main:a++,image:a\
++,front:a++,fil\
eOpener:a++,cove\
rImage:a++,dialo\
g:a++,menu:a+9E4\
,console:a+91E3,\
consoleImage:a+9\
1001,monitorZInd\
ex:a+99999}},m={\
_version:\x22$Date:\
 2016-05-08 13:2\
0:27 -0500 (Sun,\
 08 May 2016) $\x22\
,_alertNoBinary:\
!0,_allowedJmolS\
ize:[25,2048,300\
],_appletCssClas\
s:\x22\x22,_appletCssT\
ext:\x22\x22,_fileCach\
e:null,_jarFile:\
null,_j2sPath:nu\
ll,_use:null,_j2\
sLoadMonitorOpac\
ity:90,_applets:\
{},_asynchronous\
:!0,_ajaxQueue:[\
],_persistentMen\
u:!1,\x0a_getZOrder\
s:m,_z:m(Jmol.z|\
|9E3),_debugCode\
:!0,db:{_databas\
ePrefixes:\x22$=:\x22,\
_fileLoadScript:\
\x22;if (_loadScrip\
t = '' && defaul\
tLoadScript == '\
' && _filetype =\
= 'Pdb') { selec\
t protein or nuc\
leic;cartoons On\
ly;color structu\
re; select * };\x22\
,_nciLoadScript:\
\x22;n = ({molecule\
=1}.length < {mo\
lecule=2}.length\
 ? 2 : 1); selec\
t molecule=n;dis\
play selected;ce\
nter selected;\x22,\
_pubChemLoadScri\
pt:\x22\x22,_DirectDat\
abaseCalls:{\x22cac\
tus.nci.nih.gov\x22\
:null,\x22.x3dna.or\
g\x22:null,\x22rruff.g\
eo.arizona.edu\x22:\
null,\x22.rcsb.org\x22\
:null,\x22ftp.wwpdb\
.org\x22:null,\x0a\x22pdb\
e.org\x22:null,\x22mat\
erialsproject.or\
g\x22:null,\x22.ebi.ac\
.uk\x22:null,\x22pubch\
em.ncbi.nlm.nih.\
gov\x22:null,\x22http:\
//www.nmrdb.org/\
tools/jmol/predi\
ct.php\x22:null,$:\x22\
https://cactus.n\
ci.nih.gov/chemi\
cal/structure/%F\
ILENCI/file?form\
at=sdf&get3d=Tru\
e\x22,$$:\x22https://c\
actus.nci.nih.go\
v/chemical/struc\
ture/%FILENCI/fi\
le?format=sdf\x22,\x22\
=\x22:\x22http://files\
.rcsb.org/view/%\
FILE.pdb\x22,\x22*\x22:\x22h\
ttp://www.ebi.ac\
.uk/pdbe/entry-f\
iles/download/%F\
ILE.cif\x22,\x22==\x22:\x22h\
ttp://www.rcsb.o\
rg/pdb/files/lig\
and/%FILE.cif\x22,\x22\
:\x22:\x22https://pubc\
hem.ncbi.nlm.nih\
.gov/rest/pug/co\
mpound/%FILE/SDF\
?record_type=3d\x22\
},\x0a_restQueryUrl\
:\x22http://www.rcs\
b.org/pdb/rest/s\
earch\x22,_restQuer\
yXml:\x22<orgPdbQue\
ry><queryType>or\
g.pdb.query.simp\
le.AdvancedKeywo\
rdQuery</queryTy\
pe><description>\
Text Search</des\
cription><keywor\
ds>QUERY</keywor\
ds></orgPdbQuery\
>\x22,_restReportUr\
l:\x22http://www.pd\
b.org/pdb/rest/c\
ustomReport?pdbi\
ds=IDLIST&custom\
ReportColumns=st\
ructureId,struct\
ureTitle\x22},_debu\
gAlert:!1,_docum\
ent:a,_isXHTML:!\
1,_lastAppletID:\
null,_mousePageX\
:null,_mouseOwne\
r:null,_serverUr\
l:\x22http://your.s\
erver.here/jsmol\
.php\x22,_syncId:(\x22\
\x22+Math.random())\
.substring(3),\x0a_\
touching:!1,_Xht\
mlElement:null,_\
XhtmlAppendChild\
:!1};a=a.locatio\
n.href.toLowerCa\
se();m._httpProt\
o=0==a.indexOf(\x22\
https\x22)?\x22https:/\
/\x22:\x22http://\x22;m._\
isFile=0==a.inde\
xOf(\x22file:\x22);m._\
isFile&&$.ajaxSe\
tup({mimeType:\x22t\
ext/plain\x22});m._\
ajaxTestSite=m._\
httpProto+\x22googl\
e.com\x22;a=m._isFi\
le||0==a.indexOf\
(\x22http://localho\
st\x22)||0==a.index\
Of(\x22http://127.\x22\
);m._tracker=\x22ht\
tp://\x22==m._httpP\
roto&&!a&&\x22http:\
//chemapps.stola\
f.edu/jmol/JmolT\
racker.htm?id=UA\
-45940799-1\x22;m._\
isChrome=0<=navi\
gator.userAgent.\
toLowerCase().in\
dexOf(\x22chrome\x22);\
\x0am._isSafari=!m.\
_isChrome&&0<=na\
vigator.userAgen\
t.toLowerCase().\
indexOf(\x22safari\x22\
);m._isMsie=void\
 0!==window.Acti\
veXObject;m._isE\
dge=0<=navigator\
.userAgent.index\
Of(\x22Edge/\x22);m._u\
seDataURI=!m._is\
Safari&&!m._isMs\
ie&&!m._isEdge;w\
indow.requestAni\
mationFrame||(wi\
ndow.requestAnim\
ationFrame=windo\
w.setTimeout);fo\
r(var k in Jmol)\
m[k]=Jmol[k];ret\
urn m}(document,\
Jmol));\x0a(functio\
n(a,m){a.__$=m;m\
(document).ready\
(function(){a._d\
ocument=null});a\
.$=function(a,c)\
{null==a&&alert(\
c+arguments.call\
ee.caller.toStri\
ng());return m(c\
?\x22#\x22+a._id+\x22_\x22+c\
:a)};a._$=functi\
on(a){return\x22str\
ing\x22==typeof a?m\
(\x22#\x22+a):a};a.$aj\
ax=function(b){a\
._ajaxCall=b.url\
;b.cache=\x22NO\x22!=b\
.cache;b.url=a._\
fixProtocol(b.ur\
l);return m.ajax\
(b)};a._fixProto\
col=function(a){\
return 0==a.inde\
xOf(\x22http://www.\
rcsb.org/pdb/fil\
es/\x22)&&0>a.index\
Of(\x22/ligand/\x22)?\x22\
http://files.rcs\
b.org/view/\x22+a.s\
ubstring(30).rep\
lace(/\x5c.gz/,\x22\x22):\
\x0a0==a.indexOf(\x22h\
ttp://\x22)&&(0==a.\
indexOf(\x22http://\
pubchem\x22)||0==a.\
indexOf(\x22http://\
cactus\x22)||0==a.i\
ndexOf(\x22http://w\
ww.materialsproj\
ect\x22))?\x22https\x22+a\
.substring(4):a}\
;a._getNCIInfo=f\
unction(b,c){ret\
urn a._getFileDa\
ta(\x22https://cact\
us.nci.nih.gov/c\
hemical/structur\
e/\x22+b+\x22/\x22+(\x22name\
\x22==c?\x22names\x22:c))\
};a.$appEvent=fu\
nction(b,c,d,e){\
b=a.$(b,c);b.off\
(d)&&e&&b.on(d,e\
)};a.$resize=fun\
ction(a){return \
m(window).resize\
(a)};a.$after=fu\
nction(a,c){retu\
rn m(a).after(c)\
};a.$append=func\
tion(a,c){return\
 m(a).append(c)}\
;a.$bind=\x0afuncti\
on(a,c,d){return\
 d?m(a).bind(c,d\
):m(a).unbind(c)\
};a.$closest=fun\
ction(a,c){retur\
n m(a).closest(c\
)};a.$get=functi\
on(a,c){return m\
(a).get(c)};a.$d\
ocumentOff=funct\
ion(a,c){return \
m(document).off(\
a,\x22#\x22+c)};a.$doc\
umentOn=function\
(a,c,d){return m\
(document).on(a,\
\x22#\x22+c,d)};a.$get\
AncestorDiv=func\
tion(a,c){return\
 m(\x22div.\x22+c+\x22:ha\
s(#\x22+a+\x22)\x22)[0]};\
a.$supportsIECro\
ssDomainScriptin\
g=function(){ret\
urn m.support.ie\
cors};a.$attr=fu\
nction(b,c,d){re\
turn a._$(b).att\
r(c,d)};a.$css=f\
unction(b,c){ret\
urn a._$(b).css(\
c)};\x0aa.$find=fun\
ction(b,c){retur\
n a._$(b).find(c\
)};a.$focus=func\
tion(b){return a\
._$(b).focus()};\
a.$html=function\
(b,c){return a._\
$(b).html(c)};a.\
$offset=function\
(b){return a._$(\
b).offset()};a.$\
windowOn=functio\
n(a,c){return m(\
window).on(a,c)}\
;a.$prop=functio\
n(b,c,d){var e=a\
._$(b);return 3=\
=arguments.lengt\
h?e.prop(c,d):e.\
prop(c)};a.$remo\
ve=function(b){r\
eturn a._$(b).re\
move()};a.$scrol\
lTo=function(b,c\
){var d=a._$(b);\
return d.scrollT\
op(0>c?d[0].scro\
llHeight:c)};a.$\
setEnabled=funct\
ion(b,c){return \
a._$(b).attr(\x22di\
sabled\x22,\x0ac?null:\
\x22disabled\x22)};a.$\
getSize=function\
(b){b=a._$(b);re\
turn[b.width(),b\
.height()]};a.$s\
etSize=function(\
b,c,d){return a.\
_$(b).width(c).h\
eight(d)};a.$is=\
function(b,c){re\
turn a._$(b).is(\
c)};a.$setVisibl\
e=function(b,c){\
var d=a._$(b);re\
turn c?d.show():\
d.hide()};a.$sub\
mit=function(b){\
return a._$(b).s\
ubmit()};a.$val=\
function(b,c){va\
r d=a._$(b);retu\
rn 1==arguments.\
length?d.val():d\
.val(c)};a._clea\
rVars=function()\
{delete jQuery;d\
elete m;delete a\
;delete SwingCon\
troller;delete J\
;delete JM;delet\
e JS;delete JSV;\
\x0adelete JU;delet\
e JV;delete java\
;delete javajs;d\
elete Clazz;dele\
te c$};var k=doc\
ument,h=window,e\
={};e.ua=navigat\
or.userAgent.toL\
owerCase();var l\
;a:{l=[\x22linux\x22,\x22\
unix\x22,\x22mac\x22,\x22win\
\x22];for(var q=l.l\
ength;q--;)if(-1\
!=e.ua.indexOf(l\
[q])){l=l[q];bre\
ak a}l=\x22unknown\x22\
}e.os=l;e.browse\
r=function(){for\
(var a=e.ua,c=\x22k\
onqueror webkit \
omniweb opera we\
btv icab msie mo\
zilla\x22.split(\x22 \x22\
),d=0;d<c.length\
;d++)if(0<=a.ind\
exOf(c[d]))retur\
n c[d];return\x22un\
known\x22};e.browse\
rName=e.browser(\
);e.browserVersi\
on=parseFloat(e.\
ua.substring(e.u\
a.indexOf(e.brow\
serName)+\x0ae.brow\
serName.length+1\
));e.supportsXhr\
2=function(){ret\
urn m.support.co\
rs||m.support.ie\
cors};e.allowDes\
troy=\x22msie\x22!=e.b\
rowserName;e.all\
owHTML5=\x22msie\x22!=\
e.browserName||0\
>navigator.appVe\
rsion.indexOf(\x22M\
SIE 8\x22);e.getDef\
aultLanguage=fun\
ction(){return n\
avigator.languag\
e||navigator.use\
rLanguage||\x22en-U\
S\x22};e._webGLtest\
=0;e.supportsWeb\
GL=function(){if\
(!a.featureDetec\
tion._webGLtest)\
{var b;a.feature\
Detection._webGL\
test=h.WebGLRend\
eringContext&&((\
b=k.createElemen\
t(\x22canvas\x22)).get\
Context(\x22webgl\x22)\
||b.getContext(\x22\
experimental-web\
gl\x22))?\x0a1:-1}retu\
rn 0<a.featureDe\
tection._webGLte\
st};e.supportsLo\
calization=funct\
ion(){for(var a=\
k.getElementsByT\
agName(\x22meta\x22),c\
=a.length;0<=--c\
;)if(0<=a[c].out\
erHTML.toLowerCa\
se().indexOf(\x22ut\
f-8\x22))return!0;r\
eturn!1};e.suppo\
rtsJava=function\
(){a.featureDete\
ction._javaEnabl\
ed||(a.featureDe\
tection._javaEna\
bled=a._isMsie?n\
avigator.javaEna\
bled()?1:-1:navi\
gator.javaEnable\
d()&&(!navigator\
.mimeTypes||navi\
gator.mimeTypes[\
\x22application/x-j\
ava-applet\x22])?1:\
-1);return 0<a.f\
eatureDetection.\
_javaEnabled};e.\
compliantBrowser\
=\x0afunction(){var\
 a=!!k.getElemen\
tById,c=e.os;if(\
\x22opera\x22==e.brows\
erName&&7.54>=e.\
browserVersion&&\
\x22mac\x22==c||\x22webki\
t\x22==e.browserNam\
e&&125.12>e.brow\
serVersion||\x22msi\
e\x22==e.browserNam\
e&&\x22mac\x22==c||\x22ko\
nqueror\x22==e.brow\
serName&&3.3>=e.\
browserVersion)a\
=!1;return a};e.\
isFullyCompliant\
=function(){retu\
rn e.compliantBr\
owser()&&e.suppo\
rtsJava()};e.use\
IEObject=\x22win\x22==\
e.os&&\x22msie\x22==e.\
browserName&&5.5\
<=e.browserVersi\
on;e.useHtml4Obj\
ect=\x22mozilla\x22==e\
.browserName&&5<\
=e.browserVersio\
n||\x22opera\x22==e.br\
owserName&&8<=e.\
browserVersion||\
\x0a\x22webkit\x22==e.bro\
wserName;e.hasFi\
leReader=h.File&\
&h.FileReader;a.\
featureDetection\
=e;a._ajax=funct\
ion(b){if(!b.asy\
nc)return a.$aja\
x(b).responseTex\
t;a._ajaxQueue.p\
ush(b);1==a._aja\
xQueue.length&&a\
._ajaxDone()};a.\
_ajaxDone=functi\
on(){var b=a._aj\
axQueue.shift();\
b&&a.$ajax(b)};a\
._grabberOptions\
=[[\x22$\x22,\x22NCI(smal\
l molecules)\x22],[\
\x22:\x22,\x22PubChem(sma\
ll molecules)\x22],\
[\x22=\x22,\x22RCSB(macro\
molecules)\x22],[\x22*\
\x22,\x22PDBe(macromol\
ecules)\x22]];a._ge\
tGrabberOptions=\
function(b){if(0\
==a._grabberOpti\
ons.length)retur\
n\x22\x22;var c='<inpu\
t type=\x22text\x22 id\
=\x22ID_query\x22 onfo\
cus=\x22jQuery(this\
).select()\x22 onke\
ypress=\x22if(13==e\
vent.which){Jmol\
._applets[\x5c'ID\x5c'\
]._search();retu\
rn false}\x22 size=\
\x2232\x22 value=\x22\x22 />\
',\x0ad='<button id\
=\x22ID_submit\x22 onc\
lick=\x22Jmol._appl\
ets[\x5c'ID\x5c']._sea\
rch()\x22>Search</b\
utton></nobr>';1\
==a._grabberOpti\
ons.length?(c=\x22<\
nobr>\x22+c+'<span \
style=\x22display:n\
one\x22>',d=\x22</span\
>\x22+d):c+=\x22<br />\
<nobr>\x22;for(var \
c=c+'<select id=\
\x22ID_select\x22>',e=\
0;e<a._grabberOp\
tions.length;e++\
)var h=a._grabbe\
rOptions[e],c=c+\
('<option value=\
\x22'+h[0]+'\x22 '+(0=\
=e?\x22selected\x22:\x22\x22\
)+\x22>\x22+h[1]+\x22</op\
tion>\x22);c=(c+\x22</\
select>\x22+d).repl\
ace(/ID/g,b._id)\
;return\x22<br />\x22+\
c};a._getScriptF\
orDatabase=funct\
ion(b){return\x22$\x22\
==b?a.db._nciLoa\
dScript:\x0a\x22:\x22==b?\
a.db._pubChemLoa\
dScript:a.db._fi\
leLoadScript};a.\
_setInfo=functio\
n(a,c,d){var e=[\
],h=\x22\x22;if(0==d.i\
ndexOf(\x22ERROR\x22))\
h=d;else switch(\
c){case \x22=\x22:c=d.\
split(\x22<dimStruc\
ture.structureId\
>\x22);e=[\x22<table>\x22\
];for(d=1;d<c.le\
ngth;d++)e.push(\
'<tr><td valign=\
top><a href=\x22jav\
ascript:Jmol.sea\
rch('+a._id+\x22,'=\
\x22+c[d].substring\
(0,4)+\x22')\x5c\x22>\x22+c[\
d].substring(0,4\
)+\x22</a></td>\x22),e\
.push(\x22<td>\x22+c[d\
].split(\x22Title>\x22\
)[1].split(\x22</\x22)\
[0]+\x22</td></tr>\x22\
);e.push(\x22</tabl\
e>\x22);h=c.length-\
1+\x22 matches\x22;bre\
ak;case \x22$\x22:case\
 \x22:\x22:break;defau\
lt:return}a._inf\
oHeader=\x0ah;a._in\
fo=e.join(\x22\x22);a.\
_showInfo(!0)};a\
._loadSuccess=fu\
nction(b,c){c&&(\
a._ajaxDone(),c(\
b))};a._loadErro\
r=function(b){a.\
_ajaxDone();a.sa\
y(\x22Error connect\
ing to server: \x22\
+a._ajaxCall);nu\
ll!=b&&b()};a._i\
sDatabaseCall=fu\
nction(b){return\
 0<=a.db._databa\
sePrefixes.index\
Of(b.substring(0\
,1))};a._getDire\
ctDatabaseCall=f\
unction(b,c){if(\
c&&!a.featureDet\
ection.supportsX\
hr2())return b;v\
ar d=2,e=b.subst\
ring(0,d),h=a.db\
._DirectDatabase\
Calls[e]||a.db._\
DirectDatabaseCa\
lls[e=b.substrin\
g(0,--d)];h&&(\x22:\
\x22==e?(e=b.toLowe\
rCase(),\x0aisNaN(p\
arseInt(b.substr\
ing(1)))?0==e.in\
dexOf(\x22:smiles:\x22\
)?(h+=\x22?POST?smi\
les=\x22+b.substrin\
g(8),b=\x22smiles\x22)\
:0==e.indexOf(\x22:\
cid:\x22)?b=\x22cid/\x22+\
b.substring(5):(\
0==e.indexOf(\x22:n\
ame:\x22)?b=b.subst\
ring(5):0==e.ind\
exOf(\x22:cas:\x22)&&(\
b=b.substring(4)\
),b=\x22name/\x22+enco\
deURIComponent(b\
.substring(d))):\
b=\x22cid/\x22+b.subst\
ring(1)):b=encod\
eURIComponent(b.\
substring(d)),0<\
=b.indexOf(\x22.mmt\
f\x22)?b=\x22http://mm\
tf.rcsb.org/full\
/\x22+b:0<=h.indexO\
f(\x22FILENCI\x22)?(b=\
b.replace(/\x5c%2F/\
g,\x22/\x22),b=h.repla\
ce(/\x5c%FILENCI/,b\
)):b=h.replace(/\
\x5c%FILE/,b));retu\
rn b};\x0aa._getRaw\
DataFromServer=f\
unction(b,c,d,e,\
h,k){b=\x22?call=ge\
tRawDataFromData\
base&database=\x22+\
b+(0<=c.indexOf(\
\x22?POST?\x22)?\x22?POST\
?\x22:\x22\x22)+\x22&query=\x22\
+encodeURICompon\
ent(c)+(h?\x22&enco\
ding=base64\x22:\x22\x22)\
+(k?\x22\x22:\x22&script=\
\x22+encodeURICompo\
nent(a._getScrip\
tForDatabase(b))\
);return a._cont\
actServer(b,d,e)\
};a._checkFileNa\
me=function(b,c,\
d){a._isDatabase\
Call(c)&&(d&&a._\
setQueryTerm(b,c\
),c=a._getDirect\
DatabaseCall(c,!\
0),a._isDatabase\
Call(c)&&(c=a._g\
etDirectDatabase\
Call(c,!1),d&&(d\
[0]=!0)));return\
 c};a._checkCach\
e=function(b,\x0ac,\
d){if(b._cacheFi\
les&&a._fileCach\
e&&!c.endsWith(\x22\
.js\x22)){if(b=a._f\
ileCache[c])retu\
rn System.out.pr\
intln(\x22using \x22+b\
.length+\x22 bytes \
of cached data f\
or \x22+c),d(b),nul\
l;d=function(b,c\
){d(a._fileCache\
[b]=c)}}return d\
};a._playAudio=f\
unction(a){var c\
=document.create\
Element(\x22audio\x22)\
;c.controls=\x22tru\
e\x22;c.src=a;c.pla\
y()};a._loadFile\
Data=function(b,\
c,d,e){var h=[];\
c=a._checkFileNa\
me(b,c,h);d=a._c\
heckCache(b,c,d)\
;h[0]?a._getRawD\
ataFromServer(\x22_\
\x22,c,d,e):(b={typ\
e:\x22GET\x22,dataType\
:\x22text\x22,url:c,as\
ync:a._asynchron\
ous,\x0asuccess:fun\
ction(b){a._load\
Success(b,d)},er\
ror:function(){a\
._loadError(e)}}\
,a._checkAjaxPos\
t(b),a._ajax(b))\
};a._getInfoFrom\
Database=functio\
n(b,c,d){if(\x22===\
=\x22==c){var e=a.d\
b._restQueryXml.\
replace(/QUERY/,\
d),e={dataType:\x22\
text\x22,type:\x22POST\
\x22,contentType:\x22a\
pplication/x-www\
-form-urlencoded\
\x22,url:a.db._rest\
QueryUrl,data:en\
codeURIComponent\
(e)+\x22&req=browse\
r\x22,success:funct\
ion(e){a._ajaxDo\
ne();a._extractI\
nfoFromRCSB(b,c,\
d,e)},error:func\
tion(){a._loadEr\
ror(null)},async\
:a._asynchronous\
};return a._ajax\
(e)}d=\x22?call=get\
InfoFromDatabase\
&database=\x22+\x0ac+\x22\
&query=\x22+encodeU\
RIComponent(d);r\
eturn a._contact\
Server(d,functio\
n(d){a._setInfo(\
b,c,d)})};a._ext\
ractInfoFromRCSB\
=function(b,c,d,\
e){var h=e.lengt\
h/5;if(0!=h&&4==\
d.length&&1!=h){\
d=d.toUpperCase(\
);var k=e.indexO\
f(d);0<k&&0<=\x2212\
3456789\x22.indexOf\
(d.substring(0,1\
))&&(e=d+\x22,\x22+e.s\
ubstring(0,k)+e.\
substring(k+5));\
50<h&&(e=e.subst\
ring(0,250));e=e\
.replace(/\x5cn/g,\x22\
,\x22);e=a._restRep\
ortUrl.replace(/\
IDLIST/,e);a._lo\
adFileData(b,e,f\
unction(d){a._se\
tInfo(b,c,d)})}}\
;a._checkAjaxPos\
t=function(a){va\
r c=a.url.indexO\
f(\x22?POST?\x22);\x0a0<c\
&&(a.data=a.url.\
substring(c+6),a\
.url=a.url.subst\
ring(0,c),a.type\
=\x22POST\x22,a.conten\
tType=\x22applicati\
on/x-www-form-ur\
lencoded\x22)};a._c\
ontactServer=fun\
ction(b,c,d){b={\
dataType:\x22text\x22,\
type:\x22GET\x22,url:a\
._serverUrl+b,su\
ccess:function(b\
){a._loadSuccess\
(b,c)},error:fun\
ction(){a._loadE\
rror(d)},async:c\
?a._asynchronous\
:!1};a._checkAja\
xPost(b);return \
a._ajax(b)};a._s\
etQueryTerm=func\
tion(b,c){if(c&&\
b._hasOptions&&\x22\
http://\x22!=c.subs\
tring(0,7)){if(a\
._isDatabaseCall\
(c)){var d=c.sub\
string(0,1);c=c.\
substring(1);c.s\
ubstring(0,\x0a1)==\
d&&0<=\x22=$\x22.index\
Of(d)&&(c=c.subs\
tring(1));var e=\
a._getElement(b,\
\x22select\x22);if(e&&\
e.options)for(va\
r h=0;h<e.option\
s.length;h++)e[h\
].value==d&&(e[h\
].selected=!0)}a\
.$val(a.$(b,\x22que\
ry\x22),c)}};a._sea\
rch=function(b,c\
,d){1<arguments.\
length||(c=null)\
;a._setQueryTerm\
(b,c);c||(c=a.$v\
al(a.$(b,\x22query\x22\
)));0==c.indexOf\
(\x22!\x22)?b._script(\
c.substring(1)):\
(c&&(c=c.replace\
(/\x5c\x22/g,\x22\x22)),b._s\
howInfo(!1),a._s\
earchMol(b,c,d,!\
0))};a._searchMo\
l=function(b,c,d\
,e){var h;a._isD\
atabaseCall(c)?(\
h=c.substring(0,\
1),c=c.substring\
(1)):\x0ah=b._hasOp\
tions?a.$val(a.$\
(b,\x22select\x22)):\x22$\
\x22;\x22=\x22==h&&3==c.l\
ength&&(c=\x22=\x22+c)\
;var k=h+c;if(c&\
&!(0>k.indexOf(\x22\
?\x22)&&k==b._thisJ\
molModel)){b._th\
isJmolModel=k;va\
r l;e&&null!=b._\
viewSet&&null!=(\
l=a.View.__findV\
iew(b._viewSet,{\
chemID:k}))?a.Vi\
ew.__setView(l,b\
,!1):(\x22$\x22==h||\x22:\
\x22==h?b._jmolFile\
Type=\x22MOL\x22:\x22=\x22==\
h&&(b._jmolFileT\
ype=\x22PDB\x22),b._se\
archDatabase(c,h\
,d))}};a._search\
Database=functio\
n(b,c,d,e){b._sh\
owInfo(!1);retur\
n 0<=c.indexOf(\x22\
?\x22)?(a._getInfoF\
romDatabase(b,d,\
c.split(\x22?\x22)[0])\
,!0):a.db._Direc\
tDatabaseCalls[d\
]?\x0a(b._loadFile(\
d+c,e),!0):!1};a\
._syncBinaryOK=\x22\
?\x22;a._canSyncBin\
ary=function(b){\
if(a._isAsync)re\
turn!0;if(self.V\
BArray)return a.\
_syncBinaryOK=!1\
;if(\x22?\x22!=a._sync\
BinaryOK)return \
a._syncBinaryOK;\
a._syncBinaryOK=\
!0;try{var c=new\
 window.XMLHttpR\
equest;c.open(\x22t\
ext\x22,a._ajaxTest\
Site,!1);c.hasOw\
nProperty(\x22respo\
nseType\x22)?c.resp\
onseType=\x22arrayb\
uffer\x22:c.overrid\
eMimeType&&c.ove\
rrideMimeType(\x22t\
ext/plain; chars\
et=x-user-define\
d\x22)}catch(d){ret\
urn System.out.p\
rintln(\x22JSmolCor\
e.js: synchronou\
s binary file tr\
ansfer is reques\
ted but not avai\
lable\x22),\x0aa._aler\
tNoBinary&&!b&&a\
lert(\x22JSmolCore.\
js: synchronous \
binary file tran\
sfer is requeste\
d but not availa\
ble\x22),a._syncBin\
aryOK=!1}return!\
0};a._binaryType\
s=\x22mmtf .gz .jpg\
 .gif .png .zip \
.jmol .bin .smol\
 .spartan .mrc .\
map .ccp4 .dn6 .\
delphi .omap .ps\
e .dcd\x22.split(\x22 \
\x22);a._isBinaryUr\
l=function(b){fo\
r(var c=a._binar\
yTypes.length;0<\
=--c;)if(0<=b.in\
dexOf(a._binaryT\
ypes[c]))return!\
0;return!1};a._g\
etFileData=funct\
ion(b,c,d){var e\
=a._isBinaryUrl(\
b),h=0<=b.indexO\
f(\x22.gz\x22)&&0<=b.i\
ndexOf(\x22rcsb.org\
\x22);h&&(b=b.repla\
ce(/\x5c.gz/,\x0a\x22\x22),e\
=!1);var h=e&&!c\
&&!a._canSyncBin\
ary(h),k=0<=b.in\
dexOf(\x22?POST?\x22);\
0==b.indexOf(\x22fi\
le:/\x22)&&0!=b.ind\
exOf(\x22file:///\x22)\
&&(b=\x22file://\x22+b\
.substring(5));v\
ar l=0>b.indexOf\
(\x22://\x22)||0==b.in\
dexOf(document.l\
ocation.protocol\
)&&0<=b.indexOf(\
document.locatio\
n.host),q=\x22https\
://\x22==a._httpPro\
to&&0==b.indexOf\
(\x22http://\x22),m=a.\
_isDirectCall(b)\
;!m&&0<=b.indexO\
f(\x22?ALLOWSORIGIN\
?\x22)&&(m=!0,b=b.r\
eplace(/\x5c?ALLOWS\
ORIGIN\x5c?/,\x22\x22));v\
ar s=!l&&a.$supp\
ortsIECrossDomai\
nScripting(),u=n\
ull;if(q||h||!l&\
&!m||!c&&s)u=a._\
getRawDataFromSe\
rver(\x22_\x22,\x0ab,c,c,\
h,!0);else{b=b.r\
eplace(/file:\x5c/\x5c\
/\x5c/\x5c//,\x22file://\x22\
);var P={dataTyp\
e:e?\x22binary\x22:\x22te\
xt\x22,async:!!c};k\
?(P.type=\x22POST\x22,\
P.url=b.split(\x22?\
POST?\x22)[0],P.dat\
a=b.split(\x22?POST\
?\x22)[1]):(P.type=\
\x22GET\x22,P.url=b);c\
&&(P.success=fun\
ction(){c(a._xhr\
Return(P.xhr))},\
P.error=function\
(){c(P.xhr.statu\
sText)});P.xhr=a\
.$ajax(P);c||(u=\
a._xhrReturn(P.x\
hr))}if(!d)retur\
n u;null==u&&(u=\
\x22\x22,e=!1);e&&(e=a\
._canSyncBinary(\
!0));return e?a.\
_strToBytes(u):J\
U.SB.newS(u)};a.\
_xhrReturn=funct\
ion(a){return!a.\
responseText||se\
lf.Clazz&&Clazz.\
instanceOf(a.res\
ponse,\x0aself.Arra\
yBuffer)?a.respo\
nse||a.statusTex\
t:a.responseText\
};a._isDirectCal\
l=function(b){if\
(0<=b.indexOf(\x22?\
ALLOWSORIGIN?\x22))\
return!0;for(var\
 c in a.db._Dire\
ctDatabaseCalls)\
if(0<=c.indexOf(\
\x22.\x22)&&0<=b.index\
Of(c))return!0;r\
eturn!1};a._clea\
nFileData=functi\
on(a){return 0<=\
a.indexOf(\x22\x5cr\x22)&\
&0<=a.indexOf(\x22\x5c\
n\x22)?a.replace(/\x5c\
r\x5cn/g,\x22\x5cn\x22):0<=a\
.indexOf(\x22\x5cr\x22)?a\
.replace(/\x5cr/g,\x22\
\x5cn\x22):a};a._getFi\
leType=function(\
a){var c=a.subst\
ring(0,1);if(\x22$\x22\
==c||\x22:\x22==c)retu\
rn\x22MOL\x22;if(\x22=\x22==\
c)return\x22=\x22==a.s\
ubstring(1,2)?\x22L\
CIF\x22:\x22PDB\x22;a=\x0aa.\
split(\x22.\x22).pop()\
.toUpperCase();r\
eturn a.substrin\
g(0,Math.min(a.l\
ength,3))};a._ge\
tZ=function(b,c)\
{return b&&b._z&\
&b._z[c]||a._z[c\
]};a._incrZ=func\
tion(b,c){return\
 b&&b._z&&++b._z\
[c]||++a._z[c]};\
a._hideLocalFile\
Reader=function(\
b){b._localReade\
r&&a.$setVisible\
(b._localReader,\
!1);b._readingLo\
cal=!1;a._setCur\
sor(b,0)};a.load\
FileFromDialog=f\
unction(b){a._lo\
adFileAsynchrono\
usly(null,b,null\
,null)};a._loadF\
ileAsynchronousl\
y=function(b,c,d\
,e){if(d&&0!=d.i\
ndexOf(\x22?\x22)){var\
 h=d;d=a._checkF\
ileName(c,d);var\
 k=\x0afunction(k){\
a._setData(b,d,h\
,k,e,c)},k=a._ch\
eckCache(c,d,k);\
0<=d.indexOf(\x22|\x22\
)&&(d=d.split(\x22|\
\x22)[0]);return nu\
ll==k?null:a._ge\
tFileData(d,k)}i\
f(!a.featureDete\
ction.hasFileRea\
der)return b?b.s\
etData(msg,null,\
null,e,c):alert(\
msg);c._localRea\
der||(k='<div id\
=\x22ID\x22 style=\x22z-i\
ndex:'+a._getZ(c\
,\x22fileOpener\x22)+'\
;position:absolu\
te;background:#E\
0E0E0;left:10px;\
top:10px\x22><div s\
tyle=\x22margin:5px\
 5px 5px 5px;\x22><\
button id=\x22ID_lo\
adurl\x22>URL</butt\
on><input type=\x22\
file\x22 id=\x22ID_fil\
es\x22 /><button id\
=\x22ID_loadfile\x22>l\
oad</button><but\
ton id=\x22ID_cance\
l\x22>cancel</butto\
n></div><div>',\x0a\
a.$after(\x22#\x22+c._\
id+\x22_appletdiv\x22,\
k.replace(/ID/g,\
c._id+\x22_localRea\
der\x22)),c._localR\
eader=a.$(c,\x22loc\
alReader\x22));a.$a\
ppEvent(c,\x22local\
Reader_loadurl\x22,\
\x22click\x22);a.$appE\
vent(c,\x22localRea\
der_loadurl\x22,\x22cl\
ick\x22,function(){\
var b=prompt(\x22En\
ter a URL\x22);b&&(\
a._hideLocalFile\
Reader(c,0),a._s\
etData(null,b,b,\
null,e,c))});a.$\
appEvent(c,\x22loca\
lReader_loadfile\
\x22,\x22click\x22);a.$ap\
pEvent(c,\x22localR\
eader_loadfile\x22,\
\x22click\x22,function\
(){var d=a.$(c,\x22\
localReader_file\
s\x22)[0].files[0],\
h=new FileReader\
;h.onloadend=fun\
ction(h){h.targe\
t.readyState==\x0aF\
ileReader.DONE&&\
(a._hideLocalFil\
eReader(c,0),a._\
setData(b,d.name\
,d.name,h.target\
.result,e,c))};t\
ry{h.readAsArray\
Buffer(d)}catch(\
k){alert(\x22You mu\
st select a file\
 first.\x22)}});a.$\
appEvent(c,\x22loca\
lReader_cancel\x22,\
\x22click\x22);a.$appE\
vent(c,\x22localRea\
der_cancel\x22,\x22cli\
ck\x22,function(){a\
._hideLocalFileR\
eader(c);b&&b.se\
tData(\x22#CANCELED\
#\x22,null,null,e,c\
)});a.$setVisibl\
e(c._localReader\
,!0);c._readingL\
ocal=!0};a._setD\
ata=function(b,c\
,d,e,h,k){e&&(e=\
a._strToBytes(e)\
);null!=e&&(null\
==b||0<=c.indexO\
f(\x22.jdx\x22))&&a.Ca\
che.put(\x22cache:/\
/\x22+\x0ac,e);null==b\
?k._applet.openF\
ileAsyncSpecial(\
null==e?c:\x22cache\
://\x22+c,1):b.setD\
ata(c,d,e,h)};a.\
_doAjax=function\
(b,c,d){b=b.toSt\
ring();if(null!=\
d)return a._save\
File(b,d);c&&(b+\
=\x22?POST?\x22+c);ret\
urn a._getFileDa\
ta(b,null,!0)};a\
._saveFile=funct\
ion(b,c,d,e){if(\
a._localFileSave\
Function&&a._loc\
alFileSaveFuncti\
on(b,c))return\x22O\
K\x22;b=b.substring\
(b.lastIndexOf(\x22\
/\x22)+1);d||(d=0<=\
b.indexOf(\x22.pdf\x22\
)?\x22application/p\
df\x22:0<=b.indexOf\
(\x22.png\x22)?\x22image/\
png\x22:0<=b.indexO\
f(\x22.gif\x22)?\x22image\
/gif\x22:0<=b.index\
Of(\x22.jpg\x22)?\x22imag\
e/jpg\x22:\x22\x22);\x0avar \
h=\x22string\x22==type\
of c;h||(c=(JU?J\
U:J.util).Base64\
.getBase64(c).to\
String());e||(e=\
h?\x22\x22:\x22base64\x22);(\
h=a._serverUrl)&\
&0<=h.indexOf(\x22y\
our.server\x22)&&(h\
=\x22\x22);a._useDataU\
RI||!h?(e||(c=bt\
oa(c)),e=documen\
t.createElement(\
\x22a\x22),e.href=\x22dat\
a:\x22+d+\x22;base64,\x22\
+c,e.type=d||\x22te\
xt/plain\x22,e.down\
load=b,e.target=\
\x22_blank\x22,m(\x22body\
\x22).append(e),e.c\
lick(),e.remove(\
)):(a._formdiv||\
(a.$after(\x22body\x22\
,'<div id=\x22__jsm\
olformdiv__\x22 sty\
le=\x22display:none\
\x22>\x5ct\x5ct\x5ct\x5ct\x5ct\x5ct<f\
orm id=\x22__jsmolf\
orm__\x22 method=\x22p\
ost\x22 target=\x22_bl\
ank\x22 action=\x22\x22>\x5c\
t\x5ct\x5ct\x5ct\x5ct\x5ct<inpu\
t name=\x22call\x22 va\
lue=\x22saveFile\x22/>\
\x5ct\x5ct\x5ct\x5ct\x5ct\x5ct<inp\
ut id=\x22__jsmolmi\
metype__\x22 name=\x22\
mimetype\x22 value=\
\x22\x22/>\x5ct\x5ct\x5ct\x5ct\x5ct\x5ct\
<input id=\x22__jsm\
olencoding__\x22 na\
me=\x22encoding\x22 va\
lue=\x22\x22/>\x5ct\x5ct\x5ct\x5ct\
\x5ct\x5ct<input id=\x22_\
_jsmolfilename__\
\x22 name=\x22filename\
\x22 value=\x22\x22/>\x5ct\x5ct\
\x5ct\x5ct\x5ct\x5ct<textare\
a id=\x22__jsmoldat\
a__\x22 name=\x22data\x22\
></textarea>\x5ct\x5ct\
\x5ct\x5ct\x5ct\x5ct</form>\x5c\
t\x5ct\x5ct\x5ct\x5ct\x5ct</div\
>'),\x0aa._formdiv=\
\x22__jsmolform__\x22)\
,a.$attr(a._form\
div,\x22action\x22,h+\x22\
?\x22+(new Date).ge\
tMilliseconds())\
,a.$val(\x22__jsmol\
data__\x22,c),a.$va\
l(\x22__jsmolfilena\
me__\x22,b),a.$val(\
\x22__jsmolmimetype\
__\x22,d),a.$val(\x22_\
_jsmolencoding__\
\x22,e),a.$submit(\x22\
__jsmolform__\x22),\
a.$val(\x22__jsmold\
ata__\x22,\x22\x22),a.$va\
l(\x22__jsmolfilena\
me__\x22,\x22\x22));retur\
n\x22OK\x22};a._strToB\
ytes=function(a)\
{if(Clazz.instan\
ceOf(a,self.Arra\
yBuffer))return \
Clazz.newByteArr\
ay(-1,a);for(var\
 c=Clazz.newByte\
Array(a.length,0\
),d=a.length;0<=\
--d;)c[d]=a.char\
CodeAt(d)&255;re\
turn c};a._setCo\
nsoleDiv=\x0afuncti\
on(a){self.Clazz\
&&Clazz.setConso\
leDiv(a)};a._reg\
isterApplet=func\
tion(b,c){return\
 window[b]=a._ap\
plets[b]=a._appl\
ets[b+\x22__\x22+a._sy\
ncId+\x22__\x22]=c};a.\
_readyCallback=f\
unction(b,c,d,e,\
h){b=b.split(\x22_o\
bject\x22)[0];var k\
=a._applets[b];i\
f(d=d.booleanVal\
ue?d.booleanValu\
e():d)k._appletP\
anel=h||e,k._app\
let=e;a._track(k\
._readyCallback(\
b,c,d))};a._getW\
rapper=function(\
b,c){var d;if(c)\
{var e=\x22\x22;if(b._\
coverImage)var e\
=' onclick=\x22Jmol\
.coverApplet(ID,\
 false)\x22 title=\x22\
'+b._coverTitle+\
'\x22',h='<image id\
=\x22ID_coverclickg\
o\x22 src=\x22'+\x0ab._ma\
keLiveImage+'\x22 s\
tyle=\x22width:25px\
;height:25px;pos\
ition:absolute;b\
ottom:10px;left:\
10px;z-index:'+a\
._getZ(b,\x22coverI\
mage\x22)+';opacity\
:0.5;\x22'+e+\x22 />\x22,\
e='<div id=\x22ID_c\
overdiv\x22 style=\x22\
background-color\
:red;z-index:'+a\
._getZ(b,\x22coverI\
mage\x22)+';width:1\
00%;height:100%;\
display:inline;p\
osition:absolute\
;top:0px;left:0p\
x\x22><image id=\x22ID\
_coverimage\x22 src\
=\x22'+b._coverImag\
e+'\x22 style=\x22widt\
h:100%;height:10\
0%\x22'+e+\x22/>\x22+h+\x22<\
/div>\x22;h=b._isJa\
va?\x22\x22:'<image id\
=\x22ID_waitimage\x22 \
src=\x22'+b._j2sPat\
h+'/img/cursor_w\
ait.gif\x22 style=\x22\
display:none;pos\
ition:absolute;b\
ottom:10px;left:\
10px;z-index:'+\x0a\
a._getZ(b,\x22cover\
Image\x22)+';\x22 />';\
d=a._appletCssTe\
xt.replace(/\x5c'/g\
,'\x22');var k=b._g\
etSpinner&&b._ge\
tSpinner();b._sp\
inner=k=!k||\x22non\
e\x22==k?\x22\x22:\x22backgr\
ound-image:url(\x22\
+k+\x22); backgroun\
d-repeat:no-repe\
at; background-p\
osition:center;\x22\
;d=k+(0<=d.index\
Of('style=\x22')?d.\
split('style=\x22')\
[1]:'\x22 '+d);d='.\
..<div id=\x22ID_ap\
pletinfotablediv\
\x22 style=\x22width:W\
px;height:Hpx;po\
sition:relative;\
font-size:14px;t\
ext-align:left\x22>\
IMG WAIT......<d\
iv id=\x22ID_applet\
div\x22 style=\x22z-in\
dex:'+a._getZ(b,\
\x22header\x22)+\x22;widt\
h:100%;height:10\
0%;position:abso\
lute;top:0px;lef\
t:0px;\x22+\x0ad+\x22>\x22;v\
ar k=b._height,l\
=b._width;if(\x22st\
ring\x22!==typeof k\
||0>k.indexOf(\x22%\
\x22))k+=\x22px\x22;if(\x22s\
tring\x22!==typeof \
l||0>l.indexOf(\x22\
%\x22))l+=\x22px\x22;d=d.\
replace(/IMG/,e)\
.replace(/WAIT/,\
h).replace(/Hpx/\
g,k).replace(/Wp\
x/g,l)}else d='.\
.....</div>.....\
.<div id=\x22ID_2da\
ppletdiv\x22 style=\
\x22position:absolu\
te;width:100%;he\
ight:100%;overfl\
ow:hidden;displa\
y:none\x22></div>..\
....<div id=\x22ID_\
infotablediv\x22 st\
yle=\x22width:100%;\
height:100%;posi\
tion:absolute;to\
p:0px;left:0px\x22>\
.........<div id\
=\x22ID_infoheaderd\
iv\x22 style=\x22heigh\
t:20px;width:100\
%;background:yel\
low;display:none\
\x22><span id=\x22ID_i\
nfoheaderspan\x22><\
/span><span id=\x22\
ID_infocheckboxs\
pan\x22 style=\x22posi\
tion:absolute;te\
xt-align:right;r\
ight:1px;\x22><a hr\
ef=\x22javascript:J\
mol.showInfo(ID,\
false)\x22>[x]</a><\
/span></div>....\
.....<div id=\x22ID\
_infodiv\x22 style=\
\x22position:absolu\
te;top:20px;bott\
om:0px;width:100\
%;height:100%;ov\
erflow:auto\x22></d\
iv>......</div>.\
..</div>';\x0aretur\
n d.replace(/\x5c.\x5c\
.\x5c./g,\x22\x22).replac\
e(/[\x5cn\x5cr]/g,\x22\x22).\
replace(/ID/g,b.\
_id)};a._hideLoa\
dingSpinner=func\
tion(b){b._spinn\
er&&a.$css(a.$(b\
,\x22appletdiv\x22),{\x22\
background-image\
\x22:\x22\x22})};a._docum\
entWrite=functio\
n(b){if(a._docum\
ent){if(a._isXHT\
ML&&!a._XhtmlEle\
ment){var c=docu\
ment.getElements\
ByTagName(\x22scrip\
t\x22);a._XhtmlElem\
ent=c.item(c.len\
gth-1);a._XhtmlA\
ppendChild=!1}a.\
_XhtmlElement?a.\
_domWrite(b):a._\
document.write(b\
)}return b};a._d\
omWrite=function\
(b){for(var c=[0\
];c[0]<b.length;\
){var d=a._getDo\
mElement(b,c);if\
(!d)break;\x0aa._Xh\
tmlAppendChild?a\
._XhtmlElement.a\
ppendChild(d):a.\
_XhtmlElement.pa\
rentNode.insertB\
efore(d,_jmol.Xh\
tmlElement)}};a.\
_getDomElement=f\
unction(a,c){var\
 d=document.crea\
teElement(\x22span\x22\
);d.innerHTML=a;\
c[0]=a.length;re\
turn d};a._setOb\
ject=function(b,\
c,d){b._id=c;b._\
_Info={};d.z&&d.\
zIndexBase&&(a._\
z=a._getZOrders(\
d.zIndexBase));f\
or(var e in d)b.\
__Info[e]=d[e];(\
b._z=d.z)||d.zIn\
dexBase&&(b._z=b\
.__Info.z=a._get\
ZOrders(d.zIndex\
Base));b._width=\
d.width;b._heigh\
t=d.height;b._no\
script=!b._isJav\
a&&d.noscript;b.\
_console=\x0ad.cons\
ole;b._cacheFile\
s=!!d.cacheFiles\
;b._viewSet=null\
==d.viewSet||b._\
isJava?null:\x22Set\
\x22+d.viewSet;null\
!=b._viewSet&&(a\
.View.__init(b),\
b._currentView=n\
ull);!a._fileCac\
he&&b._cacheFile\
s&&(a._fileCache\
={});b._console|\
|(b._console=b._\
id+\x22_infodiv\x22);\x22\
none\x22==b._consol\
e&&(b._console=n\
ull);b._color=d.\
color?d.color.re\
place(/0x/,\x22#\x22):\
\x22#FFFFFF\x22;b._dis\
ableInitialConso\
le=d.disableInit\
ialConsole;b._no\
Monitor=d.disabl\
eJ2SLoadMonitor;\
a._j2sPath&&(d.j\
2sPath=a._j2sPat\
h);b._j2sPath=d.\
j2sPath;b._cover\
Image=d.coverIma\
ge;\x0ab._makeLiveI\
mage=d.makeLiveI\
mage||d.j2sPath+\
\x22/img/play_make_\
live.jpg\x22;b._isC\
overed=!!b._cove\
rImage;b._deferA\
pplet=d.deferApp\
let||b._isCovere\
d&&b._isJava;b._\
deferUncover=d.d\
eferUncover&&!b.\
_isJava;b._cover\
Script=d.coverSc\
ript;b._coverTit\
le=d.coverTitle;\
b._coverTitle||(\
b._coverTitle=b.\
_deferApplet?\x22ac\
tivate 3D model\x22\
:\x223D model is lo\
ading...\x22);b._co\
ntainerWidth=b._\
width+(b._width=\
=parseFloat(b._w\
idth)?\x22px\x22:\x22\x22);b\
._containerHeigh\
t=b._height+(b._\
height==parseFlo\
at(b._height)?\x22p\
x\x22:\x22\x22);b._info=\x22\
\x22;b._infoHeader=\
\x0ab._jmolType+' \x22\
'+b._id+'\x22';b._h\
asOptions=d.addS\
electionOptions;\
b._defaultModel=\
d.defaultModel;b\
._readyScript=d.\
script?d.script:\
\x22\x22;b._readyFunct\
ion=d.readyFunct\
ion;b._coverImag\
e&&!b._deferAppl\
et&&(b._readyScr\
ipt+=\x22;javascrip\
t \x22+c+\x22._display\
CoverImage(false\
)\x22);b._src=d.src\
};a._addDefaultI\
nfo=function(b,c\
){for(var d in c\
)\x22undefined\x22==ty\
peof b[d]&&(b[d]\
=c[d]);a._use&&(\
b.use=a._use);0<\
=b.use.indexOf(\x22\
SIGNED\x22)&&(0>b.j\
arFile.indexOf(\x22\
Signed\x22)&&(b.jar\
File=b.jarFile.r\
eplace(/Applet/,\
\x22AppletSigned\x22))\
,b.use=\x0ab.use.re\
place(/SIGNED/,\x22\
JAVA\x22),b.isSigne\
d=!0)};a._synced\
Applets=[];a._sy\
ncedCommands=[];\
a._syncedReady=[\
];a._syncReady=!\
1;a._isJmolJSVSy\
nc=!1;a._setRead\
y=function(b){a.\
_syncedReady[b]=\
1;for(var c=0,d=\
0;d<a._syncedApp\
lets.length;d++)\
{if(a._syncedApp\
lets[d]==b._id)a\
._syncedApplets[\
d]=b,a._syncedRe\
ady[d]=1;else if\
(!a._syncedReady\
[d])continue;c++\
}c==a._syncedApp\
lets.length&&a._\
setSyncReady()};\
a._setDestroy=fu\
nction(b){a.feat\
ureDetection.all\
owDestroy&&a.$wi\
ndowOn(\x22beforeun\
load\x22,function()\
{a._destroy(b)})\
};\x0aa._destroy=fu\
nction(b){try{b.\
_appletPanel&&b.\
_appletPanel.des\
troy();b._applet\
=null;a._unsetMo\
use(b._canvas);b\
._canvas=null;fo\
r(var c=0,d=0;d<\
a._syncedApplets\
.length;d++)a._s\
yncedApplets[d]=\
=b&&(a._syncedAp\
plets[d]=null),a\
._syncedApplets[\
d]&&c++;0<c||a._\
clearVars()}catc\
h(e){}};a._setSy\
ncReady=function\
(){a._syncReady=\
!0;for(var b=\x22\x22,\
c=0;c<a._syncedA\
pplets.length;c+\
+)a._syncedComma\
nds[c]&&(b+=\x22Jmo\
l.script(Jmol._s\
yncedApplets[\x22+c\
+\x22], Jmol._synce\
dCommands[\x22+c+\x22]\
);\x22);setTimeout(\
b,50)};a._mySync\
Callback=\x0afuncti\
on(b,c){app=a._a\
pplets[b];if(app\
._viewSet)a.View\
.updateFromSync(\
app,c);else{if(!\
a._syncReady||!a\
._isJmolJSVSync)\
return 1;for(var\
 d=0;d<a._synced\
Applets.length;d\
++)0<=c.indexOf(\
a._syncedApplets\
[d]._syncKeyword\
)&&a._syncedAppl\
ets[d]._syncScri\
pt(c);return 0}}\
;a._getElement=f\
unction(a,c){ret\
urn document.get\
ElementById(a._i\
d+\x22_\x22+c)||{}};a.\
_evalJSON=functi\
on(a,c){a+=\x22\x22;if\
(!a)return[];if(\
\x22{\x22!=a.charAt(0)\
)return 0<=a.ind\
exOf(\x22 | \x22)&&(a=\
a.replace(/\x5c \x5c|\x5c\
 /g,\x22\x5cn\x22)),a;var\
 d=(new Function\
(\x22return \x22+a))()\
;\x0areturn!d?null:\
c&&void 0!=d[c]?\
d[c]:d};a._sortM\
essages=function\
(a){function c(a\
,b){return a[0]<\
b[0]?1:a[0]>b[0]\
?-1:0}if(!a||\x22ob\
ject\x22!=typeof a)\
return[];for(var\
 d=[],e=a.length\
-1;0<=e;e--)for(\
var h=0,k=a[e].l\
ength;h<k;h++)d[\
d.length]=a[e][h\
];if(0!=d.length\
)return d=d.sort\
(c)};a._setMouse\
Owner=function(b\
,c){null==b||c?a\
._mouseOwner=b:a\
._mouseOwner==b&\
&(a._mouseOwner=\
null)};a._jsGetM\
ouseModifiers=fu\
nction(a){var c=\
0;switch(a.butto\
n){case 0:c=16;b\
reak;case 1:c=8;\
break;case 2:c=4\
}a.shiftKey&&(c+\
=1);a.altKey&&\x0a(\
c+=8);a.ctrlKey&\
&(c+=2);return c\
};a._jsGetXY=fun\
ction(b,c){if(!b\
.applet._ready||\
a._touching&&0>c\
.type.indexOf(\x22t\
ouch\x22))return!1;\
var d=a.$offset(\
b.id),e,h=c.orig\
inalEvent;c.page\
X||(c.pageX=h.pa\
geX);c.pageY||(c\
.pageY=h.pageY);\
a._mousePageX=c.\
pageX;a._mousePa\
geY=c.pageY;h.ta\
rgetTouches&&h.t\
argetTouches[0]?\
(e=h.targetTouch\
es[0].pageX-d.le\
ft,d=h.targetTou\
ches[0].pageY-d.\
top):h.changedTo\
uches?(e=h.chang\
edTouches[0].pag\
eX-d.left,d=h.ch\
angedTouches[0].\
pageY-d.top):(e=\
c.pageX-d.left,d\
=c.pageY-d.top);\
return void 0==\x0a\
e?null:[Math.rou\
nd(e),Math.round\
(d),a._jsGetMous\
eModifiers(c)]};\
a._setCursor=fun\
ction(b,c){if(!b\
._isJava&&!b._re\
adingLocal){var \
d;switch(c){case\
 1:d=\x22crosshair\x22\
;break;case 3:d=\
\x22wait\x22;a.$setVis\
ible(a.$(b,\x22wait\
image\x22),!0);brea\
k;case 8:d=\x22ns-r\
esize\x22;break;cas\
e 12:d=\x22grab\x22;br\
eak;case 13:d=\x22m\
ove\x22;break;defau\
lt:a.$setVisible\
(a.$(b,\x22waitimag\
e\x22),!1),d=\x22defau\
lt\x22}b._canvas.st\
yle.cursor=d}};a\
._gestureUpdate=\
function(b,c){c.\
stopPropagation(\
);c.preventDefau\
lt();var d=c.ori\
ginalEvent;switc\
h(c.type){case \x22\
touchstart\x22:a._t\
ouching=\x0a!0;brea\
k;case \x22touchend\
\x22:a._touching=!1\
}if(!d.touches||\
2!=d.touches.len\
gth)return!1;swi\
tch(c.type){case\
 \x22touchstart\x22:b.\
_touches=[[],[]]\
;break;case \x22tou\
chmove\x22:var e=a.\
$offset(b.id),h=\
b._touches[0],k=\
b._touches[1];h.\
push([d.touches[\
0].pageX-e.left,\
d.touches[0].pag\
eY-e.top]);k.pus\
h([d.touches[1].\
pageX-e.left,d.t\
ouches[1].pageY-\
e.top]);d=h.leng\
th;3<d&&(h.shift\
(),k.shift());2<\
=d&&b.applet._pr\
ocessGesture(b._\
touches)}return!\
0};a._jsSetMouse\
=function(b){var\
 c=function(a){r\
eturn!a.target||\
0<=(\x22\x22+a.target.\
className).index\
Of(\x22swingjs-ui\x22)\
};\x0aa.$bind(b,\x22mo\
usedown touchsta\
rt\x22,function(d){\
if(c(d))return!0\
;a._setMouseOwne\
r(b,!0);d.stopPr\
opagation();var \
e=d.target[\x22data\
-UI\x22];(!e||!e.ha\
ndleJSEvent(b,50\
1,d))&&d.prevent\
Default();b.isDr\
agging=!0;if(\x22to\
uchstart\x22==d.typ\
e&&a._gestureUpd\
ate(b,d))return!\
!e;a._setConsole\
Div(b.applet._co\
nsole);var h=a._\
jsGetXY(b,d);h&&\
(2!=d.button&&a.\
Swing.hideMenus(\
b.applet),b.appl\
et._processEvent\
(501,h));return!\
!e});a.$bind(b,\x22\
mouseup touchend\
\x22,function(d){if\
(c(d))return!0;a\
._setMouseOwner(\
null);d.stopProp\
agation();\x0avar e\
=d.target[\x22data-\
UI\x22];(!e||!e.han\
dleJSEvent(b,502\
,d))&&d.preventD\
efault();b.isDra\
gging=!1;if(\x22tou\
chend\x22==d.type&&\
a._gestureUpdate\
(b,d))return!!e;\
(d=a._jsGetXY(b,\
d))&&b.applet._p\
rocessEvent(502,\
d);return!!e});a\
.$bind(b,\x22mousem\
ove touchmove\x22,f\
unction(d){if(c(\
d))return!0;if(a\
._mouseOwner&&a.\
_mouseOwner!=b&&\
a._mouseOwner.is\
Dragging){if(!a.\
_mouseOwner.mous\
eMove)return!0;a\
._mouseOwner.mou\
seMove(d);return\
!1}return a._dra\
g(b,d)});a._drag\
=function(b,c){c\
.stopPropagation\
();c.preventDefa\
ult();if(\x22touchm\
ove\x22==\x0ac.type&&a\
._gestureUpdate(\
b,c))return!1;va\
r e=a._jsGetXY(b\
,c);if(!e)return\
!1;b.isDragging|\
|(e[2]=0);var h=\
c.target[\x22data-U\
I\x22];b.isdragging\
&&(!h||h.handleJ\
SEvent(b,506,c))\
;b.applet._proce\
ssEvent(b.isDrag\
ging?506:503,e);\
return!!h};a.$bi\
nd(b,\x22DOMMouseSc\
roll mousewheel\x22\
,function(d){if(\
c(d))return!0;d.\
stopPropagation(\
);d.preventDefau\
lt();b.isDraggin\
g=!1;var e=d.ori\
ginalEvent,e=e.d\
etail?e.detail:(\
\x22mac\x22==a.feature\
Detection.os?1:-\
1)*e.wheelDelta;\
d=a._jsGetMouseM\
odifiers(d);b.ap\
plet._processEve\
nt(-1,[0>e?-1:\x0a1\
,0,d]);return!1}\
);a.$bind(b,\x22con\
textmenu\x22,functi\
on(){return!1});\
a.$bind(b,\x22mouse\
out\x22,function(d)\
{if(c(d))return!\
0;a._mouseOwner&\
&!a._mouseOwner.\
mouseMove&&a._se\
tMouseOwner(null\
);b.applet._appl\
etPanel&&b.apple\
t._appletPanel.s\
tartHoverWatcher\
(!1);a._jsGetXY(\
b,d);return!1});\
a.$bind(b,\x22mouse\
enter\x22,function(\
d){if(c(d))retur\
n!0;b.applet._ap\
pletPanel&&b.app\
let._appletPanel\
.startHoverWatch\
er(!0);if(0===d.\
buttons||0===d.w\
hich){b.isDraggi\
ng=!1;d=a._jsGet\
XY(b,d);if(!d)re\
turn!1;b.applet.\
_processEvent(50\
4,d);\x0ab.applet._\
processEvent(502\
,d);return!1}});\
a.$bind(b,\x22mouse\
moveoutjsmol\x22,fu\
nction(d,e,h){if\
(c(h))return!0;i\
f(b==a._mouseOwn\
er&&b.isDragging\
)return a._drag(\
b,h)});b.applet.\
_is2D&&a.$resize\
(function(){b.ap\
plet&&b.applet._\
resize()});a.$bi\
nd(\x22body\x22,\x22mouse\
up touchend\x22,fun\
ction(d){if(c(d)\
)return!0;b.appl\
et&&(b.isDraggin\
g=!1);a._setMous\
eOwner(null)})};\
a._jsUnsetMouse=\
function(b){b.ap\
plet=null;a.$bin\
d(b,\x22mousedown t\
ouchstart mousem\
ove touchmove mo\
useup touchend D\
OMMouseScroll mo\
usewheel context\
menu mouseout mo\
useenter\x22,\x0anull)\
;a._setMouseOwne\
r(null)};a.Swing\
={count:0,menuIn\
itialized:0,menu\
Counter:0,htDial\
ogs:{}};var s=a.\
Swing;SwingContr\
oller=s;s.setDra\
ggable=function(\
b){b=b.prototype\
;b.setContainer|\
|(b.setContainer\
=function(b){thi\
s.container=b;b.\
obj=this;this.ig\
noreMouse=this.i\
sDragging=!1;var\
 d=this;b.bind(\x22\
mousedown touchs\
tart\x22,function(b\
){if(d.ignoreMou\
se)return d.igno\
reMouse=!1,!0;a.\
_setMouseOwner(d\
,!0);d.isDraggin\
g=!0;d.pageX=b.p\
ageX;d.pageY=b.p\
ageY;return!1});\
b.bind(\x22mousemov\
e touchmove\x22,fun\
ction(b){if(d.is\
Dragging&&\x0aa._mo\
useOwner==d)retu\
rn d.mouseMove(b\
),!1});b.bind(\x22m\
ouseup touchend\x22\
,function(b){d.m\
ouseUp(b);a._set\
MouseOwner(null)\
})},b.mouseUp=fu\
nction(b){if(thi\
s.isDragging&&a.\
_mouseOwner==thi\
s)return this.pa\
geX0+=b.pageX-th\
is.pageX,this.pa\
geY0+=b.pageY-th\
is.pageY,this.is\
Dragging=!1;a._s\
etMouseOwner(nul\
l)},b.setPositio\
n=function(){if(\
null===a._mouseP\
ageX){var b=a.$o\
ffset(this.apple\
t._id+\x22_\x22+(this.\
applet._is2D?\x22ca\
nvas2d\x22:\x22canvas\x22\
));a._mousePageX\
=b.left;a._mouse\
PageY=b.top}this\
.pageX0=a._mouse\
PageX;this.pageY\
0=\x0aa._mousePageY\
;this.container.\
css({top:a._mous\
ePageY+\x22px\x22,left\
:a._mousePageX+\x22\
px\x22})},b.mouseMo\
ve=function(b){i\
f(this.isDraggin\
g&&a._mouseOwner\
==this){this.tim\
estamp=System.cu\
rrentTimeMillis(\
);var d=this.pag\
eX0+(b.pageX-thi\
s.pageX);b=this.\
pageY0+(b.pageY-\
this.pageY);a._m\
ousePageX=d;a._m\
ousePageY=b;this\
.container.css({\
top:b+\x22px\x22,left:\
d+\x22px\x22})}},b.dra\
gBind=function(b\
){this.applet._i\
gnoreMouse=!b;th\
is.container.unb\
ind(\x22mousemoveou\
tjsmol\x22);this.co\
ntainer.unbind(\x22\
touchmoveoutjsmo\
l\x22);this.contain\
er.unbind(\x22mouse\
upoutjsmol\x22);\x0ath\
is.container.unb\
ind(\x22touchendout\
jsmol\x22);a._setMo\
useOwner(null);i\
f(b){var d=this;\
this.container.b\
ind(\x22mousemoveou\
tjsmol touchmove\
outjsmol\x22,functi\
on(a,b,c){d.mous\
eMove(c)});this.\
container.bind(\x22\
mouseupoutjsmol \
touchendoutjsmol\
\x22,function(a,b,c\
){d.mouseUp(c)})\
}})};s.JSDialog=\
function(){};s.s\
etDraggable(s.JS\
Dialog);s.getScr\
eenDimensions=fu\
nction(a){a.widt\
h=m(window).widt\
h();a.height=m(w\
indow).height()}\
;s.dispose=funct\
ion(b){a.$remove\
(b.id+\x22_mover\x22);\
delete s.htDialo\
gs[b.id];b.conta\
iner.obj.dragBin\
d(!1)};\x0as.regist\
er=function(a,c)\
{a.id=c+ ++s.cou\
nt;s.htDialogs[a\
.id]=a};s.setDia\
log=function(b){\
a._setMouseOwner\
(null);a.$remove\
(b.id);var c=b.i\
d+\x22_mover\x22,d=a._\
$(c),e;d[0]?(d.h\
tml(b.html),e=d[\
0].jd):(a.$after\
(\x22body\x22,\x22<div id\
='\x22+c+\x22' style='\
position:absolut\
e;left:0px;top:0\
px;'>\x22+b.html+\x22<\
/div>\x22),e=new s.\
JSDialog,d=a._$(\
c),b.container=d\
,e.applet=b.mana\
ger.vwr.html5App\
let,e.setContain\
er(d),e.dialog=b\
,e.setPosition()\
,e.dragBind(!0),\
d[0].jd=e);a.$bi\
nd(\x22#\x22+b.id+\x22 .J\
Button\x22,\x22mousedo\
wn touchstart\x22,f\
unction(){e.igno\
reMouse=\x0a!0});a.\
$bind(\x22#\x22+b.id+\x22\
 .JComboBox\x22,\x22mo\
usedown touchsta\
rt\x22,function(){e\
.ignoreMouse=!0}\
);a.$bind(\x22#\x22+b.\
id+\x22 .JCheckBox\x22\
,\x22mousedown touc\
hstart\x22,function\
(){e.ignoreMouse\
=!0});a.$bind(\x22#\
\x22+b.id+\x22 .JTextF\
ield\x22,\x22mousedown\
 touchstart\x22,fun\
ction(){e.ignore\
Mouse=!0});a.$bi\
nd(\x22#\x22+b.id+\x22 .J\
Table\x22,\x22mousedow\
n touchstart\x22,fu\
nction(){e.ignor\
eMouse=!0});a.$b\
ind(\x22#\x22+b.id+\x22 .\
JScrollPane\x22,\x22mo\
usedown touchsta\
rt\x22,function(){e\
.ignoreMouse=!0}\
);a.$bind(\x22#\x22+b.\
id+\x22 .JEditorPan\
e\x22,\x22mousedown to\
uchstart\x22,functi\
on(){e.ignoreMou\
se=\x0a!0})};s.setS\
elected=function\
(b){a.$prop(b.id\
,\x22checked\x22,!!b.s\
elected)};s.setS\
electedIndex=fun\
ction(b){a.$prop\
(b.id,\x22selectedI\
ndex\x22,b.selected\
Index)};s.setTex\
t=function(b){a.\
$prop(b.id,\x22valu\
e\x22,b.text)};s.se\
tVisible=functio\
n(b){a.$setVisib\
le(b.id,b.visibl\
e)};s.setEnabled\
=function(b){a.$\
setEnabled(b.id,\
b.enabled)};s.cl\
ick=function(b,c\
){var d=s.htDial\
ogs[b.id];if(d){\
var e=d.toString\
();if(0<=e.index\
Of(\x22JCheck\x22))d.s\
elected=b.checke\
d;else if(0<=e.i\
ndexOf(\x22JCombo\x22)\
)d.selectedIndex\
=b.selectedIndex\
;else if(null!=\x0a\
d.text&&(d.text=\
b.value,c&&13!=(\
c.charCode||c.ke\
yCode)))return}e\
=s.htDialogs[a.$\
getAncestorDiv(b\
.id,\x22JDialog\x22).i\
d];e.manager.act\
ionPerformed(d?d\
.name:e.registry\
Key+\x22/\x22+b.id)};s\
.setFront=functi\
on(b){var c=b.ma\
nager.vwr.html5A\
pplet;b.zIndex!=\
a._getZ(c,\x22dialo\
g\x22)&&(b.zIndex=a\
._incrZ(c,\x22dialo\
g\x22));b.container\
&&((b.container[\
0]||b.container)\
.style.zIndex=b.\
zIndex)};s.hideM\
enus=function(a)\
{if(a=a._menus)f\
or(var c in a)a[\
c].visible&&s.hi\
deMenu(a[c])};s.\
windowClosing=fu\
nction(b){b=s.ht\
Dialogs[a.$getAn\
cestorDiv(b.id,\x0a\
\x22JDialog\x22).id];b\
.registryKey?b.m\
anager.processWi\
ndowClosing(b.re\
gistryKey):b.dis\
pose()};a._track\
=function(b){if(\
a._tracker){try{\
var c='<iframe s\
tyle=\x22display:no\
ne\x22 width=\x220\x22 he\
ight=\x220\x22 framebo\
rder=\x220\x22 tabinde\
x=\x22-1\x22 src=\x22'+(a\
._tracker+\x22&appl\
et=\x22+b._jmolType\
+\x22&version=\x22+a._\
version+\x22&appver\
=\x22+a.___JmolVers\
ion+\x22&url=\x22+enco\
deURIComponent(d\
ocument.location\
.href))+'\x22></ifr\
ame>';a.$after(\x22\
body\x22,c)}catch(d\
){}delete a._tra\
cker}return b};v\
ar u;a.getProfil\
e=function(a){if\
(self.Clazz&&sel\
f.JSON)return u|\
|Clazz._startPro\
filing(u=\x0a0==arg\
uments.length||a\
),Clazz.getProfi\
le()};a._getInCh\
IKey=function(a,\
c){0<=c.indexOf(\
\x22MOL=\x22)&&c.split\
(\x22MOL=\x22)[1].spli\
t('\x22')};a._getAt\
tr=function(a,c)\
{var d=a.indexOf\
(c+\x22=\x22);return 0\
<=d&&0<=(d=a.ind\
exOf('\x22',d))?a.s\
ubstring(d+1,a.i\
ndexOf('\x22',d+1))\
:null};a.User={v\
iewUpdatedCallba\
ck:null};a.View=\
{count:0,applets\
:{},sets:{}};(fu\
nction(b){b.upda\
teView=function(\
c,d){if(null!=c.\
_viewSet){d.chem\
ID||(c._searchQu\
ery=null);d.data\
||(d.data=\x22N/A\x22)\
;d.type=c._viewT\
ype;if(null==(c.\
_currentView=b._\
_findView(c._vie\
wSet,\x0ad)))c._cur\
rentView=b.__cre\
ateViewSet(c._vi\
ewSet,d.chemID,d\
.viewID||d.chemI\
D);c._currentVie\
w[d.type].data=d\
.data;c._current\
View[d.type].smi\
les=c._getSmiles\
();a.User.viewUp\
datedCallback&&a\
.User.viewUpdate\
dCallback(c,\x22upd\
ateView\x22);b.__se\
tView(c._current\
View,c,!1)}};b.u\
pdateFromSync=fu\
nction(c,d){c._u\
pdateMsg=d;var e\
=a._getAttr(d,\x22s\
ourceID\x22)||a._ge\
tAttr(d,\x22file\x22);\
if(e){var h=b.__\
findView(c._view\
Set,{viewID:e});\
if(null==h)retur\
n a.updateView(c\
,d);h!=c._curren\
tView&&b.__setVi\
ew(h,c,!0);var k\
=(e=a._getAttr(d\
,\x0a\x22atoms\x22))&&0<=\
d.indexOf(\x22selec\
tionhalos ON\x22)?e\
val(\x22[\x22+e+\x22]\x22):[\
];setTimeout(fun\
ction(){c._curre\
ntView==h&&b.upd\
ateAtomPick(c,k)\
},10);a.User.vie\
wUpdatedCallback\
&&a.User.viewUpd\
atedCallback(c,\x22\
updateFromSync\x22)\
}};b.updateAtomP\
ick=function(b,d\
){var e=b._curre\
ntView;if(null!=\
e){for(var h in \
e)\x22info\x22!=h&&e[h\
].applet!=b&&e[h\
].applet._update\
AtomPick(d);a.Us\
er.viewUpdatedCa\
llback&&a.User.v\
iewUpdatedCallba\
ck(b,\x22updateAtom\
Pick\x22)}};b.dumpV\
iews=function(a)\
{var d=b.sets[a]\
;if(d){var e=\x22Vi\
ew set \x22+a+\x22:\x5cn\x22\
;a=b.applets[a];\
\x0afor(var h in a)\
e+=\x22\x5cnapplet \x22+a\
[h]._id+\x22 curren\
tView=\x22+(a[h]._c\
urrentView?a[h].\
_currentView.inf\
o.viewID:null);f\
or(h=d.length;0<\
=--h;){a=d[h];va\
r e=e+(\x22\x5cn\x5cn<b>v\
iew=\x22+h+\x22 viewID\
=\x22+a.info.viewID\
+\x22 chemID=\x22+a.in\
fo.chemID+\x22</b>\x5c\
n\x22),k,l;for(l in\
 a)\x22info\x22!=l&&(e\
+=\x22\x5cnview=\x22+h+\x22 \
type=\x22+l+\x22 apple\
t=\x22+((k=a[l]).ap\
plet?k.applet._i\
d:null)+\x22 SMILES\
=\x22+k.smiles+\x22\x5cn \
atomMap=\x22+JSON.s\
tringify(k.atomM\
ap)+\x22\x5cn data=\x5cn\x22\
+k.data+\x22\x5cn\x22)}re\
turn e}};b.__ini\
t=function(a){va\
r d=a._viewSet,e\
=b.applets;e[d]|\
|(e[d]={});e[d][\
a._viewType]=\x0aa}\
;b.__findView=fu\
nction(a,d){var \
e=b.sets[a];null\
==e&&(e=b.sets[a\
]=[]);for(var h=\
e.length;0<=--h;\
){var k=e[h];if(\
d.viewID){if(k.i\
nfo.viewID==d.vi\
ewID)return k}el\
se{if(null!=d.ch\
emID&&d.chemID==\
k.info.chemID)re\
turn k;for(var l\
 in k)if(\x22info\x22!\
=l&&(null!=d.dat\
a&&null!=k[l].da\
ta?d.data==k[l].\
data:d.type==l))\
return k}}return\
 null};b.__creat\
eViewSet=functio\
n(c,d,e){b.count\
++;d={info:{chem\
ID:d,viewID:e||\x22\
model_\x22+b.count}\
};for(var h in a\
._applets)e=a._a\
pplets[h],e._vie\
wSet==c&&(d[e._v\
iewType]={applet\
:e,\x0adata:null});\
b.sets[c].push(d\
);return d};b.__\
setView=function\
(a,b,e){for(var \
h in a)if(\x22info\x22\
!=h){var k=a[h],\
l=k.applet,q=e||\
null!=l&&\x22<modif\
ied>\x22==l._molDat\
a;if(!(null==l||\
l==b&&!q)){var m\
=null==k.data,s=\
null!=l._current\
View;l._currentV\
iew=a;if(!s||!(a\
[h].data==k.data\
&&!m&!q))if(l._l\
oadModelFromView\
(a),m)break}}}})\
(a.View);a.Cache\
={fileCache:{}};\
a.Cache.get=func\
tion(b){return a\
.Cache.fileCache\
[b]};a.Cache.put\
=function(b,c){a\
.Cache.fileCache\
[b]=c};a.Cache.s\
etDragDrop=funct\
ion(b){a.$appEve\
nt(b,\x22appletdiv\x22\
,\x0a\x22dragover\x22,fun\
ction(a){a=a.ori\
ginalEvent;a.sto\
pPropagation();a\
.preventDefault(\
);a.dataTransfer\
.dropEffect=\x22cop\
y\x22});a.$appEvent\
(b,\x22appletdiv\x22,\x22\
drop\x22,function(c\
){var d=c.origin\
alEvent;d.stopPr\
opagation();d.pr\
eventDefault();v\
ar e=d.dataTrans\
fer.files[0];if(\
null==e)try{e=\x22\x22\
+d.dataTransfer.\
getData(\x22text\x22),\
(0==e.indexOf(\x22f\
ile:/\x22)||0==e.in\
dexOf(\x22http:/\x22))\
&&b._scriptLoad(\
e)}catch(h){}els\
e d=new FileRead\
er,d.onloadend=f\
unction(d){if(d.\
target.readyStat\
e==FileReader.DO\
NE){var h=\x22cache\
://DROP_\x22+e.name\
;d=Clazz.newByte\
Array(-1,\x0ad.targ\
et.result);h.end\
sWith(\x22.spt\x22)||b\
._appletPanel.ca\
cheFileByName(\x22c\
ache://DROP_*\x22,!\
1);\x22JSV\x22==b._vie\
wType||h.endsWit\
h(\x22.jdx\x22)?a.Cach\
e.put(h,d):b._ap\
pletPanel.cacheP\
ut(h,d);(d=a._js\
GetXY(b._canvas,\
c))&&(!b._applet\
Panel.setStatusD\
ragDropped||b._a\
ppletPanel.setSt\
atusDragDropped(\
0,d[0],d[1],h))&\
&b._appletPanel.\
openFileAsyncSpe\
cial(h,1)}},d.re\
adAsArrayBuffer(\
e)})}})(Jmol,jQu\
ery);Jmol._debug\
Code=!1;\x0a(functi\
on(a){a._isAsync\
=!1;a._asyncCall\
backs={};a._core\
Files=[];var m=!\
1,k=[],h=[],e=0,\
l=[],q=[],s=func\
tion(b){argument\
s.length||(b=!0)\
;delete e;for(va\
r d;0<h.length&&\
\x22done\x22==(d=h[0])\
[4];)h.shift();i\
f(0!=h.length)if\
(!a._isAsync&&!b\
)setTimeout(s,10\
);else{d.push(\x22d\
one\x22);var l=\x22JSm\
ol exec \x22+d[0]._\
id+\x22 \x22+d[3]+\x22 \x22+\
d[2];self.System\
&&System.out.pri\
ntln(l);self.con\
sole&&console.lo\
g(l+\x22 -- OK\x22);k.\
push(l);d[1](d[0\
],d[2])}},u=func\
tion(b){m?s():(m\
=!0,LoadClazz(),\
b._noMonitor&&(C\
lazz._LoaderProg\
ressMonitor.show\
Status=\x0afunction\
(){}),LoadClazz=\
null,b.__Info.un\
compressed&&Claz\
z.loadClass(),Cl\
azz._Loader.onGl\
obalLoaded=funct\
ion(){Clazz._Loa\
derProgressMonit\
or.showStatus(\x22A\
pplication loade\
d.\x22,!0);if(!a._d\
ebugCode||!a.hav\
eCore)a.haveCore\
=!0,s()},Clazz._\
Loader.loadPacka\
geClasspath(\x22jav\
a\x22,null,!0,s))},\
b=function(a,b){\
Clazz._Loader.lo\
adClass(b,functi\
on(){s()})};a.sh\
owExecLog=functi\
on(){return k.jo\
in(\x22\x5cn\x22)};a._add\
Exec=function(a)\
{a[1]||(a[1]=b);\
var d=\x22JSmol loa\
d \x22+a[0]._id+\x22 \x22\
+a[3];self.conso\
le&&console.log(\
d+\x22...\x22);k.push(\
d);\x0ah.push(a)};a\
._addCoreFile=fu\
nction(b,d,e){b=\
b.toLowerCase().\
split(\x22.\x22)[0];if\
(!(0<=l.join(\x22\x22)\
.indexOf(b))){l.\
push(b);l.sort()\
;a._coreFiles=[d\
+\x22/core/core\x22+l.\
join(\x22\x22)+\x22.z.js\x22\
];if(e&&(e=e.spl\
it(\x22 \x22)))for(b=0\
;b<e.length;b++)\
0>q.join(\x22\x22).ind\
exOf(e[b])&&q.pu\
sh(d+\x22/core/core\
\x22+e[b]+\x22.z.js\x22);\
for(b=0;b<q.leng\
th;b++)a._coreFi\
les.push(q[b])}}\
;a._Canvas2D=fun\
ction(b,d,e,h){t\
his._uniqueId=(\x22\
\x22+Math.random())\
.substring(3);th\
is._id=b;this._i\
s2D=!0;this._isJ\
ava=!1;this._jmo\
lType=\x22Jmol._Can\
vas2D (\x22+e+\x22)\x22;t\
his._isLayered=\x0a\
d._isLayered||!1\
;this._isSwing=d\
._isSwing||!1;th\
is._isJSV=d._isJ\
SV||!1;this._isA\
stex=d._isAstex|\
|!1;this._platfo\
rm=d._platform||\
\x22\x22;if(h)return t\
his;window[b]=th\
is;this._createC\
anvas(b,d);if(!a\
._document||this\
._deferApplet)re\
turn this;this._\
init();return th\
is};a._setApplet\
Params=function(\
b,d,e,h){for(var\
 k in e)if(!b||0\
<=b.indexOf(\x22;\x22+\
k.toLowerCase()+\
\x22;\x22))null==e[k]|\
|\x22language\x22==k&&\
!a.featureDetect\
ion.supportsLoca\
lization()||(h?d\
.put(k,!0===e[k]\
?Boolean.TRUE:!1\
===e[k]?Boolean.\
FALSE:e[k]):d[k]\
=e[k])};\x0aa._jsSe\
tPrototype=funct\
ion(b){b._init=f\
unction(){this._\
setupJS();this._\
showInfo(!0);thi\
s._disableInitia\
lConsole&&this._\
showInfo(!1)};b.\
_createCanvas=fu\
nction(b,c,e){a.\
_setObject(this,\
b,c);e&&(this._G\
Lmol=e,this._GLm\
ol.applet=this,t\
his._GLmol.id=th\
is._id);e=a._get\
Wrapper(this,!0)\
;this._deferAppl\
et||(a._document\
?(a._documentWri\
te(e),this._newC\
anvas(!1),e=\x22\x22):\
(this._deferAppl\
et=!0,e+='<scrip\
t type=\x22text/jav\
ascript\x22>'+b+\x22._\
cover(false)\x5cx3c\
/script>\x22));e+=a\
._getWrapper(thi\
s,!1);c.addSelec\
tionOptions&&(e+\
=\x0aa._getGrabberO\
ptions(this));a.\
_debugAlert&&!a.\
_document&&alert\
(e);this._code=a\
._documentWrite(\
e)};b._newCanvas\
=function(a){thi\
s._is2D?this._cr\
eateCanvas2d(a):\
this._GLmol.crea\
te()};b._getHtml\
5Canvas=function\
(){return this._\
canvas};b._getWi\
dth=function(){r\
eturn this._canv\
as.width};b._get\
Height=function(\
){return this._c\
anvas.height};b.\
_getContentLayer\
=function(){retu\
rn a.$(this,\x22con\
tentLayer\x22)[0]};\
b._repaintNow=fu\
nction(){a._repa\
int(this,!1)};b.\
_createCanvas2d=\
function(){var b\
=a.$(this,\x22apple\
tdiv\x22);\x0atry{b[0]\
.removeChild(thi\
s._canvas),this.\
_canvas.frontLay\
er&&b[0].removeC\
hild(this._canva\
s.frontLayer),th\
is._canvas.rearL\
ayer&&b[0].remov\
eChild(this._can\
vas.rearLayer),t\
his._canvas.cont\
entLayer&&b[0].r\
emoveChild(this.\
_canvas.contentL\
ayer),a._jsUnset\
Mouse(this._mous\
eInterface)}catc\
h(c){}var e=Math\
.round(b.width()\
),h=Math.round(b\
.height()),k=doc\
ument.createElem\
ent(\x22canvas\x22);k.\
applet=this;this\
._canvas=k;k.sty\
le.width=\x22100%\x22;\
k.style.height=\x22\
100%\x22;k.width=e;\
k.height=h;k.id=\
this._id+\x22_canva\
s2d\x22;b.append(k)\
;\x0aa._$(k.id).css\
({\x22z-index\x22:a._g\
etZ(this,\x22main\x22)\
});if(this._isLa\
yered){var l=doc\
ument.createElem\
ent(\x22div\x22);k.con\
tentLayer=l;l.id\
=this._id+\x22_cont\
entLayer\x22;b.appe\
nd(l);a._$(l.id)\
.css({zIndex:a._\
getZ(this,\x22image\
\x22),position:\x22abs\
olute\x22,left:\x220px\
\x22,top:\x220px\x22,widt\
h:(this._isSwing\
?e:0)+\x22px\x22,heigh\
t:(this._isSwing\
?h:0)+\x22px\x22,overf\
low:\x22hidden\x22});t\
his._isSwing?(b=\
document.createE\
lement(\x22div\x22),b.\
id=this._id+\x22_sw\
ingdiv\x22,a._$(thi\
s._id+\x22_appletin\
fotablediv\x22).app\
end(b),a._$(b.id\
).css({zIndex:a.\
_getZ(this,\x22rear\
\x22),position:\x22abs\
olute\x22,\x0aleft:\x220p\
x\x22,top:\x220px\x22,wid\
th:e+\x22px\x22,height\
:h+\x22px\x22,overflow\
:\x22hidden\x22}),this\
._mouseInterface\
=k.contentLayer,\
k.contentLayer.a\
pplet=this):this\
._mouseInterface\
=this._getLayer(\
\x22front\x22,b,e,h,!1\
)}else this._mou\
seInterface=k;a.\
_jsSetMouse(this\
._mouseInterface\
)};b._getLayer=f\
unction(b,c,e,h,\
k){var l=documen\
t.createElement(\
\x22canvas\x22);this._\
canvas[b+\x22Layer\x22\
]=l;l.style.widt\
h=\x22100%\x22;l.style\
.height=\x22100%\x22;l\
.id=this._id+\x22_\x22\
+b+\x22Layer\x22;l.wid\
th=e;l.height=h;\
c.append(l);l.ap\
plet=this;a._$(l\
.id).css({backgr\
ound:k?\x22rgb(0,0,\
0,1)\x22:\x0a\x22rgb(0,0,\
0,0.001)\x22,\x22z-ind\
ex\x22:a._getZ(this\
,b),position:\x22ab\
solute\x22,left:\x220p\
x\x22,top:\x220px\x22,ove\
rflow:\x22hidden\x22})\
;return l};b._se\
tupJS=function()\
{window[\x22j2s.lib\
\x22]={base:this._j\
2sPath+\x22/\x22,alias\
:\x22.\x22,console:thi\
s._console,monit\
orZIndex:a._getZ\
(this,\x22monitorZI\
ndex\x22)};0==h.len\
gth&&a._addExec(\
[this,u,null,\x22lo\
adClazz\x22]);this.\
_addCoreFiles();\
a._addExec([this\
,this.__startApp\
letJS,null,\x22star\
t applet\x22]);this\
._isSigned=!0;th\
is._ready=!1;thi\
s._applet=null;t\
his._canScript=f\
unction(){return\
!0};this._savedO\
rientations=\x0a[];\
e&&clearTimeout(\
e);e=setTimeout(\
s,100)};b.__star\
tAppletJS=functi\
on(b){0==a._vers\
ion.indexOf(\x22$Da\
te: \x22)&&(a._vers\
ion=(a._version.\
substring(7)+\x22 -\
\x22).split(\x22 -\x22)[0\
]+\x22 (JSmol/j2s)\x22\
);var c=Clazz._4\
Name(\x22java.util.\
Hashtable\x22).newI\
nstance();a._set\
AppletParams(b._\
availableParams,\
c,b.__Info,!0);c\
.put(\x22appletRead\
yCallback\x22,\x22Jmol\
._readyCallback\x22\
);c.put(\x22applet\x22\
,!0);c.put(\x22name\
\x22,b._id);c.put(\x22\
syncId\x22,a._syncI\
d);a._isAsync&&c\
.put(\x22async\x22,!0)\
;b._color&&c.put\
(\x22bgcolor\x22,b._co\
lor);b._startupS\
cript&&c.put(\x22sc\
ript\x22,\x0ab._startu\
pScript);a._sync\
edApplets.length\
&&c.put(\x22synccal\
lback\x22,\x22Jmol._my\
SyncCallback\x22);c\
.put(\x22signedAppl\
et\x22,\x22true\x22);c.pu\
t(\x22platform\x22,b._\
platform);b._is2\
D&&c.put(\x22displa\
y\x22,b._id+\x22_canva\
s2d\x22);c.put(\x22doc\
umentBase\x22,docum\
ent.location.hre\
f);var e=b._j2sP\
ath+\x22/\x22;if(0>e.i\
ndexOf(\x22://\x22)){v\
ar h=document.lo\
cation.href.spli\
t(\x22#\x22)[0].split(\
\x22?\x22)[0].split(\x22/\
\x22);0==e.indexOf(\
\x22/\x22)?h=[h[0],e.s\
ubstring(1)]:h[h\
.length-1]=e;e=h\
.join(\x22/\x22)}c.put\
(\x22codePath\x22,e);a\
._registerApplet\
(b._id,b);try{b.\
_newApplet(c)}ca\
tch(k){System.ou\
t.println((a._is\
Async?\x0a\x22normal a\
sync abort from \
\x22:\x22\x22)+k);return}\
b._jsSetScreenDi\
mensions();s()};\
b._restoreState|\
|(b._restoreStat\
e=function(){});\
b._jsSetScreenDi\
mensions=functio\
n(){if(this._app\
letPanel){var b=\
a._getElement(th\
is,this._is2D?\x22c\
anvas2d\x22:\x22canvas\
\x22);this._appletP\
anel.setScreenDi\
mension(b.width,\
b.height)}};b._s\
how=function(b){\
a.$setVisible(a.\
$(this,\x22appletdi\
v\x22),b);b&&a._rep\
aint(this,!0)};b\
._canScript=func\
tion(){return!0}\
;b.equals=functi\
on(a){return thi\
s==a};b.clone=fu\
nction(){return \
this};b.hashCode\
=function(){retu\
rn parseInt(this\
._uniqueId)};\x0ab.\
_processGesture=\
function(a){retu\
rn this._appletP\
anel.processTwoP\
ointGesture(a)};\
b._processEvent=\
function(a,b){th\
is._appletPanel.\
processMouseEven\
t(a,b[0],b[1],b[\
2],System.curren\
tTimeMillis())};\
b._resize=functi\
on(){var b=\x22__re\
sizeTimeout_\x22+th\
is._id;a[b]&&cle\
arTimeout(a[b]);\
var c=this;a[b]=\
setTimeout(funct\
ion(){a._repaint\
(c,!0);a[b]=null\
},100)};return b\
};a._repaint=fun\
ction(b,e){if(b&\
&b._appletPanel)\
{var h=a.$(b,\x22ap\
pletdiv\x22),k=Math\
.round(h.width()\
),h=Math.round(h\
.height());if(b.\
_is2D&&(b._canva\
s.width!=\x0ak||b._\
canvas.height!=h\
))b._newCanvas(!\
0),b._appletPane\
l.setDisplay(b._\
canvas);b._apple\
tPanel.setScreen\
Dimension(k,h);k\
=function(){b._a\
ppletPanel.paint\
?b._appletPanel.\
paint(null):b._a\
ppletPanel.updat\
e(null)};e?reque\
stAnimationFrame\
(k):k()}};a._loa\
dImage=function(\
b,e,h,k,l,q){var\
 m=\x22echo_\x22+e+h+(\
k?\x22_\x22+k.length:\x22\
\x22),s=a._getHidde\
nCanvas(b.vwr.ht\
ml5Applet,m,0,0,\
!1,!0);if(null==\
s){if(null==q){q\
=new Image;if(nu\
ll==k)return q.o\
nload=function()\
{a._loadImage(b,\
e,h,null,l,q)},q\
.src=h,null;Syst\
em.out.println(\x22\
Jsmol.js Jmol._l\
oadImage using d\
ata URI for \x22+\x0am\
);q.src=\x22string\x22\
==typeof k?k:\x22da\
ta:\x22+JU.Rdr.gues\
sMimeTypeForByte\
s(k)+\x22;base64,\x22+\
JU.Base64.getBas\
e64(k)}var u=q.w\
idth,U=q.height;\
\x22webgl\x22==e&&(u/=\
2,U/=2);s=a._get\
HiddenCanvas(b.v\
wr.html5Applet,m\
,u,U,!0,!1);s.im\
ageWidth=u;s.ima\
geHeight=U;s.id=\
m;s.image=q;a._s\
etCanvasImage(s,\
u,U)}else System\
.out.println(\x22Js\
mol.js Jmol._loa\
dImage reading c\
ached image for \
\x22+m);return null\
==k?l(s,h):s};a.\
_canvasCache={};\
a._getHiddenCanv\
as=function(b,e,\
h,k,l,q){e=b._id\
+\x22_\x22+e;b=a._canv\
asCache[e];if(q)\
return b;if(l||!\
b||b.width!=\x0ah||\
b.height!=k)b=do\
cument.createEle\
ment(\x22canvas\x22),b\
.width=b.style.w\
idth=h,b.height=\
b.style.height=k\
,b.id=e,a._canva\
sCache[e]=b;retu\
rn b};a._setCanv\
asImage=function\
(a,b,e){a.buf32=\
null;a.width=b;a\
.height=e;a.getC\
ontext(\x222d\x22).dra\
wImage(a.image,0\
,0,a.image.width\
,a.image.height,\
0,0,b,e)};a._app\
ly=function(a,b)\
{return a(b)}})(\
Jmol);\x0a(function\
(a,m){a._Applet=\
function(e,h,k){\
window[e]=this;t\
his._jmolType=\x22J\
mol._Applet\x22+(h.\
isSigned?\x22 (sign\
ed)\x22:\x22\x22);this._v\
iewType=\x22Jmol\x22;t\
his._isJava=!0;t\
his._syncKeyword\
=\x22Select:\x22;this.\
_availableParams\
=\x22;progressbar;p\
rogresscolor;box\
bgcolor;boxfgcol\
or;allowjavascri\
pt;boxmessage;\x5ct\
\x5ct\x5ct\x5ct\x5ct\x5ct\x5ct\x5ct\x5ct\
;messagecallback\
;pickcallback;an\
imframecallback;\
appletreadycallb\
ack;atommovedcal\
lback;\x5ct\x5ct\x5ct\x5ct\x5ct\
\x5ct\x5ct\x5ct\x5ct;echocal\
lback;evalcallba\
ck;hovercallback\
;language;loadst\
ructcallback;mea\
surecallback;\x5ct\x5c\
t\x5ct\x5ct\x5ct\x5ct\x5ct\x5ct\x5ct;\
minimizationcall\
back;resizecallb\
ack;scriptcallba\
ck;statusform;st\
atustext;statust\
extarea;\x5ct\x5ct\x5ct\x5ct\
\x5ct\x5ct\x5ct\x5ct\x5ct;syncc\
allback;usecomma\
ndthread;syncid;\
appletid;startup\
script;menufile;\
\x22;\x0aif(k)return t\
his;this._isSign\
ed=h.isSigned;th\
is._readyFunctio\
n=h.readyFunctio\
n;this._ready=!1\
;this._isJava=!0\
;this._isInfoVis\
ible=!1;this._ap\
plet=null;this._\
memoryLimit=h.me\
moryLimit||512;t\
his._canScript=f\
unction(){return\
!0};this._savedO\
rientations=[];t\
his._initialize=\
function(e,k){va\
r b=!1;a._jarFil\
e&&(k=a._jarFile\
);if(this._jarFi\
le){var c=this._\
jarFile;0<=c.ind\
exOf(\x22/\x22)?(alert\
(\x22This web page \
URL is requestin\
g that the apple\
t used be \x22+c+\x22.\
 This is a possi\
ble security ris\
k, particularly \
if the applet is\
 signed, because\
 signed applets \
can read and wri\
te files on your\
 local machine o\
r network.\x22),\x0a\x22y\
es\x22==prompt(\x22Do \
you want to use \
applet \x22+c+\x22? \x22,\
\x22yes or no\x22)?(e=\
c.substring(0,c.\
lastIndexOf(\x22/\x22)\
),k=c.substring(\
c.lastIndexOf(\x22/\
\x22)+1)):b=!0):k=c\
;this_isSigned=h\
.isSigned=0<=k.i\
ndexOf(\x22Signed\x22)\
}this._jarPath=h\
.jarPath=e||\x22.\x22;\
this._jarFile=h.\
jarFile=\x22string\x22\
==typeof k?k:(k?\
\x22JmolAppletSigne\
d\x22:\x22JmolApplet\x22)\
+\x220.jar\x22;b&&aler\
t(\x22The web page \
URL was ignored.\
 Continuing usin\
g \x22+this._jarFil\
e+' in directory\
 \x22'+this._jarPat\
h+'\x22');void 0==a\
.controls||a.con\
trols._onloadRes\
etForms()};this.\
_create(e,h);ret\
urn this};\x0avar k\
=a._Applet,h=a._\
Applet.prototype\
;k._get=function\
(e,h,q){q||(q=!1\
);h||(h={});a._a\
ddDefaultInfo(h,\
{color:\x22#FFFFFF\x22\
,width:300,heigh\
t:300,addSelecti\
onOptions:!1,ser\
verURL:\x22http://y\
our.server.here/\
jsmol.php\x22,defau\
ltModel:\x22\x22,scrip\
t:null,src:null,\
readyFunction:nu\
ll,use:\x22HTML5\x22,j\
arPath:\x22java\x22,ja\
rFile:\x22JmolApple\
t0.jar\x22,isSigned\
:!1,j2sPath:\x22j2s\
\x22,coverImage:nul\
l,makeLiveImage:\
null,coverTitle:\
\x22\x22,coverCommand:\
\x22\x22,deferApplet:!\
1,deferUncover:!\
1,disableJ2SLoad\
Monitor:!1,disab\
leInitialConsole\
:!0,debug:!1});a\
._debugAlert=\x0ah.\
debug;h.serverUR\
L&&(a._serverUrl\
=h.serverURL);fo\
r(var m=!1,u=nul\
l,b=h.use.toUppe\
rCase().split(\x22#\
\x22)[0].split(\x22 \x22)\
,c=0;c<b.length;\
c++){switch(b[c]\
){case \x22JAVA\x22:m=\
!0;a.featureDete\
ction.supportsJa\
va()&&(u=new k(e\
,h,q));break;cas\
e \x22WEBGL\x22:u=k._g\
etCanvas(e,h,q,!\
0);break;case \x22H\
TML5\x22:a.featureD\
etection.allowHT\
ML5?u=k._getCanv\
as(e,h,q,!1):b.p\
ush(\x22JAVA\x22)}if(n\
ull!=u)break}nul\
l==u&&(q||!m?u={\
_jmolType:\x22none\x22\
}:m&&(u=new k(e,\
h)));return q?u:\
a._registerApple\
t(e,u)};k._getCa\
nvas=function(e,\
h,q,m){h._isLaye\
red=\x0a!1;h._platf\
orm=\x22J.awtjs2d.P\
latform\x22;return \
m&&a.featureDete\
ction.supportsWe\
bGL()?(a._Canvas\
3D.prototype=a.G\
Lmol.extendApple\
t(a._jsSetProtot\
ype(new k(e,h,!0\
))),new a._Canva\
s3D(e,h,\x22Jmol\x22,q\
)):!m?(a._Canvas\
2D.prototype=a._\
jsSetPrototype(n\
ew k(e,h,!0)),ne\
w a._Canvas2D(e,\
h,\x22Jmol\x22,q)):nul\
l};k._noJavaMsg=\
\x22Either you do n\
ot have Java app\
lets enabled in \
your web<br />br\
owser or your br\
owser is blockin\
g this applet.<b\
r />\x5ct\x5ct\x5ctCheck \
the warning mess\
age from your br\
owser and/or ena\
ble Java applets\
 in<br />\x5ct\x5ct\x5cty\
our web browser \
preferences, or \
install the Java\
 Runtime Environ\
ment from <a hre\
f='http://www.ja\
va.com'>www.java\
.com</a>\x22;\x0ak._se\
tCommonMethods=f\
unction(a){a._sh\
owInfo=h._showIn\
fo;a._search=h._\
search;a._getNam\
e=h._getName;a._\
readyCallback=h.\
_readyCallback};\
k._createApplet=\
function(e,h,q){\
e._initialize(h.\
jarPath,h.jarFil\
e);var s=e._jarF\
ile;a._isFile&&(\
s=s.replace(/0\x5c.\
jar/,\x22.jar\x22));va\
r u=0<=e._contai\
nerWidth.indexOf\
(\x22px\x22)?e._contai\
nerWidth:\x22100%\x22,\
b=0<=e._containe\
rHeight.indexOf(\
\x22px\x22)?e._contain\
erHeight:\x22100%\x22,\
u=' style=\x22width\
:'+u+\x22;height:\x22+\
b+'\x22 ',b=\x22name='\
\x22+e._id+\x22_object\
' id='\x22+e._id+\x22_\
object' \x5cn\x22+u+\x22\x5c\
n\x22;q.codebase=e.\
_jarPath;\x0aq.code\
Path=q.codebase+\
\x22/\x22;if(0>q.codeP\
ath.indexOf(\x22://\
\x22)){var c=m.loca\
tion.href.split(\
\x22#\x22)[0].split(\x22?\
\x22)[0].split(\x22/\x22)\
;c[c.length-1]=q\
.codePath;q.code\
Path=c.join(\x22/\x22)\
}q.archive=s;q.m\
ayscript=\x22true\x22;\
q.java_arguments\
=\x22-Xmx\x22+Math.rou\
nd(h.memoryLimit\
||e._memoryLimit\
)+\x22m\x22;q.permissi\
ons=e._isSigned?\
\x22all-permissions\
\x22:\x22sandbox\x22;q.do\
cumentLocation=m\
.location.href;q\
.documentBase=m.\
location.href.sp\
lit(\x22#\x22)[0].spli\
t(\x22?\x22)[0];q.jarP\
ath=h.jarPath;a.\
_syncedApplets.l\
ength&&(q.syncca\
llback=\x22Jmol._my\
SyncCallback\x22);\x0a\
e._startupScript\
&&(q.script=e._s\
tartupScript);va\
r c=\x22\x5cn\x22,d;for(d\
 in q)q[d]&&(c+=\
\x22  <param name='\
\x22+d+\x22' value='\x22+\
q[d]+\x22' />\x5cn\x22);c\
=a.featureDetect\
ion.useIEObject|\
|a.featureDetect\
ion.useHtml4Obje\
ct?\x22<object \x22+b+\
(a.featureDetect\
ion.useIEObject?\
\x22 classid='clsid\
:8AD9C840-044E-1\
1D1-B3E9-00805F4\
99D93' codebase=\
'http://java.sun\
.com/update/1.6.\
0/jinstall-6u22-\
windows-i586.cab\
'>\x22:\x22 type='appl\
ication/x-java-a\
pplet'>\x22)+c+\x22<p \
style='backgroun\
d-color:yellow;\x22\
+u.split('\x22')[1]\
+\x22;text-align:ce\
nter;vertical-al\
ign:middle;'>\x5cn\x22\
+\x0ak._noJavaMsg+\x22\
</p></object>\x5cn\x22\
:\x22<applet \x22+b+\x22 \
code='\x22+q.code+\x22\
' codebase='\x22+e.\
_jarPath+\x22' arch\
ive='\x22+s+\x22' mays\
cript='true'>\x5cn\x22\
+c+\x22<table bgcol\
or='yellow'><tr>\
<td align='cente\
r' valign='middl\
e' \x22+u+\x22>\x5cn\x22+k._\
noJavaMsg+\x22</td>\
</tr></table></a\
pplet>\x5cn\x22;e._def\
erApplet&&(e._ja\
vaCode=c,c=\x22\x22);c\
=a._getWrapper(e\
,!0)+c+a._getWra\
pper(e,!1)+(h.ad\
dSelectionOption\
s?a._getGrabberO\
ptions(e):\x22\x22);a.\
_debugAlert&&ale\
rt(c);e._code=a.\
_documentWrite(c\
)};h._newApplet=\
function(a){this\
._is2D||a.put(\x22s\
cript\x22,(a.get(\x22s\
cript\x22)||\x0a\x22\x22)+\x22;\
set multipleBond\
Spacing 0.35;\x22);\
this._viewerOpti\
ons=a;return new\
 J.appletjs.Jmol\
(a)};h._addCoreF\
iles=function(){\
a._addCoreFile(\x22\
jmol\x22,this._j2sP\
ath,this.__Info.\
preloadCore);thi\
s._is2D||a._addE\
xec([this,null,\x22\
J.export.JSExpor\
ter\x22,\x22load JSExp\
orter\x22]);a._debu\
gCode&&a._addExe\
c([this,null,\x22J.\
appletjs.Jmol\x22,\x22\
load Jmol\x22])};h.\
_create=function\
(e,h){a._setObje\
ct(this,e,h);var\
 q={syncId:a._sy\
ncId,progressbar\
:\x22true\x22,progress\
color:\x22blue\x22,box\
bgcolor:this._co\
lor||\x22black\x22,box\
fgcolor:\x22white\x22,\
boxmessage:\x22Down\
loading JmolAppl\
et ...\x22,\x0ascript:\
this._color?'bac\
kground \x22'+this.\
_color+'\x22':\x22\x22,co\
de:\x22JmolApplet.c\
lass\x22};a._setApp\
letParams(this._\
availableParams,\
q,h);var m;h.inl\
ineModel?(m=h.in\
lineModel,m=m.re\
place(/\x5cr|\x5cn|\x5cr\x5c\
n/g,0<=m.indexOf\
(\x22|\x22)?\x22\x5c\x5c/n\x22:\x22|\x22\
).replace(/'/g,\x22\
&#39;\x22),a._debug\
Alert&&alert(\x22in\
line model:\x5cn\x22+m\
)):m=\x22\x22;q.loadIn\
line=m;q.appletR\
eadyCallback=\x22Jm\
ol._readyCallbac\
k\x22;a._syncedAppl\
ets.length&&(q.s\
ynccallback=\x22Jmo\
l._mySyncCallbac\
k\x22);q.java_argum\
ents=\x22-Xmx\x22+Math\
.round(h.memoryL\
imit||this._memo\
ryLimit)+\x22m\x22;thi\
s._initialize(h.\
jarPath,\x0ah.jarFi\
le);k._createApp\
let(this,h,q)};h\
._restoreState=f\
unction(e,h){Sys\
tem.out.println(\
\x22\x5cn\x5cnasynchronou\
s restore state \
for \x22+e+\x22 \x22+h);v\
ar k=this,m=k._a\
pplet&&k._applet\
.viewer;switch(h\
){case \x22setOptio\
ns\x22:return funct\
ion(){k.__startA\
ppletJS(k)};case\
 \x22render\x22:return\
 function(){setT\
imeout(function(\
){m.refresh(2)},\
10)};default:swi\
tch(e){case \x22J.s\
hape.Balls\x22:case\
 \x22J.shape.Sticks\
\x22:case \x22J.shape.\
Frank\x22:return nu\
ll}if(m&&m.isScr\
iptExecuting&&m.\
isScriptExecutin\
g()){if(a._async\
Callbacks[e])ret\
urn System.out.p\
rintln(\x22...ignor\
ed\x22),\x0a1;var u=m.\
getEvalContextAn\
dHoldQueue(m.eva\
l),b=u.pc-1;u.as\
yncID=e;a._async\
Callbacks[e]=fun\
ction(a){u.pc=a;\
System.out.print\
ln(\x22sc.asyncID=\x22\
+u.asyncID+\x22 sc.\
pc = \x22+u.pc);m.e\
val.resumeEval(u\
)};m.eval.pc=m.e\
val.pcEnd;System\
.out.println(\x22se\
tting resume for\
 pc=\x22+u.pc+\x22 \x22+e\
+\x22 to \x22+a._async\
Callbacks[e]+\x22//\
\x22);return functi\
on(){System.out.\
println(\x22resumin\
g \x22+e+\x22 \x22+a._asy\
ncCallbacks[e]);\
a._asyncCallback\
s[e](b)}}System.\
out.println(e+\x22?\
????????????????\
????\x22+h);return \
function(){setTi\
meout(function()\
{m.refresh(2)},\x0a\
10)}}};h._readyC\
allback=function\
(e,h,k){if(k){a.\
_setDestroy(this\
);this._ready=!0\
;e=this._readySc\
ript;this._defau\
ltModel?a._searc\
h(this,this._def\
aultModel,e?\x22;\x22+\
e:\x22\x22):e?this._sc\
ript(e):this._sr\
c&&this._script(\
'load \x22'+this._s\
rc+'\x22');this._sh\
owInfo(!0);this.\
_showInfo(!1);a.\
Cache.setDragDro\
p(this);this._re\
adyFunction&&thi\
s._readyFunction\
(this);a._setRea\
dy(this);if((e=t\
his._2dapplet)&&\
e._isEmbedded&&e\
._ready&&e.__Inf\
o.visible)this._\
show2d(!0),this.\
_show2d(!1),this\
._show2d(!0);a._\
hideLoadingSpinn\
er(this)}};\x0ah._s\
howInfo=function\
(e){e&&this._2da\
pplet&&this._2da\
pplet._show(!1);\
a.$html(a.$(this\
,\x22infoheaderspan\
\x22),this._infoHea\
der);this._info&\
&a.$html(a.$(thi\
s,\x22infodiv\x22),thi\
s._info);if(!thi\
s._isInfoVisible\
!=!e){this._isIn\
foVisible=e;if(t\
his._isJava){var\
 h=e?2:\x22100%\x22;a.\
$setSize(a.$(thi\
s,\x22appletdiv\x22),h\
,h)}a.$setVisibl\
e(a.$(this,\x22info\
tablediv\x22),e);a.\
$setVisible(a.$(\
this,\x22infoheader\
div\x22),e);this._s\
how(!e)}};h._sho\
w2d=function(a){\
this._2dapplet._\
show2d(a);this._\
2dapplet._isEmbe\
dded&&(this._sho\
wInfo(!1),this._\
show(!a),\x0athis._\
2dapplet.__showC\
ontainer(!0,!0))\
};h._getSpinner=\
function(){retur\
n this.__Info.ap\
pletLoadingImage\
||this._j2sPath+\
\x22/img/JSmol_spin\
ner.gif\x22};h._get\
AtomCorrelation=\
function(a){this\
._loadMolData(a,\
\x22atommap = compa\
re({1.1} {2.1} '\
MAP' 'H'); zap 2\
.1\x22,!0);a=this._\
evaluate(\x22atomma\
p\x22);for(var h=th\
is._evaluate(\x22{*\
}.count\x22),k=[],m\
=[],u=0;u<a.leng\
th;u++){var b=a[\
u];k[b[0]+1]=b[1\
]-h+1;m[b[1]-h+1\
]=b[0]+1}return{\
fromJmol:k,toJmo\
l:m}};h._show=fu\
nction(e){var h=\
!e?2:\x22100%\x22;a.$s\
etSize(a.$(this,\
\x22object\x22),h,h);\x0a\
this._isJava||a.\
$setVisible(a.$(\
this,\x22appletdiv\x22\
),e)};h._clearCo\
nsole=function()\
{this._console==\
this._id+\x22_infod\
iv\x22&&(this.info=\
\x22\x22);self.Clazz&&\
(a._setConsoleDi\
v(this._console)\
,Clazz.Console.c\
lear())};h._addS\
cript=function(a\
){this._readyScr\
ipt||(this.ready\
Script=\x22\x22);this.\
_readyScript&&(t\
his._readyScript\
+=\x22;\x22);this._rea\
dyScript+=a;retu\
rn!0};h._script=\
function(e){if(!\
this._ready)retu\
rn this._addScri\
pt(e);a._setCons\
oleDiv(this._con\
sole);a._hideLoc\
alFileReader(thi\
s);this._applet.\
script(e)};h._sy\
ncScript=\x0afuncti\
on(a){this._appl\
et.syncScript(a)\
};h._scriptCheck\
=function(a){ret\
urn this._ready&\
&this._applet.sc\
riptCheck(a)};h.\
_scriptWait=func\
tion(a,h){var k=\
this._scriptWait\
AsArray(a),m=\x22\x22;\
if(!h)for(var u=\
k.length;0<=--u;\
)for(var b=0,c=k\
[u].length;b<c;b\
++)m+=k[u][b]+\x22\x5c\
n\x22;return m};h._\
scriptEcho=funct\
ion(a){a=this._s\
criptWaitAsArray\
(a);for(var h=\x22\x22\
,k=a.length;0<=-\
-k;)for(var m=a[\
k].length;0<=--m\
;)\x22scriptEcho\x22==\
a[k][m][1]&&(h+=\
a[k][m][3]+\x22\x5cn\x22)\
;return h.replac\
e(/ \x5c| /g,\x22\x5cn\x22)}\
;h._scriptMessag\
e=function(a){a=\
\x0athis._scriptWai\
tAsArray(a);for(\
var h=\x22\x22,k=a.len\
gth;0<=--k;)for(\
var m=a[k].lengt\
h;0<=--m;)\x22scrip\
tStatus\x22==a[k][m\
][1]&&(h+=a[k][m\
][3]+\x22\x5cn\x22);retur\
n h.replace(/ \x5c|\
 /g,\x22\x5cn\x22)};h._sc\
riptWaitOutput=f\
unction(a){var h\
=\x22\x22;try{a&&(h+=t\
his._applet.scri\
ptWaitOutput(a))\
}catch(k){}retur\
n h};h._scriptWa\
itAsArray=functi\
on(e){var h=\x22\x22;t\
ry{if(this._getS\
tatus(\x22scriptEch\
o,scriptMessage,\
scriptStatus,scr\
iptError\x22),e&&(h\
+=this._applet.s\
criptWait(e),h=a\
._evalJSON(h,\x22jm\
olStatus\x22),\x22obje\
ct\x22==typeof h))r\
eturn h}catch(k)\
{}return[[h]]};\x0a\
h._getStatus=fun\
ction(e){return \
a._sortMessages(\
this._getPropert\
yAsArray(\x22jmolSt\
atus\x22,e))};h._ge\
tPropertyAsArray\
=function(e,h){r\
eturn a._evalJSO\
N(this._getPrope\
rtyAsJSON(e,h),e\
)};h._getPropert\
yAsString=functi\
on(a,h){void 0==\
h&&(h=\x22\x22);return\
 this._applet.ge\
tPropertyAsStrin\
g(a,h)+\x22\x22};h._ge\
tPropertyAsJSON=\
function(a,h){vo\
id 0==h&&(h=\x22\x22);\
try{return this.\
_applet.getPrope\
rtyAsJSON(a,h)+\x22\
\x22}catch(k){retur\
n\x22\x22}};h._getProp\
ertyAsJavaObject\
=function(a,h){v\
oid 0==h&&(h=\x22\x22)\
;return this._ap\
plet.getProperty\
(a,h)};\x0ah._evalu\
ate=function(a){\
null!=a||(a=\x22\x22);\
return this._get\
PropertyAsArray(\
\x22variableInfo\x22,a\
)};h._evaluateDE\
PRECATED=functio\
n(a){a=\x22\x22+this._\
getPropertyAsJav\
aObject(\x22evaluat\
e\x22,a);var h=a.re\
place(/\x5c-*\x5cd+/,\x22\
\x22);if(\x22\x22==h&&!is\
NaN(parseInt(a))\
)return parseInt\
(a);h=a.replace(\
/\x5c-*\x5cd*\x5c.\x5cd*/,\x22\x22\
);return\x22\x22==h&&!\
isNaN(parseFloat\
(a))?parseFloat(\
a):a};h._saveOri\
entation=functio\
n(a){return this\
._savedOrientati\
ons[a]=this._get\
PropertyAsArray(\
\x22orientationInfo\
\x22,\x22info\x22).moveTo\
};h._restoreOrie\
ntation=function\
(a){a=this._save\
dOrientations[a]\
;\x0areturn!a||\x22\x22==\
a?a.replace(/1\x5c.\
0/,\x220\x22):this._sc\
riptWait(a)};h._\
restoreOrientati\
onDelayed=functi\
on(a,h){1>argume\
nts.length&&(h=1\
);var k=this._sa\
vedOrientations[\
a];return!k||\x22\x22=\
=k?k.replace(/1\x5c\
.0/,h):this._scr\
iptWait(k)};h._r\
esizeApplet=func\
tion(e){function\
 h(e,k){var b=\x22\x22\
+e;return 0==b.l\
ength?k?\x22\x22:a._al\
lowedJmolSize[2]\
:b.indexOf(\x22%\x22)=\
=b.length-1?b:1>\
=(e=parseFloat(e\
))&&0<e?100*e+\x22%\
\x22:(isNaN(e=Math.\
floor(e))?a._all\
owedJmolSize[2]:\
e<a._allowedJmol\
Size[0]?a._allow\
edJmolSize[0]:e>\
a._allowedJmolSi\
ze[1]?a._allowed\
JmolSize[1]:\x0ae)+\
(k?k:\x22\x22)}var k;\x22\
object\x22==typeof \
e&&null!=e?(k=e[\
0]||e.width,e=e[\
1]||e.height):k=\
e;k=[h(k,\x22px\x22),h\
(e,\x22px\x22)];e=a._g\
etElement(this,\x22\
appletinfotabled\
iv\x22);e.style.wid\
th=k[0];e.style.\
height=k[1];this\
._containerWidth\
=k[0];this._cont\
ainerHeight=k[1]\
;this._is2D&&a._\
repaint(this,!0)\
};h._search=func\
tion(e,h){a._sea\
rch(this,e,h)};h\
._searchDatabase\
=function(e,h,k)\
{if(this._2dappl\
et&&this._2dappl\
et._isEmbedded&&\
!a.$(this,\x22apple\
tdiv:visible\x22)[0\
])return this._2\
dapplet._searchD\
atabase(e,h,k);t\
his._showInfo(!1\
);\x0a0<=e.indexOf(\
\x22?\x22)?a._getInfoF\
romDatabase(this\
,h,e.split(\x22?\x22)[\
0]):(k||(k=a._ge\
tScriptForDataba\
se(h)),e=h+e,thi\
s._currentView=n\
ull,this._search\
Query=e,this._lo\
adFile(e,k,e))};\
h._loadFile=func\
tion(e,h,k){this\
._showInfo(!1);h\
||(h=\x22\x22);this._t\
hisJmolModel=\x22\x22+\
Math.random();th\
is._fileName=e;i\
f(!this._scriptL\
oad(e,h)){var m=\
this;a._loadFile\
Data(this,e,func\
tion(a){m.__load\
Model(a,h,k)},fu\
nction(){m.__loa\
dModel(null)})}}\
;h._scriptLoad=f\
unction(a,h){h||\
(h=\x22\x22);var k=thi\
s._isJava||!this\
._noscript;k&&th\
is._script(\x22zap;\
set echo middle \
center;echo Retr\
ieving data...\x22)\
;\x0aif(!this._isSi\
gned||null!=this\
._viewSet)return\
!1;k?this._scrip\
t('load async \x22'\
+a+'\x22;'+h):this.\
_applet.openFile\
(a);this._checkD\
eferred(\x22\x22);retu\
rn!0};h.__loadMo\
del=function(e,h\
,k){null!=e&&(nu\
ll!=this._viewSe\
t&&(h||(h=\x22\x22),h+\
=\x22;if ({*}.molec\
ule.max > 1 || {\
*}.modelindex.ma\
x > 0){ delete m\
olecule > 1 or m\
odelindex > 0;x \
= getProperty('e\
xtractModel',{*}\
);load inline @x\
};\x22),!h&&this._n\
oscript?this._ap\
plet.loadInlineS\
tring(e,\x22\x22,!1):t\
his._loadMolData\
(e,h,!1),null!=t\
his._viewSet&&a.\
View.updateView(\
this,{chemID:k,\x0a\
data:e}))};h._lo\
adMolData=functi\
on(a,h,k){h||(h=\
\x22\x22);k=k?\x22append\x22\
:\x22model\x22;this._a\
pplet.scriptWait\
('load DATA \x22'+k\
+'\x22'+a+'\x5cnEND \x22'\
+k+'\x22 ;'+h)};h._\
loadModelFromVie\
w=function(e){th\
is._currentView=\
e;var h=e.Jmol;n\
ull!=h.data?this\
.__loadModel(h.d\
ata,null,e.info.\
chemID):null!=e.\
info.chemID?a._s\
earchMol(this,e.\
info.chemID,null\
,!1):(h=e.JME)&&\
h.applet._show2d\
(!1,this)};h._up\
dateView=functio\
n(){null!=this._\
viewSet&&this._a\
pplet&&(chemID=\x22\
\x22+this._getPrope\
rtyAsJavaObject(\
\x22variableInfo\x22,\x22\
script('show che\
mical inchiKey')\
\x22),\x0achemID=36>ch\
emID.length()?nu\
ll:chemID.substr\
ing(36).split(\x22\x5c\
n\x22)[0],a.View.up\
dateView(this,{c\
hemID:chemID,dat\
a:\x22\x22+this._getPr\
opertyAsJavaObje\
ct(\x22evaluate\x22,\x22e\
xtractModel\x22,\x22{v\
isible}\x22)}))};h.\
_atomPickedCallb\
ack=function(e,h\
){if(!(0>h)){var\
 k=[h+1];a.View.\
updateAtomPick(t\
his,k);this._upd\
ateAtomPick(k)}}\
;h._updateAtomPi\
ck=function(a){t\
his._script(0==a\
.length?\x22select \
none\x22:\x22select on\
 visible and (@\x22\
+a.join(\x22,@\x22)+\x22)\
\x22)};h._isDeferre\
d=function(){ret\
urn!this._canvas\
&&this._cover&&t\
his._isCovered&&\
this._deferApple\
t};\x0ah._checkDefe\
rred=function(a)\
{return this._is\
Deferred()?(this\
._coverScript=a,\
this._cover(!1),\
!0):!1};h._cover\
=function(e){e||\
!this._deferAppl\
et?this._display\
CoverImage(e):(e\
=this._coverScri\
pt?this._coverSc\
ript:\x22\x22,this._co\
verScript=\x22\x22,thi\
s._deferUncover&\
&(e+=\x22;refresh;j\
avascript \x22+this\
._id+\x22._displayC\
overImage(false)\
\x22),this._script(\
e,!0),this._defe\
rUncover&&\x22activ\
ate 3D model\x22==t\
his._coverTitle&\
&(a._getElement(\
this,\x22coverimage\
\x22).title=\x223D mod\
el is loading...\
\x22),this._isJava|\
|this._newCanvas\
(!1),this._defau\
ltModel&&\x0aa._sea\
rch(this,this._d\
efaultModel),thi\
s._showInfo(!1),\
this._deferUncov\
er||this._displa\
yCoverImage(!1),\
this._isJava&&a.\
$html(a.$(this,\x22\
appletdiv\x22),this\
._javaCode),this\
._init&&this._in\
it())};h._displa\
yCoverImage=func\
tion(e){this._co\
verImage&&this._\
isCovered!=e&&(t\
his._isCovered=e\
,a._getElement(t\
his,\x22coverdiv\x22).\
style.display=e?\
\x22block\x22:\x22none\x22)}\
;h._getSmiles=fu\
nction(){return \
this._evaluate(\x22\
{visible}.find('\
SMILES')\x22)};h._g\
etMol=function()\
{return this._ev\
aluate(\x22getPrope\
rty('ExtractMode\
l',{visible})\x22)}\
;\x0ah._getMol2D=fu\
nction(){return \
this._evaluate(\x22\
script('select v\
isible;show chem\
ical sdf')\x22)};a.\
jmolSmiles=funct\
ion(a){return a.\
_getSmiles()}})(\
Jmol,document);\x0a\
(function(a){var\
 m=a.controls={_\
hasResetForms:!1\
,_scripts:[\x22\x22],_\
checkboxMasters:\
{},_checkboxItem\
s:{},_actions:{}\
,_buttonCount:0,\
_checkboxCount:0\
,_radioGroupCoun\
t:0,_radioCount:\
0,_linkCount:0,_\
cmdCount:0,_menu\
Count:0,_previou\
sOnloadHandler:n\
ull,_control:nul\
l,_element:null,\
_appletCssClass:\
null,_appletCssT\
ext:\x22\x22,_buttonCs\
sClass:null,_but\
tonCssText:\x22\x22,_c\
heckboxCssClass:\
null,_checkboxCs\
sText:\x22\x22,_radioC\
ssClass:null,_ra\
dioCssText:\x22\x22,_l\
inkCssClass:null\
,_linkCssText:\x22\x22\
,_menuCssClass:n\
ull,_menuCssText\
:\x22\x22};\x0am._addScri\
pt=function(a,h)\
{var e=m._script\
s.length;m._scri\
pts[e]=[a,h];ret\
urn e};m._getIdF\
orControl=functi\
on(a,h){return\x22s\
tring\x22==typeof a\
?a:!h||!a._canSc\
ript||a._canScri\
pt(h)?a._id:null\
};m._radio=funct\
ion(a,h,e,l,q,s,\
u,b){var c=m._ge\
tIdForControl(a,\
h);if(null==c)re\
turn null;++m._r\
adioCount;void 0\
!=s&&null!=s||(s\
=\x22jmolRadioGroup\
\x22+(m._radioGroup\
Count-1));if(!h)\
return\x22\x22;void 0!\
=u&&null!=u||(u=\
\x22jmolRadio\x22+(m._\
radioCount-1));v\
oid 0!=e&&null!=\
e||(e=h.substrin\
g(0,32));q||(q=\x22\
\x22);a=\x22</span>\x22;m\
._actions[u]=\x0am.\
_addScript(c,h);\
h='<span id=\x22spa\
n_'+u+'\x22'+(b?' t\
itle=\x22'+b+'\x22':\x22\x22\
)+\x22><input name=\
'\x22+s+\x22' id='\x22+u+\
\x22' type='radio' \
onclick='Jmol.co\
ntrols._click(th\
is);return true;\
' onmouseover='J\
mol.controls._mo\
useOver(this);re\
turn true;' onmo\
useout='Jmol.con\
trols._mouseOut(\
)' \x22+(l?\x22checked\
='true' \x22:\x22\x22)+m.\
_radioCssText+\x22 \
/>\x22;0<=e.toLower\
Case().indexOf(\x22\
<td>\x22)&&(h+=a,a=\
\x22\x22);return h+('<\
label for=\x22'+u+'\
\x22>'+e+\x22</label>\x22\
+a+q)};m._script\
Execute=function\
(k,h){var e=a._a\
pplets[h[0]],l=h\
[1];if(\x22object\x22=\
=typeof l)l[0](k\
,l,\x0ae);else\x22func\
tion\x22==typeof l?\
l(e):a.script(e,\
l)};m.__checkScr\
ipt=function(a,h\
){var e=0<=h.val\
ue.indexOf(\x22JSCO\
NSOLE \x22)||\x22\x22===a\
._scriptCheck(h.\
value);h.style.c\
olor=e?\x22black\x22:\x22\
red\x22;return e};m\
.__getCmd=functi\
on(a,h){if(h._cm\
ds&&h._cmds.leng\
th){var e=h._cmd\
s[h._cmdpt=(h._c\
mdpt+h._cmds.len\
gth+a)%h._cmds.l\
ength];setTimeou\
t(function(){h.v\
alue=e},10);h._c\
mdadd=1;h._cmddi\
r=a}};m._command\
KeyPress=functio\
n(k,h,e){k=13==k\
?13:window.event\
?window.event.ke\
yCode:k?k.keyCod\
e||k.which:0;var\
 l=document.getE\
lementById(h),\x0aq\
=a._applets[e];s\
witch(k){case 13\
:return h=l.valu\
e,m._scriptExecu\
te(l,[e,h]),l._c\
mds||(l._cmds=[]\
,l._cmddir=0,l._\
cmdpt=-1,l._cmda\
dd=0),h&&0==l._c\
mdadd?(++l._cmdp\
t,l._cmds.splice\
(l._cmdpt,0,h),l\
._cmdadd=0,l._cm\
ddir=0):l._cmdad\
d=0,l.value=\x22\x22,!\
1;case 27:return\
 setTimeout(func\
tion(){l.value=\x22\
\x22},20),!1;case 3\
8:m.__getCmd(-1,\
l);break;case 40\
:m.__getCmd(1,l)\
;break;default:l\
._cmdadd=0}setTi\
meout(function()\
{m.__checkScript\
(q,l)},20);retur\
n!0};m._click=fu\
nction(a,h){m._e\
lement=a;1==argu\
ments.length&&(h\
=m._actions[a.id\
]);\x0am._scriptExe\
cute(a,m._script\
s[h])};m._menuSe\
lected=function(\
a){var h=a.value\
;if(void 0!=h)m.\
_scriptExecute(a\
,m._scripts[h]);\
else{h=a.length;\
if(\x22number\x22==typ\
eof h)for(var e=\
0;e<h;++e)if(a[e\
].selected){m._c\
lick(a[e],a[e].v\
alue);return}ale\
rt(\x22?Que? menu s\
elected bug #873\
4\x22)}};m._cbNotif\
yMaster=function\
(a){var h=!0,e=!\
0,l=!1,q,s;for(s\
 in a.chkGroup)q\
=a.chkGroup[s],q\
.checked?e=!1:h=\
!1,q.indetermina\
te&&(l=!0);q=a.c\
hkMaster;h?q.che\
cked=!0:e?q.chec\
ked=!1:l=!0;q.in\
determinate=l;(a\
=m._checkboxItem\
s[q.id])&&\x0a(q=a.\
chkMaster)&&m._c\
bNotifyMaster(m.\
_checkboxMasters\
[q.id])};m._cbNo\
tifyGroup=functi\
on(a,h){for(var \
e in a.chkGroup)\
{var l=a.chkGrou\
p[e];l.checked!=\
h&&(l.checked=h,\
m._cbClick(l));m\
._checkboxMaster\
s[l.id]&&m._cbNo\
tifyGroup(m._che\
ckboxMasters[l.i\
d],h)}};m._cbSet\
CheckboxGroup=fu\
nction(a,h,e){va\
r l=a;\x22number\x22==\
typeof l&&(l=\x22jm\
olCheckbox\x22+l);(\
a=document.getEl\
ementById(l))||a\
lert(\x22jmolSetChe\
ckboxGroup: mast\
er checkbox not \
found: \x22+l);var \
q=m._checkboxMas\
ters[l]={};q.chk\
Master=a;q.chkGr\
oup={};\x22string\x22=\
=\x0atypeof h?(h=e,\
l=1):l=0;for(a=l\
;a<h.length;a++)\
l=h[a],\x22number\x22=\
=typeof l&&(l=\x22j\
molCheckbox\x22+l),\
(e=document.getE\
lementById(l))||\
alert(\x22jmolSetCh\
eckboxGroup: gro\
up checkbox not \
found: \x22+l),q.ch\
kGroup[l]=e,m._c\
heckboxItems[l]=\
q};m._cbClick=fu\
nction(a){m._con\
trol=a;var h=m._\
actions[a.id][0]\
,e=m._actions[a.\
id][1];m._click(\
a,a.checked?h:e)\
;m._checkboxMast\
ers[a.id]&&m._cb\
NotifyGroup(m._c\
heckboxMasters[a\
.id],a.checked);\
m._checkboxItems\
[a.id]&&m._cbNot\
ifyMaster(m._che\
ckboxItems[a.id]\
)};m._cbOver=fun\
ction(a){var h=\x0a\
m._actions[a.id]\
[0],e=m._actions\
[a.id][1];window\
.status=m._scrip\
ts[a.checked?e:h\
]};m._mouseOver=\
function(a,h){1=\
=arguments.lengt\
h&&(h=m._actions\
[a.id]);window.s\
tatus=m._scripts\
[h]};m._mouseOut\
=function(){wind\
ow.status=\x22 \x22;re\
turn!0};m._onloa\
dResetForms=func\
tion(){m._hasRes\
etForms||(m._has\
ResetForms=!0,m.\
_previousOnloadH\
andler=window.on\
load,window.onlo\
ad=function(){if\
(0<m._buttonCoun\
t+m._checkboxCou\
nt+m._menuCount+\
m._radioCount+m.\
_radioGroupCount\
)for(var a=docum\
ent.forms,h=a.le\
ngth;0<=--h;)a[h\
].reset();\x0am._pr\
eviousOnloadHand\
ler&&m._previous\
OnloadHandler()}\
)};m._getButton=\
function(k,h,e,l\
,q){k=m._getIdFo\
rControl(k,h);if\
(null==k)return\x22\
\x22;void 0!=l&&nul\
l!=l||(l=\x22jmolBu\
tton\x22+m._buttonC\
ount);void 0!=e&\
&null!=e||(e=h.s\
ubstring(0,32));\
++m._buttonCount\
;m._actions[l]=m\
._addScript(k,h)\
;h='<span id=\x22sp\
an_'+l+'\x22'+(q?' \
title=\x22'+q+'\x22':\x22\
\x22)+\x22><input type\
='button' name='\
\x22+l+\x22' id='\x22+l+\x22\
' value='\x22+e+\x22' \
onclick='Jmol.co\
ntrols._click(th\
is)' onmouseover\
='Jmol.controls.\
_mouseOver(this)\
;return true' on\
mouseout='Jmol.c\
ontrols._mouseOu\
t()' \x22+\x0am._butto\
nCssText+\x22 /></s\
pan>\x22;a._debugAl\
ert&&alert(h);re\
turn a._document\
Write(h)};m._get\
Checkbox=functio\
n(k,h,e,l,q,s,u)\
{var b=m._getIdF\
orControl(k,h);n\
ull!=b&&(b=m._ge\
tIdForControl(k,\
e));if(null==b)r\
eturn\x22\x22;void 0!=\
s&&null!=s||(s=\x22\
jmolCheckbox\x22+m.\
_checkboxCount);\
++m._checkboxCou\
nt;if(void 0==h|\
|null==h||void 0\
==e||null==e)ale\
rt(\x22jmolCheckbox\
 requires two sc\
ripts\x22);else if(\
void 0==l||null=\
=l)alert(\x22jmolCh\
eckbox requires \
a label\x22);else r\
eturn m._actions\
[s]=[m._addScrip\
t(b,h),m._addScr\
ipt(b,e)],k=\x22</s\
pan>\x22,\x0aq='<span \
id=\x22span_'+s+'\x22'\
+(u?' title=\x22'+u\
+'\x22':\x22\x22)+\x22><inpu\
t type='checkbox\
' name='\x22+s+\x22' i\
d='\x22+s+\x22' onclic\
k='Jmol.controls\
._cbClick(this)'\
 onmouseover='Jm\
ol.controls._cbO\
ver(this);return\
 true' onmouseou\
t='Jmol.controls\
._mouseOut()' \x22+\
(q?\x22checked='tru\
e' \x22:\x22\x22)+m._chec\
kboxCssText+\x22 />\
\x22,0<=l.toLowerCa\
se().indexOf(\x22<t\
d>\x22)&&(q+=k,k=\x22\x22\
),q+='<label for\
=\x22'+s+'\x22>'+l+\x22</\
label>\x22+k,a._deb\
ugAlert&&alert(q\
),a._documentWri\
te(q)};m._getCom\
mandInput=functi\
on(k,h,e,l,q,s){\
k=m._getIdForCon\
trol(k,\x22x\x22);if(n\
ull==k)return\x22\x22;\
\x0avoid 0!=l&&null\
!=l||(l=\x22jmolCmd\
\x22+m._cmdCount);v\
oid 0!=h&&null!=\
h||(h=\x22Execute\x22)\
;void 0!=e&&!isN\
aN(e)||(e=60);vo\
id 0!=s||(s=\x22hel\
p\x22);++m._cmdCoun\
t;h='<span id=\x22s\
pan_'+l+'\x22'+(q?'\
 title=\x22'+q+'\x22':\
\x22\x22)+\x22><input nam\
e='\x22+l+\x22' id='\x22+\
l+\x22' size='\x22+e+\x22\
' onkeydown='ret\
urn Jmol.control\
s._commandKeyPre\
ss(event,\x5c\x22\x22+l+'\
\x22,\x22'+k+\x22\x5c\x22)' val\
ue='\x22+s+\x22'/><inp\
ut  type='button\
' name='\x22+l+\x22Btn\
' id='\x22+l+\x22Btn' \
value = '\x22+h+\x22' \
onclick='Jmol.co\
ntrols._commandK\
eyPress(13,\x5c\x22\x22+l\
+'\x22,\x22'+k+\x22\x5c\x22)' /\
></span>\x22;a._deb\
ugAlert&&alert(h\
);return a._docu\
mentWrite(h)};\x0am\
._getLink=functi\
on(k,h,e,l,q){k=\
m._getIdForContr\
ol(k,h);if(null=\
=k)return\x22\x22;void\
 0!=l&&null!=l||\
(l=\x22jmolLink\x22+m.\
_linkCount);void\
 0!=e&&null!=e||\
(e=h.substring(0\
,32));++m._linkC\
ount;h=m._addScr\
ipt(k,h);e='<spa\
n id=\x22span_'+l+'\
\x22'+(q?' title=\x22'\
+q+'\x22':\x22\x22)+\x22><a \
name='\x22+l+\x22' id=\
'\x22+l+\x22' href='ja\
vascript:Jmol.co\
ntrols._click(nu\
ll,\x22+h+\x22);' onmo\
useover='Jmol.co\
ntrols._mouseOve\
r(null,\x22+h+\x22);re\
turn true;' onmo\
useout='Jmol.con\
trols._mouseOut(\
)' \x22+m._linkCssT\
ext+\x22>\x22+e+\x22</a><\
/span>\x22;a._debug\
Alert&&alert(e);\
return a._docume\
ntWrite(e)};\x0am._\
getMenu=function\
(k,h,e,l,q){var \
s=m._getIdForCon\
trol(k,null);voi\
d 0!=l&&null!=l|\
|(l=\x22jmolMenu\x22+m\
._menuCount);++m\
._menuCount;s=ty\
peof h;if(null!=\
s&&\x22object\x22==s&&\
h.length){var u=\
h.length;\x22number\
\x22!=typeof e||1==\
e?e=null:0>e&&(e\
=u);e='<span id=\
\x22span_'+l+'\x22'+(q\
?' title=\x22'+q+'\x22\
':\x22\x22)+\x22><select \
name='\x22+l+\x22' id=\
'\x22+l+\x22' onChange\
='Jmol.controls.\
_menuSelected(th\
is)'\x22+(e?\x22 size=\
'\x22+e+\x22' \x22:\x22\x22)+m.\
_menuCssText+\x22>\x22\
;for(l=0;l<u;++l\
){var b=h[l],s=t\
ypeof b,c=null,d\
=q=null;\x22object\x22\
==s&&null!=b?(c=\
b[0],q=b[1],d=b[\
2]):\x0ac=q=b;s=m._\
getIdForControl(\
k,c);if(null==s)\
return\x22\x22;null==q\
&&(q=c);\x22#optgro\
up\x22==c?e+=\x22<optg\
roup label='\x22+q+\
\x22'>\x22:\x22#optgroupE\
nd\x22==c?e+=\x22</opt\
group>\x22:(s=m._ad\
dScript(s,c),e+=\
\x22<option value='\
\x22+s+(d?\x22' select\
ed='true'>\x22:\x22'>\x22\
)+q+\x22</option>\x22)\
}e+=\x22</select></\
span>\x22;a._debugA\
lert&&alert(e);r\
eturn a._documen\
tWrite(e)}};m._g\
etRadio=function\
(k,h,e,l,q,s,u,b\
){0==m._radioGro\
upCount&&++m._ra\
dioGroupCount;s|\
|(s=\x22jmolRadioGr\
oup\x22+(m._radioGr\
oupCount-1));k=m\
._radio(k,h,e,l,\
q,s,u?u:s+\x22_\x22+m.\
_radioCount,b?b:\
0);if(null==\x0ak)r\
eturn\x22\x22;a._debug\
Alert&&alert(k);\
return a._docume\
ntWrite(k)};m._g\
etRadioGroup=fun\
ction(k,h,e,l,q,\
s){var u=typeof \
h;if(\x22object\x22!=u\
||null==u||!h.le\
ngth)alert(\x22inva\
lid arrayOfRadio\
Buttons\x22);else{v\
oid 0!=e&&null!=\
e||(e=\x22&#xa0; \x22)\
;var b=h.length;\
++m._radioGroupC\
ount;l||(l=\x22jmol\
RadioGroup\x22+(m._\
radioGroupCount-\
1));for(var c=\x22<\
span id='\x22+(q?q:\
l)+\x22'>\x22,d=0;d<b;\
++d){d==b-1&&(e=\
\x22\x22);var t=h[d],u\
=typeof t,F=null\
,c=\x22object\x22==u?c\
+(F=m._radio(k,t\
[0],t[1],t[2],e,\
l,3<t.length?t[3\
]:(q?q:l)+\x22_\x22+d,\
4<t.length?t[4]:\
0,\x0as)):c+(F=m._r\
adio(k,t,null,nu\
ll,e,l,(q?q:l)+\x22\
_\x22+d,s));if(null\
==F)return\x22\x22}c+=\
\x22</span>\x22;a._deb\
ugAlert&&alert(c\
);return a._docu\
mentWrite(c)}}})\
(Jmol);\x0a(functio\
n(a){var m=funct\
ion(a){a=\x22&\x22+a+\x22\
=\x22;return decode\
URI((\x22&\x22+documen\
t.location.searc\
h.substring(1)+a\
).split(a)[1].sp\
lit(\x22&\x22)[0])};a.\
_j2sPath=m(\x22_J2S\
\x22);a._jarFile=m(\
\x22_JAR\x22);a._use=m\
(\x22_USE\x22);a.getVe\
rsion=function()\
{return a._jmolI\
nfo.version};a.g\
etApplet=functio\
n(k,h,e){return \
a._Applet._get(k\
,h,e)};a.getJMEA\
pplet=function(k\
,h,e,l){return a\
._JMEApplet._get\
(k,h,e,l)};a.get\
JSVApplet=functi\
on(k,h,e){return\
 a._JSVApplet._g\
et(k,h,e)};a.loa\
dFile=function(a\
,h,e){a._loadFil\
e(h,e)};a.script\
=function(a,h){a\
._checkDeferred(\
h)||\x0aa._script(h\
)};a.scriptCheck\
=function(a,h){r\
eturn a&&a._scri\
ptCheck&&a._read\
y&&a._scriptChec\
k(h)};a.scriptWa\
it=function(a,h)\
{return a._scrip\
tWait(h)};a.scri\
ptEcho=function(\
a,h){return a._s\
criptEcho(h)};a.\
scriptMessage=fu\
nction(a,h){retu\
rn a._scriptMess\
age(h)};a.script\
WaitOutput=funct\
ion(a,h){return \
a._scriptWait(h)\
};a.scriptWaitAs\
Array=function(a\
,h){return a._sc\
riptWaitAsArray(\
h)};a.search=fun\
ction(a,h,e){a._\
search(h,e)};a.e\
valuateVar=funct\
ion(a,h){return \
a._evaluate(h)};\
a.evaluate=funct\
ion(a,h){return \
a._evaluateDEPRE\
CATED(h)};\x0aa.get\
AppletHtml=funct\
ion(k,h){if(h){v\
ar e=a._document\
;a._document=nul\
l;k=a.getApplet(\
k,h);a._document\
=e}return k._cod\
e};a.getProperty\
AsArray=function\
(a,h,e){return a\
._getPropertyAsA\
rray(h,e)};a.get\
PropertyAsJavaOb\
ject=function(a,\
h,e){return a._g\
etPropertyAsJava\
Object(h,e)};a.g\
etPropertyAsJSON\
=function(a,h,e)\
{return a._getPr\
opertyAsJSON(h,e\
)};a.getProperty\
AsString=functio\
n(a,h,e){return \
a._getPropertyAs\
String(h,e)};a.g\
etStatus=functio\
n(a,h){return a.\
_getStatus(h)};a\
.resizeApplet=fu\
nction(a,h){retu\
rn a._resizeAppl\
et(h)};\x0aa.restor\
eOrientation=fun\
ction(a,h){retur\
n a._restoreOrie\
ntation(h)};a.re\
storeOrientation\
Delayed=function\
(a,h,e){return a\
._restoreOrienta\
tionDelayed(h,e)\
};a.saveOrientat\
ion=function(a,h\
){return a._save\
Orientation(h)};\
a.say=function(a\
){alert(a)};a.cl\
earConsole=funct\
ion(a){a._clearC\
onsole()};a.getI\
nfo=function(a){\
return a._info};\
a.setInfo=functi\
on(a,h,e){a._inf\
o=h;2<arguments.\
length&&a._showI\
nfo(e)};a.showIn\
fo=function(a,h)\
{a._showInfo(h)}\
;a.show2d=functi\
on(a,h){a._show2\
d(h)};a.jmolBr=f\
unction(){return\
 a._documentWrit\
e(\x22<br />\x22)};\x0aa.\
jmolButton=funct\
ion(k,h,e,l,m){r\
eturn a.controls\
._getButton(k,h,\
e,l,m)};a.jmolCh\
eckbox=function(\
k,h,e,l,m,s,u){r\
eturn a.controls\
._getCheckbox(k,\
h,e,l,m,s,u)};a.\
jmolCommandInput\
=function(k,h,e,\
l,m,s){return a.\
controls._getCom\
mandInput(k,h,e,\
l,m,s)};a.jmolHt\
ml=function(k){r\
eturn a._documen\
tWrite(k)};a.jmo\
lLink=function(k\
,h,e,l,m){return\
 a.controls._get\
Link(k,h,e,l,m)}\
;a.jmolMenu=func\
tion(k,h,e,l,m){\
return a.control\
s._getMenu(k,h,e\
,l,m)};a.jmolRad\
io=function(k,h,\
e,l,m,s,u,b){ret\
urn a.controls._\
getRadio(k,\x0ah,e,\
l,m,s,u,b)};a.jm\
olRadioGroup=fun\
ction(k,h,e,l,m,\
s){return a.cont\
rols._getRadioGr\
oup(k,h,e,l,m,s)\
};a.setCheckboxG\
roup=function(k,\
h){a.controls._c\
bSetCheckboxGrou\
p(k,h,arguments)\
};a.setDocument=\
function(k){a._d\
ocument=k};a.set\
XHTML=function(k\
){a._isXHTML=!0;\
a._XhtmlElement=\
null;a._XhtmlApp\
endChild=!1;k&&(\
a._XhtmlElement=\
document.getElem\
entById(k),a._Xh\
tmlAppendChild=!\
0)};a.setAppletC\
ss=function(k,h)\
{null!=k&&(a._ap\
pletCssClass=k);\
a._appletCssText\
=h?h+\x22 \x22:k?'clas\
s=\x22'+k+'\x22 ':\x22\x22};\
a.setButtonCss=f\
unction(k,\x0ah){nu\
ll!=k&&(a.contro\
ls._buttonCssCla\
ss=k);a.controls\
._buttonCssText=\
h?h+\x22 \x22:k?'class\
=\x22'+k+'\x22 ':\x22\x22};a\
.setCheckboxCss=\
function(k,h){nu\
ll!=k&&(a.contro\
ls._checkboxCssC\
lass=k);a.contro\
ls._checkboxCssT\
ext=h?h+\x22 \x22:k?'c\
lass=\x22'+k+'\x22 ':\x22\
\x22};a.setRadioCss\
=function(k,h){n\
ull!=k&&(a.contr\
ols._radioCssCla\
ss=k);a.controls\
._radioCssText=h\
?h+\x22 \x22:k?'class=\
\x22'+k+'\x22 ':\x22\x22};a.\
setLinkCss=funct\
ion(k,h){null!=k\
&&(a.controls._l\
inkCssClass=k);a\
.controls._linkC\
ssText=h?h+\x22 \x22:k\
?'class=\x22'+k+'\x22 \
':\x22\x22};a.setMenuC\
ss=function(k,h)\
{null!=\x0ak&&(a.co\
ntrols._menuCssC\
lass=k);a.contro\
ls._menuCssText=\
h?h+\x22 \x22:k?'class\
=\x22'+k+'\x22 ':\x22\x22};a\
.setAppletSync=f\
unction(k,h,e){a\
._syncedApplets=\
k;a._syncedComma\
nds=h;a._syncedR\
eady={};a._isJmo\
lJSVSync=e};a.se\
tGrabberOptions=\
function(k){a._g\
rabberOptions=k}\
;a.setAppletHtml\
=function(k,h){k\
._code&&(a.$html\
(h,k._code),k._i\
nit&&!k._deferAp\
plet&&k._init())\
};a.coverApplet=\
function(a,h){a.\
_cover&&a._cover\
(h)};a.setFileCa\
ching=function(k\
,h){k?k._cacheFi\
les=h:a.fileCach\
e=h?{}:null};a.u\
pdateView=functi\
on(a,h,e){a._upd\
ateView(h,\x0ae)};a\
.getChemicalInfo\
=function(k,h,e)\
{h||(h=\x22name\x22);\x22\
string\x22!=typeof \
k&&(k=k._getSmil\
es());return a._\
getNCIInfo(k,h,e\
)};a.saveImage=f\
unction(a){switc\
h(a._viewType){c\
ase \x22Jmol\x22:a._sc\
ript('write PNGJ\
 \x22'+a._id+'.png\x22\
');break;case \x22J\
SV\x22:a._script(\x22w\
rite PDF\x22);break\
;case \x22JME\x22:a._s\
cript(\x22print\x22)}}\
})(Jmol);\x0aLoadCl\
azz=function(){c\
$=null;window[\x22j\
2s.clazzloaded\x22]\
||(window[\x22j2s.c\
lazzloaded\x22]=!1)\
;window[\x22j2s.cla\
zzloaded\x22]||(win\
dow[\x22j2s.clazzlo\
aded\x22]=!0,window\
[\x22j2s.object.nat\
ive\x22]=!0,Clazz={\
_isQuiet:!1,_deb\
ugging:!1},funct\
ion(a,m){try{a._\
debugging=0<=doc\
ument.location.h\
ref.indexOf(\x22j2s\
debug\x22)}catch(k)\
{}var h=[\x22j2s.cl\
azzloaded\x22,\x22j2s.\
object.native\x22];\
a.setGlobal=func\
tion(a,b){h.push\
(a);window[a]=b}\
;a.getGlobals=fu\
nction(){return \
h.sort().join(\x22\x5c\
n\x22)};a.setConsol\
eDiv=function(a)\
{window[\x22j2s.lib\
\x22]&&(window[\x22j2s\
.lib\x22].console=\x0a\
a)};var e=null;a\
._startProfiling\
=function(a){e=a\
&&self.JSON?{}:n\
ull};NullObject=\
function(){};a._\
supportsNativeOb\
ject=window[\x22j2s\
.object.native\x22]\
;a._supportsNati\
veObject?(a._O=f\
unction(){},a._O\
.__CLASS_NAME__=\
\x22Object\x22,a._O.ge\
tClass=function(\
){return a._O}):\
a._O=Object;a.Co\
nsole={};a.dateT\
oString=Date.pro\
totype.toString;\
a._hashCode=0;va\
r l=a._O.prototy\
pe;l.equals=func\
tion(a){return t\
his==a};l.hashCo\
de=function(){re\
turn this._$hash\
code||(this._$ha\
shcode=++a._hash\
Code)};l.getClas\
s=function(){ret\
urn a.getClass(t\
his)};\x0al.clone=f\
unction(){return\
 a.clone(this)};\
a.clone=function\
(a){var b=new a.\
constructor,c;fo\
r(c in a)b[c]=a[\
c];return b};l.f\
inalize=function\
(){};l.notify=fu\
nction(){};l.not\
ifyAll=function(\
){};l.wait=funct\
ion(){};l.to$tri\
ng=Object.protot\
ype.toString;l.t\
oString=function\
(){return this._\
_CLASS_NAME__?\x22[\
\x22+this.__CLASS_N\
AME__+\x22 object]\x22\
:this.to$tring.a\
pply(this,argume\
nts)};a._extende\
dObjectMethods=\x22\
equals hashCode \
getClass clone f\
inalize notify n\
otifyAll wait to\
$tring toString\x22\
.split(\x22 \x22);a.ex\
tendJO=function(\
b,\x0ac){c&&(b.__CL\
ASS_NAME__=b.pro\
totype.__CLASS_N\
AME__=c);if(a._s\
upportsNativeObj\
ect)for(var d=0;\
d<a._extendedObj\
ectMethods.lengt\
h;d++){var e=a._\
extendedObjectMe\
thods[d];b.proto\
type[e]=a._O.pro\
totype[e]}};a.ex\
tractClassName=f\
unction(a){a=a.s\
ubstring(1,a.len\
gth-1);return 0<\
=a.indexOf(\x22Arra\
y\x22)?\x22Array\x22:0<=a\
.indexOf(\x22object\
 \x22)?a.substring(\
7):a};a.getClass\
Name=function(b,\
c){if(null==b)re\
turn\x22NullObject\x22\
;if(b instanceof\
 a.CastedNull)re\
turn b.clazzName\
;switch(typeof b\
){case \x22number\x22:\
return\x22n\x22;case \x22\
boolean\x22:return\x22\
b\x22;\x0acase \x22string\
\x22:return\x22String\x22\
;case \x22function\x22\
:if(b.__CLASS_NA\
ME__)return c?b.\
__CLASS_NAME__:\x22\
Class\x22;var d=b.t\
oString(),e=d.in\
dexOf(\x22function\x22\
);if(0>e)return\x22\
[\x22==d.charAt(0)?\
a.extractClassNa\
me(d):d.replace(\
/[^a-zA-Z0-9]/g,\
\x22\x22);var e=e+8,h=\
d.indexOf(\x22(\x22,e)\
;if(0>h)break;d=\
d.substring(e,h)\
;if(0<=d.indexOf\
(\x22Array\x22))return\
\x22Array\x22;d=d.repl\
ace(/^\x5cs+/,\x22\x22).r\
eplace(/\x5cs+$/,\x22\x22\
);return\x22anonymo\
us\x22==d||\x22\x22==d?\x22F\
unction\x22:d;case \
\x22object\x22:if(b.__\
CLASS_NAME__)ret\
urn b.__CLASS_NA\
ME__;if(!b.const\
ructor)break;if(\
!b.constructor._\
_CLASS_NAME__){i\
f(b instanceof\x0aN\
umber)return\x22Num\
ber\x22;if(b instan\
ceof Boolean)ret\
urn\x22Boolean\x22;if(\
b instanceof Arr\
ay||b.BYTES_PER_\
ELEMENT)return\x22A\
rray\x22;d=b.toStri\
ng();if(\x22[\x22==d.c\
harAt(0))return \
a.extractClassNa\
me(d)}return a.g\
etClassName(b.co\
nstructor,!0)}re\
turn\x22Object\x22};a.\
getClass=functio\
n(b){if(!b)retur\
n a._O;if(\x22funct\
ion\x22==typeof b)r\
eturn b;if(b ins\
tanceof a.Casted\
Null)b=b.clazzNa\
me;else switch(t\
ypeof b){case \x22s\
tring\x22:return St\
ring;case \x22objec\
t\x22:if(!b.__CLASS\
_NAME__)return b\
.constructor||a.\
_O;b=b.__CLASS_N\
AME__;break;defa\
ult:return b.con\
structor}return \
a.evalType(b,\x0a!0\
)};var q=functio\
n(b,c){for(var d\
=0;d<a.innerFunc\
tionNames.length\
;d++)if(c==a.inn\
erFunctionNames[\
d]&&a._innerFunc\
tions[c]===b[c])\
return!0;return!\
1},s=function(){\
};a.inheritArgs=\
new s;a.inheritC\
lass=function(b,\
c,d){for(var e i\
n c)\x22b$\x22!=e&&(\x22p\
rototype\x22!=e&&\x22s\
uperClazz\x22!=e&&\x22\
__CLASS_NAME__\x22!\
=e&&\x22implementz\x22\
!=e&&!q(c,e))&&(\
b[e]=c[e]);a.unl\
oadedClasses[a.g\
etClassName(b,!0\
)]||(b.prototype\
=d?d:c!==Number?\
new c(a.inheritA\
rgs):new Number)\
;b.superClazz=c;\
b.prototype.__CL\
ASS_NAME__=b.__C\
LASS_NAME__};a.i\
mplementOf=\x0afunc\
tion(a,b){if(2<=\
arguments.length\
){a.implementz||\
(a.implementz=[]\
);var c=a.implem\
entz;if(2==argum\
ents.length)if(\x22\
function\x22==typeo\
f b)c.push(b),u(\
a,b);else{if(b i\
nstanceof Array)\
for(var d=0;d<b.\
length;d++)c.pus\
h(b[d]),u(a,b[d]\
)}else for(d=1;d\
<arguments.lengt\
h;d++)c.push(arg\
uments[d]),u(a,a\
rguments[d])}};v\
ar u=function(a,\
b){for(var c in \
b)if(\x22b$\x22!=c&&\x22p\
rototype\x22!=c&&\x22s\
uperClazz\x22!=c&&\x22\
__CLASS_NAME__\x22!\
=c&&\x22implementz\x22\
!=c&&(\x22function\x22\
!=typeof b[c]||!\
q(b,c)))a[c]=a.p\
rototype[c]=b[c]\
};a.extendInterf\
ace=\x0aa.implement\
Of;a.equalsOrExt\
endsLevel=functi\
on(b,c){if(b===c\
)return 0;if(b.i\
mplementz)for(va\
r d=b.implementz\
,e=0;e<d.length;\
e++){var h=a.equ\
alsOrExtendsLeve\
l(d[e],c);if(0<=\
h)return h+1}ret\
urn-1};a.getInhe\
ritedLevel=funct\
ion(b,c){if(b===\
c)return 0;var d\
=\x22string\x22==typeo\
f b;if(d&&(\x22void\
\x22==b||\x22unknown\x22=\
=b))return-1;var\
 e=\x22string\x22==typ\
eof c;if(e&&(\x22vo\
id\x22==c||\x22unknown\
\x22==c))return-1;i\
f(b===(d?\x22NullOb\
ject\x22:NullObject\
))switch(c){case\
 \x22n\x22:case \x22b\x22:re\
turn-1;case Numb\
er:case Boolean:\
case NullObject:\
break;default:re\
turn 0}d&&\x0a(b=a.\
evalType(b));e&&\
(c=a.evalType(c)\
);if(!c||!b)retu\
rn-1;d=0;for(e=b\
;e!==c&&10>d;){i\
f(e.implementz)f\
or(var h=e.imple\
mentz,k=0;k<h.le\
ngth;k++){var l=\
a.equalsOrExtend\
sLevel(h[k],c);i\
f(0<=l)return d+\
l+1}e=e.superCla\
zz;if(!e)return \
c===Object||c===\
a._O?d+1.5:-1;d+\
+}return d};a.in\
stanceOf=functio\
n(b,c){return nu\
ll!=b&&c&&(b==c|\
|b instanceof c|\
|0<=a.getInherit\
edLevel(a.getCla\
ssName(b),c))};a\
.superCall=funct\
ion(b,c,d,e){var\
 h=null,k=-1,l=b\
[d];if(l)if(l.cl\
axxOwner)l.claxx\
Owner!==c&&(h=l)\
;else if(!l.stac\
ks&&\x0a(!l.lastCla\
xxRef||!l.lastCl\
axxRef.prototype\
[d]||!l.lastClax\
xRef.prototype[d\
].stacks))h=l;el\
se{var m=l.stack\
s;m||(m=l.lastCl\
axxRef.prototype\
[d].stacks);for(\
k=m.length;0<=--\
k;)if(c===m[k]){\
h=0<k?m[--k].pro\
totype[d]:m[0].p\
rototype[d][\x22\x5c\x5cu\
nknown\x22];break}e\
lse if(0<a.getIn\
heritedLevel(c,m\
[k])){h=m[k].pro\
totype[d];break}\
}if(h)return 0==\
k&&\x22construct\x22==\
d&&(c=l.stacks)&\
&(!c[0].superCla\
zz&&c[0].con$tru\
ct)&&c[0].con$tr\
uct.apply(b,[]),\
h.apply(b,e||[])\
;\x22construct\x22!=d&\
&(a.alert([\x22j2sl\
ib\x22,\x22no class fo\
und\x22,e.typeStrin\
g]),\x0afb(b,c,d,a.\
getParamsType(e)\
.typeString))};a\
.superConstructo\
r=function(b,c,d\
){a.superCall(b,\
c,\x22construct\x22,d)\
;c.con$truct&&c.\
con$truct.apply(\
b,[])};a.CastedN\
ull=function(b){\
this.clazzName=b\
?b instanceof St\
ring?b:b instanc\
eof Function?a.g\
etClassName(b,!0\
):\x22\x22+b:\x22Object\x22;\
this.toString=fu\
nction(){return \
null};this.value\
Of=function(){re\
turn null}};a.ca\
stNullAs=functio\
n(b){return new \
a.CastedNull(b)}\
;a._initializing\
Exception=!1;a._\
callingStackTrac\
es=[];var b=func\
tion(){this.toSt\
ring=function(){\
return\x22J2S Metho\
dException\x22}},\x0ac\
;try{null.hello(\
)}catch(d){if(l=\
function(a,b,c){\
c||(c=\x22[^\x5c\x5cs]+\x22)\
;var d=a.indexOf\
(b);a=a.substrin\
g(0,d)+c+a.subst\
ring(d+b.length)\
;return RegExp(\x22\
^\x22+a+\x22$\x22)},/Oper\
a[\x5c/\x5cs](\x5cd+\x5c.\x5cd+\
)/.test(navigato\
r.userAgent)){va\
r l=d.message.in\
dexOf(\x22:\x22),t=d.m\
essage.indexOf(\x22\
:\x22,l+2),F=d.mess\
age.substr(l+1,t\
-l-20);c=functio\
n(a){return-1!=a\
.message.indexOf\
(F)}}else if(-1!\
=navigator.userA\
gent.toLowerCase\
().indexOf(\x22webk\
it\x22)){var C=l(d.\
message,\x22hello\x22)\
;c=function(a){r\
eturn C.test(a.m\
essage)}}else C=\
l(d.message,\x22$$o\
$$\x22),\x0ac=function\
(a){return C.tes\
t(a.message)}}a.\
exceptionOf=func\
tion(b,d){if(b._\
_CLASS_NAME__)re\
turn a.instanceO\
f(b,d);b.getMess\
age||(b.getMessa\
ge=function(){re\
turn\x22\x22+b+(b.stac\
k?\x22\x5cn\x22+b.stack:\x22\
\x22)});b.printStac\
kTrace||(b.print\
StackTrace=funct\
ion(){});if(d==E\
rror){if(0>(\x22\x22+b\
).indexOf(\x22Error\
\x22))return!1;Syst\
em.out.println(a\
.getStackTrace()\
);return!0}retur\
n d==Exception||\
d==Throwable||d=\
=NullPointerExce\
ption&&c(b)};a.g\
etStackTrace=fun\
ction(a){a||(a=2\
5);var b=\x22\x5cn\x22,c=\
arguments.callee\
,d=0>a;d&&(a=-a)\
;for(var e=\x0a0;e<\
a&&(c=c.caller);\
e++){var h=c.toS\
tring?c.toString\
().substring(0,c\
.toString().inde\
xOf(\x22{\x22)):\x22<nati\
ve method>\x22,b=b+\
(e+\x22 \x22+(c.exName\
?(c.claxxOwner?c\
.claxxOwner.__CL\
ASS_NAME__+\x22.\x22:\x22\
\x22)+c.exName+h.re\
place(/function \
/,\x22\x22):h)+\x22\x5cn\x22);i\
f(c==c.caller){b\
+=\x22<recursing>\x5cn\
\x22;break}if(d)for\
(var h=c.argumen\
ts,k=0;k<h.lengt\
h;k++){var l=\x22\x22+\
h[k];60<l.length\
&&(l=l.substring\
(0,60)+\x22...\x22);b+\
=\x22 args[\x22+k+\x22]=\x22\
+l.replace(/\x5cs+/\
g,\x22 \x22)+\x22\x5cn\x22}}ret\
urn b};a.makeCon\
structor=functio\
n(b,c,d){a.defin\
eMethod(b,\x22const\
ruct\x22,c,d);b.con\
$truct&&\x0a(b.con$\
truct.index=b.co\
n$truct.stacks.l\
ength)};a.overri\
deConstructor=fu\
nction(b,c,d){a.\
overrideMethod(b\
,\x22construct\x22,c,d\
);b.con$truct&&(\
b.con$truct.inde\
x=b.con$truct.st\
acks.length)};a.\
defineMethod=fun\
ction(j,c,d,h){d\
.exName=c;h=Ea(h\
);var k=j.protot\
ype,l=k[c];a._Lo\
ader._checkLoad&\
&K(j,c,h);if(!l|\
|l.claxxOwner===\
j&&l.funParams==\
h)return d.funPa\
rams=h,d.claxxOw\
ner=j,d.exClazz=\
j,k[c]=d;var m=n\
ull,q=l.stacks;q\
||(q=[],m=l,l.cl\
axxOwner&&(q[0]=\
m.claxxOwner));i\
f(!l.stacks||l.c\
laxxReference!==\
j){++P;l=functio\
n(){var j;\x0aa:{va\
r c=arguments.ca\
llee.claxxRefere\
nce,d=arguments.\
callee.methodNam\
e;j=arguments;fx\
=this[d];var h=a\
.getParamsType(j\
);if(!fx)try{Sys\
tem.out.println(\
a.getStackTrace(\
5))}catch(n){}if\
(e){var k=c.__CL\
ASS_NAME__+\x22 \x22+d\
+\x22 \x22;0>U.indexOf\
(k)&&(U+=k+\x22\x5cn\x22)\
;e[k]||(e[k]=0);\
e[k]++}if(fx.las\
tParams==h.typeS\
tring&&fx.lastCl\
axxRef===c){if(h\
.hasCastedNull){\
c=[];for(d=0;d<j\
.length;d++)c[d]\
=j[d]instanceof \
a.CastedNull?nul\
l:j[d]}else c=j;\
j=fx.lastMethod?\
fx.lastMethod.ap\
ply(this,c):null\
}else{fx.lastPar\
ams=h.typeString\
;\x0afx.lastClaxxRe\
f=c;k=fx.stacks;\
k||(k=c.prototyp\
e[d].stacks);for\
(var r=!1,l=k.le\
ngth;0<=--l;)if(\
r||k[l]===c){var\
 m=k[l].prototyp\
e[d],z=h,r=j,q=f\
x,s=[],t=!0,G=vo\
id 0;for(G in m)\
if(92==G.charCod\
eAt(0)){var u=G.\
substring(1).spl\
it(\x22\x5c\x5c\x22);u.lengt\
h==z.length&&s.p\
ush(u);t=!1}else\
 if(t&&\x22funParam\
s\x22==G&&m.funPara\
ms){G=m.funParam\
s;u=G.substring(\
1).split(\x22\x5c\x5c\x22);u\
.length==z.lengt\
h&&(s[0]=u);brea\
k}G=void 0;if(!(\
G=0==s.length)){\
G=void 0;for(var\
 G=[],Q=s.length\
,u=0;u<Q;u++){fo\
r(var x=[],za=!0\
,D=s[u].length,C\
=0;C<D;C++)if(x[\
C]=\x0aa.getInherit\
edLevel(z[C],s[u\
][C]),0>x[C]){za\
=!1;break}za&&(x\
[z.length]=u,G.p\
ush(x))}if(0==G.\
length)G=null;el\
se{Q=G[0];for(u=\
1;u<G.length;u++\
){x=!0;for(C=0;C\
<z.length;C++)if\
(Q[C]<G[u][C]){x\
=!1;break}x&&(Q=\
G[u])}G=s[Q[z.le\
ngth]].join(\x22\x5c\x5c\x22\
)}G=!(s=G)}if(G)\
r=new b;else{m=t\
?m:m[\x22\x5c\x5c\x22+s];t=n\
ull;if(z.hasCast\
edNull){t=[];for\
(z=0;z<r.length;\
z++)t[z]=r[z]ins\
tanceof a.Casted\
Null?null:r[z]}e\
lse t=r;q.lastMe\
thod=m;r=m.apply\
(this,t)}if(!(r \
instanceof b)){j\
=r;break a}r=!0}\
\x22construct\x22!=d&&\
fb(this,c,d,h.ty\
peString);\x0aj=voi\
d 0}}return j};l\
.methodName=c;l.\
claxxReference=j\
;l=k[c]=l;c=[];f\
or(k=0;k<q.lengt\
h;k++)c[k]=q[k];\
l.stacks=c}q=l.s\
tacks;0>rb(q,j)&\
&q.push(j);m&&(m\
.claxxOwner===j?\
(l[m.funParams]=\
m,m.claxxOwner=n\
ull,m.funParams=\
null):m.claxxOwn\
er||(l[\x22\x5c\x5cunknow\
n\x22]=m));d.exClaz\
z=j;l[h]=d;retur\
n l};duplicatedM\
ethods={};var K=\
function(b,c,d){\
var e=b.prototyp\
e[c];if(e&&(e.cl\
axxOwner||e.clax\
xReference)===b)\
key=b.__CLASS_NA\
ME__+\x22.\x22+c+d,(b=\
duplicatedMethod\
s[key])?(c=\x22Warn\
ing! Duplicate m\
ethod found for \
\x22+key,System.out\
.println(c),\x0aa.a\
lert(c),duplicat\
edMethods[key]=b\
+1):duplicatedMe\
thods[key]=1};a.\
showDuplicates=f\
unction(a){var b\
=\x22\x22,c=duplicated\
Methods,d=0,e;fo\
r(e in c)1<c[e]&\
&(b+=c[e]+\x22\x5ct\x22+e\
+\x22\x5cn\x22,d++);b=\x22Du\
plicates: \x22+d+\x22\x5c\
n\x5cn\x22+b;System.ou\
t.println(b);a||\
alert(b)};var rb\
=function(a,b){i\
f(a&&b)for(var c\
=a.length;0<=--c\
;)if(a[c]===b)re\
turn c;return-1}\
,Ya=function(a,b\
){var c=rb(a,b);\
if(0<=c){for(var\
 d=a.length-1;c<\
d;c++)a[c]=a[c+1\
];a.length--;ret\
urn!0}},Ea=funct\
ion(a){return a?\
a.replace(/~([NA\
BSO])/g,function\
(a,b){switch(b){\
case \x22N\x22:return\x22\
n\x22;\x0acase \x22B\x22:ret\
urn\x22b\x22;case \x22S\x22:\
return\x22String\x22;c\
ase \x22O\x22:return\x22O\
bject\x22;case \x22A\x22:\
return\x22Array\x22}re\
turn\x22Unknown\x22}).\
replace(/\x5cs+/g,\x22\
\x22).replace(/^|,/\
g,\x22\x5c\x5c\x22).replace(\
/\x5c$/g,\x22org.eclip\
se.s\x22):\x22\x5c\x5cvoid\x22}\
;a.overrideMetho\
d=function(b,c,d\
,e){d.exName=c;e\
=Ea(e);a._Loader\
._checkLoad&&K(b\
,c,e);d.funParam\
s=e;d.claxxOwner\
=b;return b.prot\
otype[c]=d};var \
U=\x22\x22;a.getProfil\
e=function(){var\
 a=\x22\x22;if(e){var \
a=[],b;for(b in \
e){var c=\x22\x22+e[b]\
;a.push(\x22       \
 \x22.substring(c.l\
ength)+c+\x22\x5ct\x22+b)\
}a=a.sort().reve\
rse().join(\x22\x5cr\x5cn\
\x22);e={}}return a\
};\x0aa.getParamsTy\
pe=function(b){v\
ar c=b.length;sw\
itch(c){case 0:v\
ar d=[\x22void\x22];d.\
typeString=\x22\x5c\x5cvo\
id\x22;return d;cas\
e 1:switch(typeo\
f obj){case \x22num\
ber\x22:return d=[\x22\
n\x22],d.typeString\
=\x22\x5c\x5cn\x22,d;case \x22b\
oolean\x22:return d\
=[\x22b\x22],d.typeStr\
ing=\x22\x5c\x5cb\x22,d}}d=[\
];d.hasCastedNul\
l=!1;if(b)for(va\
r e=0;e<c;e++)d[\
e]=a.getClassNam\
e(b[e]),b[e]inst\
anceof a.CastedN\
ull&&(d.hasCaste\
dNull=!0);d.type\
String=\x22\x5c\x5c\x22+d.jo\
in(\x22\x5c\x5c\x22);return \
d};var P=0;a.all\
Package={};a.all\
Classes={};a.las\
tPackageName=nul\
l;a.lastPackage=\
null;a.unloadedC\
lasses=[];\x0aa.dec\
larePackage=func\
tion(b){if(a.las\
tPackageName==b)\
return a.lastPac\
kage;if(b&&b.len\
gth){for(var c=b\
.split(/\x5c./),d=a\
.allPackage,e=0;\
e<c.length;e++)d\
[c[e]]||(d[c[e]]\
={__PKG_NAME__:d\
.__PKG_NAME__?d.\
__PKG_NAME__+\x22.\x22\
+c[e]:c[e]},0==e\
&&a.setGlobal(c[\
e],d[c[e]])),d=d\
[c[e]];a.lastPac\
kageName=b;retur\
n a.lastPackage=\
d}};a.evalType=f\
unction(b,c){var\
 d=b.lastIndexOf\
(\x22.\x22);if(-1!=d){\
var e=b.substrin\
g(0,d),e=a.decla\
rePackage(e),d=b\
.substring(d+1);\
return e[d]}if(c\
)return window[b\
];switch(b){case\
 \x22string\x22:return\
 String;\x0acase \x22n\
umber\x22:return Nu\
mber;case \x22objec\
t\x22:return a._O;c\
ase \x22boolean\x22:re\
turn Boolean;cas\
e \x22function\x22:ret\
urn Function;cas\
e \x22void\x22:case \x22u\
ndefined\x22:case \x22\
unknown\x22:return \
b;case \x22NullObje\
ct\x22:return NullO\
bject;default:re\
turn window[b]}}\
;a.defineType=fu\
nction(b,c,d,e){\
var h=a.unloaded\
Classes[b];h&&(c\
=h);h=b.lastInde\
xOf(\x22.\x22);if(-1!=\
h){var k=b.subst\
ring(0,h),k=a.de\
clarePackage(k),\
h=b.substring(h+\
1);if(k[h])retur\
n k[h];k[h]=c}el\
se{if(window[b])\
return window[b]\
;a.setGlobal(b,c\
)}a.decorateAsTy\
pe(c,b,d,e);b=\x0aa\
._innerFunctions\
;c.defineMethod=\
b.defineMethod;c\
.defineStaticMet\
hod=b.defineStat\
icMethod;c.makeC\
onstructor=b.mak\
eConstructor;ret\
urn c};var Fa=!1\
;-1!=navigator.u\
serAgent.indexOf\
(\x22Safari\x22)&&(l=n\
avigator.userAge\
nt,t=l.indexOf(\x22\
Version/\x22),-1!=t\
&&(l=l.substring\
(t+8),Fa=4<=pars\
eFloat(l)));a.in\
stantialize=func\
tion(a,b){if(!b|\
|!(1==b.length&&\
b[0]&&b[0]instan\
ceof s)){a insta\
nceof Number&&(a\
.valueOf=functio\
n(){return this}\
);if(Fa){for(var\
 c=[],d=0;d<b.le\
ngth;d++)c[d]=b[\
d];b=c}(c=a.cons\
truct)?a.con$tru\
ct?a.getClass().\
superClazz?\x0ac.cl\
axxOwner&&c.clax\
xOwner===a.getCl\
ass()||c.stacks&\
&c.stacks[c.stac\
ks.length-1]==a.\
getClass()?c.app\
ly(a,b):(c.claxx\
Owner&&!c.claxxO\
wner.superClazz&\
&c.claxxOwner.co\
n$truct?c.claxxO\
wner.con$truct.a\
pply(a,[]):c.sta\
cks&&(1==c.stack\
s.length&&!c.sta\
cks[0].superClaz\
z)&&c.stacks[0].\
con$truct.apply(\
a,[]),c.apply(a,\
b),a.con$truct.a\
pply(a,[])):(a.c\
on$truct.apply(a\
,[]),c.apply(a,b\
)):c.apply(a,b):\
a.con$truct&&a.c\
on$truct.apply(a\
,[])}};a.innerFu\
nctionNames=\x22isI\
nstance equals h\
ashCode getName \
getCanonicalName\
 getClassLoader \
getResource getR\
esourceAsStream \
defineMethod def\
ineStaticMethod \
makeConstructor\x22\
.split(\x22 \x22);\x0aa._\
innerFunctions={\
isInstance:funct\
ion(b){return a.\
instanceOf(b,thi\
s)},equals:funct\
ion(a){return th\
is===a},hashCode\
:function(){retu\
rn this.getName(\
).hashCode()},to\
String:function(\
){return\x22class \x22\
+this.getName()}\
,getName:functio\
n(){return a.get\
ClassName(this,!\
0)},getCanonical\
Name:function(){\
return this.__CL\
ASS_NAME__},getC\
lassLoader:funct\
ion(){var b=this\
.__CLASS_NAME__,\
c=a._Loader.getC\
lasspathFor(b),d\
=c.lastIndexOf(b\
.replace(/\x5c./g,\x22\
/\x22)),c=-1!=d?c.s\
ubstring(0,d):a.\
_Loader.getClass\
pathFor(b,!0),b=\
a._Loader.requir\
eLoaderByBase(c)\
;\x0ab.getResourceA\
sStream=a._inner\
Functions.getRes\
ourceAsStream;b.\
getResource=a._i\
nnerFunctions.ge\
tResource;return\
 b},getResource:\
function(a){retu\
rn(a=this.getRes\
ourceAsStream(a)\
)?a.url:null},ge\
tResourceAsStrea\
m:function(b){if\
(!b)return null;\
b=b.replace(/\x5c\x5c/\
g,\x22/\x22);var c=nul\
l,d=b,d=this.__C\
LASS_NAME__;2==a\
rguments.length&\
&0!=b.indexOf(\x22/\
\x22)&&(b=\x22/\x22+b);if\
(0==b.indexOf(\x22/\
\x22))if(2==argumen\
ts.length?(c=arg\
uments[1])||(c=a\
.binaryFolders[0\
]):a._Loader&&(c\
=a._Loader.getCl\
asspathFor(d,!0)\
),c){var c=c.rep\
lace(/\x5c\x5c/g,\x0a\x22/\x22)\
,e=c.length,e=c.\
charAt(e-1);\x22/\x22!\
=e&&(c+=\x22/\x22);d=c\
+b.substring(1)}\
else d=b.substri\
ng(1);else{if(th\
is.base)c=this.b\
ase;else if(a._L\
oader)if(c=a._Lo\
ader.getClasspat\
hFor(d),e=c.last\
IndexOf(d.replac\
e(/\x5c./g,\x22/\x22)),-1\
!=e)c=c.substrin\
g(0,e);else if(e\
=-1,c.indexOf(\x22.\
z.js\x22)==c.length\
-5&&-1!=(e=c.las\
tIndexOf(\x22/\x22)))f\
or(var c=c.subst\
ring(0,e+1),e=d.\
split(/\x5c./),h=1;\
h<e.length;h++){\
for(var k=\x22/\x22,l=\
0;l<h;l++)k+=e[l\
]+\x22/\x22;if(k.lengt\
h>c.length)break\
;if(c.indexOf(k)\
==c.length-k.len\
gth){c=c.substri\
ng(0,c.length-k.\
length+\x0a1);break\
}}else c=a._Load\
er.getClasspathF\
or(d,!0);else(e=\
a.binaryFolders)\
&&e.length&&(c=e\
[0]);c||(c=\x22j2s/\
\x22);c=c.replace(/\
\x5c\x5c/g,\x22/\x22);e=c.le\
ngth;e=c.charAt(\
e-1);\x22/\x22!=e&&(c+\
=\x22/\x22);this.base?\
d=c+b:(e=d.lastI\
ndexOf(\x22.\x22),d=-1\
==e||this.base?c\
+b:c+d.substring\
(0,e).replace(/\x5c\
./g,\x22/\x22)+\x22/\x22+b)}\
c=null;try{if(0>\
d.indexOf(\x22:/\x22))\
{var q=document.\
location.href.sp\
lit(\x22?\x22)[0].spli\
t(\x22/\x22);q[q.lengt\
h-1]=d;d=q.join(\
\x22/\x22)}c=new java.\
net.URL(d)}catch\
(s){}q=null==c?n\
ull:m._getFileDa\
ta(d.toString())\
;if(!q||\x22error\x22=\
=q||0==q.indexOf\
(\x22[Exception\x22))r\
eturn null;\x0aq=(n\
ew java.lang.Str\
ing(q)).getBytes\
();q=new java.io\
.BufferedInputSt\
ream(new java.io\
.ByteArrayInputS\
tream(q));q.url=\
c;return q},defi\
neMethod:functio\
n(b,c,d){a.defin\
eMethod(this,b,c\
,d)},defineStati\
cMethod:function\
(b,c,d){a.define\
Method(this,b,c,\
d);this[b]=this.\
prototype[b]},ma\
keConstructor:fu\
nction(b,c){a.ma\
keConstructor(th\
is,b,c)}};var Pa\
=[];a.pu$h=funct\
ion(a){a||(a=sel\
f.c$);a&&Pa.push\
(a)};a.p0p=funct\
ion(){return Pa.\
pop()};a.decorat\
eAsClass=functio\
n(b,c,d,e,h,k){v\
ar l=null;c&&(l=\
c.__PKG_NAME__,l\
||\x0a(l=c.__CLASS_\
NAME__));var m=(\
l?l+\x22.\x22:\x22\x22)+d;a.\
_Loader._classPe\
nding[m]&&(delet\
e a._Loader._cla\
ssPending[m],a._\
Loader._classCou\
ntOK++,a._Loader\
._classCountPend\
ing--);a._Loader\
&&a._Loader._che\
ckLoad&&System.o\
ut.println(\x22deco\
rating class \x22+l\
+\x22.\x22+d);(l=a.unl\
oadedClasses[m])\
&&(b=l);db(b,c,d\
);k?a.inheritCla\
ss(b,e,k):e&&a.i\
nheritClass(b,e)\
;h&&a.implementO\
f(b,h);return b}\
;var db=function\
(b,c,d){var e;c?\
c.__PKG_NAME__?(\
e=c.__PKG_NAME__\
+\x22.\x22+d,c[d]=b,c=\
==java.lang&&a.s\
etGlobal(d,b)):(\
e=c.__CLASS_NAME\
__+\x22.\x22+d,\x0ac[d]=b\
):(e=d,a.setGlob\
al(d,b));a.exten\
dJO(b,e);c=a.inn\
erFunctionNames;\
for(d=0;d<c.leng\
th;d++)b[c[d]]=a\
._innerFunctions\
[c[d]];a._Loader\
&&a._Loader.upda\
teNodeForFunctio\
nDecoration(e)};\
a.declareInterfa\
ce=function(b,c,\
d){var e=functio\
n(){};db(e,b,c);\
d&&a.implementOf\
(e,d);return e};\
a.declareType=fu\
nction(b,c,d,e,h\
){return a.decor\
ateAsClass(funct\
ion(){a.instanti\
alize(this,argum\
ents)},b,c,d,e,h\
)};a.declareAnon\
ymous=function(b\
,c,d,e,h){return\
 a.decorateAsCla\
ss(function(){a.\
prepareCallback(\
this,arguments);\
\x0aa.instantialize\
(this,arguments)\
},b,c,d,e,h)};a.\
decorateAsType=f\
unction(b,c,d,e,\
h,k){a.extendJO(\
b,c);b.equals=a.\
_innerFunctions.\
equals;b.getName\
=a._innerFunctio\
ns.getName;if(k)\
for(c=0;c<a.inne\
rFunctionNames.l\
ength;c++)k=a.in\
nerFunctionNames\
[c],b[k]=a._inne\
rFunctions[k];h?\
a.inheritClass(b\
,d,h):d&&a.inher\
itClass(b,d);e&&\
a.implementOf(b,\
e);return b};Num\
ber.prototype._n\
umberToString=Nu\
mber.prototype.t\
oString;a.declar\
ePackage(\x22java.i\
o\x22);a.declarePac\
kage(\x22java.lang.\
annotation\x22);a.d\
eclarePackage(\x22j\
ava.lang.instrum\
ent\x22);\x0aa.declare\
Package(\x22java.la\
ng.management\x22);\
a.declarePackage\
(\x22java.lang.refl\
ect\x22);a.declareP\
ackage(\x22java.lan\
g.ref\x22);java.lan\
g.ref.reflect=ja\
va.lang.reflect;\
a.declarePackage\
(\x22java.util\x22);a.\
declarePackage(\x22\
java.security\x22);\
a.declareInterfa\
ce(java.io,\x22Clos\
eable\x22);a.declar\
eInterface(java.\
io,\x22DataInput\x22);\
a.declareInterfa\
ce(java.io,\x22Data\
Output\x22);a.decla\
reInterface(java\
.io,\x22Externaliza\
ble\x22);a.declareI\
nterface(java.io\
,\x22Flushable\x22);a.\
declareInterface\
(java.io,\x22Serial\
izable\x22);a.decla\
reInterface(java\
.lang,\x22Iterable\x22\
);\x0aa.declareInte\
rface(java.lang,\
\x22CharSequence\x22);\
a.declareInterfa\
ce(java.lang,\x22Cl\
oneable\x22);a.decl\
areInterface(jav\
a.lang,\x22Appendab\
le\x22);a.declareIn\
terface(java.lan\
g,\x22Comparable\x22);\
a.declareInterfa\
ce(java.lang,\x22Ru\
nnable\x22);a.decla\
reInterface(java\
.util,\x22Comparato\
r\x22);java.lang.Cl\
assLoader={__CLA\
SS_NAME__:\x22Class\
Loader\x22};var fb=\
function(b,c,d,e\
){b=\x22\x22;e&&(b=e.s\
ubstring(1).repl\
ace(/\x5c\x5c/g,\x22,\x22));\
c=(d&&\x22construct\
\x22!=d?\x22Method\x22:\x22C\
onstructor\x22)+\x22 \x22\
+a.getClassName(\
c,!0)+\x22.\x22+d+\x22(\x22+\
b+\x22) is not foun\
d!\x22;throw new ja\
va.lang.NoSuchMe\
thodException(c)\
;\x0a};a.prepareCal\
lback=function(b\
,c){var d=c[0];i\
f(b&&d&&d!==wind\
ow){var e=a.getC\
lassName(d,!0),h\
={};if(b.b$)for(\
var k in b.b$)h[\
k]=b.b$[k];b.b$=\
h;h[e]=d;for(e=a\
.getClass(d);e.s\
uperClazz;)e=e.s\
uperClazz,h[a.ge\
tClassName(e,!0)\
]=d;if(d=d.b$)fo\
r(k in d)h[k]=d[\
k]}for(h=0;h<c.l\
ength-1;h++)c[h]\
=c[h+1];c.length\
--};a.innerTypeI\
nstance=function\
(b,c,d){b||(b=ar\
guments.callee.c\
aller);var e;if(\
d||c.$finals)if(\
e=new b(c,a.inhe\
ritArgs),d)if(c.\
f$){var h={},k;f\
or(k in c.f$)h[k\
]=c.f$[k];for(k \
in d)h[k]=d[k];e\
.f$=h}else e.f$=\
\x0ad;else c.f$&&(e\
.f$=c.f$);else s\
witch(arguments.\
length){case 3:r\
eturn new b(c);c\
ase 4:return c._\
_CLASS_NAME__==b\
.__CLASS_NAME__&\
&arguments[3]===\
a.inheritArgs?c:\
new b(c,argument\
s[3]);case 5:ret\
urn new b(c,argu\
ments[3],argumen\
ts[4]);case 6:re\
turn new b(c,arg\
uments[3],argume\
nts[4],arguments\
[5]);case 7:retu\
rn new b(c,argum\
ents[3],argument\
s[4],arguments[5\
],arguments[6]);\
case 8:return ne\
w b(c,arguments[\
3],arguments[4],\
arguments[5],arg\
uments[6],argume\
nts[7]);case 9:r\
eturn new b(c,ar\
guments[3],argum\
ents[4],\x0aargumen\
ts[5],arguments[\
6],arguments[7],\
arguments[8]);ca\
se 10:return new\
 b(c,arguments[3\
],arguments[4],a\
rguments[5],argu\
ments[6],argumen\
ts[7],arguments[\
8],arguments[9])\
;default:e=new b\
(c,a.inheritArgs\
)}k=arguments.le\
ngth-3;for(h=Arr\
ay(k);0<=--k;)h[\
k]=arguments[k+3\
];a.instantializ\
e(e,h);return e}\
;a.cloneFinals=f\
unction(){for(va\
r a={},b=argumen\
ts.length/2;0<=-\
-b;)a[arguments[\
b+b]]=arguments[\
b+b+1];return a}\
;a.isClassDefine\
d=a.isDefinedCla\
ss=function(b){i\
f(!b)return!1;if\
(a.allClasses[b]\
)return!0;for(va\
r c=\x0ab.split(/\x5c.\
/),d=null,e=0;e<\
c.length;e++)if(\
!(d=d?d[c[e]]:a.\
allPackage[c[0]]\
))return!1;retur\
n d&&(a.allClass\
es[b]=!0)};a.def\
ineEnumConstant=\
function(a,b,c,d\
,e){e=e?new e:ne\
w a;e.$name=b;e.\
$ordinal=c;d&&d.\
length&&e.constr\
uct.apply(e,d);a\
[b]=e;a.prototyp\
e[b]=e;a[\x22$ valu\
es\x22]||(a[\x22$ valu\
es\x22]=[],a.values\
=function(){retu\
rn this[\x22$ value\
s\x22]});a[\x22$ value\
s\x22].push(e);retu\
rn e};a.floatToI\
nt=function(a){r\
eturn isNaN(a)?0\
:0>a?Math.ceil(a\
):Math.floor(a)}\
;a.floatToByte=a\
.floatToShort=a.\
floatToLong=a.fl\
oatToInt;a.doubl\
eToByte=\x0aa.doubl\
eToShort=a.doubl\
eToLong=a.double\
ToInt=a.floatToI\
nt;a.floatToChar\
=function(a){ret\
urn String.fromC\
harCode(0>a?Math\
.ceil(a):Math.fl\
oor(a))};a.doubl\
eToChar=a.floatT\
oChar;var gb=fun\
ction(a,b){a||(a\
=0);if(\x22object\x22=\
=typeof a)var c=\
a;else for(var c\
=Array(a),d=0;d<\
a;d++)c[d]=0;c.B\
YTES_PER_ELEMENT\
=b>>3;c._fake=!0\
;return c},va=fu\
nction(a,b){a||(\
a=0);b||(b=this.\
length);if(this.\
_fake){var c=new\
 this.constructo\
r(b-a);System.ar\
raycopy(this,a,c\
,0,b-a);return c\
}return new this\
.constructor(thi\
s.buffer.slice(a\
*\x0athis.BYTES_PER\
_ELEMENT,b*this.\
BYTES_PER_ELEMEN\
T))};!0==(a.have\
Int32=!!(self.In\
t32Array&&self.I\
nt32Array!=Array\
))?Int32Array.pr\
ototype.sort||(I\
nt32Array.protot\
ype.sort=Array.p\
rototype.sort):(\
Int32Array=funct\
ion(a){return gb\
(a,32)},Int32Arr\
ay.prototype.sor\
t=Array.prototyp\
e.sort,Int32Arra\
y.prototype.toSt\
ring=function(){\
return\x22[object I\
nt32Array]\x22});In\
t32Array.prototy\
pe.slice||(Int32\
Array.prototype.\
slice=function()\
{return va.apply\
(this,arguments)\
});Int32Array.pr\
ototype.clone=fu\
nction(){var a=t\
his.slice();\x0aa.B\
YTES_PER_ELEMENT\
=4;return a};!0=\
=(a.haveFloat64=\
!!(self.Float64A\
rray&&self.Float\
64Array!=Array))\
?Float64Array.pr\
ototype.sort||(F\
loat64Array.prot\
otype.sort=Array\
.prototype.sort)\
:(Float64Array=f\
unction(a){retur\
n gb(a,64)},Floa\
t64Array.prototy\
pe.sort=Array.pr\
ototype.sort,Flo\
at64Array.protot\
ype.toString=fun\
ction(){return\x22[\
object Float64Ar\
ray]\x22});Float64A\
rray.prototype.s\
lice||(Float64Ar\
ray.prototype.sl\
ice=function(){r\
eturn va.apply(t\
his,arguments)})\
;Float64Array.pr\
ototype.clone=fu\
nction(){return \
this.slice()};\x0aa\
.newArray=functi\
on(a,b,c,d){if(-\
1!=a||2==argumen\
ts.length)return\
 la(arguments,0)\
;a=b.slice(c,d);\
a.BYTES_PER_ELEM\
ENT=b.BYTES_PER_\
ELEMENT;return a\
};var la=functio\
n(a,b){var c=a[0\
];\x22string\x22==type\
of c&&(c=c.charC\
odeAt(0));var d=\
a.length-1,e=a[d\
];if(1<d){for(va\
r e=Array(d),h=0\
;h<d;h++)e[h]=a[\
h+1];d=Array(c);\
for(h=0;h<c;h++)\
d[h]=la(e,b);ret\
urn d}0<b&&0>c&&\
(c=e);switch(b){\
case 8:return d=\
new Int8Array(c)\
,d.BYTES_PER_ELE\
MENT=1,d;case 32\
:return d=new In\
t32Array(c),d.BY\
TES_PER_ELEMENT=\
4,d;case 64:retu\
rn d=\x0anew Float6\
4Array(c),d.BYTE\
S_PER_ELEMENT=8,\
d;default:d=0>c?\
e:Array(c);d.BYT\
ES_PER_ELEMENT=0\
;if(0<c&&null!=e\
)for(h=c;0<=--h;\
)d[h]=e;return d\
}};a.newByteArra\
y=function(){ret\
urn la(arguments\
,8)};a.newIntArr\
ay=function(){re\
turn la(argument\
s,32)};a.newFloa\
tArray=function(\
){return la(argu\
ments,64)};a.new\
DoubleArray=a.ne\
wFloatArray;a.ne\
wLongArray=a.new\
ShortArray=a.new\
IntArray;a.newCh\
arArray=a.newBoo\
leanArray=a.newA\
rray;!0==(a.have\
Int8=!!self.Int8\
Array)?(Int8Arra\
y.prototype.sort\
||(Int8Array.pro\
totype.sort=\x0aArr\
ay.prototype.sor\
t),Int8Array.pro\
totype.slice||(I\
nt8Array.prototy\
pe.slice=functio\
n(){return va.ap\
ply(this,argumen\
ts)})):a.newByte\
Array=a.newIntAr\
ray;Int8Array.pr\
ototype.clone=fu\
nction(){var a=t\
his.slice();a.BY\
TES_PER_ELEMENT=\
1;return a};a.is\
AB=function(a){r\
eturn a&&\x22object\
\x22==typeof a&&1==\
a.BYTES_PER_ELEM\
ENT};a.isAI=func\
tion(a){return a\
&&\x22object\x22==type\
of a&&4==a.BYTES\
_PER_ELEMENT};a.\
isAF=function(a)\
{return a&&\x22obje\
ct\x22==typeof a&&8\
==a.BYTES_PER_EL\
EMENT};a.isAS=fu\
nction(a){return\
 a&&\x22object\x22==ty\
peof a&&\x0aa.const\
ructor==Array&&(\
\x22string\x22==typeof\
 a[0]||\x22undefine\
d\x22==typeof a[0])\
};a.isAII=functi\
on(b){return b&&\
\x22object\x22==typeof\
 b&&a.isAI(b[0])\
};a.isAFF=functi\
on(b){return b&&\
\x22object\x22==typeof\
 b&&a.isAF(b[0])\
};a.isAFFF=funct\
ion(b){return b&\
&\x22object\x22==typeo\
f b&&a.isAFF(b[0\
])};a.isASS=func\
tion(b){return b\
&&\x22object\x22==type\
of b&&a.isAS(b[0\
])};a.isAFloat=f\
unction(b){retur\
n b&&\x22object\x22==t\
ypeof b&&b.const\
ructor==Array&&a\
.instanceOf(b[0]\
,Float)};a.isAP=\
function(b){retu\
rn b&&\x22JU.P3\x22==a\
.getClassName(b[\
0])};a.defineSta\
tics=\x0afunction(a\
){for(var b=argu\
ments.length,c=(\
b-1)/2;0<=--c;){\
var d=arguments[\
--b],e=arguments\
[--b];a[e]=a.pro\
totype[e]=d}};a.\
prepareFields=fu\
nction(a,b){var \
c=[];if(a.con$tr\
uct)for(var d=a.\
con$truct.stacks\
,e=0;e<d.length;\
e++)c[e]=d[e];d=\
a.con$truct=func\
tion(){var a=arg\
uments.callee.st\
acks;if(a)for(va\
r b=0;b<a.length\
;b++)a[b].apply(\
this,[])};a.prot\
otype.con$truct=\
d;c.push(b);a.co\
n$truct.stacks=c\
;a.con$truct.ind\
ex=0};a.checkPri\
vateMethod=funct\
ion(){me=argumen\
ts.callee.caller\
;caller=argument\
s.callee.caller.\
caller;\x0avar b=\x22\x5c\
\x5c\x22+a.getParamsTy\
pe(arguments[0])\
.join(\x22\x5c\x5c\x22);me.p\
rivateNote||(me.\
privateNote=\x22You\
 are seeing this\
 note because th\
e method \x22+me.ex\
Name+b+\x22 in clas\
s \x22+me.exClazz._\
_CLASS_NAME__+\x22 \
has a superclass\
 method by the s\
ame name (possib\
ly with the same\
 parameters) tha\
t is private and\
  therefore migh\
t be called impr\
operly from this\
 class. If your \
 code does not r\
un properly, or \
you want to make\
 it run faster, \
change the name \
of this method t\
o something else\
.\x22,System.out.pr\
intln(me.private\
Note),alert(me.p\
rivateNote));\x0are\
turn null};java.\
lang.Object=a._O\
;a._O.getName=a.\
_innerFunctions.\
getName;java.lan\
g.System=System=\
{props:null,$pro\
ps:{},arraycopy:\
function(a,b,c,d\
,e){if(a!==c||b>\
d)for(;0<=--e;)c\
[d++]=a[b++];els\
e{d+=e;for(b+=e;\
0<=--e;)a[--d]=a\
[--b]}},currentT\
imeMillis:functi\
on(){return(new \
Date).getTime()}\
,gc:function(){}\
,getProperties:f\
unction(){return\
 System.props},g\
etProperty:funct\
ion(a,b){if(Syst\
em.props)return \
System.props.get\
Property(a,b);va\
r c=System.$prop\
s[a];if(\x22undefin\
ed\x22!=typeof c)re\
turn c;if(0<a.in\
dexOf(\x22.\x22)){c=\x0an\
ull;switch(a){ca\
se \x22java.version\
\x22:case \x22file.sep\
arator\x22:case \x22pa\
th.separator\x22:c=\
\x22/\x22;break;case \x22\
line.separator\x22:\
c=0<=navigator.u\
serAgent.indexOf\
(\x22Windows\x22)?\x22\x5cr\x5c\
n\x22:\x22\x5cn\x22;break;ca\
se \x22os.name\x22:cas\
e \x22os.version\x22:c\
=navigator.userA\
gent}if(c)return\
 System.$props[a\
]=c}return 1==ar\
guments.length?n\
ull:null==b?a:b}\
,getSecurityMana\
ger:function(){r\
eturn null},setP\
roperties:functi\
on(a){System.pro\
ps=a},lineSepara\
tor:function(){r\
eturn\x22\x5cn\x22},setPr\
operty:function(\
a,b){if(!System.\
props)return Sys\
tem.$props[a]=b;\
System.props.set\
Property(a,\x0ab)}}\
;System.identity\
HashCode=functio\
n(b){return null\
==b?0:b._$hashco\
de||(b._$hashcod\
e=++a._hashCode)\
};System.out=new\
 a._O;System.out\
.__CLASS_NAME__=\
\x22java.io.PrintSt\
ream\x22;System.out\
.print=function(\
){};System.out.p\
rintf=function()\
{};System.out.pr\
intln=function()\
{};System.out.wr\
ite=function(){}\
;System.err=new \
a._O;System.err.\
__CLASS_NAME__=\x22\
java.io.PrintStr\
eam\x22;System.err.\
print=function()\
{};System.err.pr\
intf=function(){\
};System.err.pri\
ntln=function(){\
};System.err.wri\
te=function(){};\
a.popup=a.assert\
=\x0aa.log=a.error=\
window.alert;Thr\
ead=function(){}\
;Thread.J2S_THRE\
AD=Thread.protot\
ype.J2S_THREAD=n\
ew Thread;Thread\
.currentThread=T\
hread.prototype.\
currentThread=fu\
nction(){return \
this.J2S_THREAD}\
;a.innerFunction\
Names=a.innerFun\
ctionNames.conca\
t(\x22getSuperclass\
 isAssignableFro\
m getConstructor\
 getDeclaredMeth\
od getDeclaredMe\
thods getMethod \
getMethods getMo\
difiers newInsta\
nce\x22.split(\x22 \x22))\
;a._innerFunctio\
ns.getSuperclass\
=function(){retu\
rn this.superCla\
zz};a._innerFunc\
tions.isAssignab\
leFrom=function(\
b){return 0<=\x0aa.\
getInheritedLeve\
l(b,this)};a._in\
nerFunctions.get\
Constructor=func\
tion(){return ne\
w java.lang.refl\
ect.Constructor(\
this,[],[],java.\
lang.reflect.Mod\
ifier.PUBLIC)};a\
._innerFunctions\
.getDeclaredMeth\
ods=a._innerFunc\
tions.getMethods\
=function(){var \
a=[],b=this.prot\
otype,c;for(c in\
 b)\x22function\x22==t\
ypeof b[c]&&!b[c\
].__CLASS_NAME__\
&&a.push(new jav\
a.lang.reflect.M\
ethod(this,c,[],\
java.lang.Void,[\
],java.lang.refl\
ect.Modifier.PUB\
LIC));b=this;for\
(c in b)\x22functio\
n\x22==typeof b[c]&\
&!b[c].__CLASS_N\
AME__&&a.push(ne\
w java.lang.refl\
ect.Method(this,\
\x0ac,[],java.lang.\
Void,[],java.lan\
g.reflect.Modifi\
er.PUBLIC|java.l\
ang.reflect.Modi\
fier.STATIC));re\
turn a};a._inner\
Functions.getDec\
laredMethod=a._i\
nnerFunctions.ge\
tMethod=function\
(a){var b=this.p\
rototype,c;for(c\
 in b)if(a==c&&\x22\
function\x22==typeo\
f b[c]&&!b[c].__\
CLASS_NAME__)ret\
urn new java.lan\
g.reflect.Method\
(this,c,[],java.\
lang.Void,[],jav\
a.lang.reflect.M\
odifier.PUBLIC);\
b=this;for(c in \
b)if(a==c&&\x22func\
tion\x22==typeof b[\
c]&&!b[c].__CLAS\
S_NAME__)return \
new java.lang.re\
flect.Method(thi\
s,c,[],java.lang\
.Void,\x0a[],java.l\
ang.reflect.Modi\
fier.PUBLIC|java\
.lang.reflect.Mo\
difier.STATIC);r\
eturn null};a._i\
nnerFunctions.ge\
tModifiers=funct\
ion(){return jav\
a.lang.reflect.M\
odifier.PUBLIC};\
a._innerFunction\
s.newInstance=fu\
nction(a){switch\
(null==a?0:a.len\
gth){case 0:retu\
rn new this;case\
 1:return new th\
is(a[0]);case 2:\
return new this(\
a[0],a[1]);case \
3:return new thi\
s(a[0],a[1],a[2]\
);case 4:return \
new this(a[0],a[\
1],a[2],a[3]);de\
fault:for(var b=\
\x22new \x22+this.__CL\
ASS_NAME__+\x22(\x22,c\
=0;c<a.length;c+\
+)b+=(0==c?\x22\x22:\x22,\
\x22)+\x22a[\x22+c+\x22]\x22;\x0ar\
eturn eval(b+\x22)\x22\
)}};l=a.innerFun\
ctionNames;for(t\
=0;t<l.length;t+\
+)a._O[l[t]]=a._\
innerFunctions[l\
[t]],Array[l[t]]\
=a._innerFunctio\
ns[l[t]];a._Load\
er=a.ClazzLoader\
=function(){};va\
r x=function(){t\
his.parents=[];t\
his.musts=[];thi\
s.optionals=[];t\
his.onLoaded=thi\
s.path=this.name\
=this.declaratio\
n=null;this.stat\
us=0;this.random\
=0.13412};(funct\
ion(a,b){b._chec\
kLoad=m._checkLo\
ad;b.updateNodeF\
orFunctionDecora\
tion=function(a)\
{(a=I(a))&&a.sta\
tus==x.STATUS_KN\
OWN&&window.setT\
imeout(function(\
a){return functi\
on(){updateNode(\
a)}}(a),\x0a1)};x.p\
rototype.toStrin\
g=function(){ret\
urn this.name||t\
his.path||\x22Clazz\
Node\x22};x.STATUS_\
UNKNOWN=0;x.STAT\
US_KNOWN=1;x.STA\
TUS_CONTENT_LOAD\
ED=2;x.STATUS_MU\
STS_LOADED=3;x.S\
TATUS_DECLARED=4\
;x.STATUS_LOAD_C\
OMPLETE=5;var c=\
[];b.requireLoad\
erByBase=functio\
n(a){for(var d=0\
;d<c.length;d++)\
if(c[d].base==a)\
return c[d];d=ne\
w b;d.base=a;c.p\
ush(d);return d}\
;var d=new x,e={\
},h=0,k=6,l=navi\
gator.userAgent.\
toLowerCase(),q=\
-1!=l.indexOf(\x22o\
pera\x22),s=-1!=l.i\
ndexOf(\x22msie\x22)&&\
!q,g=-1!=l.index\
Of(\x22gecko\x22);if(q\
&&(k=1,q=l.index\
Of(\x22opera/\x22),\x0a-1\
!=q)){var t=9;tr\
y{t=parseFloat(l\
.subString(q+6))\
}catch(u){}9.6<=\
t&&(k=6)}var C;s\
elf.Clazz&&a.isC\
lassDefined?isCl\
assDefined=a.isC\
lassDefined:(C={\
},isClassDefined\
=function(a){ret\
urn!0==C[a]});va\
r D=function(a){\
if(!a||0==a.leng\
th)return[];for(\
var b=null,c=0;c\
<a.length;c++)if\
(a[c]){if(\x22$\x22==a\
[c].charAt(0))if\
(\x22.\x22==a[c].charA\
t(1)){if(!b)cont\
inue;var d=b.las\
tIndexOf(\x22.\x22);-1\
!=d&&(b=b.substr\
ing(0,d),a[c]=b+\
a[c].substring(1\
))}else a[c]=\x22or\
g.eclipse.s\x22+a[c\
].substring(1);b\
=a[c]}return a},\
F=[],E={},K=0;b.\
loadPackageClass\
path=\x0afunction(a\
,c,d,e,g,h){g||(\
g=0);e||(e=null)\
;h||(h=0);var j=\
d&&E[\x22@\x22+a];if(0\
==g&&(d&&!E[\x22@ja\
va\x22]&&0!=a.index\
Of(\x22java\x22)&&null\
!=window[\x22java.r\
egistered\x22]&&!E[\
\x22@java\x22])&&(b.lo\
adPackage(\x22java\x22\
,e?function(){b.\
loadPackageClass\
path(a,c,d,e,1)}\
:null),e))return\
;if(a instanceof\
 Array)if(D(a),e\
)h<a.length?b.lo\
adPackageClasspa\
th(a[h],c,d,func\
tion(){b.loadPac\
kageClasspath(a,\
c,d,e,1,h+1)},1)\
:e();else for(j=\
0;j<a.length;j++\
)b.loadPackageCl\
asspath(a[j],c,d\
,null);else{swit\
ch(a){case \x22java\
.*\x22:a=\x22java\x22;cas\
e \x22java\x22:c&&\x0a(g=\
\x22@net.sf.j2s.aja\
x\x22,E[g]||(E[g]=c\
),g=\x22@net.sf.j2s\
\x22,E[g]||(E[g]=c)\
);break;case \x22sw\
t\x22:a=\x22org.eclips\
e.swt\x22;break;cas\
e \x22ajax\x22:a=\x22net.\
sf.j2s.ajax\x22;bre\
ak;case \x22j2s\x22:a=\
\x22net.sf.j2s\x22;bre\
ak;default:a.las\
tIndexOf(\x22.*\x22)==\
a.length-2&&(a=a\
.substring(0,a.l\
ength-2))}c&&(E[\
\x22@\x22+a]=c);d&&!j&\
&!window[a+\x22.reg\
istered\x22]?(K++,\x22\
java\x22==a&&(a=\x22co\
re\x22),b.loadClass\
(a+\x22.package\x22,fu\
nction(){0==--K&\
&ba()},!0,!0,1))\
:e&&e()}};a.load\
Class=function(c\
,d,e){self.Class\
||(Class=a,Class\
.forName=a._4Nam\
e,JavaObject=a._\
O);return c&&b.l\
oadClass(c,\x0ad,!0\
,e,1)};b.loadCla\
ss=function(c,g,\
h,k,l){l||(l=0);\
null==k&&(k=!1);\
if(\x22boolean\x22==ty\
peof g)return a.\
evalType(c);null\
!=window[\x22java.r\
egistered\x22]&&!E[\
\x22@java\x22]&&b.load\
Package(\x22java\x22);\
b.keepOnLoading=\
!0;if(!h&&(K&&c.\
lastIndexOf(\x22.pa\
ckage\x22)!=c.lengt\
h-8||0!=c.indexO\
f(\x22java.\x22)&&!isC\
lassDefined(ca))\
)La.push([c,g]),\
System.out.print\
ln(\x22loadclass-qu\
euing\x22+c+ca+\x22 \x22+\
isClassDefined(c\
a));else if((l=i\
sClassDefined(c)\
)||O[\x22@\x22+c]){if(\
l&&g&&(h=I(c),!h\
||h.status>=x.ST\
ATUS_LOAD_COMPLE\
TE))k?window.set\
Timeout(g,25):g(\
)}else{var m=\x0ab.\
getClasspathFor(\
c);l=e[m];if(!l)\
for(k=F.length;0\
<=--k;)if(F[k].p\
ath==m||F[k].nam\
e==c){l=!0;break\
}if(l){if(g&&(l=\
I(c)))if(l.onLoa\
ded){if(g!=l.onL\
oaded){var r=l.o\
nLoaded,q=g;l.on\
Loaded=function(\
){r();q()}}}else\
 l.onLoaded=g}el\
se{l=a.unloadedC\
lasses[c]&&I(c)|\
|new x;l.name=c;\
l.path=m;l.isPac\
kage=m.lastIndex\
Of(\x22package.js\x22)\
==m.length-10;X(\
m,c,l);l.onLoade\
d=g;l.status=x.S\
TATUS_KNOWN;c=!1\
;for(k=F.length;\
0<=--k;)if(F[k].\
status!=x.STATUS\
_LOAD_COMPLETE){\
c=!0;break}if(l.\
isPackage){for(k\
=F.length;0<=--k\
&&!F[k].isPackag\
e;)F[k+\x0a1]=F[k];\
F[++k]=l}else c&\
&F.push(l);if(!c\
){var s=!1;g&&(s\
=ga,ga=!0);h&&(g\
=null);Ja(d,l,!0\
);V(l,l.path,l.r\
equiredBy,!1,g?f\
unction(){ga=s;g\
()}:null)}}}};b.\
loadPackage=func\
tion(a,c){c||(c=\
null);window[a+\x22\
.registered\x22]=!1\
;b.loadPackageCl\
asspath(a,b.J2SL\
ibBase||(b.J2SLi\
bBase=b.getJ2SLi\
bBase()||\x22j2s/\x22)\
,!0,c)};b.jarCla\
sspath=function(\
a,b){b instanceo\
f Array||(b=[b])\
;D(b);for(var c=\
b.length;0<=--c;\
)E[\x22#\x22+b[c]]=a;E\
[\x22$\x22+a]=b};b.reg\
isterPackages=fu\
nction(c,d){for(\
var e=b.getClass\
pathFor(c+\x22.*\x22,!\
0),g=0;g<d.lengt\
h;g++)window.Cla\
zz&&\x0aa.declarePa\
ckage(c+\x22.\x22+d[g]\
),b.loadPackageC\
lasspath(c+\x22.\x22+d\
[g],e)};b.getCla\
sspathFor=functi\
on(c,d,e){var g=\
E[\x22#\x22+c];if(!g||\
d||e){var h,k;if\
(g){if(c=c.repla\
ce(/\x5c./g,\x22/\x22),0<\
=(k=g.lastIndexO\
f(c))||0<=(k=c.l\
astIndexOf(\x22/\x22))\
&&0<=(k=g.lastIn\
dexOf(c.substrin\
g(0,k))))h=g.sub\
string(0,k)}else\
{for(k=c.length+\
2;0<=(k=c.lastIn\
dexOf(\x22.\x22,k-2))&\
&!(h=E[\x22@\x22+c.sub\
string(0,k)]););\
d||(c=c.replace(\
/\x5c./g,\x22/\x22))}null\
==h&&(h=window.C\
lazz&&a.binaryFo\
lders&&a.binaryF\
olders.length?a.\
binaryFolders[0]\
:b.binaryFolders\
&&b.binaryFolder\
s.length?\x0ab.bina\
ryFolders[0]:\x22j2\
s\x22);g=(h.lastInd\
exOf(\x22/\x22)==h.len\
gth-1?h:h+\x22/\x22)+(\
d?\x22\x22:c.lastIndex\
Of(\x22/*\x22)==c.leng\
th-2?c.substring\
(0,k+1):c+(!e?\x22.\
js\x22:\x22.\x22!=e.charA\
t(0)?\x22.\x22+e:e))}r\
eturn g};b.ignor\
e=function(){var\
 a=1==arguments.\
length&&argument\
s[0]instanceof A\
rray?a=arguments\
[0]:null,b=a?a.l\
ength:arguments.\
length;if(!a)for\
(var a=Array(b),\
c=0;c<b;c++)a[c]\
=arguments[c];D(\
a);for(c=0;c<b;c\
++)O[\x22@\x22+a[c]]=1\
};b.onScriptLoad\
ing=function(){}\
;b.onScriptLoade\
d=function(){};b\
.onScriptInitial\
ized=function(){\
};b.onScriptComp\
leted=\x0afunction(\
){};b.onClassUnl\
oaded=function()\
{};b.onGlobalLoa\
ded=function(){}\
;b.keepOnLoading\
=!0;var L={},O={\
},U=function(c,d\
,e,g){if(!g)try{\
eval(e+\x22;//# sou\
rceURL=\x22+c)}catc\
h(h){if(a._isQui\
et)return;c=\x22[Ja\
va2Script] The r\
equired class fi\
le \x5cn\x5cn\x22+c+(0==e\
.indexOf(\x22[Excep\
tion\x22)&&e.indexO\
f(\x22data: no\x22)?\x22\x5c\
nwas not found.\x5c\
n\x22:\x22\x5cncould not \
be loaded. Scrip\
t error: \x22+h.mes\
sage+\x22 \x5cn\x5cndata:\
\x5cn\x5cn\x22+e)+\x22\x5cn\x5cn\x22+\
a.getStackTrace(\
);alert(c);a.ale\
rt(c);throw h;}b\
.onScriptLoaded(\
c,!1);sa(d)},aa=\
function(a){retu\
rn function(){if\
(\x22interactive\x22!=\
\x0aa.readyState){t\
ry{a.parentNode&\
&a.parentNode.re\
moveChild(a)}cat\
ch(b){}a=null}}}\
,Z=function(a){w\
indow[\x22j2s.scrip\
t.debugging\x22]||w\
indow.setTimeout\
(aa(a),1)};a._4N\
ame=function(c,d\
,e){if(a.isClass\
Defined(c))retur\
n a.evalType(c);\
d=m._isAsync&&d?\
d._restoreState(\
c,e):null;if(1==\
d)return null;if\
(b.setLoadingMod\
e(d?b.MODE_SCRIP\
T:\x22xhr.sync\x22))re\
turn b.loadClass\
(c,d,!1,!0,1),nu\
ll;b.loadClass(c\
);return a.evalT\
ype(c)};a.curren\
tPath=\x22\x22;var V=f\
unction(c,d,g,k,\
l){a.currentPath\
=d;k&&alert(\x22WHY\
>>\x22);k=e[d];e[d]\
=!0;Ya(F,\x0ad);M=!\
0;ra=!1;b._check\
Load&&System.out\
.println(\x22\x5ct\x22+d+\
(g?\x22\x5cn -- requir\
ed by \x22+g:\x22\x22)+\x22 \
 ajax=\x22+M+\x22 asyn\
c=\x22+ra);g=d;a._d\
ebugging&&(d=d.r\
eplace(/\x5c.z\x5c.js/\
,\x22.js\x22));k||Syst\
em.out.println(\x22\
loadScript \x22+d);\
b.onScriptLoadin\
g(d);if(M&&!ra){\
var r=m._getFile\
Data(d);try{U(d,\
g,r,k)}catch(q){\
alert(q+\x22 loadin\
g file \x22+d+\x22 \x22+c\
.name+\x22 \x22+a.getS\
tackTrace())}l&&\
l()}else c={data\
Type:\x22script\x22,as\
ync:!0,type:\x22GET\
\x22,url:d,success:\
ta(d,!1,l),error\
:ta(d,!0,l)},h++\
,k?setTimeout(c.\
success,0):m.$aj\
ax(c)},ta=functi\
on(c,d,e){a.getS\
tackTrace();\x0aret\
urn function(){g\
&&this.timeoutHa\
ndle&&(window.cl\
earTimeout(this.\
timeoutHandle),t\
his.timeoutHandl\
e=null);0<h&&h--\
;this.onerror=th\
is.onload=null;d\
&&alert(\x22There w\
as a problem loa\
ding \x22+c);b.onSc\
riptLoaded(c,!0)\
;var a=this,j;j=\
e?function(){Z(a\
);sa(c,e)}:funct\
ion(){Z(a);sa(c)\
};0<=W?window.se\
tTimeout(functio\
n(){sa(c,j)},W):\
sa(c,j)}},ga=!0,\
fa=!1,sa=functio\
n(c,g){var l=L[\x22\
@\x22+c];if(l){var \
m,r=E[\x22$\x22+c];if(\
r)for(var q=0;q<\
r.length;q++){va\
r t=r[q];if(t!=l\
.name&&(m=I(t)))\
m.status<x.STATU\
S_CONTENT_LOADED\
&&\x0a(m.status=x.S\
TATUS_CONTENT_LO\
ADED,updateNode(\
m));else{m=new x\
;m.name=t;var u=\
E[\x22#\x22+t];u||(ale\
rt(t+\x22 J2S error\
 in tryToLoadNex\
t\x22),error(\x22Java2\
Script implement\
ation error! Ple\
ase report this \
bug!\x22));m.path=u\
;X(m.path,t,m);m\
.status=x.STATUS\
_CONTENT_LOADED;\
Ja(d,m,!1);updat\
eNode(m)}}if(l i\
nstanceof Array)\
for(q=0;q<l.leng\
th;q++)l[q].stat\
us<x.STATUS_CONT\
ENT_LOADED&&(l[q\
].status=x.STATU\
S_CONTENT_LOADED\
,updateNode(l[q]\
));else if(l.sta\
tus<x.STATUS_CON\
TENT_LOADED){m=!\
1;r=document.get\
ElementsByTagNam\
e(\x22SCRIPT\x22);\x0afor\
(q=0;q<r.length;\
q++)if(s){if(r[q\
].onreadystatech\
ange&&r[q].onrea\
dystatechange.pa\
th==l.path&&\x22int\
eractive\x22==r[q].\
readyState){m=!0\
;break}}else if(\
r[q].onload&&r[q\
].onload.path==l\
.path){m=!0;brea\
k}m||(l.status=x\
.STATUS_CONTENT_\
LOADED,updateNod\
e(l))}if(b.keepO\
nLoading){q=!0;i\
f(m=Ka(x.STATUS_\
KNOWN))for(S(m);\
h<k&&(m=Ka(x.STA\
TUS_KNOWN));)S(m\
);else if(0!=F.l\
ength)m=F.shift(\
),!e[m.path]||0!\
=F.length||!ga||\
m.musts.length||\
m.optionals.leng\
th?(Ja(d,m,!0),V\
(m,m.path,m.requ\
iredBy,!1)):ga&&\
(ga=!1);else if(\
m=\x0aH(x.STATUS_KN\
OWN))for(S(m);h<\
k&&(m=H(x.STATUS\
_KNOWN));)S(m);e\
lse q=!1;if(!(q|\
|0<h)){l=[Ka,H];\
r=null;for(q=0;2\
>q;q++)for(;m=l[\
q](x.STATUS_CONT\
ENT_LOADED);)1==\
q&&r===m&&(m.sta\
tus=x.STATUS_LOA\
D_COMPLETE),upda\
teNode(m),r=m;fo\
r(;!(la=[],!ma(d\
,c)););for(q=0;2\
>q;q++)for(r=nul\
l;(m=l[q](x.STAT\
US_DECLARED))&&r\
!==m;)updateNode\
(r=m);r=[];for(q\
=0;2>q;q++)for(;\
m=l[q](x.STATUS_\
DECLARED);)r.pus\
h(m),m.status=x.\
STATUS_LOAD_COMP\
LETE;if(r.length\
){for(q=0;q<r.le\
ngth;q++)Da(r[q]\
);for(q=0;q<r.le\
ngth;q++)if(l=r[\
q].onLoaded)r[q]\
.onLoaded=\x0anull,\
l()}if(g)g();els\
e if(b._classCou\
ntPending)for(t \
in b._classPendi\
ng){if(m=I(t),Sy\
stem.out.println\
(\x22class left pen\
ding \x22+t+\x22 \x22+m),\
m){updateNode(m)\
;break}}else b._\
checkLoad&&(Syst\
em.out.println(\x22\
I think I'm done\
: SAEM call coun\
t: \x22+P),a.showDu\
plicates(!0));b.\
onGlobalLoaded()\
}}}},la=[],ma=fu\
nction(a,c){var \
d=la,e=d.length;\
d.push(a);for(va\
r g=e;0<=--g&&!(\
d[g]===a&&d[g].s\
tatus>=x.STATUS_\
DECLARED););if(0\
<=g){if(b._check\
Load){var h;Syst\
em.out.println(\x22\
cycle found load\
ing \x22+c+\x22 for \x22+\
a)}for(;g<e;g++)\
{var j=\x0ad[g];j.s\
tatus=x.STATUS_L\
OAD_COMPLETE;Da(\
j);for(h=0;h<j.p\
arents.length;h+\
+)updateNode(j.p\
arents[h]);j.par\
ents=[];var k=j.\
onLoaded;b._chec\
kLoad&&(h=\x22cycle\
 setting status \
to LOAD_COMPLETE\
 for \x22+j.name+(k\
?\x22 firing \x22+k.to\
String():\x22\x22),Sys\
tem.out.println(\
h));k&&(j.onLoad\
ed=null,k())}d.l\
ength=0;return!0\
}j=[a.musts,a.op\
tionals];for(h=0\
;2>h;h++){k=j[h]\
;for(g=k.length;\
0<=--g;)if(k[g].\
status==x.STATUS\
_DECLARED&&ma(k[\
g],c))return!0}d\
.length=e;return\
!1};b._classCoun\
tPending=0;b._cl\
assCountOK=0;b._\
classPending=\x0a{}\
;b.showPending=f\
unction(){var a=\
[],c;for(c in b.\
_classPending){v\
ar d=I(c);d?(a.p\
ush(d),System.ou\
t.println(va(\x22\x22,\
\x22\x22,d,\x22\x22,0))):ale\
rt(\x22No node for \
\x22+c)}return a};v\
ar va=function(a\
,b,c,d,e){b+=\x22--\
\x22+c.name;a+=b+\x22\x5c\
n\x22;if(5<e)return\
 a+(d+\x22 ...\x5cn\x22);\
d+=\x22\x5ct\x22;a+=d+\x22st\
atus: \x22+c.status\
+\x22\x5cn\x22;if(c.paren\
ts&&c.parents.le\
ngth&&c.parents[\
0]&&c.parents[0]\
.name){a+=d+\x22par\
ents: \x22+c.parent\
s.length+\x22\x5cn\x22;fo\
r(var g=0;g<c.pa\
rents.length;g++\
)a=va(a,b,c.pare\
nts[g],d+\x22\x5ct\x22,e+\
1);a+=\x22\x5cn\x22}retur\
n a};updateNode=\
function(a){if(!\
a.name||\x0aa.statu\
s>=x.STATUS_LOAD\
_COMPLETE)Da(a);\
else{var c=!0;if\
(a.musts.length&\
&a.declaration)f\
or(var d=a.musts\
.length,e=d;0<=-\
-e;){var g=a.mus\
ts[e];g.required\
By=a;if(g.status\
<x.STATUS_DECLAR\
ED&&isClassDefin\
ed(g.name)){var \
h=[];g.status=x.\
STATUS_LOAD_COMP\
LETE;Da(g);if(g.\
declaration&&g.d\
eclaration.clazz\
List){for(var j=\
0,k=g.declaratio\
n.clazzList,l=k.\
length;j<l;j++){\
var m=I(k[j]);m&\
&(m.status!=x.ST\
ATUS_LOAD_COMPLE\
TE&&m!==g)&&(m.s\
tatus=g.status,m\
.declaration=nul\
l,Da(m),m.onLoad\
ed&&h.push(m))}g\
.declaration=nul\
l}g.onLoaded&&\x0ah\
.push(g);for(j=0\
;j<h.length;j++)\
if(k=h[j].onLoad\
ed)h[j].onLoaded\
=null,k()}else g\
.status==x.STATU\
S_CONTENT_LOADED\
&&updateNode(g),\
g.status<x.STATU\
S_DECLARED&&(c=!\
1);a.musts.lengt\
h!=d&&(e=d=a.mus\
ts.length,c=!0)}\
if(c){if(a.statu\
s<x.STATUS_DECLA\
RED){if(e=a.decl\
aration)e(),e.ex\
ecuted=!0;b._che\
ckLoad&&b._class\
Pending[a.name]&\
&(delete b._clas\
sPending[a.name]\
,b._classCountOK\
,b._classCountPe\
nding--);a.statu\
s=x.STATUS_DECLA\
RED;C&&(C[a.name\
]=!0);b.onScript\
Initialized(a.pa\
th);if(a.declara\
tion&&a.declarat\
ion.clazzList){j\
=\x0a0;k=a.declarat\
ion.clazzList;fo\
r(l=k.length;j<l\
;j++)if((m=I(k[j\
]))&&m.status!=x\
.STATUS_DECLARED\
&&m!==a)m.status\
=x.STATUS_DECLAR\
ED,C&&(C[m.name]\
=!0),b.onScriptI\
nitialized(m.pat\
h)}}c=x.STATUS_D\
ECLARED;if(0==a.\
optionals.length\
&&0==a.musts.len\
gth||a.status>x.\
STATUS_KNOWN&&!a\
.declaration||Ta\
(a.musts,x.STATU\
S_LOAD_COMPLETE)\
&&Ta(a.optionals\
,x.STATUS_LOAD_C\
OMPLETE)){c=x.ST\
ATUS_LOAD_COMPLE\
TE;if(!wa(a,c))r\
eturn!1;if(a.dec\
laration&&a.decl\
aration.clazzLis\
t){j=0;k=a.decla\
ration.clazzList\
;for(l=k.length;\
j<l;j++)if((m=\x0aI\
(k[j]))&&m.statu\
s!=c&&m!==a)if(m\
.declaration=nul\
l,!wa(m,c))retur\
n!1}}if(a.parent\
s&&a.parents.len\
gth){for(e=0;e<a\
.parents.length;\
e++)j=a.parents[\
e],j.status<c&&u\
pdateNode(j,j.na\
me);c==x.STATUS_\
LOAD_COMPLETE&&(\
a.parents=[])}}}\
};var Ta=functio\
n(a,b){for(var c\
=a.length;0<=--c\
;)if(a[c].status\
<b)return!1;retu\
rn!0},wa=functio\
n(a,c){a.status=\
c;b.onScriptComp\
leted(a.path);va\
r d=a.onLoaded;i\
f(d&&(a.onLoaded\
=null,d(),!b.kee\
pOnLoading))retu\
rn!1;Da(a);retur\
n!0},ya={\x22r0.134\
12\x22:1},Ba=functi\
on(){for(;;){var\
 a=Math.random()\
,\x0ab=\x22r\x22+a;if(!ya\
[b])return ya[b]\
=1,d.random=a}},\
I=function(a){Ba\
();return Ea(a,d\
)},H=function(a)\
{Ba();return Ca(\
d,a)},Ka=functio\
n(a){return qa(d\
,a)},Ea=function\
(a,b){var c;retu\
rn b.name==a?b:(\
c=$a(a,b.musts))\
||(c=$a(a,b.opti\
onals))?c:null},\
$a=function(a,b)\
{for(var c=d.ran\
dom,e=b.length;0\
<=--e;){var g=b[\
e];if(g.name==a|\
|g.random!=c&&(g\
.random=c,g=Ea(a\
,g)))return g}re\
turn null},Aa=fu\
nction(a,b){retu\
rn a.status==b&&\
(b!=x.STATUS_KNO\
WN||!e[a.path])&\
&(b==x.STATUS_DE\
CLARED||!isClass\
Defined(a.name))\
},qa=function(a,\
\x0ab){for(var c=a.\
musts.length;0<=\
--c;){var d=a.mu\
sts[c];if(Aa(d,b\
)||(d=qa(d,b)))r\
eturn d}return A\
a(a,b)?a:null},C\
a=function(a,b){\
var c;return(c=n\
a(a.musts,b))||(\
c=na(a.optionals\
,b))||Aa(c=a,b)?\
c:null},na=funct\
ion(a,b){if(a)fo\
r(var c=d.random\
,e=0;e<a.length;\
e++){var g=a[e];\
if(Aa(g,b)||g.ra\
ndom!=c&&(g.rand\
om=c,g=Ca(g,b)))\
return g}return \
null},R=function\
(a,c,e,g){if(c i\
nstanceof Array)\
{D(c);for(var h=\
0;h<c.length;h++\
)R(a,c[h],e,g,c)\
}else{b._checkLo\
ad&&!b._classPen\
ding[c]&&(b._cla\
ssPending[c]=1,0\
==b._classCountP\
ending++&&\x0a(b._c\
lassCountOK=0),S\
ystem.out.printl\
n(\x22Loading class\
 \x22+c));h=L[\x22#\x22+c\
];h||(h=(h=I(c))\
?h:new x,h.name=\
c,h.path=E[\x22#\x22+c\
]||\x22unknown\x22,X(h\
.path,c,h),h.sta\
tus=x.STATUS_KNO\
WN,Ja(d,h,!1));i\
a(h,a,!0);5==arg\
uments.length&&g\
&&(g.status=h.st\
atus,g.clazzList\
=arguments[4]);i\
f(h.declaration=\
g)h.status=x.STA\
TUS_CONTENT_LOAD\
ED;ia(h,e,!1)}},\
ia=function(a,b,\
c){if(b&&b.lengt\
h){D(b);for(var \
d=0;d<b.length;d\
++){var e=b[d];i\
f(e&&!isClassDef\
ined(e)&&!O[\x22@\x22+\
e]){var g=I(e);g\
||(g=new x,g.nam\
e=e,g.status=x.S\
TATUS_KNOWN);g.r\
equiredBy=\x0aa;Ja(\
a,g,c)}}}};windo\
w.Clazz?a.load=R\
:b.load=R;var X=\
function(a,b,c){\
var d=\x22@\x22+a;if(a\
=L[d])if(a insta\
nceof Array){for\
(var d=!1,e=0;e<\
a.length;e++)if(\
a[e].name==b){d=\
!0;break}d||a.pu\
sh(c)}else L[d]=\
[a,c];else L[d]=\
c;L[\x22#\x22+b]=c},S=\
function(a){var \
c=a.name;if(!isC\
lassDefined(c)&&\
!O[\x22@\x22+c]){var d\
=b.getClasspathF\
or(c);a.path=d;X\
(d,c,a);if(!e[d]\
)return V(a,d,a.\
requiredBy,!1),!\
0}return!1},ca=b\
.runtimeKeyClass\
=\x22java.lang.Stri\
ng\x22,La=[];b.getJ\
2SLibBase=functi\
on(){var a=windo\
w[\x22j2s.lib\x22];ret\
urn a?a.base+(\x22.\
\x22==\x0aa.alias?\x22\x22:(\
a.alias?a.alias:\
a.version?a.vers\
ion:\x221.0.0\x22)+\x22/\x22\
):null};var ra=!\
0,M=!1,W=-1;b.MO\
DE_SCRIPT=4;b.MO\
DE_XHR=2;b.MODE_\
SYNC=1;b.setLoad\
ingMode=function\
(a,c){var d=!0,e\
=!0;\x22string\x22==ty\
peof a?(a=a.toLo\
werCase(),0<=a.i\
ndexOf(\x22script\x22)\
?e=!1:a.indexOf(\
\x22async\x22),d=!1):a\
&b.MODE_SCRIPT?e\
=!1:d=!(a&b.MODE\
_SYNC);M=e;W=(ra\
=d)&&0<=c?c:-1;r\
eturn d};var ba=\
function(){if(!K\
&&isClassDefined\
(ca)){for(var a=\
La,c=0;c<a.lengt\
h;c++)b.loadClas\
s(a[c][0],a[c][1\
]);La=[]}};b.loa\
dZJar=function(a\
,c){var d=null,e\
=c instanceof\x0aAr\
ray;e?c=c[c.leng\
th-1]:d=c==ca?ba\
:null;b.jarClass\
path(a,e?c:[c]);\
b.loadClass(c,d,\
!0)};var Fa={},P\
a=[],Ja=function\
(a,b,c){var e=!1\
;c?(c=a.musts,b.\
requiredBy||(b.r\
equiredBy=a)):c=\
a.optionals;Fa[b\
.name]||(Pa.push\
(b),Fa[b.name]=b\
);for(var g=0;g<\
c.length;g++)if(\
c[g].name==b.nam\
e){e=!0;break}e|\
|(c.push(b),ga&&\
(0!=b.name.index\
Of(\x22java\x22)&&0!=b\
.name.indexOf(\x22n\
et.sf.j2s.ajax\x22)\
)&&(fa&&(ga=!1),\
fa=!0));a:{if(a.\
name&&a!=d&&a!=b\
)for(e=0;e<b.par\
ents.length;e++)\
if(b.parents[e].\
name==a.name)bre\
ak a;b.parents.p\
ush(a)}},\x0aDa=fun\
ction(a){var b=a\
.parents;if(b)fo\
r(var c=b.length\
;0<=--c;)Ya(b[c]\
.musts,a)||Ya(b[\
c].optionals,a)}\
;a.binaryFolders\
=b.binaryFolders\
=[b.getJ2SLibBas\
e()]})(a,a._Load\
er);a._LoaderPro\
gressMonitor={};\
var Z=a._LoaderP\
rogressMonitor,L\
=null,fa=0,O=nul\
l,wa=0;Z.DEFAULT\
_OPACITY=m&&m._j\
2sLoadMonitorOpa\
city?m._j2sLoadM\
onitorOpacity:55\
;Z.hideMonitor=f\
unction(){O.styl\
e.display=\x22none\x22\
};Z.showStatus=f\
unction(a,b){if(\
!O){var c=docume\
nt.createElement\
(\x22DIV\x22);c.id=\x22_L\
oader-status\x22;c.\
style.cssText=\x22p\
osition:absolute\
;bottom:4px;left\
:4px;padding:2px\
 8px;z-index:\x22+\x0a\
(window[\x22j2s.lib\
\x22].monitorZIndex\
||1E4)+\x22;backgro\
und-color:#8e000\
0;color:yellow;f\
ont-family:Arial\
, sans-serif;fon\
t-size:10pt;whit\
e-space:nowrap;\x22\
;c.onmouseover=u\
b;O=c;document.b\
ody.appendChild(\
c);ya||(ya=!0)}j\
b(O);if(null==a)\
b?ma():Z.hideMon\
itor();else{O.ap\
pendChild(docume\
nt.createTextNod\
e(\x22\x22+a));\x22none\x22=\
=O.style.display\
&&(O.style.displ\
ay=\x22\x22);kb(Z.DEFA\
ULT_OPACITY);var\
 d,c=navigator.u\
serAgent;d=docum\
ent.body;var e=d\
.parentNode,h=e.\
clientHeight;d=d\
.scrollTop+d.off\
setTop;var k=e.s\
crollTop+e.offse\
tTop,\x0ac=0>c.inde\
xOf(\x22Opera\x22)&&do\
cument.all?0==h?\
d:k:0>c.indexOf(\
\x22Gecko\x22)?h==e.of\
fsetHeight&&h==e\
.scrollHeight?d:\
k:d;wa!=c&&(wa=c\
,O.style.bottom=\
wa+4+\x22px\x22);b&&ma\
()}};var jb=func\
tion(a){if(a)for\
(var b=a.childNo\
des.length;0<=--\
b;){var c=a.chil\
dNodes[b];if(c){\
c.childNodes&&c.\
childNodes.lengt\
h&&jb(c);try{a.r\
emoveChild(c)}ca\
tch(d){}}}},kb=f\
unction(a){L&&a=\
=Z.DEFAULT_OPACI\
TY&&(window.clea\
rTimeout(L),L=nu\
ll);fa=a;navigat\
or.userAgent.toL\
owerCase();O.sty\
le.filter=\x22Alpha\
(Opacity=\x22+a+\x22)\x22\
;O.style.opacity\
=a/100},ub=\x0afunc\
tion(){Z.hideMon\
itor()},ya=!1,ma\
=function(){\x22non\
e\x22!=O.style.disp\
lay&&(fa==Z.DEFA\
ULT_OPACITY?(L=w\
indow.setTimeout\
(function(){ma()\
},750),fa-=5):0<\
=fa-10?(kb(fa-10\
),L=window.setTi\
meout(function()\
{ma()},40)):O.st\
yle.display=\x22non\
e\x22)},D=a.Console\
,aa=System;D.max\
TotalLines=1E4;D\
.setMaxTotalLine\
s=function(a){D.\
maxTotalLines=0<\
a?a:999999};D.ma\
xLatency=40;D.se\
tMaxLatency=func\
tion(a){D.maxLat\
ency=0<a?a:40};D\
.pinning=!1;D.en\
ablePinning=func\
tion(a){D.pinnin\
g=a};D.linesCoun\
t=0;D.metLineBre\
ak=!1;D.createCo\
nsoleWindow=\x0afun\
ction(){var a=do\
cument.createEle\
ment(\x22DIV\x22);a.st\
yle.cssText=\x22fon\
t-family:monospa\
ce, Arial, sans-\
serif;\x22;document\
.body.appendChil\
d(a);return a};v\
ar V=String.from\
CharCode(160),V=\
V+(V+V+V);D.cons\
oleOutput=functi\
on(a,b){var c=wi\
ndow[\x22j2s.lib\x22];\
(c=c&&c.console)\
&&\x22string\x22==type\
of c&&(c=documen\
t.getElementById\
(c));if(!c)retur\
n!1;if(D.linesCo\
unt>D.maxTotalLi\
nes){for(var d=0\
;d<D.linesCount-\
D.maxTotalLines;\
d++)c&&0<c.child\
Nodes.length&&c.\
removeChild(c.ch\
ildNodes[0]);D.l\
inesCount=D.maxT\
otalLines}var e=\
!1;\x0aa=(\x22undefine\
d\x22==typeof a?\x22\x22:\
null==a?\x22null\x22:\x22\
\x22+a).replace(/\x5ct\
/g,V);if(0<a.len\
gth)switch(a.cha\
rAt(a.length-1))\
{case \x22\x5cn\x22:case \
\x22\x5cr\x22:a=1<a.lengt\
h?a.substring(0,\
a.length-(\x22\x5cr\x22==\
a.charAt(a.lengt\
h-2)?2:1)):\x22\x22,e=\
!0}var h=null;a=\
a.replace(/\x5ct/g,\
V);for(var h=a.s\
plit(/\x5cr\x5cn|\x5cr|\x5cn\
/g),d=0,k=h.leng\
th-1;d<=k;d++){v\
ar l=null;if(D.m\
etLineBreak||0==\
D.linesCount||1>\
c.childNodes.len\
gth)l=document.c\
reateElement(\x22DI\
V\x22),c.appendChil\
d(l),l.style.whi\
teSpace=\x22nowrap\x22\
,D.linesCount++;\
else try{l=c.chi\
ldNodes[c.childN\
odes.length-\x0a1]}\
catch(m){l=docum\
ent.createElemen\
t(\x22DIV\x22),c.appen\
dChild(l),l.styl\
e.whiteSpace=\x22no\
wrap\x22,D.linesCou\
nt++}var q=docum\
ent.createElemen\
t(\x22SPAN\x22);l.appe\
ndChild(q);q.sty\
le.whiteSpace=\x22n\
owrap\x22;b&&(q.sty\
le.color=b);l=h[\
d];0==l.length&&\
(l=V);q.appendCh\
ild(document.cre\
ateTextNode(l));\
D.pinning||(c.sc\
rollTop+=100);D.\
metLineBreak=d!=\
k||e}d=c.parentN\
ode.className;!D\
.pinning&&(d&&-1\
!=d.indexOf(\x22com\
posite\x22))&&(c.pa\
rentNode.scrollT\
op=c.parentNode.\
scrollHeight);D.\
lastOutputTime=(\
new Date).getTim\
e()};D.clear=fun\
ction(){try{D.me\
tLineBreak=\x0a!0;v\
ar a=window[\x22j2s\
.lib\x22],b=a&&a.co\
nsole;if(b&&(b=d\
ocument.getEleme\
ntById(b))){for(\
var c=b.childNod\
es,d=c.length;0<\
=--d;)b.removeCh\
ild(c[d]);D.line\
sCount=0}}catch(\
e){}};a.alert=fu\
nction(a){D.cons\
oleOutput(a+\x22\x5cr\x5c\
n\x22)};aa.out.prin\
t=function(a){D.\
consoleOutput(a)\
};aa.out.println\
=function(a){D.c\
onsoleOutput(\x22un\
defined\x22==typeof\
 a?\x22\x5cr\x5cn\x22:null==\
a?\x22null\x5cr\x5cn\x22:a+\x22\
\x5cr\x5cn\x22)};aa.out.w\
rite=function(a,\
b,c){aa.out.prin\
t(String.instant\
ialize(a).substr\
ing(b,b+c))};aa.\
err.__CLASS_NAME\
__=\x22java.io.Prin\
tStream\x22;aa.err.\
print=\x0afunction(\
a){D.consoleOutp\
ut(a,\x22red\x22)};aa.\
err.println=func\
tion(a){D.consol\
eOutput(\x22undefin\
ed\x22==typeof a?\x22\x5c\
r\x5cn\x22:null==a?\x22nu\
ll\x5cr\x5cn\x22:a+\x22\x5cr\x5cn\x22\
,\x22red\x22)};aa.err.\
write=function(a\
,b,c){aa.err.pri\
nt(String.instan\
tialize(a).subst\
ring(b,b+c))}}(C\
lazz,Jmol))};Jmo\
l.___JmolDate=\x22$\
Date: 2016-06-27\
 01:32:19 -0400 \
(Mon, 27 Jun 201\
6) $\x22;Jmol.___fu\
llJmolProperties\
=\x22src/org/jmol/v\
iewer/Jmol.prope\
rties\x22;Jmol.___J\
molVersion=\x2214.7\
.0_2016.06.27\x22;\x0a\
\
\x00\x00\xde\x13\
(\
function(a){func\
tion h(a){try{re\
turn a?new windo\
w.ActiveXObject(\
\x22Microsoft.XMLHT\
TP\x22):new window.\
XMLHttpRequest}c\
atch(d){}}a.ajax\
Settings.xhr=voi\
d 0===window.Act\
iveXObject?h:fun\
ction(){return(t\
his.url==documen\
t.location||0==t\
his.url.indexOf(\
\x22http\x22)||!this.i\
sLocal)&&/^(get|\
post|head|put|de\
lete|options)$/i\
.test(this.type)\
&&h()||h(1)};a.a\
jaxTransport(\x22+s\
cript\x22,function(\
a){var d,g=docum\
ent.head||jQuery\
(\x22head\x22)[0]||doc\
ument.documentEl\
ement;return{sen\
d:function(m,h){\
d=document.creat\
eElement(\x22script\
\x22);a.scriptChars\
et&&\x0a(d.charset=\
a.scriptCharset)\
;d.src=a.url;d.o\
nload=d.onreadys\
tatechange=funct\
ion(a,e){if(e||!\
d.readyState||/l\
oaded|complete/.\
test(d.readyStat\
e))d.onload=d.on\
readystatechange\
=null,d.parentNo\
de&&d.parentNode\
.removeChild(d),\
d=null,e||h(200,\
\x22success\x22)};g.in\
sertBefore(d,g.f\
irstChild)},abor\
t:function(){if(\
d)d.onload(void \
0,!0)}}});a.exte\
nd(a.support,{ie\
cors:!!window.XD\
omainRequest});a\
.support.iecors?\
a.ajaxTransport(\
function(a){retu\
rn{send:function\
(d,g){var m=new \
window.XDomainRe\
quest;m.onload=f\
unction(){g(200,\
\x0a\x22OK\x22,{text:m.re\
sponseText},{\x22Co\
ntent-Type\x22:m.co\
ntentType})};a.x\
hrFields&&(m.one\
rror=a.xhrFields\
.error,m.ontimeo\
ut=a.xhrFields.t\
imeout);m.open(a\
.type,a.url);m.s\
end(a.hasContent\
&&a.data||null)}\
,abort:function(\
){xdr.abort()}}}\
):(a.ajaxSetup({\
accepts:{binary:\
\x22text/plain; cha\
rset=x-user-defi\
ned\x22},responseFi\
elds:{binary:\x22re\
sponse\x22}}),a.aja\
xTransport(\x22bina\
ry\x22,function(a){\
var d;return{sen\
d:function(g,m){\
var h=a.xhr();co\
nsole.log(\x22xhr.o\
pen binary async\
=\x22+a.async+\x22 url\
=\x22+a.url);h.open\
(a.type,a.url,a.\
async);\x0avar k=!1\
;try{h.hasOwnPro\
perty(\x22responseT\
ype\x22)&&(h.respon\
seType=\x22arraybuf\
fer\x22,k=!0)}catch\
(l){}try{!k&&h.o\
verrideMimeType&\
&h.overrideMimeT\
ype(\x22text/plain;\
 charset=x-user-\
defined\x22)}catch(\
b){}!a.crossDoma\
in&&!g[\x22X-Reques\
ted-With\x22]&&(g[\x22\
X-Requested-With\
\x22]=\x22XMLHttpReque\
st\x22);try{for(var\
 f in g)h.setReq\
uestHeader(f,g[f\
])}catch(c){}h.s\
end(a.hasContent\
&&a.data||null);\
d=function(){var\
 b=h.status,f=\x22\x22\
,c=h.getAllRespo\
nseHeaders(),g={\
};try{if(d&&4===\
h.readyState){d=\
void 0;try{g.tex\
t=\x22string\x22===typ\
eof h.responseTe\
xt?\x0ah.responseTe\
xt:null}catch(k)\
{}try{g.binary=h\
.response}catch(\
l){}try{f=h.stat\
usText}catch(t){\
f=\x22\x22}!b&&a.isLoc\
al&&!a.crossDoma\
in?b=g.text?200:\
404:1223===b&&(b\
=204);m(b,f,g,c)\
}}catch(s){alert\
(s),m(-1,s)}};a.\
async?4===h.read\
yState?setTimeou\
t(d):h.onreadyst\
atechange=d:d()}\
,abort:function(\
){}}}))})(jQuery\
);\x0a(function(a,h\
,e,d){function g\
(e,g){function k\
(b){a(l).each(fu\
nction(){self.Jm\
ol&&(0<=g.indexO\
f(\x22mouseup\x22)||0<\
=g.indexOf(\x22touc\
hend\x22))&&Jmol._s\
etMouseOwner(nul\
l);var c=a(this)\
;this!==b.target\
&&!c.has(b.targe\
t).length&&c.tri\
ggerHandler(g,[b\
.target,b])})}g=\
g||e+d;var l=a()\
,b=e+\x22.\x22+g+\x22-spe\
cial-event\x22;a.ev\
ent.special[g]={\
setup:function()\
{l=l.add(this);1\
===l.length&&a(h\
).bind(b,k)},tea\
rdown:function()\
{self.Jmol&&Jmol\
._setMouseOwner(\
null);l=l.not(th\
is);0===l.length\
&&a(h).unbind(b)\
},add:function(b\
){var a=\x0ab.handl\
er;b.handler=fun\
ction(b,f){b.tar\
get=f;a.apply(th\
is,arguments)}}}\
}a.map(e.split(\x22\
 \x22),function(a){\
g(a)});g(\x22focusi\
n\x22,\x22focus\x22+d);g(\
\x22focusout\x22,\x22blur\
\x22+d)})(jQuery,do\
cument,\x22click mo\
usemove mouseup \
touchmove touche\
nd\x22,\x22outjsmol\x22);\
\x22undefined\x22==typ\
eof jQuery&&aler\
t(\x22Note -- JSmol\
jQuery is requir\
ed for JSmol, bu\
t it's not defin\
ed.\x22);self.Jmol|\
|(Jmol={});\x0aJmol\
._version||(Jmol\
=function(a){var\
 h=function(a){r\
eturn{rear:a++,h\
eader:a++,main:a\
++,image:a++,fro\
nt:a++,fileOpene\
r:a++,coverImage\
:a++,dialog:a++,\
menu:a+9E4,conso\
le:a+91E3,consol\
eImage:a+91001,m\
onitorZIndex:a+9\
9999}},h={_versi\
on:\x22$Date: 2016-\
05-08 13:20:27 -\
0500 (Sun, 08 Ma\
y 2016) $\x22,_aler\
tNoBinary:!0,_al\
lowedJmolSize:[2\
5,2048,300],_app\
letCssClass:\x22\x22,_\
appletCssText:\x22\x22\
,_fileCache:null\
,_jarFile:null,_\
j2sPath:null,_us\
e:null,_j2sLoadM\
onitorOpacity:90\
,_applets:{},_as\
ynchronous:!0,_a\
jaxQueue:[],_per\
sistentMenu:!1,\x0a\
_getZOrders:h,_z\
:h(Jmol.z||9E3),\
_debugCode:!0,db\
:{_databasePrefi\
xes:\x22$=:\x22,_fileL\
oadScript:\x22;if (\
_loadScript = ''\
 && defaultLoadS\
cript == '' && _\
filetype == 'Pdb\
') { select prot\
ein or nucleic;c\
artoons Only;col\
or structure; se\
lect * };\x22,_nciL\
oadScript:\x22;n = \
({molecule=1}.le\
ngth < {molecule\
=2}.length ? 2 :\
 1); select mole\
cule=n;display s\
elected;center s\
elected;\x22,_pubCh\
emLoadScript:\x22\x22,\
_DirectDatabaseC\
alls:{\x22cactus.nc\
i.nih.gov\x22:null,\
\x22.x3dna.org\x22:nul\
l,\x22rruff.geo.ari\
zona.edu\x22:null,\x22\
.rcsb.org\x22:null,\
\x22ftp.wwpdb.org\x22:\
null,\x0a\x22pdbe.org\x22\
:null,\x22materials\
project.org\x22:nul\
l,\x22.ebi.ac.uk\x22:n\
ull,\x22pubchem.ncb\
i.nlm.nih.gov\x22:n\
ull,\x22http://www.\
nmrdb.org/tools/\
jmol/predict.php\
\x22:null,$:\x22https:\
//cactus.nci.nih\
.gov/chemical/st\
ructure/%FILENCI\
/file?format=sdf\
&get3d=True\x22,$$:\
\x22https://cactus.\
nci.nih.gov/chem\
ical/structure/%\
FILENCI/file?for\
mat=sdf\x22,\x22=\x22:\x22ht\
tp://files.rcsb.\
org/view/%FILE.p\
db\x22,\x22*\x22:\x22http://\
www.ebi.ac.uk/pd\
be/entry-files/d\
ownload/%FILE.ci\
f\x22,\x22==\x22:\x22http://\
www.rcsb.org/pdb\
/files/ligand/%F\
ILE.cif\x22,\x22:\x22:\x22ht\
tps://pubchem.nc\
bi.nlm.nih.gov/r\
est/pug/compound\
/%FILE/SDF?recor\
d_type=3d\x22},\x0a_re\
stQueryUrl:\x22http\
://www.rcsb.org/\
pdb/rest/search\x22\
,_restQueryXml:\x22\
<orgPdbQuery><qu\
eryType>org.pdb.\
query.simple.Adv\
ancedKeywordQuer\
y</queryType><de\
scription>Text S\
earch</descripti\
on><keywords>QUE\
RY</keywords></o\
rgPdbQuery>\x22,_re\
stReportUrl:\x22htt\
p://www.pdb.org/\
pdb/rest/customR\
eport?pdbids=IDL\
IST&customReport\
Columns=structur\
eId,structureTit\
le\x22},_debugAlert\
:!1,_document:a,\
_isXHTML:!1,_las\
tAppletID:null,_\
mousePageX:null,\
_mouseOwner:null\
,_serverUrl:\x22htt\
p://your.server.\
here/jsmol.php\x22,\
_syncId:(\x22\x22+Math\
.random()).subst\
ring(3),\x0a_touchi\
ng:!1,_XhtmlElem\
ent:null,_XhtmlA\
ppendChild:!1};a\
=a.location.href\
.toLowerCase();h\
._httpProto=0==a\
.indexOf(\x22https\x22\
)?\x22https://\x22:\x22ht\
tp://\x22;h._isFile\
=0==a.indexOf(\x22f\
ile:\x22);h._isFile\
&&$.ajaxSetup({m\
imeType:\x22text/pl\
ain\x22});h._ajaxTe\
stSite=h._httpPr\
oto+\x22google.com\x22\
;a=h._isFile||0=\
=a.indexOf(\x22http\
://localhost\x22)||\
0==a.indexOf(\x22ht\
tp://127.\x22);h._t\
racker=\x22http://\x22\
==h._httpProto&&\
!a&&\x22http://chem\
apps.stolaf.edu/\
jmol/JmolTracker\
.htm?id=UA-45940\
799-1\x22;h._isChro\
me=0<=navigator.\
userAgent.toLowe\
rCase().indexOf(\
\x22chrome\x22);\x0ah._is\
Safari=!h._isChr\
ome&&0<=navigato\
r.userAgent.toLo\
werCase().indexO\
f(\x22safari\x22);h._i\
sMsie=void 0!==w\
indow.ActiveXObj\
ect;h._isEdge=0<\
=navigator.userA\
gent.indexOf(\x22Ed\
ge/\x22);h._useData\
URI=!h._isSafari\
&&!h._isMsie&&!h\
._isEdge;window.\
requestAnimation\
Frame||(window.r\
equestAnimationF\
rame=window.setT\
imeout);for(var \
e in Jmol)h[e]=J\
mol[e];return h}\
(document,Jmol))\
;\x0a(function(a,h)\
{a.__$=h;h(docum\
ent).ready(funct\
ion(){a._documen\
t=null});a.$=fun\
ction(b,a){null=\
=b&&alert(a+argu\
ments.callee.cal\
ler.toString());\
return h(a?\x22#\x22+b\
._id+\x22_\x22+a:b)};a\
._$=function(b){\
return\x22string\x22==\
typeof b?h(\x22#\x22+b\
):b};a.$ajax=fun\
ction(b){a._ajax\
Call=b.url;b.cac\
he=\x22NO\x22!=b.cache\
;b.url=a._fixPro\
tocol(b.url);ret\
urn h.ajax(b)};a\
._fixProtocol=fu\
nction(b){return\
 0==b.indexOf(\x22h\
ttp://www.rcsb.o\
rg/pdb/files/\x22)&\
&0>b.indexOf(\x22/l\
igand/\x22)?\x22http:/\
/files.rcsb.org/\
view/\x22+b.substri\
ng(30).replace(/\
\x5c.gz/,\x22\x22):\x0a0==b.\
indexOf(\x22http://\
\x22)&&(0==b.indexO\
f(\x22http://pubche\
m\x22)||0==b.indexO\
f(\x22http://cactus\
\x22)||0==b.indexOf\
(\x22http://www.mat\
erialsproject\x22))\
?\x22https\x22+b.subst\
ring(4):b};a._ge\
tNCIInfo=functio\
n(b,f){return a.\
_getFileData(\x22ht\
tps://cactus.nci\
.nih.gov/chemica\
l/structure/\x22+b+\
\x22/\x22+(\x22name\x22==f?\x22\
names\x22:f))};a.$a\
ppEvent=function\
(b,f,c,e){b=a.$(\
b,f);b.off(c)&&e\
&&b.on(c,e)};a.$\
resize=function(\
b){return h(wind\
ow).resize(b)};a\
.$after=function\
(b,a){return h(b\
).after(a)};a.$a\
ppend=function(b\
,a){return h(b).\
append(a)};a.$bi\
nd=\x0afunction(b,a\
,c){return c?h(b\
).bind(a,c):h(b)\
.unbind(a)};a.$c\
losest=function(\
b,a){return h(b)\
.closest(a)};a.$\
get=function(b,a\
){return h(b).ge\
t(a)};a.$documen\
tOff=function(b,\
a){return h(docu\
ment).off(b,\x22#\x22+\
a)};a.$documentO\
n=function(b,a,c\
){return h(docum\
ent).on(b,\x22#\x22+a,\
c)};a.$getAncest\
orDiv=function(b\
,a){return h(\x22di\
v.\x22+a+\x22:has(#\x22+b\
+\x22)\x22)[0]};a.$sup\
portsIECrossDoma\
inScripting=func\
tion(){return h.\
support.iecors};\
a.$attr=function\
(b,f,c){return a\
._$(b).attr(f,c)\
};a.$css=functio\
n(b,f){return a.\
_$(b).css(f)};\x0aa\
.$find=function(\
b,f){return a._$\
(b).find(f)};a.$\
focus=function(b\
){return a._$(b)\
.focus()};a.$htm\
l=function(b,f){\
return a._$(b).h\
tml(f)};a.$offse\
t=function(b){re\
turn a._$(b).off\
set()};a.$window\
On=function(b,a)\
{return h(window\
).on(b,a)};a.$pr\
op=function(b,f,\
c){var e=a._$(b)\
;return 3==argum\
ents.length?e.pr\
op(f,c):e.prop(f\
)};a.$remove=fun\
ction(b){return \
a._$(b).remove()\
};a.$scrollTo=fu\
nction(b,f){var \
c=a._$(b);return\
 c.scrollTop(0>f\
?c[0].scrollHeig\
ht:f)};a.$setEna\
bled=function(b,\
f){return a._$(b\
).attr(\x22disabled\
\x22,\x0af?null:\x22disab\
led\x22)};a.$getSiz\
e=function(b){b=\
a._$(b);return[b\
.width(),b.heigh\
t()]};a.$setSize\
=function(b,f,c)\
{return a._$(b).\
width(f).height(\
c)};a.$is=functi\
on(b,f){return a\
._$(b).is(f)};a.\
$setVisible=func\
tion(b,f){var c=\
a._$(b);return f\
?c.show():c.hide\
()};a.$submit=fu\
nction(b){return\
 a._$(b).submit(\
)};a.$val=functi\
on(b,f){var c=a.\
_$(b);return 1==\
arguments.length\
?c.val():c.val(f\
)};a._clearVars=\
function(){delet\
e jQuery;delete \
h;delete a;delet\
e SwingControlle\
r;delete J;delet\
e JM;delete JS;d\
elete JSV;\x0adelet\
e JU;delete JV;d\
elete java;delet\
e javajs;delete \
Clazz;delete c$}\
;var e=document,\
d=window,g={};g.\
ua=navigator.use\
rAgent.toLowerCa\
se();var m;a:{m=\
[\x22linux\x22,\x22unix\x22,\
\x22mac\x22,\x22win\x22];for\
(var j=m.length;\
j--;)if(-1!=g.ua\
.indexOf(m[j])){\
m=m[j];break a}m\
=\x22unknown\x22}g.os=\
m;g.browser=func\
tion(){for(var b\
=g.ua,a=\x22konquer\
or webkit omniwe\
b opera webtv ic\
ab msie mozilla\x22\
.split(\x22 \x22),c=0;\
c<a.length;c++)i\
f(0<=b.indexOf(a\
[c]))return a[c]\
;return\x22unknown\x22\
};g.browserName=\
g.browser();g.br\
owserVersion=par\
seFloat(g.ua.sub\
string(g.ua.inde\
xOf(g.browserNam\
e)+\x0ag.browserNam\
e.length+1));g.s\
upportsXhr2=func\
tion(){return h.\
support.cors||h.\
support.iecors};\
g.allowDestroy=\x22\
msie\x22!=g.browser\
Name;g.allowHTML\
5=\x22msie\x22!=g.brow\
serName||0>navig\
ator.appVersion.\
indexOf(\x22MSIE 8\x22\
);g.getDefaultLa\
nguage=function(\
){return navigat\
or.language||nav\
igator.userLangu\
age||\x22en-US\x22};g.\
_webGLtest=0;g.s\
upportsWebGL=fun\
ction(){if(!a.fe\
atureDetection._\
webGLtest){var b\
;a.featureDetect\
ion._webGLtest=d\
.WebGLRenderingC\
ontext&&((b=e.cr\
eateElement(\x22can\
vas\x22)).getContex\
t(\x22webgl\x22)||b.ge\
tContext(\x22experi\
mental-webgl\x22))?\
\x0a1:-1}return 0<a\
.featureDetectio\
n._webGLtest};g.\
supportsLocaliza\
tion=function(){\
for(var b=e.getE\
lementsByTagName\
(\x22meta\x22),a=b.len\
gth;0<=--a;)if(0\
<=b[a].outerHTML\
.toLowerCase().i\
ndexOf(\x22utf-8\x22))\
return!0;return!\
1};g.supportsJav\
a=function(){a.f\
eatureDetection.\
_javaEnabled||(a\
.featureDetectio\
n._javaEnabled=a\
._isMsie?navigat\
or.javaEnabled()\
?1:-1:navigator.\
javaEnabled()&&(\
!navigator.mimeT\
ypes||navigator.\
mimeTypes[\x22appli\
cation/x-java-ap\
plet\x22])?1:-1);re\
turn 0<a.feature\
Detection._javaE\
nabled};g.compli\
antBrowser=\x0afunc\
tion(){var b=!!e\
.getElementById,\
a=g.os;if(\x22opera\
\x22==g.browserName\
&&7.54>=g.browse\
rVersion&&\x22mac\x22=\
=a||\x22webkit\x22==g.\
browserName&&125\
.12>g.browserVer\
sion||\x22msie\x22==g.\
browserName&&\x22ma\
c\x22==a||\x22konquero\
r\x22==g.browserNam\
e&&3.3>=g.browse\
rVersion)b=!1;re\
turn b};g.isFull\
yCompliant=funct\
ion(){return g.c\
ompliantBrowser(\
)&&g.supportsJav\
a()};g.useIEObje\
ct=\x22win\x22==g.os&&\
\x22msie\x22==g.browse\
rName&&5.5<=g.br\
owserVersion;g.u\
seHtml4Object=\x22m\
ozilla\x22==g.brows\
erName&&5<=g.bro\
wserVersion||\x22op\
era\x22==g.browserN\
ame&&8<=g.browse\
rVersion||\x0a\x22webk\
it\x22==g.browserNa\
me;g.hasFileRead\
er=d.File&&d.Fil\
eReader;a.featur\
eDetection=g;a._\
ajax=function(b)\
{if(!b.async)ret\
urn a.$ajax(b).r\
esponseText;a._a\
jaxQueue.push(b)\
;1==a._ajaxQueue\
.length&&a._ajax\
Done()};a._ajaxD\
one=function(){v\
ar b=a._ajaxQueu\
e.shift();b&&a.$\
ajax(b)};a._grab\
berOptions=[[\x22$\x22\
,\x22NCI(small mole\
cules)\x22],[\x22:\x22,\x22P\
ubChem(small mol\
ecules)\x22],[\x22=\x22,\x22\
RCSB(macromolecu\
les)\x22],[\x22*\x22,\x22PDB\
e(macromolecules\
)\x22]];a._getGrabb\
erOptions=functi\
on(b){if(0==a._g\
rabberOptions.le\
ngth)return\x22\x22;va\
r f='<input type\
=\x22text\x22 id=\x22ID_q\
uery\x22 onfocus=\x22j\
Query(this).sele\
ct()\x22 onkeypress\
=\x22if(13==event.w\
hich){Jmol._appl\
ets[\x5c'ID\x5c']._sea\
rch();return fal\
se}\x22 size=\x2232\x22 v\
alue=\x22\x22 />',\x0ac='\
<button id=\x22ID_s\
ubmit\x22 onclick=\x22\
Jmol._applets[\x5c'\
ID\x5c']._search()\x22\
>Search</button>\
</nobr>';1==a._g\
rabberOptions.le\
ngth?(f=\x22<nobr>\x22\
+f+'<span style=\
\x22display:none\x22>'\
,c=\x22</span>\x22+c):\
f+=\x22<br /><nobr>\
\x22;for(var f=f+'<\
select id=\x22ID_se\
lect\x22>',e=0;e<a.\
_grabberOptions.\
length;e++)var d\
=a._grabberOptio\
ns[e],f=f+('<opt\
ion value=\x22'+d[0\
]+'\x22 '+(0==e?\x22se\
lected\x22:\x22\x22)+\x22>\x22+\
d[1]+\x22</option>\x22\
);f=(f+\x22</select\
>\x22+c).replace(/I\
D/g,b._id);retur\
n\x22<br />\x22+f};a._\
getScriptForData\
base=function(b)\
{return\x22$\x22==b?a.\
db._nciLoadScrip\
t:\x0a\x22:\x22==b?a.db._\
pubChemLoadScrip\
t:a.db._fileLoad\
Script};a._setIn\
fo=function(b,a,\
c){var e=[],d=\x22\x22\
;if(0==c.indexOf\
(\x22ERROR\x22))d=c;el\
se switch(a){cas\
e \x22=\x22:a=c.split(\
\x22<dimStructure.s\
tructureId>\x22);e=\
[\x22<table>\x22];for(\
c=1;c<a.length;c\
++)e.push('<tr><\
td valign=top><a\
 href=\x22javascrip\
t:Jmol.search('+\
b._id+\x22,'=\x22+a[c]\
.substring(0,4)+\
\x22')\x5c\x22>\x22+a[c].sub\
string(0,4)+\x22</a\
></td>\x22),e.push(\
\x22<td>\x22+a[c].spli\
t(\x22Title>\x22)[1].s\
plit(\x22</\x22)[0]+\x22<\
/td></tr>\x22);e.pu\
sh(\x22</table>\x22);d\
=a.length-1+\x22 ma\
tches\x22;break;cas\
e \x22$\x22:case \x22:\x22:b\
reak;default:ret\
urn}b._infoHeade\
r=\x0ad;b._info=e.j\
oin(\x22\x22);b._showI\
nfo(!0)};a._load\
Success=function\
(b,f){f&&(a._aja\
xDone(),f(b))};a\
._loadError=func\
tion(b){a._ajaxD\
one();a.say(\x22Err\
or connecting to\
 server: \x22+a._aj\
axCall);null!=b&\
&b()};a._isDatab\
aseCall=function\
(b){return 0<=a.\
db._databasePref\
ixes.indexOf(b.s\
ubstring(0,1))};\
a._getDirectData\
baseCall=functio\
n(b,f){if(f&&!a.\
featureDetection\
.supportsXhr2())\
return b;var c=2\
,e=b.substring(0\
,c),d=a.db._Dire\
ctDatabaseCalls[\
e]||a.db._Direct\
DatabaseCalls[e=\
b.substring(0,--\
c)];d&&(\x22:\x22==e?(\
e=b.toLowerCase(\
),\x0aisNaN(parseIn\
t(b.substring(1)\
))?0==e.indexOf(\
\x22:smiles:\x22)?(d+=\
\x22?POST?smiles=\x22+\
b.substring(8),b\
=\x22smiles\x22):0==e.\
indexOf(\x22:cid:\x22)\
?b=\x22cid/\x22+b.subs\
tring(5):(0==e.i\
ndexOf(\x22:name:\x22)\
?b=b.substring(5\
):0==e.indexOf(\x22\
:cas:\x22)&&(b=b.su\
bstring(4)),b=\x22n\
ame/\x22+encodeURIC\
omponent(b.subst\
ring(c))):b=\x22cid\
/\x22+b.substring(1\
)):b=encodeURICo\
mponent(b.substr\
ing(c)),0<=b.ind\
exOf(\x22.mmtf\x22)?b=\
\x22http://mmtf.rcs\
b.org/full/\x22+b:0\
<=d.indexOf(\x22FIL\
ENCI\x22)?(b=b.repl\
ace(/\x5c%2F/g,\x22/\x22)\
,b=d.replace(/\x5c%\
FILENCI/,b)):b=d\
.replace(/\x5c%FILE\
/,b));return b};\
\x0aa._getRawDataFr\
omServer=functio\
n(b,f,c,e,d,g){b\
=\x22?call=getRawDa\
taFromDatabase&d\
atabase=\x22+b+(0<=\
f.indexOf(\x22?POST\
?\x22)?\x22?POST?\x22:\x22\x22)\
+\x22&query=\x22+encod\
eURIComponent(f)\
+(d?\x22&encoding=b\
ase64\x22:\x22\x22)+(g?\x22\x22\
:\x22&script=\x22+enco\
deURIComponent(a\
._getScriptForDa\
tabase(b)));retu\
rn a._contactSer\
ver(b,c,e)};a._c\
heckFileName=fun\
ction(b,f,c){a._\
isDatabaseCall(f\
)&&(c&&a._setQue\
ryTerm(b,f),f=a.\
_getDirectDataba\
seCall(f,!0),a._\
isDatabaseCall(f\
)&&(f=a._getDire\
ctDatabaseCall(f\
,!1),c&&(c[0]=!0\
)));return f};a.\
_checkCache=func\
tion(b,\x0af,c){if(\
b._cacheFiles&&a\
._fileCache&&!f.\
endsWith(\x22.js\x22))\
{if(b=a._fileCac\
he[f])return Sys\
tem.out.println(\
\x22using \x22+b.lengt\
h+\x22 bytes of cac\
hed data for \x22+f\
),c(b),null;c=fu\
nction(b,f){c(a.\
_fileCache[b]=f)\
}}return c};a._p\
layAudio=functio\
n(b){var a=docum\
ent.createElemen\
t(\x22audio\x22);a.con\
trols=\x22true\x22;a.s\
rc=b;a.play()};a\
._loadFileData=f\
unction(b,f,c,e)\
{var d=[];f=a._c\
heckFileName(b,f\
,d);c=a._checkCa\
che(b,f,c);d[0]?\
a._getRawDataFro\
mServer(\x22_\x22,f,c,\
e):(b={type:\x22GET\
\x22,dataType:\x22text\
\x22,url:f,async:a.\
_asynchronous,\x0as\
uccess:function(\
b){a._loadSucces\
s(b,c)},error:fu\
nction(){a._load\
Error(e)}},a._ch\
eckAjaxPost(b),a\
._ajax(b))};a._g\
etInfoFromDataba\
se=function(b,f,\
c){if(\x22====\x22==f)\
{var e=a.db._res\
tQueryXml.replac\
e(/QUERY/,c),e={\
dataType:\x22text\x22,\
type:\x22POST\x22,cont\
entType:\x22applica\
tion/x-www-form-\
urlencoded\x22,url:\
a.db._restQueryU\
rl,data:encodeUR\
IComponent(e)+\x22&\
req=browser\x22,suc\
cess:function(e)\
{a._ajaxDone();a\
._extractInfoFro\
mRCSB(b,f,c,e)},\
error:function()\
{a._loadError(nu\
ll)},async:a._as\
ynchronous};retu\
rn a._ajax(e)}c=\
\x22?call=getInfoFr\
omDatabase&datab\
ase=\x22+\x0af+\x22&query\
=\x22+encodeURIComp\
onent(c);return \
a._contactServer\
(c,function(c){a\
._setInfo(b,f,c)\
})};a._extractIn\
foFromRCSB=funct\
ion(b,f,c,e){var\
 d=e.length/5;if\
(0!=d&&4==c.leng\
th&&1!=d){c=c.to\
UpperCase();var \
g=e.indexOf(c);0\
<g&&0<=\x2212345678\
9\x22.indexOf(c.sub\
string(0,1))&&(e\
=c+\x22,\x22+e.substri\
ng(0,g)+e.substr\
ing(g+5));50<d&&\
(e=e.substring(0\
,250));e=e.repla\
ce(/\x5cn/g,\x22,\x22);e=\
a._restReportUrl\
.replace(/IDLIST\
/,e);a._loadFile\
Data(b,e,functio\
n(c){a._setInfo(\
b,f,c)})}};a._ch\
eckAjaxPost=func\
tion(b){var a=b.\
url.indexOf(\x22?PO\
ST?\x22);\x0a0<a&&(b.d\
ata=b.url.substr\
ing(a+6),b.url=b\
.url.substring(0\
,a),b.type=\x22POST\
\x22,b.contentType=\
\x22application/x-w\
ww-form-urlencod\
ed\x22)};a._contact\
Server=function(\
b,f,c){b={dataTy\
pe:\x22text\x22,type:\x22\
GET\x22,url:a._serv\
erUrl+b,success:\
function(b){a._l\
oadSuccess(b,f)}\
,error:function(\
){a._loadError(c\
)},async:f?a._as\
ynchronous:!1};a\
._checkAjaxPost(\
b);return a._aja\
x(b)};a._setQuer\
yTerm=function(b\
,f){if(f&&b._has\
Options&&\x22http:/\
/\x22!=f.substring(\
0,7)){if(a._isDa\
tabaseCall(f)){v\
ar c=f.substring\
(0,1);f=f.substr\
ing(1);f.substri\
ng(0,\x0a1)==c&&0<=\
\x22=$\x22.indexOf(c)&\
&(f=f.substring(\
1));var e=a._get\
Element(b,\x22selec\
t\x22);if(e&&e.opti\
ons)for(var d=0;\
d<e.options.leng\
th;d++)e[d].valu\
e==c&&(e[d].sele\
cted=!0)}a.$val(\
a.$(b,\x22query\x22),f\
)}};a._search=fu\
nction(b,f,c){1<\
arguments.length\
||(f=null);a._se\
tQueryTerm(b,f);\
f||(f=a.$val(a.$\
(b,\x22query\x22)));0=\
=f.indexOf(\x22!\x22)?\
b._script(f.subs\
tring(1)):(f&&(f\
=f.replace(/\x5c\x22/g\
,\x22\x22)),b._showInf\
o(!1),a._searchM\
ol(b,f,c,!0))};a\
._searchMol=func\
tion(b,f,c,e){va\
r d;a._isDatabas\
eCall(f)?(d=f.su\
bstring(0,1),f=f\
.substring(1)):\x0a\
d=b._hasOptions?\
a.$val(a.$(b,\x22se\
lect\x22)):\x22$\x22;\x22=\x22=\
=d&&3==f.length&\
&(f=\x22=\x22+f);var g\
=d+f;if(f&&!(0>g\
.indexOf(\x22?\x22)&&g\
==b._thisJmolMod\
el)){b._thisJmol\
Model=g;var h;e&\
&null!=b._viewSe\
t&&null!=(h=a.Vi\
ew.__findView(b.\
_viewSet,{chemID\
:g}))?a.View.__s\
etView(h,b,!1):(\
\x22$\x22==d||\x22:\x22==d?b\
._jmolFileType=\x22\
MOL\x22:\x22=\x22==d&&(b.\
_jmolFileType=\x22P\
DB\x22),b._searchDa\
tabase(f,d,c))}}\
;a._searchDataba\
se=function(b,f,\
c,e){b._showInfo\
(!1);return 0<=f\
.indexOf(\x22?\x22)?(a\
._getInfoFromDat\
abase(b,c,f.spli\
t(\x22?\x22)[0]),!0):a\
.db._DirectDatab\
aseCalls[c]?\x0a(b.\
_loadFile(c+f,e)\
,!0):!1};a._sync\
BinaryOK=\x22?\x22;a._\
canSyncBinary=fu\
nction(b){if(a._\
isAsync)return!0\
;if(self.VBArray\
)return a._syncB\
inaryOK=!1;if(\x22?\
\x22!=a._syncBinary\
OK)return a._syn\
cBinaryOK;a._syn\
cBinaryOK=!0;try\
{var f=new windo\
w.XMLHttpRequest\
;f.open(\x22text\x22,a\
._ajaxTestSite,!\
1);f.hasOwnPrope\
rty(\x22responseTyp\
e\x22)?f.responseTy\
pe=\x22arraybuffer\x22\
:f.overrideMimeT\
ype&&f.overrideM\
imeType(\x22text/pl\
ain; charset=x-u\
ser-defined\x22)}ca\
tch(c){return Sy\
stem.out.println\
(\x22JSmolCore.js: \
synchronous bina\
ry file transfer\
 is requested bu\
t not available\x22\
),\x0aa._alertNoBin\
ary&&!b&&alert(\x22\
JSmolCore.js: sy\
nchronous binary\
 file transfer i\
s requested but \
not available\x22),\
a._syncBinaryOK=\
!1}return!0};a._\
binaryTypes=\x22mmt\
f .gz .jpg .gif \
.png .zip .jmol \
.bin .smol .spar\
tan .mrc .map .c\
cp4 .dn6 .delphi\
 .omap .pse .dcd\
\x22.split(\x22 \x22);a._\
isBinaryUrl=func\
tion(b){for(var \
f=a._binaryTypes\
.length;0<=--f;)\
if(0<=b.indexOf(\
a._binaryTypes[f\
]))return!0;retu\
rn!1};a._getFile\
Data=function(b,\
f,c){var e=a._is\
BinaryUrl(b),d=0\
<=b.indexOf(\x22.gz\
\x22)&&0<=b.indexOf\
(\x22rcsb.org\x22);d&&\
(b=b.replace(/\x5c.\
gz/,\x0a\x22\x22),e=!1);v\
ar d=e&&!f&&!a._\
canSyncBinary(d)\
,g=0<=b.indexOf(\
\x22?POST?\x22);0==b.i\
ndexOf(\x22file:/\x22)\
&&0!=b.indexOf(\x22\
file:///\x22)&&(b=\x22\
file://\x22+b.subst\
ring(5));var h=0\
>b.indexOf(\x22://\x22\
)||0==b.indexOf(\
document.locatio\
n.protocol)&&0<=\
b.indexOf(docume\
nt.location.host\
),m=\x22https://\x22==\
a._httpProto&&0=\
=b.indexOf(\x22http\
://\x22),j=a._isDir\
ectCall(b);!j&&0\
<=b.indexOf(\x22?AL\
LOWSORIGIN?\x22)&&(\
j=!0,b=b.replace\
(/\x5c?ALLOWSORIGIN\
\x5c?/,\x22\x22));var k=!\
h&&a.$supportsIE\
CrossDomainScrip\
ting(),l=null;if\
(m||d||!h&&!j||!\
f&&k)l=a._getRaw\
DataFromServer(\x22\
_\x22,\x0ab,f,f,d,!0);\
else{b=b.replace\
(/file:\x5c/\x5c/\x5c/\x5c//\
,\x22file://\x22);var \
n={dataType:e?\x22b\
inary\x22:\x22text\x22,as\
ync:!!f};g?(n.ty\
pe=\x22POST\x22,n.url=\
b.split(\x22?POST?\x22\
)[0],n.data=b.sp\
lit(\x22?POST?\x22)[1]\
):(n.type=\x22GET\x22,\
n.url=b);f&&(n.s\
uccess=function(\
){f(a._xhrReturn\
(n.xhr))},n.erro\
r=function(){f(n\
.xhr.statusText)\
});n.xhr=a.$ajax\
(n);f||(l=a._xhr\
Return(n.xhr))}i\
f(!c)return l;nu\
ll==l&&(l=\x22\x22,e=!\
1);e&&(e=a._canS\
yncBinary(!0));r\
eturn e?a._strTo\
Bytes(l):JU.SB.n\
ewS(l)};a._xhrRe\
turn=function(b)\
{return!b.respon\
seText||self.Cla\
zz&&Clazz.instan\
ceOf(b.response,\
\x0aself.ArrayBuffe\
r)?b.response||b\
.statusText:b.re\
sponseText};a._i\
sDirectCall=func\
tion(b){if(0<=b.\
indexOf(\x22?ALLOWS\
ORIGIN?\x22))return\
!0;for(var f in \
a.db._DirectData\
baseCalls)if(0<=\
f.indexOf(\x22.\x22)&&\
0<=b.indexOf(f))\
return!0;return!\
1};a._cleanFileD\
ata=function(b){\
return 0<=b.inde\
xOf(\x22\x5cr\x22)&&0<=b.\
indexOf(\x22\x5cn\x22)?b.\
replace(/\x5cr\x5cn/g,\
\x22\x5cn\x22):0<=b.index\
Of(\x22\x5cr\x22)?b.repla\
ce(/\x5cr/g,\x22\x5cn\x22):b\
};a._getFileType\
=function(b){var\
 a=b.substring(0\
,1);if(\x22$\x22==a||\x22\
:\x22==a)return\x22MOL\
\x22;if(\x22=\x22==a)retu\
rn\x22=\x22==b.substri\
ng(1,2)?\x22LCIF\x22:\x22\
PDB\x22;b=\x0ab.split(\
\x22.\x22).pop().toUpp\
erCase();return \
b.substring(0,Ma\
th.min(b.length,\
3))};a._getZ=fun\
ction(b,f){retur\
n b&&b._z&&b._z[\
f]||a._z[f]};a._\
incrZ=function(b\
,f){return b&&b.\
_z&&++b._z[f]||+\
+a._z[f]};a._hid\
eLocalFileReader\
=function(b){b._\
localReader&&a.$\
setVisible(b._lo\
calReader,!1);b.\
_readingLocal=!1\
;a._setCursor(b,\
0)};a.loadFileFr\
omDialog=functio\
n(b){a._loadFile\
Asynchronously(n\
ull,b,null,null)\
};a._loadFileAsy\
nchronously=func\
tion(b,f,c,e){if\
(c&&0!=c.indexOf\
(\x22?\x22)){var d=c;c\
=a._checkFileNam\
e(f,c);var g=\x0afu\
nction(g){a._set\
Data(b,c,d,g,e,f\
)},g=a._checkCac\
he(f,c,g);0<=c.i\
ndexOf(\x22|\x22)&&(c=\
c.split(\x22|\x22)[0])\
;return null==g?\
null:a._getFileD\
ata(c,g)}if(!a.f\
eatureDetection.\
hasFileReader)re\
turn b?b.setData\
(msg,null,null,e\
,f):alert(msg);f\
._localReader||(\
g='<div id=\x22ID\x22 \
style=\x22z-index:'\
+a._getZ(f,\x22file\
Opener\x22)+';posit\
ion:absolute;bac\
kground:#E0E0E0;\
left:10px;top:10\
px\x22><div style=\x22\
margin:5px 5px 5\
px 5px;\x22><button\
 id=\x22ID_loadurl\x22\
>URL</button><in\
put type=\x22file\x22 \
id=\x22ID_files\x22 />\
<button id=\x22ID_l\
oadfile\x22>load</b\
utton><button id\
=\x22ID_cancel\x22>can\
cel</button></di\
v><div>',\x0aa.$aft\
er(\x22#\x22+f._id+\x22_a\
ppletdiv\x22,g.repl\
ace(/ID/g,f._id+\
\x22_localReader\x22))\
,f._localReader=\
a.$(f,\x22localRead\
er\x22));a.$appEven\
t(f,\x22localReader\
_loadurl\x22,\x22click\
\x22);a.$appEvent(f\
,\x22localReader_lo\
adurl\x22,\x22click\x22,f\
unction(){var b=\
prompt(\x22Enter a \
URL\x22);b&&(a._hid\
eLocalFileReader\
(f,0),a._setData\
(null,b,b,null,e\
,f))});a.$appEve\
nt(f,\x22localReade\
r_loadfile\x22,\x22cli\
ck\x22);a.$appEvent\
(f,\x22localReader_\
loadfile\x22,\x22click\
\x22,function(){var\
 c=a.$(f,\x22localR\
eader_files\x22)[0]\
.files[0],d=new \
FileReader;d.onl\
oadend=function(\
d){d.target.read\
yState==\x0aFileRea\
der.DONE&&(a._hi\
deLocalFileReade\
r(f,0),a._setDat\
a(b,c.name,c.nam\
e,d.target.resul\
t,e,f))};try{d.r\
eadAsArrayBuffer\
(c)}catch(g){ale\
rt(\x22You must sel\
ect a file first\
.\x22)}});a.$appEve\
nt(f,\x22localReade\
r_cancel\x22,\x22click\
\x22);a.$appEvent(f\
,\x22localReader_ca\
ncel\x22,\x22click\x22,fu\
nction(){a._hide\
LocalFileReader(\
f);b&&b.setData(\
\x22#CANCELED#\x22,nul\
l,null,e,f)});a.\
$setVisible(f._l\
ocalReader,!0);f\
._readingLocal=!\
0};a._setData=fu\
nction(b,f,c,e,d\
,g){e&&(e=a._str\
ToBytes(e));null\
!=e&&(null==b||0\
<=f.indexOf(\x22.jd\
x\x22))&&a.Cache.pu\
t(\x22cache://\x22+\x0af,\
e);null==b?g._ap\
plet.openFileAsy\
ncSpecial(null==\
e?f:\x22cache://\x22+f\
,1):b.setData(f,\
c,e,d)};a._doAja\
x=function(b,f,c\
){b=b.toString()\
;if(null!=c)retu\
rn a._saveFile(b\
,c);f&&(b+=\x22?POS\
T?\x22+f);return a.\
_getFileData(b,n\
ull,!0)};a._save\
File=function(b,\
f,c,e){if(a._loc\
alFileSaveFuncti\
on&&a._localFile\
SaveFunction(b,f\
))return\x22OK\x22;b=b\
.substring(b.las\
tIndexOf(\x22/\x22)+1)\
;c||(c=0<=b.inde\
xOf(\x22.pdf\x22)?\x22app\
lication/pdf\x22:0<\
=b.indexOf(\x22.png\
\x22)?\x22image/png\x22:0\
<=b.indexOf(\x22.gi\
f\x22)?\x22image/gif\x22:\
0<=b.indexOf(\x22.j\
pg\x22)?\x22image/jpg\x22\
:\x22\x22);\x0avar d=\x22str\
ing\x22==typeof f;d\
||(f=(JU?JU:J.ut\
il).Base64.getBa\
se64(f).toString\
());e||(e=d?\x22\x22:\x22\
base64\x22);(d=a._s\
erverUrl)&&0<=d.\
indexOf(\x22your.se\
rver\x22)&&(d=\x22\x22);a\
._useDataURI||!d\
?(e||(f=btoa(f))\
,e=document.crea\
teElement(\x22a\x22),e\
.href=\x22data:\x22+c+\
\x22;base64,\x22+f,e.t\
ype=c||\x22text/pla\
in\x22,e.download=b\
,e.target=\x22_blan\
k\x22,h(\x22body\x22).app\
end(e),e.click()\
,e.remove()):(a.\
_formdiv||(a.$af\
ter(\x22body\x22,'<div\
 id=\x22__jsmolform\
div__\x22 style=\x22di\
splay:none\x22>\x5ct\x5ct\
\x5ct\x5ct\x5ct\x5ct<form id\
=\x22__jsmolform__\x22\
 method=\x22post\x22 t\
arget=\x22_blank\x22 a\
ction=\x22\x22>\x5ct\x5ct\x5ct\x5c\
t\x5ct\x5ct<input name\
=\x22call\x22 value=\x22s\
aveFile\x22/>\x5ct\x5ct\x5ct\
\x5ct\x5ct\x5ct<input id=\
\x22__jsmolmimetype\
__\x22 name=\x22mimety\
pe\x22 value=\x22\x22/>\x5ct\
\x5ct\x5ct\x5ct\x5ct\x5ct<input\
 id=\x22__jsmolenco\
ding__\x22 name=\x22en\
coding\x22 value=\x22\x22\
/>\x5ct\x5ct\x5ct\x5ct\x5ct\x5ct<i\
nput id=\x22__jsmol\
filename__\x22 name\
=\x22filename\x22 valu\
e=\x22\x22/>\x5ct\x5ct\x5ct\x5ct\x5ct\
\x5ct<textarea id=\x22\
__jsmoldata__\x22 n\
ame=\x22data\x22></tex\
tarea>\x5ct\x5ct\x5ct\x5ct\x5ct\
\x5ct</form>\x5ct\x5ct\x5ct\x5c\
t\x5ct\x5ct</div>'),\x0aa\
._formdiv=\x22__jsm\
olform__\x22),a.$at\
tr(a._formdiv,\x22a\
ction\x22,d+\x22?\x22+(ne\
w Date).getMilli\
seconds()),a.$va\
l(\x22__jsmoldata__\
\x22,f),a.$val(\x22__j\
smolfilename__\x22,\
b),a.$val(\x22__jsm\
olmimetype__\x22,c)\
,a.$val(\x22__jsmol\
encoding__\x22,e),a\
.$submit(\x22__jsmo\
lform__\x22),a.$val\
(\x22__jsmoldata__\x22\
,\x22\x22),a.$val(\x22__j\
smolfilename__\x22,\
\x22\x22));return\x22OK\x22}\
;a._strToBytes=f\
unction(b){if(Cl\
azz.instanceOf(b\
,self.ArrayBuffe\
r))return Clazz.\
newByteArray(-1,\
b);for(var a=Cla\
zz.newByteArray(\
b.length,0),c=b.\
length;0<=--c;)a\
[c]=b.charCodeAt\
(c)&255;return a\
};a._setConsoleD\
iv=\x0afunction(b){\
self.Clazz&&Claz\
z.setConsoleDiv(\
b)};a._registerA\
pplet=function(b\
,f){return windo\
w[b]=a._applets[\
b]=a._applets[b+\
\x22__\x22+a._syncId+\x22\
__\x22]=f};a._ready\
Callback=functio\
n(b,f,c,e,d){b=b\
.split(\x22_object\x22\
)[0];var g=a._ap\
plets[b];if(c=c.\
booleanValue?c.b\
ooleanValue():c)\
g._appletPanel=d\
||e,g._applet=e;\
a._track(g._read\
yCallback(b,f,c)\
)};a._getWrapper\
=function(b,f){v\
ar c;if(f){var e\
=\x22\x22;if(b._coverI\
mage)var e=' onc\
lick=\x22Jmol.cover\
Applet(ID, false\
)\x22 title=\x22'+b._c\
overTitle+'\x22',d=\
'<image id=\x22ID_c\
overclickgo\x22 src\
=\x22'+\x0ab._makeLive\
Image+'\x22 style=\x22\
width:25px;heigh\
t:25px;position:\
absolute;bottom:\
10px;left:10px;z\
-index:'+a._getZ\
(b,\x22coverImage\x22)\
+';opacity:0.5;\x22\
'+e+\x22 />\x22,e='<di\
v id=\x22ID_coverdi\
v\x22 style=\x22backgr\
ound-color:red;z\
-index:'+a._getZ\
(b,\x22coverImage\x22)\
+';width:100%;he\
ight:100%;displa\
y:inline;positio\
n:absolute;top:0\
px;left:0px\x22><im\
age id=\x22ID_cover\
image\x22 src=\x22'+b.\
_coverImage+'\x22 s\
tyle=\x22width:100%\
;height:100%\x22'+e\
+\x22/>\x22+d+\x22</div>\x22\
;d=b._isJava?\x22\x22:\
'<image id=\x22ID_w\
aitimage\x22 src=\x22'\
+b._j2sPath+'/im\
g/cursor_wait.gi\
f\x22 style=\x22displa\
y:none;position:\
absolute;bottom:\
10px;left:10px;z\
-index:'+\x0aa._get\
Z(b,\x22coverImage\x22\
)+';\x22 />';c=a._a\
ppletCssText.rep\
lace(/\x5c'/g,'\x22');\
var g=b._getSpin\
ner&&b._getSpinn\
er();b._spinner=\
g=!g||\x22none\x22==g?\
\x22\x22:\x22background-i\
mage:url(\x22+g+\x22);\
 background-repe\
at:no-repeat; ba\
ckground-positio\
n:center;\x22;c=g+(\
0<=c.indexOf('st\
yle=\x22')?c.split(\
'style=\x22')[1]:'\x22\
 '+c);c='...<div\
 id=\x22ID_appletin\
fotablediv\x22 styl\
e=\x22width:Wpx;hei\
ght:Hpx;position\
:relative;font-s\
ize:14px;text-al\
ign:left\x22>IMG WA\
IT......<div id=\
\x22ID_appletdiv\x22 s\
tyle=\x22z-index:'+\
a._getZ(b,\x22heade\
r\x22)+\x22;width:100%\
;height:100%;pos\
ition:absolute;t\
op:0px;left:0px;\
\x22+\x0ac+\x22>\x22;var g=b\
._height,h=b._wi\
dth;if(\x22string\x22!\
==typeof g||0>g.\
indexOf(\x22%\x22))g+=\
\x22px\x22;if(\x22string\x22\
!==typeof h||0>h\
.indexOf(\x22%\x22))h+\
=\x22px\x22;c=c.replac\
e(/IMG/,e).repla\
ce(/WAIT/,d).rep\
lace(/Hpx/g,g).r\
eplace(/Wpx/g,h)\
}else c='......<\
/div>......<div \
id=\x22ID_2dappletd\
iv\x22 style=\x22posit\
ion:absolute;wid\
th:100%;height:1\
00%;overflow:hid\
den;display:none\
\x22></div>......<d\
iv id=\x22ID_infota\
blediv\x22 style=\x22w\
idth:100%;height\
:100%;position:a\
bsolute;top:0px;\
left:0px\x22>......\
...<div id=\x22ID_i\
nfoheaderdiv\x22 st\
yle=\x22height:20px\
;width:100%;back\
ground:yellow;di\
splay:none\x22><spa\
n id=\x22ID_infohea\
derspan\x22></span>\
<span id=\x22ID_inf\
ocheckboxspan\x22 s\
tyle=\x22position:a\
bsolute;text-ali\
gn:right;right:1\
px;\x22><a href=\x22ja\
vascript:Jmol.sh\
owInfo(ID,false)\
\x22>[x]</a></span>\
</div>.........<\
div id=\x22ID_infod\
iv\x22 style=\x22posit\
ion:absolute;top\
:20px;bottom:0px\
;width:100%;heig\
ht:100%;overflow\
:auto\x22></div>...\
...</div>...</di\
v>';\x0areturn c.re\
place(/\x5c.\x5c.\x5c./g,\
\x22\x22).replace(/[\x5cn\
\x5cr]/g,\x22\x22).replac\
e(/ID/g,b._id)};\
a._hideLoadingSp\
inner=function(b\
){b._spinner&&a.\
$css(a.$(b,\x22appl\
etdiv\x22),{\x22backgr\
ound-image\x22:\x22\x22})\
};a._documentWri\
te=function(b){i\
f(a._document){i\
f(a._isXHTML&&!a\
._XhtmlElement){\
var f=document.g\
etElementsByTagN\
ame(\x22script\x22);a.\
_XhtmlElement=f.\
item(f.length-1)\
;a._XhtmlAppendC\
hild=!1}a._Xhtml\
Element?a._domWr\
ite(b):a._docume\
nt.write(b)}retu\
rn b};a._domWrit\
e=function(b){fo\
r(var f=[0];f[0]\
<b.length;){var \
c=a._getDomEleme\
nt(b,f);if(!c)br\
eak;\x0aa._XhtmlApp\
endChild?a._Xhtm\
lElement.appendC\
hild(c):a._Xhtml\
Element.parentNo\
de.insertBefore(\
c,_jmol.XhtmlEle\
ment)}};a._getDo\
mElement=functio\
n(b,a){var c=doc\
ument.createElem\
ent(\x22span\x22);c.in\
nerHTML=b;a[0]=b\
.length;return c\
};a._setObject=f\
unction(b,f,c){b\
._id=f;b.__Info=\
{};c.z&&c.zIndex\
Base&&(a._z=a._g\
etZOrders(c.zInd\
exBase));for(var\
 e in c)b.__Info\
[e]=c[e];(b._z=c\
.z)||c.zIndexBas\
e&&(b._z=b.__Inf\
o.z=a._getZOrder\
s(c.zIndexBase))\
;b._width=c.widt\
h;b._height=c.he\
ight;b._noscript\
=!b._isJava&&c.n\
oscript;b._conso\
le=\x0ac.console;b.\
_cacheFiles=!!c.\
cacheFiles;b._vi\
ewSet=null==c.vi\
ewSet||b._isJava\
?null:\x22Set\x22+c.vi\
ewSet;null!=b._v\
iewSet&&(a.View.\
__init(b),b._cur\
rentView=null);!\
a._fileCache&&b.\
_cacheFiles&&(a.\
_fileCache={});b\
._console||(b._c\
onsole=b._id+\x22_i\
nfodiv\x22);\x22none\x22=\
=b._console&&(b.\
_console=null);b\
._color=c.color?\
c.color.replace(\
/0x/,\x22#\x22):\x22#FFFF\
FF\x22;b._disableIn\
itialConsole=c.d\
isableInitialCon\
sole;b._noMonito\
r=c.disableJ2SLo\
adMonitor;a._j2s\
Path&&(c.j2sPath\
=a._j2sPath);b._\
j2sPath=c.j2sPat\
h;b._coverImage=\
c.coverImage;\x0ab.\
_makeLiveImage=c\
.makeLiveImage||\
c.j2sPath+\x22/img/\
play_make_live.j\
pg\x22;b._isCovered\
=!!b._coverImage\
;b._deferApplet=\
c.deferApplet||b\
._isCovered&&b._\
isJava;b._deferU\
ncover=c.deferUn\
cover&&!b._isJav\
a;b._coverScript\
=c.coverScript;b\
._coverTitle=c.c\
overTitle;b._cov\
erTitle||(b._cov\
erTitle=b._defer\
Applet?\x22activate\
 3D model\x22:\x223D m\
odel is loading.\
..\x22);b._containe\
rWidth=b._width+\
(b._width==parse\
Float(b._width)?\
\x22px\x22:\x22\x22);b._cont\
ainerHeight=b._h\
eight+(b._height\
==parseFloat(b._\
height)?\x22px\x22:\x22\x22)\
;b._info=\x22\x22;b._i\
nfoHeader=\x0ab._jm\
olType+' \x22'+b._i\
d+'\x22';b._hasOpti\
ons=c.addSelecti\
onOptions;b._def\
aultModel=c.defa\
ultModel;b._read\
yScript=c.script\
?c.script:\x22\x22;b._\
readyFunction=c.\
readyFunction;b.\
_coverImage&&!b.\
_deferApplet&&(b\
._readyScript+=\x22\
;javascript \x22+f+\
\x22._displayCoverI\
mage(false)\x22);b.\
_src=c.src};a._a\
ddDefaultInfo=fu\
nction(b,f){for(\
var c in f)\x22unde\
fined\x22==typeof b\
[c]&&(b[c]=f[c])\
;a._use&&(b.use=\
a._use);0<=b.use\
.indexOf(\x22SIGNED\
\x22)&&(0>b.jarFile\
.indexOf(\x22Signed\
\x22)&&(b.jarFile=b\
.jarFile.replace\
(/Applet/,\x22Apple\
tSigned\x22)),b.use\
=\x0ab.use.replace(\
/SIGNED/,\x22JAVA\x22)\
,b.isSigned=!0)}\
;a._syncedApplet\
s=[];a._syncedCo\
mmands=[];a._syn\
cedReady=[];a._s\
yncReady=!1;a._i\
sJmolJSVSync=!1;\
a._setReady=func\
tion(b){a._synce\
dReady[b]=1;for(\
var f=0,c=0;c<a.\
_syncedApplets.l\
ength;c++){if(a.\
_syncedApplets[c\
]==b._id)a._sync\
edApplets[c]=b,a\
._syncedReady[c]\
=1;else if(!a._s\
yncedReady[c])co\
ntinue;f++}f==a.\
_syncedApplets.l\
ength&&a._setSyn\
cReady()};a._set\
Destroy=function\
(b){a.featureDet\
ection.allowDest\
roy&&a.$windowOn\
(\x22beforeunload\x22,\
function(){a._de\
stroy(b)})};\x0aa._\
destroy=function\
(b){try{b._apple\
tPanel&&b._apple\
tPanel.destroy()\
;b._applet=null;\
a._unsetMouse(b.\
_canvas);b._canv\
as=null;for(var \
f=0,c=0;c<a._syn\
cedApplets.lengt\
h;c++)a._syncedA\
pplets[c]==b&&(a\
._syncedApplets[\
c]=null),a._sync\
edApplets[c]&&f+\
+;0<f||a._clearV\
ars()}catch(e){}\
};a._setSyncRead\
y=function(){a._\
syncReady=!0;for\
(var b=\x22\x22,f=0;f<\
a._syncedApplets\
.length;f++)a._s\
yncedCommands[f]\
&&(b+=\x22Jmol.scri\
pt(Jmol._syncedA\
pplets[\x22+f+\x22], J\
mol._syncedComma\
nds[\x22+f+\x22]);\x22);s\
etTimeout(b,50)}\
;a._mySyncCallba\
ck=\x0afunction(b,f\
){app=a._applets\
[b];if(app._view\
Set)a.View.updat\
eFromSync(app,f)\
;else{if(!a._syn\
cReady||!a._isJm\
olJSVSync)return\
 1;for(var c=0;c\
<a._syncedApplet\
s.length;c++)0<=\
f.indexOf(a._syn\
cedApplets[c]._s\
yncKeyword)&&a._\
syncedApplets[c]\
._syncScript(f);\
return 0}};a._ge\
tElement=functio\
n(b,a){return do\
cument.getElemen\
tById(b._id+\x22_\x22+\
a)||{}};a._evalJ\
SON=function(b,a\
){b+=\x22\x22;if(!b)re\
turn[];if(\x22{\x22!=b\
.charAt(0))retur\
n 0<=b.indexOf(\x22\
 | \x22)&&(b=b.repl\
ace(/\x5c \x5c|\x5c /g,\x22\x5c\
n\x22)),b;var c=(ne\
w Function(\x22retu\
rn \x22+b))();\x0aretu\
rn!c?null:a&&voi\
d 0!=c[a]?c[a]:c\
};a._sortMessage\
s=function(b){fu\
nction a(b,c){re\
turn b[0]<c[0]?1\
:b[0]>c[0]?-1:0}\
if(!b||\x22object\x22!\
=typeof b)return\
[];for(var c=[],\
e=b.length-1;0<=\
e;e--)for(var d=\
0,g=b[e].length;\
d<g;d++)c[c.leng\
th]=b[e][d];if(0\
!=c.length)retur\
n c=c.sort(a)};a\
._setMouseOwner=\
function(b,f){nu\
ll==b||f?a._mous\
eOwner=b:a._mous\
eOwner==b&&(a._m\
ouseOwner=null)}\
;a._jsGetMouseMo\
difiers=function\
(b){var a=0;swit\
ch(b.button){cas\
e 0:a=16;break;c\
ase 1:a=8;break;\
case 2:a=4}b.shi\
ftKey&&(a+=1);b.\
altKey&&\x0a(a+=8);\
b.ctrlKey&&(a+=2\
);return a};a._j\
sGetXY=function(\
b,f){if(!b.apple\
t._ready||a._tou\
ching&&0>f.type.\
indexOf(\x22touch\x22)\
)return!1;var c=\
a.$offset(b.id),\
e,d=f.originalEv\
ent;f.pageX||(f.\
pageX=d.pageX);f\
.pageY||(f.pageY\
=d.pageY);a._mou\
sePageX=f.pageX;\
a._mousePageY=f.\
pageY;d.targetTo\
uches&&d.targetT\
ouches[0]?(e=d.t\
argetTouches[0].\
pageX-c.left,c=d\
.targetTouches[0\
].pageY-c.top):d\
.changedTouches?\
(e=d.changedTouc\
hes[0].pageX-c.l\
eft,c=d.changedT\
ouches[0].pageY-\
c.top):(e=f.page\
X-c.left,c=f.pag\
eY-c.top);return\
 void 0==\x0ae?null\
:[Math.round(e),\
Math.round(c),a.\
_jsGetMouseModif\
iers(f)]};a._set\
Cursor=function(\
b,f){if(!b._isJa\
va&&!b._readingL\
ocal){var c;swit\
ch(f){case 1:c=\x22\
crosshair\x22;break\
;case 3:c=\x22wait\x22\
;a.$setVisible(a\
.$(b,\x22waitimage\x22\
),!0);break;case\
 8:c=\x22ns-resize\x22\
;break;case 12:c\
=\x22grab\x22;break;ca\
se 13:c=\x22move\x22;b\
reak;default:a.$\
setVisible(a.$(b\
,\x22waitimage\x22),!1\
),c=\x22default\x22}b.\
_canvas.style.cu\
rsor=c}};a._gest\
ureUpdate=functi\
on(b,f){f.stopPr\
opagation();f.pr\
eventDefault();v\
ar c=f.originalE\
vent;switch(f.ty\
pe){case \x22touchs\
tart\x22:a._touchin\
g=\x0a!0;break;case\
 \x22touchend\x22:a._t\
ouching=!1}if(!c\
.touches||2!=c.t\
ouches.length)re\
turn!1;switch(f.\
type){case \x22touc\
hstart\x22:b._touch\
es=[[],[]];break\
;case \x22touchmove\
\x22:var e=a.$offse\
t(b.id),d=b._tou\
ches[0],g=b._tou\
ches[1];d.push([\
c.touches[0].pag\
eX-e.left,c.touc\
hes[0].pageY-e.t\
op]);g.push([c.t\
ouches[1].pageX-\
e.left,c.touches\
[1].pageY-e.top]\
);c=d.length;3<c\
&&(d.shift(),g.s\
hift());2<=c&&b.\
applet._processG\
esture(b._touche\
s)}return!0};a._\
jsSetMouse=funct\
ion(b){var f=fun\
ction(b){return!\
b.target||0<=(\x22\x22\
+b.target.classN\
ame).indexOf(\x22sw\
ingjs-ui\x22)};\x0aa.$\
bind(b,\x22mousedow\
n touchstart\x22,fu\
nction(c){if(f(c\
))return!0;a._se\
tMouseOwner(b,!0\
);c.stopPropagat\
ion();var e=c.ta\
rget[\x22data-UI\x22];\
(!e||!e.handleJS\
Event(b,501,c))&\
&c.preventDefaul\
t();b.isDragging\
=!0;if(\x22touchsta\
rt\x22==c.type&&a._\
gestureUpdate(b,\
c))return!!e;a._\
setConsoleDiv(b.\
applet._console)\
;var d=a._jsGetX\
Y(b,c);d&&(2!=c.\
button&&a.Swing.\
hideMenus(b.appl\
et),b.applet._pr\
ocessEvent(501,d\
));return!!e});a\
.$bind(b,\x22mouseu\
p touchend\x22,func\
tion(c){if(f(c))\
return!0;a._setM\
ouseOwner(null);\
c.stopPropagatio\
n();\x0avar e=c.tar\
get[\x22data-UI\x22];(\
!e||!e.handleJSE\
vent(b,502,c))&&\
c.preventDefault\
();b.isDragging=\
!1;if(\x22touchend\x22\
==c.type&&a._ges\
tureUpdate(b,c))\
return!!e;(c=a._\
jsGetXY(b,c))&&b\
.applet._process\
Event(502,c);ret\
urn!!e});a.$bind\
(b,\x22mousemove to\
uchmove\x22,functio\
n(c){if(f(c))ret\
urn!0;if(a._mous\
eOwner&&a._mouse\
Owner!=b&&a._mou\
seOwner.isDraggi\
ng){if(!a._mouse\
Owner.mouseMove)\
return!0;a._mous\
eOwner.mouseMove\
(c);return!1}ret\
urn a._drag(b,c)\
});a._drag=funct\
ion(b,e){e.stopP\
ropagation();e.p\
reventDefault();\
if(\x22touchmove\x22==\
\x0ae.type&&a._gest\
ureUpdate(b,e))r\
eturn!1;var f=a.\
_jsGetXY(b,e);if\
(!f)return!1;b.i\
sDragging||(f[2]\
=0);var d=e.targ\
et[\x22data-UI\x22];b.\
isdragging&&(!d|\
|d.handleJSEvent\
(b,506,e));b.app\
let._processEven\
t(b.isDragging?5\
06:503,f);return\
!!d};a.$bind(b,\x22\
DOMMouseScroll m\
ousewheel\x22,funct\
ion(c){if(f(c))r\
eturn!0;c.stopPr\
opagation();c.pr\
eventDefault();b\
.isDragging=!1;v\
ar e=c.originalE\
vent,e=e.detail?\
e.detail:(\x22mac\x22=\
=a.featureDetect\
ion.os?1:-1)*e.w\
heelDelta;c=a._j\
sGetMouseModifie\
rs(c);b.applet._\
processEvent(-1,\
[0>e?-1:\x0a1,0,c])\
;return!1});a.$b\
ind(b,\x22contextme\
nu\x22,function(){r\
eturn!1});a.$bin\
d(b,\x22mouseout\x22,f\
unction(e){if(f(\
e))return!0;a._m\
ouseOwner&&!a._m\
ouseOwner.mouseM\
ove&&a._setMouse\
Owner(null);b.ap\
plet._appletPane\
l&&b.applet._app\
letPanel.startHo\
verWatcher(!1);a\
._jsGetXY(b,e);r\
eturn!1});a.$bin\
d(b,\x22mouseenter\x22\
,function(e){if(\
f(e))return!0;b.\
applet._appletPa\
nel&&b.applet._a\
ppletPanel.start\
HoverWatcher(!0)\
;if(0===e.button\
s||0===e.which){\
b.isDragging=!1;\
e=a._jsGetXY(b,e\
);if(!e)return!1\
;b.applet._proce\
ssEvent(504,e);\x0a\
b.applet._proces\
sEvent(502,e);re\
turn!1}});a.$bin\
d(b,\x22mousemoveou\
tjsmol\x22,function\
(e,d,g){if(f(g))\
return!0;if(b==a\
._mouseOwner&&b.\
isDragging)retur\
n a._drag(b,g)})\
;b.applet._is2D&\
&a.$resize(funct\
ion(){b.applet&&\
b.applet._resize\
()});a.$bind(\x22bo\
dy\x22,\x22mouseup tou\
chend\x22,function(\
e){if(f(e))retur\
n!0;b.applet&&(b\
.isDragging=!1);\
a._setMouseOwner\
(null)})};a._jsU\
nsetMouse=functi\
on(b){b.applet=n\
ull;a.$bind(b,\x22m\
ousedown touchst\
art mousemove to\
uchmove mouseup \
touchend DOMMous\
eScroll mousewhe\
el contextmenu m\
ouseout mouseent\
er\x22,\x0anull);a._se\
tMouseOwner(null\
)};a.Swing={coun\
t:0,menuInitiali\
zed:0,menuCounte\
r:0,htDialogs:{}\
};var k=a.Swing;\
SwingController=\
k;k.setDraggable\
=function(b){b=b\
.prototype;b.set\
Container||(b.se\
tContainer=funct\
ion(b){this.cont\
ainer=b;b.obj=th\
is;this.ignoreMo\
use=this.isDragg\
ing=!1;var e=thi\
s;b.bind(\x22moused\
own touchstart\x22,\
function(b){if(e\
.ignoreMouse)ret\
urn e.ignoreMous\
e=!1,!0;a._setMo\
useOwner(e,!0);e\
.isDragging=!0;e\
.pageX=b.pageX;e\
.pageY=b.pageY;r\
eturn!1});b.bind\
(\x22mousemove touc\
hmove\x22,function(\
b){if(e.isDraggi\
ng&&\x0aa._mouseOwn\
er==e)return e.m\
ouseMove(b),!1})\
;b.bind(\x22mouseup\
 touchend\x22,funct\
ion(b){e.mouseUp\
(b);a._setMouseO\
wner(null)})},b.\
mouseUp=function\
(b){if(this.isDr\
agging&&a._mouse\
Owner==this)retu\
rn this.pageX0+=\
b.pageX-this.pag\
eX,this.pageY0+=\
b.pageY-this.pag\
eY,this.isDraggi\
ng=!1;a._setMous\
eOwner(null)},b.\
setPosition=func\
tion(){if(null==\
=a._mousePageX){\
var b=a.$offset(\
this.applet._id+\
\x22_\x22+(this.applet\
._is2D?\x22canvas2d\
\x22:\x22canvas\x22));a._\
mousePageX=b.lef\
t;a._mousePageY=\
b.top}this.pageX\
0=a._mousePageX;\
this.pageY0=\x0aa._\
mousePageY;this.\
container.css({t\
op:a._mousePageY\
+\x22px\x22,left:a._mo\
usePageX+\x22px\x22})}\
,b.mouseMove=fun\
ction(b){if(this\
.isDragging&&a._\
mouseOwner==this\
){this.timestamp\
=System.currentT\
imeMillis();var \
e=this.pageX0+(b\
.pageX-this.page\
X);b=this.pageY0\
+(b.pageY-this.p\
ageY);a._mousePa\
geX=e;a._mousePa\
geY=b;this.conta\
iner.css({top:b+\
\x22px\x22,left:e+\x22px\x22\
})}},b.dragBind=\
function(b){this\
.applet._ignoreM\
ouse=!b;this.con\
tainer.unbind(\x22m\
ousemoveoutjsmol\
\x22);this.containe\
r.unbind(\x22touchm\
oveoutjsmol\x22);th\
is.container.unb\
ind(\x22mouseupoutj\
smol\x22);\x0athis.con\
tainer.unbind(\x22t\
ouchendoutjsmol\x22\
);a._setMouseOwn\
er(null);if(b){v\
ar e=this;this.c\
ontainer.bind(\x22m\
ousemoveoutjsmol\
 touchmoveoutjsm\
ol\x22,function(b,a\
,f){e.mouseMove(\
f)});this.contai\
ner.bind(\x22mouseu\
poutjsmol touche\
ndoutjsmol\x22,func\
tion(b,a,f){e.mo\
useUp(f)})}})};k\
.JSDialog=functi\
on(){};k.setDrag\
gable(k.JSDialog\
);k.getScreenDim\
ensions=function\
(b){b.width=h(wi\
ndow).width();b.\
height=h(window)\
.height()};k.dis\
pose=function(b)\
{a.$remove(b.id+\
\x22_mover\x22);delete\
 k.htDialogs[b.i\
d];b.container.o\
bj.dragBind(!1)}\
;\x0ak.register=fun\
ction(b,a){b.id=\
a+ ++k.count;k.h\
tDialogs[b.id]=b\
};k.setDialog=fu\
nction(b){a._set\
MouseOwner(null)\
;a.$remove(b.id)\
;var e=b.id+\x22_mo\
ver\x22,c=a._$(e),d\
;c[0]?(c.html(b.\
html),d=c[0].jd)\
:(a.$after(\x22body\
\x22,\x22<div id='\x22+e+\
\x22' style='positi\
on:absolute;left\
:0px;top:0px;'>\x22\
+b.html+\x22</div>\x22\
),d=new k.JSDial\
og,c=a._$(e),b.c\
ontainer=c,d.app\
let=b.manager.vw\
r.html5Applet,d.\
setContainer(c),\
d.dialog=b,d.set\
Position(),d.dra\
gBind(!0),c[0].j\
d=d);a.$bind(\x22#\x22\
+b.id+\x22 .JButton\
\x22,\x22mousedown tou\
chstart\x22,functio\
n(){d.ignoreMous\
e=\x0a!0});a.$bind(\
\x22#\x22+b.id+\x22 .JCom\
boBox\x22,\x22mousedow\
n touchstart\x22,fu\
nction(){d.ignor\
eMouse=!0});a.$b\
ind(\x22#\x22+b.id+\x22 .\
JCheckBox\x22,\x22mous\
edown touchstart\
\x22,function(){d.i\
gnoreMouse=!0});\
a.$bind(\x22#\x22+b.id\
+\x22 .JTextField\x22,\
\x22mousedown touch\
start\x22,function(\
){d.ignoreMouse=\
!0});a.$bind(\x22#\x22\
+b.id+\x22 .JTable\x22\
,\x22mousedown touc\
hstart\x22,function\
(){d.ignoreMouse\
=!0});a.$bind(\x22#\
\x22+b.id+\x22 .JScrol\
lPane\x22,\x22mousedow\
n touchstart\x22,fu\
nction(){d.ignor\
eMouse=!0});a.$b\
ind(\x22#\x22+b.id+\x22 .\
JEditorPane\x22,\x22mo\
usedown touchsta\
rt\x22,function(){d\
.ignoreMouse=\x0a!0\
})};k.setSelecte\
d=function(b){a.\
$prop(b.id,\x22chec\
ked\x22,!!b.selecte\
d)};k.setSelecte\
dIndex=function(\
b){a.$prop(b.id,\
\x22selectedIndex\x22,\
b.selectedIndex)\
};k.setText=func\
tion(b){a.$prop(\
b.id,\x22value\x22,b.t\
ext)};k.setVisib\
le=function(b){a\
.$setVisible(b.i\
d,b.visible)};k.\
setEnabled=funct\
ion(b){a.$setEna\
bled(b.id,b.enab\
led)};k.click=fu\
nction(b,e){var \
c=k.htDialogs[b.\
id];if(c){var d=\
c.toString();if(\
0<=d.indexOf(\x22JC\
heck\x22))c.selecte\
d=b.checked;else\
 if(0<=d.indexOf\
(\x22JCombo\x22))c.sel\
ectedIndex=b.sel\
ectedIndex;else \
if(null!=\x0ac.text\
&&(c.text=b.valu\
e,e&&13!=(e.char\
Code||e.keyCode)\
))return}d=k.htD\
ialogs[a.$getAnc\
estorDiv(b.id,\x22J\
Dialog\x22).id];d.m\
anager.actionPer\
formed(c?c.name:\
d.registryKey+\x22/\
\x22+b.id)};k.setFr\
ont=function(b){\
var e=b.manager.\
vwr.html5Applet;\
b.zIndex!=a._get\
Z(e,\x22dialog\x22)&&(\
b.zIndex=a._incr\
Z(e,\x22dialog\x22));b\
.container&&((b.\
container[0]||b.\
container).style\
.zIndex=b.zIndex\
)};k.hideMenus=f\
unction(b){if(b=\
b._menus)for(var\
 a in b)b[a].vis\
ible&&k.hideMenu\
(b[a])};k.window\
Closing=function\
(b){b=k.htDialog\
s[a.$getAncestor\
Div(b.id,\x0a\x22JDial\
og\x22).id];b.regis\
tryKey?b.manager\
.processWindowCl\
osing(b.registry\
Key):b.dispose()\
};a._track=funct\
ion(b){if(a._tra\
cker){try{var e=\
'<iframe style=\x22\
display:none\x22 wi\
dth=\x220\x22 height=\x22\
0\x22 frameborder=\x22\
0\x22 tabindex=\x22-1\x22\
 src=\x22'+(a._trac\
ker+\x22&applet=\x22+b\
._jmolType+\x22&ver\
sion=\x22+a._versio\
n+\x22&appver=\x22+a._\
__JmolVersion+\x22&\
url=\x22+encodeURIC\
omponent(documen\
t.location.href)\
)+'\x22></iframe>';\
a.$after(\x22body\x22,\
e)}catch(c){}del\
ete a._tracker}r\
eturn b};var l;a\
.getProfile=func\
tion(b){if(self.\
Clazz&&self.JSON\
)return l||Clazz\
._startProfiling\
(l=\x0a0==arguments\
.length||b),Claz\
z.getProfile()};\
a._getInChIKey=f\
unction(b,a){0<=\
a.indexOf(\x22MOL=\x22\
)&&a.split(\x22MOL=\
\x22)[1].split('\x22')\
};a._getAttr=fun\
ction(b,a){var e\
=b.indexOf(a+\x22=\x22\
);return 0<=e&&0\
<=(e=b.indexOf('\
\x22',e))?b.substri\
ng(e+1,b.indexOf\
('\x22',e+1)):null}\
;a.User={viewUpd\
atedCallback:nul\
l};a.View={count\
:0,applets:{},se\
ts:{}};(function\
(b){b.updateView\
=function(e,c){i\
f(null!=e._viewS\
et){c.chemID||(e\
._searchQuery=nu\
ll);c.data||(c.d\
ata=\x22N/A\x22);c.typ\
e=e._viewType;if\
(null==(e._curre\
ntView=b.__findV\
iew(e._viewSet,\x0a\
c)))e._currentVi\
ew=b.__createVie\
wSet(e._viewSet,\
c.chemID,c.viewI\
D||c.chemID);e._\
currentView[c.ty\
pe].data=c.data;\
e._currentView[c\
.type].smiles=e.\
_getSmiles();a.U\
ser.viewUpdatedC\
allback&&a.User.\
viewUpdatedCallb\
ack(e,\x22updateVie\
w\x22);b.__setView(\
e._currentView,e\
,!1)}};b.updateF\
romSync=function\
(e,c){e._updateM\
sg=c;var d=a._ge\
tAttr(c,\x22sourceI\
D\x22)||a._getAttr(\
c,\x22file\x22);if(d){\
var g=b.__findVi\
ew(e._viewSet,{v\
iewID:d});if(nul\
l==g)return a.up\
dateView(e,c);g!\
=e._currentView&\
&b.__setView(g,e\
,!0);var h=(d=a.\
_getAttr(c,\x0a\x22ato\
ms\x22))&&0<=c.inde\
xOf(\x22selectionha\
los ON\x22)?eval(\x22[\
\x22+d+\x22]\x22):[];setT\
imeout(function(\
){e._currentView\
==g&&b.updateAto\
mPick(e,h)},10);\
a.User.viewUpdat\
edCallback&&a.Us\
er.viewUpdatedCa\
llback(e,\x22update\
FromSync\x22)}};b.u\
pdateAtomPick=fu\
nction(b,e){var \
d=b._currentView\
;if(null!=d){for\
(var g in d)\x22inf\
o\x22!=g&&d[g].appl\
et!=b&&d[g].appl\
et._updateAtomPi\
ck(e);a.User.vie\
wUpdatedCallback\
&&a.User.viewUpd\
atedCallback(b,\x22\
updateAtomPick\x22)\
}};b.dumpViews=f\
unction(a){var e\
=b.sets[a];if(e)\
{var d=\x22View set\
 \x22+a+\x22:\x5cn\x22;a=b.a\
pplets[a];\x0afor(v\
ar g in a)d+=\x22\x5cn\
applet \x22+a[g]._i\
d+\x22 currentView=\
\x22+(a[g]._current\
View?a[g]._curre\
ntView.info.view\
ID:null);for(g=e\
.length;0<=--g;)\
{a=e[g];var d=d+\
(\x22\x5cn\x5cn<b>view=\x22+\
g+\x22 viewID=\x22+a.i\
nfo.viewID+\x22 che\
mID=\x22+a.info.che\
mID+\x22</b>\x5cn\x22),h,\
m;for(m in a)\x22in\
fo\x22!=m&&(d+=\x22\x5cnv\
iew=\x22+g+\x22 type=\x22\
+m+\x22 applet=\x22+((\
h=a[m]).applet?h\
.applet._id:null\
)+\x22 SMILES=\x22+h.s\
miles+\x22\x5cn atomMa\
p=\x22+JSON.stringi\
fy(h.atomMap)+\x22\x5c\
n data=\x5cn\x22+h.dat\
a+\x22\x5cn\x22)}return d\
}};b.__init=func\
tion(a){var e=a.\
_viewSet,d=b.app\
lets;d[e]||(d[e]\
={});d[e][a._vie\
wType]=\x0aa};b.__f\
indView=function\
(a,e){var d=b.se\
ts[a];null==d&&(\
d=b.sets[a]=[]);\
for(var g=d.leng\
th;0<=--g;){var \
h=d[g];if(e.view\
ID){if(h.info.vi\
ewID==e.viewID)r\
eturn h}else{if(\
null!=e.chemID&&\
e.chemID==h.info\
.chemID)return h\
;for(var m in h)\
if(\x22info\x22!=m&&(n\
ull!=e.data&&nul\
l!=h[m].data?e.d\
ata==h[m].data:e\
.type==m))return\
 h}}return null}\
;b.__createViewS\
et=function(e,c,\
d){b.count++;c={\
info:{chemID:c,v\
iewID:d||\x22model_\
\x22+b.count}};for(\
var g in a._appl\
ets)d=a._applets\
[g],d._viewSet==\
e&&(c[d._viewTyp\
e]={applet:d,\x0ada\
ta:null});b.sets\
[e].push(c);retu\
rn c};b.__setVie\
w=function(b,a,e\
){for(var d in b\
)if(\x22info\x22!=d){v\
ar g=b[d],h=g.ap\
plet,m=e||null!=\
h&&\x22<modified>\x22=\
=h._molData;if(!\
(null==h||h==a&&\
!m)){var j=null=\
=g.data,k=null!=\
h._currentView;h\
._currentView=b;\
if(!k||!(b[d].da\
ta==g.data&&!j&!\
m))if(h._loadMod\
elFromView(b),j)\
break}}}})(a.Vie\
w);a.Cache={file\
Cache:{}};a.Cach\
e.get=function(b\
){return a.Cache\
.fileCache[b]};a\
.Cache.put=funct\
ion(b,e){a.Cache\
.fileCache[b]=e}\
;a.Cache.setDrag\
Drop=function(b)\
{a.$appEvent(b,\x22\
appletdiv\x22,\x0a\x22dra\
gover\x22,function(\
b){b=b.originalE\
vent;b.stopPropa\
gation();b.preve\
ntDefault();b.da\
taTransfer.dropE\
ffect=\x22copy\x22});a\
.$appEvent(b,\x22ap\
pletdiv\x22,\x22drop\x22,\
function(e){var \
c=e.originalEven\
t;c.stopPropagat\
ion();c.preventD\
efault();var d=c\
.dataTransfer.fi\
les[0];if(null==\
d)try{d=\x22\x22+c.dat\
aTransfer.getDat\
a(\x22text\x22),(0==d.\
indexOf(\x22file:/\x22\
)||0==d.indexOf(\
\x22http:/\x22))&&b._s\
criptLoad(d)}cat\
ch(g){}else c=ne\
w FileReader,c.o\
nloadend=functio\
n(c){if(c.target\
.readyState==Fil\
eReader.DONE){va\
r g=\x22cache://DRO\
P_\x22+d.name;c=Cla\
zz.newByteArray(\
-1,\x0ac.target.res\
ult);g.endsWith(\
\x22.spt\x22)||b._appl\
etPanel.cacheFil\
eByName(\x22cache:/\
/DROP_*\x22,!1);\x22JS\
V\x22==b._viewType|\
|g.endsWith(\x22.jd\
x\x22)?a.Cache.put(\
g,c):b._appletPa\
nel.cachePut(g,c\
);(c=a._jsGetXY(\
b._canvas,e))&&(\
!b._appletPanel.\
setStatusDragDro\
pped||b._appletP\
anel.setStatusDr\
agDropped(0,c[0]\
,c[1],g))&&b._ap\
pletPanel.openFi\
leAsyncSpecial(g\
,1)}},c.readAsAr\
rayBuffer(d)})}}\
)(Jmol,jQuery);J\
mol._debugCode=!\
1;Jmol._grabberO\
ptions=[[\x22$\x22,\x22NC\
I(small molecule\
s)\x22],[\x22:\x22,\x22PubCh\
em(small molecul\
es)\x22]];Jmol.say=\
function(a){aler\
t(a)};\x0aJmol._TMA\
pplet=function(a\
,h,e){this._uniq\
ueId=(\x22\x22+Math.ra\
ndom()).substrin\
g(3);this._id=a;\
this._is2D=!0;th\
is._isJava=!1;th\
is._ready=!0;thi\
s._mouseDown=!1;\
this._jmolType=\x22\
Jmol._Canvas2D (\
TwirlyMol)\x22;if(e\
)return this;thi\
s._createCanvas(\
a,h);return this\
};\x0aJmol._TMApple\
t._getApplet=fun\
ction(a,h,e){if(\
!Jmol.featureDet\
ection.allowHTML\
5)return null;e|\
|(e=!1);h||(h={}\
);Jmol._addDefau\
ltInfo(h,{color:\
\x22#FFFFFF\x22,width:\
300,height:300,a\
ddSelectionOptio\
ns:!1,serverURL:\
\x22http://your.ser\
ver.here/jsmol.p\
hp\x22,defaultModel\
:\x22\x22,readyFunctio\
n:null,use:\x22HTML\
5\x22,bondWidth:5,s\
hadeAtoms:!1,zoo\
mScaling:1.5,pin\
chScaling:2,mous\
eDragFactor:0.5,\
touchDragFactor:\
0.15,multipleBon\
dSpacing:4,spinR\
ateX:0,spinRateY\
:0.5,spinFPS:20,\
spin:!1,noscript\
:!0,debug:!1});h\
=new Jmol._TMApp\
let(a,h,\x0ae);retu\
rn e?h:Jmol._reg\
isterApplet(a,h)\
};Jmol.getTMAppl\
et=Jmol._TMApple\
t._getApplet;\x0a(f\
unction(a){a._CP\
K=\x22#FF1493 #FFFF\
FF #D9FFFF #CC80\
FF #C2FF00 #FFB5\
B5 #909090 #3050\
F8 #FF0D0D #90E0\
50 #B3E3F5 #AB5C\
F2 #8AFF00 #BFA6\
A6 #F0C8A0 #FF80\
00 #FFFF30 #1FF0\
1F #80D1E3 #8F40\
D4 #3DFF00 #E6E6\
E6 #BFC2C7 #A6A6\
AB #8A99C7 #9C7A\
C7 #E06633 #F090\
A0 #50D050 #C880\
33 #7D80B0 #C28F\
8F #668F8F #BD80\
E3 #FFA100 #A629\
29 #5CB8D1 #702E\
B0 #00FF00 #94FF\
FF #94E0E0 #73C2\
C9 #54B5B5 #3B9E\
9E #248F8F #0A7D\
8C #006985 #C0C0\
C0 #FFD98F #A675\
73 #668080 #9E63\
B5 #D47A00 #9400\
94 #429EB0 #5717\
8F #00C900\x22.spli\
t(\x22 \x22);a._elem=\x22\
X H He Li Be B C\
 N O F Ne Na Mg \
Al Si P S Cl Ar \
K Ca Sc Ti V Cr \
Mn Fe Co Ni Cu Z\
n Ga Ge As Se Br\
 Kr Rb Sr Y Zr N\
b Mo Tc Ru Rh Pd\
 Ag Cd In Sn Sb \
Te I Xe Cs Ba La\
 Ce Pr Nd Pm Sm \
Eu Gd Tb Dy Ho E\
r Tm Yb Lu Hf Ta\
 W Re Os Ir Pt A\
u Hg Tl Pb Bi Po\
 At Rn Fr Ra Ac \
Th Pa U Np Pu Am\
 Cm Bk Cf Es\x22.sp\
lit(\x22 \x22);\x0aa._ele\
mNo={};var h=a.p\
rototype;h.spin=\
function(a){this\
.__Info.spin=a;t\
his._spin(a)};h.\
_spin=function(a\
){this._spinThre\
ad&&clearTimeout\
(this._spinThrea\
d);if(0==this.sp\
inFPS||0==this.s\
pinRateX&&0==thi\
s.spinRateY)a=!1\
;if(a){var d=thi\
s;a=1E3/this.spi\
nFPS;this._mouse\
Down||(this._rot\
ate(this.spinRat\
eY,this.spinRate\
X),this._draw())\
;this._spinThrea\
d=setTimeout(fun\
ction(){d._spin(\
!0)},a)}};h._ini\
tParams=function\
(){this.zoom=thi\
s.__Info.default\
Zoom||100;this.d\
oSpin=this.__Inf\
o.spin||!1;this.\
center2D=[this._\
canvas.width/\x0a2,\
this._canvas.hei\
ght/2,0];this._g\
etCenterAndRadiu\
s();this.rotatio\
n=new a.M3;this.\
shadeAtoms=!1;th\
is._setParams()}\
;h._setParams=fu\
nction(){this.bo\
ndWidth=this.__I\
nfo.bondWidth||5\
;this.zoomScalin\
g=this.__Info.zo\
omScaling||1.5;t\
his.pinchScaling\
=this.__Info.pin\
chScaling||1;thi\
s.mouseDragFacto\
r=this.__Info.mo\
useDragFactor||0\
.5;this.touchDra\
gFactor=this.__I\
nfo.touchDragFac\
tor||0.15;this.m\
ultipleBondSpaci\
ng=this.__Info.m\
ultipleBondSpaci\
ng||4;this.spinR\
ateX=this.__Info\
.spinRateX||0;th\
is.spinRateY=thi\
s.__Info.spinRat\
eY||\x0a0;this.spin\
FPS=this.__Info.\
spinFPS||0;var a\
=this.shadeAtoms\
;(this.shadeAtom\
s=this.__Info.sh\
adeAtoms||!1)&&!\
a&&this._setAtom\
Shades()};h._set\
AtomShades=funct\
ion(){if(this.at\
oms)for(var a=th\
is.atoms.length;\
0<=--a;)this.ato\
ms[a].color50=th\
is._getColor(thi\
s.atoms[a].color\
,0.5)};h._create\
Canvas=function(\
a,d){Jmol._setOb\
ject(this,a,d);t\
his._color=this.\
_color.replace(/\
0x/,\x22#\x22);var g=J\
mol._getWrapper(\
this,!0);Jmol._d\
ocument?(Jmol._d\
ocumentWrite(g),\
this._createCanv\
as2d(!1),g=\x22\x22):g\
+='<script type=\
\x22text/javascript\
\x22>'+\x0aa+\x22._create\
Canvas2d(false)\x5c\
x3c/script>\x22;g+=\
Jmol._getWrapper\
(this,!1);d.addS\
electionOptions&\
&(g+=Jmol._getGr\
abberOptions(thi\
s,\x22\x22));Jmol._deb\
ugAlert&&!Jmol._\
document&&alert(\
g);this._code=Jm\
ol._documentWrit\
e(g)};h._createC\
anvas2d=function\
(a){var d=docume\
nt.createElement\
(\x22canvas\x22),g=Jmo\
l.$(this,\x22applet\
div\x22);a&&(g[0].r\
emoveChild(this.\
_canvas),Jmol._j\
sUnsetMouse(this\
._canvas));a=Mat\
h.round(g.width(\
));var h=Math.ro\
und(g.height());\
d.applet=this;th\
is._canvas=d;d.s\
tyle.width=\x22100%\
\x22;d.style.height\
=\x22100%\x22;d.width=\
\x0aa;d.height=h;d.\
id=this._id+\x22_ca\
nvas2d\x22;g.append\
(d);setTimeout(t\
his._id+\x22._start\
()\x22,10)};h._star\
t=function(){Jmo\
l._jsSetMouse(th\
is._canvas);this\
._defaultModel?J\
mol._search(this\
,this._defaultMo\
del,this._readyS\
cript?this._read\
yScript:\x22\x22):this\
._src&&this._loa\
dFile(this._src)\
;this._showInfo(\
!0);this._showIn\
fo(!1)};h._searc\
h=function(a,d){\
Jmol._search(thi\
s,a,d)};h._searc\
hDatabase=functi\
on(a,d,g){this._\
showInfo(!1);0<=\
a.indexOf(\x22?\x22)?J\
mol._getInfoFrom\
Database(this,d,\
a.split(\x22?\x22)[0])\
:this._loadFile(\
d+a,g)};\x0ah.__loa\
dModel=function(\
a){this._spin(!1\
);\x22''\x22==a&&(a=th\
is._mol);a?(this\
._parse(a),this.\
_initParams(),th\
is._draw(),this.\
_showInfo(!1),th\
is.doSpin&&this.\
_spin(!0)):alert\
(\x22No model data.\
\x22)};h._showInfo=\
function(a){Jmol\
.$html(Jmol.$(th\
is,\x22infoheadersp\
an\x22),this._infoH\
eader);this._inf\
o&&Jmol.$html(Jm\
ol.$(this,\x22infod\
iv\x22),this._info)\
;!this._isInfoVi\
sible!=!a&&(this\
._isInfoVisible=\
a,Jmol.$setVisib\
le(Jmol.$(this,\x22\
infotablediv\x22),a\
),Jmol.$setVisib\
le(Jmol.$(this,\x22\
infoheaderdiv\x22),\
a),this._show(!a\
))};h._show=func\
tion(a){Jmol.$se\
tVisible(Jmol.$(\
this,\x0a\x22appletdiv\
\x22),a);a&&this._d\
raw()};h._resize\
=function(){var \
a=\x22__resizeTimeo\
ut_\x22+this._id;Jm\
ol[a]&&clearTime\
out(Jmol[a]);var\
 d=this;Jmol[a]=\
setTimeout(funct\
ion(){d._draw();\
Jmol[a]=null},10\
0)};h._canScript\
=function(){retu\
rn!0};h._script=\
function(a){for(\
var d=a.split(\x22;\
\x22),g=0;g<d.lengt\
h;g++)a=d[g].tri\
m(),\x22image\x22==a?w\
indow.open(this.\
_canvas.toDataUR\
L(\x22image/png\x22)):\
0==a.indexOf(\x22lo\
ad \x22)?this._load\
File(a.substring\
(5).trim()):0==a\
.indexOf(\x22spin \x22\
)&&this.spin(0>a\
.toLowerCase().i\
ndexOf(\x22off\x22))};\
h._loadFile=\x0afun\
ction(a){this._s\
howInfo(!1);this\
._thisJmolModel=\
a;var d=this;Jmo\
l._loadFileData(\
this,a,function(\
a){d.__loadModel\
(a)})};h._proces\
sEvent=function(\
a,d){switch(a){c\
ase 502:case 503\
:this._mouseDown\
=!1;default:retu\
rn;case 501:this\
._mouseX=d[0];th\
is._mouseY=d[1];\
this._mouseDown=\
!0;return;case 5\
06:var g=d[0]-th\
is._mouseX,h=d[1\
]-this._mouseY,g\
=0>g?-1:0<g?1:0,\
h=0>h?-1:0<h?1:0\
;switch(d[2]){ca\
se 17:this._zoom\
By(h);break;case\
 24:this.center2\
D[0]+=g;this.cen\
ter2D[1]+=h;brea\
k;default:this._\
rotate(g,h)}this\
._mouseX=\x0ad[0];t\
his._mouseY=d[1]\
;break;case -1:t\
his._zoomBy(d[1]\
)}this._draw()};\
h._processGestur\
e=function(e){if\
(!(2>e[0].length\
)){var d=e[0],g=\
e[1],h=d[0],j=d[\
g.length-1];e=h[\
0];var k=j[0],h=\
h[1],j=j[1],l=[k\
-e,j-h,0],b=a._l\
ength(l),f=g[0],\
c=g[g.length-1],\
g=f[0],q=c[0],f=\
f[1],c=c[1],p=[q\
-g,c-f,0],r=a._l\
ength(p);3>b||3>\
r||(a._scale(l,1\
/b),a._scale(p,1\
/r),l=a._dot(l,p\
),0.8<l?(e=Math.\
round(k-d[d.leng\
th-2][0]),d=Math\
.round(j-d[d.len\
gth-2][1]),this.\
center2D[0]+=e,t\
his.center2D[1]+\
=d):-0.8>l&&(l=[\
g-e,f-h,0],p=[q-\
\x0ak,c-j,0],d=a._l\
ength(p)-a._leng\
th(l),this.zoom+\
=(0>d?-1:1)*this\
.pinchScaling),t\
his._draw())}};h\
._zoomBy=functio\
n(a){this.zoom+=\
a*this.zoomScali\
ng;5>this.zoom&&\
(this.zoom=5);50\
0<this.zoom&&(th\
is.zoom=500)};h.\
_getRotationScal\
ing=function(){r\
eturn[1/Math.max\
(this._canvas.wi\
dth,500)*this.mo\
useDragFactor*a.\
deg_per_radian,1\
/Math.max(this._\
canvas.height,50\
0)*this.mouseDra\
gFactor*a.deg_pe\
r_radian]};h._ro\
tate=function(e,\
d){var g=this._g\
etRotationScalin\
g();d&&(a._m3.ro\
tX(d*g[1]),this.\
rotation.mul(a._\
m3));e&&\x0a(a._m3.\
rotY(e*g[0]),thi\
s.rotation.mul(a\
._m3))};h._getCe\
nterAndRadius=fu\
nction(){Math.mi\
n(this._canvas.w\
idth,this._canva\
s.height);for(va\
r e=[999999,9999\
99,999999],d=[-9\
99999,-999999,-9\
99999],g=this.at\
oms.length;0<=--\
g;)for(var h=3;0\
<=--h;){var j=th\
is.atoms[g].xyz[\
h];j<e[h]&&(e[h]\
=j);j>d[h]&&(d[h\
]=j)}j=[0,0,0];f\
or(h=3;0<=--h;)j\
[h]=(d[h]+e[h])/\
2;e=0;for(g=this\
.atoms.length;0<\
=--g;)d=this.ato\
ms[g],d=a._dista\
nce(d.xyz,j)+(1=\
=d.elemNo?1:1.5)\
,d>e&&(e=d);this\
.center=j;this.m\
odelRadius=0==e?\
10:e};h._setScre\
enCoords=\x0afuncti\
on(){for(var a=t\
his.center,d=thi\
s.rotation,g=thi\
s.center2D,h=Mat\
h.min(this._canv\
as.width,this._c\
anvas.height)/2/\
this.modelRadius\
*this.zoom/100,j\
=this.atoms.leng\
th;0<=--j;){var \
k=this.atoms[j];\
this._transform(\
k.xyz,k.sxyz,a,d\
,h,g);k.srad=h*k\
.radius}for(j=th\
is.bonds.length;\
0<=--j;)k=this.b\
onds[j],this._tr\
ansform(k.xyz,k.\
sxyz,a,d,h,g),th\
is._transform(k.\
pts[0],k.spts[0]\
,a,d,h,g),this._\
transform(k.pts[\
1],k.spts[1],a,d\
,h,g)};h._transf\
orm=function(e,d\
,g,h,j,k){for(va\
r l=a._temp1,b=a\
._temp2,f=3;0<=\x0a\
--f;)l[f]=(e[f]-\
g[f])*j;h.transf\
orm(l,b);b[1]=-b\
[1];b[2]=-b[2];f\
or(f=3;0<=--f;)d\
[f]=b[f]+k[f]};h\
._parse=function\
(a){this._parseS\
DF(a)};h._parseS\
DF=function(e){t\
his._mol=e;if(!a\
._elemNo.H)for(v\
ar d=a._elem.len\
gth;0<=--d;)a._e\
lemNo[a._elem[d]\
]=d;e=e.split(\x22\x5c\
n\x22);var g=3,h=e[\
g++];this.nAtoms\
=parseFloat(h.su\
bstring(0,3));th\
is.nBonds=parseF\
loat(h.substring\
(3,6));this.atom\
s=Array(this.nAt\
oms);this.bonds=\
Array(this.nBond\
s);this.elements\
=Array(this.nAto\
ms+this.nBonds);\
for(var j=0,k,l,\
b,d=0;d<this.nAt\
oms;d++){h=\x0ae[g+\
+];k=parseFloat(\
h.substring(0,10\
));l=parseFloat(\
h.substring(10,2\
0));b=parseFloat\
(h.substring(20,\
30));var h=h.sub\
string(31,34).re\
place(/\x5cs+/g,\x22\x22)\
,h=a._elemNo[h]|\
|0,f=1==h?0.23:0\
.35,c=a._CPK[h]|\
|a._CPK[0];this.\
elements[j++]=th\
is.atoms[d]={typ\
e:0,elemNo:h,xyz\
:[k,l,b],sxyz:[0\
,0,0],radius:f,c\
olor:c,color50:c\
}}for(d=0;d<this\
.nBonds;d++){h=e\
[g++];k=this.ato\
ms[parseFloat(h.\
substring(0,3))-\
1];l=this.atoms[\
parseFloat(h.sub\
string(3,6))-1];\
b=Math.abs(parse\
Float(h.substrin\
g(6,9)));switch(\
b){case 4:case 5\
:case 6:case 8:b\
=\x0a1;break;case 7\
:b=2}h=a._getPoi\
ntAlong(k.xyz,l.\
xyz,0.5);c=a._di\
stance(k.xyz,h);\
f=k.radius<c?a._\
getPointAlong(k.\
xyz,h,k.radius/c\
):[0,0,99999];c=\
l.radius<c?a._ge\
tPointAlong(l.xy\
z,h,l.radius/c):\
[0,0,99999];this\
.elements[j++]=t\
his.bonds[d]={ty\
pe:1,atoms:[k,l]\
,xyz:h,pts:[f,c]\
,sxyz:[0,0,0],sp\
ts:[[0,0,0],[0,0\
,0]],order:b,col\
or:0}}};h._getCo\
lor=function(a,d\
){\x22#FFFFFF\x22==a&&\
(a=\x22#D0D0D0\x22);va\
r g=parseInt(\x220x\
\x22+a.substring(1)\
,16),h=g>>16&255\
,j=g>>8&255,g=g&\
255;255!=h&&(h+=\
Math.floor((255-\
h)*d));255!=j&&(\
j+=Math.floor((2\
55-\x0aj)*d));255!=\
g&&(g+=Math.floo\
r((255-g)*d));h=\
\x22000000\x22+(h<<16|\
j<<8|g).toString\
(16);return\x22#\x22+h\
.substring(h.len\
gth-6,h.length)}\
;h._draw=functio\
n(){if(this.atom\
s){this._setPara\
ms();this._setSc\
reenCoords();var\
 e=this.elements\
;e.sort(a._zorde\
r);var d=this._c\
anvas.getContext\
(\x222d\x22);d.fillSty\
le=this._color;d\
.fillRect(0,0,th\
is._canvas.width\
,this._canvas.he\
ight);for(var g=\
e.length;0<=--g;\
){var h=e[g];0==\
h.type?this._dra\
wAtom(d,h):this.\
_drawBond(d,h)}}\
};h._drawAtom=fu\
nction(e,d){e.be\
ginPath();if(thi\
s.shadeAtoms){va\
r g=\x0ad.srad/4,g=\
e.createRadialGr\
adient(d.sxyz[0]\
-g,d.sxyz[1]-g,g\
,d.sxyz[0],d.sxy\
z[1],d.srad);g.a\
ddColorStop(0,d.\
color50);g.addCo\
lorStop(1,\x22#FFFF\
FF\x22==d.color?\x22#D\
0D0D0\x22:d.color);\
e.fillStyle=g;e.\
arc(d.sxyz[0],d.\
sxyz[1],d.srad,0\
,a._pi2);e.fill(\
)}else e.fillSty\
le=d.color,e.arc\
(d.sxyz[0],d.sxy\
z[1],d.srad,0,a.\
_pi2),e.fill(),e\
.strokeStyle=\x22#0\
00000\x22,e.lineWid\
th=1,e.stroke()}\
;h._drawBond=fun\
ction(a,d){99999\
!=d.pts[0][2]&&t\
his._drawBondLin\
es(a,d,d.spts[0]\
,d.atoms[0].colo\
r);99999!=d.pts[\
1][2]&&this._dra\
wBondLines(a,\x0ad,\
d.spts[1],d.atom\
s[1].color)};h._\
drawBondLines=fu\
nction(e,d,g,h){\
var j=a._temp;j.\
width=this.bondW\
idth;j.color=d.c\
olor?d.color:h;i\
f(1==d.order)j.p\
t1=g,j.pt2=d.sxy\
z,this._drawLine\
(e,j);else{j.pt1\
=a._temp1;j.pt2=\
a._temp2;j.pta=g\
;j.ptb=d.sxyz;j.\
dx=j.ptb[0]-j.pt\
a[0];j.dy=j.ptb[\
1]-j.pta[1];j.ma\
g2d=Math.round(M\
ath.sqrt(j.dx*j.\
dx+j.dy*j.dy));j\
.bondOrder=d.ord\
er;for(this._res\
etAxisCoordinate\
s(j);0<j.bondOrd\
er;)this._drawLi\
ne(e,j),j.bondOr\
der--,this._step\
AxisCoordinates(\
j)}};h._drawLine\
=function(a,d){a\
.beginPath();\x0aa.\
strokeStyle=d.co\
lor;a.moveTo(d.p\
t1[0],d.pt1[1]);\
a.lineTo(d.pt2[0\
],d.pt2[1]);a.li\
neWidth=d.width;\
a.stroke()};h._r\
esetAxisCoordina\
tes=function(a){\
var d=a.mag2d>>3\
;1!=this.multipl\
eBondSpacing&&(d\
*=this.multipleB\
ondSpacing);d=a.\
width+d;a.dxStep\
=Math.round(d*a.\
dy/a.mag2d);a.dy\
Step=Math.round(\
d*-a.dx/a.mag2d)\
;a.pt1[0]=a.pta[\
0];a.pt1[1]=a.pt\
a[1];a.pt2[0]=a.\
ptb[0];a.pt2[1]=\
a.ptb[1];d=a.bon\
dOrder-1;a.pt1[0\
]-=Math.round(a.\
dxStep*d/2);a.pt\
1[1]-=Math.round\
(a.dyStep*d/2);a\
.pt2[0]-=Math.ro\
und(a.dxStep*d/2\
);a.pt2[1]-=\x0aMat\
h.round(a.dyStep\
*d/2)};h._stepAx\
isCoordinates=fu\
nction(a){a.pt1[\
0]+=a.dxStep;a.p\
t1[1]+=a.dyStep;\
a.pt2[0]+=a.dxSt\
ep;a.pt2[1]+=a.d\
yStep};a._distan\
ce=function(a,d)\
{for(var g=0,h=3\
;0<=--h;)var j=a\
[h]-d[h],g=g+j*j\
;return Math.sqr\
t(g)};a._dot=fun\
ction(a,d){for(v\
ar g=0,h=3;0<=--\
h;)g+=a[h]*d[h];\
return g};a._set\
Pt=function(a,d)\
{for(var g=3;0<=\
--g;)d[g]=a[g];r\
eturn d};a._scal\
e=function(a,d){\
for(var g=3;0<=-\
-g;)a[g]*=d};a._\
length=function(\
a){for(var d=0,g\
=3;0<=--g;)d+=a[\
g]*a[g];return M\
ath.sqrt(d)};a._\
getPointAlong=\x0af\
unction(a,d,g){r\
eturn[(d[0]-a[0]\
)*g+a[0],(d[1]-a\
[1])*g+a[1],(d[2\
]-a[2])*g+a[2]]}\
;a._zorder=funct\
ion(a,d){var g=a\
.sxyz[2],h=d.sxy\
z[2];return g<h?\
-1:g>h?1:0};a.M3\
=function(){this\
.m00=1;this.m10=\
this.m02=this.m0\
1=0;this.m11=1;t\
his.m21=this.m20\
=this.m12=0;this\
.m22=1};a.M3.pro\
totype.set=funct\
ion(a,d,g,h,j,k,\
l,b,f){this.m00=\
a;this.m01=d;thi\
s.m02=g;this.m10\
=h;this.m11=j;th\
is.m12=k;this.m2\
0=l;this.m21=b;t\
his.m22=f};a.M3.\
prototype.transf\
orm=function(a,d\
){d[0]=this.m00*\
a[0]+this.m01*a[\
1]+this.m02*a[2]\
;d[1]=\x0athis.m10*\
a[0]+this.m11*a[\
1]+this.m12*a[2]\
;d[2]=this.m20*a\
[0]+this.m21*a[1\
]+this.m22*a[2]}\
;a.M3.prototype.\
rotX=function(a)\
{var d=Math.cos(\
a);a=Math.sin(a)\
;this.m00=1;this\
.m10=this.m02=th\
is.m01=0;this.m1\
1=d;this.m12=-a;\
this.m20=0;this.\
m21=a;this.m22=d\
};a.M3.prototype\
.rotY=function(a\
){var d=Math.cos\
(a);a=Math.sin(a\
);this.m00=d;thi\
s.m01=0;this.m02\
=a;this.m10=0;th\
is.m11=1;this.m1\
2=0;this.m20=-a;\
this.m21=0;this.\
m22=d};a.M3.prot\
otype.mul=functi\
on(a){this.set(a\
.m00*this.m00+a.\
m01*this.m10+a.m\
02*this.m20,\x0aa.m\
00*this.m01+a.m0\
1*this.m11+a.m02\
*this.m21,a.m00*\
this.m02+a.m01*t\
his.m12+a.m02*th\
is.m22,a.m10*thi\
s.m00+a.m11*this\
.m10+a.m12*this.\
m20,a.m10*this.m\
01+a.m11*this.m1\
1+a.m12*this.m21\
,a.m10*this.m02+\
a.m11*this.m12+a\
.m12*this.m22,a.\
m20*this.m00+a.m\
21*this.m10+a.m2\
2*this.m20,a.m20\
*this.m01+a.m21*\
this.m11+a.m22*t\
his.m21,a.m20*th\
is.m02+a.m21*thi\
s.m12+a.m22*this\
.m22)};a._pi2=2*\
Math.PI;a.deg_pe\
r_radian=180/Mat\
h.PI;a._z3=[0,0,\
0];a._temp1=[0,0\
,0];a._temp2=[0,\
0,0];a._temp={};\
a._m3=new a.M3})\
(Jmol._TMApplet)\
;\x0a\
\x00\x00\x12i\
\x00\
\x00@\xc9x\xda\xb5<\xfdS\xdbH\xb2?'U\xf9\
\x1f&~\xbb\x07\xde\xb5e[\xfe\x02\x8c}\xc7\x02\xd9\
%\x05I6\x90\xdbw\xfb\xde\x155\x96\xc6\xf6\x80\xac\
\xd1jF`\x87\xe2\x7f\xbf\xee\x1e\xc9\x96\xc1$`\xfb\
\xb2\x85-\xcdGw\xcfL\x7f\xf7x\xf7\xdf\x1e}<\
\xbc\xf8\xd7\xa7c62\xe3\xa0\xf7\xe6\xf5~\xf6m\xa4\
\x09D\xef\xb7\x8b\xb3\xd3fY\x85\xc1\x94\xf1\xd0g\x7f\
\x88\xfe\xaf\xa7\xec\xfdX\x05\xecH\x8c\xd5~\xc5\x8e\xc2\
i\x82\xfb\xf8=\x16\x863o\xc4c-L\xb7\x90\x98\
Ay\xa7\x80\xedo\xcbe\xd6\x8f\x05\xbf\x96\xe1\x90\xa9\
\xc403\x12,\x90\xfd\x98\xc7S6P1\xf3E?\
\x19\x0e\xb1\xb7\x5c\xc6\x09\xda\x8be\x04\xc3\xa6\x91\xe8\x16\
\x8c\x98\x98\xca\x15\xbf\xe1\xb6\xb5\xc0t\xecu\x0bW\x7f\
%\x22\x9eV\xec\x97s\xa5\x0b\xbd\xfd\x8a\x1d\xf0\x5c\x00\
\xba\xf2\xfe\x1c\x16s\xf5;B8\x9e\x98u\x80\x1c\xaa\
X\xac3\xff \x8a\x02a\xd6\x83 \xd7[@hb\
\x15\xe8\x15a\x5c\xb9\xfa\x0a\xa0\xacC\xc1\x9a\xd4k\x15\
\xacu\x02g\x22L\x1e\xcdG\xc6\xadT\x80E\x83@\
\xdd\x22{\x9a[\xc5H B\xe1\x09\xad3\xfe\xb5\xa2\
q#b-U\xb8\xc7\xde\xbc~>\x1b\xa7\xe8/F\
\xb1X\x8b\xfe_O\x97\xec\xe1\xf7@\xd0\x10\x94h\xe7\
R\xea\x03=\x0d=\xd6e\x03\x1eh\xd1\x99\xf5\x0c\x85\
\xf9\x14\xab\x81\x0c\xc4v\x117#\x16\x9e\x8a}\x0d\xdf\
\x91\xe0\x86y<\x0843\xb0-\xb0\xfcX\xfa\xbe\x08\
\x19\xec\x08\xbe\x05\x8a\xfb\xc2g\xef\x01\x1f\x03\xd50R\
\xbeF\xa87<fW3\x9e\xafv\x10((\x0c\x96\
DL\x86\x0c\x95\x0e3\xbc\x1f\x88\x12\xeb\x0b\xd8v\x9c\
\x02#\x12-\xd8\xdf/\xbf\x9c\x1fw\xdf\x1f\xfc\xf3\x00\
Q\xd0\xcb\xf9\xc9\xaf\x1f\x8e\x8ff\xaf\xa4\xb2p\x06\x22\
\x805}\x06\xcd4\xc55%\xa1g\xe0l\xb69!\
-\xb2\xbb7\xaf_\xf9\xcaK\xc6\x224\x0e)2\x18\
\x95\xf6\xc2f\xf8\xecgV`\x12W\x09\x00\x0aE\x18\
m\xb7\x09v\xe38\x108+\x1d\x5cb\x05\xfb\xe0\xcb\
\x9bB\xd1\xd1f\x0a|\xd8\x87\x1d\x12q\xb7P\x8b&\
\x0c\x18\x13\xc0\xf5\x83D\x14\xde\xbc\x06\xd6\xb8\x7f\xf5\x0a\
\x09<\x09\x07\x0aP\x22\x1d\xb7\xd27\xa3=\xd6p\xab\
%x\x1b\x099\x1c\x99=V\xaf\xd2+\xa9\xc6={\
(\xf8\xee\xa9@\xc5{\xac\xf0?\xef\xaa\xf8_\x01\xdb\
\xbe\x9e\x84\xbe\x98\xfc\xc2\xb5\xd8cn\xb5j'~\xdd\
\xbb\x1b\xabP\x1a\x15\xffI\xdd{\xb5j\xf5\x1e;\xb8\
\xef\x9f\x8b@\xd0~|\x8c\xf0S\xef1\x13'\x04^\
\x8b\x18N\xee\xcb\xe7S@12&\xda\xabT\xbc\x91\
\x18\xc3\x125\xacM\x05|\xe0\x08?\xa9\xe0\xf6V\xae\
4~F\xa3\xc8>9\xf0D\xe4$HG\x81\x8e\x02\
\xdf\x19\x1cp\xc0\xc3a\xc2\x87\xd8>\x88\x0b%<\xf2\
\x0f\x1f/\x8e\xf7\xd8\xe9\xc7\xc3\x83\xd3\x93?\x0f.N\
>~`\x9f\x8f\x7f\xffr\xf2\xf9\xf8\x9c-\xb7$l\
[\x0b\xc1f\xfa\x96L\x913\x00&Lbq$\x8c\
]\x91\xa3\x93(R\xb1\xd1\xa7\x0aXS~\xe5\xd8\x88\
\xe7w\xc5\xe3O\x1c\xf7\xb9\x80\x02@\x84\x82\xd6\xca\x9a\
\x5cm[x\xfc\x0e8\x1dZ\xde\xe7\xb42\x8f\xa9S\
\xeas9\x0c\x85\x9f;\x0d_jd\xd5\xf7\xee\xf9)\
0\xfb\x99\xdd\xef\xc7\xfd'\xd0.y\xa6\xa6\xb2~\xdc\
\x05_\x0cx\x12\x18\x16\xaa[d7<\x06\x98F\x5c\
\xf7.\xe5\xd9=\x96gf:ATGs1\x9e\x9d\
^\xa5\xf2\xca\xf2\x22\x12\x03\xea\xeadl\xb7<T\xa1\
\xa0\x15d\xe3\x0b(o_\x95\x1a\x07<\x1e\x8aT\xe2\
\xb1\x8d\x87H\xa7\xe4\x1a\x08\x8f\x02>\xed\xa0\x0c3N\
\x9a\xc1\xe7\x86W<>\x18\x08\x19\x0a\x07H\xea\x14\x08\
\xe5\x02\xd0\x19\x80\xa3\x14\x006\xea\x91\xba5r\x0c\x14\
}\x17\xde\xabJ\xa5\x94\xee\xc9\x99\xf2E\x00`\xf7|\
\x15q\x98L\xf2\x03{V\x0aU~\xdd4\xc7\xcbv\
6]k~koe\x10\x80*\xc9\xeb\x9cK\x09\xd2\
\x07\x02Ks\xbfM\x7f\x9f{\xd7\xc3X%\xe0\x00\xdd\
\x8e\xa4\x11v\x05KiG\xe2\x80d>e\xf5\xfc\xb4\
\xa9\xc0\xe3\xea\xd8\x9e\xaaS{\x0c\x12M\xc86\xaaE\
\x09\x1a\x01\x14\xa2d\xfb\xac\x86\xdf?wk\xc5\xbbX\
\x19n\x04C\xa8\x19\x8cj\xed\x1e\xf0\xdd\xa3\x1e!%\
\x9f3\x19\x95\xcc\x19\xeb+\x7fJ\xbe\x1c2 #\x1d\
\xd3\x05\x15Pe\x1e\xd0\x13\x81\x12\x80\xe3\x80\x06\x1a\x12\
\xf7\xf6\x8d\xcf@\xb5\xe8\x88\x87]\x97\x91\x16\xeb\x16\x06\
\xe0\x14\x94\xb5\xfc*\xf6v\xac\xb1x\x07\x84r\xf6U\
F\x0c\xed\x01L\x08\x0d\x97!\x1aF`I\xf2\xea\xb0\
]\xa3\x1e7#`g_\x82\xb5\x00\x89\x98\x96@\xf1\
\xa1\xf0\xees\x06\x86n\xd0\xfd\x9ej\x01\x14\x15\x12o\
x\xe8\xbdd\xf0~\x85\xf7\x1c\x86\x9br\x81\x04\x18\xa1\
\x0d\x8b@\x0a\xd0~h\x96\x84\xc0Gr \xc1*Y\
B\xd1\xaf\xf5x\xc8\xe48\xb2Z\x9d\x16\xa1I\xcc\xad\
\xab\x9biylO\xc2e=\xb0'W\x09\xa0A;\
wn\xad-\x82%\xfd\x07\xfbnF8\x02\xbf\xd1\xf3\
%O\xc1\x12x\x18\x0b_\x1a\x8d\xee\x82\xf5\x1fdh\
D<\xe0\x1e\x9cV,\x8d\x01C\xda\x9f\xb2\xfd~\xef\
\x82_\xf3P\xc5\x92}\xc0\x07\xb1_\xe9\xd3\x12\x11\x9f\
\x9b\x22\x5c\x9c\xf0'\xa0b\x9fEx%yXb\xc8\
\xd5\x81\x83\xb3`\xceWp\xbb\x1f\x8c>0:\x19\xc9\
k\xc5\xfe\xc5\xc7<\x04\x14\x84\xc0Z\x7f8b\x9f\xce\
9\xf5m\xd0\xd0\xe7\xd6i\x01\xfc\xa2\xfa\xec7\x0e\x02\
\x18f\xa4!\x1f\x1a\x1f<\x11\xe0\xac9\x7f\xdd\x80`\
\x0d\xc3\xaeQQ/\xe5\xdb\x9c\xa3\x02\x02\x1b*`s\
3\xe2\xf6\x10@\x1e$\xb1n\xc8\xc7\x82\x9d}9\xbf\
`cn\xbcQ\xcaf1\x1dl\x0c}\xb0i\xc8p\
\x7f%0][\xc09Q\x07\x89\xca\xdc\x18\xdb\xb2]\
\xc8\xf5\x82\xa6@C\x5c|D\x01\xeacK\x9d&\x06\
\x01\xfd\xa1\x91=\xe4x\x0c\xa7\x06\xf2\x88A\xd1\x00Q\
#9\x97\x16\x1cS\xfd+\xe0wT\xe4\x1e\xa8p#\
|\x0b\x97\x08\xb0\xd0\xb6s\xc8K\x85\x9c&\x18\xc6\xa0\
l2\xf9n\xe6uD?\x80gtAPC\x04\x5c\
\xa3;6\x8eL\xb7\xdaY\x90|\x14y\xda\xedT\xc4\
\x0a9\x03\xf1\x14\x01[\xa9\xde\xdc*\x16z\xe9#\x0a\
\xd0\x0b\x81H43\x08\x82\x1e,\x80\xd4~\xbc\x10\xd2\
2\x0dl\xad\x13\x82\x1f\xc0\xdaE\xbc\x02\x81K\xc1\xa2\
\xed@\xa8\x1a\xbc\x8ch\x06\x96\xb6\x10\xfa\x0d\xe8\xe4\xf1\
y$\xc0\xda\xaf\x80l\x01\x00\xdb\x014\x8c|\xcc\xee\
\x16\xea\xc9\xd4e\xd1[\xbd\x9d\x15\x17\xb3\x08\xbf\x9d\x83\
\x1f\xaa\xf9JA/o\xf5\xda\x1bA\xd1ZDab\
\x10\xf7 \xf1D\xe8M\xb7z\xad\x8d\xa0h\xe6P\xe8\
\x84\xf4 \x18\x10\x05\x8a\xca\xdf\xea57\x82\xa2\x91C\
\xe1\xf1\xd8(`ypFp9\x9e\xd8\xea56\x82\
\xa4\x9eC2\x14j\xb6\x14N\xab\x81C\xafo\x04\x8d\
\x9bC\x03\x06]FZI?\x87\xc5\xdd\x08\x96Z\x0e\
\xcb-\x18\xf3\x01*\x5c\x8a\x80\xb7z\xb5\xbc\xc8\xa0C\
\xc5\x9eF\x06\x0e \xea\xd9\x05t$\x81$\x80\xea\xf6\
;\xc4z\x81\xe0q\xea=\xe7a\xa0\xda\xc2\xae\xef\xad\
u)z\xd2+\x00a$\xfdTi\xd9\xc5\xbcp\xcb\
0\x92b?uf\xfc\xa4\x06\x83\x0e\xb8Q\x9e\x18\xa0\
\xdfI[\x85\x8b\xccZV:\x96e8\xe6\xc7Q\x06\
\xa7\x12q`\xcb\xc6\xc0\xcf\x97\xe0\xd6\x7f\xcc!\x03\x5c\
(\xa9\xbd>h\xb2\xbfi#\xbd\xeb\xd5QF\xe0\xda\
\x82\x03\x8d\xfeQ\x98\xc0AJ/GC\xbaqY\xc3\
\x8a\xec\x9cN\x7f\xc7AS\xcdT\xfe\x00\xdf6\x01p\
f\x9a\xc0q\xd8\x18<\x0a\x99F\x22\x1eCh\x10\x88\
\x1b\x11\xb0*\x11\x0d\x82\xb92\x9bR\xd6\x00\xf7\x1b,\
\x9d\x01\xcf\xc5\xa8q\xa8\xac\xd5\xc7\x0e\xfb\xbe\xc2\x0a\xec\
t/\xba\x9e\xc3\x82\x97\x95\x01i8!\x0fm\xe3\x1c\
\xdc\xac)\xafmV\xe3o\xa93m\xccn\xfc[r\
X\x16ZVq}\xe6\x00\xc0w\x03W\x14\xa1\x82\xf8\
\xac\x02j\xc0\xb6\xef\xecAP\xf8w\xef\x80{\x8b\x96\
\x1c\xd3 \x10\xc0t!4,\xdey\xf0\x9e\x04\x18\x0f\
.\xf4\xde?X\x1c\xb8\xca\x11\x1b\x8b\x08\xc9\x81\xaf\xf5\
V6\xb7\xf6\x06\xe1\xe5^\xd7\x83\x0ba\xfd_V \
\xedS\xc6\xdd\xd9)\x07\xbc/\x02\xcd^\xbc\x8b\x97\x18\
\xdb]L#\xda\xb3\xbfa\x5c\xd0\xf9\xe4\xf7\xedC\xf1\
.c\x07\xe7\xf0\xa0C\x18\xd8\x8f\xe1\x8f\xf1=`\x12\
\xb3\xbe\xac\x83\xdfwfMDg\xb8\x8e~M\xd7\x03\
\xec\xb1:\x97`H\xce\x847R\xcc\xadBD\x12\xcb\
Ag\x80\x11z\xd7\xad\x92\xde\xa0.\x88\xb0\x18\x1e\x8f\
\x88;\xf4n\x1b!\x14F\xbc\xf8\xb2\x22{\xbe%T\
\xc5\xbb\x0c\xe3\xbd\xc5\xcd~\xee\xb2FgN\xd9?l\
\xab\xa5\x0eQR\x96)\xde0\xd22\x22\xc5\x01\xf6\x15\
E&\x1d\x04!_\x0d\x87-%\x88\x8c\xf1\x18\x8cW\
FP\x16\xab>\x0cP1\xf0\x8e\xa7\x14\x86\xaaD\xb3\
~b\x0c\x98!\x87\x9d\x0c\xc0\xc3\x9e\x9a\x11f=|\
%t\xb8\x05\xe1\xb7\x8a\xaf\xc1s\x12\x5c\xcfS\x1cc\
.\x03\xa3\xf6F\x14\x18\xc7\xff\x98'-z\x18)\x82\
%\xbd\x0e\xad\xdfC\xa19K\x95:\xfc\xd9\xf8\x193\
1O\xe6a\x0e\x938\xc6hT\x1b\x88$\xf4\x1ek\
\xb3\xf3\xe3O\xc0\x11\xb5:+\x13\xa4\x1e\x05\xef\x10\x87\
\x22eH\xa9\xa70\xc3Aa+\xc6\xef\xe5A,D\
\x89\xc5\xe2\xafD\xc6T\x95\xc3\xa2\x06\xa5,\xd2L\xc1\
\x05\x84\xb5\x00g\xc1\x1d$B\x15\xa5\x8c1\x17kX\
\x0d\xf3\x01\xb0\xef\x8c2\x92\x9aj!1\x8f\xa4\xcf(\
i\x85\xe3\xd4\x80\x8d1\x91g;3p\xdaF\xd9#\
~\x83\x85@\xb4t~>\xaf\xe0\xf1\x88\xf7e \xc1\
Tm\xcbO\xdc\xaf\xc8O#\x15\x02\xc1\x94\xcc2\xba\
h\x93\x0c\x9fT\x94\xa0\x9a\x0b\x93R\x1a\xac3P#\
\x09\xac\xa7\x04g\x04\xd1(R\x00]\x91\x84\xcf\x1b\xac\
7\xda\x86\xb1\xba\x11\xf6\xd3\xa8\x12\x1ba\xad\xa2D9\
\x9b\xeda\x02\xce\xa0_d!\xbf\x91\xc3tt\xc4\x13\
-*\x10\xaf%ph<\x16\x94\xebJ\xf7\x15Bp\
\xe40]Ie;k~\x1cn\xce'`\xf2s\x14\
\xab\x90\xb8J\x86XCB\xdc\xff{vj\xb3j\x98\
\xfc\xc5#\x99\xc1z\xf3:s\x82J\x0b\x91\x17\xac,\
\x0b.\xcae\xa2\x0a\xa9\xcbN\x1c\xfc*\xce4%\xb6\
\xd2\x5c\x94{\x84\xa9\x0c\x90:'-X\x01\x7f\x04B\
C\xc4\x80^\x06\xb8\x06~\xc9\xe6\xab(\x9d\xd5\x87\x00\
\xd2c\x10\x1dGi\x9e\x0c\xe3>11v\xeb\xdf\xbc\
>F\xfd\xc2\x0ao\x0b\xd4\xc9\x91\xc3\xc6\xf8$C\xe0\
\x09\xca\xa2\x81c\xee\x8dX_MhD\x14#\xaa\xe3\
\x0f\x17\xc7\x9f\x91k\xc4Dx\x09\x981\x8e\x02cP\
A\x98\xeee?\xe0\xe1\xf5\xf32\x84\xbe\xf2t/=\
\xf4\x145\x09\x13\xa6a\xd9~\x05\xc5\xa7\xb7 Si\
\x224\x9f\xfdl\xf6\x96\xa6\xa6\x80\xedA\xba|a\x05\
#\xad\x90\xa4B\xfa\x8a\xa5\xe0\xd8L\xd0Q\xb1\xba\xce\
\xc8\x8c\xe7\xe5\xa9\xde\xb2L!\x92\x87\x133z\x96O\
\xb7\x05\xad\xde\xf2\xe9\xdf\x9dM\x07\xdd\xa3\x12\x09\xdb\xb6\
\xa7\x8e\x92]|\x80\xfb)\xda\xff8\xfe\xe5\xd7\xd3l\
:\xf1\xc8\xc2LX>\xec\xcd\xb5\x98\x02\x8f\xf9\xe9\xf9\
\x0am\xf5E:\xe0\x1b\xd6\x9a\x86/\xea\xf7n\x96B\
\xff;\xaa\xe5\xf9\x1b\xdb\xfe|x\xfeK1\xb7\xe4\x17\
C\xae\xf5\x83\xc4B\xa5\xa7M@\xf4\xe20\x85\x88O\
\x0b\x10\x97\x9b\x10\xdc-\xcc\x83\x97}\x05\xd6 \xb4\xb5\
\xd2\xe7n\xd7\x12sH\xa5\x07ZO\x87-\x18\xfb@\
\x0c\x8c5\xf5\x81\xad\xfc\x90\xff\x87\xda\xc4q\x9c\x0e\x86\
nB\x8f\xf2.\xa2u\x86\x08\x94}\x04-\xaaG \
\xe2\x18\xf1\x11$\x5c\xe8\xf1\xd19\x01B.y\xee\xce\
=E6ULj^_;\x1ex\x05k\x92\xef\xab\
\xdbPsRm.\x035\x02\xbe\x14fMA\xd7$\
\xa1\x8f\x0a\xc7.j\x86\xf3\xd2\x1d\xa8\x81\xe7\x00\xd4%\
\xab\xcd\xc3\xcd\x94\xb5D\xfb\xce\x5c\xa7\xca\xee~\xba\x9f\
\xed\x87\xeb\xb8g\xbf\xb0\xe3\xa3\xb3\xdc\x8e\x90D\xb1\x95\
\xb6\x84\x98)\xc02\xe5\x82\xe2\xcf\x07:/\x83\x8a\xc5\
\x8d1\xb8\x09\xe4\xf5\xa7\xcf3\xf9}i`JV\xfb\
Z\x1a\xfc&\xd72\x82X\x9f\x9c\x9e\x98\x0f\xcfr\x98\
\xf0\xbd\x9cG\xf7Rlo\xc1\x091\x9d\x878s\xc1\
p\x86\x19lsh\xc8\xa3\xa4)k\xb0dj8\x88\
A\x06\x81\x98\x0c\xa4qtdl\x9c-&\x12-\xc5\
@\x9a\xd5\x8fb\xce\xf3~\xc8\x9d\xc8f\x09>M\xcf\
>\x9e\x02\xebk*\xa5\x94\x19tmD\xac\x80\x19\xc1\
\x9fp\xbcq\xd0\xb1Q(l$\xc4\x1cI \xdev\
k\x1d\xeb\xe7\xb0\xcaO\xcc\xc81\xf8=|\x22\xf5A\
8\x84\x15\xfeT\xc1Z\x22\xbbc\xe5fk\x97\x95\xdd\
V\x8b\xb5\xdb;\xac\xd6\xae:\xae{\x8f3\xb0F\x9c\
9\x1d\xd6\x9f\x839n\xad\xea\xec\xd0L\xfc\x83Q6\
\xd6(\xcd\x9c\xbe\xcf\xc0\xc7\xe0\xdc\xc0\xd0\xbb\x9a\xd3\xaa\
\xb9n\xbb\xdd\xdai\xedV\x1b\xed\x96\xcb\xeaN{\xa7\
\xdd\xae\xd7]x\xaba[\x9d\xe1\xa0\xea\xae\xdb\xaa7\
\xa9\xa1Uk\xdd\xb3Z\xcb\xa9\xef\xee\x02]\xcdZ}\
\xa7]m\xd6\x9b\x88i\xee\x97\xcd\x90\xe6\x88+\x81'\
\x13\x81\xff\x82\x88\x818V\xbdg\xbbNc\xa7\xb9[\
\xafV\x1b\xb5\xaa[s\x1b;\xb0\xcc\xaaSo\xc1\x1a\
\xdd\xb6\xbb\xdbl\xb6\xddV\x93U\x89\xa9\xe6\xdb\xb8\x0a\
\x17\xcf\x8f\x03\xc6F\xced\x1c \xcc\xecy=\x88\xb7\
\x10\xf0\xc7\xceD\xf9S|\xa5\x5c\xdfBK\xde7`\
\xeb\xc8\x02\xea5\x14\x84G\xf5'\x0a\xfcG\xa8\xa1\xd6\
\xb5\x06\xe4N#8zXe_\xac+\x8e \xec\xd3\
\x1a\xc4\x90\x1ey\xa4P^\x04\x01\xb4\x85\x85\x80\x0f\x1b\
\x11\xe7\x85{\x05\x18\xe1\x02\x87\x83\x07\xb1]d=\x90\
\xb8z\xf1.\x95\xe8\x1a\x19N\xca\x5c\xb0G\xc3\xdaE\
6\x1f\x17\xe3\x95\xa2{F#\xe7\xad`z\xef\x1f\x1d\
\xf47\xee)\x90Y\xa1\xc9\x9b_\xe6\xb2\xdc\x85\xa5\xa4\
\xe6T\xado\x90\x8d\xcf\xb5\xd3\xe5\x92\xec.\xd3\x88\x07\
\x0a\xf3\xc6Y\xca\xe6\xf2\xa3\x9d\xa7&\xd3\xa1\x08\x17f\
\xd9\xfe\x0f\xb6?\x94 \xf6\x8b#R\xa0\x0c/\x93\xd8\
A\x14$\xd2\xad6\x08f(_J\xa6\x0fgT\xa8\
o\x8d-\xc1\xba\xee\xa4\xfb\xe8\xe6In\xa7\xa6^\xa0\
Fb\xc2C\xf1.\x90\x91\x83\xb3;\x0f\xaf\xea\xb0.\
\x9btfQ/\x99R\x08]\x03\x19\xfa\xb1\x1a\x8b\x5c\
\x8f\x0a\x91\xf4\xd9\xfbf\xce\xb25j9x\x09\x8c\x95\
\xeb\x9d\xf4\xc2\xca\x84\xd5a\xaf#\xcc\xef\x87\x9dY\xf4\
\x9d\xa2\xc7\xf6\xca\xacq34(\x97H\x00\x83\x07\xc7\
\x05\x1f\xe7\xbf\x7f9\xf8||d\xd9v\xa1i3\xce\
\xechr\xebD\xe1\xd0zq\x0f[\xc9\xef\xda^\x1e\
\xdb.\x0c\x9cW\xcd\x8bk\x93\xa4\xffJx,.\x81\
\x1dB\x1e\x83\x1e\xe7\xb1\xe1\xe1\x22}K\x87ld?\
R\x934\xfd\xea\x0c\xbf.\xe2\xcc\xf7\xac\x81\xea+\x8f\
:\x11y\xee9\xf7^\xc3\xe69\xd4\x9a\xba\xf6\x83$\
\x08\xa6\x81\xb4~\xa2\x1d^x0\xb2\xb0\x18K?M\
\x05.\x01\xef\x03.\xd2\xf1H{-\xae6\xdf\xb3i\
D\xa5\xad\xc7Q\xdc\xe2\xa8\xab\x9bI`\xdb\x1f\x148\
\x0a\x0bC\x0a\xcf<\x87o\x10\x86Q\xb0\x13\xf9}\x22\
\x0a\xd3\xeeR\xbbG`u\x1e\x97\xaf2\xcb\xf3\xa8\xa7\
E\x1a<\x96\xfd\xbe\x0a\x0ft\x04*\xf73\xea\x03\xd6\
\xb8_,\x04v\x1e\xd4\x82:\x0fd.\xa5d\x03\xbb\
}]m\x80\xab\x881\xeaV\xca\xdbv3S\xe6\xba\
\xab\x81\xdd\xac\xdd/\xa2\x9f\xcf\xc9\xfa7q\xec\x81\xab\
\x9c!\x07v\xd5\x0f\xd8k\xde\xb1a4p\x8e\x14\x80\
\x81\x09ts'\x0a\x0eC>^\x9e\xbb\x11\x8c\xca\xc3\
\xa1\xc2\xce\xfbL\xeb\x22\xb1\xdbD\xed\xcfE\x96\xb6=\
\x97\xce\xa51\xed\x8c\xa2E\x84\x9dW\xf0\x1e$\x16a\
\xfa\xb8\x8a\xff\xb6\xb88[/\xd3\xa3\x15!\xe5\xe8\xa3\
PrV\xef\x9f\xaf}\x95`5\xf3\x8d\xc6S\xb2\x15\
\xec\xff \xb4\xf9w\xe7Q\xb3\x0d~\x9a\xd5\x5cv%\
\xeb\xb2\x9f9}\xd1W}4>9M1\xbf\xbb\xb5\
&u\xda\xe3\x01\xde\x13\xa0k\x02\x13|\xd8 X\xf0\
\xce,Xx\xd8 X7\x03\xebn\x08\xecb\x91\x8f\
e\xff\xd6\x86\xfb\xed\x83|\x9a'\xf2\xd5\xcb5I\xb0\
 kU{+\x01\x22f\xb3A\xb0\x96\xd2\xb1\xf47\
\x08\xb3j\xef\xabd7Uf2\xb8f\xde\x08\xbd\xf2\
\x01\xb8\xe3n\x969ZhX9\x11\xf6Tz+\xab\
\x0c\xb2\xa7s\xcd\xf6\xba5Q\xd7\xc7R$\xe5\x9b\xb7\
\x97\x91\x00<\x1f\x9b\xed\xad\xb3\xf3\x93c\xac\x09\x85\x0a\
f)\x96\xafLy\xb1\xd2\xb3\xc45\xa5')\xd12\
\xc0\x94\x8bV\x18oNU\xc2n9^\x99V8\x19\
\x0bz%j\x1cc\xf9(J\x0c\x9b\xfd,\x04\x8c8\
\xf6\xc4\xec\xe3\x1f\x1f\x98\xfd\x89\x89\xad\x09)i\xe7K\
\xc3\x12\xbc\xafH\xb7q\x9d\xd9\x8fPJ\x18xz#\
*\x1d\xd2\x85r\xba\xca\x0d\xdf[\xec\xe7\x07C\xa1a\
\xeb\xff\xc3\x03*Qe\xbf\xc4\xc2\xe2\xa3\x9d6Jo\
\xac\xc33\x96\x1d_\xfe\xc3\x16\xc7L\xe8d\x92\x90*\
f\xb8q\xe4\xb2?3\x9b\xbf\xdc\x02\xff\x90\xb9d3\
\x0b?ka\xdb Yc\xf6\xe1\xf0\xa4\xb8\x9e\x95\xa7\
\x1c?\x9a\xf6,L\xc4\xb3&\x87\xbc\xf3\xcc[X\x8f\
\x9c\xaf\xecB\xc3\x8cj\xc2\x91R\xfc\xb0\xcc\xb2\x12\xc9\
~\xab\xf5_'\x19pl\x90\xe4\x06H\xc7\x7f\x9bd\
\xc4\xb19\x92\xf7j\xbb;\xf5\x19pzc\xdb\x9f\x92\
\xfe!H\x05;<9Z\x17<\x87\x10?\x96\xf3\xe8\
3k\x98#\xc1\x8b\xfd\xebb\xd1c\xfc\x1d\xc7\xde\xe1\
a\xe5\xb0\x0b\x7f\x87st\x0f{\xe6x\xcf\xcfNN\
\x8f\xcf\x8bkE@?<\xc6\xf8C\x0e\x15\xc8\xed\x0b\
\xd1,+9\xee\xcd\xf4\xc3b\xdc\x97\xbb\xe0\xf5\xf0r\
\x96]\xfb\x5c\x8b\xa4kN\x0b\xfb0\xe1\xd9\x1b\xbe\x8c\
\xa0\x1f\xf2\x04=\xa7\xaeP\xdb\x81\xbf6\xa3\xdf\x1d\xd5\
\xda\xbbNk\xf7\xe9\xb2\x02\x8eJk\x0a\xf8\xf7\x9d\xc2\
B\xb9\xea4\x1a;\xed\xc6\xee\xec_\xb3\x81Y\xcb\x1d\
L\xf6\xcf\xff\xb9x;\xb6\xdaj\xba\xbb\xb9\x7f\xed{\
\xd6t\x9a\xf5V\xbb^sw\xeb\xadj\xad\xd1\xdc]\
\xa9\xbaPn8XX\xd8\xad\xee\xec\xee4\xean\xbb\
\x01\xe8jN\x1b\xdaj\xed\xe6\xee\xceN\xbd\xe1\xee\xb8\
X^xtm\xef\x90\xae\xed\xbd\xe4Ps\xa6\x01\xb8\
+=\xd0\xb3\xb3w\xefv\x1b/:\xd7'\x14X\xf7\
\xb7\xe3\xb3\xb9\xaa\xc17[\xe0f\xe0c\x80\xa9\x9e\x81\
\xf7\xe5\x0d\x93~w\x92\xff5\x1d\xfd\xce\xf0\x12L\xe9\
\xe5H\x05\xbe\x88{\xfb\x15\x18\xf6\x9d\xe1\x0f\x86\xce\x7f\
0\x04\x1fxS#k\xa3\xaf\xc5\xd6\xec\xa7m\x95\xf4\
\xffW\xf0\x1f\xb4\xcf\x95\xd7\
"

qt_resource_name = b"\
\x00\x08\
\x08\xb6\x8e\xf9\
\x003\
\x00r\x00d\x00p\x00a\x00r\x00t\x00y\
\x00\x11\
\x0a\xf8\xd6\xd3\
\x00J\
\x00S\x00m\x00o\x00l\x00.\x00m\x00i\x00n\x00.\x00n\x00o\x00j\x00q\x00.\x00j\x00s\
\
\x00\x0d\
\x0cB\xfa\x93\
\x00J\
\x00S\x00m\x00o\x00l\x00.\x00l\x00i\x00t\x00e\x00.\x00j\x00s\
\x00\x0c\
\x0c\xcc\x9e\xf3\
\x00J\
\x00S\x00m\x00o\x00l\x00.\x00m\x00i\x00n\x00.\x00j\x00s\
\x00\x12\
\x0c\xe9\x9aS\
\x00J\
\x00S\x00m\x00o\x00l\x00.\x00l\x00i\x00t\x00e\x00.\x00n\x00o\x00j\x00q\x00.\x00j\
\x00s\
\x00\x09\
\x0au\xba-\
\x00t\
\x00e\x00s\x00t\x002\x00.\x00h\x00t\x00m\
"

qt_resource_struct = b"\
\x00\x00\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x01\
\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x00\x00\x02\x00\x00\x00\x05\x00\x00\x00\x02\
\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\xa6\x00\x01\x00\x00\x00\x01\x00\x08\xae|\
\x00\x00\x01U\x8d\xcc\x91\x90\
\x00\x00\x00\x16\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\
\x00\x00\x01U\x8d\xce\x08\x90\
\x00\x00\x00>\x00\x00\x00\x00\x00\x01\x00\x01\xfc\x9c\
\x00\x00\x01U\x8d\xce\x10`\
\x00\x00\x00^\x00\x00\x00\x00\x00\x01\x00\x04V\xe0\
\x00\x00\x01U\x8d\xcdlP\
\x00\x00\x00|\x00\x00\x00\x00\x00\x01\x00\x07\xd0e\
\x00\x00\x01U\x8d\xce\x180\
"

def qInitResources():
    QtCore.qRegisterResourceData(0x03, qt_resource_struct, qt_resource_name, qt_resource_data)

def qCleanupResources():
    QtCore.qUnregisterResourceData(0x03, qt_resource_struct, qt_resource_name, qt_resource_data)

qInitResources()
