# Import superclass.
from hunian import Hunian

class Rumah(Hunian):
    # Constructor with complete data as its parameter.
    def __init__(self, nama_pemilik, jml_penghuni, jml_kamar, luas_tanah):
        super().__init__("Rumah", jml_penghuni, jml_kamar, luas_tanah)
        self.nama_pemilik = nama_pemilik

    # Get document.
    def get_dokumen(self):
        return "Izin Mendirikan Bangunan (IMB) a/n " + self.nama_pemilik

    # Get owner's name.
    def get_nama_pemilik(self):
        return self.nama_pemilik
   