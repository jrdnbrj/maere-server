from ..db.documents import Category


def get_categories():
    return Category.objects().order_by('sequence')

def create_category(name):
    sequence = get_categories().count()
    return Category(name=name, sequence=sequence+1).save()