dictionary = [dict(Trang=38, Thu=38, Ngoc=27, Thanh=26, Yen=25, Hang=22, Thuy=22)]
def unique_value_dict(dictionary):
    print( set( val for dic in dictionary for val in dic.values()))
unique_value_dict(dictionary)