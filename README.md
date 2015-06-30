# modeltranslation-grappelli

This package allow usage modeltranslation packages with grappelli admin interface.

## Usage

Install package.

```bash
pip install modeltranslation-grappelli
```

Include to installed apps.

```python
INSTALLED_APPS = (
    ...
    'modeltranslation_grappelli',
)
```

And inherit your admin class from this mixin.

```python
from modeltranslation_grappelli.admin.mixin import CustomMinTabbedTranslationAdmin

class YourModelAdmin(CustomMinTabbedTranslationAdmin):
    pass
```