# SDP — Testy odsłuchowe auralizacji

Projekt realizowany w ramach przedmiotu SDP.  
Zespół: Anna Celińska, Jakub Kubiński, Patrycja Jaworek, Sandra Rojek, Paweł Kabała

---

## Cel projektu

Ocena zgodności nagrań auralizowanych z nagraniami referencyjnymi wykonanymi w rzeczywistych pomieszczeniach. Auralizacja polega na splocie nagrań bezechowych instrumentów z odpowiedziami impulsowymi pomieszczeń. Testy odsłuchowe pozwalają ocenić, jak wiernie ta metoda odwzorowuje rzeczywiste brzmienie.

---

## Zawartość repozytorium

```
├── mushra_test.html          — Test MUSHRA (ocena globalna, skala 0–100)
├── test_parametryczny.html   — Test parametryczny (4 atrybuty, skala 1–5)
├── README.md
└── audio/
    ├── ref/                  — nagrania referencyjne (rzeczywiste pomieszczenia)
    ├── auraliz/              — nagrania auralizowane (splot bezechowe × IR)
    └── anchor/               — kotwice (nagrania referencyjne po filtrze LP 2500 Hz)
```

---

## Materiał testowy

**Instrumenty:** akordeon, wiolonczela, saksofon  
**Pomieszczenia:** sala 123, korytarz ZEA, studio  
**Pozycja mikrofonu:** na wprost źródła  
**Liczba zadań:** 9 (3 instrumenty × 3 pomieszczenia)

---

## Metodyka testów

### Test MUSHRA (`mushra_test.html`)

Ocena globalnego podobieństwa nagrania auralizowanego do referencyjnego.  
W każdym zadaniu uczestnik ocenia 3 anonimowe próbki w skali 0–100:

| Próbka | Opis |
|--------|------|
| Auralizowana | nagranie uzyskane przez splot z odpowiedzią impulsową |
| Ukryta referencja | identyczna z jawną referencją — powinna uzyskać ~100 pkt |
| Kotwica | nagranie referencyjne po filtrze LP 2500 Hz — powinna uzyskać ~0–20 pkt |

Kolejność próbek jest losowa. Uczestnik nie wie, która jest która.

### Test parametryczny (`test_parametryczny.html`)

Ocena wybranych cech percepcyjnych w skali 1–5 (1 = bardzo mała zgodność, 5 = bardzo duża zgodność).

| Atrybut | Co oceniamy |
|---------|-------------|
| Barwa | Czy instrument brzmi tak samo — bas, wysokie tony, ogólny charakter |
| Przestrzenność | Czy czujesz się w tym samym miejscu — odległość i kierunek źródła |
| Naturalność | Czy brzmi jak prawdziwy instrument — brak artefaktów i zniekształceń |
| Pogłos | Czy pomieszczenie brzmi tak samo — wybrzmiewanie, echo, odbicia |

---

## Uruchomienie

Przeglądarki blokują ładowanie plików audio z dysku lokalnego — wymagany jest serwer lokalny.

**VS Code (zalecane):**
1. Zainstaluj rozszerzenie **Live Server** (Ritwick Dey)
2. Kliknij prawym przyciskiem na `mushra_test.html` → **Open with Live Server**

**Python:**
```bash
python -m http.server 8000
# http://localhost:8000/mushra_test.html
```

---

## Wyniki

Po zakończeniu każdego testu należy kliknąć **Eksportuj wyniki CSV**.  
Plik zawiera: dane uczestnika, sprzęt odsłuchowy, oceny wszystkich próbek/atrybutów, datę.

Zalecana kolejność dla każdego uczestnika:
1. `mushra_test.html`
2. `test_parametryczny.html`
