def test_decorator(func):
    def wrapp():
        print('начало')
        func()
        print('конец')
    return wrapp
@test_decorator
def text_message():
    print('text')
text_message()