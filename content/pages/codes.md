Title: Codes
Date: 2019-07-07
Modified: 2019-07-07
Lang: en
Slug: codes


## [pyaneti](https://github.com/oscaribv/pyaneti) 

<center>
<img src="https://raw.githubusercontent.com/oscaribv/pyaneti/master/src/images/logo_pyaneti.png" alt="pyaneti-logo" width="300"/>
</center>

#### Paper 1

<a href="https://academic.oup.com/mnras/advance-article/doi/10.1093/mnras/sty2472/5094600"><img src="https://img.shields.io/badge/MNRAS-2019,482,1017-purple.svg" alt="MNRAS" /></a>
<a href="https://arxiv.org/abs/1809.04609"><img src="https://img.shields.io/badge/arXiv-1809.04609-green.svg" alt="arXiv:1809.04609" /></a>
<a href="http://ascl.net/1707.003"><img src="https://img.shields.io/badge/ascl-1707.003-green.svg" alt="ascl:1707.003" /></a>
<a href="https://github.com/oscaribv/pyaneti/wiki"><img src="https://img.shields.io/badge/wiki-building-yellow.svg" alt="pyaneti wiki" /></a>


#### Paper 2

<a href="https://academic.oup.com/mnras/advance-article-abstract/doi/10.1093/mnras/stab2889/6383008"><img src="https://img.shields.io/badge/MNRAS-2022, 509, 866-blueviolet.svg" alt="MNRAS" /></a>
<a href="https://arxiv.org/abs/2109.14086"><img src="https://img.shields.io/badge/arXiv-2109.140860-green.svg" alt="arXiv:2109.140860" /></a>

**Pyaneti** is a multi-planet radial velocity and transit fit software. 
The code uses Markov chain Monte Carlo (MCMC) methods with a Bayesian approach and a parallelized ensemble 
sampler algorithm in Fortran which makes the code fast. It creates posteriors, correlations, and ready-to-publish 
plots automatically, and handles circular and eccentric orbits. It is capable of multi-planet fitting and handles 
stellar limb darkening, systemic velocities for multiple instruments, and short and long cadence data, 
and offers additional capabilities.

Tne new vesion of pyaneti includes:

* Now the code runs in python 3.
* It runs transit fits for single transits.
* It runs GPs and multi-GPs approaches (no tutorials provided by now).
* It runs multi-band fits (even if each band has a different cadence).
* Changes in plots.

