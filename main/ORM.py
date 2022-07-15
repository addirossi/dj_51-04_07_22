#SELECT

# SELECT * FROM product;
# Product.objects.all()

#один объект
# Product.objects.get(...)

#фильтрация
# SELECT * FROM product WHERE условие;
# Product.objects.filter(условие)

#ORDER BY
# SELECT * FROM product ORDER BY price ASC;
# Product.objects.order_by('price')
# SELECT * FROM product ORDER BY price DESC;
# Product.objects.order_by('-price')

#INSERT
#одна запись

# INSERT INTO product (...) VALUES (...);
# Product.objects.create(...)

# product = Product(...)
# product.save()

#несколько записей
# INSERT INTO product (...) VALUES (...), (...), (...);

# Product.objects.bulk_create([
#     Product(...),
#     Product(...),
#     Product(...)
# ])

#UPDATE
# UPDATE product SET price = 100000;
# Product.objects.update(price=10000)

#UPDATE product SET price = 100000 WHERE price > 120000;
# Product.objects.filter(price__gt=120000).update(price=100000)


#DELETE
# DELETE * FROM product;
# Product.objects.delete()

#DELETE * FROM product WHERE price > 50000;
# Product.objects.filter(price__gt=50000).delete()