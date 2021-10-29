from ..db.documents import Category


def get_categories():
    return Category.objects().order_by('sequence')


def create_category(name):
    sequence = get_categories().count()
    return Category(name=name, sequence=sequence+1).save()


def edit_category(id, name):
    category = Category.objects(id=id)
    category.name = name
    category.save()

    return True


def delete_category(id):
    Category.objects(id=id).delete()

    return True
