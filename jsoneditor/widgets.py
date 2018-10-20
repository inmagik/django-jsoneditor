from __future__ import absolute_import

from django import forms
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from django.core.serializers.json import DjangoJSONEncoder
from django.template.loader import render_to_string
from django.utils.encoding import force_text
from django.utils.functional import Promise
from django.utils.html import conditional_escape
from django.utils.safestring import mark_safe
from django.utils.translation import get_language
import json

try:
    # Django >=1.7
    from django.forms.utils import flatatt
except ImportError:
    # Django <1.7
    from django.forms.util import flatatt


#TODO : ????
class LazyEncoder(DjangoJSONEncoder):

    def default(self, obj):
        if isinstance(obj, Promise):
            return force_text(obj)
        return super(LazyEncoder, self).default(obj)


json_encode = LazyEncoder().encode



class JSONEditorWidget(forms.Textarea):
    """
    Widget providing JSON EHDITOR
    """
    class Media:
        js = ()

        try:
            js += (
                settings.STATIC_URL + 'jsoneditor/json-editor-0.7.26/dist/jsoneditor.js',
                settings.STATIC_URL + 'jsoneditor/bootstraptheme.js',
                settings.STATIC_URL + 'jsoneditor/jsoneditor-init.js',
                '//cdnjs.cloudflare.com/ajax/libs/ace/1.2.3/ace.js',


            )
        except AttributeError, e:
            raise e

    def __init__(self, schema, *args, **kwargs):
        super(JSONEditorWidget, self).__init__(*args, **kwargs)
        self.schema = schema.copy()
        #todo: validate schema

    def render(self, name, value, attrs=None):
        if value is None:
            value = ''
        final_attrs = self.build_attrs(attrs, name=name)
        self._set_schema()

        return mark_safe(render_to_string('jsoneditor/widget.html', {
            'final_attrs': flatatt(final_attrs),
            'value': value,
            'id': final_attrs['id'],
            'schema': json.dumps(self.schema)
        }))

    def _set_schema(self):
        #TODO: do something to alter schema?
        return
