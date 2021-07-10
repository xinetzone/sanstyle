class Embed:
    """
    Generic class to embed an embed in an IPython notebook
    """

    embed = \
        """<embed typeName="{typeName}" width="{width}" height="{height}" src="{src} {params}">"""

    def __init__(self, typeName, src, width, height, **kwargs):
        self.typeName = typeName
        self.src = src
        self.width = width
        self.height = height
        self.params = kwargs

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
        return self.embed.format(
            typeName=self.typeName,
            src=self.src,
            width=self.width,
            height=self.height,
            params=params)
