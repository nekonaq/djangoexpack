from django.contrib.humanize.templatetags.humanize import NaturalTimeFormatter


class NaturalTimeJaFormatter(NaturalTimeFormatter):
    @classmethod
    def string_for(cls, value):
        ret = super().string_for(value)
        return 'と'.join(ret.split(', ')).replace('\xa0', '')
