class Human:

    name="Mert"

    def __init__(self,name):
        self.name=name
        print("Bir human instance üretildi")

    def talk(self,sentence):
     
        print(f"{self.name}: {sentence}")
    def walk(self):
        print(f"{self.name} is walking")

    def __str__(self) -> str:
        return f"STR function result {self.name}"

human1=Human()
human1.name="Hasan"
human1.talk("Merhaba Ali")
human1.walk()

human2=Human()
human2.name="Ali"
human2.talk("Selam Hasan")

Human("Veli").talk("Naber")