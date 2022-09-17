
from app.mini_calc import Minicalc

class TestMiniCalc:
    def setup_method(self):
        print('Se executa la inceput')
        self.calc = Minicalc()

    def teardown_method(self):
        print('Se executa la final')

    def test_adunare(self):
        assert self.calc.adunare(10,10) == 20, 'Adunarea nu functioneaza corect'

    def test_scadere(self):
        assert self.calc.scardere(-100,10) == -110, 'Adunarea nu functioneaza corect'

    def test_inmultire(self):
        assert self.calc.inmultire(12,13) == 156, 'Inmultirea nu functioneza corect'

    def test_impartire(self):
        assert self.calc.impartire(100,2) == 50, 'Impartirea nu functioneaza corect'

