import inspect
import numpy as np
import pandas as pd

TRADING_DAYS_YEAR = 252
TRADING_DAYS_TWOYEAR = 504
TRADING_DAYS_HALF = 126
TRADING_DAYS_QUARTER = 63
TRADING_DAYS_MONTH = 21
TRADING_DAYS_WEEK = 5


# ===== generic helpers =====
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


def _rank(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).rank(pct=True) - 0.5


def _rmax(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).max()


def _rmin(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).min()


# ===== folder domain primitives (capex / content spend magnitude & funding) =====
def _f27_spend(capex):
    return capex.abs()


def _f27_intensity(capex, base):
    return _f27_spend(capex) / base.replace(0, np.nan)


def _f27_growth(s, w):
    return s / s.shift(w).replace(0, np.nan) - 1.0


def _f27_loggrowth(s, w):
    return np.log(s.replace(0, np.nan) / s.shift(w).replace(0, np.nan))


def _f27_invest_intensity(ncfi, base):
    return (-ncfi) / base.replace(0, np.nan)


def _f27_capex_vs_depamor(capex, depamor):
    return _f27_spend(capex) / depamor.replace(0, np.nan)


# slope roc=63d of cxassetstilt_504d_base_v001_signal
def f27cx_f27_capex_content_spend_cxassetstilt_504d_slope_v001_signal(capex, assets):
    b = _f27_intensity(capex, assets)
    _b = b - b.ewm(span=504, min_periods=126).mean()
    _d = (_b - _b.shift(63)) / 63.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope roc=63d of cxassetsz_504d_base_v002_signal
def f27cx_f27_capex_content_spend_cxassetsz_504d_slope_v002_signal(capex, assets):
    b = _f27_intensity(capex, assets)
    _b = _z(b, 504)
    _d = (_b - _b.shift(63)) / 63.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope roc=42d of cxdep_252d_base_v003_signal
def f27cx_f27_capex_content_spend_cxdep_252d_slope_v003_signal(capex, depamor):
    b = _f27_capex_vs_depamor(capex, depamor)
    _b = _mean(b, 252)
    _d = (_b - _b.shift(42)) / 42.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope roc=63d of cxdeptilt_504d_base_v004_signal
def f27cx_f27_capex_content_spend_cxdeptilt_504d_slope_v004_signal(capex, depamor):
    b = _f27_capex_vs_depamor(capex, depamor)
    _b = b - b.ewm(span=504, min_periods=126).mean()
    _d = (_b - _b.shift(63)) / 63.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope roc=42d of cxppne_252d_base_v005_signal
def f27cx_f27_capex_content_spend_cxppne_252d_slope_v005_signal(capex, ppnenet):
    b = _f27_intensity(capex, ppnenet)
    _b = _mean(b, 252)
    _d = (_b - _b.shift(42)) / 42.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope roc=42d of cxppnez_252d_base_v006_signal
def f27cx_f27_capex_content_spend_cxppnez_252d_slope_v006_signal(capex, ppnenet):
    b = _f27_intensity(capex, ppnenet)
    _b = _z(b, 252)
    _d = (_b - _b.shift(42)) / 42.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope roc=42d of ncfiassets_252d_base_v007_signal
def f27cx_f27_capex_content_spend_ncfiassets_252d_slope_v007_signal(ncfi, assets):
    b = _f27_invest_intensity(ncfi, assets)
    _b = _mean(b, 252)
    _d = (_b - _b.shift(42)) / 42.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope roc=63d of ncfiassetsz_504d_base_v008_signal
def f27cx_f27_capex_content_spend_ncfiassetsz_504d_slope_v008_signal(ncfi, assets):
    b = _f27_invest_intensity(ncfi, assets)
    _b = _z(b, 504)
    _d = (_b - _b.shift(63)) / 63.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope roc=42d of cxgrow_252d_base_v009_signal
def f27cx_f27_capex_content_spend_cxgrow_252d_slope_v009_signal(capex):
    sp = _f27_spend(capex)
    _b = _f27_growth(sp, 252)
    _d = (_b - _b.shift(42)) / 42.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope roc=21d of cxloggrow_126d_base_v010_signal
def f27cx_f27_capex_content_spend_cxloggrow_126d_slope_v010_signal(capex):
    sp = _f27_spend(capex)
    _b = _f27_loggrowth(sp, 126)
    _d = (_b - _b.shift(21)) / 21.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope roc=42d of cxburst_252d_base_v011_signal
def f27cx_f27_capex_content_spend_cxburst_252d_slope_v011_signal(capex):
    sp = _f27_spend(capex)
    _b = sp / _mean(sp, 252).replace(0, np.nan) - 1.0
    _d = (_b - _b.shift(42)) / 42.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope roc=42d of cxcv_252d_base_v012_signal
def f27cx_f27_capex_content_spend_cxcv_252d_slope_v012_signal(capex):
    sp = _f27_spend(capex)
    _b = _std(sp, 252) / _mean(sp, 252).replace(0, np.nan)
    _d = (_b - _b.shift(42)) / 42.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope roc=42d of cxbasewedge_252d_base_v013_signal
def f27cx_f27_capex_content_spend_cxbasewedge_252d_slope_v013_signal(capex, assets, ppnenet):
    a = _f27_intensity(capex, assets)
    p = _f27_intensity(capex, ppnenet)
    _b = _z(a, 252) - _z(p, 252)
    _d = (_b - _b.shift(42)) / 42.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope roc=10d of cxdepbalmom_63d_base_v014_signal
def f27cx_f27_capex_content_spend_cxdepbalmom_63d_slope_v014_signal(capex, depamor):
    sp = _f27_spend(capex)
    d = depamor
    bal = (sp - d) / (sp + d).replace(0, np.nan)
    _b = bal - bal.shift(63)
    _d = (_b - _b.shift(10)) / 10.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope roc=63d of noncxinv_504d_base_v015_signal
def f27cx_f27_capex_content_spend_noncxinv_504d_slope_v015_signal(ncfi, capex):
    out = (-ncfi)
    share = (out - _f27_spend(capex)) / out.replace(0, np.nan)
    _b = _rank(share, 504)
    _d = (_b - _b.shift(63)) / 63.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope roc=63d of cxassetsrank_504d_base_v016_signal
def f27cx_f27_capex_content_spend_cxassetsrank_504d_slope_v016_signal(capex, assets):
    b = _f27_intensity(capex, assets)
    _b = _rank(b, 504)
    _d = (_b - _b.shift(63)) / 63.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope roc=63d of cxdeprank_504d_base_v017_signal
def f27cx_f27_capex_content_spend_cxdeprank_504d_slope_v017_signal(capex, depamor):
    b = _f27_capex_vs_depamor(capex, depamor)
    _b = _rank(b, 504)
    _d = (_b - _b.shift(63)) / 63.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope roc=21d of cxaccel_126d_base_v018_signal
def f27cx_f27_capex_content_spend_cxaccel_126d_slope_v018_signal(capex):
    sp = _f27_spend(capex)
    g = _f27_growth(sp, 126)
    _b = g - g.shift(126)
    _d = (_b - _b.shift(21)) / 21.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope roc=10d of depcxshareaccel_63d_base_v019_signal
def f27cx_f27_capex_content_spend_depcxshareaccel_63d_slope_v019_signal(depamor, capex):
    sp = _f27_spend(capex)
    share = depamor / (depamor + sp).replace(0, np.nan)
    g = share - share.shift(63)
    _b = g - g.shift(63)
    _d = (_b - _b.shift(10)) / 10.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope roc=42d of cxassetsspr_63v252_base_v020_signal
def f27cx_f27_capex_content_spend_cxassetsspr_63v252_slope_v020_signal(capex, assets):
    b = _f27_intensity(capex, assets)
    _b = _mean(b, 63) - _mean(b, 252)
    _d = (_b - _b.shift(42)) / 42.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope roc=42d of cxppnespr_63v252_base_v021_signal
def f27cx_f27_capex_content_spend_cxppnespr_63v252_slope_v021_signal(capex, ppnenet):
    b = _f27_intensity(capex, ppnenet)
    _b = _mean(b, 63) - _mean(b, 252)
    _d = (_b - _b.shift(42)) / 42.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope roc=42d of cxinvshare_252d_base_v022_signal
def f27cx_f27_capex_content_spend_cxinvshare_252d_slope_v022_signal(capex, ncfi):
    sp = _f27_spend(capex)
    out = (-ncfi)
    _b = _mean(sp / out.replace(0, np.nan), 252)
    _d = (_b - _b.shift(42)) / 42.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope roc=63d of netinvassets_504d_base_v023_signal
def f27cx_f27_capex_content_spend_netinvassets_504d_slope_v023_signal(capex, depamor, assets):
    net = (_f27_spend(capex) - depamor) / assets.replace(0, np.nan)
    _b = net - net.ewm(span=504, min_periods=126).mean()
    _d = (_b - _b.shift(63)) / 63.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope roc=42d of cxassetsyoy_252d_base_v024_signal
