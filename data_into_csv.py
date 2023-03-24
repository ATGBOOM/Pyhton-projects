import csv 
rowheader1 = ["NAMES"]
rowheader2 = ["BOOK NAME"]
names = []
bookName = []
for i in range(100):
  g = input().split("-")
  #names.append()
  bookName.append([g[1]])

with open("sheet.sheet.csv", "w", newline = "") as csvfile:
  write = csv.writer(csvfile)
  write.writerow(rowheader2)
  write.writerows(bookName)
  write.writerow(rowheader1)
  write.writerows(names)


