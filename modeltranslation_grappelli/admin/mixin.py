# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from modeltranslation.admin import TabbedTranslationAdmin, TranslationAdmin


class CustomMinTabbedTranslationAdmin(TranslationAdmin):
    class Media:
        js = (
            'modeltranslation-grappelli/js/force_jquery.js',
            'modeltranslation-grappelli/js/tabbed_translation_fields.js',
        )
        css = {
            'all': (
                'modeltranslation-grappelli/css/tabbed_translation_fields.css',
                'modeltranslation-grappelli/css/custom_tabbed_translation_fields.css'
            ),
        }


class MinTabbedTranslationAdmin(TabbedTranslationAdmin):
    class Media:
        css = {
            'all': (
                'modeltranslation-grappelli/css/tabbed_translation_fields.css',
                'modeltranslation-grappelli/css/custom_tabbed_translation_fields.css'
            ),
        }