²to be able to see models in admin space, we need to registerthe models in admin.py

```python
# Register your models here.
from .models import Question, Choice

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["question_text"]}),
        ("Date information", {"fields": ["pub_date"]}),
    ]

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
```

```python 
class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3
```
this declare that in admin/questions will be enough space to add 3 choices

we can also use "TabularInline" for a more compact view
