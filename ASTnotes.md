https://youtube.com/shorts/maAM4VcsZAU?si=GqSQOr13MiMr86lQ (how zed does parsing)
https://www.youtube.com/watch?v=NxiKlnUtyio&pp=ygUMYXN0ICBwYXJzaW5n (interesting , but not necessary)


https://youtu.be/tM_S-pa4xDk?si=O0ewhThoKnaDP0yM (quick tutorial)
when you are changing soemthing that affects a lot of files in your codebase , youd have to review each file separately and this takes a lot of time.
THATS where AST helps you make better decisions , it unlocks your ability to make it better
ASTs have a much broader application than just refactoring
<img width="1884" height="468" alt="image" src="https://github.com/user-attachments/assets/6a7e9232-e899-4df3-b9f3-5c8680e175b1" />


an AST is an intermediate representation of the source code as tree structure
<img width="1108" height="740" alt="image" src="https://github.com/user-attachments/assets/fe6bcfa6-3940-44b6-bbac-97580c0ecaa4" />

clear heirachy

<img width="1220" height="576" alt="image" src="https://github.com/user-attachments/assets/deaff325-2a64-4f25-bcc2-907233773318" />


in frontend , they are the equivalent to webpack or parcel
<img width="1044" height="480" alt="image" src="https://github.com/user-attachments/assets/6e923eae-0a33-43e1-800b-92e942b30e1b" />
https://webpack.js.org/ (similar to compiler but a bit different , do read on this)


the AST is the intermediate between the frontend and backend
<img width="1376" height="418" alt="image" src="https://github.com/user-attachments/assets/20480656-3a9d-4734-b0b2-40cde683f863" />


learning ASTs will unlock things like :
-how many times is a variable /function used in source code
-transforming code from one syntax to another
-enforcing rules for syntax
-other static analysis


<img width="1326" height="564" alt="image" src="https://github.com/user-attachments/assets/f15943ec-58ce-4345-a890-0c51223a60a8" />



<img width="1218" height="796" alt="image" src="https://github.com/user-attachments/assets/e3ebc35b-6217-4842-898f-1def7f4cdc87" />
generate in json structure


<img width="488" height="792" alt="image" src="https://github.com/user-attachments/assets/8d047603-a311-4d35-ad08-1f680921e3a6" />
this is a binary expression

<img width="1152" height="702" alt="image" src="https://github.com/user-attachments/assets/d2ef1e55-d95b-4f1f-8370-0a06aea35b37" />

https://astexplorer.net/ (use this site)
<img width="1282" height="766" alt="image" src="https://github.com/user-attachments/assets/8d821d5f-3140-4b6e-8ee3-35a2d0ae9031" />

parser options
<img width="968" height="782" alt="image" src="https://github.com/user-attachments/assets/7d8e3838-c1f2-4181-8a99-45af247c871e" />
<img width="2870" height="1580" alt="image" src="https://github.com/user-attachments/assets/5107596c-cdf1-48c7-b96b-743ea720354a" />




some JS + AST ecosystem
-prettier 
-ESlint
-Babel (js compiler)


ENviornments:
npm v6
node v12


Generating a JS AST
<img width="1152" height="766" alt="image" src="https://github.com/user-attachments/assets/aa6adb7a-ded4-43ff-ab3a-1a18bceee6a1" />
https://www.npmjs.com/package/@babel/parser

babel would help you transpile modern js syntax to compatible with  older java script 
has plugins for different things like support for syntax not supported by broswer


todo : try making a custom babel plugin (look for some cool implementation of this)


<img width="330" height="430" alt="image" src="https://github.com/user-attachments/assets/b4a89c98-6da4-443c-a327-2127b4242e4a" />
babel core pacakage and what they do:
parser- parses code string into AST
travese- travesr nodes
generator- converts ast back into source code
types- new nodes to add or repalce existing nodes in the ast



<img width="1314" height="648" alt="image" src="https://github.com/user-attachments/assets/b38bec96-14a8-405b-985b-5a5687071111" />

<img width="804" height="786" alt="image" src="https://github.com/user-attachments/assets/a26570ea-a59d-48e4-870b-b94a1ee190fb" />

<img width="582" height="800" alt="image" src="https://github.com/user-attachments/assets/ecf0ba6d-6614-4e4b-89bc-672ea65ceba4" />
body proprty is to contain various types of nodes 

<img width="446" height="72" alt="image" src="https://github.com/user-attachments/assets/4e861177-658a-45bf-a7f5-85dc3c94f109" />



<img width="1190" height="808" alt="image" src="https://github.com/user-attachments/assets/840e4866-5855-4162-84c0-0defeb95d173" />

 binary expression -> left , operator , right


 <img width="634" height="42" alt="image" src="https://github.com/user-attachments/assets/29e40e40-7921-4fdb-92da-c3eb4d5a9565" />
this time only the value 2 is there


Traversing an AST
<img width="792" height="148" alt="image" src="https://github.com/user-attachments/assets/5eca9eea-4226-45f0-871e-60210aa79a93" />
 

<img width="1406" height="636" alt="image" src="https://github.com/user-attachments/assets/996400a5-9ad8-4ea5-bd2d-19c593fd61f7" />

How to build ast?
1-take the 1st operator appearing from the left to right , (which is not inside any bracket)

2-list down the numbericals and operators  on its left and right  (if theres a bracket , take its operator)
if theres a normal numerical , put it as it is


at the end the leaf must always be numerical values.


install the babel traverse package
<img width="1040" height="464" alt="image" src="https://github.com/user-attachments/assets/7f4a7bdf-c701-41d8-a46e-761aba6fb635" />


<img width="572" height="330" alt="image" src="https://github.com/user-attachments/assets/ba457eb4-7af3-4ac1-96e8-fc7714ef73d9" />

the second argument in the traverse function is an object of visitors

keys in the object are type of nodes
value is function , visitor 



<img width="1114" height="786" alt="image" src="https://github.com/user-attachments/assets/d78ebbb0-b581-4add-960c-f5688685a822" />
wrapper around the node helps  represnts metadata 


 <img width="478" height="174" alt="image" src="https://github.com/user-attachments/assets/3e7f7c76-1cf4-4975-a4d2-f9f78cab8829" />
finds all numerc literal nodes

if you want values then :
<img width="988" height="188" alt="image" src="https://github.com/user-attachments/assets/720ac240-419b-4d09-94b4-d3365453cf4a" />

<img width="624" height="154" alt="image" src="https://github.com/user-attachments/assets/dddc7c21-e7b4-4604-9081-a33dff6cd224" />


define a visitor when visiting the node from bottom to top or an exit
<img width="620" height="396" alt="image" src="https://github.com/user-attachments/assets/c6ace7ed-6309-48ee-bfb3-d1a46b1e68cd" />
  


<img width="334" height="206" alt="image" src="https://github.com/user-attachments/assets/b7437f98-0251-4de1-94d7-4866c18a486a" />



