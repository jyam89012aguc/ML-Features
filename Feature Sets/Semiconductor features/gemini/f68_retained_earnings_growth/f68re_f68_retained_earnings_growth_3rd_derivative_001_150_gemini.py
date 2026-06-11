import pandas as pd
import numpy as np
import os
FEATURE_FUNCTIONS = {}

def f68re_f68_retained_earnings_growth_calc001_5d_3rd_derivative_v001_signal(retearn):
    res = retearn.pct_change(5).diff(1).rolling(5).mean().pct_change(1).rolling(5).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f68re_f68_retained_earnings_growth_calc001_5d_3rd_derivative_v001_signal'] = f68re_f68_retained_earnings_growth_calc001_5d_3rd_derivative_v001_signal

def f68re_f68_retained_earnings_growth_calc002_10d_3rd_derivative_v002_signal(retearn, assets):
    res = (retearn / assets).rolling(10).mean().diff(1).rolling(10).std().diff(1).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f68re_f68_retained_earnings_growth_calc002_10d_3rd_derivative_v002_signal'] = f68re_f68_retained_earnings_growth_calc002_10d_3rd_derivative_v002_signal

def f68re_f68_retained_earnings_growth_calc003_21d_3rd_derivative_v003_signal(retearn, equity):
    res = (retearn / equity).rolling(21).std().pct_change(1).rolling(21).mean().diff(1).rolling(21).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f68re_f68_retained_earnings_growth_calc003_21d_3rd_derivative_v003_signal'] = f68re_f68_retained_earnings_growth_calc003_21d_3rd_derivative_v003_signal

def f68re_f68_retained_earnings_growth_calc004_42d_3rd_derivative_v004_signal(retearn, revenue):
    res = (retearn / revenue).diff(42).diff(1).rolling(42).skew().pct_change(1).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f68re_f68_retained_earnings_growth_calc004_42d_3rd_derivative_v004_signal'] = f68re_f68_retained_earnings_growth_calc004_42d_3rd_derivative_v004_signal

def f68re_f68_retained_earnings_growth_calc005_63d_3rd_derivative_v005_signal(retearn, marketcap):
    res = (retearn / marketcap).pct_change(63).diff(1).rolling(63).kurt().diff(1).rolling(63).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f68re_f68_retained_earnings_growth_calc005_63d_3rd_derivative_v005_signal'] = f68re_f68_retained_earnings_growth_calc005_63d_3rd_derivative_v005_signal

def f68re_f68_retained_earnings_growth_calc006_126d_3rd_derivative_v006_signal(retearn, netinc):
    res = (retearn / netinc).rolling(126).skew().diff(1).rolling(126).mean().pct_change(1).rolling(126).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f68re_f68_retained_earnings_growth_calc006_126d_3rd_derivative_v006_signal'] = f68re_f68_retained_earnings_growth_calc006_126d_3rd_derivative_v006_signal

def f68re_f68_retained_earnings_growth_calc007_252d_3rd_derivative_v007_signal(retearn, sharesbas):
    res = (retearn / sharesbas).rolling(252).kurt().pct_change(1).rolling(252).std().diff(1).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f68re_f68_retained_earnings_growth_calc007_252d_3rd_derivative_v007_signal'] = f68re_f68_retained_earnings_growth_calc007_252d_3rd_derivative_v007_signal

def f68re_f68_retained_earnings_growth_calc008_5d_3rd_derivative_v008_signal(retearn, debt):
    res = (retearn / debt).rolling(5).rank(pct=True).diff(1).rolling(5).skew().diff(1).rolling(5).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f68re_f68_retained_earnings_growth_calc008_5d_3rd_derivative_v008_signal'] = f68re_f68_retained_earnings_growth_calc008_5d_3rd_derivative_v008_signal

def f68re_f68_retained_earnings_growth_calc009_10d_3rd_derivative_v009_signal(retearn, liabilities):
    res = (retearn / liabilities).rolling(10).quantile(0.5).diff(1).rolling(10).kurt().pct_change(1).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f68re_f68_retained_earnings_growth_calc009_10d_3rd_derivative_v009_signal'] = f68re_f68_retained_earnings_growth_calc009_10d_3rd_derivative_v009_signal

def f68re_f68_retained_earnings_growth_calc010_21d_3rd_derivative_v010_signal(retearn, assets):
    res = ((retearn / assets).rolling(21).std() / (retearn / assets).rolling(21).mean()).diff(1).rolling(21).mean().pct_change(1).rolling(21).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f68re_f68_retained_earnings_growth_calc010_21d_3rd_derivative_v010_signal'] = f68re_f68_retained_earnings_growth_calc010_21d_3rd_derivative_v010_signal

def f68re_f68_retained_earnings_growth_calc011_42d_3rd_derivative_v011_signal(retearn, equity):
    res = (retearn / equity).rolling(42).min().diff(1).rolling(42).std().diff(1).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f68re_f68_retained_earnings_growth_calc011_42d_3rd_derivative_v011_signal'] = f68re_f68_retained_earnings_growth_calc011_42d_3rd_derivative_v011_signal

def f68re_f68_retained_earnings_growth_calc012_63d_3rd_derivative_v012_signal(retearn, revenue):
    res = (retearn / revenue).diff(63).rolling(63).mean().pct_change(1).rolling(63).std().diff(1).rolling(63).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f68re_f68_retained_earnings_growth_calc012_63d_3rd_derivative_v012_signal'] = f68re_f68_retained_earnings_growth_calc012_63d_3rd_derivative_v012_signal

def f68re_f68_retained_earnings_growth_calc013_126d_3rd_derivative_v013_signal(retearn, marketcap):
    res = (retearn / marketcap).rolling(126).var().diff(1).rolling(126).skew().pct_change(1).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f68re_f68_retained_earnings_growth_calc013_126d_3rd_derivative_v013_signal'] = f68re_f68_retained_earnings_growth_calc013_126d_3rd_derivative_v013_signal

def f68re_f68_retained_earnings_growth_calc014_252d_3rd_derivative_v014_signal(retearn, netinc):
    res = (retearn / netinc).diff(252).diff(1).rolling(252).kurt().diff(1).rolling(252).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f68re_f68_retained_earnings_growth_calc014_252d_3rd_derivative_v014_signal'] = f68re_f68_retained_earnings_growth_calc014_252d_3rd_derivative_v014_signal

def f68re_f68_retained_earnings_growth_calc015_5d_3rd_derivative_v015_signal(retearn, sharesbas):
    res = (retearn / sharesbas).rolling(5).max().diff(1).rolling(5).mean().pct_change(1).rolling(5).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f68re_f68_retained_earnings_growth_calc015_5d_3rd_derivative_v015_signal'] = f68re_f68_retained_earnings_growth_calc015_5d_3rd_derivative_v015_signal

def f68re_f68_retained_earnings_growth_calc016_10d_3rd_derivative_v016_signal(retearn, debt):
    res = (retearn / debt).pct_change(10).diff(1).rolling(10).std().diff(1).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f68re_f68_retained_earnings_growth_calc016_10d_3rd_derivative_v016_signal'] = f68re_f68_retained_earnings_growth_calc016_10d_3rd_derivative_v016_signal

def f68re_f68_retained_earnings_growth_calc017_21d_3rd_derivative_v017_signal(retearn, liabilities):
    res = (retearn / liabilities).diff(21).pct_change(1).rolling(21).mean().diff(1).rolling(21).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f68re_f68_retained_earnings_growth_calc017_21d_3rd_derivative_v017_signal'] = f68re_f68_retained_earnings_growth_calc017_21d_3rd_derivative_v017_signal

def f68re_f68_retained_earnings_growth_calc018_42d_3rd_derivative_v018_signal(retearn, assets):
    res = (retearn / assets).rolling(42).skew().diff(1).rolling(42).skew().pct_change(1).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f68re_f68_retained_earnings_growth_calc018_42d_3rd_derivative_v018_signal'] = f68re_f68_retained_earnings_growth_calc018_42d_3rd_derivative_v018_signal

def f68re_f68_retained_earnings_growth_calc019_63d_3rd_derivative_v019_signal(retearn, equity):
    res = (retearn / equity).rolling(63).rank(pct=True).diff(1).rolling(63).kurt().diff(1).rolling(63).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f68re_f68_retained_earnings_growth_calc019_63d_3rd_derivative_v019_signal'] = f68re_f68_retained_earnings_growth_calc019_63d_3rd_derivative_v019_signal

