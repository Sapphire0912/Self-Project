import pdfplumber
import json
import os

AnswerDir = "./Answer/"
subjectsPath = [AnswerDir + path + "/" for path in os.listdir(AnswerDir)]

# for subject in subjectsPath:
#     fileList = os.listdir(subject)
#
#     answerDict = dict()  # 儲存解答的字典
#     for file in fileList:
#         path = subject + file
#
#         years = file.split('_')[0]  # 抓取該解答的年份
#         answerDict[years] = list()  # 拿年份當成字典
#
#         # 開啟 pdf 檔案, 並讀取表格資料
#         with pdfplumber.open(path) as pdf:
#             page = pdf.pages[0]  # 解答只有一頁
#             table = page.extract_tables()  # 讀取表格資料
#
#             for line in table:
#                 answers = line[1][1:]
#                 for i in answers:
#                     answerDict[years].append(i)
#
#     # 將資料寫入 json 檔案
#     jsonFile = open(subject + "Answers.json", 'w')
#     json.dump(answerDict, jsonFile)

targetPath = "./Question/學習者發展與適性輔導/112_學習者發展與適性輔導.pdf"
pdf = pdfplumber.open(targetPath)
page = pdf.pages[5]
text = page.extract_text_simple()
print(text)