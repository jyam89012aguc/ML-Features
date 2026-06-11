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


# v076: 42d intang growth × close (cumulative deal cadence)
def f41mas_f41_medtech_acquisition_signature_intanggrcum_42d_base_v076_signal(intangibles, closeadj):
    g = _f41_intangibles_growth(intangibles, 42)
    result = g.rolling(63, min_periods=21).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v077: 126d intang growth cum 252d × close
def f41mas_f41_medtech_acquisition_signature_intanggrcum_126d_base_v077_signal(intangibles, closeadj):
    g = _f41_intangibles_growth(intangibles, 126)
    result = g.rolling(252, min_periods=63).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v078: 252d intang growth cum 504d × close
def f41mas_f41_medtech_acquisition_signature_intanggrcum_252d_base_v078_signal(intangibles, closeadj):
    g = _f41_intangibles_growth(intangibles, 252)
    result = g.rolling(504, min_periods=126).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v079: 21d intang growth × pulse 63d (cross window)
def f41mas_f41_medtech_acquisition_signature_grxpulsex_2163_base_v079_signal(intangibles, assets, closeadj):
    g = _f41_intangibles_growth(intangibles, 21)
    p = _f41_asset_pulse(assets, intangibles, 63)
    result = g * p * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v080: 63d intang growth × pulse 252d
def f41mas_f41_medtech_acquisition_signature_grxpulsex_63252_base_v080_signal(intangibles, assets, closeadj):
    g = _f41_intangibles_growth(intangibles, 63)
    p = _f41_asset_pulse(assets, intangibles, 252)
    result = g * p * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v081: 126d intang growth × pulse 504d
def f41mas_f41_medtech_acquisition_signature_grxpulsex_126504_base_v081_signal(intangibles, assets, closeadj):
    g = _f41_intangibles_growth(intangibles, 126)
    p = _f41_asset_pulse(assets, intangibles, 504)
    result = g * p * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v082: 21d acq score × pulse 63d
def f41mas_f41_medtech_acquisition_signature_acqxpulsex_2163_base_v082_signal(intangibles, capex, assets, closeadj):
    a = _f41_acquisition_score(intangibles, capex, 21)
    p = _f41_asset_pulse(assets, intangibles, 63)
    result = a * p * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v083: 63d acq score × pulse 252d
def f41mas_f41_medtech_acquisition_signature_acqxpulsex_63252_base_v083_signal(intangibles, capex, assets, closeadj):
    a = _f41_acquisition_score(intangibles, capex, 63)
    p = _f41_asset_pulse(assets, intangibles, 252)
    result = a * p * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v084: 21d acq score × growth 252d (long memory)
def f41mas_f41_medtech_acquisition_signature_acqxgrlong_21d_base_v084_signal(intangibles, capex, closeadj):
    a = _f41_acquisition_score(intangibles, capex, 21)
    g = _f41_intangibles_growth(intangibles, 252)
    result = a * g * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v085: 63d acq score × growth 504d
def f41mas_f41_medtech_acquisition_signature_acqxgrlong_63d_base_v085_signal(intangibles, capex, closeadj):
    a = _f41_acquisition_score(intangibles, capex, 63)
    g = _f41_intangibles_growth(intangibles, 504)
    result = a * g * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v086: 21d EMA of acq score scaled
