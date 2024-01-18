hexa = {0:'0',1:'1',2:'2',3:'3',4:'4',5:'5',6:'6',7:'7',8:'8',9:'9',10:'A',11:'B',12:'C',13:'D',14:'E',15:'F',}



def dectohex(decimal):
    result = ""
    while decimal > 0:
        result = hexa[decimal%16]+result
        decimal = int(decimal/16)
    return(result)

try:
    decimal = int(input("Enter an integer: "))
except ValueError:
    print("Please input an integer")
    

print("In hexadecimal: "+ dectohex(decimal))