def f27cx_f27_capex_content_spend_cxassetsyoy_252d_slope_v024_signal(capex, assets):
    b = _f27_intensity(capex, assets)
    _b = b - b.shift(252)
    _d = (_b - _b.shift(42)) / 42.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope roc=42d of cxdepyoy_252d_base_v025_signal
def f27cx_f27_capex_content_spend_cxdepyoy_252d_slope_v025_signal(capex, depamor):
    b = _f27_capex_vs_depamor(capex, depamor)
    _b = b - b.shift(252)
    _d = (_b - _b.shift(42)) / 42.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope roc=42d of ncfistreak_252d_base_v026_signal
def f27cx_f27_capex_content_spend_ncfistreak_252d_slope_v026_signal(ncfi, assets):
    b = _f27_invest_intensity(ncfi, assets)
    med = b.rolling(252, min_periods=126).median()
    hot = (b > med).astype(float)
    _b = hot.rolling(252, min_periods=126).mean() - 0.5
    _d = (_b - _b.shift(42)) / 42.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope roc=42d of cxstepmag_252d_base_v027_signal
def f27cx_f27_capex_content_spend_cxstepmag_252d_slope_v027_signal(capex):
    sp = _f27_spend(capex)
    step = (sp / sp.shift(63).replace(0, np.nan) - 1.0).abs()
    _b = step.rolling(252, min_periods=126).mean()
    _d = (_b - _b.shift(42)) / 42.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope roc=42d of cxconc_252d_base_v028_signal
def f27cx_f27_capex_content_spend_cxconc_252d_slope_v028_signal(capex, ppnenet, assets):
    p = _f27_intensity(capex, ppnenet)
    a = _f27_intensity(capex, assets)
    _b = _mean(p / a.replace(0, np.nan), 252)
    _d = (_b - _b.shift(42)) / 42.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope roc=42d of otherinv_252d_base_v029_signal
def f27cx_f27_capex_content_spend_otherinv_252d_slope_v029_signal(ncfi, capex, assets):
    inv = _f27_invest_intensity(ncfi, assets)
    cx = _f27_intensity(capex, assets)
    _b = _mean(inv - cx, 252)
    _d = (_b - _b.shift(42)) / 42.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope roc=63d of cxdepregfrac_504d_base_v030_signal
def f27cx_f27_capex_content_spend_cxdepregfrac_504d_slope_v030_signal(capex, depamor):
    b = _f27_capex_vs_depamor(capex, depamor)
    med = b.rolling(504, min_periods=252).median()
    above = (b > med).astype(float)
    _b = above.rolling(252, min_periods=126).mean() - 0.5
    _d = (_b - _b.shift(63)) / 63.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope roc=42d of cxrevz_252d_base_v031_signal
def f27cx_f27_capex_content_spend_cxrevz_252d_slope_v031_signal(capex, revenue):
    b = _f27_intensity(capex, revenue)
    _b = _z(b, 252)
    _d = (_b - _b.shift(42)) / 42.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope roc=42d of cxassetsconv_252d_base_v032_signal
def f27cx_f27_capex_content_spend_cxassetsconv_252d_slope_v032_signal(capex, assets):
    b = _f27_intensity(capex, assets)
    m = _mean(b, 252)
    d = b - m
    _b = np.sign(d) * (d ** 2)
    _d = (_b - _b.shift(42)) / 42.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope roc=42d of ncfispr_63v252_base_v033_signal
def f27cx_f27_capex_content_spend_ncfispr_63v252_slope_v033_signal(ncfi, assets):
    b = _f27_invest_intensity(ncfi, assets)
    _b = _mean(b, 63) - _mean(b, 252)
    _d = (_b - _b.shift(42)) / 42.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope roc=21d of cxdepdisp_ema_base_v034_signal
def f27cx_f27_capex_content_spend_cxdepdisp_ema_slope_v034_signal(capex, depamor):
    b = _f27_capex_vs_depamor(capex, depamor)
    _b = b - b.ewm(span=189, min_periods=63).mean()
    _d = (_b - _b.shift(21)) / 21.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope roc=42d of cxassetsdisp_252d_base_v035_signal
def f27cx_f27_capex_content_spend_cxassetsdisp_252d_slope_v035_signal(capex, assets):
    b = _f27_intensity(capex, assets)
    _b = b - b.ewm(span=189, min_periods=63).mean()
    _d = (_b - _b.shift(42)) / 42.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope roc=42d of cxcycle_252d_base_v036_signal
def f27cx_f27_capex_content_spend_cxcycle_252d_slope_v036_signal(capex):
    sp = _f27_spend(capex)
    _b = _mean(sp, 63) / _mean(sp, 252).replace(0, np.nan) - 1.0
    _d = (_b - _b.shift(42)) / 42.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope roc=63d of netinvppnerank_504d_base_v037_signal
def f27cx_f27_capex_content_spend_netinvppnerank_504d_slope_v037_signal(capex, depamor, ppnenet):
    net = (_f27_spend(capex) - depamor) / ppnenet.replace(0, np.nan)
    _b = _rank(net, 504)
    _d = (_b - _b.shift(63)) / 63.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope roc=42d of ncfiyoy_252d_base_v038_signal
def f27cx_f27_capex_content_spend_ncfiyoy_252d_slope_v038_signal(ncfi, assets):
    b = _f27_invest_intensity(ncfi, assets)
    _b = b - b.shift(252)
    _d = (_b - _b.shift(42)) / 42.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope roc=42d of cxdepdisp_252d_base_v039_signal
def f27cx_f27_capex_content_spend_cxdepdisp_252d_slope_v039_signal(capex, depamor):
    b = _f27_capex_vs_depamor(capex, depamor)
    _b = _std(b, 252)
    _d = (_b - _b.shift(42)) / 42.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope roc=63d of cxppnerank_504d_base_v040_signal
def f27cx_f27_capex_content_spend_cxppnerank_504d_slope_v040_signal(capex, ppnenet):
    b = _f27_intensity(capex, ppnenet)
    _b = _rank(b, 504)
    _d = (_b - _b.shift(63)) / 63.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope roc=63d of cxburstrank_504d_base_v041_signal
def f27cx_f27_capex_content_spend_cxburstrank_504d_slope_v041_signal(capex):
    sp = _f27_spend(capex)
    ratio = sp / _mean(sp, 252).replace(0, np.nan)
    _b = _rank(ratio, 504)
    _d = (_b - _b.shift(63)) / 63.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope roc=21d of cxvsassetgrow_126d_base_v042_signal
def f27cx_f27_capex_content_spend_cxvsassetgrow_126d_slope_v042_signal(capex, assets):
    sp = _f27_spend(capex)
    _b = _f27_growth(sp, 126) - _f27_growth(assets, 126)
    _d = (_b - _b.shift(21)) / 21.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope roc=42d of ppnevsdepgrow_252d_base_v043_signal
def f27cx_f27_capex_content_spend_ppnevsdepgrow_252d_slope_v043_signal(ppnenet, depamor):
    _b = _f27_growth(ppnenet, 252) - _f27_growth(depamor, 252)
    _d = (_b - _b.shift(42)) / 42.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope roc=42d of invgap_252d_base_v044_signal
def f27cx_f27_capex_content_spend_invgap_252d_slope_v044_signal(ncfi, capex, ppnenet):
    gap = ((-ncfi) - _f27_spend(capex)) / ppnenet.replace(0, np.nan)
    _b = _z(gap, 252)
    _d = (_b - _b.shift(42)) / 42.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope roc=63d of cxassetszdist_504d_base_v045_signal
def f27cx_f27_capex_content_spend_cxassetszdist_504d_slope_v045_signal(capex, assets):
    b = _f27_intensity(capex, assets)
    med = b.rolling(504, min_periods=252).median()
    sd = _std(b, 252)
    _b = (b - med) / sd.replace(0, np.nan)
    _d = (_b - _b.shift(63)) / 63.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope roc=42d of buildstab_252d_base_v046_signal
def f27cx_f27_capex_content_spend_buildstab_252d_slope_v046_signal(capex, depamor):
    b = _f27_capex_vs_depamor(capex, depamor)
    _b = _mean(b, 126) / _std(b, 252).replace(0, np.nan)
    _d = (_b - _b.shift(42)) / 42.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope roc=42d of cxasym_252d_base_v047_signal
def f27cx_f27_capex_content_spend_cxasym_252d_slope_v047_signal(capex):
    sp = _f27_spend(capex)
    m = _mean(sp, 252)
    med = sp.rolling(252, min_periods=126).median()
    sd = _std(sp, 252)
    _b = (m - med) / sd.replace(0, np.nan)
    _d = (_b - _b.shift(42)) / 42.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope roc=42d of cxppnereldrift_252d_base_v048_signal
def f27cx_f27_capex_content_spend_cxppnereldrift_252d_slope_v048_signal(capex, ppnenet):
    b = _f27_intensity(capex, ppnenet)
    _b = (b - b.shift(252)) / b.replace(0, np.nan)
    _d = (_b - _b.shift(42)) / 42.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope roc=10d of cxppnemom_63d_base_v049_signal
def f27cx_f27_capex_content_spend_cxppnemom_63d_slope_v049_signal(capex, ppnenet):
    b = _f27_intensity(capex, ppnenet)
    _b = b - b.shift(63)
    _d = (_b - _b.shift(10)) / 10.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope roc=42d of ncficonv_252d_base_v050_signal
