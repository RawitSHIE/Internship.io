# 🧠 Word Guessing Game
เกมทายคำตามหมวดหมู่ที่ทางผู้เล่นเลือกโดยจะมี `hint` ให้กับผู้เล่น
โดยกฎกติกาเป็นดังนี้

1. การทายคำแต่ละคำนั้นจะมีคะแนนตาม จำนวนตัวอักษร * 15
2. การทายถูกแต่ละครั้งจะได้ 15*n คะแนน (n จำนวนอักษรที่เราทายอยู่ในคำนั้นๆ)
3. การทายผิดจะถูก -5 คะแนน
4. สามารถทายผิดได้ 10 ครั้ง
5. คำที่ผู้เล่นทายมาจะไม่สามารถทายซ้ำได้ (จะไม่คำนวนคะแนนส่วนนั้น)

โดยเกมจะมีหมวดหมู่คำอยู่ 3 หมวดคือ
1. Computer Knowledge ซึ่งจะเป็นความรู้พื้นฐานทางคอมพิวเตอร์ต่างๆ
2. Big Company ซึ่งจะเกี่ยวกับชื่อบริษัทดังๆในโลก
3. Famous Person ซึ่งจะเกี่ยวกับชื่อของคนดังในโลกตอนนี้
## Pre-required
* python 3
* file `hang.py`
* file `cat1.txt`, `catt2.txt`, `cat3.txt`

##  การ Run
1. ใน Terminal/cmd ไปยัง Directory ขอ File `hang.py`
2. ทำการ Run File `hang.py`

mac os
```
$ python3 hang.py
```
Windows
```
$ py -3 hang.py
```

##  การเล่น

เมือทำการ run file `hang.py` ได้แล้วก็จะขึ้นตัว category ให้เลือก
```
Select Category:
1. Computer Knowledge
2. Big Company
3. Famous Person
```
ให้กดเลือก category ที่ต้องการเล่น โดยการกดเลขที่ตรงกับ category

ส่วนขอการทายคำ
ให้ทายตัวอักษรทีละตัวอักษรไปเรื่อยๆ จนกว่าจทายถูกหมดหรือ remaining guess เท่ากับ 0
```
Hint: "Part of Edge Network"
_ _ _   _ _ _ _ _ _      score 0, remaining guess word 10
p
_ _ _   _ _ _ _ _ _      score 0, remaining guess word 9, wrong guessed: p
```

เมื่อผู้เล่นเล่นชนะ
```
G o o g l _      score 75, remaining guess word 10
e
G o o g l e      score 90, remaining guess word 10
You guessed!!!!
Google, Score : 90
```
เมื่อผู้เล่นเล่นแพ้
```
E n _   _ _ _ t e m      score 40, remaining guess word 1, wrong guessed: v c x z w q u k j
h
E n _   _ _ _ t e m      score 35, remaining guess word 0, wrong guessed: v c x z w q u k j h
You lose
The answer is End System
```

# Contact
<center>

|<a href=""><img src="https://avatars0.githubusercontent.com/u/31315990?s=460&v=4" width="100px"></a>  |
| :-: |
|รวิชญ์ โลหะขจรพันธ์|
|      Rawitgun@gmail.com      |
|     0910349301    |

</center>
