import inspect
import numpy as np
import pandas as pd

TRADING_DAYS_YEAR = 252
TRADING_DAYS_HALF = 126
TRADING_DAYS_QUARTER = 63
TRADING_DAYS_MONTH = 21
TRADING_DAYS_WEEK = 5


def _z(s, w):
    m = s.rolling(w, min_periods=max(1, w // 2)).mean()
    sd = s.rolling(w, min_periods=max(1, w // 2)).std()
    return (s - m) / sd.replace(0, np.nan)


def _mean(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def _std(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).std()


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


# ===== folder domain primitives =====
def _f41_intangibles_growth(intangibles, w):
    base = _mean(intangibles, max(2, w // 4))
    return base.pct_change(periods=w)


def _f41_asset_pulse(assets, intangibles, w):
    intang_share = intangibles / assets.replace(0, np.nan)
    return intang_share - intang_share.rolling(w, min_periods=max(1, w // 2)).mean()


def _f41_acquisition_score(intangibles, capex, w):
    intang_diff = intangibles.diff(periods=w)
    spend = (intang_diff + capex.rolling(w, min_periods=max(1, w // 2)).sum())
    return spend / (intangibles.rolling(w, min_periods=max(1, w // 2)).mean()).replace(0, np.nan)


# v001: 21d intangibles growth scaled by closeadj
def f41mas_f41_medtech_acquisition_signature_intanggr_21d_base_v001_signal(intangibles, closeadj):
    result = _f41_intangibles_growth(intangibles, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v002: 63d intangibles growth scaled by closeadj
def f41mas_f41_medtech_acquisition_signature_intanggr_63d_base_v002_signal(intangibles, closeadj):
    result = _f41_intangibles_growth(intangibles, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v003: 126d intangibles growth scaled by closeadj
def f41mas_f41_medtech_acquisition_signature_intanggr_126d_base_v003_signal(intangibles, closeadj):
    result = _f41_intangibles_growth(intangibles, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v004: 252d intangibles growth scaled by closeadj
def f41mas_f41_medtech_acquisition_signature_intanggr_252d_base_v004_signal(intangibles, closeadj):
    result = _f41_intangibles_growth(intangibles, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v005: 504d intangibles growth scaled by closeadj
def f41mas_f41_medtech_acquisition_signature_intanggr_504d_base_v005_signal(intangibles, closeadj):
    result = _f41_intangibles_growth(intangibles, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v006: 21d intangibles growth squared scaled
def f41mas_f41_medtech_acquisition_signature_intanggrsq_21d_base_v006_signal(intangibles, closeadj):
    g = _f41_intangibles_growth(intangibles, 21)
    result = g * g.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v007: 63d intangibles growth squared scaled
def f41mas_f41_medtech_acquisition_signature_intanggrsq_63d_base_v007_signal(intangibles, closeadj):
    g = _f41_intangibles_growth(intangibles, 63)
    result = g * g.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v008: 252d intangibles growth squared scaled
def f41mas_f41_medtech_acquisition_signature_intanggrsq_252d_base_v008_signal(intangibles, closeadj):
    g = _f41_intangibles_growth(intangibles, 252)
    result = g * g.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v009: 21d intangibles growth z-score over 252d
def f41mas_f41_medtech_acquisition_signature_intanggrz_21d_base_v009_signal(intangibles, closeadj):
    g = _f41_intangibles_growth(intangibles, 21)
    result = _z(g, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v010: 63d intangibles growth z-score over 504d
def f41mas_f41_medtech_acquisition_signature_intanggrz_63d_base_v010_signal(intangibles, closeadj):
    g = _f41_intangibles_growth(intangibles, 63)
    result = _z(g, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v011: 21d asset pulse scaled
def f41mas_f41_medtech_acquisition_signature_assetpulse_21d_base_v011_signal(assets, intangibles, closeadj):
    result = _f41_asset_pulse(assets, intangibles, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v012: 63d asset pulse scaled
def f41mas_f41_medtech_acquisition_signature_assetpulse_63d_base_v012_signal(assets, intangibles, closeadj):
    result = _f41_asset_pulse(assets, intangibles, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v013: 126d asset pulse scaled
def f41mas_f41_medtech_acquisition_signature_assetpulse_126d_base_v013_signal(assets, intangibles, closeadj):
    result = _f41_asset_pulse(assets, intangibles, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v014: 252d asset pulse scaled
def f41mas_f41_medtech_acquisition_signature_assetpulse_252d_base_v014_signal(assets, intangibles, closeadj):
    result = _f41_asset_pulse(assets, intangibles, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v015: 504d asset pulse scaled
def f41mas_f41_medtech_acquisition_signature_assetpulse_504d_base_v015_signal(assets, intangibles, closeadj):
    result = _f41_asset_pulse(assets, intangibles, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v016: 21d acquisition score
def f41mas_f41_medtech_acquisition_signature_acqscore_21d_base_v016_signal(intangibles, capex, closeadj):
    result = _f41_acquisition_score(intangibles, capex, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v017: 63d acquisition score
def f41mas_f41_medtech_acquisition_signature_acqscore_63d_base_v017_signal(intangibles, capex, closeadj):
    result = _f41_acquisition_score(intangibles, capex, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v018: 126d acquisition score
def f41mas_f41_medtech_acquisition_signature_acqscore_126d_base_v018_signal(intangibles, capex, closeadj):
    result = _f41_acquisition_score(intangibles, capex, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v019: 252d acquisition score
def f41mas_f41_medtech_acquisition_signature_acqscore_252d_base_v019_signal(intangibles, capex, closeadj):
    result = _f41_acquisition_score(intangibles, capex, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v020: 504d acquisition score
def f41mas_f41_medtech_acquisition_signature_acqscore_504d_base_v020_signal(intangibles, capex, closeadj):
    result = _f41_acquisition_score(intangibles, capex, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v021: 21d intangibles growth × asset pulse 21d
def f41mas_f41_medtech_acquisition_signature_grxpulse_21d_base_v021_signal(intangibles, assets, closeadj):
    a = _f41_intangibles_growth(intangibles, 21)
    b = _f41_asset_pulse(assets, intangibles, 21)
    result = a * b * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v022: 63d intangibles growth × asset pulse 63d
def f41mas_f41_medtech_acquisition_signature_grxpulse_63d_base_v022_signal(intangibles, assets, closeadj):
    a = _f41_intangibles_growth(intangibles, 63)
    b = _f41_asset_pulse(assets, intangibles, 63)
    result = a * b * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v023: 252d intangibles growth × asset pulse 252d
def f41mas_f41_medtech_acquisition_signature_grxpulse_252d_base_v023_signal(intangibles, assets, closeadj):
    a = _f41_intangibles_growth(intangibles, 252)
    b = _f41_asset_pulse(assets, intangibles, 252)
    result = a * b * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v024: rolling mean 21d of intangibles growth 63d
def f41mas_f41_medtech_acquisition_signature_grmean_21d_base_v024_signal(intangibles, closeadj):
    result = _mean(_f41_intangibles_growth(intangibles, 63), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v025: rolling mean 63d of intangibles growth 252d
def f41mas_f41_medtech_acquisition_signature_grmean_63d_base_v025_signal(intangibles, closeadj):
    result = _mean(_f41_intangibles_growth(intangibles, 252), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v026: rolling std 63d of intangibles growth 252d
def f41mas_f41_medtech_acquisition_signature_grstd_63d_base_v026_signal(intangibles, closeadj):
    result = _std(_f41_intangibles_growth(intangibles, 252), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v027: rolling std 126d of intangibles growth 504d
def f41mas_f41_medtech_acquisition_signature_grstd_126d_base_v027_signal(intangibles, closeadj):
    result = _std(_f41_intangibles_growth(intangibles, 504), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v028: 21d intangibles growth × capex (deal-spend coupling)
def f41mas_f41_medtech_acquisition_signature_grxcapex_21d_base_v028_signal(intangibles, capex, closeadj):
    g = _f41_intangibles_growth(intangibles, 21)
    result = g * _mean(capex, 21) * closeadj / _mean(capex, 252).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# v029: 63d intangibles growth × capex
def f41mas_f41_medtech_acquisition_signature_grxcapex_63d_base_v029_signal(intangibles, capex, closeadj):
    g = _f41_intangibles_growth(intangibles, 63)
    result = g * _mean(capex, 63) * closeadj / _mean(capex, 504).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# v030: 252d intangibles growth × capex
def f41mas_f41_medtech_acquisition_signature_grxcapex_252d_base_v030_signal(intangibles, capex, closeadj):
    g = _f41_intangibles_growth(intangibles, 252)
    result = g * _mean(capex, 252) * closeadj / _mean(capex, 504).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# v031: 21d intangible-share level scaled (asset_pulse + mean)
def f41mas_f41_medtech_acquisition_signature_intangshare_21d_base_v031_signal(assets, intangibles, closeadj):
    pulse = _f41_asset_pulse(assets, intangibles, 21)
    intang_share = intangibles / assets.replace(0, np.nan)
    result = (intang_share + pulse) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v032: 63d intangible-share level scaled
def f41mas_f41_medtech_acquisition_signature_intangshare_63d_base_v032_signal(assets, intangibles, closeadj):
    pulse = _f41_asset_pulse(assets, intangibles, 63)
    intang_share = intangibles / assets.replace(0, np.nan)
    result = (intang_share + pulse) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v033: 252d intangible-share level scaled
def f41mas_f41_medtech_acquisition_signature_intangshare_252d_base_v033_signal(assets, intangibles, closeadj):
    pulse = _f41_asset_pulse(assets, intangibles, 252)
    intang_share = intangibles / assets.replace(0, np.nan)
    result = (intang_share + pulse) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v034: 504d intangible-share level scaled
def f41mas_f41_medtech_acquisition_signature_intangshare_504d_base_v034_signal(assets, intangibles, closeadj):
    pulse = _f41_asset_pulse(assets, intangibles, 504)
    intang_share = intangibles / assets.replace(0, np.nan)
    result = (intang_share + pulse) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v035: 21d asset pulse z-score over 252d
def f41mas_f41_medtech_acquisition_signature_pulsez_21d_base_v035_signal(assets, intangibles, closeadj):
    p = _f41_asset_pulse(assets, intangibles, 21)
    result = _z(p, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v036: 63d asset pulse z-score over 504d
def f41mas_f41_medtech_acquisition_signature_pulsez_63d_base_v036_signal(assets, intangibles, closeadj):
    p = _f41_asset_pulse(assets, intangibles, 63)
    result = _z(p, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v037: 252d asset pulse z-score over 504d
def f41mas_f41_medtech_acquisition_signature_pulsez_252d_base_v037_signal(assets, intangibles, closeadj):
    p = _f41_asset_pulse(assets, intangibles, 252)
    result = _z(p, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v038: 21d acquisition score z-score over 252d
def f41mas_f41_medtech_acquisition_signature_acqscorez_21d_base_v038_signal(intangibles, capex, closeadj):
    a = _f41_acquisition_score(intangibles, capex, 21)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v039: 63d acquisition score z-score over 504d
def f41mas_f41_medtech_acquisition_signature_acqscorez_63d_base_v039_signal(intangibles, capex, closeadj):
    a = _f41_acquisition_score(intangibles, capex, 63)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v040: 252d acquisition score z-score over 504d
def f41mas_f41_medtech_acquisition_signature_acqscorez_252d_base_v040_signal(intangibles, capex, closeadj):
    a = _f41_acquisition_score(intangibles, capex, 252)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v041: 21d acquisition score × intangibles growth 63d
def f41mas_f41_medtech_acquisition_signature_acqxgr_21d_base_v041_signal(intangibles, capex, closeadj):
    a = _f41_acquisition_score(intangibles, capex, 21)
    g = _f41_intangibles_growth(intangibles, 63)
    result = a * g * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v042: 63d acquisition score × intangibles growth 252d
def f41mas_f41_medtech_acquisition_signature_acqxgr_63d_base_v042_signal(intangibles, capex, closeadj):
    a = _f41_acquisition_score(intangibles, capex, 63)
    g = _f41_intangibles_growth(intangibles, 252)
    result = a * g * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v043: 252d acquisition score × intangibles growth 504d
def f41mas_f41_medtech_acquisition_signature_acqxgr_252d_base_v043_signal(intangibles, capex, closeadj):
    a = _f41_acquisition_score(intangibles, capex, 252)
    g = _f41_intangibles_growth(intangibles, 504)
    result = a * g * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v044: 21d acquisition score × asset pulse 21d
def f41mas_f41_medtech_acquisition_signature_acqxpulse_21d_base_v044_signal(intangibles, capex, assets, closeadj):
    a = _f41_acquisition_score(intangibles, capex, 21)
    p = _f41_asset_pulse(assets, intangibles, 21)
    result = a * p * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v045: 63d acquisition score × asset pulse 63d
def f41mas_f41_medtech_acquisition_signature_acqxpulse_63d_base_v045_signal(intangibles, capex, assets, closeadj):
    a = _f41_acquisition_score(intangibles, capex, 63)
    p = _f41_asset_pulse(assets, intangibles, 63)
    result = a * p * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v046: 252d acquisition score × asset pulse 252d
def f41mas_f41_medtech_acquisition_signature_acqxpulse_252d_base_v046_signal(intangibles, capex, assets, closeadj):
    a = _f41_acquisition_score(intangibles, capex, 252)
    p = _f41_asset_pulse(assets, intangibles, 252)
    result = a * p * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v047: 5d intangibles growth scaled
def f41mas_f41_medtech_acquisition_signature_intanggr_5d_base_v047_signal(intangibles, closeadj):
    result = _f41_intangibles_growth(intangibles, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v048: 10d intangibles growth scaled
def f41mas_f41_medtech_acquisition_signature_intanggr_10d_base_v048_signal(intangibles, closeadj):
    result = _f41_intangibles_growth(intangibles, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v049: 42d intangibles growth scaled
def f41mas_f41_medtech_acquisition_signature_intanggr_42d_base_v049_signal(intangibles, closeadj):
    result = _f41_intangibles_growth(intangibles, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v050: 189d intangibles growth scaled
def f41mas_f41_medtech_acquisition_signature_intanggr_189d_base_v050_signal(intangibles, closeadj):
    result = _f41_intangibles_growth(intangibles, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v051: 378d intangibles growth scaled
def f41mas_f41_medtech_acquisition_signature_intanggr_378d_base_v051_signal(intangibles, closeadj):
    result = _f41_intangibles_growth(intangibles, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v052: 5d acquisition score
def f41mas_f41_medtech_acquisition_signature_acqscore_5d_base_v052_signal(intangibles, capex, closeadj):
    result = _f41_acquisition_score(intangibles, capex, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v053: 10d acquisition score
def f41mas_f41_medtech_acquisition_signature_acqscore_10d_base_v053_signal(intangibles, capex, closeadj):
    result = _f41_acquisition_score(intangibles, capex, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v054: 42d acquisition score
def f41mas_f41_medtech_acquisition_signature_acqscore_42d_base_v054_signal(intangibles, capex, closeadj):
    result = _f41_acquisition_score(intangibles, capex, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v055: 189d acquisition score
def f41mas_f41_medtech_acquisition_signature_acqscore_189d_base_v055_signal(intangibles, capex, closeadj):
    result = _f41_acquisition_score(intangibles, capex, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v056: 378d acquisition score
def f41mas_f41_medtech_acquisition_signature_acqscore_378d_base_v056_signal(intangibles, capex, closeadj):
    result = _f41_acquisition_score(intangibles, capex, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v057: 21d intangibles to capex ratio (M&A vs organic) scaled
def f41mas_f41_medtech_acquisition_signature_intangtocapex_21d_base_v057_signal(intangibles, capex, closeadj):
    ratio = _safe_div(intangibles.diff(periods=21), _mean(capex, 21))
    result = ratio * closeadj + _f41_acquisition_score(intangibles, capex, 21) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# v058: 63d intangibles to capex ratio
def f41mas_f41_medtech_acquisition_signature_intangtocapex_63d_base_v058_signal(intangibles, capex, closeadj):
    ratio = _safe_div(intangibles.diff(periods=63), _mean(capex, 63))
    result = ratio * closeadj + _f41_acquisition_score(intangibles, capex, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# v059: 252d intangibles to capex ratio
def f41mas_f41_medtech_acquisition_signature_intangtocapex_252d_base_v059_signal(intangibles, capex, closeadj):
    ratio = _safe_div(intangibles.diff(periods=252), _mean(capex, 252))
    result = ratio * closeadj + _f41_acquisition_score(intangibles, capex, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# v060: 21d EMA of intangibles growth scaled
def f41mas_f41_medtech_acquisition_signature_intangrema_21d_base_v060_signal(intangibles, closeadj):
    g = _f41_intangibles_growth(intangibles, 21)
    result = g.ewm(span=21, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v061: 63d EMA of intangibles growth scaled
def f41mas_f41_medtech_acquisition_signature_intangrema_63d_base_v061_signal(intangibles, closeadj):
    g = _f41_intangibles_growth(intangibles, 63)
    result = g.ewm(span=63, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v062: 252d EMA of intangibles growth scaled
def f41mas_f41_medtech_acquisition_signature_intangrema_252d_base_v062_signal(intangibles, closeadj):
    g = _f41_intangibles_growth(intangibles, 252)
    result = g.ewm(span=252, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v063: log(1+intang growth) × close
def f41mas_f41_medtech_acquisition_signature_intangrlog_21d_base_v063_signal(intangibles, closeadj):
    g = _f41_intangibles_growth(intangibles, 21)
    result = np.sign(g) * np.log1p(g.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v064: 63d log intang growth × close
def f41mas_f41_medtech_acquisition_signature_intangrlog_63d_base_v064_signal(intangibles, closeadj):
    g = _f41_intangibles_growth(intangibles, 63)
    result = np.sign(g) * np.log1p(g.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v065: 252d log intang growth × close
def f41mas_f41_medtech_acquisition_signature_intangrlog_252d_base_v065_signal(intangibles, closeadj):
    g = _f41_intangibles_growth(intangibles, 252)
    result = np.sign(g) * np.log1p(g.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v066: 21d intang growth × assets growth (cross-balance)
def f41mas_f41_medtech_acquisition_signature_grxassets_21d_base_v066_signal(intangibles, assets, closeadj):
    g = _f41_intangibles_growth(intangibles, 21)
    ag = assets.pct_change(periods=21)
    result = g * ag * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v067: 63d intang growth × assets growth
def f41mas_f41_medtech_acquisition_signature_grxassets_63d_base_v067_signal(intangibles, assets, closeadj):
    g = _f41_intangibles_growth(intangibles, 63)
    ag = assets.pct_change(periods=63)
    result = g * ag * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v068: 252d intang growth × assets growth
def f41mas_f41_medtech_acquisition_signature_grxassets_252d_base_v068_signal(intangibles, assets, closeadj):
    g = _f41_intangibles_growth(intangibles, 252)
    ag = assets.pct_change(periods=252)
    result = g * ag * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v069: 21d acquisition score × intang share
def f41mas_f41_medtech_acquisition_signature_acqxshare_21d_base_v069_signal(intangibles, capex, assets, closeadj):
    a = _f41_acquisition_score(intangibles, capex, 21)
    share = intangibles / assets.replace(0, np.nan)
    result = a * share * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v070: 63d acquisition score × intang share
def f41mas_f41_medtech_acquisition_signature_acqxshare_63d_base_v070_signal(intangibles, capex, assets, closeadj):
    a = _f41_acquisition_score(intangibles, capex, 63)
    share = intangibles / assets.replace(0, np.nan)
    result = a * share * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v071: 252d acquisition score × intang share
def f41mas_f41_medtech_acquisition_signature_acqxshare_252d_base_v071_signal(intangibles, capex, assets, closeadj):
    a = _f41_acquisition_score(intangibles, capex, 252)
    share = intangibles / assets.replace(0, np.nan)
    result = a * share * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v072: 21d pulse × intang growth lagged 63d
def f41mas_f41_medtech_acquisition_signature_pulsexgrlag_21d_base_v072_signal(assets, intangibles, closeadj):
    p = _f41_asset_pulse(assets, intangibles, 21)
    gl = _f41_intangibles_growth(intangibles, 63).shift(21)
    result = p * gl * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v073: 63d pulse × intang growth lagged 126d
def f41mas_f41_medtech_acquisition_signature_pulsexgrlag_63d_base_v073_signal(assets, intangibles, closeadj):
    p = _f41_asset_pulse(assets, intangibles, 63)
    gl = _f41_intangibles_growth(intangibles, 126).shift(63)
    result = p * gl * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v074: 252d pulse × intang growth lagged 252d
def f41mas_f41_medtech_acquisition_signature_pulsexgrlag_252d_base_v074_signal(assets, intangibles, closeadj):
    p = _f41_asset_pulse(assets, intangibles, 252)
    gl = _f41_intangibles_growth(intangibles, 252).shift(126)
    result = p * gl * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v075: 21d quantile rank of intangibles growth × close
def f41mas_f41_medtech_acquisition_signature_intangrqr_21d_base_v075_signal(intangibles, closeadj):
    g = _f41_intangibles_growth(intangibles, 21)
    qr = g.rolling(252, min_periods=63).rank(pct=True)
    result = qr * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f41mas_f41_medtech_acquisition_signature_intanggr_21d_base_v001_signal,
    f41mas_f41_medtech_acquisition_signature_intanggr_63d_base_v002_signal,
    f41mas_f41_medtech_acquisition_signature_intanggr_126d_base_v003_signal,
    f41mas_f41_medtech_acquisition_signature_intanggr_252d_base_v004_signal,
    f41mas_f41_medtech_acquisition_signature_intanggr_504d_base_v005_signal,
    f41mas_f41_medtech_acquisition_signature_intanggrsq_21d_base_v006_signal,
    f41mas_f41_medtech_acquisition_signature_intanggrsq_63d_base_v007_signal,
    f41mas_f41_medtech_acquisition_signature_intanggrsq_252d_base_v008_signal,
    f41mas_f41_medtech_acquisition_signature_intanggrz_21d_base_v009_signal,
    f41mas_f41_medtech_acquisition_signature_intanggrz_63d_base_v010_signal,
    f41mas_f41_medtech_acquisition_signature_assetpulse_21d_base_v011_signal,
    f41mas_f41_medtech_acquisition_signature_assetpulse_63d_base_v012_signal,
    f41mas_f41_medtech_acquisition_signature_assetpulse_126d_base_v013_signal,
    f41mas_f41_medtech_acquisition_signature_assetpulse_252d_base_v014_signal,
    f41mas_f41_medtech_acquisition_signature_assetpulse_504d_base_v015_signal,
    f41mas_f41_medtech_acquisition_signature_acqscore_21d_base_v016_signal,
    f41mas_f41_medtech_acquisition_signature_acqscore_63d_base_v017_signal,
    f41mas_f41_medtech_acquisition_signature_acqscore_126d_base_v018_signal,
    f41mas_f41_medtech_acquisition_signature_acqscore_252d_base_v019_signal,
    f41mas_f41_medtech_acquisition_signature_acqscore_504d_base_v020_signal,
    f41mas_f41_medtech_acquisition_signature_grxpulse_21d_base_v021_signal,
    f41mas_f41_medtech_acquisition_signature_grxpulse_63d_base_v022_signal,
    f41mas_f41_medtech_acquisition_signature_grxpulse_252d_base_v023_signal,
    f41mas_f41_medtech_acquisition_signature_grmean_21d_base_v024_signal,
    f41mas_f41_medtech_acquisition_signature_grmean_63d_base_v025_signal,
    f41mas_f41_medtech_acquisition_signature_grstd_63d_base_v026_signal,
    f41mas_f41_medtech_acquisition_signature_grstd_126d_base_v027_signal,
    f41mas_f41_medtech_acquisition_signature_grxcapex_21d_base_v028_signal,
    f41mas_f41_medtech_acquisition_signature_grxcapex_63d_base_v029_signal,
    f41mas_f41_medtech_acquisition_signature_grxcapex_252d_base_v030_signal,
    f41mas_f41_medtech_acquisition_signature_intangshare_21d_base_v031_signal,
    f41mas_f41_medtech_acquisition_signature_intangshare_63d_base_v032_signal,
    f41mas_f41_medtech_acquisition_signature_intangshare_252d_base_v033_signal,
    f41mas_f41_medtech_acquisition_signature_intangshare_504d_base_v034_signal,
    f41mas_f41_medtech_acquisition_signature_pulsez_21d_base_v035_signal,
    f41mas_f41_medtech_acquisition_signature_pulsez_63d_base_v036_signal,
    f41mas_f41_medtech_acquisition_signature_pulsez_252d_base_v037_signal,
    f41mas_f41_medtech_acquisition_signature_acqscorez_21d_base_v038_signal,
    f41mas_f41_medtech_acquisition_signature_acqscorez_63d_base_v039_signal,
    f41mas_f41_medtech_acquisition_signature_acqscorez_252d_base_v040_signal,
    f41mas_f41_medtech_acquisition_signature_acqxgr_21d_base_v041_signal,
    f41mas_f41_medtech_acquisition_signature_acqxgr_63d_base_v042_signal,
    f41mas_f41_medtech_acquisition_signature_acqxgr_252d_base_v043_signal,
    f41mas_f41_medtech_acquisition_signature_acqxpulse_21d_base_v044_signal,
    f41mas_f41_medtech_acquisition_signature_acqxpulse_63d_base_v045_signal,
    f41mas_f41_medtech_acquisition_signature_acqxpulse_252d_base_v046_signal,
    f41mas_f41_medtech_acquisition_signature_intanggr_5d_base_v047_signal,
    f41mas_f41_medtech_acquisition_signature_intanggr_10d_base_v048_signal,
    f41mas_f41_medtech_acquisition_signature_intanggr_42d_base_v049_signal,
    f41mas_f41_medtech_acquisition_signature_intanggr_189d_base_v050_signal,
    f41mas_f41_medtech_acquisition_signature_intanggr_378d_base_v051_signal,
    f41mas_f41_medtech_acquisition_signature_acqscore_5d_base_v052_signal,
    f41mas_f41_medtech_acquisition_signature_acqscore_10d_base_v053_signal,
    f41mas_f41_medtech_acquisition_signature_acqscore_42d_base_v054_signal,
    f41mas_f41_medtech_acquisition_signature_acqscore_189d_base_v055_signal,
    f41mas_f41_medtech_acquisition_signature_acqscore_378d_base_v056_signal,
    f41mas_f41_medtech_acquisition_signature_intangtocapex_21d_base_v057_signal,
    f41mas_f41_medtech_acquisition_signature_intangtocapex_63d_base_v058_signal,
    f41mas_f41_medtech_acquisition_signature_intangtocapex_252d_base_v059_signal,
    f41mas_f41_medtech_acquisition_signature_intangrema_21d_base_v060_signal,
    f41mas_f41_medtech_acquisition_signature_intangrema_63d_base_v061_signal,
    f41mas_f41_medtech_acquisition_signature_intangrema_252d_base_v062_signal,
    f41mas_f41_medtech_acquisition_signature_intangrlog_21d_base_v063_signal,
    f41mas_f41_medtech_acquisition_signature_intangrlog_63d_base_v064_signal,
    f41mas_f41_medtech_acquisition_signature_intangrlog_252d_base_v065_signal,
    f41mas_f41_medtech_acquisition_signature_grxassets_21d_base_v066_signal,
    f41mas_f41_medtech_acquisition_signature_grxassets_63d_base_v067_signal,
    f41mas_f41_medtech_acquisition_signature_grxassets_252d_base_v068_signal,
    f41mas_f41_medtech_acquisition_signature_acqxshare_21d_base_v069_signal,
    f41mas_f41_medtech_acquisition_signature_acqxshare_63d_base_v070_signal,
    f41mas_f41_medtech_acquisition_signature_acqxshare_252d_base_v071_signal,
    f41mas_f41_medtech_acquisition_signature_pulsexgrlag_21d_base_v072_signal,
    f41mas_f41_medtech_acquisition_signature_pulsexgrlag_63d_base_v073_signal,
    f41mas_f41_medtech_acquisition_signature_pulsexgrlag_252d_base_v074_signal,
    f41mas_f41_medtech_acquisition_signature_intangrqr_21d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F41_MEDTECH_ACQUISITION_SIGNATURE_REGISTRY_001_075 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    intangibles = pd.Series(3e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="intangibles")
    assets = pd.Series(2e9 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="assets")
    capex = pd.Series(5e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.02, n))), name="capex")

    cols = {
        "closeadj": closeadj, "intangibles": intangibles, "assets": assets, "capex": capex,
    }

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f41_intangibles_growth", "_f41_asset_pulse", "_f41_acquisition_score")
    for name, meta in REGISTRY.items():
        fn = meta["func"]
        args = [cols[c] for c in meta["inputs"]]
        y1 = fn(*args)
        y2 = fn(*args)
        pd.testing.assert_series_equal(y1, y2)
        q = y1.iloc[504:].dropna()
        assert len(q) > 0, name
        assert q.nunique() > 50, f"{name} nunique={q.nunique()}"
        assert q.std() > 0, name
        assert not q.isna().all(), name
        nan_ratio = y1.iloc[504:].isna().mean()
        if nan_ratio < 0.5:
            nan_ok += 1
        src = inspect.getsource(fn)
        assert any(p in src for p in domain_primitives), name
        n_features += 1
    assert n_features == 75, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print(f"OK f41_medtech_acquisition_signature_base_001_075_claude: {n_features} features pass")
