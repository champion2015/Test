import os
import sys
import codecs
import xlrd

def getFileList( p ):
    p = str( p )
    if p=="":
          return [ ]
    p = p.replace( "/","\\")
    if p[ -1] != "\\":
         p = p+"\\"
    a = os.listdir( p )
    b = [ x   for x in a if os.path.isfile( p + x ) ]
    return b

def FloatToString (aFloat):
    if type(aFloat) != float:
        return ""
    strTemp = str(aFloat)
    strList = strTemp.split(".")
    if len(strList) == 1 :
        return strTemp
    else:
        if strList[1] == "0" :
            return strList[0]
        else:
            return strTemp

def table2json(excelfileName, jsonfilename):
	workbook = xlrd.open_workbook(excelfileName)
	f = codecs.open(jsonfilename,"w","utf-8")
	i = 0
	f.write(u"{")

	for sheet in workbook.sheets():
	    nrows = sheet.nrows
	    ncols = sheet.ncols
	    f.write(u"\n\t\"" + sheet.name + "\":[\n")
	    flag = True
	    for r in range(nrows-1):
	    	if str(sheet.cell_value(r+1,0)) == "END":
	    		flag = False
	    	if str(sheet.cell_value(r+1,0)) != "NO":
		        f.write(u"\t\t{ ")
		        for c in range(ncols-1):
		            strCellValue = u""
		            CellObj = sheet.cell_value(r+1,c+1)
		            if type(CellObj) == unicode:
		                strCellValue = u"\""  + str(CellObj) + u"\""
		            elif type(CellObj) == float:
		                strCellValue = FloatToString(CellObj)
		            else:
		                strCellValue = u"\""  + str(CellObj) + u"\""
	            
		            strTmp = u"\""  + sheet.cell_value(0,c+1) + u"\":"+ strCellValue
		            if c< ncols-2:
		                strTmp += u", "
		            f.write(strTmp)
		        f.write(u" }")
		        if r < nrows-2 and flag:
		            f.write(u",")
		        f.write(u"\n")

		        if not flag:
		        	break

	    f.write(u"\t]")

	    i = i + 1
	    if i < workbook.nsheets:
	    	f.write(u",")	    

	f.write(u"\n}")
	f.close()
	print "Create ",jsonfilename," OK"
	return

excelsFolder = os.path.join(sys.argv[1] ,"excel")
jsonsFolder = os.path.join(sys.argv[1] ,"json")
if not os.path.exists(jsonsFolder):
	os.makedirs(jsonsFolder)

excels = getFileList(excelsFolder)
for f in excels:
	jsonfile = f.replace(".xls", ".json")
	jsonfile = os.path.join(jsonsFolder ,jsonfile)
	excelfile = os.path.join(excelsFolder ,f)
	table2json(excelfile, jsonfile)
	#print jsonfile

#data = xlrd.open_workbook(excelFileName)
#jsonFileNames = excelFileName.replace(".xls", ".json")
#print jsonFileNames
#table = data.sheet_by_name(u"tablelist")
#rs = table.nrows
#for r in range(rs-1):
#    print table.cell_value(r+1,0), "==>", table.cell_value(r+1,2)
 #   desttable = data.sheet_by_name(table.cell_value(r+1,0))
  #  destfilename = table.cell_value(r+1,2)
   # table2json(desttable,destfilename)

print "All OK"