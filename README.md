# Navegador Municipal RD

Datos abiertos y verificables sobre los gobiernos locales de la República Dominicana.
Piloto: Distrito Nacional, Santo Domingo, Santiago, San Cristóbal y La Altagracia (66 ayuntamientos y juntas de distrito municipal).

El sitio es un único archivo, `index.html`, con los datos y el mapa incluidos. Se publica con GitHub Pages.

## Estructura

- `index.html`: el sitio publicado.
- `scripts/template.html`: la plantilla del sitio, con marcadores `__DATA__`, `__GEO__` y `__ASP__`.
- `data/data.json`: datos de cada gobierno local (resultados, censo, SISMAP, presupuesto, concejo).
- `data/geo.json`: límites simplificados para el mapa (ONE / HDX COD-AB, válidos desde 2021-06-29).
- `data/asp.json`: aspirantes a 2028, generado desde la pestaña Personas del libro de trabajo.
- `scripts/build_page.py`: une la plantilla y los datos en `index.html`.
- `scripts/build_asp.py`: convierte la pestaña Personas en `data/asp.json`.

## Fuentes

JCE, ONE, MAP (SISMAP Municipal), DIGEPRES y FEDOMU. Detalle, definiciones y limitaciones en la página «Metodología y fuentes» del sitio.

## Neutralidad

El sitio no apoya a ningún partido, candidato ni aspirante.
