# Distribuidora — lectura moderna

Entidades identificadas en el diagrama original: **LIBRO, EDITORIAL, TEMA, AUTOR, FACTURA, LIBRERÍA, PAGO** y el detalle de factura.

```mermaid
erDiagram
  EDITORIAL ||--o{ LIBRO : edita
  TEMA ||--o{ LIBRO : clasifica
  AUTOR }o--o{ LIBRO : escribe
  LIBRERIA ||--o{ FACTURA : recibe
  FACTURA ||--|{ DETALLE_FACTURA : contiene
  LIBRO ||--o{ DETALLE_FACTURA : aparece_en
  FACTURA ||--|| PAGO : tiene
```

La vista Mermaid prioriza legibilidad y normalización. Los ficheros Dia originales son la referencia histórica para las cardinalidades.
