
import csv
#simple multiplication with mapping
# def multiplication(a):
#     return a * a 

# numbers = (1,2,3,4)
# result = map(multiplication, numbers)
# print(list(result))

# #mapping from CSV file
# csvFile = open("csv_files/analysis-public-place-assaults-sexual-assaults-and-robberies-2015-csv.csv")
# print(csvFile.read())

# def readColumns():
#     csvFile = open(
#         "csv_files/analysis-public-place-assaults-sexual-assaults-and-robberies-2015-csv.csv")
#     colnames = ["Urban_area_2013_label",
#                 "Territorial_authority_area_2013_label"]
    
    

def readfileprintonscreen():
    with open("csv_files/analysis-public-place-assaults-sexual-assaults-and-robberies-2015-csv.csv", "r") as csv_file1:
        csv_reader = csv.reader(csv_file1, delimiter=',')
        for lines in csv_reader:
            #print(lines[11])
            searchWord = "Dunedin City"
            if searchWord in lines[11]:
                print(lines.count(searchWord), "print stuff")

print(readfileprintonscreen())

