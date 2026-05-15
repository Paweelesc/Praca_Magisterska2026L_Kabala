

# Praca_Magisterska2026L_Kabala

Autorska aplikacja do lokalnego przeprowadzania testu odsłuchowego typu **MUSHRA** do porównania jakości auralizacji nagrań instrumentów muzycznych.

## Zawartość repozytorium

* `audio/` — pliki audio wykorzystywane w teście
* `local_mushra_fixed.py` — lokalna aplikacja testowa w Pythonie
* `README.md` — opis projektu

## Wymagania

Do uruchomienia aplikacji potrzebne są:

* Python 3.10 lub nowszy
* biblioteki:

  * `sounddevice`
  * `soundfile`

## Instalacja

W terminalu uruchom:

```
pip install sounddevice soundfile
```

## Uruchomienie

Przejdź do folderu projektu i uruchom:

```
python local_mushra_fixed.py
```

## Struktura folderów

Projekt powinien mieć taką strukturę:

```
Praca_Magisterska2026L_Kabala/
├── audio/
│   ├── anchor/
│   ├── Anchor_mono/
│   ├── Auraliz_12/
│   ├── Auraliz_24/
│   ├── auraliz_48/
│   └── ref/
├── local_mushra_fixed.py
└── README.md
```

## Opis działania

Aplikacja umożliwia przeprowadzenie testu MUSHRA dla 10 zadań odsłuchowych.

W każdym zadaniu uczestnik porównuje:

* referencję,
* 3 wersje auralizacji,
* ukrytą referencję,
* kotwicę.

Próbki są losowo przypisywane do etykiet **A–E**.

Każda próbka oceniana jest w skali **0–100**.

## Wyniki

Po zakończeniu testu aplikacja:

* wyświetla podsumowanie wyników,
* pokazuje szczegółowe oceny,
* umożliwia eksport danych do pliku `.csv`.

## Uwagi

* Aplikacja działa lokalnie, bez użycia przeglądarki.
* Pliki audio muszą znajdować się dokładnie w folderze `audio/`.
* Ścieżki do plików są zapisane bezpośrednio w kodzie `local_mushra_fixed.py`.

## Autor

Paweł Kabala
