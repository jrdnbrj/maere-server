from ..db.documents import Category


def get_categories():
    return Category.objects().order_by('sequence')


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
