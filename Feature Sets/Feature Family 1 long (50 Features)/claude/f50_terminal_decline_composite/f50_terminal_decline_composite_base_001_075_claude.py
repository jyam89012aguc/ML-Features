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


def _diff(s, n):
    return s.diff(periods=n)


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


# ===== folder domain primitives =====
def _f50_terminal_decline(revenue, opinc, marketcap, w):
    # composite: revenue decline + margin compression + valuation collapse
    rev_decline = -revenue.diff(w) / revenue.shift(w).abs().replace(0, np.nan)
    margin = opinc / revenue.replace(0, np.nan)
    margin_compression = -margin.diff(w)
    val_collapse = -marketcap.diff(w) / marketcap.shift(w).abs().replace(0, np.nan)
    return rev_decline + margin_compression + val_collapse


def _f50_revdecline(revenue, w):
    return -revenue.diff(w) / revenue.shift(w).abs().replace(0, np.nan)


def _f50_margincompress(opinc, revenue, w):
    margin = opinc / revenue.replace(0, np.nan)
    return -margin.diff(w)


# 21d terminal-decline composite × marketcap
def f50tdc_f50_terminal_decline_composite_decline_21d_base_v001_signal(revenue, opinc, marketcap):
    base = _f50_terminal_decline(revenue, opinc, marketcap, 21)
    result = base * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 63d terminal-decline composite × marketcap
def f50tdc_f50_terminal_decline_composite_decline_63d_base_v002_signal(revenue, opinc, marketcap):
    base = _f50_terminal_decline(revenue, opinc, marketcap, 63)
    result = base * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 126d terminal-decline composite × marketcap
def f50tdc_f50_terminal_decline_composite_decline_126d_base_v003_signal(revenue, opinc, marketcap):
    base = _f50_terminal_decline(revenue, opinc, marketcap, 126)
    result = base * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d terminal-decline composite × marketcap
def f50tdc_f50_terminal_decline_composite_decline_252d_base_v004_signal(revenue, opinc, marketcap):
    base = _f50_terminal_decline(revenue, opinc, marketcap, 252)
    result = base * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 504d terminal-decline composite × marketcap
def f50tdc_f50_terminal_decline_composite_decline_504d_base_v005_signal(revenue, opinc, marketcap):
    base = _f50_terminal_decline(revenue, opinc, marketcap, 504)
    result = base * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 21d mean decline × marketcap
def f50tdc_f50_terminal_decline_composite_declinemean_21d_base_v006_signal(revenue, opinc, marketcap):
    base = _f50_terminal_decline(revenue, opinc, marketcap, 63)
    result = _mean(base, 21) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean decline × marketcap
def f50tdc_f50_terminal_decline_composite_declinemean_63d_base_v007_signal(revenue, opinc, marketcap):
    base = _f50_terminal_decline(revenue, opinc, marketcap, 252)
    result = _mean(base, 63) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 21d std decline
def f50tdc_f50_terminal_decline_composite_declinestd_21d_base_v008_signal(revenue, opinc, marketcap):
    base = _f50_terminal_decline(revenue, opinc, marketcap, 63)
    result = _std(base, 21) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 63d std decline
def f50tdc_f50_terminal_decline_composite_declinestd_63d_base_v009_signal(revenue, opinc, marketcap):
    base = _f50_terminal_decline(revenue, opinc, marketcap, 252)
    result = _std(base, 63) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d std decline
def f50tdc_f50_terminal_decline_composite_declinestd_252d_base_v010_signal(revenue, opinc, marketcap):
    base = _f50_terminal_decline(revenue, opinc, marketcap, 252)
    result = _std(base, 252) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 21d zscore decline over 252d
def f50tdc_f50_terminal_decline_composite_declinez_252d_base_v011_signal(revenue, opinc, marketcap):
    base = _f50_terminal_decline(revenue, opinc, marketcap, 63)
    result = _z(base, 252) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 63d zscore decline over 504d
