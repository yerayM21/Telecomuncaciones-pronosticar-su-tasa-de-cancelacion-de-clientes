# Proyecto Final Bootcamp TripleTen
Al operador de telecomunicaciones Interconnect le gustaría poder pronosticar su tasa de cancelación de clientes. Si se descubre que un usuario o usuaria planea irse, se le ofrecerán códigos promocionales y opciones de planes especiales. El equipo de marketing de Interconnect ha recopilado algunos de los datos personales de sus clientes, incluyendo información sobre sus planes y contratos.
# Objectivos
- Entrenadar un modelo de aprendizaja Automatico 
- Para predecir tasa de cancelacion del cliente
- Característica objetivo: la columna `'EndDate'` es igual a `'No'`.

Métrica principal: AUC-ROC.

Métrica adicional: exactitud.

Criterios de evaluación:

- AUC-ROC < 0.75 
- 0.75 ≤ AUC-ROC < 0.81 
- 0.81 ≤ AUC-ROC < 0.85 
- 0.85 ≤ AUC-ROC < 0.87 
- 0.87 ≤ AUC-ROC < 0.88 
- AUC-ROC ≥ 0.88 

# Estructura del repositorio 
- datasets
   - Input
   - Output