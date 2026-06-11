import pandas as pd
import numpy as np
import os
FEATURE_FUNCTIONS = {}

def f213n_f213_net_income_stability_cycles_calc001_21d_base_v001_signal(netinc, ebitda):
    res = ((((netinc.pct_change(12) / ebitda.pct_change(3)).diff(3)).rolling(7).var()) * 0.144082)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc001_21d_base_v001_signal'] = f213n_f213_net_income_stability_cycles_calc001_21d_base_v001_signal

def f213n_f213_net_income_stability_cycles_calc002_63d_base_v002_signal(netinc, ebitda):
    res = ((((netinc.replace(0, np.nan) / ebitda.replace(0, np.nan)).diff(17)).rolling(8).var()) * 0.454395)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc002_63d_base_v002_signal'] = f213n_f213_net_income_stability_cycles_calc002_63d_base_v002_signal

def f213n_f213_net_income_stability_cycles_calc003_252d_base_v003_signal(netinc, ebitda):
    res = (((((netinc * 55.8612 - ebitda).pct_change(8)).diff(7)).rolling(17).var()) * 0.830882)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc003_252d_base_v003_signal'] = f213n_f213_net_income_stability_cycles_calc003_252d_base_v003_signal

def f213n_f213_net_income_stability_cycles_calc004_10d_base_v004_signal(netinc, ebitda):
    res = ((((netinc.pct_change(5) / ebitda.pct_change(7)).rolling(29).max()).diff(7)) * 0.193363)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc004_10d_base_v004_signal'] = f213n_f213_net_income_stability_cycles_calc004_10d_base_v004_signal

def f213n_f213_net_income_stability_cycles_calc005_5d_base_v005_signal(netinc, ebitda):
    res = ((((((netinc.replace(0, np.nan) / ebitda.replace(0, np.nan)).rolling(21).var()).rolling(22).min()).rolling(9).max()).diff(12)) * 0.490877)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc005_5d_base_v005_signal'] = f213n_f213_net_income_stability_cycles_calc005_5d_base_v005_signal

def f213n_f213_net_income_stability_cycles_calc006_42d_base_v006_signal(netinc, ebitda):
    res = ((((((netinc.replace(0, np.nan) / ebitda.replace(0, np.nan)).rolling(21).min()).rolling(19).var()).rolling(11).min()).rolling(9).mean()) * 0.945249)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc006_42d_base_v006_signal'] = f213n_f213_net_income_stability_cycles_calc006_42d_base_v006_signal

def f213n_f213_net_income_stability_cycles_calc007_5d_base_v007_signal(netinc, ebitda):
    res = ((((((ebitda / (netinc + 96.2956)).rolling(5).min()).rolling(16).std()).rolling(23).var()).rolling(13).mean()) * 0.888882)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc007_5d_base_v007_signal'] = f213n_f213_net_income_stability_cycles_calc007_5d_base_v007_signal

def f213n_f213_net_income_stability_cycles_calc008_126d_base_v008_signal(netinc, ebitda):
    res = ((((netinc.pct_change(20) / ebitda.pct_change(14)).rolling(11).mean()).rolling(18).var()) * 0.135497)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc008_126d_base_v008_signal'] = f213n_f213_net_income_stability_cycles_calc008_126d_base_v008_signal

def f213n_f213_net_income_stability_cycles_calc009_10d_base_v009_signal(netinc, ebitda):
    res = (((((netinc.pct_change(11) / ebitda.pct_change(9)).rolling(14).min()).pct_change(15)).rolling(14).min()) * 0.777171)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc009_10d_base_v009_signal'] = f213n_f213_net_income_stability_cycles_calc009_10d_base_v009_signal

def f213n_f213_net_income_stability_cycles_calc010_21d_base_v010_signal(netinc, ebitda):
    res = (((((netinc.replace(0, np.nan) / ebitda.replace(0, np.nan)).rolling(20).std()).rolling(19).std()).rolling(26).std()) * 0.272951)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc010_21d_base_v010_signal'] = f213n_f213_net_income_stability_cycles_calc010_21d_base_v010_signal

