class Test:
    def test(self):
         phrase = input('Set a phrase ')
         assert len(phrase) < 15, 'The phrase must be less than 15 characters'