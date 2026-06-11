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
def _f035_ad_line(high, low, closeadj, volume):
    rng = (high - low).replace(0, np.nan)
    clv = ((closeadj - low) - (high - closeadj)) / rng
    return (clv.fillna(0.0) * volume).cumsum()


def _f035_ad_slope(high, low, closeadj, volume, w):
    rng = (high - low).replace(0, np.nan)
    clv = ((closeadj - low) - (high - closeadj)) / rng
    ad = (clv.fillna(0.0) * volume).cumsum()
    return ad.diff(w) / ad.abs().replace(0, np.nan)


def _f035_chaikin_trend(high, low, closeadj, volume, w):
    rng = (high - low).replace(0, np.nan)
    clv = ((closeadj - low) - (high - closeadj)) / rng
    ad = (clv.fillna(0.0) * volume).cumsum()
    fast = ad.ewm(span=max(3, w // 4), adjust=False).mean()
    slow = ad.ewm(span=w, adjust=False).mean()
    return (fast - slow) / ad.abs().replace(0, np.nan).rolling(w, min_periods=max(1, w // 2)).mean()


def f035ads_f035_ad_line_slope_zchaikin_126d_base_v076_signal(high, low, closeadj, volume):
    c = _f035_chaikin_trend(high, low, closeadj, volume, 126)
    result = _z(c, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_zchaikin_189d_base_v077_signal(high, low, closeadj, volume):
    c = _f035_chaikin_trend(high, low, closeadj, volume, 189)
    result = _z(c, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_zchaikin_252d_base_v078_signal(high, low, closeadj, volume):
    c = _f035_chaikin_trend(high, low, closeadj, volume, 252)
    result = _z(c, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_zchaikin_378d_base_v079_signal(high, low, closeadj, volume):
    c = _f035_chaikin_trend(high, low, closeadj, volume, 378)
    result = _z(c, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_zchaikin_504d_base_v080_signal(high, low, closeadj, volume):
    c = _f035_chaikin_trend(high, low, closeadj, volume, 504)
    result = _z(c, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_adlineband_5d_base_v081_signal(high, low, closeadj, volume):
    ad = _f035_ad_line(high, low, closeadj, volume)
    m = _mean(ad, 5)
    result = (ad - m) / ad.abs().rolling(5, min_periods=1).mean().replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_adlineband_10d_base_v082_signal(high, low, closeadj, volume):
    ad = _f035_ad_line(high, low, closeadj, volume)
    m = _mean(ad, 10)
    result = (ad - m) / ad.abs().rolling(10, min_periods=2).mean().replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_adlineband_21d_base_v083_signal(high, low, closeadj, volume):
    ad = _f035_ad_line(high, low, closeadj, volume)
    m = _mean(ad, 21)
    result = (ad - m) / ad.abs().rolling(21, min_periods=5).mean().replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_adlineband_42d_base_v084_signal(high, low, closeadj, volume):
    ad = _f035_ad_line(high, low, closeadj, volume)
    m = _mean(ad, 42)
    result = (ad - m) / ad.abs().rolling(42, min_periods=10).mean().replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_adlineband_63d_base_v085_signal(high, low, closeadj, volume):
    ad = _f035_ad_line(high, low, closeadj, volume)
    m = _mean(ad, 63)
    result = (ad - m) / ad.abs().rolling(63, min_periods=15).mean().replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_adlineband_126d_base_v086_signal(high, low, closeadj, volume):
    ad = _f035_ad_line(high, low, closeadj, volume)
    m = _mean(ad, 126)
    result = (ad - m) / ad.abs().rolling(126, min_periods=31).mean().replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_adlineband_189d_base_v087_signal(high, low, closeadj, volume):
    ad = _f035_ad_line(high, low, closeadj, volume)
    m = _mean(ad, 189)
    result = (ad - m) / ad.abs().rolling(189, min_periods=47).mean().replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_adlineband_252d_base_v088_signal(high, low, closeadj, volume):
    ad = _f035_ad_line(high, low, closeadj, volume)
    m = _mean(ad, 252)
    result = (ad - m) / ad.abs().rolling(252, min_periods=63).mean().replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_adlineband_378d_base_v089_signal(high, low, closeadj, volume):
    ad = _f035_ad_line(high, low, closeadj, volume)
    m = _mean(ad, 378)
    result = (ad - m) / ad.abs().rolling(378, min_periods=94).mean().replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_adlineband_504d_base_v090_signal(high, low, closeadj, volume):
    ad = _f035_ad_line(high, low, closeadj, volume)
    m = _mean(ad, 504)
    result = (ad - m) / ad.abs().rolling(504, min_periods=126).mean().replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_sqadslope_5d_base_v091_signal(high, low, closeadj, volume):
    sl = _f035_ad_slope(high, low, closeadj, volume, 5)
    result = (sl * sl) * np.sign(sl) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_sqadslope_10d_base_v092_signal(high, low, closeadj, volume):
    sl = _f035_ad_slope(high, low, closeadj, volume, 10)
    result = (sl * sl) * np.sign(sl) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_sqadslope_21d_base_v093_signal(high, low, closeadj, volume):
    sl = _f035_ad_slope(high, low, closeadj, volume, 21)
    result = (sl * sl) * np.sign(sl) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_sqadslope_42d_base_v094_signal(high, low, closeadj, volume):
    sl = _f035_ad_slope(high, low, closeadj, volume, 42)
    result = (sl * sl) * np.sign(sl) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_sqadslope_63d_base_v095_signal(high, low, closeadj, volume):
    sl = _f035_ad_slope(high, low, closeadj, volume, 63)
    result = (sl * sl) * np.sign(sl) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_sqadslope_126d_base_v096_signal(high, low, closeadj, volume):
    sl = _f035_ad_slope(high, low, closeadj, volume, 126)
    result = (sl * sl) * np.sign(sl) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_sqadslope_189d_base_v097_signal(high, low, closeadj, volume):
    sl = _f035_ad_slope(high, low, closeadj, volume, 189)
    result = (sl * sl) * np.sign(sl) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_sqadslope_252d_base_v098_signal(high, low, closeadj, volume):
    sl = _f035_ad_slope(high, low, closeadj, volume, 252)
    result = (sl * sl) * np.sign(sl) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_sqadslope_378d_base_v099_signal(high, low, closeadj, volume):
    sl = _f035_ad_slope(high, low, closeadj, volume, 378)
    result = (sl * sl) * np.sign(sl) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_sqadslope_504d_base_v100_signal(high, low, closeadj, volume):
    sl = _f035_ad_slope(high, low, closeadj, volume, 504)
    result = (sl * sl) * np.sign(sl) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_adslopexsign_5d_base_v101_signal(high, low, closeadj, volume):
    sl = _f035_ad_slope(high, low, closeadj, volume, 5)
    ret = closeadj.pct_change(1)
    result = sl * np.sign(ret).fillna(0.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_adslopexsign_10d_base_v102_signal(high, low, closeadj, volume):
    sl = _f035_ad_slope(high, low, closeadj, volume, 10)
    ret = closeadj.pct_change(2)
    result = sl * np.sign(ret).fillna(0.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_adslopexsign_21d_base_v103_signal(high, low, closeadj, volume):
    sl = _f035_ad_slope(high, low, closeadj, volume, 21)
    ret = closeadj.pct_change(5)
    result = sl * np.sign(ret).fillna(0.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_adslopexsign_42d_base_v104_signal(high, low, closeadj, volume):
    sl = _f035_ad_slope(high, low, closeadj, volume, 42)
    ret = closeadj.pct_change(10)
    result = sl * np.sign(ret).fillna(0.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_adslopexsign_63d_base_v105_signal(high, low, closeadj, volume):
    sl = _f035_ad_slope(high, low, closeadj, volume, 63)
    ret = closeadj.pct_change(15)
    result = sl * np.sign(ret).fillna(0.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_adslopexsign_126d_base_v106_signal(high, low, closeadj, volume):
    sl = _f035_ad_slope(high, low, closeadj, volume, 126)
    ret = closeadj.pct_change(31)
    result = sl * np.sign(ret).fillna(0.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_adslopexsign_189d_base_v107_signal(high, low, closeadj, volume):
    sl = _f035_ad_slope(high, low, closeadj, volume, 189)
    ret = closeadj.pct_change(47)
    result = sl * np.sign(ret).fillna(0.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_adslopexsign_252d_base_v108_signal(high, low, closeadj, volume):
    sl = _f035_ad_slope(high, low, closeadj, volume, 252)
    ret = closeadj.pct_change(63)
    result = sl * np.sign(ret).fillna(0.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_adslopexsign_378d_base_v109_signal(high, low, closeadj, volume):
    sl = _f035_ad_slope(high, low, closeadj, volume, 378)
    ret = closeadj.pct_change(94)
    result = sl * np.sign(ret).fillna(0.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_adslopexsign_504d_base_v110_signal(high, low, closeadj, volume):
    sl = _f035_ad_slope(high, low, closeadj, volume, 504)
    ret = closeadj.pct_change(126)
    result = sl * np.sign(ret).fillna(0.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_emaadline_5d_base_v111_signal(high, low, closeadj, volume):
    ad = _f035_ad_line(high, low, closeadj, volume)
    e = ad.ewm(span=5, adjust=False).mean()
    result = (ad - e) / ad.abs().rolling(63, min_periods=5).mean().replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_emaadline_10d_base_v112_signal(high, low, closeadj, volume):
    ad = _f035_ad_line(high, low, closeadj, volume)
    e = ad.ewm(span=10, adjust=False).mean()
    result = (ad - e) / ad.abs().rolling(63, min_periods=5).mean().replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_emaadline_21d_base_v113_signal(high, low, closeadj, volume):
    ad = _f035_ad_line(high, low, closeadj, volume)
    e = ad.ewm(span=21, adjust=False).mean()
    result = (ad - e) / ad.abs().rolling(63, min_periods=5).mean().replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_emaadline_42d_base_v114_signal(high, low, closeadj, volume):
    ad = _f035_ad_line(high, low, closeadj, volume)
    e = ad.ewm(span=42, adjust=False).mean()
    result = (ad - e) / ad.abs().rolling(63, min_periods=10).mean().replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_emaadline_63d_base_v115_signal(high, low, closeadj, volume):
    ad = _f035_ad_line(high, low, closeadj, volume)
    e = ad.ewm(span=63, adjust=False).mean()
    result = (ad - e) / ad.abs().rolling(63, min_periods=15).mean().replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_emaadline_126d_base_v116_signal(high, low, closeadj, volume):
    ad = _f035_ad_line(high, low, closeadj, volume)
    e = ad.ewm(span=126, adjust=False).mean()
    result = (ad - e) / ad.abs().rolling(126, min_periods=31).mean().replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_emaadline_189d_base_v117_signal(high, low, closeadj, volume):
    ad = _f035_ad_line(high, low, closeadj, volume)
    e = ad.ewm(span=189, adjust=False).mean()
    result = (ad - e) / ad.abs().rolling(189, min_periods=47).mean().replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_emaadline_252d_base_v118_signal(high, low, closeadj, volume):
    ad = _f035_ad_line(high, low, closeadj, volume)
    e = ad.ewm(span=252, adjust=False).mean()
    result = (ad - e) / ad.abs().rolling(252, min_periods=63).mean().replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_emaadline_378d_base_v119_signal(high, low, closeadj, volume):
    ad = _f035_ad_line(high, low, closeadj, volume)
    e = ad.ewm(span=378, adjust=False).mean()
    result = (ad - e) / ad.abs().rolling(378, min_periods=94).mean().replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_emaadline_504d_base_v120_signal(high, low, closeadj, volume):
    ad = _f035_ad_line(high, low, closeadj, volume)
    e = ad.ewm(span=504, adjust=False).mean()
    result = (ad - e) / ad.abs().rolling(504, min_periods=126).mean().replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_diffchaikin_5d_base_v121_signal(high, low, closeadj, volume):
    c = _f035_chaikin_trend(high, low, closeadj, volume, 5)
    result = c.diff(2) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_diffchaikin_10d_base_v122_signal(high, low, closeadj, volume):
    c = _f035_chaikin_trend(high, low, closeadj, volume, 10)
    result = c.diff(2) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_diffchaikin_21d_base_v123_signal(high, low, closeadj, volume):
    c = _f035_chaikin_trend(high, low, closeadj, volume, 21)
    result = c.diff(5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_diffchaikin_42d_base_v124_signal(high, low, closeadj, volume):
    c = _f035_chaikin_trend(high, low, closeadj, volume, 42)
    result = c.diff(10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_diffchaikin_63d_base_v125_signal(high, low, closeadj, volume):
    c = _f035_chaikin_trend(high, low, closeadj, volume, 63)
    result = c.diff(15) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_diffchaikin_126d_base_v126_signal(high, low, closeadj, volume):
    c = _f035_chaikin_trend(high, low, closeadj, volume, 126)
    result = c.diff(31) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_diffchaikin_189d_base_v127_signal(high, low, closeadj, volume):
    c = _f035_chaikin_trend(high, low, closeadj, volume, 189)
    result = c.diff(47) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_diffchaikin_252d_base_v128_signal(high, low, closeadj, volume):
    c = _f035_chaikin_trend(high, low, closeadj, volume, 252)
    result = c.diff(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_diffchaikin_378d_base_v129_signal(high, low, closeadj, volume):
    c = _f035_chaikin_trend(high, low, closeadj, volume, 378)
    result = c.diff(94) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_diffchaikin_504d_base_v130_signal(high, low, closeadj, volume):
    c = _f035_chaikin_trend(high, low, closeadj, volume, 504)
    result = c.diff(126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_adgap_5d_base_v131_signal(high, low, closeadj, volume):
    sl = _f035_ad_slope(high, low, closeadj, volume, 5)
    c = _f035_chaikin_trend(high, low, closeadj, volume, 5)
    result = (sl - c) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_adgap_10d_base_v132_signal(high, low, closeadj, volume):
    sl = _f035_ad_slope(high, low, closeadj, volume, 10)
    c = _f035_chaikin_trend(high, low, closeadj, volume, 10)
    result = (sl - c) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_adgap_21d_base_v133_signal(high, low, closeadj, volume):
    sl = _f035_ad_slope(high, low, closeadj, volume, 21)
    c = _f035_chaikin_trend(high, low, closeadj, volume, 21)
    result = (sl - c) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_adgap_42d_base_v134_signal(high, low, closeadj, volume):
    sl = _f035_ad_slope(high, low, closeadj, volume, 42)
    c = _f035_chaikin_trend(high, low, closeadj, volume, 42)
    result = (sl - c) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_adgap_63d_base_v135_signal(high, low, closeadj, volume):
    sl = _f035_ad_slope(high, low, closeadj, volume, 63)
    c = _f035_chaikin_trend(high, low, closeadj, volume, 63)
    result = (sl - c) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_adgap_126d_base_v136_signal(high, low, closeadj, volume):
    sl = _f035_ad_slope(high, low, closeadj, volume, 126)
    c = _f035_chaikin_trend(high, low, closeadj, volume, 126)
    result = (sl - c) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_adgap_189d_base_v137_signal(high, low, closeadj, volume):
    sl = _f035_ad_slope(high, low, closeadj, volume, 189)
    c = _f035_chaikin_trend(high, low, closeadj, volume, 189)
    result = (sl - c) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_adgap_252d_base_v138_signal(high, low, closeadj, volume):
    sl = _f035_ad_slope(high, low, closeadj, volume, 252)
    c = _f035_chaikin_trend(high, low, closeadj, volume, 252)
    result = (sl - c) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_adgap_378d_base_v139_signal(high, low, closeadj, volume):
    sl = _f035_ad_slope(high, low, closeadj, volume, 378)
    c = _f035_chaikin_trend(high, low, closeadj, volume, 378)
    result = (sl - c) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_adgap_504d_base_v140_signal(high, low, closeadj, volume):
    sl = _f035_ad_slope(high, low, closeadj, volume, 504)
    c = _f035_chaikin_trend(high, low, closeadj, volume, 504)
    result = (sl - c) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_diffadslope_5d_base_v141_signal(high, low, closeadj, volume):
    sl = _f035_ad_slope(high, low, closeadj, volume, 5)
    result = sl.diff(2) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_diffadslope_10d_base_v142_signal(high, low, closeadj, volume):
    sl = _f035_ad_slope(high, low, closeadj, volume, 10)
    result = sl.diff(2) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_diffadslope_21d_base_v143_signal(high, low, closeadj, volume):
    sl = _f035_ad_slope(high, low, closeadj, volume, 21)
    result = sl.diff(5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_diffadslope_42d_base_v144_signal(high, low, closeadj, volume):
    sl = _f035_ad_slope(high, low, closeadj, volume, 42)
    result = sl.diff(10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_diffadslope_63d_base_v145_signal(high, low, closeadj, volume):
    sl = _f035_ad_slope(high, low, closeadj, volume, 63)
    result = sl.diff(15) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_diffadslope_126d_base_v146_signal(high, low, closeadj, volume):
    sl = _f035_ad_slope(high, low, closeadj, volume, 126)
    result = sl.diff(31) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_diffadslope_189d_base_v147_signal(high, low, closeadj, volume):
    sl = _f035_ad_slope(high, low, closeadj, volume, 189)
    result = sl.diff(47) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_diffadslope_252d_base_v148_signal(high, low, closeadj, volume):
    sl = _f035_ad_slope(high, low, closeadj, volume, 252)
    result = sl.diff(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_diffadslope_378d_base_v149_signal(high, low, closeadj, volume):
    sl = _f035_ad_slope(high, low, closeadj, volume, 378)
    result = sl.diff(94) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f035ads_f035_ad_line_slope_diffadslope_504d_base_v150_signal(high, low, closeadj, volume):
    sl = _f035_ad_slope(high, low, closeadj, volume, 504)
    result = sl.diff(126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f035ads_f035_ad_line_slope_zchaikin_126d_base_v076_signal,
    f035ads_f035_ad_line_slope_zchaikin_189d_base_v077_signal,
    f035ads_f035_ad_line_slope_zchaikin_252d_base_v078_signal,
    f035ads_f035_ad_line_slope_zchaikin_378d_base_v079_signal,
    f035ads_f035_ad_line_slope_zchaikin_504d_base_v080_signal,
    f035ads_f035_ad_line_slope_adlineband_5d_base_v081_signal,
    f035ads_f035_ad_line_slope_adlineband_10d_base_v082_signal,
    f035ads_f035_ad_line_slope_adlineband_21d_base_v083_signal,
    f035ads_f035_ad_line_slope_adlineband_42d_base_v084_signal,
    f035ads_f035_ad_line_slope_adlineband_63d_base_v085_signal,
    f035ads_f035_ad_line_slope_adlineband_126d_base_v086_signal,
    f035ads_f035_ad_line_slope_adlineband_189d_base_v087_signal,
    f035ads_f035_ad_line_slope_adlineband_252d_base_v088_signal,
    f035ads_f035_ad_line_slope_adlineband_378d_base_v089_signal,
    f035ads_f035_ad_line_slope_adlineband_504d_base_v090_signal,
    f035ads_f035_ad_line_slope_sqadslope_5d_base_v091_signal,
    f035ads_f035_ad_line_slope_sqadslope_10d_base_v092_signal,
    f035ads_f035_ad_line_slope_sqadslope_21d_base_v093_signal,
    f035ads_f035_ad_line_slope_sqadslope_42d_base_v094_signal,
    f035ads_f035_ad_line_slope_sqadslope_63d_base_v095_signal,
    f035ads_f035_ad_line_slope_sqadslope_126d_base_v096_signal,
    f035ads_f035_ad_line_slope_sqadslope_189d_base_v097_signal,
    f035ads_f035_ad_line_slope_sqadslope_252d_base_v098_signal,
    f035ads_f035_ad_line_slope_sqadslope_378d_base_v099_signal,
    f035ads_f035_ad_line_slope_sqadslope_504d_base_v100_signal,
    f035ads_f035_ad_line_slope_adslopexsign_5d_base_v101_signal,
    f035ads_f035_ad_line_slope_adslopexsign_10d_base_v102_signal,
    f035ads_f035_ad_line_slope_adslopexsign_21d_base_v103_signal,
    f035ads_f035_ad_line_slope_adslopexsign_42d_base_v104_signal,
    f035ads_f035_ad_line_slope_adslopexsign_63d_base_v105_signal,
    f035ads_f035_ad_line_slope_adslopexsign_126d_base_v106_signal,
    f035ads_f035_ad_line_slope_adslopexsign_189d_base_v107_signal,
    f035ads_f035_ad_line_slope_adslopexsign_252d_base_v108_signal,
    f035ads_f035_ad_line_slope_adslopexsign_378d_base_v109_signal,
    f035ads_f035_ad_line_slope_adslopexsign_504d_base_v110_signal,
    f035ads_f035_ad_line_slope_emaadline_5d_base_v111_signal,
    f035ads_f035_ad_line_slope_emaadline_10d_base_v112_signal,
    f035ads_f035_ad_line_slope_emaadline_21d_base_v113_signal,
    f035ads_f035_ad_line_slope_emaadline_42d_base_v114_signal,
    f035ads_f035_ad_line_slope_emaadline_63d_base_v115_signal,
    f035ads_f035_ad_line_slope_emaadline_126d_base_v116_signal,
    f035ads_f035_ad_line_slope_emaadline_189d_base_v117_signal,
    f035ads_f035_ad_line_slope_emaadline_252d_base_v118_signal,
    f035ads_f035_ad_line_slope_emaadline_378d_base_v119_signal,
    f035ads_f035_ad_line_slope_emaadline_504d_base_v120_signal,
    f035ads_f035_ad_line_slope_diffchaikin_5d_base_v121_signal,
    f035ads_f035_ad_line_slope_diffchaikin_10d_base_v122_signal,
    f035ads_f035_ad_line_slope_diffchaikin_21d_base_v123_signal,
    f035ads_f035_ad_line_slope_diffchaikin_42d_base_v124_signal,
    f035ads_f035_ad_line_slope_diffchaikin_63d_base_v125_signal,
    f035ads_f035_ad_line_slope_diffchaikin_126d_base_v126_signal,
    f035ads_f035_ad_line_slope_diffchaikin_189d_base_v127_signal,
    f035ads_f035_ad_line_slope_diffchaikin_252d_base_v128_signal,
    f035ads_f035_ad_line_slope_diffchaikin_378d_base_v129_signal,
    f035ads_f035_ad_line_slope_diffchaikin_504d_base_v130_signal,
    f035ads_f035_ad_line_slope_adgap_5d_base_v131_signal,
    f035ads_f035_ad_line_slope_adgap_10d_base_v132_signal,
    f035ads_f035_ad_line_slope_adgap_21d_base_v133_signal,
    f035ads_f035_ad_line_slope_adgap_42d_base_v134_signal,
    f035ads_f035_ad_line_slope_adgap_63d_base_v135_signal,
    f035ads_f035_ad_line_slope_adgap_126d_base_v136_signal,
    f035ads_f035_ad_line_slope_adgap_189d_base_v137_signal,
    f035ads_f035_ad_line_slope_adgap_252d_base_v138_signal,
    f035ads_f035_ad_line_slope_adgap_378d_base_v139_signal,
    f035ads_f035_ad_line_slope_adgap_504d_base_v140_signal,
    f035ads_f035_ad_line_slope_diffadslope_5d_base_v141_signal,
    f035ads_f035_ad_line_slope_diffadslope_10d_base_v142_signal,
    f035ads_f035_ad_line_slope_diffadslope_21d_base_v143_signal,
    f035ads_f035_ad_line_slope_diffadslope_42d_base_v144_signal,
    f035ads_f035_ad_line_slope_diffadslope_63d_base_v145_signal,
    f035ads_f035_ad_line_slope_diffadslope_126d_base_v146_signal,
    f035ads_f035_ad_line_slope_diffadslope_189d_base_v147_signal,
    f035ads_f035_ad_line_slope_diffadslope_252d_base_v148_signal,
    f035ads_f035_ad_line_slope_diffadslope_378d_base_v149_signal,
    f035ads_f035_ad_line_slope_diffadslope_504d_base_v150_signal,
]



def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F035_AD_LINE_SLOPE_REGISTRY_076_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    high = closeadj * (1.0 + np.abs(np.random.normal(0, 0.01, n)))
    low = closeadj * (1.0 - np.abs(np.random.normal(0, 0.01, n)))
    high = pd.Series(high, name="high")
    low = pd.Series(low, name="low")
    volume = pd.Series(np.abs(np.random.normal(1e6, 3e5, n)), name="volume")

    cols = {"closeadj": closeadj, "high": high, "low": low, "volume": volume}

    n_features = 0
    nan_ok = 0
    domain_primitives = ('_f035_ad_line', '_f035_ad_slope', '_f035_chaikin_trend')
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
    print(f"OK f035_ad_line_slope_base_076_150_claude: {n_features} features pass")
