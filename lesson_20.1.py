def your_name(name):
    def say_hello():
        print(f'Hello {name}')

    return say_hello


your_name('Ilya')
