from django import template
register = template.Library()

@register.tag(name='snippet')
def snippet(parser, token):
    try:
        tag_name, template_name = token.split_contents()
    except ValueError:
        raise template.TemplateSyntaxError(
            "%r tag requires a single snippet name" % token.contents.split()[0]
        )
    if not (template_name[0] == template_name[-1] and template_name[0] in ('"', "'")):
        raise template.TemplateSyntaxError(
            "%r tag's argument should be in quotes" % tag_name
        )

    return TemplateNode('snippets', template_name[1:-1])


class TemplateNode(template.Node):
    def __init__(self, folder, template_name):
        self.folder = folder
        self.template_name = template_name
    
    def render(self, context):
        t = context.template.engine.get_template(f'{self.folder}/{self.template_name}.html')
        return t.render( template.Context(context, autoescape=context.autoescape))