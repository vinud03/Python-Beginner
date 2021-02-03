class apple:
    manufacturer ='Apple Inc.'
    contactwebsite = "www.aaple.com/contact"

    def contactdetails(self):
        print("To contact us, log on to",self.contactwebsite)


class macbook(apple):
    def __init__(self):
        self.yearofmanufacturer=2017

    def manufacturedetails(self):
        print("This macbookwas manufactured in the year {} by {}".format(self.yearofmanufacturer,self.manufacturer))


macbook = macbook()
macbook.manufacturedetails()
macbook.contactdetails()
