from notes.models import Note


def common_tags(request):
    return {'common_tags': Note.tags.most_common()}