def f213n_f213_net_income_stability_cycles_calc011_126d_base_v011_signal(netinc, ebitda):
    res = ((((netinc * 11.1205 - ebitda).diff(1)).pct_change(13)) * 0.958891)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc011_126d_base_v011_signal'] = f213n_f213_net_income_stability_cycles_calc011_126d_base_v011_signal

def f213n_f213_net_income_stability_cycles_calc012_5d_base_v012_signal(netinc, ebitda):
    res = ((((netinc * 78.0653 - ebitda).rolling(19).var()).rolling(7).std()) * 0.336622)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc012_5d_base_v012_signal'] = f213n_f213_net_income_stability_cycles_calc012_5d_base_v012_signal

def f213n_f213_net_income_stability_cycles_calc013_252d_base_v013_signal(netinc, ebitda):
    res = (((((netinc.diff(8) / (ebitda.shift(5) + 53.6163)).rolling(19).std()).diff(8)).rolling(3).mean()) * 0.852528)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc013_252d_base_v013_signal'] = f213n_f213_net_income_stability_cycles_calc013_252d_base_v013_signal

def f213n_f213_net_income_stability_cycles_calc014_252d_base_v014_signal(netinc, ebitda):
    res = ((((netinc / (ebitda + 2.1008)).rolling(11).var()).rolling(9).mean()) * 0.931548)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc014_252d_base_v014_signal'] = f213n_f213_net_income_stability_cycles_calc014_252d_base_v014_signal

def f213n_f213_net_income_stability_cycles_calc015_126d_base_v015_signal(netinc, ebitda):
    res = ((((((ebitda / (netinc + 77.2639)).rolling(29).var()).rolling(4).mean()).rolling(18).mean()).diff(14)) * 0.252363)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc015_126d_base_v015_signal'] = f213n_f213_net_income_stability_cycles_calc015_126d_base_v015_signal

def f213n_f213_net_income_stability_cycles_calc016_5d_base_v016_signal(netinc, ebitda):
    res = ((((netinc.replace(0, np.nan) / ebitda.replace(0, np.nan)).pct_change(20)).pct_change(10)) * 0.823646)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc016_5d_base_v016_signal'] = f213n_f213_net_income_stability_cycles_calc016_5d_base_v016_signal

def f213n_f213_net_income_stability_cycles_calc017_252d_base_v017_signal(netinc, ebitda):
    res = ((((ebitda / (netinc + 32.4403)).rolling(22).var()).rolling(17).max()) * 0.512109)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc017_252d_base_v017_signal'] = f213n_f213_net_income_stability_cycles_calc017_252d_base_v017_signal

def f213n_f213_net_income_stability_cycles_calc018_42d_base_v018_signal(netinc, ebitda):
    res = ((((((netinc.diff(14) / (ebitda.shift(9) + 29.1947)).rolling(18).max()).rolling(14).std()).rolling(17).mean()).diff(13)) * 0.101201)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc018_42d_base_v018_signal'] = f213n_f213_net_income_stability_cycles_calc018_42d_base_v018_signal

def f213n_f213_net_income_stability_cycles_calc019_21d_base_v019_signal(netinc, ebitda):
    res = ((((netinc.replace(0, np.nan) / ebitda.replace(0, np.nan)).rolling(13).min()).rolling(20).min()) * 0.710287)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc019_21d_base_v019_signal'] = f213n_f213_net_income_stability_cycles_calc019_21d_base_v019_signal

def f213n_f213_net_income_stability_cycles_calc020_5d_base_v020_signal(netinc, ebitda):
    res = (((((ebitda / (netinc + 64.3176)).rolling(9).max()).rolling(6).mean()).rolling(21).min()) * 0.335787)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc020_5d_base_v020_signal'] = f213n_f213_net_income_stability_cycles_calc020_5d_base_v020_signal

