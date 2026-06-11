import inspect
import numpy as np
import pandas as pd

TRADING_DAYS_YEAR = 252
TRADING_DAYS_TWOYEAR = 504
TRADING_DAYS_FIVEYEAR = 1260
TRADING_DAYS_HALF = 126
TRADING_DAYS_QUARTER = 63
TRADING_DAYS_MONTH = 21
TRADING_DAYS_WEEK = 5

HURDLE = 0.08


def _z(s, w):
    m = s.rolling(w, min_periods=max(1, w // 2)).mean()
    sd = s.rolling(w, min_periods=max(1, w // 2)).std()
    return (s - m) / sd.replace(0, np.nan)


def _mean(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def _std(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).std()


def _pctrank(s, w):
    return s.rolling(w, min_periods=max(1, w // 4)).rank(pct=True) - 0.5


def _assetturn(revenue, assets):
    return revenue / assets.replace(0, np.nan)


def _equityturn(revenue, equity):
    return revenue / equity.replace(0, np.nan)


def _invcapturn(revenue, invcap):
    return revenue / invcap.replace(0, np.nan)


def _tangroic(ebit, tangibles):
    return ebit / tangibles.replace(0, np.nan)


def _intangshare(intangibles, assets):
    return intangibles / assets.replace(0, np.nan)


def _tangshare(tangibles, assets):
    return tangibles / assets.replace(0, np.nan)


def _retmean(roic, roa, ros):
    return pd.concat([roic, roa, ros], axis=1).mean(axis=1)


def _retdisp(roic, roa, ros):
    return pd.concat([roic, roa, ros], axis=1).std(axis=1)

def f50rq_f50_capital_returns_quality_roiclvl_21d_slope_v001_signal(roic):
    base = roic
    d = base.diff(21) / float(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f50rq_f50_capital_returns_quality_roiclvl_63d_slope_v002_signal(roic):
    base = roic
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f50rq_f50_capital_returns_quality_roiclvl_252d_slope_v003_signal(roic):
    base = roic
    d = base.diff(252) / float(252)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f50rq_f50_capital_returns_quality_roicz_42d_slope_v004_signal(roic):
    base = _z(roic, 252)
    d = base.diff(42) / float(42)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f50rq_f50_capital_returns_quality_roicz_126d_slope_v005_signal(roic):
    base = _z(roic, 252)
    d = base.diff(126) / float(126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f50rq_f50_capital_returns_quality_roicz_252d_slope_v006_signal(roic):
    base = _z(roic, 252)
    d = base.diff(252) / float(252)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f50rq_f50_capital_returns_quality_roicpct_21d_slope_v007_signal(roic):
    base = _pctrank(roic, 504)
    d = base.diff(21) / float(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f50rq_f50_capital_returns_quality_roicpct_63d_slope_v008_signal(roic):
    base = _pctrank(roic, 504)
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f50rq_f50_capital_returns_quality_roicpct_126d_slope_v009_signal(roic):
    base = _pctrank(roic, 504)
    d = base.diff(126) / float(126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f50rq_f50_capital_returns_quality_roicvol_21d_slope_v010_signal(roic):
    base = _std(roic, 63)
    d = base.diff(21) / float(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f50rq_f50_capital_returns_quality_roicvol_63d_slope_v011_signal(roic):
    base = _std(roic, 63)
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f50rq_f50_capital_returns_quality_roicvol_126d_slope_v012_signal(roic):
    base = _std(roic, 63)
    d = base.diff(126) / float(126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f50rq_f50_capital_returns_quality_roicconv_21d_slope_v013_signal(roic):
    base = np.sign(roic - HURDLE) * (roic - HURDLE) ** 2
    d = base.diff(21) / float(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f50rq_f50_capital_returns_quality_roicconv_63d_slope_v014_signal(roic):
    base = np.sign(roic - HURDLE) * (roic - HURDLE) ** 2
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f50rq_f50_capital_returns_quality_roicconv_252d_slope_v015_signal(roic):
    base = np.sign(roic - HURDLE) * (roic - HURDLE) ** 2
    d = base.diff(252) / float(252)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f50rq_f50_capital_returns_quality_roicconsist_42d_slope_v016_signal(roic):
    base = _mean(roic, 126) / _std(roic, 126).replace(0, np.nan)
    d = base.diff(42) / float(42)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f50rq_f50_capital_returns_quality_roicconsist_126d_slope_v017_signal(roic):
    base = _mean(roic, 126) / _std(roic, 126).replace(0, np.nan)
    d = base.diff(126) / float(126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f50rq_f50_capital_returns_quality_roicconsist_252d_slope_v018_signal(roic):
    base = _mean(roic, 126) / _std(roic, 126).replace(0, np.nan)
    d = base.diff(252) / float(252)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f50rq_f50_capital_returns_quality_roalvl_21d_slope_v019_signal(roa):
    base = roa
    d = base.diff(21) / float(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f50rq_f50_capital_returns_quality_roalvl_63d_slope_v020_signal(roa):
    base = roa
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f50rq_f50_capital_returns_quality_roalvl_252d_slope_v021_signal(roa):
    base = roa
    d = base.diff(252) / float(252)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f50rq_f50_capital_returns_quality_roaz_42d_slope_v022_signal(roa):
    base = _z(roa, 252)
    d = base.diff(42) / float(42)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f50rq_f50_capital_returns_quality_roaz_126d_slope_v023_signal(roa):
    base = _z(roa, 252)
    d = base.diff(126) / float(126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f50rq_f50_capital_returns_quality_roaz_252d_slope_v024_signal(roa):
    base = _z(roa, 252)
    d = base.diff(252) / float(252)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f50rq_f50_capital_returns_quality_roapct_21d_slope_v025_signal(roa):
    base = _pctrank(roa, 504)
    d = base.diff(21) / float(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f50rq_f50_capital_returns_quality_roapct_63d_slope_v026_signal(roa):
    base = _pctrank(roa, 504)
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f50rq_f50_capital_returns_quality_roapct_126d_slope_v027_signal(roa):
    base = _pctrank(roa, 504)
    d = base.diff(126) / float(126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f50rq_f50_capital_returns_quality_roavol_21d_slope_v028_signal(roa):
    base = _std(roa, 63)
    d = base.diff(21) / float(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f50rq_f50_capital_returns_quality_roavol_63d_slope_v029_signal(roa):
    base = _std(roa, 63)
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f50rq_f50_capital_returns_quality_roavol_252d_slope_v030_signal(roa):
    base = _std(roa, 63)
    d = base.diff(252) / float(252)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f50rq_f50_capital_returns_quality_roaconv_42d_slope_v031_signal(roa):
    base = np.sign(roa - _mean(roa, 252)) * (roa - _mean(roa, 252)) ** 2
    d = base.diff(42) / float(42)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f50rq_f50_capital_returns_quality_roaconv_126d_slope_v032_signal(roa):
    base = np.sign(roa - _mean(roa, 252)) * (roa - _mean(roa, 252)) ** 2
    d = base.diff(126) / float(126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f50rq_f50_capital_returns_quality_roaconv_252d_slope_v033_signal(roa):
    base = np.sign(roa - _mean(roa, 252)) * (roa - _mean(roa, 252)) ** 2
    d = base.diff(252) / float(252)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f50rq_f50_capital_returns_quality_roslvl_21d_slope_v034_signal(ros):
    base = ros
    d = base.diff(21) / float(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f50rq_f50_capital_returns_quality_roslvl_63d_slope_v035_signal(ros):
    base = ros
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f50rq_f50_capital_returns_quality_roslvl_252d_slope_v036_signal(ros):
    base = ros
    d = base.diff(252) / float(252)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f50rq_f50_capital_returns_quality_rosz_42d_slope_v037_signal(ros):
    base = _z(ros, 252)
    d = base.diff(42) / float(42)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f50rq_f50_capital_returns_quality_rosz_126d_slope_v038_signal(ros):
    base = _z(ros, 252)
    d = base.diff(126) / float(126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f50rq_f50_capital_returns_quality_rosz_252d_slope_v039_signal(ros):
    base = _z(ros, 252)
    d = base.diff(252) / float(252)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f50rq_f50_capital_returns_quality_rospct_21d_slope_v040_signal(ros):
    base = _pctrank(ros, 504)
    d = base.diff(21) / float(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f50rq_f50_capital_returns_quality_rospct_63d_slope_v041_signal(ros):
    base = _pctrank(ros, 504)
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f50rq_f50_capital_returns_quality_rospct_126d_slope_v042_signal(ros):
    base = _pctrank(ros, 504)
    d = base.diff(126) / float(126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f50rq_f50_capital_returns_quality_rosvol_21d_slope_v043_signal(ros):
    base = _std(ros, 63)
    d = base.diff(21) / float(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f50rq_f50_capital_returns_quality_rosvol_63d_slope_v044_signal(ros):
    base = _std(ros, 63)
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f50rq_f50_capital_returns_quality_rosvol_252d_slope_v045_signal(ros):
    base = _std(ros, 63)
    d = base.diff(252) / float(252)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f50rq_f50_capital_returns_quality_retmean_21d_slope_v046_signal(roic, roa, ros):
    base = _retmean(roic, roa, ros)
    d = base.diff(21) / float(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f50rq_f50_capital_returns_quality_retmean_63d_slope_v047_signal(roic, roa, ros):
    base = _retmean(roic, roa, ros)
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f50rq_f50_capital_returns_quality_retmean_252d_slope_v048_signal(roic, roa, ros):
    base = _retmean(roic, roa, ros)
    d = base.diff(252) / float(252)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f50rq_f50_capital_returns_quality_retcv_42d_slope_v049_signal(roic, roa, ros):
    base = _retdisp(roic, roa, ros) / _retmean(roic, roa, ros).abs().replace(0, np.nan)
    d = base.diff(42) / float(42)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f50rq_f50_capital_returns_quality_retcv_126d_slope_v050_signal(roic, roa, ros):
    base = _retdisp(roic, roa, ros) / _retmean(roic, roa, ros).abs().replace(0, np.nan)
    d = base.diff(126) / float(126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f50rq_f50_capital_returns_quality_retcv_252d_slope_v051_signal(roic, roa, ros):
    base = _retdisp(roic, roa, ros) / _retmean(roic, roa, ros).abs().replace(0, np.nan)
    d = base.diff(252) / float(252)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f50rq_f50_capital_returns_quality_retmeanz_21d_slope_v052_signal(roic, roa, ros):
    base = _z(_retmean(roic, roa, ros), 252)
    d = base.diff(21) / float(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f50rq_f50_capital_returns_quality_retmeanz_63d_slope_v053_signal(roic, roa, ros):
    base = _z(_retmean(roic, roa, ros), 252)
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f50rq_f50_capital_returns_quality_retmeanz_126d_slope_v054_signal(roic, roa, ros):
    base = _z(_retmean(roic, roa, ros), 252)
    d = base.diff(126) / float(126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f50rq_f50_capital_returns_quality_retdisppct_21d_slope_v055_signal(roic, roa, ros):
    base = _pctrank(_retdisp(roic, roa, ros), 504)
    d = base.diff(21) / float(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f50rq_f50_capital_returns_quality_retdisppct_63d_slope_v056_signal(roic, roa, ros):
    base = _pctrank(_retdisp(roic, roa, ros), 504)
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f50rq_f50_capital_returns_quality_retdisppct_126d_slope_v057_signal(roic, roa, ros):
    base = _pctrank(_retdisp(roic, roa, ros), 504)
    d = base.diff(126) / float(126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f50rq_f50_capital_returns_quality_roicroaspr_21d_slope_v058_signal(roic, roa):
    base = roic - roa
    d = base.diff(21) / float(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f50rq_f50_capital_returns_quality_roicroaspr_63d_slope_v059_signal(roic, roa):
    base = roic - roa
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f50rq_f50_capital_returns_quality_roicroaspr_252d_slope_v060_signal(roic, roa):
    base = roic - roa
    d = base.diff(252) / float(252)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f50rq_f50_capital_returns_quality_roicrosspr_42d_slope_v061_signal(roic, ros):
    base = roic - ros
    d = base.diff(42) / float(42)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f50rq_f50_capital_returns_quality_roicrosspr_126d_slope_v062_signal(roic, ros):
    base = roic - ros
    d = base.diff(126) / float(126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f50rq_f50_capital_returns_quality_roicrosspr_252d_slope_v063_signal(roic, ros):
    base = roic - ros
    d = base.diff(252) / float(252)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f50rq_f50_capital_returns_quality_roarosspr_21d_slope_v064_signal(roa, ros):
    base = roa - ros
    d = base.diff(21) / float(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f50rq_f50_capital_returns_quality_roarosspr_63d_slope_v065_signal(roa, ros):
    base = roa - ros
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f50rq_f50_capital_returns_quality_roarosspr_126d_slope_v066_signal(roa, ros):
    base = roa - ros
    d = base.diff(126) / float(126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f50rq_f50_capital_returns_quality_assetturn_21d_slope_v067_signal(revenue, assets):
    base = _assetturn(revenue, assets)
    d = base.diff(21) / float(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f50rq_f50_capital_returns_quality_assetturn_63d_slope_v068_signal(revenue, assets):
    base = _assetturn(revenue, assets)
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f50rq_f50_capital_returns_quality_assetturn_252d_slope_v069_signal(revenue, assets):
    base = _assetturn(revenue, assets)
    d = base.diff(252) / float(252)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f50rq_f50_capital_returns_quality_assetturnz_42d_slope_v070_signal(revenue, assets):
    base = _z(_assetturn(revenue, assets), 252)
    d = base.diff(42) / float(42)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f50rq_f50_capital_returns_quality_assetturnz_126d_slope_v071_signal(revenue, assets):
    base = _z(_assetturn(revenue, assets), 252)
    d = base.diff(126) / float(126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f50rq_f50_capital_returns_quality_assetturnz_252d_slope_v072_signal(revenue, assets):
    base = _z(_assetturn(revenue, assets), 252)
    d = base.diff(252) / float(252)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f50rq_f50_capital_returns_quality_assetturnpct_21d_slope_v073_signal(revenue, assets):
    base = _pctrank(_assetturn(revenue, assets), 504)
    d = base.diff(21) / float(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f50rq_f50_capital_returns_quality_assetturnpct_63d_slope_v074_signal(revenue, assets):
    base = _pctrank(_assetturn(revenue, assets), 504)
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f50rq_f50_capital_returns_quality_assetturnpct_126d_slope_v075_signal(revenue, assets):
    base = _pctrank(_assetturn(revenue, assets), 504)
    d = base.diff(126) / float(126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f50rq_f50_capital_returns_quality_atcol_21d_slope_v076_signal(assetturnover):
    base = assetturnover
    d = base.diff(21) / float(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f50rq_f50_capital_returns_quality_atcol_63d_slope_v077_signal(assetturnover):
    base = assetturnover
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f50rq_f50_capital_returns_quality_atcol_252d_slope_v078_signal(assetturnover):
    base = assetturnover
    d = base.diff(252) / float(252)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f50rq_f50_capital_returns_quality_atcolz_42d_slope_v079_signal(assetturnover):
    base = _z(assetturnover, 252)
    d = base.diff(42) / float(42)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f50rq_f50_capital_returns_quality_atcolz_126d_slope_v080_signal(assetturnover):
    base = _z(assetturnover, 252)
    d = base.diff(126) / float(126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f50rq_f50_capital_returns_quality_atcolz_252d_slope_v081_signal(assetturnover):
    base = _z(assetturnover, 252)
    d = base.diff(252) / float(252)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f50rq_f50_capital_returns_quality_atcolpct_21d_slope_v082_signal(assetturnover):
    base = _pctrank(assetturnover, 504)
    d = base.diff(21) / float(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f50rq_f50_capital_returns_quality_atcolpct_63d_slope_v083_signal(assetturnover):
    base = _pctrank(assetturnover, 504)
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f50rq_f50_capital_returns_quality_atcolpct_126d_slope_v084_signal(assetturnover):
    base = _pctrank(assetturnover, 504)
    d = base.diff(126) / float(126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f50rq_f50_capital_returns_quality_eqturn_21d_slope_v085_signal(revenue, equity):
    base = _equityturn(revenue, equity)
    d = base.diff(21) / float(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f50rq_f50_capital_returns_quality_eqturn_63d_slope_v086_signal(revenue, equity):
    base = _equityturn(revenue, equity)
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f50rq_f50_capital_returns_quality_eqturn_252d_slope_v087_signal(revenue, equity):
    base = _equityturn(revenue, equity)
    d = base.diff(252) / float(252)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f50rq_f50_capital_returns_quality_eqturnz_42d_slope_v088_signal(revenue, equity):
    base = _z(_equityturn(revenue, equity), 252)
    d = base.diff(42) / float(42)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f50rq_f50_capital_returns_quality_eqturnz_126d_slope_v089_signal(revenue, equity):
    base = _z(_equityturn(revenue, equity), 252)
    d = base.diff(126) / float(126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f50rq_f50_capital_returns_quality_eqturnz_252d_slope_v090_signal(revenue, equity):
    base = _z(_equityturn(revenue, equity), 252)
    d = base.diff(252) / float(252)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f50rq_f50_capital_returns_quality_invcapturn_21d_slope_v091_signal(revenue, invcap):
    base = _invcapturn(revenue, invcap)
    d = base.diff(21) / float(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f50rq_f50_capital_returns_quality_invcapturn_63d_slope_v092_signal(revenue, invcap):
    base = _invcapturn(revenue, invcap)
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f50rq_f50_capital_returns_quality_invcapturn_252d_slope_v093_signal(revenue, invcap):
    base = _invcapturn(revenue, invcap)
    d = base.diff(252) / float(252)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f50rq_f50_capital_returns_quality_invcapturnz_42d_slope_v094_signal(revenue, invcap):
    base = _z(_invcapturn(revenue, invcap), 252)
    d = base.diff(42) / float(42)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f50rq_f50_capital_returns_quality_invcapturnz_126d_slope_v095_signal(revenue, invcap):
    base = _z(_invcapturn(revenue, invcap), 252)
    d = base.diff(126) / float(126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f50rq_f50_capital_returns_quality_invcapturnz_252d_slope_v096_signal(revenue, invcap):
    base = _z(_invcapturn(revenue, invcap), 252)
    d = base.diff(252) / float(252)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f50rq_f50_capital_returns_quality_dupontturn_21d_slope_v097_signal(ros, assetturnover):
    base = ros * (assetturnover - _mean(assetturnover, 252))
    d = base.diff(21) / float(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f50rq_f50_capital_returns_quality_dupontturn_63d_slope_v098_signal(ros, assetturnover):
    base = ros * (assetturnover - _mean(assetturnover, 252))
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f50rq_f50_capital_returns_quality_dupontturn_252d_slope_v099_signal(ros, assetturnover):
    base = ros * (assetturnover - _mean(assetturnover, 252))
    d = base.diff(252) / float(252)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f50rq_f50_capital_returns_quality_dupontz_42d_slope_v100_signal(ros, assetturnover):
    base = _z(ros * assetturnover, 252)
    d = base.diff(42) / float(42)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f50rq_f50_capital_returns_quality_dupontz_126d_slope_v101_signal(ros, assetturnover):
    base = _z(ros * assetturnover, 252)
    d = base.diff(126) / float(126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f50rq_f50_capital_returns_quality_dupontz_189d_slope_v102_signal(ros, assetturnover):
    base = _z(ros * assetturnover, 252)
    d = base.diff(189) / float(189)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f50rq_f50_capital_returns_quality_tangroicpct_21d_slope_v103_signal(ebit, tangibles):
    base = _pctrank(_tangroic(ebit, tangibles), 504)
    d = base.diff(21) / float(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f50rq_f50_capital_returns_quality_tangroicpct_63d_slope_v104_signal(ebit, tangibles):
    base = _pctrank(_tangroic(ebit, tangibles), 504)
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f50rq_f50_capital_returns_quality_tangroicpct_126d_slope_v105_signal(ebit, tangibles):
    base = _pctrank(_tangroic(ebit, tangibles), 504)
    d = base.diff(126) / float(126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f50rq_f50_capital_returns_quality_tangvsasset_21d_slope_v106_signal(ebit, tangibles, assets):
    base = ebit / tangibles.replace(0, np.nan) - ebit / assets.replace(0, np.nan)
    d = base.diff(21) / float(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f50rq_f50_capital_returns_quality_tangvsasset_63d_slope_v107_signal(ebit, tangibles, assets):
    base = ebit / tangibles.replace(0, np.nan) - ebit / assets.replace(0, np.nan)
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f50rq_f50_capital_returns_quality_tangvsasset_252d_slope_v108_signal(ebit, tangibles, assets):
    base = ebit / tangibles.replace(0, np.nan) - ebit / assets.replace(0, np.nan)
    d = base.diff(252) / float(252)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f50rq_f50_capital_returns_quality_ebitmargin_21d_slope_v109_signal(ebit, revenue):
    base = ebit / revenue.replace(0, np.nan)
    d = base.diff(21) / float(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f50rq_f50_capital_returns_quality_ebitmargin_63d_slope_v110_signal(ebit, revenue):
    base = ebit / revenue.replace(0, np.nan)
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f50rq_f50_capital_returns_quality_ebitmargin_252d_slope_v111_signal(ebit, revenue):
    base = ebit / revenue.replace(0, np.nan)
    d = base.diff(252) / float(252)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f50rq_f50_capital_returns_quality_ebitmarginz_42d_slope_v112_signal(ebit, revenue):
    base = _z(ebit / revenue.replace(0, np.nan), 252)
    d = base.diff(42) / float(42)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f50rq_f50_capital_returns_quality_ebitmarginz_126d_slope_v113_signal(ebit, revenue):
    base = _z(ebit / revenue.replace(0, np.nan), 252)
    d = base.diff(126) / float(126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f50rq_f50_capital_returns_quality_ebitmarginz_252d_slope_v114_signal(ebit, revenue):
    base = _z(ebit / revenue.replace(0, np.nan), 252)
    d = base.diff(252) / float(252)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f50rq_f50_capital_returns_quality_ebitmarginpct_21d_slope_v115_signal(ebit, revenue):
    base = _pctrank(ebit / revenue.replace(0, np.nan), 504)
    d = base.diff(21) / float(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f50rq_f50_capital_returns_quality_ebitmarginpct_63d_slope_v116_signal(ebit, revenue):
    base = _pctrank(ebit / revenue.replace(0, np.nan), 504)
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f50rq_f50_capital_returns_quality_ebitmarginpct_126d_slope_v117_signal(ebit, revenue):
    base = _pctrank(ebit / revenue.replace(0, np.nan), 504)
    d = base.diff(126) / float(126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f50rq_f50_capital_returns_quality_ebitoneqspr_42d_slope_v118_signal(ebit, equity, invcap):
    base = ebit / equity.replace(0, np.nan) - ebit / invcap.replace(0, np.nan)
    d = base.diff(42) / float(42)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f50rq_f50_capital_returns_quality_ebitoneqspr_126d_slope_v119_signal(ebit, equity, invcap):
    base = ebit / equity.replace(0, np.nan) - ebit / invcap.replace(0, np.nan)
    d = base.diff(126) / float(126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f50rq_f50_capital_returns_quality_ebitoneqspr_252d_slope_v120_signal(ebit, equity, invcap):
    base = ebit / equity.replace(0, np.nan) - ebit / invcap.replace(0, np.nan)
    d = base.diff(252) / float(252)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f50rq_f50_capital_returns_quality_opvsrep_21d_slope_v121_signal(ebit, invcap, roic):
    base = ebit / invcap.replace(0, np.nan) - roic
    d = base.diff(21) / float(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f50rq_f50_capital_returns_quality_opvsrep_63d_slope_v122_signal(ebit, invcap, roic):
    base = ebit / invcap.replace(0, np.nan) - roic
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f50rq_f50_capital_returns_quality_opvsrep_126d_slope_v123_signal(ebit, invcap, roic):
    base = ebit / invcap.replace(0, np.nan) - roic
    d = base.diff(126) / float(126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f50rq_f50_capital_returns_quality_intangshare_21d_slope_v124_signal(intangibles, assets):
    base = _intangshare(intangibles, assets)
    d = base.diff(21) / float(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f50rq_f50_capital_returns_quality_intangshare_63d_slope_v125_signal(intangibles, assets):
    base = _intangshare(intangibles, assets)
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f50rq_f50_capital_returns_quality_intangshare_252d_slope_v126_signal(intangibles, assets):
    base = _intangshare(intangibles, assets)
    d = base.diff(252) / float(252)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f50rq_f50_capital_returns_quality_intangsharez_42d_slope_v127_signal(intangibles, assets):
    base = _z(_intangshare(intangibles, assets), 252)
    d = base.diff(42) / float(42)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f50rq_f50_capital_returns_quality_intangsharez_126d_slope_v128_signal(intangibles, assets):
    base = _z(_intangshare(intangibles, assets), 252)
    d = base.diff(126) / float(126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f50rq_f50_capital_returns_quality_intangsharez_252d_slope_v129_signal(intangibles, assets):
    base = _z(_intangshare(intangibles, assets), 252)
    d = base.diff(252) / float(252)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f50rq_f50_capital_returns_quality_tangshare_21d_slope_v130_signal(tangibles, assets):
    base = _tangshare(tangibles, assets)
    d = base.diff(21) / float(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f50rq_f50_capital_returns_quality_tangshare_63d_slope_v131_signal(tangibles, assets):
    base = _tangshare(tangibles, assets)
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f50rq_f50_capital_returns_quality_tangshare_252d_slope_v132_signal(tangibles, assets):
    base = _tangshare(tangibles, assets)
    d = base.diff(252) / float(252)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f50rq_f50_capital_returns_quality_intangeq_21d_slope_v133_signal(intangibles, equity):
    base = intangibles / equity.replace(0, np.nan)
    d = base.diff(21) / float(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f50rq_f50_capital_returns_quality_intangeq_63d_slope_v134_signal(intangibles, equity):
    base = intangibles / equity.replace(0, np.nan)
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f50rq_f50_capital_returns_quality_intangeq_252d_slope_v135_signal(intangibles, equity):
    base = intangibles / equity.replace(0, np.nan)
    d = base.diff(252) / float(252)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f50rq_f50_capital_returns_quality_compscore_21d_slope_v136_signal(roic, assetturnover):
    base = _z(roic * assetturnover, 252)
    d = base.diff(21) / float(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f50rq_f50_capital_returns_quality_compscore_63d_slope_v137_signal(roic, assetturnover):
    base = _z(roic * assetturnover, 252)
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f50rq_f50_capital_returns_quality_compscore_126d_slope_v138_signal(roic, assetturnover):
    base = _z(roic * assetturnover, 252)
    d = base.diff(126) / float(126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f50rq_f50_capital_returns_quality_earnchurn_42d_slope_v139_signal(roa, assetturnover):
    base = (roa * assetturnover).ewm(span=63, min_periods=21).mean()
    d = base.diff(42) / float(42)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f50rq_f50_capital_returns_quality_earnchurn_126d_slope_v140_signal(roa, assetturnover):
    base = (roa * assetturnover).ewm(span=63, min_periods=21).mean()
    d = base.diff(126) / float(126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f50rq_f50_capital_returns_quality_earnchurn_252d_slope_v141_signal(roa, assetturnover):
    base = (roa * assetturnover).ewm(span=63, min_periods=21).mean()
    d = base.diff(252) / float(252)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f50rq_f50_capital_returns_quality_tangturn_21d_slope_v142_signal(revenue, tangibles):
    base = revenue / tangibles.replace(0, np.nan)
    d = base.diff(21) / float(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f50rq_f50_capital_returns_quality_tangturn_63d_slope_v143_signal(revenue, tangibles):
    base = revenue / tangibles.replace(0, np.nan)
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f50rq_f50_capital_returns_quality_tangturn_252d_slope_v144_signal(revenue, tangibles):
    base = revenue / tangibles.replace(0, np.nan)
    d = base.diff(252) / float(252)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f50rq_f50_capital_returns_quality_roavsasgrow_21d_slope_v145_signal(roa, assets):
    base = roa - (assets / assets.shift(252).replace(0, np.nan) - 1.0)
    d = base.diff(21) / float(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f50rq_f50_capital_returns_quality_roavsasgrow_63d_slope_v146_signal(roa, assets):
    base = roa - (assets / assets.shift(252).replace(0, np.nan) - 1.0)
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f50rq_f50_capital_returns_quality_roavsasgrow_126d_slope_v147_signal(roa, assets):
    base = roa - (assets / assets.shift(252).replace(0, np.nan) - 1.0)
    d = base.diff(126) / float(126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f50rq_f50_capital_returns_quality_qualcomp_21d_slope_v148_signal(roic, ebit, revenue, assets):
    base = (_z(roic - HURDLE, 252) + _z(ebit / revenue.replace(0, np.nan), 252) + _z(_assetturn(revenue, assets), 252)) / 3.0
    d = base.diff(21) / float(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f50rq_f50_capital_returns_quality_qualcomp_63d_slope_v149_signal(roic, ebit, revenue, assets):
    base = (_z(roic - HURDLE, 252) + _z(ebit / revenue.replace(0, np.nan), 252) + _z(_assetturn(revenue, assets), 252)) / 3.0
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f50rq_f50_capital_returns_quality_qualcomp_126d_slope_v150_signal(roic, ebit, revenue, assets):
    base = (_z(roic - HURDLE, 252) + _z(ebit / revenue.replace(0, np.nan), 252) + _z(_assetturn(revenue, assets), 252)) / 3.0
    d = base.diff(126) / float(126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

_FEATURES = [
    f50rq_f50_capital_returns_quality_roiclvl_21d_slope_v001_signal,
    f50rq_f50_capital_returns_quality_roiclvl_63d_slope_v002_signal,
    f50rq_f50_capital_returns_quality_roiclvl_252d_slope_v003_signal,
    f50rq_f50_capital_returns_quality_roicz_42d_slope_v004_signal,
    f50rq_f50_capital_returns_quality_roicz_126d_slope_v005_signal,
    f50rq_f50_capital_returns_quality_roicz_252d_slope_v006_signal,
    f50rq_f50_capital_returns_quality_roicpct_21d_slope_v007_signal,
    f50rq_f50_capital_returns_quality_roicpct_63d_slope_v008_signal,
    f50rq_f50_capital_returns_quality_roicpct_126d_slope_v009_signal,
    f50rq_f50_capital_returns_quality_roicvol_21d_slope_v010_signal,
    f50rq_f50_capital_returns_quality_roicvol_63d_slope_v011_signal,
    f50rq_f50_capital_returns_quality_roicvol_126d_slope_v012_signal,
    f50rq_f50_capital_returns_quality_roicconv_21d_slope_v013_signal,
    f50rq_f50_capital_returns_quality_roicconv_63d_slope_v014_signal,
    f50rq_f50_capital_returns_quality_roicconv_252d_slope_v015_signal,
    f50rq_f50_capital_returns_quality_roicconsist_42d_slope_v016_signal,
    f50rq_f50_capital_returns_quality_roicconsist_126d_slope_v017_signal,
    f50rq_f50_capital_returns_quality_roicconsist_252d_slope_v018_signal,
    f50rq_f50_capital_returns_quality_roalvl_21d_slope_v019_signal,
    f50rq_f50_capital_returns_quality_roalvl_63d_slope_v020_signal,
    f50rq_f50_capital_returns_quality_roalvl_252d_slope_v021_signal,
    f50rq_f50_capital_returns_quality_roaz_42d_slope_v022_signal,
    f50rq_f50_capital_returns_quality_roaz_126d_slope_v023_signal,
    f50rq_f50_capital_returns_quality_roaz_252d_slope_v024_signal,
    f50rq_f50_capital_returns_quality_roapct_21d_slope_v025_signal,
    f50rq_f50_capital_returns_quality_roapct_63d_slope_v026_signal,
    f50rq_f50_capital_returns_quality_roapct_126d_slope_v027_signal,
    f50rq_f50_capital_returns_quality_roavol_21d_slope_v028_signal,
    f50rq_f50_capital_returns_quality_roavol_63d_slope_v029_signal,
    f50rq_f50_capital_returns_quality_roavol_252d_slope_v030_signal,
    f50rq_f50_capital_returns_quality_roaconv_42d_slope_v031_signal,
    f50rq_f50_capital_returns_quality_roaconv_126d_slope_v032_signal,
    f50rq_f50_capital_returns_quality_roaconv_252d_slope_v033_signal,
    f50rq_f50_capital_returns_quality_roslvl_21d_slope_v034_signal,
    f50rq_f50_capital_returns_quality_roslvl_63d_slope_v035_signal,
    f50rq_f50_capital_returns_quality_roslvl_252d_slope_v036_signal,
    f50rq_f50_capital_returns_quality_rosz_42d_slope_v037_signal,
    f50rq_f50_capital_returns_quality_rosz_126d_slope_v038_signal,
    f50rq_f50_capital_returns_quality_rosz_252d_slope_v039_signal,
    f50rq_f50_capital_returns_quality_rospct_21d_slope_v040_signal,
    f50rq_f50_capital_returns_quality_rospct_63d_slope_v041_signal,
    f50rq_f50_capital_returns_quality_rospct_126d_slope_v042_signal,
    f50rq_f50_capital_returns_quality_rosvol_21d_slope_v043_signal,
    f50rq_f50_capital_returns_quality_rosvol_63d_slope_v044_signal,
    f50rq_f50_capital_returns_quality_rosvol_252d_slope_v045_signal,
    f50rq_f50_capital_returns_quality_retmean_21d_slope_v046_signal,
    f50rq_f50_capital_returns_quality_retmean_63d_slope_v047_signal,
    f50rq_f50_capital_returns_quality_retmean_252d_slope_v048_signal,
    f50rq_f50_capital_returns_quality_retcv_42d_slope_v049_signal,
    f50rq_f50_capital_returns_quality_retcv_126d_slope_v050_signal,
    f50rq_f50_capital_returns_quality_retcv_252d_slope_v051_signal,
    f50rq_f50_capital_returns_quality_retmeanz_21d_slope_v052_signal,
    f50rq_f50_capital_returns_quality_retmeanz_63d_slope_v053_signal,
    f50rq_f50_capital_returns_quality_retmeanz_126d_slope_v054_signal,
    f50rq_f50_capital_returns_quality_retdisppct_21d_slope_v055_signal,
    f50rq_f50_capital_returns_quality_retdisppct_63d_slope_v056_signal,
    f50rq_f50_capital_returns_quality_retdisppct_126d_slope_v057_signal,
    f50rq_f50_capital_returns_quality_roicroaspr_21d_slope_v058_signal,
    f50rq_f50_capital_returns_quality_roicroaspr_63d_slope_v059_signal,
    f50rq_f50_capital_returns_quality_roicroaspr_252d_slope_v060_signal,
    f50rq_f50_capital_returns_quality_roicrosspr_42d_slope_v061_signal,
    f50rq_f50_capital_returns_quality_roicrosspr_126d_slope_v062_signal,
    f50rq_f50_capital_returns_quality_roicrosspr_252d_slope_v063_signal,
    f50rq_f50_capital_returns_quality_roarosspr_21d_slope_v064_signal,
    f50rq_f50_capital_returns_quality_roarosspr_63d_slope_v065_signal,
    f50rq_f50_capital_returns_quality_roarosspr_126d_slope_v066_signal,
    f50rq_f50_capital_returns_quality_assetturn_21d_slope_v067_signal,
    f50rq_f50_capital_returns_quality_assetturn_63d_slope_v068_signal,
    f50rq_f50_capital_returns_quality_assetturn_252d_slope_v069_signal,
    f50rq_f50_capital_returns_quality_assetturnz_42d_slope_v070_signal,
    f50rq_f50_capital_returns_quality_assetturnz_126d_slope_v071_signal,
    f50rq_f50_capital_returns_quality_assetturnz_252d_slope_v072_signal,
    f50rq_f50_capital_returns_quality_assetturnpct_21d_slope_v073_signal,
    f50rq_f50_capital_returns_quality_assetturnpct_63d_slope_v074_signal,
    f50rq_f50_capital_returns_quality_assetturnpct_126d_slope_v075_signal,
    f50rq_f50_capital_returns_quality_atcol_21d_slope_v076_signal,
    f50rq_f50_capital_returns_quality_atcol_63d_slope_v077_signal,
    f50rq_f50_capital_returns_quality_atcol_252d_slope_v078_signal,
    f50rq_f50_capital_returns_quality_atcolz_42d_slope_v079_signal,
    f50rq_f50_capital_returns_quality_atcolz_126d_slope_v080_signal,
    f50rq_f50_capital_returns_quality_atcolz_252d_slope_v081_signal,
    f50rq_f50_capital_returns_quality_atcolpct_21d_slope_v082_signal,
    f50rq_f50_capital_returns_quality_atcolpct_63d_slope_v083_signal,
    f50rq_f50_capital_returns_quality_atcolpct_126d_slope_v084_signal,
    f50rq_f50_capital_returns_quality_eqturn_21d_slope_v085_signal,
    f50rq_f50_capital_returns_quality_eqturn_63d_slope_v086_signal,
    f50rq_f50_capital_returns_quality_eqturn_252d_slope_v087_signal,
    f50rq_f50_capital_returns_quality_eqturnz_42d_slope_v088_signal,
    f50rq_f50_capital_returns_quality_eqturnz_126d_slope_v089_signal,
    f50rq_f50_capital_returns_quality_eqturnz_252d_slope_v090_signal,
    f50rq_f50_capital_returns_quality_invcapturn_21d_slope_v091_signal,
    f50rq_f50_capital_returns_quality_invcapturn_63d_slope_v092_signal,
    f50rq_f50_capital_returns_quality_invcapturn_252d_slope_v093_signal,
    f50rq_f50_capital_returns_quality_invcapturnz_42d_slope_v094_signal,
    f50rq_f50_capital_returns_quality_invcapturnz_126d_slope_v095_signal,
    f50rq_f50_capital_returns_quality_invcapturnz_252d_slope_v096_signal,
    f50rq_f50_capital_returns_quality_dupontturn_21d_slope_v097_signal,
    f50rq_f50_capital_returns_quality_dupontturn_63d_slope_v098_signal,
    f50rq_f50_capital_returns_quality_dupontturn_252d_slope_v099_signal,
    f50rq_f50_capital_returns_quality_dupontz_42d_slope_v100_signal,
    f50rq_f50_capital_returns_quality_dupontz_126d_slope_v101_signal,
    f50rq_f50_capital_returns_quality_dupontz_189d_slope_v102_signal,
    f50rq_f50_capital_returns_quality_tangroicpct_21d_slope_v103_signal,
    f50rq_f50_capital_returns_quality_tangroicpct_63d_slope_v104_signal,
    f50rq_f50_capital_returns_quality_tangroicpct_126d_slope_v105_signal,
    f50rq_f50_capital_returns_quality_tangvsasset_21d_slope_v106_signal,
    f50rq_f50_capital_returns_quality_tangvsasset_63d_slope_v107_signal,
    f50rq_f50_capital_returns_quality_tangvsasset_252d_slope_v108_signal,
    f50rq_f50_capital_returns_quality_ebitmargin_21d_slope_v109_signal,
    f50rq_f50_capital_returns_quality_ebitmargin_63d_slope_v110_signal,
    f50rq_f50_capital_returns_quality_ebitmargin_252d_slope_v111_signal,
    f50rq_f50_capital_returns_quality_ebitmarginz_42d_slope_v112_signal,
    f50rq_f50_capital_returns_quality_ebitmarginz_126d_slope_v113_signal,
    f50rq_f50_capital_returns_quality_ebitmarginz_252d_slope_v114_signal,
    f50rq_f50_capital_returns_quality_ebitmarginpct_21d_slope_v115_signal,
    f50rq_f50_capital_returns_quality_ebitmarginpct_63d_slope_v116_signal,
    f50rq_f50_capital_returns_quality_ebitmarginpct_126d_slope_v117_signal,
    f50rq_f50_capital_returns_quality_ebitoneqspr_42d_slope_v118_signal,
    f50rq_f50_capital_returns_quality_ebitoneqspr_126d_slope_v119_signal,
    f50rq_f50_capital_returns_quality_ebitoneqspr_252d_slope_v120_signal,
    f50rq_f50_capital_returns_quality_opvsrep_21d_slope_v121_signal,
    f50rq_f50_capital_returns_quality_opvsrep_63d_slope_v122_signal,
    f50rq_f50_capital_returns_quality_opvsrep_126d_slope_v123_signal,
    f50rq_f50_capital_returns_quality_intangshare_21d_slope_v124_signal,
    f50rq_f50_capital_returns_quality_intangshare_63d_slope_v125_signal,
    f50rq_f50_capital_returns_quality_intangshare_252d_slope_v126_signal,
    f50rq_f50_capital_returns_quality_intangsharez_42d_slope_v127_signal,
    f50rq_f50_capital_returns_quality_intangsharez_126d_slope_v128_signal,
    f50rq_f50_capital_returns_quality_intangsharez_252d_slope_v129_signal,
    f50rq_f50_capital_returns_quality_tangshare_21d_slope_v130_signal,
    f50rq_f50_capital_returns_quality_tangshare_63d_slope_v131_signal,
    f50rq_f50_capital_returns_quality_tangshare_252d_slope_v132_signal,
    f50rq_f50_capital_returns_quality_intangeq_21d_slope_v133_signal,
    f50rq_f50_capital_returns_quality_intangeq_63d_slope_v134_signal,
    f50rq_f50_capital_returns_quality_intangeq_252d_slope_v135_signal,
    f50rq_f50_capital_returns_quality_compscore_21d_slope_v136_signal,
    f50rq_f50_capital_returns_quality_compscore_63d_slope_v137_signal,
    f50rq_f50_capital_returns_quality_compscore_126d_slope_v138_signal,
    f50rq_f50_capital_returns_quality_earnchurn_42d_slope_v139_signal,
    f50rq_f50_capital_returns_quality_earnchurn_126d_slope_v140_signal,
    f50rq_f50_capital_returns_quality_earnchurn_252d_slope_v141_signal,
    f50rq_f50_capital_returns_quality_tangturn_21d_slope_v142_signal,
    f50rq_f50_capital_returns_quality_tangturn_63d_slope_v143_signal,
    f50rq_f50_capital_returns_quality_tangturn_252d_slope_v144_signal,
    f50rq_f50_capital_returns_quality_roavsasgrow_21d_slope_v145_signal,
    f50rq_f50_capital_returns_quality_roavsasgrow_63d_slope_v146_signal,
    f50rq_f50_capital_returns_quality_roavsasgrow_126d_slope_v147_signal,
    f50rq_f50_capital_returns_quality_qualcomp_21d_slope_v148_signal,
    f50rq_f50_capital_returns_quality_qualcomp_63d_slope_v149_signal,
    f50rq_f50_capital_returns_quality_qualcomp_126d_slope_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F50_CAPITAL_RETURNS_QUALITY_REGISTRY_001_150 = REGISTRY

if __name__ == "__main__":
    np.random.seed(42)
    n = 1500

    def _fund(seed, base=1e8, drift=0.0, vol=0.08, allow_neg=False):
        g = np.random.default_rng(seed)
        steps = np.repeat(g.normal(drift, vol, n // 63 + 1), 63)[:n]
        s = base * np.exp(np.cumsum(steps / 63))
        if allow_neg:
            s = s - base * 0.5
        return pd.Series(s, name=None)

    roic = _fund(1, base=0.12, drift=0.0, vol=0.10, allow_neg=True).rename("roic")
    roa = _fund(2, base=0.08, drift=0.0, vol=0.09, allow_neg=True).rename("roa")
    ros = _fund(3, base=0.10, drift=0.0, vol=0.11, allow_neg=True).rename("ros")
    ebit = _fund(4, base=5e7, drift=0.0, vol=0.12, allow_neg=True).rename("ebit")
    assetturnover = (_fund(5, base=0.7, drift=0.0, vol=0.07) + 0.1).rename("assetturnover")
    invcap = _fund(6, base=8e8, drift=0.01, vol=0.05).rename("invcap")
    equity = _fund(7, base=6e8, drift=0.01, vol=0.05).rename("equity")
    intangibles = _fund(8, base=2e8, drift=0.0, vol=0.06).rename("intangibles")
    tangibles = _fund(9, base=7e8, drift=0.005, vol=0.05).rename("tangibles")
    revenue = _fund(10, base=9e8, drift=0.01, vol=0.06).rename("revenue")
    assets = _fund(11, base=1.2e9, drift=0.01, vol=0.05).rename("assets")

    cols = {"roic": roic, "roa": roa, "ros": ros, "ebit": ebit,
            "assetturnover": assetturnover, "invcap": invcap, "equity": equity,
            "intangibles": intangibles, "tangibles": tangibles,
            "revenue": revenue, "assets": assets}

    n_features = 0
    nan_ok = 0
    results = {}
    for name, meta in REGISTRY.items():
        fn = meta["func"]
        args = [cols[c] for c in meta["inputs"]]
        y1 = fn(*args)
        y2 = fn(*args)
        pd.testing.assert_series_equal(y1, y2)
        q = y1.iloc[504:].dropna()
        assert len(q) > 0, name
        assert q.nunique() > 20, "%s nunique=%d" % (name, q.nunique())
        assert q.std() > 0, name
        assert not q.isna().all(), name
        nan_ratio = y1.iloc[504:].isna().mean()
        if nan_ratio < 0.5:
            nan_ok += 1
        results[name] = y1.iloc[504:]
        n_features += 1

    assert n_features == 150, n_features
    assert nan_ok >= int(0.8 * n_features), "nan_ok=%d/%d" % (nan_ok, n_features)

    items = list(results.items())
    for i in range(len(items)):
        ni, si = items[i]
        ai = si.dropna()
        for j in range(i + 1, len(items)):
            nj, sj = items[j]
            aj = sj.dropna()
            idx = ai.index.intersection(aj.index)
            if len(idx) < 30:
                continue
            c = ai.loc[idx].corr(aj.loc[idx])
            if c is None or np.isnan(c):
                continue
            assert abs(c) <= 0.97, "CORR %s vs %s = %.4f" % (ni, nj, c)

    print("OK f50_capital_returns_quality_2nd_derivatives_001_150_claude: %d features pass" % n_features)
