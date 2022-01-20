from notes.models import Note


def common_tags(request):
    if 'notes' in request.resolver_match.app_names:
        return {'common_tags': Note.tags.most_common()}
    else:
        return {}
