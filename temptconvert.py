TempConvert=input("请输入带有符号的温度值：")
if TempConvert[-1] in ["c","C"]:
    C=(eval(TempConvert[0:-1])*1.8)+32
    print("转换后的温度是{:.2f}C".format(C))
elif TempConvert[-1] in ["f","F"]:
    F=(eval(TempConvert[0:-1])-32)/1.8
    print("转换后的温度是{:.2f}C".format(F))
else :
    print("输入错误")