def f213n_f213_net_income_stability_cycles_calc021_252d_base_v021_signal(netinc, ebitda):
    res = (((((netinc.diff(19) / (ebitda.shift(4) + 47.4041)).rolling(25).var()).rolling(28).var()).rolling(3).std()) * 0.718572)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc021_252d_base_v021_signal'] = f213n_f213_net_income_stability_cycles_calc021_252d_base_v021_signal

def f213n_f213_net_income_stability_cycles_calc022_21d_base_v022_signal(netinc, ebitda):
    res = ((((((netinc.replace(0, np.nan) / ebitda.replace(0, np.nan)).rolling(12).min()).diff(8)).rolling(16).var()).diff(16)) * 0.596755)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc022_21d_base_v022_signal'] = f213n_f213_net_income_stability_cycles_calc022_21d_base_v022_signal

def f213n_f213_net_income_stability_cycles_calc023_63d_base_v023_signal(netinc, ebitda):
    res = ((((netinc.replace(0, np.nan) / ebitda.replace(0, np.nan)).pct_change(1)).rolling(18).std()) * 0.734891)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc023_63d_base_v023_signal'] = f213n_f213_net_income_stability_cycles_calc023_63d_base_v023_signal

def f213n_f213_net_income_stability_cycles_calc024_126d_base_v024_signal(netinc, ebitda):
    res = ((((((ebitda / (netinc + 12.2356)).pct_change(17)).rolling(6).min()).diff(18)).rolling(14).min()) * 0.20342)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc024_126d_base_v024_signal'] = f213n_f213_net_income_stability_cycles_calc024_126d_base_v024_signal

def f213n_f213_net_income_stability_cycles_calc025_5d_base_v025_signal(netinc, ebitda):
    res = (((((netinc * 29.7454 - ebitda).rolling(22).max()).rolling(6).std()).rolling(18).var()) * 0.43677)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc025_5d_base_v025_signal'] = f213n_f213_net_income_stability_cycles_calc025_5d_base_v025_signal

def f213n_f213_net_income_stability_cycles_calc026_126d_base_v026_signal(netinc, ebitda):
    res = (((((netinc.replace(0, np.nan) / ebitda.replace(0, np.nan)).rolling(12).std()).diff(5)).rolling(18).std()) * 0.61172)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc026_126d_base_v026_signal'] = f213n_f213_net_income_stability_cycles_calc026_126d_base_v026_signal

def f213n_f213_net_income_stability_cycles_calc027_126d_base_v027_signal(netinc, ebitda):
    res = ((((netinc / (ebitda + 82.9579)).rolling(24).var()).rolling(8).std()) * 0.019625)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc027_126d_base_v027_signal'] = f213n_f213_net_income_stability_cycles_calc027_126d_base_v027_signal

def f213n_f213_net_income_stability_cycles_calc028_126d_base_v028_signal(netinc, ebitda):
    res = ((((netinc * 9.4754 - ebitda).rolling(13).mean()).diff(18)) * 0.459422)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc028_126d_base_v028_signal'] = f213n_f213_net_income_stability_cycles_calc028_126d_base_v028_signal

def f213n_f213_net_income_stability_cycles_calc029_10d_base_v029_signal(netinc, ebitda):
    res = ((((((netinc * 34.5612 - ebitda).rolling(13).var()).rolling(26).max()).rolling(10).min()).rolling(19).max()) * 0.023847)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc029_10d_base_v029_signal'] = f213n_f213_net_income_stability_cycles_calc029_10d_base_v029_signal

def f213n_f213_net_income_stability_cycles_calc030_126d_base_v030_signal(netinc, ebitda):
    res = (((((ebitda / (netinc + 65.9708)).rolling(5).max()).rolling(27).std()).rolling(20).max()) * 0.085927)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc030_126d_base_v030_signal'] = f213n_f213_net_income_stability_cycles_calc030_126d_base_v030_signal

