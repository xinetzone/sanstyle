from string import Template

element_template = Template(
    '''<${tag} class="${className}" type="${typeName}" ${params}>${content}</${tag}>''')
null_element_template = Template(
    '''<${tag} class="${className}" type="${typeName}" ${params}>''')


class FrameElement:
    def __init__(self, tag, src, height,
                 width='100%',
                 typeName='text/html',
                 className='w3-card',
                 **kwargs):
        self.tag = tag
        self.typeName = typeName
        self.src = src
        self.width = width
        self.height = height
        self.params = kwargs
        self.className = className

    def _repr_html_(self):
        """return the embed iframe"""
        if self.params:
            try:
                from urllib.parse import urlencode  # Py 3
            except ImportError:
                from urllib import urlencode
            params = "?" + urlencode(self.params)
        else:
            params = ""
        config = {
            'tag': self.tag,
            'typeName': self.typeName,
            'src': self.src,
            'width': self.width,
            'height': self.height,
            'params': params,
            'className': self.className
        }
        return null_element_template.substitute(config)


def IFrame(src, height,
           width='100%',
           typeName='text/html',
           className='w3-card',
           **kwargs):
    '''<iframe>'''
    return FrameElement('iframe', src, height,
                        width,
                        typeName,
                        className,
                        **kwargs)


def Embed(src, height,
          width='100%',
          typeName='text/html',
          className='w3-card',
          **kwargs):
    '''<embed>'''
    return FrameElement('embed', src, height,
                        width,
                        typeName,
                        className,
                        **kwargs)
