# modeltranslation-grappelli

This package allow usage modeltranslation packages with grappelli admin interface.

## Installation

### Requirments

<table>
<tr>
<td>Modeltranslation-grappelli</td><td>Django</td>
</tr><tr>
<td>2.0.0</td><td>1.7</td>
</tr><tr>
<td>1.0.0</td><td>1.4-1.6</td>
</tr>
</table>

### Using pip

```bash
pip install modeltranslation-grappelli
```

### Configure

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