def f50tdc_f50_terminal_decline_composite_declinez_504d_base_v012_signal(revenue, opinc, marketcap):
    base = _f50_terminal_decline(revenue, opinc, marketcap, 252)
    result = _z(base, 504) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 21d revenue decline × marketcap
def f50tdc_f50_terminal_decline_composite_revdecline_21d_base_v013_signal(revenue, marketcap):
    base = _f50_revdecline(revenue, 21)
    result = base * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 63d revenue decline × marketcap
def f50tdc_f50_terminal_decline_composite_revdecline_63d_base_v014_signal(revenue, marketcap):
    base = _f50_revdecline(revenue, 63)
    result = base * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d revenue decline × marketcap
def f50tdc_f50_terminal_decline_composite_revdecline_252d_base_v015_signal(revenue, marketcap):
    base = _f50_revdecline(revenue, 252)
    result = base * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 504d revenue decline × marketcap
def f50tdc_f50_terminal_decline_composite_revdecline_504d_base_v016_signal(revenue, marketcap):
    base = _f50_revdecline(revenue, 504)
    result = base * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 21d std revdecline
def f50tdc_f50_terminal_decline_composite_revdeclinestd_21d_base_v017_signal(revenue, marketcap):
    base = _f50_revdecline(revenue, 63)
    result = _std(base, 21) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 63d std revdecline
def f50tdc_f50_terminal_decline_composite_revdeclinestd_63d_base_v018_signal(revenue, marketcap):
    base = _f50_revdecline(revenue, 252)
    result = _std(base, 63) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 21d zscore revdecline
def f50tdc_f50_terminal_decline_composite_revdeclinez_252d_base_v019_signal(revenue, marketcap):
    base = _f50_revdecline(revenue, 63)
    result = _z(base, 252) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 63d zscore revdecline
def f50tdc_f50_terminal_decline_composite_revdeclinez_504d_base_v020_signal(revenue, marketcap):
    base = _f50_revdecline(revenue, 252)
    result = _z(base, 504) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 21d margin compression × marketcap
def f50tdc_f50_terminal_decline_composite_margcomp_21d_base_v021_signal(opinc, revenue, marketcap):
    base = _f50_margincompress(opinc, revenue, 21)
    result = base * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 63d margin compression × marketcap
def f50tdc_f50_terminal_decline_composite_margcomp_63d_base_v022_signal(opinc, revenue, marketcap):
    base = _f50_margincompress(opinc, revenue, 63)
    result = base * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d margin compression × marketcap
def f50tdc_f50_terminal_decline_composite_margcomp_252d_base_v023_signal(opinc, revenue, marketcap):
    base = _f50_margincompress(opinc, revenue, 252)
    result = base * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 504d margin compression × marketcap
def f50tdc_f50_terminal_decline_composite_margcomp_504d_base_v024_signal(opinc, revenue, marketcap):
    base = _f50_margincompress(opinc, revenue, 504)
    result = base * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 63d std margin compression
def f50tdc_f50_terminal_decline_composite_margcompstd_63d_base_v025_signal(opinc, revenue, marketcap):
    base = _f50_margincompress(opinc, revenue, 252)
    result = _std(base, 63) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d std margin compression
def f50tdc_f50_terminal_decline_composite_margcompstd_252d_base_v026_signal(opinc, revenue, marketcap):
    base = _f50_margincompress(opinc, revenue, 252)
    result = _std(base, 252) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 21d zscore margin compression
def f50tdc_f50_terminal_decline_composite_margcompz_252d_base_v027_signal(opinc, revenue, marketcap):
    base = _f50_margincompress(opinc, revenue, 63)
    result = _z(base, 252) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 63d zscore margin compression
def f50tdc_f50_terminal_decline_composite_margcompz_504d_base_v028_signal(opinc, revenue, marketcap):
    base = _f50_margincompress(opinc, revenue, 252)
    result = _z(base, 504) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d count strong-decline (>10%)
def f50tdc_f50_terminal_decline_composite_decline10cnt_252d_base_v029_signal(revenue, opinc, marketcap):
    base = _f50_terminal_decline(revenue, opinc, marketcap, 63)
    result = (base).rolling(252, min_periods=63).mean() * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 504d count strong-decline (>30%)