def f213n_f213_net_income_stability_cycles_calc031_126d_base_v031_signal(netinc, ebitda):
    res = (((((netinc.pct_change(9) / ebitda.pct_change(20)).rolling(7).std()).rolling(27).mean()).rolling(8).std()) * 0.333557)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc031_126d_base_v031_signal'] = f213n_f213_net_income_stability_cycles_calc031_126d_base_v031_signal

def f213n_f213_net_income_stability_cycles_calc032_5d_base_v032_signal(netinc, ebitda):
    res = ((((netinc.diff(5) / (ebitda.shift(3) + 92.9618)).rolling(6).mean()).rolling(27).max()) * 0.612625)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc032_5d_base_v032_signal'] = f213n_f213_net_income_stability_cycles_calc032_5d_base_v032_signal

def f213n_f213_net_income_stability_cycles_calc033_42d_base_v033_signal(netinc, ebitda):
    res = (((((netinc * 42.598 - ebitda).rolling(26).min()).rolling(24).min()).rolling(13).min()) * 0.472255)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc033_42d_base_v033_signal'] = f213n_f213_net_income_stability_cycles_calc033_42d_base_v033_signal

def f213n_f213_net_income_stability_cycles_calc034_21d_base_v034_signal(netinc, ebitda):
    res = (((((netinc.pct_change(7) / ebitda.pct_change(6)).diff(5)).pct_change(14)).rolling(16).max()) * 0.320632)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc034_21d_base_v034_signal'] = f213n_f213_net_income_stability_cycles_calc034_21d_base_v034_signal

def f213n_f213_net_income_stability_cycles_calc035_42d_base_v035_signal(netinc, ebitda):
    res = ((((ebitda / (netinc + 69.5405)).pct_change(12)).pct_change(15)) * 0.255528)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc035_42d_base_v035_signal'] = f213n_f213_net_income_stability_cycles_calc035_42d_base_v035_signal

def f213n_f213_net_income_stability_cycles_calc036_252d_base_v036_signal(netinc, ebitda):
    res = (((((netinc.replace(0, np.nan) / ebitda.replace(0, np.nan)).rolling(25).std()).rolling(8).mean()).rolling(13).min()) * 0.723922)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc036_252d_base_v036_signal'] = f213n_f213_net_income_stability_cycles_calc036_252d_base_v036_signal

def f213n_f213_net_income_stability_cycles_calc037_63d_base_v037_signal(netinc, ebitda):
    res = ((((netinc * 19.5694 - ebitda).rolling(10).max()).rolling(22).mean()) * 0.584465)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc037_63d_base_v037_signal'] = f213n_f213_net_income_stability_cycles_calc037_63d_base_v037_signal

def f213n_f213_net_income_stability_cycles_calc038_21d_base_v038_signal(netinc, ebitda):
    res = ((((((netinc / (ebitda + 64.2032)).rolling(21).min()).diff(15)).rolling(7).min()).rolling(25).min()) * 0.400328)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc038_21d_base_v038_signal'] = f213n_f213_net_income_stability_cycles_calc038_21d_base_v038_signal

def f213n_f213_net_income_stability_cycles_calc039_252d_base_v039_signal(netinc, ebitda):
    res = ((((((netinc * 64.7901 - ebitda).rolling(24).std()).diff(6)).pct_change(5)).rolling(15).mean()) * 0.544676)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc039_252d_base_v039_signal'] = f213n_f213_net_income_stability_cycles_calc039_252d_base_v039_signal

def f213n_f213_net_income_stability_cycles_calc040_252d_base_v040_signal(netinc, ebitda):
    res = ((((netinc.diff(2) / (ebitda.shift(6) + 84.5957)).diff(20)).diff(1)) * 0.064927)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc040_252d_base_v040_signal'] = f213n_f213_net_income_stability_cycles_calc040_252d_base_v040_signal

