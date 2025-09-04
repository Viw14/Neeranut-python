""" เขียน function ชื่อ welcome_message ที่มีคุณสมบัติดังนี้:
 
รับ parameter 2 ตัว คือ name และ course
return ข้อความต้อนรับในรูปแบบ string
รูปแบบ: "Welcome [name] to [course] class!"
 
"""
def welcome_message(name, course):
    # Your Problem 1 solution
    return f"Welcome {name} to {course} class!"
 
""" เขียน function ชื่อ calculate_circle ที่มีคุณสมบัติดังนี้:
 
รับ parameter 1 ตัว คือ radius
return dictionary ที่มี area และ circumference
ใช้ค่า π = 3.14159
ปัดเศษทั้งสองค่าให้เหลือ 2 ตำแหน่งหลังจุดทศนิยม """
 
def calculate_circle(radius):
    # Your Problem 2 solution
    pi = 3.14159
    area = round(pi * radius ** 2, 2)
    circumference = round(2 * pi * radius, 2)
    return {
        'area': area,
        'circumference': circumference
    }
 
 
""" เขียน function ชื่อ create_user_profile ที่มีคุณสมบัติดังนี้:
 
รับ parameters: username (จำเป็น), age (ค่าเริ่มต้น 18), premium (ค่าเริ่มต้น False)
return string ที่จัดรูปแบบข้อมูลผู้ใช้
รูปแบบ: "[username] (age: [age]) - [Premium User / Standard User]"
 
"""
 
def create_user_profile(username, age=18, premium=False):
    # Your Problem 3 solution
    if premium:
        return username +"(age:"+ age + "- Premium User"
    else:
        return username +"(age:"+ age + "- Standard User"
 
""" เขียน function ชื่อ analyze_scores ที่มีคุณสมบัติดังนี้:
 
รับ list ของคะแนน (ตัวเลข)
return dictionary ที่มี:
 
total: ผลรวมของคะแนนทั้งหมด
average: คะแนนเฉลี่ย (ปัดเศษ 1 ตำแหน่งหลังจุดทศนิยม)
highest: คะแนนสูงสุด
lowest: คะแนนต่ำสุด
passed: จำนวนคะแนนที่ >= 70 """
 
def analyze_scores(scores):
    # Your Problem 4 solution
    total = sum(scores)
    count =len(scores)
    average = total / scores
    highest = max(scores)
    lowest = min(scores)
 
    for score in scores:
        if score >=70:
            passed += 1
   
 
    return {
        'total': total,
        'average': average,
        'highest': highest,
        'lowest': lowest,
        'passed':  passed
 
    }
 
""" เขียน function ชื่อ count_vowels_consonants ที่มีคุณสมบัติดังนี้:
 
รับ parameter text เป็น string
นับสระ (a, e, i, o, u) และพยัญชนะ (ไม่นับช่องว่างและตัวเลข)
return dictionary ที่มี vowels และ consonants counts
ไม่สนใจตัวใหญ่ตัวเล็ก (case insensitive) """
 
def count_vowels_consonants(text):
    # Your Problem 5 solution
    text = text.replace(" ","")
    text = text.lower()
    vowels = text.count('a') +text.count('e') +text.count('i') +text.count('o') +text.count('u')
    numbers = text.count('0') +text.count('1') +text.count('2') +text.count('3') +text.count('4')  
    consonants = len(text) - vowels - numbers
    return{
        "vowels": vowels,
        "consonants":consonants
    }