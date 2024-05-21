my_list = ["Apples", "Oranges", "Strawberry", "Bananas", "Pears", "Mandarins"]
print(my_list)

print(my_list[0])
print(my_list[-1])
print(my_list[3:5])

my_list[3] = "Carrots!"
print(my_list)

my_dict = {
    "howl": "выть",
    "poor": "бедный",
    "sit": "сидеть",
    "fry": "жарить",
    "sip": "попивать",
    "ring": "звонить"
}


print(my_dict)
print(f"Ring - {my_dict['ring']}")
my_dict['ring'] = 'кольцо'
print(f"Ring - {my_dict['ring']}")
my_dict["impoverished"] = my_dict.pop("poor")
print(my_dict)