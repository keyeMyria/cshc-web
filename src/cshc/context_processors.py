""" Context processors for the CSHC website.

    Provides common key/value pairs that will be added to the
    context of all requests.

    Ref: https://docs.djangoproject.com/en/1.11/ref/templates/api/#writing-your-own-context-processors

    Note: This requires the following TEMPLATE_CONTEXT_PROCESSOR:
        'core.context_processors.utils'
"""

from django.conf import settings

# pylint: disable=W0613


def utils(request):
    """ Returns common context items. """
    context = {
        'VERSION': settings.VERSION,
        'STATIC_URL': settings.STATIC_URL,
        "GMAPS_API_KEY": settings.GMAPS_API_KEY,
        'TEAMS': [
            {
                'title': 'Mens',
                'list': [
                    ('m1', 'Mens 1sts',),
                    ('m2', 'Mens 2nds',),
                    ('m3', 'Mens 3rds',),
                    ('m4', 'Mens 4ths',),
                    ('m5', 'Mens 5ths',),
                ],
            },
            {
                'title': 'Ladies',
                'list': [
                    ('l1', 'Ladies 1sts',),
                    ('l2', 'Ladies 2nds',),
                    ('l3', 'Ladies 3rds',),
                    ('l4', 'Ladies 4ths',),
                ],
            },
            {
                'title': 'Other',
                'list': [
                    ('mixed', 'Mixed',),
                    ('indoor', 'Indoor',),
                    ('vets', 'Vets',),
                ],
            },
        ],
    }
    return context