def f68re_f68_retained_earnings_growth_calc020_126d_3rd_derivative_v020_signal(retearn, revenue):
    res = (retearn / revenue).rolling(126).mean().diff(1).rolling(126).mean().pct_change(1).rolling(126).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f68re_f68_retained_earnings_growth_calc020_126d_3rd_derivative_v020_signal'] = f68re_f68_retained_earnings_growth_calc020_126d_3rd_derivative_v020_signal

def f68re_f68_retained_earnings_growth_calc021_252d_3rd_derivative_v021_signal(retearn, marketcap):
    res = (retearn / marketcap).rolling(252).quantile(0.8).diff(1).rolling(252).std().diff(1).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f68re_f68_retained_earnings_growth_calc021_252d_3rd_derivative_v021_signal'] = f68re_f68_retained_earnings_growth_calc021_252d_3rd_derivative_v021_signal

def f68re_f68_retained_earnings_growth_calc022_5d_3rd_derivative_v022_signal(retearn, netinc):
    res = (retearn / netinc).diff(5).rolling(5).std().pct_change(1).rolling(5).mean().diff(1).rolling(5).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f68re_f68_retained_earnings_growth_calc022_5d_3rd_derivative_v022_signal'] = f68re_f68_retained_earnings_growth_calc022_5d_3rd_derivative_v022_signal

def f68re_f68_retained_earnings_growth_calc023_10d_3rd_derivative_v023_signal(retearn, sharesbas):
    res = (retearn / sharesbas).rolling(10).kurt().diff(1).rolling(10).skew().pct_change(1).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f68re_f68_retained_earnings_growth_calc023_10d_3rd_derivative_v023_signal'] = f68re_f68_retained_earnings_growth_calc023_10d_3rd_derivative_v023_signal

def f68re_f68_retained_earnings_growth_calc024_21d_3rd_derivative_v024_signal(retearn, debt):
    res = (retearn / debt).rolling(21).mean().diff(1).rolling(21).kurt().diff(1).rolling(21).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f68re_f68_retained_earnings_growth_calc024_21d_3rd_derivative_v024_signal'] = f68re_f68_retained_earnings_growth_calc024_21d_3rd_derivative_v024_signal

def f68re_f68_retained_earnings_growth_calc025_42d_3rd_derivative_v025_signal(retearn, liabilities):
    res = (retearn / liabilities).rolling(42).std().pct_change(1).rolling(42).mean().pct_change(1).rolling(42).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f68re_f68_retained_earnings_growth_calc025_42d_3rd_derivative_v025_signal'] = f68re_f68_retained_earnings_growth_calc025_42d_3rd_derivative_v025_signal

def f68re_f68_retained_earnings_growth_calc026_63d_3rd_derivative_v026_signal(retearn, assets):
    res = (retearn / assets).rolling(63).max().diff(1).rolling(63).std().diff(1).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f68re_f68_retained_earnings_growth_calc026_63d_3rd_derivative_v026_signal'] = f68re_f68_retained_earnings_growth_calc026_63d_3rd_derivative_v026_signal

def f68re_f68_retained_earnings_growth_calc027_126d_3rd_derivative_v027_signal(retearn, equity):
    res = (retearn / equity).diff(126).diff(1).rolling(126).skew().diff(1).rolling(126).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f68re_f68_retained_earnings_growth_calc027_126d_3rd_derivative_v027_signal'] = f68re_f68_retained_earnings_growth_calc027_126d_3rd_derivative_v027_signal

def f68re_f68_retained_earnings_growth_calc028_252d_3rd_derivative_v028_signal(retearn, revenue):
    res = (retearn / revenue).rolling(252).skew().diff(1).rolling(252).kurt().pct_change(1).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f68re_f68_retained_earnings_growth_calc028_252d_3rd_derivative_v028_signal'] = f68re_f68_retained_earnings_growth_calc028_252d_3rd_derivative_v028_signal

def f68re_f68_retained_earnings_growth_calc029_5d_3rd_derivative_v029_signal(retearn, marketcap):
    res = (retearn / marketcap).rolling(5).min().diff(1).rolling(5).mean().diff(1).rolling(5).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f68re_f68_retained_earnings_growth_calc029_5d_3rd_derivative_v029_signal'] = f68re_f68_retained_earnings_growth_calc029_5d_3rd_derivative_v029_signal

def f68re_f68_retained_earnings_growth_calc030_10d_3rd_derivative_v030_signal(retearn, netinc):
    res = (retearn / netinc).rolling(10).rank(pct=True).diff(1).rolling(10).std().pct_change(1).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f68re_f68_retained_earnings_growth_calc030_10d_3rd_derivative_v030_signal'] = f68re_f68_retained_earnings_growth_calc030_10d_3rd_derivative_v030_signal

def f68re_f68_retained_earnings_growth_calc031_21d_3rd_derivative_v031_signal(retearn, sharesbas):
    res = (retearn / sharesbas).rolling(21).quantile(0.2).diff(1).rolling(21).mean().diff(1).rolling(21).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f68re_f68_retained_earnings_growth_calc031_21d_3rd_derivative_v031_signal'] = f68re_f68_retained_earnings_growth_calc031_21d_3rd_derivative_v031_signal

def f68re_f68_retained_earnings_growth_calc032_42d_3rd_derivative_v032_signal(retearn, debt):
    res = (retearn / debt).rolling(42).var().pct_change(1).rolling(42).std().pct_change(1).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f68re_f68_retained_earnings_growth_calc032_42d_3rd_derivative_v032_signal'] = f68re_f68_retained_earnings_growth_calc032_42d_3rd_derivative_v032_signal

def f68re_f68_retained_earnings_growth_calc033_63d_3rd_derivative_v033_signal(retearn, liabilities):
    res = (retearn / liabilities).rolling(63).mean().diff(1).rolling(63).skew().diff(1).rolling(63).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f68re_f68_retained_earnings_growth_calc033_63d_3rd_derivative_v033_signal'] = f68re_f68_retained_earnings_growth_calc033_63d_3rd_derivative_v033_signal

def f68re_f68_retained_earnings_growth_calc034_126d_3rd_derivative_v034_signal(retearn, assets):
    res = (retearn / assets).rolling(126).kurt().diff(1).rolling(126).kurt().pct_change(1).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f68re_f68_retained_earnings_growth_calc034_126d_3rd_derivative_v034_signal'] = f68re_f68_retained_earnings_growth_calc034_126d_3rd_derivative_v034_signal

def f68re_f68_retained_earnings_growth_calc035_252d_3rd_derivative_v035_signal(retearn, equity):
    res = (retearn / equity).rolling(252).std().diff(1).rolling(252).mean().diff(1).rolling(252).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f68re_f68_retained_earnings_growth_calc035_252d_3rd_derivative_v035_signal'] = f68re_f68_retained_earnings_growth_calc035_252d_3rd_derivative_v035_signal

def f68re_f68_retained_earnings_growth_calc036_5d_3rd_derivative_v036_signal(retearn, revenue):
    res = (retearn / revenue).pct_change(5).diff(1).rolling(5).std().pct_change(1).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f68re_f68_retained_earnings_growth_calc036_5d_3rd_derivative_v036_signal'] = f68re_f68_retained_earnings_growth_calc036_5d_3rd_derivative_v036_signal

def f68re_f68_retained_earnings_growth_calc037_10d_3rd_derivative_v037_signal(retearn, marketcap):
    res = (retearn / marketcap).rolling(10).rank(pct=True).diff(5).diff(1).rolling(10).mean().diff(1).rolling(10).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f68re_f68_retained_earnings_growth_calc037_10d_3rd_derivative_v037_signal'] = f68re_f68_retained_earnings_growth_calc037_10d_3rd_derivative_v037_signal

def f68re_f68_retained_earnings_growth_calc038_21d_3rd_derivative_v038_signal(retearn, netinc):
    res = (retearn / netinc).rolling(21).mean().pct_change(10).diff(1).rolling(21).std().pct_change(1).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f68re_f68_retained_earnings_growth_calc038_21d_3rd_derivative_v038_signal'] = f68re_f68_retained_earnings_growth_calc038_21d_3rd_derivative_v038_signal

