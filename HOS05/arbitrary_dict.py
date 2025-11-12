def menu(item, quan, **restaurant):
    restaurant['Item'] = item
    restaurant['Quantity'] = quan
    return restaurant

restaurant = menu('soup', 2, location='Main Street', zip='12345')
print(restaurant)