This new version is available online as a beta version, 
you can check it [here](https://github.com/oscaribv/pyaneti2-beta-).

This code works in simililar way to pyaneti, and you should be able to compile it and run it following this tutorial. But, this new version uses the lapack and blas libraries, be sure you have them, if no, the code may not compile.
You should be able to re-run all your scripts of the old pyaneti in this one (But not all the input files for this new pyaneti will run in the old one!).

## [Citlalicue](https://github.com/oscaribv/citlalicue)

*_Citlalicue_* is the name of the Aztec Goddess who created the stars together with her husband Citlalatonac.
This code allows you to mimic Citlalicue powers to create and manipulate stellar light curves.

The actual version of the code allows you to create synthetic stellar light curves (transits, stellar variability and white noise)
and detrend light curves using Gaussian Processes (GPs). 


#### Simulate light curves

Transits are implemented using [PyTransit](https://github.com/hpparvi/PyTransit), 
while the stellar variability is added from samples of a Quasi-Periodic Kernel with covariance given by

<a href="https://www.codecogs.com/eqnedit.php?latex=\gamma(t_i,t_j)&space;=&space;A&space;\exp&space;\left[&space;-&space;\frac{\sin^2[\pi(t_i&space;-&space;t_j)/P_{\rm&space;GP}]}{2&space;\lambda_{\rm&space;P}^2}&space;-&space;\frac{(t_i&space;-&space;t_j)^2}{2\lambda_{\rm&space;e}^2}&space;\right]" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\gamma(t_i,t_j)&space;=&space;A&space;\exp&space;\left[&space;-&space;\frac{\sin^2[\pi(t_i&space;-&space;t_j)/P_{\rm&space;GP}]}{2&space;\lambda_{\rm&space;P}^2}&space;-&space;\frac{(t_i&space;-&space;t_j)^2}{2\lambda_{\rm&space;e}^2}&space;\right]" title="\gamma(t_i,t_j) = A \exp \left[ - \frac{\sin^2[\pi(t_i - t_j)/P_{\rm GP}]}{2 \lambda_{\rm P}^2} - \frac{(t_i - t_j)^2}{2\lambda_{\rm e}^2} \right]" /></a>

Check the example of how to use Citlalicue to create light curves in the link
[example_light_curves.ipynb](https://github.com/oscaribv/citlalicue/blob/master/example_light_curves.ipynb).

This is an example of a light curve created with Citlalicue

<center>
<img src="https://raw.githubusercontent.com/oscaribv/oscaribv.github.io/master/images/citlalc_created.png" alt="citlalicue created" width="500"/>
</center>

#### Detrend light curves

Check the example of how to use Citlalicue to detrend light curves in the link
[example_detrending.ipynb](https://github.com/oscaribv/citlalicue/blob/master/example_detrending.ipynb).

This is an example of a detrended light curve with Citlalicue

<center>
<img src="https://raw.githubusercontent.com/oscaribv/oscaribv.github.io/master/images/citlalc.png" alt="citlalicue detrending" width="500"/>
</center>

## [Citlalatonac](https://github.com/oscaribv/pyaneti)

*_Citlalatonac_* is the name of the Aztec God who created the stars together with his wife [Citlalicue](https://github.com/oscaribv/citlalicue).
This code allows you to mimic Citlalatonac powers to create spectroscopic-like time-series of RVs and activity indicators for active stars.
You can create mock spectroscopic observations assuming that the area covered by active regions on the stellar surface can be described with
a function G(t). You can create RV-like time-series with stellar (that behave as G(t) + dG(t)/dt) and planetary signals (coherent Keplerians).
Simultaneously, you can create time-series of photometric-like activity idicators (such as the Calcium II H & K or FWHM) or Bisector Span-like 
activity indicators (that behave as G(t) + dG(t)/dt). This can be useful to see how different combinations of activity indicators with RVs can 
allow you to recover Keplerian signals from your RV-like time-series. This is useful, for example, to write telescope proposals!

If you want to learn how to use citlalatonac, go to this [link to create synthetic observations offers
K2-100](https://github.com/oscaribv/pyaneti/blob/master/pyaneti_extras/synthetic_k2100.ipynb), an active young star.



## [tango](https://github.com/oscaribv/tango)

Planets perform a gravitational TANGO around their host stars which is called orbit. 
If the orbit inclination is close to 90°, the presence of a planet orbiting its host star can be inferred
by detecting the periodic drops of stellar flux caused by the planet partly occulting the stellar disc. 
This phenomenon is called transit. If we observe the transits caused by planets in stellar light curves 
(flux vs time), we are able to decode the gravitational coreography and obtain planetary 
and orbital properties of the system.
This code helps you to visualise how the planet's motion was looking when they were transiting the stellar disc.|

Here you can find some examples of the kind of animations you can do with TANGO

<center>
[<img src="https://raw.githubusercontent.com/oscaribv/oscaribv.github.io/master/images/tango/k2141.gif" alt="K2-141" width="300"/>](https://arxiv.org/abs/1711.02097)
[<img src="https://raw.githubusercontent.com/oscaribv/oscaribv.github.io/master/images/tango/gj9827model.gif" alt="GJ9827" width="300"/>](https://arxiv.org/abs/1802.09557)
</center>

## [exotrending](https://github.com/oscaribv/exotrending)

<a href="http://ascl.net/1706.001"><img src="https://img.shields.io/badge/ascl-1706.001-blue.svg?colorB=262255" alt="ascl:1706.001" /></a>

The simple, straightforward Exotrending code detrends exoplanet transit light curves given a light curve (flux versus time) 
and good ephemeris (epoch of first transit and orbital period). The code has been tested with
 Kepler and K2 light curves and should work with any other light curve.
