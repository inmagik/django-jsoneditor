from __future__ import absolute_import

from django import forms
from django.db import models

from .widgets import JSONEditorWidget
from  django.contrib.postgres.fields import JSONField
from django.contrib.postgres.forms import JSONField as FormJSONField

class JSONSchemaField(JSONField):

    def __init__(self, *args, **kwargs):
        self.schema = kwargs.pop("schema", {})
        super(JSONSchemaField, self).__init__(*args, **kwargs)

    def formfield(self, **kwargs):
        defaults = {
            'form_class': self._get_form_class(),
            'schema': self.schema,
        }
        defaults.update(kwargs)
        return super(JSONSchemaField, self).formfield(**defaults)

    @staticmethod
    def _get_form_class():
        return JSONSchemaFormField


class JSONSchemaFormField(FormJSONField):

    def __init__(self, schema, extra_plugins=None, *args, **kwargs):
        kwargs.update({'widget': JSONEditorWidget(schema)})
        super(JSONSchemaFormField, self).__init__(*args, **kwargs)

try:
    from south.modelsinspector import add_introspection_rules
    add_introspection_rules([], ["^jsoneditor\.fields\.JSONSchemaField"])
except ImportError:
    pass
