# poisson-exposure-forge

## Français

Générer des événements conditionnés par une exposition déclarée.

Données fictives ; aucun accès réseau ni secret requis.

```sh
python -m poisson_exposure_forge examples/demo.json --lang fr
python -m unittest discover -s tests -v
```

### Méthode et différence

Génère des comptages Poisson classiques avec lambda=taux×exposition et graine fixée ; retourne taux normalisé plutôt qu’une comparaison brute des comptes.

### Limites

Indépendance et taux constant déclarés, lambda≤100 ; pas de surdispersion ni validation Jev ou données réelles.

### Validation

Tests de domaine, cas limites et interface FR/EN/ES. La CI teste Python 3.11/3.13 et exécute la wheel installée hors du checkout. JSON conserve les identifiants techniques et les données fournis. Erreur d’entrée : code de sortie 2.

## English

Generate events conditional on declared exposure.

Synthetic data; no network access or secret required.

```sh
python -m poisson_exposure_forge examples/demo.json --lang en
python -m unittest discover -s tests -v
```

### Method and difference

Generates classical Poisson counts with lambda=rate×exposure and fixed seed; returns exposure-normalized rates rather than raw-count comparisons.

### Limits

Declared independence and constant rate, lambda≤100; no overdispersion, Jev validation or real data.

### Validation

Domain tests, boundary cases and FR/EN/ES interface. CI tests Python 3.11/3.13 and runs the installed wheel outside the checkout. JSON preserves technical identifiers and supplied data. Invalid input exits with code 2.

## Español

Generar eventos condicionados por exposición declarada.

Datos sintéticos; no requiere red ni secretos.

```sh
python -m poisson_exposure_forge examples/demo.json --lang es
python -m unittest discover -s tests -v
```

### Método y diferencia

Genera conteos Poisson clásicos con lambda=tasa×exposición y semilla fija; devuelve tasas normalizadas por exposición.

### Límites

Independencia y tasa constante declaradas, lambda≤100; sin sobredispersión, validación Jev ni datos reales.

### Validación

Pruebas de dominio, casos límite e interfaz FR/EN/ES. CI prueba Python 3.11/3.13 y ejecuta la wheel instalada fuera del repositorio. JSON conserva identificadores técnicos y datos proporcionados. Entrada inválida termina con código 2.

## Sources / Fuentes

- https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.poisson.html
