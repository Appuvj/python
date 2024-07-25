# area of circle=PI*radius*radius

def area(radius,PI=3.14):
    print('radius: ',radius)
    print('PI: ',PI)
    result=PI*radius*radius
    return result

def main():
    #position argument
    output_1=area(10,20)
    print('area of circle is : ',output_1)

    #first argument is positional and second is default
    output_1=area(10)
    print('area of circle: ',output_1)

    #keyword argument
    output_2 = area(PI=3,radius=12)
    print('area of circle : ',output_2)

    # keyword argument and second is default
    output_2 = area(radius=12)
    print('area of circle : ',output_2)

if __name__ =="__main__":
    main()

    