def f50tdc_f50_terminal_decline_composite_decline30cnt_504d_base_v030_signal(revenue, opinc, marketcap):
    base = _f50_terminal_decline(revenue, opinc, marketcap, 252)
    result = (base).rolling(504, min_periods=126).mean() * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d count revenue decline > 5%
def f50tdc_f50_terminal_decline_composite_revdecline5cnt_252d_base_v031_signal(revenue, marketcap):
    base = _f50_revdecline(revenue, 63)
    result = (base).rolling(252, min_periods=63).mean() * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 504d count revenue decline > 15%
def f50tdc_f50_terminal_decline_composite_revdecline15cnt_504d_base_v032_signal(revenue, marketcap):
    base = _f50_revdecline(revenue, 252)
    result = (base).rolling(504, min_periods=126).mean() * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d count margin compression > 2pp
def f50tdc_f50_terminal_decline_composite_margcomp2cnt_252d_base_v033_signal(opinc, revenue, marketcap):
    base = _f50_margincompress(opinc, revenue, 63)
    result = (base).rolling(252, min_periods=63).mean() * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 504d count margin compression > 5pp
def f50tdc_f50_terminal_decline_composite_margcomp5cnt_504d_base_v034_signal(opinc, revenue, marketcap):
    base = _f50_margincompress(opinc, revenue, 252)
    result = (base).rolling(504, min_periods=126).mean() * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 21d worst (max) decline × marketcap
def f50tdc_f50_terminal_decline_composite_worstdecline_21d_base_v035_signal(revenue, opinc, marketcap):
    base = _f50_terminal_decline(revenue, opinc, marketcap, 63)
    result = base.rolling(21, min_periods=5).max() * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 63d worst decline
def f50tdc_f50_terminal_decline_composite_worstdecline_63d_base_v036_signal(revenue, opinc, marketcap):
    base = _f50_terminal_decline(revenue, opinc, marketcap, 63)
    result = base.rolling(63, min_periods=21).max() * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d worst decline
def f50tdc_f50_terminal_decline_composite_worstdecline_252d_base_v037_signal(revenue, opinc, marketcap):
    base = _f50_terminal_decline(revenue, opinc, marketcap, 252)
    result = base.rolling(252, min_periods=63).max() * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 504d worst decline
def f50tdc_f50_terminal_decline_composite_worstdecline_504d_base_v038_signal(revenue, opinc, marketcap):
    base = _f50_terminal_decline(revenue, opinc, marketcap, 504)
    result = base.rolling(504, min_periods=126).max() * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 21d EMA decline
def f50tdc_f50_terminal_decline_composite_declineema_21d_base_v039_signal(revenue, opinc, marketcap):
    base = _f50_terminal_decline(revenue, opinc, marketcap, 63)
    result = base.ewm(span=21, adjust=False).mean() * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 63d EMA decline
def f50tdc_f50_terminal_decline_composite_declineema_63d_base_v040_signal(revenue, opinc, marketcap):
    base = _f50_terminal_decline(revenue, opinc, marketcap, 63)
    result = base.ewm(span=63, adjust=False).mean() * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d EMA decline
def f50tdc_f50_terminal_decline_composite_declineema_252d_base_v041_signal(revenue, opinc, marketcap):
    base = _f50_terminal_decline(revenue, opinc, marketcap, 252)
    result = base.ewm(span=252, adjust=False).mean() * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 21d squared decline
def f50tdc_f50_terminal_decline_composite_declinesq_21d_base_v042_signal(revenue, opinc, marketcap):
    base = _f50_terminal_decline(revenue, opinc, marketcap, 21)
    result = base * base.abs() * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 63d squared decline
def f50tdc_f50_terminal_decline_composite_declinesq_63d_base_v043_signal(revenue, opinc, marketcap):
    base = _f50_terminal_decline(revenue, opinc, marketcap, 63)
    result = base * base.abs() * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d squared decline
