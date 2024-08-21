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

# Resultados

Con los datos adquiridos, podemos decir que los clientes que abandonan los servicios tienen una tasa del 26.5% de los datos entregados, de los cuales la mayoría deja el servicio en el primer mes. Una buena estrategia sería darle más seguimiento a estos clientes durante el primer mes de uso del servicio para mantenerlos.

Además, notamos que estos clientes tienden a tener un alto cargo en sus pagos mensuales, en comparación con los clientes que se mantienen.

Los clientes que hacen su pago de forma electrónica, tienen un contrato mensual y contratan fibra óptica tienen mayor probabilidad de dejar el servicio.

Al realizar el entrenamiento de los modelos con los diferentes datos tratados, los mejores modelos para esta tarea que dieron buen resultado fueron `RandomForestClassifier` y `LogisticRegression`.

Cada uno de estos modelos tiene un `ROC_AUC` mayor de `0.75`, que era el valor buscado para considerar estos modelos de aprendizaje automático para ayudar en la detección de clientes que puedan dejar el servicio.

# Herramienta utilizadas 
 - pandas
 - numpy 
 - seaborn 
 - matplotlib
 - sklearn

