"""Pruebas de integridad y de límites de inferencia de la demostración pública."""
import unittest,sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from generar_datos import build
from analizar_datos import analyze

class Demonstration(unittest.TestCase):
 def test_reproducibilidad_sin_originales(self):
  self.assertEqual(build(42),build(42))
  self.assertNotEqual(build(42)[0]['registros'],build(43)[0]['registros'])
 def test_integridad_y_limite(self):
  a,b,_=build();r=analyze(a,b)
  self.assertEqual(r['integridad']['filas'],35)
  self.assertEqual(r['integridad']['criterios'],700)
  self.assertEqual(r['integridad']['asistencias_faltantes'],2)
  self.assertEqual(r['escenario_agregado']['desempeno_por_RA'],'NOT_CALCULABLE')
  self.assertEqual(r['escenario_ampliado']['logro_por_RA'],'NO_SE_EMITE_DICTAMEN')
 def test_detecta_corrupcion_de_suma(self):
  a,b,_=build();a['registros'][0]['NF']+=1
  with self.assertRaises(AssertionError):analyze(a,b)
 def test_detecta_vinculo_huerfano(self):
  a,b,_=build();b['registros'][0]['persona_id']='NO_EXISTE'
  with self.assertRaises(AssertionError):analyze(a,b)
 def test_detecta_criterio_fuera_de_escala(self):
  a,b,_=build();b['registros'][0]['puntos']=999
  with self.assertRaises(AssertionError):analyze(a,b)

if __name__=='__main__':unittest.main()
