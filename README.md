# shop_django

# Usage commands

python manage.py dumpdata goods.ProductCategory --indent=4 > fixtures/goods/prodcategories.json
python manage.py dumpdata goods.Product --indent=4 > fixtures/goods/products.json

python manage.py loaddata fixtures/goods/prodcategories.json
python manage.py loaddata fixtures/goods/products.json
