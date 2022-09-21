def divison(data1,code):
    if len(data1) > len(code):
        data = list(data1[:len(code)])
        data1 = "".join(data1[len(code):])
        for i in range(len(data)):
            data[i] = str(int(data[i])^int(code[i]))
        data = "".join(data)
        data = data+ data1
        data = int(data)
        return divison(list(str(data)),code)
    else:
        res = ""
        if len(data1) == len(code)-1:
            res = res.join(data1)
        else:
            app = "0"* ((len(code)-1)-len(data1))
            res = res + app +"".join( data1)
        return res
data = input()
code = input()
app ="0" *(len(code)-1)
data1 = data + app
print(f"code is {divison(list(data1),code)}")
final = data + divison(list(data1),code)
print(f"decoding is {divison(list(final),code)}")
if list(divison(list(final),code)).count('0') == len(code)-1:
    print("Data transferred without any errors")