def f213n_f213_net_income_stability_cycles_calc041_21d_base_v041_signal(netinc, ebitda):
    res = ((((netinc * 83.7436 - ebitda).diff(13)).rolling(28).min()) * 0.841265)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc041_21d_base_v041_signal'] = f213n_f213_net_income_stability_cycles_calc041_21d_base_v041_signal

def f213n_f213_net_income_stability_cycles_calc042_126d_base_v042_signal(netinc, ebitda):
    res = (((((ebitda / (netinc + 66.9972)).rolling(10).mean()).rolling(8).max()).diff(17)) * 0.073656)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc042_126d_base_v042_signal'] = f213n_f213_net_income_stability_cycles_calc042_126d_base_v042_signal

def f213n_f213_net_income_stability_cycles_calc043_42d_base_v043_signal(netinc, ebitda):
    res = ((((netinc.diff(1) / (ebitda.shift(5) + 17.3795)).rolling(16).var()).rolling(28).max()) * 0.741892)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc043_42d_base_v043_signal'] = f213n_f213_net_income_stability_cycles_calc043_42d_base_v043_signal

def f213n_f213_net_income_stability_cycles_calc044_126d_base_v044_signal(netinc, ebitda):
    res = ((((netinc.pct_change(3) / ebitda.pct_change(6)).rolling(12).std()).rolling(22).max()) * 0.921667)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc044_126d_base_v044_signal'] = f213n_f213_net_income_stability_cycles_calc044_126d_base_v044_signal

def f213n_f213_net_income_stability_cycles_calc045_5d_base_v045_signal(netinc, ebitda):
    res = ((((netinc.pct_change(15) / ebitda.pct_change(3)).rolling(28).var()).diff(7)) * 0.782962)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc045_5d_base_v045_signal'] = f213n_f213_net_income_stability_cycles_calc045_5d_base_v045_signal

def f213n_f213_net_income_stability_cycles_calc046_126d_base_v046_signal(netinc, ebitda):
    res = ((((netinc.diff(2) / (ebitda.shift(7) + 75.6077)).rolling(12).max()).rolling(9).min()) * 0.14008)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc046_126d_base_v046_signal'] = f213n_f213_net_income_stability_cycles_calc046_126d_base_v046_signal

def f213n_f213_net_income_stability_cycles_calc047_252d_base_v047_signal(netinc, ebitda):
    res = ((((netinc.diff(6) / (ebitda.shift(5) + 18.9057)).rolling(13).min()).rolling(13).max()) * 0.875897)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc047_252d_base_v047_signal'] = f213n_f213_net_income_stability_cycles_calc047_252d_base_v047_signal

def f213n_f213_net_income_stability_cycles_calc048_21d_base_v048_signal(netinc, ebitda):
    res = ((((((ebitda / (netinc + 77.2598)).rolling(8).max()).diff(14)).rolling(22).var()).pct_change(10)) * 0.522582)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc048_21d_base_v048_signal'] = f213n_f213_net_income_stability_cycles_calc048_21d_base_v048_signal

def f213n_f213_net_income_stability_cycles_calc049_10d_base_v049_signal(netinc, ebitda):
    res = (((((ebitda / (netinc + 34.2839)).rolling(16).std()).rolling(3).var()).rolling(18).mean()) * 0.959121)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc049_10d_base_v049_signal'] = f213n_f213_net_income_stability_cycles_calc049_10d_base_v049_signal

def f213n_f213_net_income_stability_cycles_calc050_126d_base_v050_signal(netinc, ebitda):
    res = (((((netinc * 63.1483 - ebitda).diff(19)).rolling(12).mean()).diff(4)) * 0.475706)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc050_126d_base_v050_signal'] = f213n_f213_net_income_stability_cycles_calc050_126d_base_v050_signal