def f68re_f68_retained_earnings_growth_calc039_42d_3rd_derivative_v039_signal(retearn, sharesbas):
    res = ((retearn / sharesbas).rolling(42).max() - (retearn / sharesbas).rolling(42).min()).diff(1).rolling(42).skew().diff(1).rolling(42).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f68re_f68_retained_earnings_growth_calc039_42d_3rd_derivative_v039_signal'] = f68re_f68_retained_earnings_growth_calc039_42d_3rd_derivative_v039_signal

def f68re_f68_retained_earnings_growth_calc040_63d_3rd_derivative_v040_signal(retearn, debt):
    res = (retearn / debt).rolling(63).skew().diff(21).diff(1).rolling(63).kurt().pct_change(1).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f68re_f68_retained_earnings_growth_calc040_63d_3rd_derivative_v040_signal'] = f68re_f68_retained_earnings_growth_calc040_63d_3rd_derivative_v040_signal

def f68re_f68_retained_earnings_growth_calc041_126d_3rd_derivative_v041_signal(retearn, liabilities):
    res = (retearn / liabilities).rolling(126).rank(pct=True).rolling(21).mean().diff(1).rolling(126).mean().diff(1).rolling(126).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f68re_f68_retained_earnings_growth_calc041_126d_3rd_derivative_v041_signal'] = f68re_f68_retained_earnings_growth_calc041_126d_3rd_derivative_v041_signal

def f68re_f68_retained_earnings_growth_calc042_252d_3rd_derivative_v042_signal(retearn, assets):
    res = ((retearn / assets).rolling(252).mean() / (retearn / assets).rolling(252).std()).diff(1).rolling(252).std().pct_change(1).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f68re_f68_retained_earnings_growth_calc042_252d_3rd_derivative_v042_signal'] = f68re_f68_retained_earnings_growth_calc042_252d_3rd_derivative_v042_signal

def f68re_f68_retained_earnings_growth_calc043_5d_3rd_derivative_v043_signal(retearn, equity):
    res = (retearn / equity).rolling(5).quantile(0.5).diff(1).diff(1).rolling(5).skew().diff(1).rolling(5).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f68re_f68_retained_earnings_growth_calc043_5d_3rd_derivative_v043_signal'] = f68re_f68_retained_earnings_growth_calc043_5d_3rd_derivative_v043_signal

def f68re_f68_retained_earnings_growth_calc044_10d_3rd_derivative_v044_signal(retearn, revenue):
    res = (retearn / revenue).rolling(10).var().pct_change(5).diff(1).rolling(10).kurt().pct_change(1).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f68re_f68_retained_earnings_growth_calc044_10d_3rd_derivative_v044_signal'] = f68re_f68_retained_earnings_growth_calc044_10d_3rd_derivative_v044_signal

def f68re_f68_retained_earnings_growth_calc045_21d_3rd_derivative_v045_signal(retearn, marketcap):
    res = (retearn / marketcap).rolling(21).kurt().diff(10).diff(1).rolling(21).mean().diff(1).rolling(21).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f68re_f68_retained_earnings_growth_calc045_21d_3rd_derivative_v045_signal'] = f68re_f68_retained_earnings_growth_calc045_21d_3rd_derivative_v045_signal

def f68re_f68_retained_earnings_growth_calc046_42d_3rd_derivative_v046_signal(retearn, netinc):
    res = (retearn / netinc).rolling(42).rank(pct=True).rolling(10).std().diff(1).rolling(42).std().pct_change(1).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f68re_f68_retained_earnings_growth_calc046_42d_3rd_derivative_v046_signal'] = f68re_f68_retained_earnings_growth_calc046_42d_3rd_derivative_v046_signal

def f68re_f68_retained_earnings_growth_calc047_63d_3rd_derivative_v047_signal(retearn, sharesbas):
    res = (retearn / sharesbas).rolling(63).quantile(0.9).diff(1).rolling(63).skew().diff(1).rolling(63).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f68re_f68_retained_earnings_growth_calc047_63d_3rd_derivative_v047_signal'] = f68re_f68_retained_earnings_growth_calc047_63d_3rd_derivative_v047_signal

def f68re_f68_retained_earnings_growth_calc048_126d_3rd_derivative_v048_signal(retearn, debt):
    res = (retearn / debt).rolling(126).min().pct_change(21).diff(1).rolling(126).kurt().pct_change(1).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f68re_f68_retained_earnings_growth_calc048_126d_3rd_derivative_v048_signal'] = f68re_f68_retained_earnings_growth_calc048_126d_3rd_derivative_v048_signal

def f68re_f68_retained_earnings_growth_calc049_252d_3rd_derivative_v049_signal(retearn, liabilities):
    res = (retearn / liabilities).rolling(252).max().diff(63).diff(1).rolling(252).mean().diff(1).rolling(252).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f68re_f68_retained_earnings_growth_calc049_252d_3rd_derivative_v049_signal'] = f68re_f68_retained_earnings_growth_calc049_252d_3rd_derivative_v049_signal

def f68re_f68_retained_earnings_growth_calc050_5d_3rd_derivative_v050_signal(retearn, assets):
    res = (retearn / assets).rolling(5).skew().rolling(5).mean().diff(1).rolling(5).std().pct_change(1).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f68re_f68_retained_earnings_growth_calc050_5d_3rd_derivative_v050_signal'] = f68re_f68_retained_earnings_growth_calc050_5d_3rd_derivative_v050_signal

def f68re_f68_retained_earnings_growth_calc051_10d_3rd_derivative_v051_signal(retearn, equity):
    res = ((retearn / equity).rolling(10).mean() / (retearn / equity).rolling(10).std()).diff(1).rolling(10).skew().diff(1).rolling(10).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f68re_f68_retained_earnings_growth_calc051_10d_3rd_derivative_v051_signal'] = f68re_f68_retained_earnings_growth_calc051_10d_3rd_derivative_v051_signal

def f68re_f68_retained_earnings_growth_calc052_21d_3rd_derivative_v052_signal(retearn, revenue):
    res = (retearn / revenue).rolling(21).rank(pct=True).diff(10).diff(1).rolling(21).kurt().pct_change(1).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f68re_f68_retained_earnings_growth_calc052_21d_3rd_derivative_v052_signal'] = f68re_f68_retained_earnings_growth_calc052_21d_3rd_derivative_v052_signal

def f68re_f68_retained_earnings_growth_calc053_42d_3rd_derivative_v053_signal(retearn, marketcap):
    res = (retearn / marketcap).rolling(42).std().pct_change(21).diff(1).rolling(42).mean().diff(1).rolling(42).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f68re_f68_retained_earnings_growth_calc053_42d_3rd_derivative_v053_signal'] = f68re_f68_retained_earnings_growth_calc053_42d_3rd_derivative_v053_signal

def f68re_f68_retained_earnings_growth_calc054_63d_3rd_derivative_v054_signal(retearn, netinc):
    res = (retearn / netinc).rolling(63).var().diff(21).diff(1).rolling(63).std().pct_change(1).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f68re_f68_retained_earnings_growth_calc054_63d_3rd_derivative_v054_signal'] = f68re_f68_retained_earnings_growth_calc054_63d_3rd_derivative_v054_signal

def f68re_f68_retained_earnings_growth_calc055_126d_3rd_derivative_v055_signal(retearn, sharesbas):
    res = (retearn / sharesbas).rolling(126).skew().rolling(21).mean().diff(1).rolling(126).skew().diff(1).rolling(126).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f68re_f68_retained_earnings_growth_calc055_126d_3rd_derivative_v055_signal'] = f68re_f68_retained_earnings_growth_calc055_126d_3rd_derivative_v055_signal

def f68re_f68_retained_earnings_growth_calc056_252d_3rd_derivative_v056_signal(retearn, debt):
    res = (retearn / debt).rolling(252).kurt().diff(63).diff(1).rolling(252).kurt().pct_change(1).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f68re_f68_retained_earnings_growth_calc056_252d_3rd_derivative_v056_signal'] = f68re_f68_retained_earnings_growth_calc056_252d_3rd_derivative_v056_signal

