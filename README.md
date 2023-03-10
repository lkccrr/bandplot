[![bandplot](https://img.shields.io/pypi/v/bandplot?style=flat-square)](https://pypi.org/project/bandplot/)
[![bandplot](https://img.shields.io/pypi/pyversions/bandplot?style=flat-square)](https://pypi.org/project/bandplot/)
[![bandplot](https://img.shields.io/pypi/l/bandplot?style=flat-square)](https://pypi.org/project/bandplot/)
[![bandplot](https://img.shields.io/pypi/dm/bandplot?style=flat-square)](https://pypi.org/project/bandplot/)
[![bandplot](https://img.shields.io/pypi/wheel/bandplot?style=flat-square)](https://pypi.org/project/bandplot/)
[![bandplot](https://img.shields.io/github/last-commit/lkccrr/bandplot?style=flat-square)](https://github.com/lkccrr/bandplot)
[![bandplot](https://img.shields.io/github/release-date/lkccrr/bandplot?style=flat-square)](https://github.com/lkccrr/bandplot)

### bandplot

Bandplot is used for plotting the band structure, DOS or phonon band structure plot from ***vaspkit*** or ***phonopy*** results. The code will provide two scripts, <b style="color:blue;"><i>bandplot</b></i> for band structure or DOS plotting from ***vaspkit*** <b style="color:darkred;"><i>\*.dat</b></i> files, and <b style="color:blue;"><i>pbandplot</b></i> for phonon band structure or DOS plotting from ***phonopy*** <b style="color:darkred;"><i>\*.dat</b></i> files.
***
<b style="color:blue;"><i>bandplot</b></i>
* To execute <b style="color:blue;"><i>bandplot</b></i> <b style="color:red;"><i>\-h</b></i> for the parameters to use.
* Example:
```bash
bandplot -h
bandplot -i band.dat -o band.png -l g m k g -d PDOS* -F
bandplot -b -l g m k g -y -5 2
```
***
<b style="color:blue;"><i>pbandplot</b></i>
* To execute <b style="color:blue;"><i>pbandplot</b></i> <b style="color:red;"><i>\-h</b></i> for the parameters to use.
* Example:
```bash
pbandplot -h
pbandplot -i band.dat -o pband.png -l g m k g -d projected_dos.dat
pbandplot -b 23 100 -l g m k g -y -2 110
```