def f27cx_f27_capex_content_spend_ncficonv_252d_slope_v050_signal(ncfi, assets):
    b = _f27_invest_intensity(ncfi, assets)
    d = b - _mean(b, 252)
    _b = np.sign(d) * (d ** 2)
    _d = (_b - _b.shift(42)) / 42.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope roc=42d of netbuildvol_252d_base_v051_signal
def f27cx_f27_capex_content_spend_netbuildvol_252d_slope_v051_signal(capex, depamor, assets):
    net = (_f27_spend(capex) - depamor) / assets.replace(0, np.nan)
    _b = _std(net, 252)
    _d = (_b - _b.shift(42)) / 42.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope roc=42d of cxdeplogspr_252d_base_v052_signal
def f27cx_f27_capex_content_spend_cxdeplogspr_252d_slope_v052_signal(capex, depamor):
    b = _f27_capex_vs_depamor(capex, depamor)
    s = _mean(b, 63)
    l = _mean(b, 252)
    _b = np.log(s.replace(0, np.nan) / l.replace(0, np.nan))
    _d = (_b - _b.shift(42)) / 42.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope roc=42d of cxdrawdown_252d_base_v053_signal
def f27cx_f27_capex_content_spend_cxdrawdown_252d_slope_v053_signal(capex):
    sp = _f27_spend(capex)
    peak = _rmax(sp, 252)
    _b = sp / peak.replace(0, np.nan) - 1.0
    _d = (_b - _b.shift(42)) / 42.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope roc=42d of cxrecov_252d_base_v054_signal
def f27cx_f27_capex_content_spend_cxrecov_252d_slope_v054_signal(capex):
    sp = _f27_spend(capex)
    trough = _rmin(sp, 252)
    _b = sp / trough.replace(0, np.nan) - 1.0
    _d = (_b - _b.shift(42)) / 42.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope roc=42d of cxdeprngpos_252d_base_v055_signal
def f27cx_f27_capex_content_spend_cxdeprngpos_252d_slope_v055_signal(capex, depamor):
    b = _f27_capex_vs_depamor(capex, depamor)
    hi = _rmax(b, 252)
    lo = _rmin(b, 252)
    _b = (b - lo) / (hi - lo).replace(0, np.nan) - 0.5
    _d = (_b - _b.shift(42)) / 42.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope roc=42d of ncfipull_252d_base_v056_signal
def f27cx_f27_capex_content_spend_ncfipull_252d_slope_v056_signal(ncfi, assets):
    b = _f27_invest_intensity(ncfi, assets)
    peak = _rmax(b, 252)
    _b = b / peak.replace(0, np.nan) - 1.0
    _d = (_b - _b.shift(42)) / 42.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope roc=42d of ncfidisp_252d_base_v057_signal
def f27cx_f27_capex_content_spend_ncfidisp_252d_slope_v057_signal(ncfi, assets):
    b = _f27_invest_intensity(ncfi, assets)
    _b = b - b.ewm(span=189, min_periods=63).mean()
    _d = (_b - _b.shift(42)) / 42.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope roc=21d of cxcv_126d_base_v058_signal
def f27cx_f27_capex_content_spend_cxcv_126d_slope_v058_signal(capex):
    sp = _f27_spend(capex)
    _b = _std(sp, 126) / _mean(sp, 126).replace(0, np.nan)
    _d = (_b - _b.shift(21)) / 21.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope roc=21d of netbuildaccel_126d_base_v059_signal
def f27cx_f27_capex_content_spend_netbuildaccel_126d_slope_v059_signal(capex, depamor, assets):
    net = (_f27_spend(capex) - depamor) / assets.replace(0, np.nan)
    g = net - net.shift(126)
    _b = g - g.shift(126)
    _d = (_b - _b.shift(21)) / 21.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope roc=42d of cxppnedisp_252d_base_v060_signal
def f27cx_f27_capex_content_spend_cxppnedisp_252d_slope_v060_signal(capex, ppnenet):
    b = _f27_intensity(capex, ppnenet)
    _b = b - b.ewm(span=189, min_periods=63).mean()
    _d = (_b - _b.shift(42)) / 42.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope roc=63d of cxassetsdrift_504d_base_v061_signal
def f27cx_f27_capex_content_spend_cxassetsdrift_504d_slope_v061_signal(capex, assets):
    b = _f27_intensity(capex, assets)
    _b = b - b.shift(504)
    _d = (_b - _b.shift(63)) / 63.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope roc=42d of cxdepppnez_252d_base_v062_signal
def f27cx_f27_capex_content_spend_cxdepppnez_252d_slope_v062_signal(capex, depamor, ppnenet):
    d = _f27_capex_vs_depamor(capex, depamor)
    p = _f27_intensity(capex, ppnenet)
    _b = _z(d, 252) - _z(p, 252)
    _d = (_b - _b.shift(42)) / 42.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope roc=42d of cxefficiency_252d_base_v063_signal
def f27cx_f27_capex_content_spend_cxefficiency_252d_slope_v063_signal(capex):
    sp = np.log(_f27_spend(capex).replace(0, np.nan))
    net = (sp - sp.shift(252)).abs()
    path = sp.diff().abs().rolling(252, min_periods=126).sum()
    _b = net / path.replace(0, np.nan)
    _d = (_b - _b.shift(42)) / 42.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope roc=63d of ncfirank_504d_base_v064_signal
def f27cx_f27_capex_content_spend_ncfirank_504d_slope_v064_signal(ncfi, assets):
    b = _f27_invest_intensity(ncfi, assets)
    _b = _rank(b, 504)
    _d = (_b - _b.shift(63)) / 63.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope roc=63d of netinvrank_504d_base_v065_signal
def f27cx_f27_capex_content_spend_netinvrank_504d_slope_v065_signal(capex, depamor, assets):
    net = (_f27_spend(capex) - depamor) / assets.replace(0, np.nan)
    _b = _rank(net, 504)
    _d = (_b - _b.shift(63)) / 63.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope roc=42d of cxdualbase_252d_base_v066_signal
def f27cx_f27_capex_content_spend_cxdualbase_252d_slope_v066_signal(capex, depamor, assets):
    d = _f27_capex_vs_depamor(capex, depamor)
    a = _f27_intensity(capex, assets)
    # de-trend each via z so the difference is scale-comparable
    _b = _z(d, 252) - _z(a, 252)
    _d = (_b - _b.shift(42)) / 42.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope roc=42d of cxdeptrend_252d_base_v067_signal
def f27cx_f27_capex_content_spend_cxdeptrend_252d_slope_v067_signal(capex, depamor):
    b = _f27_capex_vs_depamor(capex, depamor)
    sm = _mean(b, 126)
    _b = sm - sm.shift(63)
    _d = (_b - _b.shift(42)) / 42.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope roc=42d of cxassetsstab_252d_base_v068_signal
def f27cx_f27_capex_content_spend_cxassetsstab_252d_slope_v068_signal(capex, assets):
    b = _f27_intensity(capex, assets)
    _b = _mean(b, 252) / _std(b, 252).replace(0, np.nan)
    _d = (_b - _b.shift(42)) / 42.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope roc=42d of invcompdrift_252d_base_v069_signal
def f27cx_f27_capex_content_spend_invcompdrift_252d_slope_v069_signal(ncfi, capex):
    out = (-ncfi)
    sp = _f27_spend(capex)
    share = (out - sp) / out.replace(0, np.nan)
    _b = share - share.shift(252)
    _d = (_b - _b.shift(42)) / 42.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope roc=42d of cxppnestab_252d_base_v070_signal
def f27cx_f27_capex_content_spend_cxppnestab_252d_slope_v070_signal(capex, ppnenet):
    b = _f27_intensity(capex, ppnenet)
    _b = _mean(b, 252) / _std(b, 252).replace(0, np.nan)
    _d = (_b - _b.shift(42)) / 42.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope roc=42d of cxassetsvolratio_252d_base_v071_signal
def f27cx_f27_capex_content_spend_cxassetsvolratio_252d_slope_v071_signal(capex, assets):
    b = _f27_intensity(capex, assets)
    _b = _std(b, 63) / _std(b, 252).replace(0, np.nan)
    _d = (_b - _b.shift(42)) / 42.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope roc=42d of netinvppnez_252d_base_v072_signal
def f27cx_f27_capex_content_spend_netinvppnez_252d_slope_v072_signal(capex, depamor, ppnenet):
    net = (_f27_spend(capex) - depamor) / ppnenet.replace(0, np.nan)
    _b = _z(net, 252)
    _d = (_b - _b.shift(42)) / 42.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope roc=42d of cxdepconv_252d_base_v073_signal
def f27cx_f27_capex_content_spend_cxdepconv_252d_slope_v073_signal(capex, depamor):
    b = _f27_capex_vs_depamor(capex, depamor)
    d = b - _mean(b, 252)
    _b = np.sign(d) * (d ** 2)
    _d = (_b - _b.shift(42)) / 42.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope roc=42d of invdivz_252d_base_v074_signal
