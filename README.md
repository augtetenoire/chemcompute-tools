# chemcompute-tools
This repository contains the tools I developped to analyze the calculations I performed with the different computational chemistry software I used.


## Use package in scripts
examples of how to load specific modules from packages comtained in "chemcompute"


```
{
import chemcompute.common as c
c.dcolors

import chemcompute.dftbplus as dftb
dftb.dftb_load_modes_out('modes_dftb_polarizability_calculation_138848.out')
}
```