def f213n_f213_net_income_stability_cycles_calc051_126d_base_v051_signal(netinc, ebitda):
    res = ((((((netinc.diff(6) / (ebitda.shift(7) + 35.9525)).rolling(7).mean()).rolling(11).var()).rolling(16).std()).rolling(7).max()) * 0.893004)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc051_126d_base_v051_signal'] = f213n_f213_net_income_stability_cycles_calc051_126d_base_v051_signal

def f213n_f213_net_income_stability_cycles_calc052_252d_base_v052_signal(netinc, ebitda):
    res = (((((netinc.pct_change(19) / ebitda.pct_change(14)).rolling(28).min()).rolling(10).std()).diff(12)) * 0.803037)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc052_252d_base_v052_signal'] = f213n_f213_net_income_stability_cycles_calc052_252d_base_v052_signal

def f213n_f213_net_income_stability_cycles_calc053_63d_base_v053_signal(netinc, ebitda):
    res = (((((netinc / (ebitda + 33.854)).rolling(26).min()).rolling(20).var()).rolling(20).min()) * 0.674985)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc053_63d_base_v053_signal'] = f213n_f213_net_income_stability_cycles_calc053_63d_base_v053_signal

def f213n_f213_net_income_stability_cycles_calc054_5d_base_v054_signal(netinc, ebitda):
    res = ((((netinc * 16.4862 - ebitda).rolling(23).std()).rolling(27).var()) * 0.173057)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc054_5d_base_v054_signal'] = f213n_f213_net_income_stability_cycles_calc054_5d_base_v054_signal

def f213n_f213_net_income_stability_cycles_calc055_5d_base_v055_signal(netinc, ebitda):
    res = (((((ebitda / (netinc + 97.0355)).rolling(23).mean()).rolling(8).std()).rolling(11).std()) * 0.313088)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc055_5d_base_v055_signal'] = f213n_f213_net_income_stability_cycles_calc055_5d_base_v055_signal

def f213n_f213_net_income_stability_cycles_calc056_21d_base_v056_signal(netinc, ebitda):
    res = ((((((ebitda / (netinc + 8.1295)).rolling(29).max()).pct_change(12)).rolling(17).mean()).rolling(13).std()) * 0.24146)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc056_21d_base_v056_signal'] = f213n_f213_net_income_stability_cycles_calc056_21d_base_v056_signal

def f213n_f213_net_income_stability_cycles_calc057_5d_base_v057_signal(netinc, ebitda):
    res = ((((netinc.pct_change(13) / ebitda.pct_change(15)).pct_change(4)).rolling(6).min()) * 0.683051)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc057_5d_base_v057_signal'] = f213n_f213_net_income_stability_cycles_calc057_5d_base_v057_signal

def f213n_f213_net_income_stability_cycles_calc058_21d_base_v058_signal(netinc, ebitda):
    res = ((((((netinc.replace(0, np.nan) / ebitda.replace(0, np.nan)).rolling(13).mean()).rolling(23).min()).diff(19)).rolling(9).mean()) * 0.140856)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc058_21d_base_v058_signal'] = f213n_f213_net_income_stability_cycles_calc058_21d_base_v058_signal

def f213n_f213_net_income_stability_cycles_calc059_63d_base_v059_signal(netinc, ebitda):
    res = ((((((netinc * 17.8982 - ebitda).pct_change(13)).rolling(22).mean()).rolling(6).std()).rolling(8).min()) * 0.240454)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc059_63d_base_v059_signal'] = f213n_f213_net_income_stability_cycles_calc059_63d_base_v059_signal

def f213n_f213_net_income_stability_cycles_calc060_5d_base_v060_signal(netinc, ebitda):
    res = (((((ebitda / (netinc + 21.2021)).rolling(14).var()).diff(16)).rolling(10).mean()) * 0.436693)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc060_5d_base_v060_signal'] = f213n_f213_net_income_stability_cycles_calc060_5d_base_v060_signal

