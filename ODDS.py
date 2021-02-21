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
de_text = deshift_right(en_text) #ถอดรหัสข้อความ
#print(de_text)