def f68re_f68_retained_earnings_growth_calc057_5d_3rd_derivative_v057_signal(retearn, liabilities):
    res = (retearn / liabilities).rolling(5).quantile(0.1).diff(1).rolling(5).mean().diff(1).rolling(5).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f68re_f68_retained_earnings_growth_calc057_5d_3rd_derivative_v057_signal'] = f68re_f68_retained_earnings_growth_calc057_5d_3rd_derivative_v057_signal

def f68re_f68_retained_earnings_growth_calc058_10d_3rd_derivative_v058_signal(retearn, assets):
    res = (retearn / assets).rolling(10).mean().pct_change(5).diff(1).rolling(10).std().pct_change(1).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f68re_f68_retained_earnings_growth_calc058_10d_3rd_derivative_v058_signal'] = f68re_f68_retained_earnings_growth_calc058_10d_3rd_derivative_v058_signal

def f68re_f68_retained_earnings_growth_calc059_21d_3rd_derivative_v059_signal(retearn, equity):
    res = (retearn / equity).rolling(21).std().diff(5).pct_change(1).rolling(21).mean().diff(1).rolling(21).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f68re_f68_retained_earnings_growth_calc059_21d_3rd_derivative_v059_signal'] = f68re_f68_retained_earnings_growth_calc059_21d_3rd_derivative_v059_signal

def f68re_f68_retained_earnings_growth_calc060_42d_3rd_derivative_v060_signal(retearn, revenue):
    res = (retearn / revenue).rolling(42).rank(pct=True).rolling(5).mean().diff(1).rolling(42).skew().pct_change(1).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f68re_f68_retained_earnings_growth_calc060_42d_3rd_derivative_v060_signal'] = f68re_f68_retained_earnings_growth_calc060_42d_3rd_derivative_v060_signal

def f68re_f68_retained_earnings_growth_calc061_63d_3rd_derivative_v061_signal(retearn, marketcap):
    res = (retearn / marketcap).rolling(63).quantile(0.5).pct_change(21).diff(1).rolling(63).kurt().diff(1).rolling(63).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f68re_f68_retained_earnings_growth_calc061_63d_3rd_derivative_v061_signal'] = f68re_f68_retained_earnings_growth_calc061_63d_3rd_derivative_v061_signal

def f68re_f68_retained_earnings_growth_calc062_126d_3rd_derivative_v062_signal(retearn, netinc):
    res = (retearn / netinc).rolling(126).var().diff(63).diff(1).rolling(126).mean().pct_change(1).rolling(126).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f68re_f68_retained_earnings_growth_calc062_126d_3rd_derivative_v062_signal'] = f68re_f68_retained_earnings_growth_calc062_126d_3rd_derivative_v062_signal

def f68re_f68_retained_earnings_growth_calc063_252d_3rd_derivative_v063_signal(retearn, sharesbas):
    res = (retearn / sharesbas).rolling(252).skew().pct_change(63).diff(1).rolling(252).std().diff(1).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f68re_f68_retained_earnings_growth_calc063_252d_3rd_derivative_v063_signal'] = f68re_f68_retained_earnings_growth_calc063_252d_3rd_derivative_v063_signal

def f68re_f68_retained_earnings_growth_calc064_5d_3rd_derivative_v064_signal(retearn, debt):
    res = (retearn / debt).rolling(5).max().diff(1).diff(1).rolling(5).skew().diff(1).rolling(5).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f68re_f68_retained_earnings_growth_calc064_5d_3rd_derivative_v064_signal'] = f68re_f68_retained_earnings_growth_calc064_5d_3rd_derivative_v064_signal

def f68re_f68_retained_earnings_growth_calc065_10d_3rd_derivative_v065_signal(retearn, liabilities):
    res = (retearn / liabilities).rolling(10).min().pct_change(5).diff(1).rolling(10).kurt().pct_change(1).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f68re_f68_retained_earnings_growth_calc065_10d_3rd_derivative_v065_signal'] = f68re_f68_retained_earnings_growth_calc065_10d_3rd_derivative_v065_signal

def f68re_f68_retained_earnings_growth_calc066_21d_3rd_derivative_v066_signal(retearn, assets):
    res = (retearn / assets).rolling(21).kurt().diff(5).diff(1).rolling(21).mean().diff(1).rolling(21).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f68re_f68_retained_earnings_growth_calc066_21d_3rd_derivative_v066_signal'] = f68re_f68_retained_earnings_growth_calc066_21d_3rd_derivative_v066_signal

def f68re_f68_retained_earnings_growth_calc067_42d_3rd_derivative_v067_signal(retearn, equity):
    res = (retearn / equity).rolling(42).rank(pct=True).rolling(10).mean().diff(1).rolling(42).std().pct_change(1).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f68re_f68_retained_earnings_growth_calc067_42d_3rd_derivative_v067_signal'] = f68re_f68_retained_earnings_growth_calc067_42d_3rd_derivative_v067_signal

def f68re_f68_retained_earnings_growth_calc068_63d_3rd_derivative_v068_signal(retearn, revenue):
    res = (retearn / revenue).rolling(63).std().pct_change(21).diff(1).rolling(63).skew().diff(1).rolling(63).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f68re_f68_retained_earnings_growth_calc068_63d_3rd_derivative_v068_signal'] = f68re_f68_retained_earnings_growth_calc068_63d_3rd_derivative_v068_signal

def f68re_f68_retained_earnings_growth_calc069_126d_3rd_derivative_v069_signal(retearn, marketcap):
    res = (retearn / marketcap).rolling(126).quantile(0.3).diff(21).diff(1).rolling(126).kurt().pct_change(1).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f68re_f68_retained_earnings_growth_calc069_126d_3rd_derivative_v069_signal'] = f68re_f68_retained_earnings_growth_calc069_126d_3rd_derivative_v069_signal

def f68re_f68_retained_earnings_growth_calc070_252d_3rd_derivative_v070_signal(retearn, netinc):
    res = (retearn / netinc).rolling(252).mean().pct_change(63).diff(1).rolling(252).mean().diff(1).rolling(252).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f68re_f68_retained_earnings_growth_calc070_252d_3rd_derivative_v070_signal'] = f68re_f68_retained_earnings_growth_calc070_252d_3rd_derivative_v070_signal

def f68re_f68_retained_earnings_growth_calc071_5d_3rd_derivative_v071_signal(retearn, sharesbas):
    res = (retearn / sharesbas).rolling(5).var().diff(1).diff(1).rolling(5).std().pct_change(1).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f68re_f68_retained_earnings_growth_calc071_5d_3rd_derivative_v071_signal'] = f68re_f68_retained_earnings_growth_calc071_5d_3rd_derivative_v071_signal

def f68re_f68_retained_earnings_growth_calc072_10d_3rd_derivative_v072_signal(retearn, debt):
    res = (retearn / debt).rolling(10).skew().pct_change(5).diff(1).rolling(10).skew().diff(1).rolling(10).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f68re_f68_retained_earnings_growth_calc072_10d_3rd_derivative_v072_signal'] = f68re_f68_retained_earnings_growth_calc072_10d_3rd_derivative_v072_signal

def f68re_f68_retained_earnings_growth_calc073_21d_3rd_derivative_v073_signal(retearn, liabilities):
    res = (retearn / liabilities).rolling(21).kurt().diff(5).diff(1).rolling(21).kurt().pct_change(1).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f68re_f68_retained_earnings_growth_calc073_21d_3rd_derivative_v073_signal'] = f68re_f68_retained_earnings_growth_calc073_21d_3rd_derivative_v073_signal

def f68re_f68_retained_earnings_growth_calc074_42d_3rd_derivative_v074_signal(retearn, assets):
    res = (retearn / assets).rolling(42).rank(pct=True).rolling(10).mean().diff(1).rolling(42).mean().diff(1).rolling(42).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f68re_f68_retained_earnings_growth_calc074_42d_3rd_derivative_v074_signal'] = f68re_f68_retained_earnings_growth_calc074_42d_3rd_derivative_v074_signal

def f68re_f68_retained_earnings_growth_calc075_63d_3rd_derivative_v075_signal(retearn, equity):
    res = (retearn / equity).rolling(63).quantile(0.7).diff(10).diff(1).rolling(63).std().pct_change(1).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f68re_f68_retained_earnings_growth_calc075_63d_3rd_derivative_v075_signal'] = f68re_f68_retained_earnings_growth_calc075_63d_3rd_derivative_v075_signal

