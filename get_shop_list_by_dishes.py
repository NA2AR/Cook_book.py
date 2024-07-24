import os 
file_path_cook_book = os.path.join(os.path.dirname(__file__), 'cook_book.txt')
file_path_txt1 = os.path.join(os.path.dirname(__file__), '1.txt')
file_path_txt2 = os.path.join(os.path.dirname(__file__), '2.txt')
file_path_txt3 = os.path.join(os.path.dirname(__file__), '3.txt')
file_path_result = os.path.join(os.path.dirname(__file__), 'result.txt')
cook_book = dict()
with open(file_path_cook_book, 'r', encoding='utf-8') as file:
    data = file.readlines()
    G_dish = []
    ingred = []
    for lines in data:
        if ': [' not in lines:
            if "{'" in lines:
                if "}," in lines:
                    ingred = lines.strip()[1:-2]
                else:
                    ingred = lines.strip()[1:-1]
                    
        elif ': [' in lines:
            dish = lines.split("'")[1]
            G_dish = (lines.split("'")[1])
            if G_dish != dish:
                G_dish = (lines.split("'")[1])
                
        if len(G_dish) and len(ingred) != 0:
            if G_dish in cook_book and ingred not in cook_book[G_dish]:
                cook_book[G_dish].append(ingred)
            elif G_dish in cook_book and ingred in cook_book[G_dish]:
                ingred = []
            else:
                cook_book[G_dish] = [ingred]

with open(file_path_txt1, 'r+', encoding='utf-8') as file1, open(file_path_txt2, 'r+', encoding='utf-8') as file2, open(file_path_txt3, 'r+', encoding='utf-8') as file3, open(file_path_result, 'r+', encoding='utf-8') as result_path:
    data1 = file1.readlines() 
    data2 = file2.readlines()
    data3 = file3.readlines()
    text1 = '' 
    for l in data1:
        text1 += l
    text2 = ''
    for l in data2:
        text2 += l
    text3 = ''
    for l in data3:
        text3 += l
    result_path.write(max(text1, text2, text3) + (str(text1+text2+text3).replace(max(text1, text2, text3)+min(text1, text2, text3), '')) + min(text1, text2, text3))

def get_shop_list_by_dishes(dishes, person_count):
    for dish in dishes:
        for elements in cook_book[dish]:
            quantity =()
            ing_name =()
            measure = ()
            for i in elements.split(', '):
                if 'quantity' in i:
                    quantity = int(i.split(': ')[1]) * person_count
                if 'ingredient_name' in i:
                    ing_name = i.split(': ')[1]
                if 'measure' in i:
                    measure = i
            print(f"{ing_name}: {measure}, 'quantity' : {quantity}")
            
    
get_shop_list_by_dishes(['Запеченный картофель', 'Омлет', 'Утка по-пекински'], 2)


