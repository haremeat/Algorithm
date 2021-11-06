def solution(ings, menu, sell):
    answer = 0

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

    # for i in gradient_list:
    #     grad_price = 0
    #     for j in range(len(ings_al_list)):
    #         grad_price = gradient_list.count(ings_al_list[j]) * ings_price_list[j]
    #
    #         print(grad_price)

    for i in sell:
        menu_name = i.split()[0]
        menu_qty = i.split()[1]
        m_idx = menu_list.index(menu_name)
        m_price = price_list[m_idx]

    # 판매금액
    sell_price = int(menu_qty) * int(m_price)

    # 재료비

    return answer
