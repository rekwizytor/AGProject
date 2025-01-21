# AGProject
Projekt **Ewolucyjne Generowanie Obrazów** przygotowany na zajęcia z algorytmów genetycznych.

Celem projektu było przygotowanie oprogramowania, które za pomocą generowania i ewolucji rysunków z losowo rozmieszczonymi kształtami próbuje jak najlepiej odwzorować obrazek docelowy podany jako input programu.

## Wymagania
- **Python 3.11** lub nowszy
- Wirtualne środowisko (zalecane)

### Wymagane biblioteki
- **numpy**
- **matplotlib**
- **pillow** 

## Konfiguracja i uruchomienie
Aby uruchomić program trzeba wgrać docelowy obrazek (w formacie **.jpg** lub **.png**) do folderu z projektem i utworzyć folder zawierający podkatalogi: **last_population**, **the_bests**, **the_worsts**. Następnie w pliku **main.py** ustawić dwa parametry: **label** - nazwa katalogu, w którym zostaną zapisane wyniki działania programu, **input_filename** - ścieżka do pliku z obrazkiem docelowym. W celu uruchomienia programu należy przejść do katalogu, w którym jest projekt (**_cd AGProject/_**), a następnie wykonać komendę: **_python3 main.py_**.

W wyniku działania programu w podanym folderze zostanie utworzony plik **data_out.txt** zawierajacy dane wyjściowe programu i plik **best.png** - z wygenerowanym rysunkiem najlepiej odwzorowującym obraz docelowy. W folderze **last_population** zostaną zapisane wszystkie rysunki z ostatniego pokolenia w algorytmie, w folderze **the_bests**, **the_worsts** odpowiednio najlepiej i najgorzej przystosowane osobniki w każdym pokoleniu.

Na podstawie danych w pliku **data_out.txt** można wykonać wykresy funkcji dopasowania  najlepiej przystosowanego osobnika oraz średniego przystosowania w każdym pokoleniu. W tym celu należy w pliku **plot.py** ustawić parametr **label** jako nazwę folderu z plikami wyjściowymi, a następnie uruchomić go komendą: **_python3 plot.py_**. W wyniku działania tego skryptu w podanym folderze powstaną wykresy zapisane w plikach **best_graf.png** i **mean_graf.png**.
