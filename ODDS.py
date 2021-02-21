#อันดามัน นพนภาพร [ภูเขา]
def enshift_right(str): #เข้ารหัสข้อความ
    new_text = ''
    for i in str:
        t = chr(ord(i) +1)
        new_text = new_text+t
    #print(new_text)
    return new_text

def deshift_right(str): #ถอดรหัสข้อความ
    new_text = ''
    for i in str:
        t = chr(ord(i) -1)
        new_text = new_text+t
    #print(new_text)
    return new_text


text = """A mosquito net ,
A can of petrol | 9 : ถังน้ำมัน อาจมีน้ำมันใช้จุดไฟ หรือถังเอาไว้ลอยน้ำได้ ,
A water container | 5 ใช้เก็บน้ำดื่มได้ ,
A shaving mirror | 10 : อาจเอาไว้ใช้ส่งสัญญาณขอความช่วยเหลือเมื่อมีเรือแล่นมาใกล้ๆได้ ,
A sextant ,
Emergency rations | 1 : เพราะอาหารสำคัญกับอาหารเอาชีวิตรอด ,
A sea chart | 8 เราอาจใช้แผนที่ไม่ได้แต่อาจนำมาใช้เป็นเชื้อไฟ หรือกระดาษไว้เขียนขอความช่วยเหลือได้ ,
กันการจมน้ำและลอยคอเข้าสู่เกาะได้ ,
A rope | 4 เชือกใช้ผูกตัวเราติดกับเบาะลอยน้ำกันจม และเมื่อขึ้นฝั่งก็นำไปใช้ประโยชน์ได้ ,
Some chocolate bars | 2 : อาหารอีกชิ้น ,
A waterproof sheet | 6 ใช้รองน้ำค้างหรือน้ำฝนใช้ดื่มได้ ,
A fishing rod | 11 : อาจใช้ตกปลาได้ แต่ถ้าไม่ได้จริงๆด้ามและเส้นเอ็นก็นำไปใช้ประโยชน์ได้ ,
Shark repellent ,
A bottle of rum | 7 อาจใช้เลนส์ของขวดจุดไฟได้ ,
A VHF radio ,"""

en_text = enshift_right(text) #เข้ารหัสข้อความ
print(en_text)

print('-----------------------------------------------------------------')
#ข้อความที่เข้ารหัสแล้ว
#'B!nptrvjup!ofu!-B!dbo!pg!qfuspm!}!:!;!ทาจบ๊ิยาบ!ฮำฉยึบ๊ิยาบไซ๊ฉูตๅภ!ฬฤุฮทาจแฮำๅศ๊ฦฮรบ๊ิๅต๊!-B!xbufs!dpoubjofs!}!6!ไซ๊แข่ปบ๊ิตุ้ยๅต๊!-B!tibwjoh!njssps!}!21!;!ฮำฉแฮำๅศ๊ไซ๊ห้จหาฎฎำดฃฮฅศำยซ้ศรแฬฦุฮแยุ้ฮยึแฤุฮโฦ้บยำไขฦ๊็ๅต๊!-B!tfyubou!-Fnfshfodz!sbujpot!}!2!;!แฟฤำัฮำฬำฤหิฅาฎขาปฮำฬำฤแฮำซึศีถฤฮต!-B!tfb!dibsu!}!9!แฤำฮำฉไซ๊โฝบธึ้ๅย้ๅต๊โถ้ฮำฉบิยำไซ๊แผ่บแซุ๊ฮๅภ!ฬฤุฮขฤัตำสๅศ๊แฃึรบฃฮฅศำยซ้ศรแฬฦุฮๅต๊!-ขาบขำฤฉยบ๊ิโฦัฦฮรฅฮแฃ๊ำหฺ้แขำัๅต๊!-B!spqf!}!5!แซุฮขไซ๊ฝฺขถาศแฤำถีตขาปแปำัฦฮรบ๊ิขาบฉย!โฦัแยุ้ฮฃื๊บพา้จข่บิๅผไซ๊ผฤัใรซบํๅต๊!-Tpnf!dipdpmbuf!cbst!}!3!;!ฮำฬำฤฮึขซี๊บ!-B!xbufsqsppg!tiffu!}!7!ไซ๊ฤฮจบ๊ิฅ๊ำจฬฤุฮบ๊ิพบไซ๊ตุ้ยๅต๊!-B!gjtijoh!spe!}!22!;!ฮำฉไซ๊ถขผฦำๅต๊!โถ้ท๊ำๅย้ๅต๊ฉฤีจ็ต๊ำยโฦัแห๊บแฮ่บข่บิๅผไซ๊ผฤัใรซบํๅต๊!-Tibsl!sfqfmmfou!-B!cpuumf!pg!svn!}!8!ฮำฉไซ๊แฦบหํฃฮจฃศตฉูตๅภๅต๊!-B!WIG!sbejp!-'
#
de_text = deshift_right(en_text) #ถอดรหัสข้อความ
#print(de_text)
