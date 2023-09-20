class SampleClass:
    sample_class_attr = "Sample Class Attribute"
    def __init__(self):
        super().__init__()
        self.__private_value = 0
        self.public_value = 5

    def get_value(self):
        return self.__private_value

    def set_value(self, value):
        self.__private_value = value

if __name__ == "__main__":
    sampleClass = SampleClass()
    print(sampleClass.sample_class_attr)
    print(sampleClass.get_value())
    print(sampleClass.public_value) 
    print(sampleClass._private_value)