def f27cx_f27_capex_content_spend_invdivz_252d_slope_v074_signal(ncfi, capex, assets):
    inv = _f27_invest_intensity(ncfi, assets)
    cx = _f27_intensity(capex, assets)
    _b = _z(inv, 252) - _z(cx, 252)
    _d = (_b - _b.shift(42)) / 42.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope roc=42d of ncfixover_252d_base_v075_signal
def f27cx_f27_capex_content_spend_ncfixover_252d_slope_v075_signal(ncfi, assets):
    b = _f27_invest_intensity(ncfi, assets)
    fast = b.ewm(span=63, min_periods=21).mean()
    slow = b.ewm(span=252, min_periods=63).mean()
    _b = np.tanh((fast - slow) / slow.abs().replace(0, np.nan))
    _d = (_b - _b.shift(42)) / 42.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope roc=21d of cxassets126_base_v076_signal
def f27cx_f27_capex_content_spend_cxassets126_slope_v076_signal(capex, assets):
    b = _f27_intensity(capex, assets)
    _b = _mean(b, 126)
    _d = (_b - _b.shift(21)) / 21.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope roc=21d of cxdep126_base_v077_signal
def f27cx_f27_capex_content_spend_cxdep126_slope_v077_signal(capex, depamor):
    b = _f27_capex_vs_depamor(capex, depamor)
    _b = _mean(b, 126)
    _d = (_b - _b.shift(21)) / 21.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope roc=21d of cxppnez126_base_v078_signal
def f27cx_f27_capex_content_spend_cxppnez126_slope_v078_signal(capex, ppnenet):
    b = _f27_intensity(capex, ppnenet)
    _b = _z(b, 126)
    _d = (_b - _b.shift(21)) / 21.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope roc=42d of ncfippne_252d_base_v079_signal
def f27cx_f27_capex_content_spend_ncfippne_252d_slope_v079_signal(ncfi, ppnenet):
    b = _f27_invest_intensity(ncfi, ppnenet)
    _b = _mean(b, 252)
    _d = (_b - _b.shift(42)) / 42.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope roc=42d of ncfidepz_252d_base_v080_signal
def f27cx_f27_capex_content_spend_ncfidepz_252d_slope_v080_signal(ncfi, depamor):
    b = _f27_invest_intensity(ncfi, depamor)
    _b = _z(b, 252)
    _d = (_b - _b.shift(42)) / 42.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope roc=10d of cxgrow63_base_v081_signal
def f27cx_f27_capex_content_spend_cxgrow63_slope_v081_signal(capex):
    sp = _f27_spend(capex)
    _b = _f27_growth(sp, 63)
    _d = (_b - _b.shift(10)) / 10.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope roc=63d of cxloggrow504_base_v082_signal
def f27cx_f27_capex_content_spend_cxloggrow504_slope_v082_signal(capex):
    sp = _f27_spend(capex)
    _b = _f27_loggrowth(sp, 504)
    _d = (_b - _b.shift(63)) / 63.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope roc=63d of cxassetsyoyrank_504d_base_v083_signal
def f27cx_f27_capex_content_spend_cxassetsyoyrank_504d_slope_v083_signal(capex, assets):
    b = _f27_intensity(capex, assets)
    yoy = b - b.shift(252)
    _b = _rank(yoy, 504)
    _d = (_b - _b.shift(63)) / 63.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope roc=42d of cxdepmedtiltrank_252d_base_v084_signal
def f27cx_f27_capex_content_spend_cxdepmedtiltrank_252d_slope_v084_signal(capex, depamor):
    b = _f27_capex_vs_depamor(capex, depamor)
    tilt = b - _mean(b, 126)
    _b = _rank(tilt, 252)
    _d = (_b - _b.shift(42)) / 42.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope roc=42d of cxinvsharez_252d_base_v085_signal
def f27cx_f27_capex_content_spend_cxinvsharez_252d_slope_v085_signal(capex, ncfi):
    sp = _f27_spend(capex)
    out = (-ncfi)
    share = sp / out.replace(0, np.nan)
    _b = _z(share, 252)
    _d = (_b - _b.shift(42)) / 42.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope roc=21d of cxppnecurv_base_v086_signal
def f27cx_f27_capex_content_spend_cxppnecurv_slope_v086_signal(capex, ppnenet):
    b = _f27_intensity(capex, ppnenet)
    _b = (b - b.shift(126)) - (b - b.shift(63))
    _d = (_b - _b.shift(21)) / 21.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope roc=21d of cxvsppnegrow_126d_base_v087_signal
def f27cx_f27_capex_content_spend_cxvsppnegrow_126d_slope_v087_signal(capex, ppnenet):
    sp = _f27_spend(capex)
    _b = _f27_growth(sp, 126) - _f27_growth(ppnenet, 126)
    _d = (_b - _b.shift(21)) / 21.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope roc=42d of otherinvdepz_252d_base_v088_signal
def f27cx_f27_capex_content_spend_otherinvdepz_252d_slope_v088_signal(ncfi, capex, depamor):
    other = ((-ncfi) - _f27_spend(capex)) / depamor.replace(0, np.nan)
    _b = _z(other, 252)
    _d = (_b - _b.shift(42)) / 42.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope roc=21d of cxassetsconv126_base_v089_signal
def f27cx_f27_capex_content_spend_cxassetsconv126_slope_v089_signal(capex, assets):
    b = _f27_intensity(capex, assets)
    d = b - _mean(b, 126)
    _b = np.sign(d) * (d ** 2)
    _d = (_b - _b.shift(21)) / 21.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope roc=42d of cxdepregfrac_252d_base_v090_signal
def f27cx_f27_capex_content_spend_cxdepregfrac_252d_slope_v090_signal(capex, depamor):
    b = _f27_capex_vs_depamor(capex, depamor)
    med = b.rolling(252, min_periods=126).median()
    above = (b > med).astype(float)
    _b = above.rolling(126, min_periods=63).mean() - 0.5
    _d = (_b - _b.shift(42)) / 42.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope roc=63d of cxdrawdown504_base_v091_signal
def f27cx_f27_capex_content_spend_cxdrawdown504_slope_v091_signal(capex):
    sp = _f27_spend(capex)
    peak = _rmax(sp, 504)
    _b = sp / peak.replace(0, np.nan) - 1.0
    _d = (_b - _b.shift(63)) / 63.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope roc=63d of cxrecov504_base_v092_signal
def f27cx_f27_capex_content_spend_cxrecov504_slope_v092_signal(capex):
    sp = _f27_spend(capex)
    trough = _rmin(sp, 504)
    _b = sp / trough.replace(0, np.nan) - 1.0
    _d = (_b - _b.shift(63)) / 63.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope roc=63d of cxassetsrngpos_504d_base_v093_signal
def f27cx_f27_capex_content_spend_cxassetsrngpos_504d_slope_v093_signal(capex, assets):
    b = _f27_intensity(capex, assets)
    hi = _rmax(b, 504)
    lo = _rmin(b, 504)
    _b = (b - lo) / (hi - lo).replace(0, np.nan) - 0.5
    _d = (_b - _b.shift(63)) / 63.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope roc=42d of ncfirngpos_252d_base_v094_signal
def f27cx_f27_capex_content_spend_ncfirngpos_252d_slope_v094_signal(ncfi, assets):
    b = _f27_invest_intensity(ncfi, assets)
    hi = _rmax(b, 252)
    lo = _rmin(b, 252)
    _b = (b - lo) / (hi - lo).replace(0, np.nan) - 0.5
    _d = (_b - _b.shift(42)) / 42.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope roc=21d of cxdepdisp126_base_v095_signal
def f27cx_f27_capex_content_spend_cxdepdisp126_slope_v095_signal(capex, depamor):
    b = _f27_capex_vs_depamor(capex, depamor)
    _b = _std(b, 126)
    _d = (_b - _b.shift(21)) / 21.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope roc=63d of cxcvrank_504d_base_v096_signal
def f27cx_f27_capex_content_spend_cxcvrank_504d_slope_v096_signal(capex):
    sp = _f27_spend(capex)
    cv = _std(sp, 126) / _mean(sp, 126).replace(0, np.nan)
    _b = _rank(cv, 504)
    _d = (_b - _b.shift(63)) / 63.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope roc=21d of cxinvgapdepz_126d_base_v097_signal
def f27cx_f27_capex_content_spend_cxinvgapdepz_126d_slope_v097_signal(capex, ncfi, depamor):
    gap = (_f27_spend(capex) - (-ncfi)) / depamor.replace(0, np.nan)
    _b = _z(gap, 126)
    _d = (_b - _b.shift(21)) / 21.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope roc=42d of cxdepema252disp_base_v098_signal
def f27cx_f27_capex_content_spend_cxdepema252disp_slope_v098_signal(capex, depamor):
    b = _f27_capex_vs_depamor(capex, depamor)
    _b = b - b.ewm(span=252, min_periods=63).mean()
    _d = (_b - _b.shift(42)) / 42.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope roc=10d of cxassetsmom_63d_base_v099_signal