def f41mas_f41_medtech_acquisition_signature_acqema_21d_base_v086_signal(intangibles, capex, closeadj):
    a = _f41_acquisition_score(intangibles, capex, 21)
    result = a.ewm(span=21, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v087: 63d EMA of acq score scaled
def f41mas_f41_medtech_acquisition_signature_acqema_63d_base_v087_signal(intangibles, capex, closeadj):
    a = _f41_acquisition_score(intangibles, capex, 63)
    result = a.ewm(span=63, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v088: 252d EMA of acq score scaled
def f41mas_f41_medtech_acquisition_signature_acqema_252d_base_v088_signal(intangibles, capex, closeadj):
    a = _f41_acquisition_score(intangibles, capex, 252)
    result = a.ewm(span=252, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v089: 21d pulse EMA scaled
def f41mas_f41_medtech_acquisition_signature_pulseema_21d_base_v089_signal(assets, intangibles, closeadj):
    p = _f41_asset_pulse(assets, intangibles, 21)
    result = p.ewm(span=21, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v090: 63d pulse EMA scaled
def f41mas_f41_medtech_acquisition_signature_pulseema_63d_base_v090_signal(assets, intangibles, closeadj):
    p = _f41_asset_pulse(assets, intangibles, 63)
    result = p.ewm(span=63, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v091: 252d pulse EMA scaled
def f41mas_f41_medtech_acquisition_signature_pulseema_252d_base_v091_signal(assets, intangibles, closeadj):
    p = _f41_asset_pulse(assets, intangibles, 252)
    result = p.ewm(span=252, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v092: 21d acq score std over 252d × close
def f41mas_f41_medtech_acquisition_signature_acqstd_21d_base_v092_signal(intangibles, capex, closeadj):
    a = _f41_acquisition_score(intangibles, capex, 21)
    result = _std(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v093: 63d acq score std over 252d × close
def f41mas_f41_medtech_acquisition_signature_acqstd_63d_base_v093_signal(intangibles, capex, closeadj):
    a = _f41_acquisition_score(intangibles, capex, 63)
    result = _std(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v094: 252d acq score std over 504d × close
def f41mas_f41_medtech_acquisition_signature_acqstd_252d_base_v094_signal(intangibles, capex, closeadj):
    a = _f41_acquisition_score(intangibles, capex, 252)
    result = _std(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v095: 21d pulse std over 252d × close
def f41mas_f41_medtech_acquisition_signature_pulsestd_21d_base_v095_signal(assets, intangibles, closeadj):
    p = _f41_asset_pulse(assets, intangibles, 21)
    result = _std(p, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v096: 63d pulse std over 252d × close
def f41mas_f41_medtech_acquisition_signature_pulsestd_63d_base_v096_signal(assets, intangibles, closeadj):
    p = _f41_asset_pulse(assets, intangibles, 63)
    result = _std(p, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v097: 252d pulse std over 504d × close
def f41mas_f41_medtech_acquisition_signature_pulsestd_252d_base_v097_signal(assets, intangibles, closeadj):
    p = _f41_asset_pulse(assets, intangibles, 252)
    result = _std(p, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v098: intang growth bigger than 5% indicator × close (deal event)
def f41mas_f41_medtech_acquisition_signature_dealind_63d_base_v098_signal(intangibles, closeadj):
    g = _f41_intangibles_growth(intangibles, 63)
    ind = (g > 0.05).astype(float)
    result = ind.rolling(252, min_periods=63).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v099: intang growth bigger than 10% indicator × close
def f41mas_f41_medtech_acquisition_signature_dealind_252d_base_v099_signal(intangibles, closeadj):
    g = _f41_intangibles_growth(intangibles, 252)
    ind = (g > 0.10).astype(float)
    result = ind.rolling(504, min_periods=126).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v100: acq score above 0.5 indicator × close
def f41mas_f41_medtech_acquisition_signature_acqind_63d_base_v100_signal(intangibles, capex, closeadj):
    a = _f41_acquisition_score(intangibles, capex, 63)
    ind = (a > 0.5).astype(float)
    result = ind.rolling(252, min_periods=63).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v101: 21d intang growth × capex z-score
def f41mas_f41_medtech_acquisition_signature_grxcapexz_21d_base_v101_signal(intangibles, capex, closeadj):
    g = _f41_intangibles_growth(intangibles, 21)
    cz = _z(capex, 252)
    result = g * cz * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v102: 63d intang growth × capex z-score
def f41mas_f41_medtech_acquisition_signature_grxcapexz_63d_base_v102_signal(intangibles, capex, closeadj):
    g = _f41_intangibles_growth(intangibles, 63)
    cz = _z(capex, 252)
    result = g * cz * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v103: 252d intang growth × capex z-score
def f41mas_f41_medtech_acquisition_signature_grxcapexz_252d_base_v103_signal(intangibles, capex, closeadj):
    g = _f41_intangibles_growth(intangibles, 252)
    cz = _z(capex, 504)
    result = g * cz * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v104: 21d acq score difference vs lag 21d × close
def f41mas_f41_medtech_acquisition_signature_acqdiff_21d_base_v104_signal(intangibles, capex, closeadj):
    a = _f41_acquisition_score(intangibles, capex, 21)
    result = (a - a.shift(21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v105: 63d acq score difference vs lag 63d × close
def f41mas_f41_medtech_acquisition_signature_acqdiff_63d_base_v105_signal(intangibles, capex, closeadj):
    a = _f41_acquisition_score(intangibles, capex, 63)
    result = (a - a.shift(63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v106: 252d acq score diff × close
def f41mas_f41_medtech_acquisition_signature_acqdiff_252d_base_v106_signal(intangibles, capex, closeadj):
    a = _f41_acquisition_score(intangibles, capex, 252)
    result = (a - a.shift(252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v107: pulse diff vs lag × close
def f41mas_f41_medtech_acquisition_signature_pulsediff_21d_base_v107_signal(assets, intangibles, closeadj):
    p = _f41_asset_pulse(assets, intangibles, 21)
    result = (p - p.shift(21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v108: pulse diff 63d × close
def f41mas_f41_medtech_acquisition_signature_pulsediff_63d_base_v108_signal(assets, intangibles, closeadj):
    p = _f41_asset_pulse(assets, intangibles, 63)
    result = (p - p.shift(63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v109: pulse diff 252d × close
def f41mas_f41_medtech_acquisition_signature_pulsediff_252d_base_v109_signal(assets, intangibles, closeadj):
    p = _f41_asset_pulse(assets, intangibles, 252)
    result = (p - p.shift(252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v110: max acq score over 63d × close
def f41mas_f41_medtech_acquisition_signature_acqmax_63d_base_v110_signal(intangibles, capex, closeadj):
    a = _f41_acquisition_score(intangibles, capex, 21)
    result = a.rolling(63, min_periods=21).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v111: max acq score over 252d × close
def f41mas_f41_medtech_acquisition_signature_acqmax_252d_base_v111_signal(intangibles, capex, closeadj):
    a = _f41_acquisition_score(intangibles, capex, 63)
    result = a.rolling(252, min_periods=63).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v112: max acq score over 504d × close
def f41mas_f41_medtech_acquisition_signature_acqmax_504d_base_v112_signal(intangibles, capex, closeadj):
    a = _f41_acquisition_score(intangibles, capex, 126)
    result = a.rolling(504, min_periods=126).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v113: min intang growth (negative shock) × close
def f41mas_f41_medtech_acquisition_signature_grmin_63d_base_v113_signal(intangibles, closeadj):
    g = _f41_intangibles_growth(intangibles, 21)
    result = g.rolling(63, min_periods=21).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v114: min intang growth 252d × close
def f41mas_f41_medtech_acquisition_signature_grmin_252d_base_v114_signal(intangibles, closeadj):
    g = _f41_intangibles_growth(intangibles, 63)
    result = g.rolling(252, min_periods=63).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v115: pulse max 252d × close
def f41mas_f41_medtech_acquisition_signature_pulsemax_252d_base_v115_signal(assets, intangibles, closeadj):
    p = _f41_asset_pulse(assets, intangibles, 63)
    result = p.rolling(252, min_periods=63).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v116: pulse min 252d × close (asset-mix shrink)
def f41mas_f41_medtech_acquisition_signature_pulsemin_252d_base_v116_signal(assets, intangibles, closeadj):
    p = _f41_asset_pulse(assets, intangibles, 63)
    result = p.rolling(252, min_periods=63).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v117: pulse range 252d × close
def f41mas_f41_medtech_acquisition_signature_pulserng_252d_base_v117_signal(assets, intangibles, closeadj):
    p = _f41_asset_pulse(assets, intangibles, 63)
    r = p.rolling(252, min_periods=63).max() - p.rolling(252, min_periods=63).min()
    result = r * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v118: acq score range 252d × close
def f41mas_f41_medtech_acquisition_signature_acqrng_252d_base_v118_signal(intangibles, capex, closeadj):
    a = _f41_acquisition_score(intangibles, capex, 63)
    r = a.rolling(252, min_periods=63).max() - a.rolling(252, min_periods=63).min()
    result = r * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v119: intang growth deciles × close (rank within window)
def f41mas_f41_medtech_acquisition_signature_grqr_63d_base_v119_signal(intangibles, closeadj):
    g = _f41_intangibles_growth(intangibles, 63)
    qr = g.rolling(252, min_periods=63).rank(pct=True)
    result = qr * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v120: acq score rank × close
def f41mas_f41_medtech_acquisition_signature_acqqr_63d_base_v120_signal(intangibles, capex, closeadj):
    a = _f41_acquisition_score(intangibles, capex, 63)
    qr = a.rolling(252, min_periods=63).rank(pct=True)
    result = qr * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v121: pulse rank × close
def f41mas_f41_medtech_acquisition_signature_pulseqr_63d_base_v121_signal(assets, intangibles, closeadj):
    p = _f41_asset_pulse(assets, intangibles, 63)
    qr = p.rolling(252, min_periods=63).rank(pct=True)
    result = qr * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v122: intang growth vs lag 63 (acceleration of M&A) × close
def f41mas_f41_medtech_acquisition_signature_graccel_63d_base_v122_signal(intangibles, closeadj):
    g1 = _f41_intangibles_growth(intangibles, 63)
    g2 = _f41_intangibles_growth(intangibles, 63).shift(63)
    result = (g1 - g2) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v123: intang growth vs lag 252 × close
def f41mas_f41_medtech_acquisition_signature_graccel_252d_base_v123_signal(intangibles, closeadj):
    g1 = _f41_intangibles_growth(intangibles, 252)
    g2 = _f41_intangibles_growth(intangibles, 252).shift(252)
    result = (g1 - g2) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v124: acq score acceleration × close
def f41mas_f41_medtech_acquisition_signature_acqaccel_63d_base_v124_signal(intangibles, capex, closeadj):
    a1 = _f41_acquisition_score(intangibles, capex, 63)
    a2 = a1.shift(63)
    result = (a1 - a2) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v125: acq score acceleration 252d × close
def f41mas_f41_medtech_acquisition_signature_acqaccel_252d_base_v125_signal(intangibles, capex, closeadj):
    a1 = _f41_acquisition_score(intangibles, capex, 252)
    a2 = a1.shift(252)
    result = (a1 - a2) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v126: intang growth × intang share squared × close
def f41mas_f41_medtech_acquisition_signature_grxsharesq_63d_base_v126_signal(intangibles, assets, closeadj):
    g = _f41_intangibles_growth(intangibles, 63)
    share = intangibles / assets.replace(0, np.nan)
    result = g * share * share * closeadj + _f41_asset_pulse(assets, intangibles, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# v127: intang growth × intang share squared 252d × close
def f41mas_f41_medtech_acquisition_signature_grxsharesq_252d_base_v127_signal(intangibles, assets, closeadj):
    g = _f41_intangibles_growth(intangibles, 252)
    share = intangibles / assets.replace(0, np.nan)
    result = g * share * share * closeadj + _f41_asset_pulse(assets, intangibles, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# v128: 21d acq score × capex/assets ratio × close
def f41mas_f41_medtech_acquisition_signature_acqxcapexa_21d_base_v128_signal(intangibles, capex, assets, closeadj):
    a = _f41_acquisition_score(intangibles, capex, 21)
    ratio = _safe_div(capex, assets)
    result = a * ratio * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v129: 63d acq score × capex/assets × close
def f41mas_f41_medtech_acquisition_signature_acqxcapexa_63d_base_v129_signal(intangibles, capex, assets, closeadj):
    a = _f41_acquisition_score(intangibles, capex, 63)
    ratio = _safe_div(capex, assets)
    result = a * ratio * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v130: 252d acq score × capex/assets × close
def f41mas_f41_medtech_acquisition_signature_acqxcapexa_252d_base_v130_signal(intangibles, capex, assets, closeadj):
    a = _f41_acquisition_score(intangibles, capex, 252)
    ratio = _safe_div(capex, assets)
    result = a * ratio * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v131: 21d intang growth × close × mean capex/assets ratio
def f41mas_f41_medtech_acquisition_signature_grxcapexamean_21d_base_v131_signal(intangibles, capex, assets, closeadj):
    g = _f41_intangibles_growth(intangibles, 21)
    ratio = _mean(_safe_div(capex, assets), 21)
    result = g * ratio * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v132: 63d intang growth × mean ratio
def f41mas_f41_medtech_acquisition_signature_grxcapexamean_63d_base_v132_signal(intangibles, capex, assets, closeadj):
    g = _f41_intangibles_growth(intangibles, 63)
    ratio = _mean(_safe_div(capex, assets), 63)
    result = g * ratio * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v133: 252d intang growth × mean ratio
def f41mas_f41_medtech_acquisition_signature_grxcapexamean_252d_base_v133_signal(intangibles, capex, assets, closeadj):
    g = _f41_intangibles_growth(intangibles, 252)
    ratio = _mean(_safe_div(capex, assets), 252)
    result = g * ratio * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v134: 21d pulse × close^2 (price-amplified)
def f41mas_f41_medtech_acquisition_signature_pulsexpricesq_21d_base_v134_signal(assets, intangibles, closeadj):
    p = _f41_asset_pulse(assets, intangibles, 21)
    result = p * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v135: 63d pulse × close^2
def f41mas_f41_medtech_acquisition_signature_pulsexpricesq_63d_base_v135_signal(assets, intangibles, closeadj):
    p = _f41_asset_pulse(assets, intangibles, 63)
    result = p * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v136: 252d pulse × close^2
def f41mas_f41_medtech_acquisition_signature_pulsexpricesq_252d_base_v136_signal(assets, intangibles, closeadj):
    p = _f41_asset_pulse(assets, intangibles, 252)
    result = p * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v137: 21d acq score × close^2
def f41mas_f41_medtech_acquisition_signature_acqxpricesq_21d_base_v137_signal(intangibles, capex, closeadj):
    a = _f41_acquisition_score(intangibles, capex, 21)
    result = a * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v138: 63d acq score × close^2
def f41mas_f41_medtech_acquisition_signature_acqxpricesq_63d_base_v138_signal(intangibles, capex, closeadj):
    a = _f41_acquisition_score(intangibles, capex, 63)
    result = a * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v139: 252d acq score × close^2
def f41mas_f41_medtech_acquisition_signature_acqxpricesq_252d_base_v139_signal(intangibles, capex, closeadj):
    a = _f41_acquisition_score(intangibles, capex, 252)
    result = a * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v140: deal cadence (rolling sum of acq score) × close, 63d
def f41mas_f41_medtech_acquisition_signature_acqcad_63d_base_v140_signal(intangibles, capex, closeadj):
    a = _f41_acquisition_score(intangibles, capex, 21)
    result = a.rolling(63, min_periods=21).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v141: deal cadence (rolling sum of acq score), 252d
def f41mas_f41_medtech_acquisition_signature_acqcad_252d_base_v141_signal(intangibles, capex, closeadj):
    a = _f41_acquisition_score(intangibles, capex, 63)
    result = a.rolling(252, min_periods=63).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v142: deal cadence 504d
def f41mas_f41_medtech_acquisition_signature_acqcad_504d_base_v142_signal(intangibles, capex, closeadj):
    a = _f41_acquisition_score(intangibles, capex, 126)
    result = a.rolling(504, min_periods=126).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v143: pulse cumulated 252d × close
def f41mas_f41_medtech_acquisition_signature_pulsecum_252d_base_v143_signal(assets, intangibles, closeadj):
    p = _f41_asset_pulse(assets, intangibles, 21)
    result = p.rolling(252, min_periods=63).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v144: pulse cumulated 504d × close
def f41mas_f41_medtech_acquisition_signature_pulsecum_504d_base_v144_signal(assets, intangibles, closeadj):
    p = _f41_asset_pulse(assets, intangibles, 63)
    result = p.rolling(504, min_periods=126).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v145: intang growth × pulse × ratio cap/asset
def f41mas_f41_medtech_acquisition_signature_triplet_63d_base_v145_signal(intangibles, capex, assets, closeadj):
    g = _f41_intangibles_growth(intangibles, 63)
    p = _f41_asset_pulse(assets, intangibles, 63)
    ratio = _safe_div(capex, assets)
    result = g * p * ratio * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v146: intang growth × pulse × ratio cap/asset 252d
def f41mas_f41_medtech_acquisition_signature_triplet_252d_base_v146_signal(intangibles, capex, assets, closeadj):
    g = _f41_intangibles_growth(intangibles, 252)
    p = _f41_asset_pulse(assets, intangibles, 252)
    ratio = _safe_div(capex, assets)
    result = g * p * ratio * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v147: composite M&A signature (z + z + z) × close
def f41mas_f41_medtech_acquisition_signature_composite_63d_base_v147_signal(intangibles, capex, assets, closeadj):
    g = _f41_intangibles_growth(intangibles, 63)
    p = _f41_asset_pulse(assets, intangibles, 63)
    a = _f41_acquisition_score(intangibles, capex, 63)
    result = (_z(g, 252) + _z(p, 252) + _z(a, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v148: composite 252d
def f41mas_f41_medtech_acquisition_signature_composite_252d_base_v148_signal(intangibles, capex, assets, closeadj):
    g = _f41_intangibles_growth(intangibles, 252)
    p = _f41_asset_pulse(assets, intangibles, 252)
    a = _f41_acquisition_score(intangibles, capex, 252)
    result = (_z(g, 504) + _z(p, 504) + _z(a, 504)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v149: composite 504d
def f41mas_f41_medtech_acquisition_signature_composite_504d_base_v149_signal(intangibles, capex, assets, closeadj):
    g = _f41_intangibles_growth(intangibles, 504)
    p = _f41_asset_pulse(assets, intangibles, 504)
    a = _f41_acquisition_score(intangibles, capex, 504)
    result = (_z(g, 504) + _z(p, 504) + _z(a, 504)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v150: deal-spend amplification: acq score × capex pct change 63 × close
def f41mas_f41_medtech_acquisition_signature_acqxcapexchg_63d_base_v150_signal(intangibles, capex, closeadj):
    a = _f41_acquisition_score(intangibles, capex, 63)
    cc = capex.pct_change(63)
    result = a * cc * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f41mas_f41_medtech_acquisition_signature_intanggrcum_42d_base_v076_signal,
    f41mas_f41_medtech_acquisition_signature_intanggrcum_126d_base_v077_signal,
    f41mas_f41_medtech_acquisition_signature_intanggrcum_252d_base_v078_signal,
    f41mas_f41_medtech_acquisition_signature_grxpulsex_2163_base_v079_signal,
    f41mas_f41_medtech_acquisition_signature_grxpulsex_63252_base_v080_signal,
    f41mas_f41_medtech_acquisition_signature_grxpulsex_126504_base_v081_signal,
    f41mas_f41_medtech_acquisition_signature_acqxpulsex_2163_base_v082_signal,
    f41mas_f41_medtech_acquisition_signature_acqxpulsex_63252_base_v083_signal,
    f41mas_f41_medtech_acquisition_signature_acqxgrlong_21d_base_v084_signal,
    f41mas_f41_medtech_acquisition_signature_acqxgrlong_63d_base_v085_signal,
    f41mas_f41_medtech_acquisition_signature_acqema_21d_base_v086_signal,
    f41mas_f41_medtech_acquisition_signature_acqema_63d_base_v087_signal,
    f41mas_f41_medtech_acquisition_signature_acqema_252d_base_v088_signal,
    f41mas_f41_medtech_acquisition_signature_pulseema_21d_base_v089_signal,
    f41mas_f41_medtech_acquisition_signature_pulseema_63d_base_v090_signal,
    f41mas_f41_medtech_acquisition_signature_pulseema_252d_base_v091_signal,
    f41mas_f41_medtech_acquisition_signature_acqstd_21d_base_v092_signal,
    f41mas_f41_medtech_acquisition_signature_acqstd_63d_base_v093_signal,
    f41mas_f41_medtech_acquisition_signature_acqstd_252d_base_v094_signal,
    f41mas_f41_medtech_acquisition_signature_pulsestd_21d_base_v095_signal,
    f41mas_f41_medtech_acquisition_signature_pulsestd_63d_base_v096_signal,
    f41mas_f41_medtech_acquisition_signature_pulsestd_252d_base_v097_signal,
    f41mas_f41_medtech_acquisition_signature_dealind_63d_base_v098_signal,
    f41mas_f41_medtech_acquisition_signature_dealind_252d_base_v099_signal,
    f41mas_f41_medtech_acquisition_signature_acqind_63d_base_v100_signal,
    f41mas_f41_medtech_acquisition_signature_grxcapexz_21d_base_v101_signal,
    f41mas_f41_medtech_acquisition_signature_grxcapexz_63d_base_v102_signal,
    f41mas_f41_medtech_acquisition_signature_grxcapexz_252d_base_v103_signal,
    f41mas_f41_medtech_acquisition_signature_acqdiff_21d_base_v104_signal,
    f41mas_f41_medtech_acquisition_signature_acqdiff_63d_base_v105_signal,
    f41mas_f41_medtech_acquisition_signature_acqdiff_252d_base_v106_signal,
    f41mas_f41_medtech_acquisition_signature_pulsediff_21d_base_v107_signal,
    f41mas_f41_medtech_acquisition_signature_pulsediff_63d_base_v108_signal,
    f41mas_f41_medtech_acquisition_signature_pulsediff_252d_base_v109_signal,
    f41mas_f41_medtech_acquisition_signature_acqmax_63d_base_v110_signal,
    f41mas_f41_medtech_acquisition_signature_acqmax_252d_base_v111_signal,
    f41mas_f41_medtech_acquisition_signature_acqmax_504d_base_v112_signal,
    f41mas_f41_medtech_acquisition_signature_grmin_63d_base_v113_signal,
    f41mas_f41_medtech_acquisition_signature_grmin_252d_base_v114_signal,
    f41mas_f41_medtech_acquisition_signature_pulsemax_252d_base_v115_signal,
    f41mas_f41_medtech_acquisition_signature_pulsemin_252d_base_v116_signal,
    f41mas_f41_medtech_acquisition_signature_pulserng_252d_base_v117_signal,
    f41mas_f41_medtech_acquisition_signature_acqrng_252d_base_v118_signal,
    f41mas_f41_medtech_acquisition_signature_grqr_63d_base_v119_signal,
    f41mas_f41_medtech_acquisition_signature_acqqr_63d_base_v120_signal,
    f41mas_f41_medtech_acquisition_signature_pulseqr_63d_base_v121_signal,
    f41mas_f41_medtech_acquisition_signature_graccel_63d_base_v122_signal,
    f41mas_f41_medtech_acquisition_signature_graccel_252d_base_v123_signal,
    f41mas_f41_medtech_acquisition_signature_acqaccel_63d_base_v124_signal,
    f41mas_f41_medtech_acquisition_signature_acqaccel_252d_base_v125_signal,
    f41mas_f41_medtech_acquisition_signature_grxsharesq_63d_base_v126_signal,
    f41mas_f41_medtech_acquisition_signature_grxsharesq_252d_base_v127_signal,
    f41mas_f41_medtech_acquisition_signature_acqxcapexa_21d_base_v128_signal,
    f41mas_f41_medtech_acquisition_signature_acqxcapexa_63d_base_v129_signal,
    f41mas_f41_medtech_acquisition_signature_acqxcapexa_252d_base_v130_signal,
    f41mas_f41_medtech_acquisition_signature_grxcapexamean_21d_base_v131_signal,
    f41mas_f41_medtech_acquisition_signature_grxcapexamean_63d_base_v132_signal,
    f41mas_f41_medtech_acquisition_signature_grxcapexamean_252d_base_v133_signal,
    f41mas_f41_medtech_acquisition_signature_pulsexpricesq_21d_base_v134_signal,
    f41mas_f41_medtech_acquisition_signature_pulsexpricesq_63d_base_v135_signal,
    f41mas_f41_medtech_acquisition_signature_pulsexpricesq_252d_base_v136_signal,
    f41mas_f41_medtech_acquisition_signature_acqxpricesq_21d_base_v137_signal,
    f41mas_f41_medtech_acquisition_signature_acqxpricesq_63d_base_v138_signal,
    f41mas_f41_medtech_acquisition_signature_acqxpricesq_252d_base_v139_signal,
    f41mas_f41_medtech_acquisition_signature_acqcad_63d_base_v140_signal,
    f41mas_f41_medtech_acquisition_signature_acqcad_252d_base_v141_signal,
    f41mas_f41_medtech_acquisition_signature_acqcad_504d_base_v142_signal,
    f41mas_f41_medtech_acquisition_signature_pulsecum_252d_base_v143_signal,
    f41mas_f41_medtech_acquisition_signature_pulsecum_504d_base_v144_signal,
    f41mas_f41_medtech_acquisition_signature_triplet_63d_base_v145_signal,
    f41mas_f41_medtech_acquisition_signature_triplet_252d_base_v146_signal,
    f41mas_f41_medtech_acquisition_signature_composite_63d_base_v147_signal,
    f41mas_f41_medtech_acquisition_signature_composite_252d_base_v148_signal,
    f41mas_f41_medtech_acquisition_signature_composite_504d_base_v149_signal,
    f41mas_f41_medtech_acquisition_signature_acqxcapexchg_63d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F41_MEDTECH_ACQUISITION_SIGNATURE_REGISTRY_076_150 = REGISTRY


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
    print(f"OK f41_medtech_acquisition_signature_base_076_150_claude: {n_features} features pass")