def f50tdc_f50_terminal_decline_composite_declinesq_252d_base_v044_signal(revenue, opinc, marketcap):
    base = _f50_terminal_decline(revenue, opinc, marketcap, 252)
    result = base * base.abs() * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# decline × ev (size-scaled severity)
def f50tdc_f50_terminal_decline_composite_declinexev_63d_base_v045_signal(revenue, opinc, marketcap, ev):
    base = _f50_terminal_decline(revenue, opinc, marketcap, 63)
    result = base * ev
    return result.replace([np.inf, -np.inf], np.nan)


# 252d decline × ev
def f50tdc_f50_terminal_decline_composite_declinexev_252d_base_v046_signal(revenue, opinc, marketcap, ev):
    base = _f50_terminal_decline(revenue, opinc, marketcap, 252)
    result = base * ev
    return result.replace([np.inf, -np.inf], np.nan)


# decline × pe 63d
def f50tdc_f50_terminal_decline_composite_declinexpe_63d_base_v047_signal(revenue, opinc, marketcap, pe):
    base = _f50_terminal_decline(revenue, opinc, marketcap, 63)
    result = base * pe * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# decline × ps 63d
def f50tdc_f50_terminal_decline_composite_declinexps_63d_base_v048_signal(revenue, opinc, marketcap, ps):
    base = _f50_terminal_decline(revenue, opinc, marketcap, 63)
    result = base * ps * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# decline × evebitda 63d
def f50tdc_f50_terminal_decline_composite_declinexevebitda_63d_base_v049_signal(revenue, opinc, marketcap, evebitda):
    base = _f50_terminal_decline(revenue, opinc, marketcap, 63)
    result = base * evebitda * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# decline × evebit 63d
def f50tdc_f50_terminal_decline_composite_declinexevebit_63d_base_v050_signal(revenue, opinc, marketcap, evebit):
    base = _f50_terminal_decline(revenue, opinc, marketcap, 63)
    result = base * evebit * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# decline × pb 63d
def f50tdc_f50_terminal_decline_composite_declinexpb_63d_base_v051_signal(revenue, opinc, marketcap, pb):
    base = _f50_terminal_decline(revenue, opinc, marketcap, 63)
    result = base * pb * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# revdecline × ev 63d
def f50tdc_f50_terminal_decline_composite_revdeclinexev_63d_base_v052_signal(revenue, marketcap, ev):
    base = _f50_revdecline(revenue, 63)
    result = base * ev + _f50_margincompress(revenue, revenue, 21) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# revdecline × pe 63d
def f50tdc_f50_terminal_decline_composite_revdeclinexpe_63d_base_v053_signal(revenue, marketcap, pe):
    base = _f50_revdecline(revenue, 63)
    result = base * pe * marketcap + _f50_margincompress(revenue, revenue, 21) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# revdecline × ps 252d
def f50tdc_f50_terminal_decline_composite_revdeclinexps_252d_base_v054_signal(revenue, marketcap, ps):
    base = _f50_revdecline(revenue, 252)
    result = base * ps * marketcap + _f50_margincompress(revenue, revenue, 21) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# margcomp × ev 63d
def f50tdc_f50_terminal_decline_composite_margcompxev_63d_base_v055_signal(opinc, revenue, marketcap, ev):
    base = _f50_margincompress(opinc, revenue, 63)
    result = base * ev + _f50_revdecline(revenue, 21) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# margcomp × pe 63d
def f50tdc_f50_terminal_decline_composite_margcompxpe_63d_base_v056_signal(opinc, revenue, marketcap, pe):
    base = _f50_margincompress(opinc, revenue, 63)
    result = base * pe * marketcap + _f50_revdecline(revenue, 21) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 21d gap of decline 63m252
def f50tdc_f50_terminal_decline_composite_declinegap_63m252_base_v057_signal(revenue, opinc, marketcap):
    a = _f50_terminal_decline(revenue, opinc, marketcap, 63)
    b = _f50_terminal_decline(revenue, opinc, marketcap, 252)
    result = (a - b) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# decline 21m63 gap
