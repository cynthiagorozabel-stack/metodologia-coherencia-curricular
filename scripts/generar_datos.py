"""Datos inventados desde cero. No lee ni transforma registros de personas reales.
Copyright 2026 Cynthia Mercedes Gorozabel Villavicencio. Ver LICENSE.
"""
from pathlib import Path
import json, random, sys
ROOT=Path(__file__).resolve().parents[1]
SEED=20261021
CAPS={'ND':15,'NP':10,'NTA':10,'NE':15}
# Distribución ficticia para enseñar trazabilidad, no obtenida del caso real.
PLAN={1:(1,[3,2,2,3]),2:(1,[6,4,4,6]),3:(1,[6,4,4,6]),4:(2,[8,5,5,7]),5:(2,[7,5,5,8])}
CRITERIOS={
1:['Modela una ecuación contextualizada','Resuelve un sistema y muestra procedimiento','Verifica y explica su solución','Resuelve un problema individual'],
2:['Representa desigualdades del problema','Obtiene la región factible','Justifica la interpretación de restricciones','Aplica un método gráfico'],
3:['Identifica los elementos de la ecuación','Representa los casos de pendiente','Explica la relación entre pendiente y gráfica','Interpreta una recta en contexto'],
4:['Aplica reglas de logaritmos','Resuelve una tarea con funciones','Comprueba el procedimiento utilizado','Resuelve un problema de aplicación'],
5:['Organiza datos en un modelo matricial','Ejecuta un procedimiento de optimización','Explica pasos y restricciones del modelo','Aplica simplex en una tarea individual'],
}

def build(seed=SEED):
 rng=random.Random(seed)
 first=['Alba','Bruno','Clara','Dario','Elia','Fabio','Gala']
 last=['Lumen','Cedral','Nuvia','Terral','Brisalia']
 people=[{'id':f'DEMO-{i+1:03}','nombre_ficticio':f'{first[i%7]} {last[i//7]}','tipo':'PERSONA_FICTICIA'} for i in range(35)]
 details=[];records=[]
 for person in people:
  cycles={1:{c:0 for c in CAPS},2:{c:0 for c in CAPS}}
  for unit,(cycle,maximums) in PLAN.items():
   for k,(component,maximum) in enumerate(zip(CAPS,maximums)):
    score=rng.randint(0,maximum)
    cycles[cycle][component]+=score
    details.append({'persona_id':person['id'],'silabo_id':'SIM-S1','unidad':unit,'RA':f'RA{unit}','ciclo':cycle,'componente':component,'actividad_id':f'SIM-U{unit}-{component}','criterio_id':f'SIM-U{unit}-{component}-C1','criterio':CRITERIOS[unit][k],'puntos':score,'maximo':maximum,'tipo':'SINTETICO_PROPUESTA_NO_VALIDADA'})
  records.append({'id':person['id'],'nombre_ficticio':person['nombre_ficticio'],'ND':cycles[2]['ND'],'NP':cycles[2]['NP'],'NTA':cycles[2]['NTA'],'NE':cycles[2]['NE'],'NF':sum(cycles[2].values()),'TOT':sum(sum(c.values()) for c in cycles.values()),'asistencia':None if person['id'] in ('DEMO-007','DEMO-031') else rng.randrange(0,101,5),'observacion':'SIN_DICTAMEN_SIMULADO','tipo':'SINTETICO_NO_OFICIAL'})
 metadata={'tipo':'DATOS_SINTETICOS_NO_OFICIALES','semilla':seed,'personas':35,'autora':'Cynthia Mercedes Gorozabel Villavicencio','aviso':'No son filas reales renombradas. No representan resultados empíricos ni aprobación.','firmas':[{'rol':'Elaboración del ejemplo','nombre_ficticio':'Ines Nuvia','firma':'Firma ficticia — sin validez'},{'rol':'Revisión del ejemplo documental','nombre_ficticio':'Samuel Cedral','firma':'Firma ficticia — sin validez'}]}
 aggregate={'metadatos':metadata,'columnas':{'ND':'Nota Docencia','NP':'Nota Práctica','NTA':'Nota Trabajo Autónomo','NE':'Nota Examen','NF':'Suma segundo ciclo','TOT':'Suma primero y segundo ciclo','asistencia':'Sobre 100 o null'},'maximos_segundo_ciclo':CAPS,'registros':records}
 enriched={'metadatos':metadata,'nota':'Vínculos inventados para una propuesta de registro. Su disponibilidad no implica validez del criterio ni logro acreditado. No se reconstruyen notas por RA del caso real.','registros':details}
 syllabi=[]
 units=['Ecuaciones lineales','Desigualdades','Ecuación de la recta','Funciones','Matrices y simplex']
 ra=['Aplicar y resolver ecuaciones lineales en situaciones contextualizadas','Aplicar desigualdades y método gráfico a problemas','Identificar la ecuación, analizar la pendiente y graficar','Calcular operaciones con funciones logarítmicas en problemas','Aplicar matrices a optimización mediante simplex']
 for i,period in enumerate(['2025-A','2025-B','2026-B'],1):
  syllabi.append({'id':f'SIM-S{i}','periodo':period,'institucion':'Instituto Horizonte Curricular — institución ficticia','asignatura':'Matemáticas para Gestión — ejemplo ficticio','docente':'Ines Nuvia — persona ficticia','firma':'Firma ficticia — sin validez','tipo':'SILABO_SINTETICO_RESUMIDO','objetivo':'Desarrollar pensamiento lógico y aplicación matemática en problemas de gestión','unidades':[{'unidad':u,'tema':units[u-1],'RA':ra[u-1],'taxonomia':'Comprensión' if u==3 else 'Aplicación','actividad':'Ejercicios, gráficas y evidencia contextual' if u==3 else 'Ejercicios y problemas','precision_adicional':'Formulación de problemas; ensayo argumentativo; portafolio reflexivo según unidad' if i==3 else None} for u in range(1,6)]})
 return aggregate,enriched,syllabi