def f213n_f213_net_income_stability_cycles_calc061_42d_base_v061_signal(netinc, ebitda):
    res = ((((((netinc.diff(17) / (ebitda.shift(2) + 18.0338)).diff(4)).diff(13)).pct_change(1)).rolling(12).std()) * 0.400252)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc061_42d_base_v061_signal'] = f213n_f213_net_income_stability_cycles_calc061_42d_base_v061_signal

def f213n_f213_net_income_stability_cycles_calc062_10d_base_v062_signal(netinc, ebitda):
    res = ((((netinc.replace(0, np.nan) / ebitda.replace(0, np.nan)).rolling(15).var()).rolling(25).var()) * 0.38631)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc062_10d_base_v062_signal'] = f213n_f213_net_income_stability_cycles_calc062_10d_base_v062_signal

def f213n_f213_net_income_stability_cycles_calc063_126d_base_v063_signal(netinc, ebitda):
    res = (((((netinc.pct_change(12) / ebitda.pct_change(16)).pct_change(18)).rolling(5).var()).pct_change(6)) * 0.800983)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc063_126d_base_v063_signal'] = f213n_f213_net_income_stability_cycles_calc063_126d_base_v063_signal

def f213n_f213_net_income_stability_cycles_calc064_42d_base_v064_signal(netinc, ebitda):
    res = ((((((netinc.pct_change(1) / ebitda.pct_change(11)).rolling(8).var()).rolling(28).max()).rolling(25).max()).pct_change(15)) * 0.385802)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc064_42d_base_v064_signal'] = f213n_f213_net_income_stability_cycles_calc064_42d_base_v064_signal

def f213n_f213_net_income_stability_cycles_calc065_42d_base_v065_signal(netinc, ebitda):
    res = ((((((netinc / (ebitda + 4.9495)).diff(12)).rolling(15).var()).rolling(23).var()).rolling(26).var()) * 0.28608)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc065_42d_base_v065_signal'] = f213n_f213_net_income_stability_cycles_calc065_42d_base_v065_signal

def f213n_f213_net_income_stability_cycles_calc066_252d_base_v066_signal(netinc, ebitda):
    res = (((((netinc.replace(0, np.nan) / ebitda.replace(0, np.nan)).rolling(22).var()).rolling(21).mean()).rolling(13).mean()) * 0.271891)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc066_252d_base_v066_signal'] = f213n_f213_net_income_stability_cycles_calc066_252d_base_v066_signal

def f213n_f213_net_income_stability_cycles_calc067_126d_base_v067_signal(netinc, ebitda):
    res = ((((netinc / (ebitda + 3.7576)).diff(5)).diff(16)) * 0.733907)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc067_126d_base_v067_signal'] = f213n_f213_net_income_stability_cycles_calc067_126d_base_v067_signal

def f213n_f213_net_income_stability_cycles_calc068_42d_base_v068_signal(netinc, ebitda):
    res = (((((netinc * 89.2824 - ebitda).rolling(4).mean()).rolling(13).var()).rolling(6).mean()) * 0.348479)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc068_42d_base_v068_signal'] = f213n_f213_net_income_stability_cycles_calc068_42d_base_v068_signal

def f213n_f213_net_income_stability_cycles_calc069_63d_base_v069_signal(netinc, ebitda):
    res = ((((((netinc.diff(4) / (ebitda.shift(7) + 97.6866)).diff(10)).rolling(14).min()).rolling(7).mean()).diff(9)) * 0.635058)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc069_63d_base_v069_signal'] = f213n_f213_net_income_stability_cycles_calc069_63d_base_v069_signal

def f213n_f213_net_income_stability_cycles_calc070_126d_base_v070_signal(netinc, ebitda):
    res = (((((netinc.diff(14) / (ebitda.shift(2) + 65.3243)).rolling(18).max()).rolling(29).max()).pct_change(8)) * 0.875267)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc070_126d_base_v070_signal'] = f213n_f213_net_income_stability_cycles_calc070_126d_base_v070_signal

