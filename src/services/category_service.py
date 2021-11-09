from ..db.documents import Category, Product


def get_categories():
    products = Product.objects()
    categories = Category.objects().order_by('sequence')

    for category in categories:
        cont = 0
        for product in products:
            if product.category == category.name:
                cont = cont + 1
        category.products = cont

    return categories


def create_category(name):
    sequence = get_categories().count()
    Category(name=name, sequence=sequence+1).save()

    return True


def edit_category(id, name):
    Category.objects(id=id).update(name=name)

    return True


def delete_category(id):
    Category.objects(id=id).delete()

    return True
