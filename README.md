# CardImageGenerator
Can be use to put text/image from data list onto background image programmatically

First use : Chulalongkorn Rubnongkaomai 2018

(มีคำอธิบายภาษาไทยประกอบ)

### Requirements / โปรแกรมที่ต้องลงก่อน

1.Python 3 (I use 3.6 / ผมใช้ 3.6)

2.Pillow (Install via command prompt with below command / ลงผ่าน command prompt ด้วยคำสั่งด้านล่าง)

```
pip3 install pillow
```

3.Other library that I may forgot to mention , pleaser refer to errors while running example!! / อาจจะมีอย่างอื่นที่ผมลืมบอก ให้ลองรัน example แล้วแก้ตาม error ที่ขึ้นมา

### Setup Checking / เช็คว่าลงโปรแกรมครบแล้ว

When I say run , you can use anything to run , like IDLE or Command Prompt / คำว่ารันของผมสามารถใช้ command prompt หรือ IDLE ก็ได้

Run start.py , there should be no errors and the output should be similar to the below block

รัน start.py , ไม่ควรจะมี error และควรมี output คล้ายๆด้านล่าง

```
1 / 4
2 / 4
3 / 4
4 / 4
```

## Enough BS! Let's get to use this with your work! / ถึงเวลาเซทให้มันใช้กับงานของคุณได้แล้ว!!

### 1.Set bigData.json / เปิด bigData.json แล้วเปลี่ยนเป็นข้อมูลของคุณ

You can have as many fields as you want , including unused fields , but you must have field `id` which must be distinct for every person along with the field that define which background to use , mine was `alias`. For images , you actually have to define type of images `url` or `local` , refer to the example provided

ไฟล์นี้จะมีกี่คนหรือกี่ Field ก็ได้ แต่ต้องมี Field ที่จำเป็นคือ `id` ซึ่งต้องแตกต่างกันสำหรับทุกคน และต้องมีอีก Field เพื่อบอกว่าจะใช้ background รูปอะไร ของผมคือ `alias` และสำหรับรูปภาพ จะต้องมีการบอกชนิดภาพว่าจะเอามาจาก online หรือ offline ดูในตัวอย่างเพื่อความเข้าใจ


### 2.Set globalConfig.json / เปิด globalConfig.json แล้วเปลี่ยนเป็นข้อมูลของคุณ

It is mandatory to set `backgroundSelectorField` to the field name you used last step , mine was 'alias'.

You also should set `groupBy` to what you would like the program to group files into folder for you for example `["alias","university","position"]` means that we will group by `alias` first , and inside each of the alias folder will exist more folders for `university`..... and so on , you can see it in the output folder/grouped. Note that there are always the `raw` folder in case you want to use all the files without grouping

เปลี่ยน `backgroundSelectorField` เป็นชื่อ field ที่คุณใช้แยก background ในขั้นตอนที่แล้ว ของผมใช้ 'alias'.

ตั้ง `groupBy` เป็นลำดับขั้นของการจัดกลุ่มข้อมูลเข้าโฟลเดอร์ เช่น `["alias","university","position"]` แปลว่าเราจะแบ่งกลุ่มตาม `alias` ก่อน , และในแต่ละโฟลเดอร์ของ alias ที่ต่างกันก็จะแบ่งย่อยตาม `university`..... ลองดูตัวอย่างใน folder output/grouped สังเกตว่าใน Folder raw จะเป็นไฟล์ทั้งหมดโดยไม่แบ่งกลุ่ม

### 3.Set backgroundConfig.json / เปิด backgroundConfig.json แล้วเปลี่ยนเป็นข้อมูลของคุณ

First you must have your background images into your background folder , fonts in font folder / อย่าลืมย้ายภาพ background มาไว้ใน folder background , และ font ก็เช่นกัน

The keys of json object are the different values of backgroundSelectorField(mine was `alias`) inside your bigData.json
, I have `boogle` and `basecook` as my background names. For each background there exists `fileName` which is the name of the file and `props` which will be explained later

Keys ของ object นี้คือค่าที่ต่างกันของ backgroundSelectorField(ของผมคือ `alias`) ใน bigData.json ซึ่งของผมมีแค่สองแบบ คือ `boogle` กับ `basecook` โดยสำหรับแต่ละ background จะมี `fileName` คือชื่อไฟล์ และ `props` ซึ่งจะเป็นไปตามคำอธิบายด้านล่าง

#### Props

`type: image`

```
field : field that this prop is linked to / ชื่อ field ที่ link กัน
xTopLeft : Self explainatory(in pixels) / ค่า x ของมุมบนซ้ายหน่วย pixels
yTopLeft : Self explainatory(in pixels) / ค่า y ของมุมบนซ้ายหน่วย pixels
xLength : Self explainatory(in pixels) / ความกว้าง หน่วย pixels
yLength : Self explainatory(in pixels) / ความสูง หน่วย pixels
```

`type: text`

```
including all fields of type image with some additions
xAlign: alignment in x axis(left,right,center) , การชิดซ้ายขวากลาง (left,right,center)
yAlign: alignment in y axis(top,bottom,center) , การชิดบนล่างกลาง (top,bottom,center)
font: fontFile name , ชื่อไฟล์ font
size: font size
fill: RGBA representation of font color , สี font ในรูปแบบ RGBA
```

## Done!!

Run `start.py`

I wrote lots of error handling , so if there are any errors , it should pop up.

You can just read the errors and fix accordingly.

แก้ปัญหาไปตามที่เจอแล้วกันนะครับ ผมก็จำไม่ได้ว่าเขียน handle อะไรไว้บ้าง

## Bye

I know this readme is very confusing , as I am right now , so sorry for that.

ขอโทษถ้าอ่านไม่รู้เรื่องนะครับ ฮ่าๆ

#### PoomrokC

#### 31/12/2018