def f27cx_f27_capex_content_spend_cxassetsmom_63d_slope_v099_signal(capex, assets):
    b = _f27_intensity(capex, assets)
    _b = b - b.shift(63)
    _d = (_b - _b.shift(10)) / 10.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope roc=42d of cxgrowaccel_252d_base_v100_signal
def f27cx_f27_capex_content_spend_cxgrowaccel_252d_slope_v100_signal(capex):
    sp = _f27_spend(capex)
    g = _f27_growth(sp, 252)
    _b = g - g.shift(252)
    _d = (_b - _b.shift(42)) / 42.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope roc=42d of ncfiaccel_252d_base_v101_signal
def f27cx_f27_capex_content_spend_ncfiaccel_252d_slope_v101_signal(ncfi, assets):
    b = _f27_invest_intensity(ncfi, assets)
    g = b - b.shift(126)
    _b = g - g.shift(126)
    _d = (_b - _b.shift(42)) / 42.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope roc=21d of cxppnestab126_base_v102_signal
def f27cx_f27_capex_content_spend_cxppnestab126_slope_v102_signal(capex, ppnenet):
    b = _f27_intensity(capex, ppnenet)
    _b = _mean(b, 126) / _std(b, 126).replace(0, np.nan)
    _d = (_b - _b.shift(21)) / 21.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope roc=21d of ncfifastturn_base_v103_signal
def f27cx_f27_capex_content_spend_ncfifastturn_slope_v103_signal(ncfi, assets):
    b = _f27_invest_intensity(ncfi, assets)
    fast = b.ewm(span=21, min_periods=10).mean()
    slow = b.ewm(span=126, min_periods=42).mean()
    _b = np.tanh((fast - slow) / slow.abs().replace(0, np.nan))
    _d = (_b - _b.shift(21)) / 21.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope roc=42d of cxassetsrank_252d_base_v104_signal
def f27cx_f27_capex_content_spend_cxassetsrank_252d_slope_v104_signal(capex, assets):
    b = _f27_intensity(capex, assets)
    _b = _rank(b, 252)
    _d = (_b - _b.shift(42)) / 42.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope roc=10d of cxppneassetmom_63d_base_v105_signal
def f27cx_f27_capex_content_spend_cxppneassetmom_63d_slope_v105_signal(capex, ppnenet, assets):
    p = _z(_f27_intensity(capex, ppnenet), 252)
    a = _z(_f27_intensity(capex, assets), 252)
    spread = p - a
    _b = spread - spread.shift(63)
    _d = (_b - _b.shift(10)) / 10.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope roc=42d of netinvppnerank_252d_base_v106_signal
def f27cx_f27_capex_content_spend_netinvppnerank_252d_slope_v106_signal(capex, depamor, ppnenet):
    net = (_f27_spend(capex) - depamor) / ppnenet.replace(0, np.nan)
    _b = _rank(net, 252)
    _d = (_b - _b.shift(42)) / 42.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope roc=21d of cxasym126_base_v107_signal
def f27cx_f27_capex_content_spend_cxasym126_slope_v107_signal(capex):
    sp = _f27_spend(capex)
    m = _mean(sp, 126)
    med = sp.rolling(126, min_periods=63).median()
    sd = _std(sp, 126)
    _b = (m - med) / sd.replace(0, np.nan)
    _d = (_b - _b.shift(21)) / 21.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope roc=42d of cxassetseff_252d_base_v108_signal
def f27cx_f27_capex_content_spend_cxassetseff_252d_slope_v108_signal(capex, assets):
    b = _f27_intensity(capex, assets)
    net = (b - b.shift(252)).abs()
    path = b.diff().abs().rolling(252, min_periods=126).sum()
    _b = net / path.replace(0, np.nan)
    _d = (_b - _b.shift(42)) / 42.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope roc=42d of ncfidisp252_base_v109_signal
def f27cx_f27_capex_content_spend_ncfidisp252_slope_v109_signal(ncfi, assets):
    b = _f27_invest_intensity(ncfi, assets)
    _b = _std(b, 252)
    _d = (_b - _b.shift(42)) / 42.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope roc=10d of ncfippnepulse_63d_base_v110_signal
def f27cx_f27_capex_content_spend_ncfippnepulse_63d_slope_v110_signal(ncfi, ppnenet):
    b = _f27_invest_intensity(ncfi, ppnenet)
    _b = b - b.ewm(span=63, min_periods=21).mean()
    _d = (_b - _b.shift(10)) / 10.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope roc=42d of cxburstrank_252d_base_v111_signal
def f27cx_f27_capex_content_spend_cxburstrank_252d_slope_v111_signal(capex):
    sp = _f27_spend(capex)
    ratio = sp / _mean(sp, 126).replace(0, np.nan)
    _b = _rank(ratio, 252)
    _d = (_b - _b.shift(42)) / 42.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope roc=42d of cxppneconv_252d_base_v112_signal
def f27cx_f27_capex_content_spend_cxppneconv_252d_slope_v112_signal(capex, ppnenet):
    b = _f27_intensity(capex, ppnenet)
    d = b - _mean(b, 252)
    _b = np.sign(d) * (d ** 2)
    _d = (_b - _b.shift(42)) / 42.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope roc=10d of cxdepexcessmom_63d_base_v113_signal
def f27cx_f27_capex_content_spend_cxdepexcessmom_63d_slope_v113_signal(capex, depamor):
    b = _f27_capex_vs_depamor(capex, depamor) - 1.0
    sm = _mean(b, 126)
    _b = sm - sm.shift(63)
    _d = (_b - _b.shift(10)) / 10.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope roc=63d of cxassetsregime_504d_base_v114_signal
def f27cx_f27_capex_content_spend_cxassetsregime_504d_slope_v114_signal(capex, assets):
    b = _f27_intensity(capex, assets)
    _b = _mean(b, 252) - _mean(b, 504)
    _d = (_b - _b.shift(63)) / 63.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope roc=63d of ncfitilt_504d_base_v115_signal
def f27cx_f27_capex_content_spend_ncfitilt_504d_slope_v115_signal(ncfi, assets):
    b = _f27_invest_intensity(ncfi, assets)
    _b = b - _mean(b, 504)
    _d = (_b - _b.shift(63)) / 63.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope roc=21d of cxrevsizez_126d_base_v116_signal
def f27cx_f27_capex_content_spend_cxrevsizez_126d_slope_v116_signal(capex, revenue):
    sp = np.log(_f27_spend(capex).replace(0, np.nan))
    rv = np.log(revenue.replace(0, np.nan))
    _b = _z(sp - rv, 126)
    _d = (_b - _b.shift(21)) / 21.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope roc=42d of cxdeprank_252d_base_v117_signal
def f27cx_f27_capex_content_spend_cxdeprank_252d_slope_v117_signal(capex, depamor):
    b = _f27_capex_vs_depamor(capex, depamor)
    _b = _rank(b, 252)
    _d = (_b - _b.shift(42)) / 42.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope roc=21d of cxassetsaccel_126d_base_v118_signal
def f27cx_f27_capex_content_spend_cxassetsaccel_126d_slope_v118_signal(capex, assets):
    b = _f27_intensity(capex, assets)
    sm = _mean(b, 126)
    g = sm - sm.shift(126)
    _b = g - g.shift(126)
    _d = (_b - _b.shift(21)) / 21.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope roc=10d of cxppnepulse_63d_base_v119_signal
def f27cx_f27_capex_content_spend_cxppnepulse_63d_slope_v119_signal(capex, ppnenet):
    b = _f27_intensity(capex, ppnenet)
    _b = b - b.ewm(span=63, min_periods=21).mean()
    _d = (_b - _b.shift(10)) / 10.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope roc=42d of netinveff_252d_base_v120_signal
def f27cx_f27_capex_content_spend_netinveff_252d_slope_v120_signal(capex, depamor, assets):
    net = (_f27_spend(capex) - depamor) / assets.replace(0, np.nan)
    num = (net - net.shift(252)).abs()
    path = net.diff().abs().rolling(252, min_periods=126).sum()
    _b = num / path.replace(0, np.nan)
    _d = (_b - _b.shift(42)) / 42.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope roc=21d of cxgrowshape_base_v121_signal
def f27cx_f27_capex_content_spend_cxgrowshape_slope_v121_signal(capex):
    sp = _f27_spend(capex)
    _b = _f27_growth(sp, 126) - _f27_growth(sp, 63)
    _d = (_b - _b.shift(21)) / 21.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope roc=42d of cxdepamp_252d_base_v122_signal
def f27cx_f27_capex_content_spend_cxdepamp_252d_slope_v122_signal(capex, depamor):
    b = _f27_capex_vs_depamor(capex, depamor)
    hi = _rmax(b, 252)
    lo = _rmin(b, 252)
    _b = (hi - lo) / _mean(b, 252).replace(0, np.nan)
    _d = (_b - _b.shift(42)) / 42.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope roc=42d of cxassetsamp_252d_base_v123_signal
def f27cx_f27_capex_content_spend_cxassetsamp_252d_slope_v123_signal(capex, assets):
    b = _f27_intensity(capex, assets)
    hi = _rmax(b, 252)
    lo = _rmin(b, 252)
    _b = (hi - lo) / _mean(b, 252).replace(0, np.nan)
    _d = (_b - _b.shift(42)) / 42.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope roc=42d of cxdeproot_252d_base_v124_signal
