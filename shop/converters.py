class FourDigitYearConverter:
    regex = r'\d{4}'
    
    def to_python(self, value):
        return int(value)

    def to_url(self, Value):
        return '%04d' % value