def f50tdc_f50_terminal_decline_composite_declinegap_21m63_base_v058_signal(revenue, opinc, marketcap):
    a = _f50_terminal_decline(revenue, opinc, marketcap, 21)
    b = _f50_terminal_decline(revenue, opinc, marketcap, 63)
    result = (a - b) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# decline 252m504 gap
def f50tdc_f50_terminal_decline_composite_declinegap_252m504_base_v059_signal(revenue, opinc, marketcap):
    a = _f50_terminal_decline(revenue, opinc, marketcap, 252)
    b = _f50_terminal_decline(revenue, opinc, marketcap, 504)
    result = (a - b) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 63d / 252d decline ratio
def f50tdc_f50_terminal_decline_composite_declineratio_63v252_base_v060_signal(revenue, opinc, marketcap):
    a = _f50_terminal_decline(revenue, opinc, marketcap, 63)
    b = _f50_terminal_decline(revenue, opinc, marketcap, 252).replace(0, np.nan)
    result = (a / b) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 21d / 63d decline ratio
def f50tdc_f50_terminal_decline_composite_declineratio_21v63_base_v061_signal(revenue, opinc, marketcap):
    a = _f50_terminal_decline(revenue, opinc, marketcap, 21)
    b = _f50_terminal_decline(revenue, opinc, marketcap, 63).replace(0, np.nan)
    result = (a / b) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# expanding worst decline × marketcap
def f50tdc_f50_terminal_decline_composite_declineworstever_base_v062_signal(revenue, opinc, marketcap):
    base = _f50_terminal_decline(revenue, opinc, marketcap, 252)
    result = base.expanding(min_periods=63).max() * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# decline vs ever 63d
def f50tdc_f50_terminal_decline_composite_declinevsever_63d_base_v063_signal(revenue, opinc, marketcap):
    base = _f50_terminal_decline(revenue, opinc, marketcap, 63)
    worst = base.expanding(min_periods=63).max()
    result = (worst - base) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# decline vs ever 252d
def f50tdc_f50_terminal_decline_composite_declinevsever_252d_base_v064_signal(revenue, opinc, marketcap):
    base = _f50_terminal_decline(revenue, opinc, marketcap, 252)
    worst = base.expanding(min_periods=63).max()
    result = (worst - base) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# decline × marketcap squared
def f50tdc_f50_terminal_decline_composite_declinexmcapsq_63d_base_v065_signal(revenue, opinc, marketcap):
    base = _f50_terminal_decline(revenue, opinc, marketcap, 63)
    result = base * marketcap * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d decline × marketcap squared
def f50tdc_f50_terminal_decline_composite_declinexmcapsq_252d_base_v066_signal(revenue, opinc, marketcap):
    base = _f50_terminal_decline(revenue, opinc, marketcap, 252)
    result = base * marketcap * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# decline × log marketcap
def f50tdc_f50_terminal_decline_composite_declinexlogmcap_63d_base_v067_signal(revenue, opinc, marketcap):
    base = _f50_terminal_decline(revenue, opinc, marketcap, 63)
    lm = np.log(marketcap.replace(0, np.nan).abs())
    result = base * lm * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# decline × revenue 63d
def f50tdc_f50_terminal_decline_composite_declinexrev_63d_base_v068_signal(revenue, opinc, marketcap):
    base = _f50_terminal_decline(revenue, opinc, marketcap, 63)
    result = base * revenue
    return result.replace([np.inf, -np.inf], np.nan)


# decline × assets 63d
def f50tdc_f50_terminal_decline_composite_declinexassets_63d_base_v069_signal(revenue, opinc, marketcap, assets):
    base = _f50_terminal_decline(revenue, opinc, marketcap, 63)
    result = base * assets + _f50_revdecline(revenue, 21) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# decline × debt 252d
def f50tdc_f50_terminal_decline_composite_declinexdebt_252d_base_v070_signal(revenue, opinc, marketcap, debt):
    base = _f50_terminal_decline(revenue, opinc, marketcap, 252)
    result = base * debt + _f50_revdecline(revenue, 21) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 63d decline area
