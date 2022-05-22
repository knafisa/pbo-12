class negara:
    def jumlah_negara(self):
        print("jumlah negara ada banyak")
    def capital(self):
        print("setiap negara punya ibu kota")
    def language(self):
        print("setiap negara beda bahasa")
class India():
    def capital(self):
        print("ibukota delhi")
    def language(self):
        print("bahasa hindi")
class Indonesia():
    def capital(self):
        print("ibukota jakarta")
    def language(self):
        print("bahasa indonesia")

obj_india = India()
obj_indo = Indonesia()
obj_india.capital()
obj_india.language()

for negara in (obj_india, obj_indo):
    negara.capital()
    negara.language()