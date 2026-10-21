"""Comprueba integridad y alcance de datos sintéticos; no calcula promedios ni valida juicios.
Copyright 2026 Cynthia Mercedes Gorozabel Villavicencio. Ver LICENSE.
"""
from pathlib import Path
import json
ROOT=Path(__file__).resolve().parents[1]

def analyze(aggregate,enriched):
 rows=aggregate['registros'];details=enriched['registros'];caps=aggregate['maximos_segundo_ciclo']
 ids=[r['id'] for r in rows]
 assert len(rows)==35 and len(set(ids))==35
 assert len(details)==700
 assert all(r['NF']==sum(r[c] for c in caps) for r in rows)
 assert all(0<=r[c]<=cap for r in rows for c,cap in caps.items())
 assert all(0<=r['TOT']-r['NF']<=50 for r in rows)
 assert all(r['asistencia'] is None or 0<=r['asistencia']<=100 for r in rows)
 assert all(d['persona_id'] in ids and 0<=d['puntos']<=d['maximo'] for d in details)
 assert len({(d['persona_id'],d['criterio_id']) for d in details})==700
 for r in rows:
  ds=[d for d in details if d['persona_id']==r['id']]
  assert sum(d['puntos'] for d in ds)==r['TOT']
  for cycle in (1,2):
   for c,cap in caps.items():
    subset=[d for d in ds if d['ciclo']==cycle and d['componente']==c]
    assert sum(d['maximo'] for d in subset)==cap
    if cycle==2:assert sum(d['puntos'] for d in subset)==r[c]
 trace=[]
 for r in rows:
  for u in range(1,6):
   subset=[d for d in details if d['persona_id']==r['id'] and d['unidad']==u]
   trace.append({'persona_id':r['id'],'RA':f'RA{u}','criterios':[d['criterio_id'] for d in subset],'puntos_registrados':sum(d['puntos'] for d in subset),'maximo':sum(d['maximo'] for d in subset),'logro':'NO_ACREDITADO_POR_ESTE_ANALISIS','tipo':'SINTETICO'})
 return {'tipo':'RESULTADO_EXCLUSIVAMENTE_SINTETICO','integridad':{'filas':len(rows),'criterios':len(details),'sumas_consistentes':True,'asistencias_faltantes':sum(r['asistencia'] is None for r in rows)},'escenario_agregado':{'desempeno_por_RA':'NOT_CALCULABLE','dice':'Puntos por componente, acumulados y asistencia','dice_parcialmente':'Composición evaluativa por componente','no_dice':'Actividad, criterio y RA que originan cada nota'},'escenario_ampliado':{'trazabilidad':'VINCULOS_FICTICIOS_DISPONIBLES','logro_por_RA':'NO_SE_EMITE_DICTAMEN','limite':'Una relación estructural explícita no garantiza que el criterio sea válido ni que los puntos acrediten logro','rastreo':trace}}

def main():
 folder=ROOT/'datos/sinteticos'
 data=analyze(json.loads((folder/'acta_agregada.json').read_text(encoding='utf-8')),json.loads((folder/'registro_ampliado.json').read_text(encoding='utf-8')))
 out=ROOT/'resultados';out.mkdir(exist_ok=True)
 (out/'diagnostico_sintetico.json').write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
 r=json.loads((folder/'acta_agregada.json').read_text(encoding='utf-8'))['registros'][1]
 text=f'''# Resultado de la demostración sintética

**Datos ficticios, no resultados del caso real.** 35 registros, 700 criterios ficticios, sumas y máximos consistentes. No se calculan promedios ni se emite acreditación de RA.

## Escenario agregado

Los campos informan componentes, acumulado y asistencia. No identifican actividad, criterio o RA: desempeño por RA NOT_CALCULABLE.

## Ejemplo DEMO-002, sin correspondencia con E02 real

| Docencia | Práctica | Trabajo Autónomo | Examen | NF segundo ciclo | TOT ambos ciclos | Asistencia |
|---|---|---|---|---|---|---|
| {r['ND']} | {r['NP']} | {r['NTA']} | {r['NE']} | {r['NF']} | {r['TOT']} | {r['asistencia']} |

## Escenario ampliado

Los vínculos actividad-criterio-RA son explícitos por construcción ficticia. Se pueden seguir las contribuciones sin repartir notas a posteriori. Esto demuestra disponibilidad estructural de un vínculo propuesto; no valida los criterios, no reconstruye el caso real y no permite declarar logrado un RA sin una regla fundamentada y evidencia válida.

Los nombres y firmas del ejemplo son ficticios y sin validez. Autoría: Cynthia Mercedes Gorozabel Villavicencio.
'''
 (out/'DEMO.md').write_text(text,encoding='utf-8')
 print('Integridad sintetica comprobada; dictamen por RA no emitido. Ver resultados/DEMO.md.')
if __name__=='__main__':main()
