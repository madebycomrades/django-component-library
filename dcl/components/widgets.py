from django.forms import (
    EmailInput,
    DateInput,
    HiddenInput,
    Select,
    TextInput,
    Textarea
)


class ComponentWidgetContextMixin():

    def get_context(self, name, value, attrs):
        context = {}
        context['data'] = {
            'name': name,
            'is_hidden': self.is_hidden,
            'required': self.is_required,
            'value': self.format_value(value),
            'attrs': self.build_attrs(self.attrs, attrs),
            'template_name': self.template_name,
        }
        return context


class ComponentEmailInput(ComponentWidgetContextMixin, EmailInput):
    template_name = 'components/form/FormInput/FormInput.html'

    def get_context(self, name, value, attrs):
        context = super(ComponentEmailInput, self).get_context(
            name, value, attrs
        )
        context['data']['type'] = 'email'
        return context


class ComponentDateInput(ComponentWidgetContextMixin, DateInput):
    template_name = 'components/form/FormInput/FormInput.html'

    def get_context(self, name, value, attrs):
        context = super(ComponentDateInput, self).get_context(
            name, value, attrs
        )
        context['data']['type'] = 'date'
        return context


class ComponentTextInput(ComponentWidgetContextMixin, TextInput):
    template_name = 'components/form/FormInput/FormInput.html'

    def get_context(self, name, value, attrs):
        context = super(ComponentTextInput, self).get_context(
            name, value, attrs
        )
        context['data']['type'] = 'text'
        return context


class ComponentHiddenInput(ComponentWidgetContextMixin, HiddenInput):
    template_name = 'components/form/FormInput/FormInput.html'
    is_hidden = True

    def get_context(self, name, value, attrs):
        context = super(ComponentHiddenInput, self).get_context(
            name, value, attrs
        )
        context['data']['type'] = 'hidden'
        return context


class ComponentTelInput(ComponentWidgetContextMixin, TextInput):
    template_name = 'components/form/FormInput/FormInput.html'

    def get_context(self, name, value, attrs):
        context = super(ComponentTelInput, self).get_context(
            name, value, attrs
        )
        context['data']['type'] = 'tel'
        return context


class ComponentSelect(Select):
    template_name = 'components/form/FormSelect/FormSelect.html'

    def get_context(self, name, value, attrs):
        context = super(ComponentSelect, self).get_context(name, value, attrs)
        context['data'] = context['widget']
        # Map options to match component. Component doesn't support optgroups
        if (
            len(context['widget']['optgroups']) > 0 and
            len(context['widget']['optgroups'][0]) > 1
        ):
            context['data']['options'] = context['widget']['optgroups'][0][1]
        return context


class ComponentTextarea(ComponentWidgetContextMixin, Textarea):
    template_name = 'components/form/FormTextarea/FormTextarea.html'