def f50tdc_f50_terminal_decline_composite_declinearea_63d_base_v071_signal(revenue, opinc, marketcap):
    base = _f50_terminal_decline(revenue, opinc, marketcap, 63).abs()
    result = base.rolling(63, min_periods=21).sum() * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d decline area
def f50tdc_f50_terminal_decline_composite_declinearea_252d_base_v072_signal(revenue, opinc, marketcap):
    base = _f50_terminal_decline(revenue, opinc, marketcap, 252).abs()
    result = base.rolling(252, min_periods=63).sum() * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 504d decline area
def f50tdc_f50_terminal_decline_composite_declinearea_504d_base_v073_signal(revenue, opinc, marketcap):
    base = _f50_terminal_decline(revenue, opinc, marketcap, 504).abs()
    result = base.rolling(504, min_periods=126).sum() * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 63d revdecline × margin compression (joint)
def f50tdc_f50_terminal_decline_composite_revxmargcomp_63d_base_v074_signal(revenue, opinc, marketcap):
    a = _f50_revdecline(revenue, 63)
    b = _f50_margincompress(opinc, revenue, 63)
    result = a * b * marketcap + _f50_terminal_decline(revenue, opinc, marketcap, 21) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 252d composite severity × ev
def f50tdc_f50_terminal_decline_composite_compositesev_252d_base_v075_signal(revenue, opinc, marketcap, ev):
    a = _f50_revdecline(revenue, 252).abs()
    b = _f50_margincompress(opinc, revenue, 252).abs()
    c = _f50_terminal_decline(revenue, opinc, marketcap, 252).abs()
    result = (a + b + c) * ev
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [v for k, v in list(globals().items()) if k.startswith("f50tdc_") and callable(v)]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F50_TERMINAL_DECLINE_COMPOSITE_REGISTRY_001_075 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(np.random.normal(0.0005, 0.02, n))), name="closeadj")
    marketcap = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0005, 0.015, n))), name="marketcap")
    revenue = pd.Series(5e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.005, n))), name="revenue")
    netinc = pd.Series(5e7 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="netinc")
    fcf = pd.Series(3e7 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="fcf")
    ncfo = pd.Series(4e7 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="ncfo")
    equity = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.004, n))), name="equity")
    debt = pd.Series(5e8 * np.exp(np.cumsum(np.random.normal(0.0001, 0.005, n))), name="debt")
    assets = pd.Series(2e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.003, n))), name="assets")
    ebitda = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.006, n))), name="ebitda")
    capex = pd.Series(3e7 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="capex")
    sharesbas = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(0.0001, 0.002, n))), name="sharesbas")
    opinc = pd.Series(8e7 * np.exp(np.cumsum(np.random.normal(0.0002, 0.007, n))), name="opinc")
    ev = marketcap + debt
    ev = pd.Series(ev.values, name="ev")
    evebit = pd.Series((ev / opinc.replace(0, np.nan)).values, name="evebit")
    evebitda = pd.Series((ev / ebitda.replace(0, np.nan)).values, name="evebitda")
    pe = pd.Series((marketcap / netinc.replace(0, np.nan)).values, name="pe")
    pb = pd.Series((marketcap / equity.replace(0, np.nan)).values, name="pb")
    ps = pd.Series((marketcap / revenue.replace(0, np.nan)).values, name="ps")

    cols = {"closeadj": closeadj, "marketcap": marketcap, "ev": ev, "evebit": evebit, "evebitda": evebitda,
            "pe": pe, "pb": pb, "ps": ps, "revenue": revenue, "netinc": netinc, "fcf": fcf, "ncfo": ncfo,
            "equity": equity, "debt": debt, "assets": assets, "ebitda": ebitda, "capex": capex,
            "sharesbas": sharesbas, "opinc": opinc}

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f50_terminal_decline", "_f50_revdecline", "_f50_margincompress")
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
    print(f"OK f50_terminal_decline_composite_base_001_075_claude: {n_features} features pass")
