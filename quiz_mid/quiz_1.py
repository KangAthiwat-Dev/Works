def cal_bmi(weight, height): # สร้าง function มี parameter 2 ตัว -> weight, height
    bmi = weight/(height/100)**2 # คำนวณค่า bmi weight/(height ยกกำลัง2) โดย height แปลงเป็นหน่วยเมตร
    status = "Obesity" if bmi > 30 else "Overweight" if 25 <= bmi <= 29.99 else "Normal weight" if 18.5 <= bmi <= 24.99 else "Underweight" # if-else sort-hand
    return "BMI={:.2f} {}".format(bmi, status) # return result พร้อม format ผลลัพธ์

weight, height = map(int, input().split(',')) # input มา 2 ค่า แบ่งด้วย ',' แปลง datatype เป็น int ด้วยการ map() เก็บลงตัวแปร weight, height
result = cal_bmi(weight, height) # สร้างตัวแปรมารอรับค่าที่ return มาจาก cal_bmi function ส่ง argument ไป2ตัว -> weight, height
print(result) # แสดงผลลัพธ์