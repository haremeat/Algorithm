# 재료 ings
# 메뉴 menu
# 판매실적 sell
# 구해야 할 것 : 총 수익

ings = ["r 10", "a 23", "t 124", "k 9"]
menu = ["PIZZA arraak 145", "HAMBURGER tkar 180", "BREAD kkk 30", "ICECREAM rar 50", "SHAVEDICE rar 45", "JUICE rra 55", "WATER a 20"]
sell = ["BREAD 5", "ICECREAM 100", "PIZZA 7", "JUICE 10", "WATER 1"]


dictionary = dict(zip(menu, sell))

# print(dictionary)


menu_list = []
gradient_list = []
price_list = []

for i in menu:
    menus = i.split()

    menu_list.append(menus[0])
    gradient_list.append(menus[1])
    price_list.append(menus[2])

    dictionary = dict(zip(menu_list, gradient_list))


ings_al_list = []
ings_price_list = []

for i in ings:
    material = i.split()
    ings_al_list.append(material[0])
    ings_price_list.append(material[1])


for i in sell:
    menu_name = i.split()[0]
    menu_qty = i.split()[1]
    m_idx = menu_list.index(menu_name)
    m_price = price_list[m_idx]

    # 판매금액
    sell_price = int(menu_qty) * int(m_price)

    # 재료비


    # print(sell_price)


def solution(ings, menu, sell):
    answer = 0
    return answer