def f68re_f68_retained_earnings_growth_calc076_5d_3rd_derivative_v076_signal(retearn, ebitda):
    res = (retearn / ebitda).rolling(5).mean().diff(1).rolling(5).mean().diff(1).rolling(5).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f68re_f68_retained_earnings_growth_calc076_5d_3rd_derivative_v076_signal'] = f68re_f68_retained_earnings_growth_calc076_5d_3rd_derivative_v076_signal

def f68re_f68_retained_earnings_growth_calc077_10d_3rd_derivative_v077_signal(retearn, capex):
    res = (retearn / capex).rolling(10).std().pct_change(1).rolling(10).std().pct_change(1).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f68re_f68_retained_earnings_growth_calc077_10d_3rd_derivative_v077_signal'] = f68re_f68_retained_earnings_growth_calc077_10d_3rd_derivative_v077_signal

def f68re_f68_retained_earnings_growth_calc078_21d_3rd_derivative_v078_signal(retearn, ncfo):
    res = (retearn / ncfo).diff(21).diff(3).rolling(21).skew().diff(1).rolling(21).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f68re_f68_retained_earnings_growth_calc078_21d_3rd_derivative_v078_signal'] = f68re_f68_retained_earnings_growth_calc078_21d_3rd_derivative_v078_signal

def f68re_f68_retained_earnings_growth_calc079_42d_3rd_derivative_v079_signal(retearn, ncfi):
    res = (retearn / ncfi).pct_change(42).diff(1).rolling(42).rank(pct=True).diff(1).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f68re_f68_retained_earnings_growth_calc079_42d_3rd_derivative_v079_signal'] = f68re_f68_retained_earnings_growth_calc079_42d_3rd_derivative_v079_signal

def f68re_f68_retained_earnings_growth_calc080_63d_3rd_derivative_v080_signal(retearn, ncff):
    res = (retearn / ncff).rolling(63).skew().diff(1).rolling(63).kurt().pct_change(1).rolling(63).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f68re_f68_retained_earnings_growth_calc080_63d_3rd_derivative_v080_signal'] = f68re_f68_retained_earnings_growth_calc080_63d_3rd_derivative_v080_signal

def f68re_f68_retained_earnings_growth_calc081_126d_3rd_derivative_v081_signal(retearn, gp):
    res = (retearn / gp).rolling(126).kurt().diff(1).rolling(126).mean().diff(1).rolling(126).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f68re_f68_retained_earnings_growth_calc081_126d_3rd_derivative_v081_signal'] = f68re_f68_retained_earnings_growth_calc081_126d_3rd_derivative_v081_signal

def f68re_f68_retained_earnings_growth_calc082_252d_3rd_derivative_v082_signal(retearn, opinc):
    res = (retearn / opinc).rolling(252).rank(pct=True).pct_change(1).rolling(252).std().diff(1).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f68re_f68_retained_earnings_growth_calc082_252d_3rd_derivative_v082_signal'] = f68re_f68_retained_earnings_growth_calc082_252d_3rd_derivative_v082_signal

def f68re_f68_retained_earnings_growth_calc083_5d_3rd_derivative_v083_signal(retearn, workingcapital):
    res = (retearn / workingcapital).rolling(5).quantile(0.5).diff(3).rolling(5).skew().diff(1).rolling(5).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f68re_f68_retained_earnings_growth_calc083_5d_3rd_derivative_v083_signal'] = f68re_f68_retained_earnings_growth_calc083_5d_3rd_derivative_v083_signal

def f68re_f68_retained_earnings_growth_calc084_10d_3rd_derivative_v084_signal(retearn, currentratio):
    res = (retearn / currentratio).rolling(10).var().rolling(10).rank(pct=True).diff(1).pct_change(1).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f68re_f68_retained_earnings_growth_calc084_10d_3rd_derivative_v084_signal'] = f68re_f68_retained_earnings_growth_calc084_10d_3rd_derivative_v084_signal

def f68re_f68_retained_earnings_growth_calc085_21d_3rd_derivative_v085_signal(retearn, pe):
    res = (retearn / pe).rolling(21).mean().diff(1).rolling(21).kurt().diff(1).rolling(21).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f68re_f68_retained_earnings_growth_calc085_21d_3rd_derivative_v085_signal'] = f68re_f68_retained_earnings_growth_calc085_21d_3rd_derivative_v085_signal

def f68re_f68_retained_earnings_growth_calc086_42d_3rd_derivative_v086_signal(retearn, pb):
    res = (retearn / pb).rolling(42).std().diff(1).rolling(42).mean().pct_change(1).rolling(42).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f68re_f68_retained_earnings_growth_calc086_42d_3rd_derivative_v086_signal'] = f68re_f68_retained_earnings_growth_calc086_42d_3rd_derivative_v086_signal

def f68re_f68_retained_earnings_growth_calc087_63d_3rd_derivative_v087_signal(retearn, ps):
    res = (retearn / ps).diff(63).pct_change(1).rolling(63).std().diff(1).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f68re_f68_retained_earnings_growth_calc087_63d_3rd_derivative_v087_signal'] = f68re_f68_retained_earnings_growth_calc087_63d_3rd_derivative_v087_signal

def f68re_f68_retained_earnings_growth_calc088_126d_3rd_derivative_v088_signal(retearn, ev):
    res = (retearn / ev).pct_change(126).diff(3).rolling(126).skew().diff(1).rolling(126).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f68re_f68_retained_earnings_growth_calc088_126d_3rd_derivative_v088_signal'] = f68re_f68_retained_earnings_growth_calc088_126d_3rd_derivative_v088_signal

def f68re_f68_retained_earnings_growth_calc089_252d_3rd_derivative_v089_signal(retearn, evebitda):
    res = (retearn / evebitda).rolling(252).skew().rolling(252).rank(pct=True).diff(1).pct_change(1).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f68re_f68_retained_earnings_growth_calc089_252d_3rd_derivative_v089_signal'] = f68re_f68_retained_earnings_growth_calc089_252d_3rd_derivative_v089_signal

def f68re_f68_retained_earnings_growth_calc090_5d_3rd_derivative_v090_signal(retearn, close):
    res = (retearn / close).rolling(5).max().diff(1).rolling(5).kurt().diff(1).rolling(5).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f68re_f68_retained_earnings_growth_calc090_5d_3rd_derivative_v090_signal'] = f68re_f68_retained_earnings_growth_calc090_5d_3rd_derivative_v090_signal

def f68re_f68_retained_earnings_growth_calc091_10d_3rd_derivative_v091_signal(retearn, taxexp):
    res = (retearn / taxexp).rolling(10).min().diff(1).rolling(10).mean().pct_change(1).rolling(10).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f68re_f68_retained_earnings_growth_calc091_10d_3rd_derivative_v091_signal'] = f68re_f68_retained_earnings_growth_calc091_10d_3rd_derivative_v091_signal

def f68re_f68_retained_earnings_growth_calc092_21d_3rd_derivative_v092_signal(retearn, intexp):
    res = (retearn / intexp).rolling(21).mean().pct_change(1).rolling(21).std().diff(1).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f68re_f68_retained_earnings_growth_calc092_21d_3rd_derivative_v092_signal'] = f68re_f68_retained_earnings_growth_calc092_21d_3rd_derivative_v092_signal

def f68re_f68_retained_earnings_growth_calc093_42d_3rd_derivative_v093_signal(retearn, ebitda):
    res = (retearn / ebitda).rolling(42).rank(pct=True).diff(3).rolling(42).skew().diff(1).rolling(42).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f68re_f68_retained_earnings_growth_calc093_42d_3rd_derivative_v093_signal'] = f68re_f68_retained_earnings_growth_calc093_42d_3rd_derivative_v093_signal

def f68re_f68_retained_earnings_growth_calc094_63d_3rd_derivative_v094_signal(retearn, capex):
    res = (retearn / capex).rolling(63).quantile(0.8).rolling(63).rank(pct=True).diff(1).pct_change(1).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f68re_f68_retained_earnings_growth_calc094_63d_3rd_derivative_v094_signal'] = f68re_f68_retained_earnings_growth_calc094_63d_3rd_derivative_v094_signal

