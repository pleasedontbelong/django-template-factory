def add_class(field, class_name, disabled=False):
    attrs = {
        "class": field.field.widget.attrs.get('class', '') + ' ' + class_name
    }
    if disabled:
        attrs['disabled'] = True
    return field.as_widget(attrs=attrs)
