# Create formatted string ------------------------------------------------------
title = "\n{:-^50}\n\n".format(" NCT-CSB22 ")

line = "| {:^3} | {:<18} | {:^9} | {:^7} |"
row_divider = "+ {:-^3} + {:-^18} + {:-^9} + {:-^7} +".format("","","","")
row_header = line.format("STT","Họ và tên","Giới tính","Vai trò")

row_0 = line.format("0","Ngô Quang Việt","Nam","GV")
row_1 = line.format("1","Nguyễn Hoàng Long","Nam","HS")
row_2 = line.format("2","Mai Bảo Lâm","Nam","HS")
row_3 = line.format("3","Dương Minh Khánh","Nam","HS")
row_4 = line.format("4","Tạ Trung Tín","Nam","HS")
row_5 = line.format("5","Võ Lê Hải Triều","Nam","HS")
row_6 = line.format("6","Triệu Quốc Anh","Nam","HS")


# Print result -----------------------------------------------------------------
# Print the title
print(title)

# Table header
print(row_divider)
print(row_header)
print(row_divider)
# Table body
print(row_0)
print(row_1)
print(row_2)
print(row_3)
print(row_4)
print(row_5)
print(row_6)
print(row_divider)