from notes.models import Note


def common_tags(request):
    print(Note.tags.most_common())
    return {'common_tags': Note.tags.most_common()}