def f27cx_f27_capex_content_spend_cxdeproot_252d_slope_v124_signal(capex, depamor):
    sp = _f27_spend(capex)
    d = depamor
    diff = (sp - d) / (sp + d).replace(0, np.nan)
    _b = np.sign(diff) * (diff.abs() ** 0.5)
    _d = (_b - _b.shift(42)) / 42.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope roc=42d of invcxdepz_252d_base_v125_signal
def f27cx_f27_capex_content_spend_invcxdepz_252d_slope_v125_signal(ncfi, capex, depamor):
    inv = _f27_invest_intensity(ncfi, depamor)
    cx = _f27_capex_vs_depamor(capex, depamor)
    _b = _z(inv, 252) - _z(cx, 252)
    _d = (_b - _b.shift(42)) / 42.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope roc=21d of cxdepcurv_base_v126_signal
def f27cx_f27_capex_content_spend_cxdepcurv_slope_v126_signal(capex, depamor):
    b = _f27_capex_vs_depamor(capex, depamor)
    _b = (b - b.shift(126)) - (b - b.shift(63))
    _d = (_b - _b.shift(21)) / 21.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope roc=63d of cxdepeff_504d_base_v127_signal
def f27cx_f27_capex_content_spend_cxdepeff_504d_slope_v127_signal(capex, depamor):
    b = _f27_capex_vs_depamor(capex, depamor)
    num = (b - b.shift(504)).abs()
    path = b.diff().abs().rolling(504, min_periods=252).sum()
    _b = num / path.replace(0, np.nan)
    _d = (_b - _b.shift(63)) / 63.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope roc=63d of cxcyclerank_504d_base_v128_signal
def f27cx_f27_capex_content_spend_cxcyclerank_504d_slope_v128_signal(capex):
    sp = _f27_spend(capex)
    cyc = _mean(sp, 63) / _mean(sp, 252).replace(0, np.nan)
    _b = _rank(cyc, 504)
    _d = (_b - _b.shift(63)) / 63.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope roc=42d of otherinvz_252d_base_v129_signal
def f27cx_f27_capex_content_spend_otherinvz_252d_slope_v129_signal(ncfi, capex, assets):
    inv = _f27_invest_intensity(ncfi, assets)
    cx = _f27_intensity(capex, assets)
    _b = _z(inv - cx, 252)
    _d = (_b - _b.shift(42)) / 42.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope roc=63d of cxppnedrift_504d_base_v130_signal
def f27cx_f27_capex_content_spend_cxppnedrift_504d_slope_v130_signal(capex, ppnenet):
    b = _f27_intensity(capex, ppnenet)
    _b = b - b.shift(504)
    _d = (_b - _b.shift(63)) / 63.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope roc=42d of amortbuildgap_252d_base_v131_signal
def f27cx_f27_capex_content_spend_amortbuildgap_252d_slope_v131_signal(depamor, capex, ppnenet):
    amort = depamor / ppnenet.replace(0, np.nan)
    build = _f27_intensity(capex, ppnenet)
    _b = _mean(amort - build, 252)
    _d = (_b - _b.shift(42)) / 42.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope roc=10d of cxassetspulse_63d_base_v132_signal
def f27cx_f27_capex_content_spend_cxassetspulse_63d_slope_v132_signal(capex, assets):
    b = _f27_intensity(capex, assets)
    _b = b - b.ewm(span=63, min_periods=21).mean()
    _d = (_b - _b.shift(10)) / 10.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope roc=21d of cxburstpers126_base_v133_signal
def f27cx_f27_capex_content_spend_cxburstpers126_slope_v133_signal(capex):
    sp = _f27_spend(capex)
    dev = sp / _mean(sp, 126).replace(0, np.nan) - 1.0
    _b = dev.rolling(63, min_periods=21).mean()
    _d = (_b - _b.shift(21)) / 21.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope roc=63d of cxdepz_504d_base_v134_signal
def f27cx_f27_capex_content_spend_cxdepz_504d_slope_v134_signal(capex, depamor):
    b = _f27_capex_vs_depamor(capex, depamor)
    _b = _z(b, 504)
    _d = (_b - _b.shift(63)) / 63.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope roc=21d of ncfiz_126d_base_v135_signal
def f27cx_f27_capex_content_spend_ncfiz_126d_slope_v135_signal(ncfi, assets):
    b = _f27_invest_intensity(ncfi, assets)
    _b = _z(b, 126)
    _d = (_b - _b.shift(21)) / 21.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope roc=42d of cxdepvsassetintgrow_252d_base_v136_signal
def f27cx_f27_capex_content_spend_cxdepvsassetintgrow_252d_slope_v136_signal(capex, depamor, assets):
    d = _f27_capex_vs_depamor(capex, depamor)
    a = _f27_intensity(capex, assets)
    _b = _f27_growth(d, 252) - _f27_growth(a, 252)
    _d = (_b - _b.shift(42)) / 42.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope roc=63d of cxppneregfrac_504d_base_v137_signal
def f27cx_f27_capex_content_spend_cxppneregfrac_504d_slope_v137_signal(capex, ppnenet):
    b = _f27_intensity(capex, ppnenet)
    med = b.rolling(504, min_periods=252).median()
    above = (b > med).astype(float)
    _b = above.rolling(252, min_periods=126).mean() - 0.5
    _d = (_b - _b.shift(63)) / 63.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope roc=21d of cxdrawdown126_base_v138_signal
def f27cx_f27_capex_content_spend_cxdrawdown126_slope_v138_signal(capex):
    sp = _f27_spend(capex)
    peak = _rmax(sp, 126)
    _b = sp / peak.replace(0, np.nan) - 1.0
    _d = (_b - _b.shift(21)) / 21.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope roc=63d of cxdeprngpos_504d_base_v139_signal
def f27cx_f27_capex_content_spend_cxdeprngpos_504d_slope_v139_signal(capex, depamor):
    b = _f27_capex_vs_depamor(capex, depamor)
    hi = _rmax(b, 504)
    lo = _rmin(b, 504)
    _b = (b - lo) / (hi - lo).replace(0, np.nan) - 0.5
    _d = (_b - _b.shift(63)) / 63.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope roc=21d of cxassetsstab126_base_v140_signal
def f27cx_f27_capex_content_spend_cxassetsstab126_slope_v140_signal(capex, assets):
    b = _f27_intensity(capex, assets)
    _b = _mean(b, 126) / _std(b, 126).replace(0, np.nan)
    _d = (_b - _b.shift(21)) / 21.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope roc=63d of cxstepmag_504d_base_v141_signal
def f27cx_f27_capex_content_spend_cxstepmag_504d_slope_v141_signal(capex):
    sp = _f27_spend(capex)
    step = (sp / sp.shift(63).replace(0, np.nan) - 1.0).abs()
    _b = step.rolling(504, min_periods=252).mean()
    _d = (_b - _b.shift(63)) / 63.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope roc=42d of cxinvsharerank_252d_base_v142_signal
def f27cx_f27_capex_content_spend_cxinvsharerank_252d_slope_v142_signal(capex, ncfi):
    sp = _f27_spend(capex)
    out = (-ncfi)
    share = sp / out.replace(0, np.nan)
    _b = _rank(share, 252)
    _d = (_b - _b.shift(42)) / 42.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope roc=10d of cxdualbasemom_63d_base_v143_signal
def f27cx_f27_capex_content_spend_cxdualbasemom_63d_slope_v143_signal(capex, depamor, assets):
    d = _z(_f27_capex_vs_depamor(capex, depamor), 252)
    a = _z(_f27_intensity(capex, assets), 252)
    spread = d - a
    _b = spread - spread.shift(63)
    _d = (_b - _b.shift(10)) / 10.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope roc=21d of ncfimedtilt_126d_base_v144_signal
def f27cx_f27_capex_content_spend_ncfimedtilt_126d_slope_v144_signal(ncfi, assets):
    b = _f27_invest_intensity(ncfi, assets)
    _b = b - _mean(b, 126)
    _d = (_b - _b.shift(21)) / 21.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope roc=21d of cxassetsbursttanh126_base_v145_signal
def f27cx_f27_capex_content_spend_cxassetsbursttanh126_slope_v145_signal(capex, assets):
    b = _f27_intensity(capex, assets)
    ratio = b / _mean(b, 126).replace(0, np.nan) - 1.0
    _b = np.tanh(3.0 * ratio)
    _d = (_b - _b.shift(21)) / 21.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope roc=63d of cxdepamprank_504d_base_v146_signal
def f27cx_f27_capex_content_spend_cxdepamprank_504d_slope_v146_signal(capex, depamor):
    b = _f27_capex_vs_depamor(capex, depamor)
    amp = (_rmax(b, 252) - _rmin(b, 252)) / _mean(b, 252).replace(0, np.nan)
    _b = _rank(amp, 504)
    _d = (_b - _b.shift(63)) / 63.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope roc=63d of netinvppnetilt_504d_base_v147_signal