def main():
 out=ROOT/'datos/sinteticos';out.mkdir(parents=True,exist_ok=True)
 aggregate,enriched,syllabi=build()
 for name,data in [('acta_agregada.json',aggregate),('registro_ampliado.json',enriched),('silabos_demostracion.json',syllabi)]:
  (out/name).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
 docs=ROOT/'ejemplos';docs.mkdir(exist_ok=True)
 text='# Acta de demostración — DATOS SINTÉTICOS\n\nInstituto Horizonte Curricular, institución ficticia. Matemáticas para Gestión. Este documento no es un acta oficial ni corresponde a estudiantes reales.\n\n'
 text+='| ID | Nombre ficticio | ND | NP | NTA | NE | NF segundo ciclo | TOT ambos ciclos | Asistencia /100 |\n|---|---|---|---|---|---|---|---|---|\n'
 for r in aggregate['registros']:
  text+='| '+' | '.join(str(r[k]) if r[k] is not None else 'Sin dato' for k in ['id','nombre_ficticio','ND','NP','NTA','NE','NF','TOT','asistencia'])+' |\n'
 text+='\n## Rótulos ficticios de ejemplo\n\n'
 for f in aggregate['metadatos']['firmas']:text+=f"- {f['rol']}: {f['nombre_ficticio']}. **{f['firma']}**.\n"
 text+='\nNo existe dictamen de acreditación. Autoría del material: Cynthia Mercedes Gorozabel Villavicencio.\n'
 (docs/'ACTA_SINTETICA.md').write_text(text,encoding='utf-8')
 for s in syllabi:
  text=f"# {s['id']} — Sílabo resumido de demostración\n\n**DOCUMENTO FICTICIO — SIN VALIDEZ**\n\n{s['institucion']}\n\n{s['asignatura']}, período {s['periodo']}.\n\nObjetivo: {s['objetivo']}.\n\n| Unidad | Tema | RA sintetizado | Taxonomía | Actividad |\n|---|---|---|---|---|\n"
  for u in s['unidades']:text+=f"| {u['unidad']} | {u['tema']} | {u['RA']} | {u['taxonomia']} | {u['actividad']} |\n"
  if s['id']=='SIM-S3':text+='\nEsta versión ilustra mayor especificación de tareas: formulación de problemas, ensayo argumentativo y portafolio reflexivo. La redacción es resumida y no transcribe un documento oficial.\n'
  text+=f"\nResponsable ficticia: {s['docente']}. **{s['firma']}**.\n\nAutoría del material: Cynthia Mercedes Gorozabel Villavicencio.\n"
  (docs/(s['id']+'.md')).write_text(text,encoding='utf-8')
 print('Generados 35 registros agregados, 700 criterios ficticios y 3 silabos de demostracion.')
if __name__=='__main__':main()