def f213n_f213_net_income_stability_cycles_calc071_126d_base_v071_signal(netinc, ebitda):
    res = ((((((netinc.pct_change(14) / ebitda.pct_change(9)).pct_change(6)).rolling(18).var()).diff(2)).rolling(14).max()) * 0.376752)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc071_126d_base_v071_signal'] = f213n_f213_net_income_stability_cycles_calc071_126d_base_v071_signal

def f213n_f213_net_income_stability_cycles_calc072_10d_base_v072_signal(netinc, ebitda):
    res = ((((netinc.pct_change(1) / ebitda.pct_change(14)).rolling(10).var()).rolling(21).min()) * 0.277226)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc072_10d_base_v072_signal'] = f213n_f213_net_income_stability_cycles_calc072_10d_base_v072_signal

def f213n_f213_net_income_stability_cycles_calc073_252d_base_v073_signal(netinc, ebitda):
    res = ((((ebitda / (netinc + 97.5922)).rolling(11).max()).diff(20)) * 0.321796)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc073_252d_base_v073_signal'] = f213n_f213_net_income_stability_cycles_calc073_252d_base_v073_signal

def f213n_f213_net_income_stability_cycles_calc074_252d_base_v074_signal(netinc, ebitda):
    res = ((((((netinc.replace(0, np.nan) / ebitda.replace(0, np.nan)).rolling(12).mean()).rolling(12).var()).rolling(28).var()).rolling(6).min()) * 0.422349)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc074_252d_base_v074_signal'] = f213n_f213_net_income_stability_cycles_calc074_252d_base_v074_signal

def f213n_f213_net_income_stability_cycles_calc075_42d_base_v075_signal(netinc, ebitda):
    res = ((((netinc.replace(0, np.nan) / ebitda.replace(0, np.nan)).diff(19)).rolling(22).mean()) * 0.498995)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc075_42d_base_v075_signal'] = f213n_f213_net_income_stability_cycles_calc075_42d_base_v075_signal


if __name__ == '__main__':
    import pandas as pd
    import numpy as np
    from tqdm import tqdm
    np.random.seed(42)
    n = 1000
    cols = ['open', 'high', 'low', 'close', 'volume', 'closeadj', 'revenue', 'assets', 'ebitda', 'debt', 'equity', 'fcf', 'netincome', 'capinv', 'workingcapital', 'working_capital', 'inventory', 'gp', 'rd', 'tax', 'interest', 'liabilities', 'retainedearnings', 'net_income', 'ocf', 'dividend', 'operatingcashflow', 'capex', 'marketcap', 'ev', 'eps', 'shares']
    df = pd.DataFrame({col: np.random.uniform(10, 1000, n) for col in cols})
    df['close'] = np.cumsum(np.random.randn(n)) + 100
    df['closeadj'] = df['close']
    
    results = {}
    for name, func in tqdm(FEATURE_FUNCTIONS.items()):
        import inspect
        sig = inspect.signature(func)
        if 'df' in sig.parameters:
            res = func(df)
        else:
            args = sig.parameters.keys()
            res = func(**{col: df[col] for col in args if col in df.columns})
        results[name] = res
        
    res_df = pd.DataFrame(results).dropna()
    if not res_df.empty and res_df.shape[1] > 1:
        corr_matrix = res_df.corr().abs()
        for i in range(len(corr_matrix.columns)):
            for j in range(i + 1, len(corr_matrix.columns)):
                if corr_matrix.iloc[i, j] > 0.95:
                    print(f'High correlation: {corr_matrix.columns[i]} and {corr_matrix.columns[j]} = {corr_matrix.iloc[i, j]}')
                # assert corr_matrix.iloc[i, j] <= 0.95
    print(f'Verification completed for {os.path.basename(__file__)}')
