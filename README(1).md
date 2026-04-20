# Testy odsłuchowe — Auralizacja
## Zawartość

- `mushra_test.html` — Test MUSHRA (skala 0–100, ocena globalna)
- `test_parametryczny.html` — Test parametryczny (skala 1–5, barwa/przestrzenność/pogłosowość)
- `audio/` — folder na pliki audio (stwórz go sam)

---

## Jak uruchomić

### 1. Skopiuj pliki audio

Stwórz folder `audio/` obok plików HTML i wrzuć do niego swoje nagrania:

```
projekt/
├── mushra_test.html
├── test_parametryczny.html
├── README.md
└── audio/
    ├── skrzypce_sala_ref.wav
    ├── skrzypce_sala_auraliz.wav
    ├── skrzypce_sala_anchor.wav      ← plik referencyjny przepuszczony przez LP ~3500 Hz
    ├── fortepian_koncert_ref.wav
    ├── fortepian_koncert_auraliz.wav
    ├── fortepian_koncert_anchor.wav
    ├── gitara_studio_ref.wav
    ├── gitara_studio_auraliz.wav
    └── gitara_studio_anchor.wav
```

### 2. Uruchom przez serwer lokalny (WYMAGANE dla audio)

Przeglądarki blokują ładowanie plików audio z dysku bez serwera.
Użyj jednej z metod:

**VS Code — Live Server (najprostsze):**
1. Zainstaluj rozszerzenie "Live Server" w VS Code
2. Kliknij prawym przyciskiem na `mushra_test.html`
3. Wybierz "Open with Live Server"

**Python (terminal):**
```bash
cd folder_z_plikami
python -m http.server 8000
# Otwórz: http://localhost:8000/mushra_test.html
```

**Node.js:**
```bash
npx serve .
```

---

## Jak dostosować zadania

W obu plikach HTML na górze skryptu `<script>` znajdziesz tablicę `TASKS`:

```javascript
const TASKS = [
  {
    id: 1,
    instrument: 'Skrzypce',
    room: 'Sala kameralna',
    position: 'Na wprost źródła',
    refFile: 'audio/skrzypce_sala_ref.wav',
    // mushra_test.html ma tu też tablicę samples[] z typami próbek
  },
  // ...
];
```

Zmień nazwy plików i opisy na swoje. Możesz dodać więcej zadań kopiując blok `{ id: ... }`.

---

## Co robi kotwica (anchor)?

W teście MUSHRA kotwica to próbka o celowo obniżonej jakości.
Najłatwiej ją wygenerować w Audacity lub Python:

```python
import numpy as np
from scipy.io import wavfile
from scipy.signal import butter, sosfilt

def make_anchor(input_file, output_file, cutoff=3500):
    sr, data = wavfile.read(input_file)
    sos = butter(4, cutoff / (sr / 2), btype='low', output='sos')
    filtered = sosfilt(sos, data.astype(float), axis=0)
    wavfile.write(output_file, sr, filtered.astype(data.dtype))

make_anchor('audio/skrzypce_sala_ref.wav', 'audio/skrzypce_sala_anchor.wav')
```

---

## Wyniki

Po zakończeniu testu kliknij "Eksportuj wyniki CSV". Plik CSV zawiera:
- dane uczestnika (imię, doświadczenie, sprzęt)
- oceny wszystkich próbek/parametrów
- datę i godzinę

Pliki CSV z wynikami 5 uczestników możesz zebrać i przeanalizować w Excelu lub Python (pandas).

---

## Kolejność testów

Zalecana kolejność dla każdego uczestnika:
1. `mushra_test.html` — test MUSHRA (globalny)
2. `test_parametryczny.html` — test parametryczny (szczegółowy)