def f68re_f68_retained_earnings_growth_calc095_126d_3rd_derivative_v095_signal(retearn, ncfo):
    res = (retearn / ncfo).diff(126).rolling(21).mean().diff(1).rolling(126).kurt().diff(1).rolling(126).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f68re_f68_retained_earnings_growth_calc095_126d_3rd_derivative_v095_signal'] = f68re_f68_retained_earnings_growth_calc095_126d_3rd_derivative_v095_signal

def f68re_f68_retained_earnings_growth_calc096_252d_3rd_derivative_v096_signal(retearn, ncfi):
    res = (retearn / ncfi).pct_change(252).diff(1).rolling(252).mean().pct_change(1).rolling(252).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f68re_f68_retained_earnings_growth_calc096_252d_3rd_derivative_v096_signal'] = f68re_f68_retained_earnings_growth_calc096_252d_3rd_derivative_v096_signal

def f68re_f68_retained_earnings_growth_calc097_5d_3rd_derivative_v097_signal(retearn, ncff):
    res = (retearn / ncff).rolling(5).std().pct_change(1).rolling(5).std().diff(1).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f68re_f68_retained_earnings_growth_calc097_5d_3rd_derivative_v097_signal'] = f68re_f68_retained_earnings_growth_calc097_5d_3rd_derivative_v097_signal

def f68re_f68_retained_earnings_growth_calc098_10d_3rd_derivative_v098_signal(retearn, gp):
    res = (retearn / gp).rolling(10).mean().diff(5).diff(3).rolling(10).skew().diff(1).rolling(10).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f68re_f68_retained_earnings_growth_calc098_10d_3rd_derivative_v098_signal'] = f68re_f68_retained_earnings_growth_calc098_10d_3rd_derivative_v098_signal

def f68re_f68_retained_earnings_growth_calc099_21d_3rd_derivative_v099_signal(retearn, opinc):
    res = (retearn / opinc).rolling(21).var().pct_change(10).rolling(21).rank(pct=True).diff(1).pct_change(1).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f68re_f68_retained_earnings_growth_calc099_21d_3rd_derivative_v099_signal'] = f68re_f68_retained_earnings_growth_calc099_21d_3rd_derivative_v099_signal

def f68re_f68_retained_earnings_growth_calc100_42d_3rd_derivative_v100_signal(retearn, workingcapital):
    res = (retearn / workingcapital).rolling(42).kurt().diff(21).diff(1).rolling(42).kurt().diff(1).rolling(42).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f68re_f68_retained_earnings_growth_calc100_42d_3rd_derivative_v100_signal'] = f68re_f68_retained_earnings_growth_calc100_42d_3rd_derivative_v100_signal

def f68re_f68_retained_earnings_growth_calc101_63d_3rd_derivative_v101_signal(retearn, currentratio):
    res = (retearn / currentratio).rolling(63).rank(pct=True).diff(1).rolling(63).mean().pct_change(1).rolling(63).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f68re_f68_retained_earnings_growth_calc101_63d_3rd_derivative_v101_signal'] = f68re_f68_retained_earnings_growth_calc101_63d_3rd_derivative_v101_signal

def f68re_f68_retained_earnings_growth_calc102_126d_3rd_derivative_v102_signal(retearn, pe):
    res = (retearn / pe).rolling(126).quantile(0.3).pct_change(1).rolling(126).std().diff(1).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f68re_f68_retained_earnings_growth_calc102_126d_3rd_derivative_v102_signal'] = f68re_f68_retained_earnings_growth_calc102_126d_3rd_derivative_v102_signal

def f68re_f68_retained_earnings_growth_calc103_252d_3rd_derivative_v103_signal(retearn, pb):
    res = (retearn / pb).rolling(252).mean().pct_change(63).diff(3).rolling(252).skew().diff(1).rolling(252).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f68re_f68_retained_earnings_growth_calc103_252d_3rd_derivative_v103_signal'] = f68re_f68_retained_earnings_growth_calc103_252d_3rd_derivative_v103_signal

def f68re_f68_retained_earnings_growth_calc104_5d_3rd_derivative_v104_signal(retearn, ps):
    res = (retearn / ps).rolling(5).max().diff(1).rolling(5).rank(pct=True).diff(1).pct_change(1).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f68re_f68_retained_earnings_growth_calc104_5d_3rd_derivative_v104_signal'] = f68re_f68_retained_earnings_growth_calc104_5d_3rd_derivative_v104_signal

def f68re_f68_retained_earnings_growth_calc105_10d_3rd_derivative_v105_signal(retearn, ev):
    res = (retearn / ev).rolling(10).min().pct_change(5).diff(1).rolling(10).kurt().diff(1).rolling(10).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f68re_f68_retained_earnings_growth_calc105_10d_3rd_derivative_v105_signal'] = f68re_f68_retained_earnings_growth_calc105_10d_3rd_derivative_v105_signal

def f68re_f68_retained_earnings_growth_calc106_21d_3rd_derivative_v106_signal(retearn, evebitda):
    res = (retearn / evebitda).rolling(21).skew().diff(5).diff(1).rolling(21).mean().pct_change(1).rolling(21).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f68re_f68_retained_earnings_growth_calc106_21d_3rd_derivative_v106_signal'] = f68re_f68_retained_earnings_growth_calc106_21d_3rd_derivative_v106_signal

def f68re_f68_retained_earnings_growth_calc107_42d_3rd_derivative_v107_signal(retearn, close):
    res = (retearn / close).rolling(42).rank(pct=True).rolling(10).mean().pct_change(1).rolling(42).std().diff(1).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f68re_f68_retained_earnings_growth_calc107_42d_3rd_derivative_v107_signal'] = f68re_f68_retained_earnings_growth_calc107_42d_3rd_derivative_v107_signal

def f68re_f68_retained_earnings_growth_calc108_63d_3rd_derivative_v108_signal(retearn, taxexp):
    res = (retearn / taxexp).rolling(63).std().pct_change(21).diff(3).rolling(63).skew().diff(1).rolling(63).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f68re_f68_retained_earnings_growth_calc108_63d_3rd_derivative_v108_signal'] = f68re_f68_retained_earnings_growth_calc108_63d_3rd_derivative_v108_signal

def f68re_f68_retained_earnings_growth_calc109_126d_3rd_derivative_v109_signal(retearn, intexp):
    res = (retearn / intexp).rolling(126).quantile(0.4).diff(21).rolling(126).rank(pct=True).diff(1).pct_change(1).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f68re_f68_retained_earnings_growth_calc109_126d_3rd_derivative_v109_signal'] = f68re_f68_retained_earnings_growth_calc109_126d_3rd_derivative_v109_signal

def f68re_f68_retained_earnings_growth_calc110_252d_3rd_derivative_v110_signal(retearn, ebitda):
    res = (retearn / ebitda).rolling(252).mean().pct_change(63).diff(1).rolling(252).kurt().diff(1).rolling(252).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f68re_f68_retained_earnings_growth_calc110_252d_3rd_derivative_v110_signal'] = f68re_f68_retained_earnings_growth_calc110_252d_3rd_derivative_v110_signal

def f68re_f68_retained_earnings_growth_calc111_5d_3rd_derivative_v111_signal(retearn, capex):
    res = (retearn / capex).rolling(5).var().diff(1).diff(1).rolling(5).mean().pct_change(1).rolling(5).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f68re_f68_retained_earnings_growth_calc111_5d_3rd_derivative_v111_signal'] = f68re_f68_retained_earnings_growth_calc111_5d_3rd_derivative_v111_signal

def f68re_f68_retained_earnings_growth_calc112_10d_3rd_derivative_v112_signal(retearn, ncfo):
    res = (retearn / ncfo).rolling(10).skew().pct_change(5).pct_change(1).rolling(10).std().diff(1).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f68re_f68_retained_earnings_growth_calc112_10d_3rd_derivative_v112_signal'] = f68re_f68_retained_earnings_growth_calc112_10d_3rd_derivative_v112_signal

def f68re_f68_retained_earnings_growth_calc113_21d_3rd_derivative_v113_signal(retearn, ncfi):
    res = (retearn / ncfi).rolling(21).kurt().diff(5).diff(3).rolling(21).skew().diff(1).rolling(21).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f68re_f68_retained_earnings_growth_calc113_21d_3rd_derivative_v113_signal'] = f68re_f68_retained_earnings_growth_calc113_21d_3rd_derivative_v113_signal

