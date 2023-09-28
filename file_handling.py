# with open('filename.txt', 'r') as file:
#     data = file.read()


class ContextManager:
    def __enter__(self):
        print("File is entered")
        return self
    def __exit__(self, exception_type, exception_value, exception_traceback):
        print("File is exited")

with ContextManager() as context:
    print("inside file")