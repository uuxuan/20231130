# 學生類別
class student:
    # 建構式
    def __init__(self,school,department,name,teacher,studentname,ID,address,score,GPA):
        self.name = name  # 屬性
        self.department = department 
        self.teacher = teacher
        self.studentname = studentname
        self.ID = ID
        self.address = address
        self.score = score
        self.GPA = GPA
        self.school = school
    def getshool(self):
        return self.school
    def setshool(self,value):
        self.school=value
p=student("南台科技大學","資訊工程系","小朱","吳建中","陳宥瑄","4B0G0162","南台街1號","155","52")
print(p.getshool())
p.setshool("南應科技大學")
print(p.getshool())