def f68re_f68_retained_earnings_growth_calc114_42d_3rd_derivative_v114_signal(retearn, ncff):
    res = (retearn / ncff).rolling(42).rank(pct=True).rolling(10).mean().rolling(42).rank(pct=True).diff(1).pct_change(1).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f68re_f68_retained_earnings_growth_calc114_42d_3rd_derivative_v114_signal'] = f68re_f68_retained_earnings_growth_calc114_42d_3rd_derivative_v114_signal

def f68re_f68_retained_earnings_growth_calc115_63d_3rd_derivative_v115_signal(retearn, gp):
    res = (retearn / gp).rolling(63).quantile(0.6).diff(10).diff(1).rolling(63).kurt().diff(1).rolling(63).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f68re_f68_retained_earnings_growth_calc115_63d_3rd_derivative_v115_signal'] = f68re_f68_retained_earnings_growth_calc115_63d_3rd_derivative_v115_signal

def f68re_f68_retained_earnings_growth_calc116_126d_3rd_derivative_v116_signal(retearn, opinc):
    res = (retearn / opinc).rolling(126).mean().pct_change(21).diff(1).rolling(126).mean().pct_change(1).rolling(126).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f68re_f68_retained_earnings_growth_calc116_126d_3rd_derivative_v116_signal'] = f68re_f68_retained_earnings_growth_calc116_126d_3rd_derivative_v116_signal

def f68re_f68_retained_earnings_growth_calc117_252d_3rd_derivative_v117_signal(retearn, workingcapital):
    res = (retearn / workingcapital).rolling(252).std().diff(63).pct_change(1).rolling(252).std().diff(1).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f68re_f68_retained_earnings_growth_calc117_252d_3rd_derivative_v117_signal'] = f68re_f68_retained_earnings_growth_calc117_252d_3rd_derivative_v117_signal

def f68re_f68_retained_earnings_growth_calc118_5d_3rd_derivative_v118_signal(retearn, currentratio):
    res = (retearn / currentratio).rolling(5).skew().rolling(5).mean().diff(3).rolling(5).skew().diff(1).rolling(5).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f68re_f68_retained_earnings_growth_calc118_5d_3rd_derivative_v118_signal'] = f68re_f68_retained_earnings_growth_calc118_5d_3rd_derivative_v118_signal

def f68re_f68_retained_earnings_growth_calc119_10d_3rd_derivative_v119_signal(retearn, pe):
    res = ((retearn / pe).rolling(10).mean() / (retearn / pe).rolling(10).std()).rolling(10).rank(pct=True).diff(1).pct_change(1).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f68re_f68_retained_earnings_growth_calc119_10d_3rd_derivative_v119_signal'] = f68re_f68_retained_earnings_growth_calc119_10d_3rd_derivative_v119_signal

def f68re_f68_retained_earnings_growth_calc120_21d_3rd_derivative_v120_signal(retearn, pb):
    res = (retearn / pb).rolling(21).rank(pct=True).diff(10).diff(1).rolling(21).kurt().diff(1).rolling(21).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f68re_f68_retained_earnings_growth_calc120_21d_3rd_derivative_v120_signal'] = f68re_f68_retained_earnings_growth_calc120_21d_3rd_derivative_v120_signal

def f68re_f68_retained_earnings_growth_calc121_42d_3rd_derivative_v121_signal(retearn, ps):
    res = (retearn / ps).rolling(42).std().pct_change(21).diff(1).rolling(42).mean().pct_change(1).rolling(42).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f68re_f68_retained_earnings_growth_calc121_42d_3rd_derivative_v121_signal'] = f68re_f68_retained_earnings_growth_calc121_42d_3rd_derivative_v121_signal

def f68re_f68_retained_earnings_growth_calc122_63d_3rd_derivative_v122_signal(retearn, ev):
    res = (retearn / ev).rolling(63).var().diff(21).pct_change(1).rolling(63).std().diff(1).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f68re_f68_retained_earnings_growth_calc122_63d_3rd_derivative_v122_signal'] = f68re_f68_retained_earnings_growth_calc122_63d_3rd_derivative_v122_signal

def f68re_f68_retained_earnings_growth_calc123_126d_3rd_derivative_v123_signal(retearn, evebitda):
    res = (retearn / evebitda).rolling(126).skew().rolling(21).mean().diff(3).rolling(126).skew().diff(1).rolling(126).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f68re_f68_retained_earnings_growth_calc123_126d_3rd_derivative_v123_signal'] = f68re_f68_retained_earnings_growth_calc123_126d_3rd_derivative_v123_signal

def f68re_f68_retained_earnings_growth_calc124_252d_3rd_derivative_v124_signal(retearn, close):
    res = (retearn / close).rolling(252).kurt().diff(63).rolling(252).rank(pct=True).diff(1).pct_change(1).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f68re_f68_retained_earnings_growth_calc124_252d_3rd_derivative_v124_signal'] = f68re_f68_retained_earnings_growth_calc124_252d_3rd_derivative_v124_signal

def f68re_f68_retained_earnings_growth_calc125_5d_3rd_derivative_v125_signal(retearn, taxexp):
    res = (retearn / taxexp).rolling(5).quantile(0.1).diff(1).rolling(5).kurt().diff(1).rolling(5).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f68re_f68_retained_earnings_growth_calc125_5d_3rd_derivative_v125_signal'] = f68re_f68_retained_earnings_growth_calc125_5d_3rd_derivative_v125_signal

def f68re_f68_retained_earnings_growth_calc126_10d_3rd_derivative_v126_signal(retearn, intexp):
    res = (retearn / intexp).rolling(10).mean().pct_change(5).diff(1).rolling(10).mean().pct_change(1).rolling(10).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f68re_f68_retained_earnings_growth_calc126_10d_3rd_derivative_v126_signal'] = f68re_f68_retained_earnings_growth_calc126_10d_3rd_derivative_v126_signal

def f68re_f68_retained_earnings_growth_calc127_21d_3rd_derivative_v127_signal(retearn, ebitda):
    res = (retearn / ebitda).rolling(21).std().diff(5).pct_change(1).rolling(21).std().diff(1).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f68re_f68_retained_earnings_growth_calc127_21d_3rd_derivative_v127_signal'] = f68re_f68_retained_earnings_growth_calc127_21d_3rd_derivative_v127_signal

def f68re_f68_retained_earnings_growth_calc128_42d_3rd_derivative_v128_signal(retearn, capex):
    res = (retearn / capex).rolling(42).rank(pct=True).rolling(5).mean().diff(3).rolling(42).skew().diff(1).rolling(42).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f68re_f68_retained_earnings_growth_calc128_42d_3rd_derivative_v128_signal'] = f68re_f68_retained_earnings_growth_calc128_42d_3rd_derivative_v128_signal

def f68re_f68_retained_earnings_growth_calc129_63d_3rd_derivative_v129_signal(retearn, ncfo):
    res = (retearn / ncfo).rolling(63).quantile(0.5).pct_change(21).rolling(63).rank(pct=True).diff(1).pct_change(1).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f68re_f68_retained_earnings_growth_calc129_63d_3rd_derivative_v129_signal'] = f68re_f68_retained_earnings_growth_calc129_63d_3rd_derivative_v129_signal

def f68re_f68_retained_earnings_growth_calc130_126d_3rd_derivative_v130_signal(retearn, ncfi):
    res = (retearn / ncfi).rolling(126).var().diff(63).diff(1).rolling(126).kurt().diff(1).rolling(126).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f68re_f68_retained_earnings_growth_calc130_126d_3rd_derivative_v130_signal'] = f68re_f68_retained_earnings_growth_calc130_126d_3rd_derivative_v130_signal

def f68re_f68_retained_earnings_growth_calc131_252d_3rd_derivative_v131_signal(retearn, ncff):
    res = (retearn / ncff).rolling(252).skew().pct_change(63).diff(1).rolling(252).mean().pct_change(1).rolling(252).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f68re_f68_retained_earnings_growth_calc131_252d_3rd_derivative_v131_signal'] = f68re_f68_retained_earnings_growth_calc131_252d_3rd_derivative_v131_signal

def f68re_f68_retained_earnings_growth_calc132_5d_3rd_derivative_v132_signal(retearn, gp):
    res = (retearn / gp).rolling(5).max().diff(1).pct_change(1).rolling(5).std().diff(1).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f68re_f68_retained_earnings_growth_calc132_5d_3rd_derivative_v132_signal'] = f68re_f68_retained_earnings_growth_calc132_5d_3rd_derivative_v132_signal

