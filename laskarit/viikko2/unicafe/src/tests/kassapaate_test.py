import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.maksukortti = Maksukortti(1000)

    def test_alkusaldo_on_oikein(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000)

    def test_edullisia_myyty_alussa_nolla(self):
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_maukkaita_myyty_alussa_nolla(self):
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_edullisen_ostaminen_kateisella_jos_maksu_riittava(self):
        vaihtoraha = self.kassapaate.syo_edullisesti_kateisella(300)

        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1002.40)
        self.assertEqual(self.kassapaate.edulliset, 1)
        self.assertEqual(vaihtoraha, 60)

    def test_edullisen_ostaminen_kateisella_jos_maksu_ei_riittava(self):
        vaihtoraha = self.kassapaate.syo_edullisesti_kateisella(200)

        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000.00)
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(vaihtoraha, 200)

    def test_maukkaan_ostaminen_kateisella_jos_maksu_riittava(self):
        vaihtoraha = self.kassapaate.syo_maukkaasti_kateisella(500)

        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1004.00)
        self.assertEqual(self.kassapaate.maukkaat, 1)
        self.assertEqual(vaihtoraha, 100)

    def test_maukkaan_ostaminen_kateisella_jos_maksu_ei_riittava(self):
        vaihtoraha = self.kassapaate.syo_maukkaasti_kateisella(200)

        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000.00)
        self.assertEqual(self.kassapaate.maukkaat, 0)
        self.assertEqual(vaihtoraha, 200)

    def test_edullisen_ostaminen_kortilla_jos_saldo_riittava(self):
        viesti = self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)

        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000.00)
        self.assertEqual(self.kassapaate.edulliset, 1)
        self.assertEqual(viesti, True)

    def test_edullisen_ostaminen_kortilla_jos_saldo_ei_riittava(self):
        kortti = Maksukortti(100)
        viesti = self.kassapaate.syo_edullisesti_kortilla(kortti)

        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000.00)
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(viesti, False)

    def test_maukkaan_ostaminen_kortilla_jos_saldo_riittava(self):
        viesti = self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)

        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000.00)
        self.assertEqual(self.kassapaate.maukkaat, 1)
        self.assertEqual(viesti, True)

    def test_maukkaan_ostaminen_kortilla_jos_saldo_ei_riittava(self):
        kortti = Maksukortti(100)
        viesti = self.kassapaate.syo_maukkaasti_kortilla(kortti)

        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000.00)
        self.assertEqual(self.kassapaate.maukkaat, 0)
        self.assertEqual(viesti, False)

    def test_kortin_lataaminen_kerryttaa_kassaa(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 100)

        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1001.00)

    def test_kortin_lataaminen_kasvattaa_kortin_saldoa(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 100)

        self.assertEqual(self.maksukortti.saldo_euroina(), 11.00)

    def test_kortin_lataaminen_negatiivisella_summalla_kerryta_kassaa(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, -100)

        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000.00)

    def test_kortin_lataaminen_negatiivisella_summalla_ei_kasvata_saldoa(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, -100)

        self.assertEqual(self.maksukortti.saldo_euroina(), 10.00)