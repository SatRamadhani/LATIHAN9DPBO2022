class Hunian():
    # Constructor with complete data as its parameter (add "luas tanah" as additional attribute).
    def __init__(self, jenis, jml_penghuni = 1, jml_kamar = 1, luas_tanah = 0):
        self.jenis = jenis
        self.jml_penghuni = jml_penghuni
        self.jml_kamar = jml_kamar
        self.luas_tanah = luas_tanah

    # Get residence's type.
    def get_jenis(self):
        return self.jenis

    # Get total residents.
    def get_jml_penghuni(self):
        return self.jml_penghuni

    # Get total rooms.
    def get_jml_kamar(self):
        return self.jml_kamar

    # Get land area.
    def get_luas_tanah(self):
        return self.luas_tanah

    # Get document.
    def get_dokumen(self):
        pass

    # Get data summary.
    def get_summary(self):
        return "Hunian : "+ self.jenis + ".\n" + "Luas tanah : " + str(self.luas_tanah) + "m^2.\n" + "Jumlah kamar : " + str(self.jml_kamar) + " kamar.\n" + "Ditempati oleh : " + str(self.jml_penghuni) + " orang.\n\n"

    # I don't know why owner's name isn't included in this class, considering
    # it's in every subclass. However, there's so much to fix if I move the
    # attribute. Also it seems weird if some subclass have only one overriding
    # attribute and/or method, so I decided to leave it. :D #