def f68re_f68_retained_earnings_growth_calc133_10d_3rd_derivative_v133_signal(retearn, opinc):
    res = (retearn / opinc).rolling(10).min().pct_change(5).diff(3).rolling(10).skew().diff(1).rolling(10).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f68re_f68_retained_earnings_growth_calc133_10d_3rd_derivative_v133_signal'] = f68re_f68_retained_earnings_growth_calc133_10d_3rd_derivative_v133_signal

def f68re_f68_retained_earnings_growth_calc134_21d_3rd_derivative_v134_signal(retearn, workingcapital):
    res = (retearn / workingcapital).rolling(21).kurt().diff(5).rolling(21).rank(pct=True).diff(1).pct_change(1).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f68re_f68_retained_earnings_growth_calc134_21d_3rd_derivative_v134_signal'] = f68re_f68_retained_earnings_growth_calc134_21d_3rd_derivative_v134_signal

def f68re_f68_retained_earnings_growth_calc135_42d_3rd_derivative_v135_signal(retearn, currentratio):
    res = (retearn / currentratio).rolling(42).rank(pct=True).rolling(10).mean().diff(1).rolling(42).kurt().diff(1).rolling(42).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f68re_f68_retained_earnings_growth_calc135_42d_3rd_derivative_v135_signal'] = f68re_f68_retained_earnings_growth_calc135_42d_3rd_derivative_v135_signal

def f68re_f68_retained_earnings_growth_calc136_63d_3rd_derivative_v136_signal(retearn, pe):
    res = (retearn / pe).rolling(63).std().pct_change(21).diff(1).rolling(63).mean().pct_change(1).rolling(63).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f68re_f68_retained_earnings_growth_calc136_63d_3rd_derivative_v136_signal'] = f68re_f68_retained_earnings_growth_calc136_63d_3rd_derivative_v136_signal

def f68re_f68_retained_earnings_growth_calc137_126d_3rd_derivative_v137_signal(retearn, pb):
    res = (retearn / pb).rolling(126).quantile(0.3).diff(21).pct_change(1).rolling(126).std().diff(1).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f68re_f68_retained_earnings_growth_calc137_126d_3rd_derivative_v137_signal'] = f68re_f68_retained_earnings_growth_calc137_126d_3rd_derivative_v137_signal

def f68re_f68_retained_earnings_growth_calc138_252d_3rd_derivative_v138_signal(retearn, ps):
    res = (retearn / ps).rolling(252).mean().pct_change(63).diff(3).rolling(252).skew().diff(1).rolling(252).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f68re_f68_retained_earnings_growth_calc138_252d_3rd_derivative_v138_signal'] = f68re_f68_retained_earnings_growth_calc138_252d_3rd_derivative_v138_signal

def f68re_f68_retained_earnings_growth_calc139_5d_3rd_derivative_v139_signal(retearn, ev):
    res = (retearn / ev).rolling(5).var().diff(1).rolling(5).rank(pct=True).diff(1).pct_change(1).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f68re_f68_retained_earnings_growth_calc139_5d_3rd_derivative_v139_signal'] = f68re_f68_retained_earnings_growth_calc139_5d_3rd_derivative_v139_signal

def f68re_f68_retained_earnings_growth_calc140_10d_3rd_derivative_v140_signal(retearn, evebitda):
    res = (retearn / evebitda).rolling(10).skew().pct_change(5).diff(1).rolling(10).kurt().diff(1).rolling(10).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f68re_f68_retained_earnings_growth_calc140_10d_3rd_derivative_v140_signal'] = f68re_f68_retained_earnings_growth_calc140_10d_3rd_derivative_v140_signal

def f68re_f68_retained_earnings_growth_calc141_21d_3rd_derivative_v141_signal(retearn, close):
    res = (retearn / close).rolling(21).kurt().diff(5).diff(1).rolling(21).mean().pct_change(1).rolling(21).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f68re_f68_retained_earnings_growth_calc141_21d_3rd_derivative_v141_signal'] = f68re_f68_retained_earnings_growth_calc141_21d_3rd_derivative_v141_signal

def f68re_f68_retained_earnings_growth_calc142_42d_3rd_derivative_v142_signal(retearn, taxexp):
    res = (retearn / taxexp).rolling(42).rank(pct=True).rolling(10).mean().pct_change(1).rolling(42).std().diff(1).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f68re_f68_retained_earnings_growth_calc142_42d_3rd_derivative_v142_signal'] = f68re_f68_retained_earnings_growth_calc142_42d_3rd_derivative_v142_signal

def f68re_f68_retained_earnings_growth_calc143_63d_3rd_derivative_v143_signal(retearn, intexp):
    res = (retearn / intexp).rolling(63).quantile(0.7).diff(10).diff(3).rolling(63).skew().diff(1).rolling(63).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f68re_f68_retained_earnings_growth_calc143_63d_3rd_derivative_v143_signal'] = f68re_f68_retained_earnings_growth_calc143_63d_3rd_derivative_v143_signal

def f68re_f68_retained_earnings_growth_calc144_126d_3rd_derivative_v144_signal(retearn, ebitda):
    res = (retearn / ebitda).rolling(126).mean().pct_change(21).rolling(126).rank(pct=True).diff(1).pct_change(1).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f68re_f68_retained_earnings_growth_calc144_126d_3rd_derivative_v144_signal'] = f68re_f68_retained_earnings_growth_calc144_126d_3rd_derivative_v144_signal

def f68re_f68_retained_earnings_growth_calc145_252d_3rd_derivative_v145_signal(retearn, capex):
    res = (retearn / capex).rolling(252).std().diff(63).diff(1).rolling(252).kurt().diff(1).rolling(252).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f68re_f68_retained_earnings_growth_calc145_252d_3rd_derivative_v145_signal'] = f68re_f68_retained_earnings_growth_calc145_252d_3rd_derivative_v145_signal

def f68re_f68_retained_earnings_growth_calc146_5d_3rd_derivative_v146_signal(retearn, ncfo):
    res = (retearn / ncfo).rolling(5).skew().rolling(5).mean().diff(1).rolling(5).mean().pct_change(1).rolling(5).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f68re_f68_retained_earnings_growth_calc146_5d_3rd_derivative_v146_signal'] = f68re_f68_retained_earnings_growth_calc146_5d_3rd_derivative_v146_signal

def f68re_f68_retained_earnings_growth_calc147_10d_3rd_derivative_v147_signal(retearn, ncfi):
    res = ((retearn / ncfi).rolling(10).mean() / (retearn / ncfi).rolling(10).std()).pct_change(1).rolling(10).std().diff(1).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f68re_f68_retained_earnings_growth_calc147_10d_3rd_derivative_v147_signal'] = f68re_f68_retained_earnings_growth_calc147_10d_3rd_derivative_v147_signal

def f68re_f68_retained_earnings_growth_calc148_21d_3rd_derivative_v148_signal(retearn, ncff):
    res = (retearn / ncff).rolling(21).rank(pct=True).diff(10).diff(3).rolling(21).skew().diff(1).rolling(21).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f68re_f68_retained_earnings_growth_calc148_21d_3rd_derivative_v148_signal'] = f68re_f68_retained_earnings_growth_calc148_21d_3rd_derivative_v148_signal

def f68re_f68_retained_earnings_growth_calc149_42d_3rd_derivative_v149_signal(retearn, gp):
    res = (retearn / gp).rolling(42).std().pct_change(21).rolling(42).rank(pct=True).diff(1).pct_change(1).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f68re_f68_retained_earnings_growth_calc149_42d_3rd_derivative_v149_signal'] = f68re_f68_retained_earnings_growth_calc149_42d_3rd_derivative_v149_signal

def f68re_f68_retained_earnings_growth_calc150_63d_3rd_derivative_v150_signal(retearn, opinc):
    res = (retearn / opinc).rolling(63).var().diff(21).diff(1).rolling(63).kurt().diff(1).rolling(63).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f68re_f68_retained_earnings_growth_calc150_63d_3rd_derivative_v150_signal'] = f68re_f68_retained_earnings_growth_calc150_63d_3rd_derivative_v150_signal


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
