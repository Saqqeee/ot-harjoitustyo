import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_kortin_saldo_on_alussa_oikein(self):
        self.assertEqual(self.maksukortti.saldo_euroina(), 10)

    def test_rahan_lataaminen_kasvattaa_saldoa_oikein(self):
        self.maksukortti.lataa_rahaa(100)

        self.assertEqual(self.maksukortti.saldo_euroina(), 11)

    def test_rahan_ottaminen_vahentaa_saldoa_oikein(self):
        self.maksukortti.ota_rahaa(100)

        self.assertEqual(self.maksukortti.saldo_euroina(), 9)

    def test_rahaa_ei_voi_vahentaa_yli_saldon(self):
        self.maksukortti.ota_rahaa(2000)

        self.assertEqual(self.maksukortti.saldo_euroina(), 10)

    def test_true_jos_saldo_riittaa(self):
        viesti = self.maksukortti.ota_rahaa(100)

        self.assertEqual(viesti, True)

    def test_false_jos_saldo_ei_riita(self):
        viesti = self.maksukortti.ota_rahaa(2000)

        self.assertEqual(viesti, False)

    def test_tulostus_nayttaa_oikean_saldon(self):
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")