# Import superclass.
from hunian import Hunian

class Apartemen(Hunian):
    # Constructor with complete data as its parameter.
    def __init__(self, nama_pemilik, jml_penghuni, jml_kamar, luas_tanah):
        super().__init__("Apartemen", jml_penghuni, jml_kamar, luas_tanah)
        self.nama_pemilik = nama_pemilik

    # Get document.
    def get_dokumen(self):
        return "Sertifikat Hak Milik Atas Satuan Rumah Susun (SHMSRS) a/n " + self.nama_pemilik + "."

    # Get owner's name.
    def get_nama_pemilik(self):
        return self.nama_pemilik
        