def f27cx_f27_capex_content_spend_netinvppnetilt_504d_slope_v147_signal(capex, depamor, ppnenet):
    net = (_f27_spend(capex) - depamor) / ppnenet.replace(0, np.nan)
    _b = net - _mean(net, 504)
    _d = (_b - _b.shift(63)) / 63.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope roc=21d of cxassetslogspr_126d_base_v148_signal
def f27cx_f27_capex_content_spend_cxassetslogspr_126d_slope_v148_signal(capex, assets):
    b = _f27_intensity(capex, assets)
    s = _mean(b, 63)
    l = _mean(b, 126)
    _b = np.log(s.replace(0, np.nan) / l.replace(0, np.nan))
    _d = (_b - _b.shift(21)) / 21.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope roc=42d of ncfieff_252d_base_v149_signal
def f27cx_f27_capex_content_spend_ncfieff_252d_slope_v149_signal(ncfi, assets):
    b = _f27_invest_intensity(ncfi, assets)
    num = (b - b.shift(252)).abs()
    path = b.diff().abs().rolling(252, min_periods=126).sum()
    _b = num / path.replace(0, np.nan)
    _d = (_b - _b.shift(42)) / 42.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope roc=21d of cxppnefastcycle_base_v150_signal
def f27cx_f27_capex_content_spend_cxppnefastcycle_slope_v150_signal(capex, ppnenet):
    b = _f27_intensity(capex, ppnenet)
    _b = _mean(b, 21) / _mean(b, 126).replace(0, np.nan) - 1.0
    _d = (_b - _b.shift(21)) / 21.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f27cx_f27_capex_content_spend_cxassetstilt_504d_slope_v001_signal,
    f27cx_f27_capex_content_spend_cxassetsz_504d_slope_v002_signal,
    f27cx_f27_capex_content_spend_cxdep_252d_slope_v003_signal,
    f27cx_f27_capex_content_spend_cxdeptilt_504d_slope_v004_signal,
    f27cx_f27_capex_content_spend_cxppne_252d_slope_v005_signal,
    f27cx_f27_capex_content_spend_cxppnez_252d_slope_v006_signal,
    f27cx_f27_capex_content_spend_ncfiassets_252d_slope_v007_signal,
    f27cx_f27_capex_content_spend_ncfiassetsz_504d_slope_v008_signal,
    f27cx_f27_capex_content_spend_cxgrow_252d_slope_v009_signal,
    f27cx_f27_capex_content_spend_cxloggrow_126d_slope_v010_signal,
    f27cx_f27_capex_content_spend_cxburst_252d_slope_v011_signal,
    f27cx_f27_capex_content_spend_cxcv_252d_slope_v012_signal,
    f27cx_f27_capex_content_spend_cxbasewedge_252d_slope_v013_signal,
    f27cx_f27_capex_content_spend_cxdepbalmom_63d_slope_v014_signal,
    f27cx_f27_capex_content_spend_noncxinv_504d_slope_v015_signal,
    f27cx_f27_capex_content_spend_cxassetsrank_504d_slope_v016_signal,
    f27cx_f27_capex_content_spend_cxdeprank_504d_slope_v017_signal,
    f27cx_f27_capex_content_spend_cxaccel_126d_slope_v018_signal,
    f27cx_f27_capex_content_spend_depcxshareaccel_63d_slope_v019_signal,
    f27cx_f27_capex_content_spend_cxassetsspr_63v252_slope_v020_signal,
    f27cx_f27_capex_content_spend_cxppnespr_63v252_slope_v021_signal,
    f27cx_f27_capex_content_spend_cxinvshare_252d_slope_v022_signal,
    f27cx_f27_capex_content_spend_netinvassets_504d_slope_v023_signal,
    f27cx_f27_capex_content_spend_cxassetsyoy_252d_slope_v024_signal,
    f27cx_f27_capex_content_spend_cxdepyoy_252d_slope_v025_signal,
    f27cx_f27_capex_content_spend_ncfistreak_252d_slope_v026_signal,
    f27cx_f27_capex_content_spend_cxstepmag_252d_slope_v027_signal,
    f27cx_f27_capex_content_spend_cxconc_252d_slope_v028_signal,
    f27cx_f27_capex_content_spend_otherinv_252d_slope_v029_signal,
    f27cx_f27_capex_content_spend_cxdepregfrac_504d_slope_v030_signal,
    f27cx_f27_capex_content_spend_cxrevz_252d_slope_v031_signal,
    f27cx_f27_capex_content_spend_cxassetsconv_252d_slope_v032_signal,
    f27cx_f27_capex_content_spend_ncfispr_63v252_slope_v033_signal,
    f27cx_f27_capex_content_spend_cxdepdisp_ema_slope_v034_signal,
    f27cx_f27_capex_content_spend_cxassetsdisp_252d_slope_v035_signal,
    f27cx_f27_capex_content_spend_cxcycle_252d_slope_v036_signal,
    f27cx_f27_capex_content_spend_netinvppnerank_504d_slope_v037_signal,
    f27cx_f27_capex_content_spend_ncfiyoy_252d_slope_v038_signal,
    f27cx_f27_capex_content_spend_cxdepdisp_252d_slope_v039_signal,
    f27cx_f27_capex_content_spend_cxppnerank_504d_slope_v040_signal,
    f27cx_f27_capex_content_spend_cxburstrank_504d_slope_v041_signal,
    f27cx_f27_capex_content_spend_cxvsassetgrow_126d_slope_v042_signal,
    f27cx_f27_capex_content_spend_ppnevsdepgrow_252d_slope_v043_signal,
    f27cx_f27_capex_content_spend_invgap_252d_slope_v044_signal,
    f27cx_f27_capex_content_spend_cxassetszdist_504d_slope_v045_signal,
    f27cx_f27_capex_content_spend_buildstab_252d_slope_v046_signal,
    f27cx_f27_capex_content_spend_cxasym_252d_slope_v047_signal,
    f27cx_f27_capex_content_spend_cxppnereldrift_252d_slope_v048_signal,
    f27cx_f27_capex_content_spend_cxppnemom_63d_slope_v049_signal,
    f27cx_f27_capex_content_spend_ncficonv_252d_slope_v050_signal,
    f27cx_f27_capex_content_spend_netbuildvol_252d_slope_v051_signal,
    f27cx_f27_capex_content_spend_cxdeplogspr_252d_slope_v052_signal,
    f27cx_f27_capex_content_spend_cxdrawdown_252d_slope_v053_signal,
    f27cx_f27_capex_content_spend_cxrecov_252d_slope_v054_signal,
    f27cx_f27_capex_content_spend_cxdeprngpos_252d_slope_v055_signal,
    f27cx_f27_capex_content_spend_ncfipull_252d_slope_v056_signal,
    f27cx_f27_capex_content_spend_ncfidisp_252d_slope_v057_signal,
    f27cx_f27_capex_content_spend_cxcv_126d_slope_v058_signal,
    f27cx_f27_capex_content_spend_netbuildaccel_126d_slope_v059_signal,
    f27cx_f27_capex_content_spend_cxppnedisp_252d_slope_v060_signal,
    f27cx_f27_capex_content_spend_cxassetsdrift_504d_slope_v061_signal,
    f27cx_f27_capex_content_spend_cxdepppnez_252d_slope_v062_signal,
    f27cx_f27_capex_content_spend_cxefficiency_252d_slope_v063_signal,
    f27cx_f27_capex_content_spend_ncfirank_504d_slope_v064_signal,
    f27cx_f27_capex_content_spend_netinvrank_504d_slope_v065_signal,
    f27cx_f27_capex_content_spend_cxdualbase_252d_slope_v066_signal,
    f27cx_f27_capex_content_spend_cxdeptrend_252d_slope_v067_signal,
    f27cx_f27_capex_content_spend_cxassetsstab_252d_slope_v068_signal,
    f27cx_f27_capex_content_spend_invcompdrift_252d_slope_v069_signal,
    f27cx_f27_capex_content_spend_cxppnestab_252d_slope_v070_signal,
    f27cx_f27_capex_content_spend_cxassetsvolratio_252d_slope_v071_signal,
    f27cx_f27_capex_content_spend_netinvppnez_252d_slope_v072_signal,
    f27cx_f27_capex_content_spend_cxdepconv_252d_slope_v073_signal,
    f27cx_f27_capex_content_spend_invdivz_252d_slope_v074_signal,
    f27cx_f27_capex_content_spend_ncfixover_252d_slope_v075_signal,
    f27cx_f27_capex_content_spend_cxassets126_slope_v076_signal,
    f27cx_f27_capex_content_spend_cxdep126_slope_v077_signal,
    f27cx_f27_capex_content_spend_cxppnez126_slope_v078_signal,
    f27cx_f27_capex_content_spend_ncfippne_252d_slope_v079_signal,
    f27cx_f27_capex_content_spend_ncfidepz_252d_slope_v080_signal,
    f27cx_f27_capex_content_spend_cxgrow63_slope_v081_signal,
    f27cx_f27_capex_content_spend_cxloggrow504_slope_v082_signal,
    f27cx_f27_capex_content_spend_cxassetsyoyrank_504d_slope_v083_signal,
    f27cx_f27_capex_content_spend_cxdepmedtiltrank_252d_slope_v084_signal,
    f27cx_f27_capex_content_spend_cxinvsharez_252d_slope_v085_signal,
    f27cx_f27_capex_content_spend_cxppnecurv_slope_v086_signal,
    f27cx_f27_capex_content_spend_cxvsppnegrow_126d_slope_v087_signal,
    f27cx_f27_capex_content_spend_otherinvdepz_252d_slope_v088_signal,
    f27cx_f27_capex_content_spend_cxassetsconv126_slope_v089_signal,
    f27cx_f27_capex_content_spend_cxdepregfrac_252d_slope_v090_signal,
    f27cx_f27_capex_content_spend_cxdrawdown504_slope_v091_signal,
    f27cx_f27_capex_content_spend_cxrecov504_slope_v092_signal,
    f27cx_f27_capex_content_spend_cxassetsrngpos_504d_slope_v093_signal,
    f27cx_f27_capex_content_spend_ncfirngpos_252d_slope_v094_signal,
    f27cx_f27_capex_content_spend_cxdepdisp126_slope_v095_signal,
    f27cx_f27_capex_content_spend_cxcvrank_504d_slope_v096_signal,
    f27cx_f27_capex_content_spend_cxinvgapdepz_126d_slope_v097_signal,
    f27cx_f27_capex_content_spend_cxdepema252disp_slope_v098_signal,
    f27cx_f27_capex_content_spend_cxassetsmom_63d_slope_v099_signal,
    f27cx_f27_capex_content_spend_cxgrowaccel_252d_slope_v100_signal,
    f27cx_f27_capex_content_spend_ncfiaccel_252d_slope_v101_signal,
    f27cx_f27_capex_content_spend_cxppnestab126_slope_v102_signal,
    f27cx_f27_capex_content_spend_ncfifastturn_slope_v103_signal,
    f27cx_f27_capex_content_spend_cxassetsrank_252d_slope_v104_signal,
    f27cx_f27_capex_content_spend_cxppneassetmom_63d_slope_v105_signal,
    f27cx_f27_capex_content_spend_netinvppnerank_252d_slope_v106_signal,
    f27cx_f27_capex_content_spend_cxasym126_slope_v107_signal,
    f27cx_f27_capex_content_spend_cxassetseff_252d_slope_v108_signal,
    f27cx_f27_capex_content_spend_ncfidisp252_slope_v109_signal,
    f27cx_f27_capex_content_spend_ncfippnepulse_63d_slope_v110_signal,
    f27cx_f27_capex_content_spend_cxburstrank_252d_slope_v111_signal,
    f27cx_f27_capex_content_spend_cxppneconv_252d_slope_v112_signal,
    f27cx_f27_capex_content_spend_cxdepexcessmom_63d_slope_v113_signal,
    f27cx_f27_capex_content_spend_cxassetsregime_504d_slope_v114_signal,
    f27cx_f27_capex_content_spend_ncfitilt_504d_slope_v115_signal,
    f27cx_f27_capex_content_spend_cxrevsizez_126d_slope_v116_signal,
    f27cx_f27_capex_content_spend_cxdeprank_252d_slope_v117_signal,
    f27cx_f27_capex_content_spend_cxassetsaccel_126d_slope_v118_signal,
    f27cx_f27_capex_content_spend_cxppnepulse_63d_slope_v119_signal,
    f27cx_f27_capex_content_spend_netinveff_252d_slope_v120_signal,
    f27cx_f27_capex_content_spend_cxgrowshape_slope_v121_signal,
    f27cx_f27_capex_content_spend_cxdepamp_252d_slope_v122_signal,
    f27cx_f27_capex_content_spend_cxassetsamp_252d_slope_v123_signal,
    f27cx_f27_capex_content_spend_cxdeproot_252d_slope_v124_signal,
    f27cx_f27_capex_content_spend_invcxdepz_252d_slope_v125_signal,
    f27cx_f27_capex_content_spend_cxdepcurv_slope_v126_signal,
    f27cx_f27_capex_content_spend_cxdepeff_504d_slope_v127_signal,
    f27cx_f27_capex_content_spend_cxcyclerank_504d_slope_v128_signal,
    f27cx_f27_capex_content_spend_otherinvz_252d_slope_v129_signal,
    f27cx_f27_capex_content_spend_cxppnedrift_504d_slope_v130_signal,
    f27cx_f27_capex_content_spend_amortbuildgap_252d_slope_v131_signal,
    f27cx_f27_capex_content_spend_cxassetspulse_63d_slope_v132_signal,
    f27cx_f27_capex_content_spend_cxburstpers126_slope_v133_signal,
    f27cx_f27_capex_content_spend_cxdepz_504d_slope_v134_signal,
    f27cx_f27_capex_content_spend_ncfiz_126d_slope_v135_signal,
    f27cx_f27_capex_content_spend_cxdepvsassetintgrow_252d_slope_v136_signal,
    f27cx_f27_capex_content_spend_cxppneregfrac_504d_slope_v137_signal,
    f27cx_f27_capex_content_spend_cxdrawdown126_slope_v138_signal,
    f27cx_f27_capex_content_spend_cxdeprngpos_504d_slope_v139_signal,
    f27cx_f27_capex_content_spend_cxassetsstab126_slope_v140_signal,
    f27cx_f27_capex_content_spend_cxstepmag_504d_slope_v141_signal,
    f27cx_f27_capex_content_spend_cxinvsharerank_252d_slope_v142_signal,
    f27cx_f27_capex_content_spend_cxdualbasemom_63d_slope_v143_signal,
    f27cx_f27_capex_content_spend_ncfimedtilt_126d_slope_v144_signal,
    f27cx_f27_capex_content_spend_cxassetsbursttanh126_slope_v145_signal,
    f27cx_f27_capex_content_spend_cxdepamprank_504d_slope_v146_signal,
    f27cx_f27_capex_content_spend_netinvppnetilt_504d_slope_v147_signal,
    f27cx_f27_capex_content_spend_cxassetslogspr_126d_slope_v148_signal,
    f27cx_f27_capex_content_spend_ncfieff_252d_slope_v149_signal,
    f27cx_f27_capex_content_spend_cxppnefastcycle_slope_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F27_CAPEX_CONTENT_SPEND_REGISTRY_001_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500

    ALLOW = {
        "open", "high", "low", "close", "closeadj", "volume",
        "revenue", "revenueusd", "deferredrev", "gp", "grossmargin", "opinc",
        "opex", "sgna", "cor", "rnd", "sbcomp", "ebit", "ebitda", "ebitdamargin",
        "netinc", "netinccmn", "netmargin", "eps", "epsdil", "fcf", "fcfps",
        "ncfo", "ncff", "ncfi", "ncfcommon", "ncfdebt", "ncfbus", "capex",
        "depamor", "sharesbas", "shareswa", "shareswadil", "assets", "assetsc",
        "tangibles", "intangibles", "ppnenet", "investments", "inventory",
        "receivables", "payables", "equity", "retearn", "workingcapital", "debt",
        "debtc", "debtnc", "liabilities", "liabilitiesc", "cashneq", "currentratio",
        "roic", "roe", "roa", "ros", "assetturnover", "invcap", "intexp", "taxexp",
        "ebt", "sps", "bvps", "de", "ncfdiv", "dps", "divyield", "payoutratio",
        "prefdivis", "marketcap", "ev", "evebit", "evebitda", "pe", "pb", "ps",
        "shrholders", "shrvalue", "shrunits", "totalvalue", "percentoftotal",
        "fndholders", "undholders", "prfholders", "dbtholders", "putholders",
        "putvalue", "cllholders", "cllvalue", "wntholders", "wntvalue", "dbtvalue",
    }

    def _fund(seed, base=1e8, drift=0.03, vol=0.07, allow_neg=False):
        g = np.random.default_rng(seed)
        steps = np.repeat(g.normal(drift, vol, n // 63 + 1), 63)[:n]
        s = base * np.exp(np.cumsum(steps / 63))
        if allow_neg:
            s = s - base * 0.6
        return pd.Series(s, name=None)

    capex = (-_fund(271, base=4.0e7, drift=0.030, vol=0.09)).rename("capex")
    revenue = _fund(272, base=1.5e8, drift=0.035, vol=0.08).rename("revenue")
    assets = _fund(273, base=8.0e8, drift=0.020, vol=0.05).rename("assets")
    ppnenet = _fund(274, base=2.0e8, drift=0.025, vol=0.06).rename("ppnenet")
    depamor = _fund(275, base=3.0e7, drift=0.022, vol=0.07).rename("depamor")
    ncfi = _fund(276, base=6.0e7, drift=0.028, vol=0.10, allow_neg=True)
    ncfi = (ncfi - 8.0e7).rename("ncfi")

    cols = {"capex": capex, "revenue": revenue, "assets": assets,
            "ppnenet": ppnenet, "depamor": depamor, "ncfi": ncfi}

    n_features = 0
    nan_ok = 0
    results = {}
    for name, meta in REGISTRY.items():
        assert set(meta["inputs"]) <= ALLOW, "%s inputs %s" % (name, meta["inputs"])
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

    print("OK f27_capex_content_spend_2nd_derivatives_001_150_claude: %d features pass" % n_features)
