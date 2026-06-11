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


# ===== generic helpers =====
def _z(s, w):
    m = s.rolling(w, min_periods=max(1, w // 2)).mean()
    sd = s.rolling(w, min_periods=max(1, w // 2)).std()
    return (s - m) / sd.replace(0, np.nan)


def _mean(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def _std(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).std()


def _rank(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).rank(pct=True) - 0.5


def _jerk(s, w):
    # 2nd math derivative (acceleration / jerk) of a series over step w
    d1 = s - s.shift(w)
    return d1 - d1.shift(w)


def _slope(s, w):
    idx = np.arange(w, dtype=float)
    idx = idx - idx.mean()
    denom = float((idx * idx).sum())

    def _f(a):
        if np.isnan(a).any():
            return np.nan
        return float((idx * (a - a.mean())).sum() / denom)

    return s.rolling(w, min_periods=w).apply(_f, raw=True)


# ===== folder domain primitives (FCF trajectory) =====
def _f25_growth(s, w):
    base = s.shift(w)
    return np.sign(base) * (s - base) / base.abs().replace(0, np.nan)


def _f25_fcf_margin(fcf, revenue):
    return fcf / revenue.replace(0, np.nan)


def _f25_margin_trend(fcf, revenue, w):
    return _slope(_f25_fcf_margin(fcf, revenue), w)


def _f25_consistency(s, w):
    return (s > 0).astype(float).rolling(w, min_periods=max(1, w // 2)).mean()


# ============================================================
# jerk of FCF YoY growth (252d base -> 63d 2nd difference)
def f25ft_f25_fcf_trajectory_fcfgr_252d_jerk_v001_signal(fcf):
    base = _f25_growth(fcf, 252)
    b = _jerk(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of FCF half-year growth (126d base -> 21d 2nd diff)
def f25ft_f25_fcf_trajectory_fcfgr_126d_jerk_v002_signal(fcf):
    base = _f25_growth(fcf, 126)
    b = _jerk(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of ncfo YoY growth (252d -> 63d 2nd diff)
def f25ft_f25_fcf_trajectory_ncfogr_252d_jerk_v003_signal(ncfo):
    base = _f25_growth(ncfo, 252)
    b = _jerk(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of FCF-per-share YoY growth (252d -> 63d 2nd diff)
def f25ft_f25_fcf_trajectory_fcfpsgr_252d_jerk_v004_signal(fcfps):
    base = _f25_growth(fcfps, 252)
    b = _jerk(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of FCF margin level (-> 21d 2nd diff)
def f25ft_f25_fcf_trajectory_fcfmargin_jerk_v005_signal(fcf, revenue):
    base = _f25_fcf_margin(fcf, revenue)
    b = _jerk(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of FCF margin year-trend (252d trend -> 63d 2nd diff)
def f25ft_f25_fcf_trajectory_fcfmargtrend_252d_jerk_v006_signal(fcf, revenue):
    base = _f25_margin_trend(fcf, revenue, 252)
    b = _jerk(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of FCF margin half-year trend (126d trend -> 21d 2nd diff)
def f25ft_f25_fcf_trajectory_fcfmargtrend_126d_jerk_v007_signal(fcf, revenue):
    base = _f25_margin_trend(fcf, revenue, 126)
    b = _jerk(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of FCF positivity consistency (252d -> 21d 2nd diff)
def f25ft_f25_fcf_trajectory_fcfconsist_252d_jerk_v008_signal(fcf):
    base = _f25_consistency(fcf, 252)
    b = _jerk(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of ncfo positivity consistency (126d -> 21d 2nd diff)
def f25ft_f25_fcf_trajectory_ncfoconsist_126d_jerk_v009_signal(ncfo):
    base = _f25_consistency(ncfo, 126)
    b = _jerk(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of FCF conversion (fcf/ncfo) (-> 21d 2nd diff)
def f25ft_f25_fcf_trajectory_conv_jerk_v010_signal(fcf, ncfo):
    base = fcf / ncfo.replace(0, np.nan)
    b = _jerk(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of FCF level z-score (504d z -> 63d 2nd diff)
def f25ft_f25_fcf_trajectory_fcflevelz_504d_jerk_v011_signal(fcf):
    base = _z(fcf, 504)
    b = _jerk(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of ncfo level rank (504d rank -> 63d 2nd diff)
def f25ft_f25_fcf_trajectory_ncfolevelrank_504d_jerk_v012_signal(ncfo):
    base = _rank(ncfo, 504)
    b = _jerk(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of FCF margin range-position (504d band -> 63d 2nd diff)
def f25ft_f25_fcf_trajectory_fcfmargrngpos_504d_jerk_v013_signal(fcf, revenue):
    m = _f25_fcf_margin(fcf, revenue)
    hi = m.rolling(504, min_periods=252).max()
    lo = m.rolling(504, min_periods=252).min()
    base = (m - lo) / (hi - lo).replace(0, np.nan)
    b = _jerk(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of FCF drawdown vs trailing peak (504d -> 63d 2nd diff)
def f25ft_f25_fcf_trajectory_fcfdrawdown_504d_jerk_v014_signal(fcf):
    hi = fcf.rolling(504, min_periods=252).max()
    base = (fcf - hi) / hi.abs().replace(0, np.nan)
    b = _jerk(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of FCF YoY growth ranked (504d rank -> 63d 2nd diff)
def f25ft_f25_fcf_trajectory_fcfgrrank_504d_jerk_v015_signal(fcf):
    base = _rank(_f25_growth(fcf, 252), 504)
    b = _jerk(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of ncfo scale-free trend (252d -> 63d 2nd diff)
def f25ft_f25_fcf_trajectory_ncfotrend_252d_jerk_v016_signal(ncfo):
    base = _slope(ncfo, 252) / _mean(ncfo, 252).abs().replace(0, np.nan)
    b = _jerk(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of FCF scale-free trend (252d -> 63d 2nd diff)
def f25ft_f25_fcf_trajectory_fcftrendnorm_252d_jerk_v017_signal(fcf):
    base = _slope(fcf, 252) / _mean(fcf, 252).abs().replace(0, np.nan)
    b = _jerk(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of FCF margin change-vs-year-ago (252d base -> 21d 2nd diff)
def f25ft_f25_fcf_trajectory_fcfmargchg_252d_jerk_v018_signal(fcf, revenue):
    m = _f25_fcf_margin(fcf, revenue)
    base = m - m.shift(252)
    b = _jerk(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of FCF margin Sharpe-like ratio (252d -> 63d 2nd diff)
def f25ft_f25_fcf_trajectory_fcfmargsharpe_252d_jerk_v019_signal(fcf, revenue):
    m = _f25_fcf_margin(fcf, revenue)
    base = _mean(m, 252) / _std(m, 252).replace(0, np.nan)
    b = _jerk(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of ncfo margin level (-> 21d 2nd diff)
def f25ft_f25_fcf_trajectory_ncfomargin_jerk_v020_signal(ncfo, revenue):
    base = ncfo / revenue.replace(0, np.nan)
    b = _jerk(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of FCF-per-share displacement from EMA (126d -> 21d 2nd diff)
def f25ft_f25_fcf_trajectory_fcfpsdisp_126d_jerk_v021_signal(fcfps):
    ema = fcfps.ewm(span=126, min_periods=63).mean()
    base = (fcfps - ema) / ema.abs().replace(0, np.nan)
    b = _jerk(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of FCF displacement from EMA (252d -> 63d 2nd diff)
def f25ft_f25_fcf_trajectory_fcflvldisp_252d_jerk_v022_signal(fcf):
    ema = fcf.ewm(span=252, min_periods=126).mean()
    base = (fcf - ema) / ema.abs().replace(0, np.nan)
    b = _jerk(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of FCF conversion consistency, smoothed (252d -> 21d 2nd diff)
def f25ft_f25_fcf_trajectory_convconsist_252d_jerk_v023_signal(fcf, ncfo):
    conv = fcf / ncfo.replace(0, np.nan)
    base = (conv > 0.5).astype(float).rolling(252, min_periods=126).mean().ewm(span=21, min_periods=10).mean()
    b = _jerk(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of FCF margin above-median time, smoothed (252d -> 21d 2nd diff)
def f25ft_f25_fcf_trajectory_fcfmargabovemed_252d_jerk_v024_signal(fcf, revenue):
    m = _f25_fcf_margin(fcf, revenue)
    med = m.rolling(252, min_periods=126).median()
    base = (m > med).astype(float).rolling(252, min_periods=126).mean().ewm(span=21, min_periods=10).mean()
    b = _jerk(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of FCF up-day rate, smoothed (252d -> 21d 2nd diff)
def f25ft_f25_fcf_trajectory_fcfuprate_252d_jerk_v025_signal(fcf):
    base = (fcf.diff() > 0).astype(float).rolling(252, min_periods=126).mean().ewm(span=21, min_periods=10).mean()
    b = _jerk(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of FCF margin volatility (252d -> 63d 2nd diff)
def f25ft_f25_fcf_trajectory_fcfmargvol_252d_jerk_v026_signal(fcf, revenue):
    m = _f25_fcf_margin(fcf, revenue)
    base = _std(m, 252)
    b = _jerk(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of FCF growth dispersion across windows (-> 21d 2nd diff)
def f25ft_f25_fcf_trajectory_fcfgrdisp_jerk_v027_signal(fcf):
    g1 = _f25_growth(fcf, 63)
    g2 = _f25_growth(fcf, 126)
    g3 = _f25_growth(fcf, 252)
    base = pd.concat([g1, g2, g3], axis=1).std(axis=1)
    b = _jerk(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of FCF-per-share growth (126d -> 21d 2nd diff)
def f25ft_f25_fcf_trajectory_fcfpsgr_126d_jerk_v028_signal(fcfps):
    base = _f25_growth(fcfps, 126)
    b = _jerk(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of ncfo quarterly growth (63d -> 21d 2nd diff)
def f25ft_f25_fcf_trajectory_ncfogr_63d_jerk_v029_signal(ncfo):
    base = _f25_growth(ncfo, 63)
    b = _jerk(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of FCF margin EMA crossover (-> 21d 2nd diff)
def f25ft_f25_fcf_trajectory_fcfmargemacross_jerk_v030_signal(fcf, revenue):
    m = _f25_fcf_margin(fcf, revenue)
    base = m.ewm(span=42, min_periods=21).mean() - m.ewm(span=126, min_periods=63).mean()
    b = _jerk(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of FCF margin recent-vs-baseline spread (-> 21d 2nd diff)
def f25ft_f25_fcf_trajectory_fcfmargrecbase_jerk_v031_signal(fcf, revenue):
    m = _f25_fcf_margin(fcf, revenue)
    base = _mean(m, 126) - _mean(m, 504)
    b = _jerk(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of FCF recovery position (504d band -> 63d 2nd diff)
def f25ft_f25_fcf_trajectory_fcfrecovpos_504d_jerk_v032_signal(fcf):
    hi = fcf.rolling(504, min_periods=252).max()
    lo = fcf.rolling(504, min_periods=252).min()
    base = (fcf - lo) / (hi - lo).replace(0, np.nan)
    b = _jerk(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of ncfo recovery position (504d band -> 63d 2nd diff)
def f25ft_f25_fcf_trajectory_ncforecovpos_504d_jerk_v033_signal(ncfo):
    hi = ncfo.rolling(504, min_periods=252).max()
    lo = ncfo.rolling(504, min_periods=252).min()
    base = (ncfo - lo) / (hi - lo).replace(0, np.nan)
    b = _jerk(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of FCF margin percentile rank (504d rank -> 63d 2nd diff)
def f25ft_f25_fcf_trajectory_fcfmargrank_504d_jerk_v034_signal(fcf, revenue):
    base = _rank(_f25_fcf_margin(fcf, revenue), 504)
    b = _jerk(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of FCF growth EMA (126d -> 21d 2nd diff)
def f25ft_f25_fcf_trajectory_fcfgrema_126d_jerk_v035_signal(fcf):
    base = _f25_growth(fcf, 126).ewm(span=63, min_periods=31).mean()
    b = _jerk(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of ncfo growth EMA (252d -> 63d 2nd diff)
def f25ft_f25_fcf_trajectory_ncfogrema_252d_jerk_v036_signal(ncfo):
    base = _f25_growth(ncfo, 252).ewm(span=84, min_periods=42).mean()
    b = _jerk(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of ncfo growth Sharpe (-> 63d 2nd diff)
def f25ft_f25_fcf_trajectory_ncfogrsharpe_252d_jerk_v037_signal(ncfo):
    g = _f25_growth(ncfo, 63)
    base = _mean(g, 252) / _std(g, 252).replace(0, np.nan)
    b = _jerk(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of FCF margin trend rank (504d rank -> 63d 2nd diff)
def f25ft_f25_fcf_trajectory_fcfmargtrendrank_jerk_v038_signal(fcf, revenue):
    base = _rank(_f25_margin_trend(fcf, revenue, 126), 504)
    b = _jerk(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of FCF positivity EMA (-> 21d 2nd diff)
def f25ft_f25_fcf_trajectory_fcfposema_jerk_v039_signal(fcf):
    base = (fcf > 0).astype(float).ewm(span=126, min_periods=63).mean()
    b = _jerk(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of ncfo margin change (252d base -> 21d 2nd diff)
def f25ft_f25_fcf_trajectory_ncfomargchg_252d_jerk_v040_signal(ncfo, revenue):
    nm = ncfo / revenue.replace(0, np.nan)
    base = nm - nm.shift(252)
    b = _jerk(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of FCF growth asymmetry (252d -> 21d 2nd diff)
def f25ft_f25_fcf_trajectory_fcfgrasym_252d_jerk_v041_signal(fcf):
    g = _f25_growth(fcf, 63)
    up = g.clip(lower=0).rolling(252, min_periods=126).mean()
    dn = (-g.clip(upper=0)).rolling(252, min_periods=126).mean()
    base = (up - dn) / (up + dn).replace(0, np.nan)
    b = _jerk(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of FCF margin displacement (252d -> 21d 2nd diff)
def f25ft_f25_fcf_trajectory_fcfmargdisp_252d_jerk_v042_signal(fcf, revenue):
    m = _f25_fcf_margin(fcf, revenue)
    base = m - m.ewm(span=126, min_periods=63).mean()
    b = _jerk(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of FCF-vs-revenue normalized-change spread (-> 21d 2nd diff)
def f25ft_f25_fcf_trajectory_fcfrevnormchg_jerk_v043_signal(fcf, revenue):
    cf = (fcf - _mean(fcf, 252)) / _std(fcf, 252).replace(0, np.nan)
    cr = (revenue - _mean(revenue, 252)) / _std(revenue, 252).replace(0, np.nan)
    base = cf - cr
    b = _jerk(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of FCF margin width (504d -> 63d 2nd diff)
def f25ft_f25_fcf_trajectory_fcfmargwidth_504d_jerk_v044_signal(fcf, revenue):
    m = _f25_fcf_margin(fcf, revenue)
    base = m.rolling(504, min_periods=252).max() - m.rolling(504, min_periods=252).min()
    b = _jerk(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of FCF margin hit-rate, smoothed (252d -> 21d 2nd diff)
def f25ft_f25_fcf_trajectory_fcfmarghit_252d_jerk_v045_signal(fcf, revenue):
    m = _f25_fcf_margin(fcf, revenue)
    base = (m > m.shift(63)).astype(float).rolling(252, min_periods=126).mean().ewm(span=21, min_periods=10).mean()
    b = _jerk(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of ncfo scale-free recent-vs-baseline spread (-> 21d 2nd diff)
def f25ft_f25_fcf_trajectory_ncforecbase_jerk_v046_signal(ncfo):
    base = (_mean(ncfo, 63) - _mean(ncfo, 504)) / _mean(ncfo, 504).abs().replace(0, np.nan)
    b = _jerk(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of FCF margin short trend (63d trend -> 21d 2nd diff)
def f25ft_f25_fcf_trajectory_fcfmargtrend_63d_jerk_v047_signal(fcf, revenue):
    base = _f25_margin_trend(fcf, revenue, 63)
    b = _jerk(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of FCF stability score (504d -> 63d 2nd diff)
def f25ft_f25_fcf_trajectory_fcfstabscore_504d_jerk_v048_signal(fcf):
    g = _f25_growth(fcf, 63)
    base = 1.0 / (1.0 + _std(g, 504))
    b = _jerk(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of ncfo stability score (252d -> 21d 2nd diff)
def f25ft_f25_fcf_trajectory_ncfostabscore_252d_jerk_v049_signal(ncfo):
    g = _f25_growth(ncfo, 63)
    base = 1.0 / (1.0 + _std(g, 252))
    b = _jerk(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of FCF trough-recovery gap (504d -> 63d 2nd diff)
def f25ft_f25_fcf_trajectory_fcftroughrecov_504d_jerk_v050_signal(fcf):
    lo = fcf.rolling(504, min_periods=252).min()
    base = (fcf - lo) / lo.abs().replace(0, np.nan)
    b = _jerk(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of FCF YoY growth de-meaned surprise (-> 21d 2nd diff)
def f25ft_f25_fcf_trajectory_fcfgrsurprise_jerk_v051_signal(fcf):
    g = _f25_growth(fcf, 252)
    base = g - _mean(g, 504)
    b = _jerk(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of ncfo YoY growth surprise (-> 21d 2nd diff)
def f25ft_f25_fcf_trajectory_ncfogrsurprise_jerk_v052_signal(ncfo):
    g = _f25_growth(ncfo, 252)
    base = g - _mean(g, 504)
    b = _jerk(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of FCF half-year clean slope (126d -> 21d 2nd diff)
def f25ft_f25_fcf_trajectory_fcfslopecln_126d_jerk_v053_signal(fcf):
    base = _slope(fcf, 126) / _std(fcf, 126).replace(0, np.nan)
    b = _jerk(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of ncfo half-year clean slope (126d -> 21d 2nd diff)
def f25ft_f25_fcf_trajectory_ncfoslopecln_126d_jerk_v054_signal(ncfo):
    base = _slope(ncfo, 126) / _std(ncfo, 126).replace(0, np.nan)
    b = _jerk(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of FCF-per-share growth stability (-> 63d 2nd diff)
def f25ft_f25_fcf_trajectory_fcfpsgrstab_252d_jerk_v055_signal(fcfps):
    g = _f25_growth(fcfps, 63)
    base = -_std(g, 252)
    b = _jerk(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of FCF margin acceleration EMA (-> 21d 2nd diff)
def f25ft_f25_fcf_trajectory_fcfmargaccema_jerk_v056_signal(fcf, revenue):
    m = _f25_fcf_margin(fcf, revenue)
    acc = (m - m.shift(63)) - (m.shift(63) - m.shift(126))
    base = acc.ewm(span=42, min_periods=21).mean()
    b = _jerk(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of ncfo-FCF level z divergence (504d -> 63d 2nd diff)
def f25ft_f25_fcf_trajectory_ncfofcfzdiv_504d_jerk_v057_signal(ncfo, fcf):
    base = _z(ncfo, 504) - _z(fcf, 504)
    b = _jerk(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of FCF net-direction run (126d -> 21d 2nd diff)
def f25ft_f25_fcf_trajectory_fcfnetdir_126d_jerk_v058_signal(fcf):
    base = (np.sign(fcf.diff())).rolling(126, min_periods=63).mean()
    b = _jerk(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of FCF positive-quarters fraction (504d -> 63d 2nd diff)
def f25ft_f25_fcf_trajectory_fcfposqtrs_504d_jerk_v059_signal(fcf):
    qpos = (fcf.rolling(63, min_periods=42).mean() > 0).astype(float)
    base = qpos.rolling(504, min_periods=252).mean()
    b = _jerk(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of FCF margin compression depth (-> 21d 2nd diff)
def f25ft_f25_fcf_trajectory_fcfmargcompress_jerk_v060_signal(fcf, revenue):
    m = _f25_fcf_margin(fcf, revenue)
    med = m.rolling(252, min_periods=126).median()
    base = (med - m).clip(lower=0).rolling(126, min_periods=63).mean()
    b = _jerk(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of FCF level percentile rank (504d -> 63d 2nd diff)
def f25ft_f25_fcf_trajectory_fcfrank_504d_jerk_v061_signal(fcf):
    base = _rank(fcf, 504)
    b = _jerk(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of FCF-per-share level rank (504d -> 63d 2nd diff)
def f25ft_f25_fcf_trajectory_fcfpsrank_504d_jerk_v062_signal(fcfps):
    base = _rank(fcfps, 504)
    b = _jerk(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of FCF margin OLS residual ranked (-> 63d 2nd diff)
def f25ft_f25_fcf_trajectory_fcfmargresid_252d_jerk_v063_signal(fcf, revenue):
    m = _f25_fcf_margin(fcf, revenue)
    sl = _slope(m, 252)
    fitted = _mean(m, 252) + sl * (252.0 / 2.0)
    base = _rank(m - fitted, 252)
    b = _jerk(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of FCF margin sequential change EMA (-> 21d 2nd diff)
def f25ft_f25_fcf_trajectory_fcfmargseq_jerk_v064_signal(fcf, revenue):
    m = _f25_fcf_margin(fcf, revenue)
    base = (m - m.shift(63)).ewm(span=42, min_periods=21).mean()
    b = _jerk(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of FCF conversion trend interacted with level sign (-> 63d 2nd diff)
def f25ft_f25_fcf_trajectory_convtrendlvl_252d_jerk_v065_signal(fcf, ncfo):
    conv = fcf / ncfo.replace(0, np.nan)
    base = _slope(conv, 252) * np.sign(_mean(conv, 63))
    b = _jerk(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of FCF margin level (63d step view -> 63d 2nd diff)
def f25ft_f25_fcf_trajectory_fcfmargin63_jerk_v066_signal(fcf, revenue):
    base = _f25_fcf_margin(fcf, revenue)
    b = _jerk(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of ncfo margin level (63d step -> 63d 2nd diff)
def f25ft_f25_fcf_trajectory_ncfomargin63_jerk_v067_signal(ncfo, revenue):
    base = ncfo / revenue.replace(0, np.nan)
    b = _jerk(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of FCF growth flip rate, smoothed (252d -> 21d 2nd diff)
def f25ft_f25_fcf_trajectory_fcfgrflip_252d_jerk_v068_signal(fcf):
    g = _f25_growth(fcf, 63)
    base = (np.sign(g) != np.sign(g.shift(21))).astype(float).rolling(252, min_periods=126).mean().ewm(span=21, min_periods=10).mean()
    b = _jerk(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of FCF margin trend EMA (-> 21d 2nd diff)
def f25ft_f25_fcf_trajectory_fcfmargtrendema_jerk_v069_signal(fcf, revenue):
    base = _f25_margin_trend(fcf, revenue, 126).ewm(span=63, min_periods=31).mean()
    b = _jerk(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of ncfo trend per revenue scale (252d -> 63d 2nd diff)
def f25ft_f25_fcf_trajectory_ncfotrendrev_252d_jerk_v070_signal(ncfo, revenue):
    base = _slope(ncfo, 252) / _mean(revenue, 252).replace(0, np.nan)
    b = _jerk(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of ncfo EMA crossover (-> 21d 2nd diff)
def f25ft_f25_fcf_trajectory_ncfoemacross_jerk_v071_signal(ncfo):
    fast = ncfo.ewm(span=42, min_periods=21).mean()
    slow = ncfo.ewm(span=189, min_periods=90).mean()
    base = (fast - slow) / slow.abs().replace(0, np.nan)
    b = _jerk(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of FCF dollar-change per revenue (252d -> 63d 2nd diff)
def f25ft_f25_fcf_trajectory_fcfdeltarev_252d_jerk_v072_signal(fcf, revenue):
    base = (fcf - fcf.shift(252)) / _mean(revenue, 252).replace(0, np.nan)
    b = _jerk(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of ncfo dollar-change per revenue (126d -> 21d 2nd diff)
def f25ft_f25_fcf_trajectory_ncfodeltarev_126d_jerk_v073_signal(ncfo, revenue):
    base = (ncfo - ncfo.shift(126)) / _mean(revenue, 126).replace(0, np.nan)
    b = _jerk(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of FCF margin above-median streak, smoothed (-> 21d 2nd diff)
def f25ft_f25_fcf_trajectory_fcfmargabovestrk_jerk_v074_signal(fcf, revenue):
    m = _f25_fcf_margin(fcf, revenue)
    med = m.rolling(252, min_periods=126).median()
    above = (m > med).astype(float)
    grp = (above == 0).cumsum()
    base = (above.groupby(grp).cumsum() / 252.0).ewm(span=21, min_periods=10).mean()
    b = _jerk(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of FCF margin curvature level (-> 21d 2nd diff)
def f25ft_f25_fcf_trajectory_fcfmargcurv_jerk_v075_signal(fcf, revenue):
    m = _f25_fcf_margin(fcf, revenue)
    base = (m - m.shift(126)) - (m.shift(126) - m.shift(252))
    b = _jerk(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of FCF scale-free curvature ranked (252d -> 21d 2nd diff)
def f25ft_f25_fcf_trajectory_fcfcurv_252d_jerk_v076_signal(fcf):
    d1 = fcf - fcf.shift(126)
    d2 = d1 - d1.shift(126)
    base = _rank(d2 / _mean(fcf, 252).abs().replace(0, np.nan), 252)
    b = _jerk(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of ncfo scale-free curvature, ranked (252d -> 21d 2nd diff)
def f25ft_f25_fcf_trajectory_ncfocurv_252d_jerk_v077_signal(ncfo):
    d1 = ncfo - ncfo.shift(126)
    d2 = d1 - d1.shift(126)
    base = _rank(d2 / _mean(ncfo, 252).abs().replace(0, np.nan), 252)
    b = _jerk(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of FCF margin trend 504d (-> 63d 2nd diff)
def f25ft_f25_fcf_trajectory_fcfmargtrend_504d_jerk_v078_signal(fcf, revenue):
    base = _f25_margin_trend(fcf, revenue, 504)
    b = _jerk(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of FCF two-year growth (504d -> 63d 2nd diff)
def f25ft_f25_fcf_trajectory_fcfgr_504d_jerk_v079_signal(fcf):
    base = _f25_growth(fcf, 504)
    b = _jerk(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of ncfo two-year growth ranked (-> 63d 2nd diff)
def f25ft_f25_fcf_trajectory_ncfogrrk_504d_jerk_v080_signal(ncfo):
    base = _rank(_f25_growth(ncfo, 504), 252)
    b = _jerk(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of FCF growth tilt (-> 21d 2nd diff)
def f25ft_f25_fcf_trajectory_fcfgrtilt_jerk_v081_signal(fcf):
    g = _f25_growth(fcf, 63)
    base = g.ewm(span=21, min_periods=10).mean() - g.ewm(span=126, min_periods=63).mean()
    b = _jerk(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of ncfo growth tilt (-> 21d 2nd diff)
def f25ft_f25_fcf_trajectory_ncfogrtilt_jerk_v082_signal(ncfo):
    g = _f25_growth(ncfo, 63)
    base = g.ewm(span=21, min_periods=10).mean() - g.ewm(span=126, min_periods=63).mean()
    b = _jerk(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of FCF/ncfo conversion change-vs-year (252d -> 21d 2nd diff)
def f25ft_f25_fcf_trajectory_convchg_252d_jerk_v083_signal(fcf, ncfo):
    conv = fcf / ncfo.replace(0, np.nan)
    base = conv - conv.shift(252)
    b = _jerk(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of FCF margin acceleration ranked (-> 21d 2nd diff)
def f25ft_f25_fcf_trajectory_fcfmargaccrank_jerk_v084_signal(fcf, revenue):
    m = _f25_fcf_margin(fcf, revenue)
    acc = (m - m.shift(63)) - (m.shift(63) - m.shift(126))
    base = _rank(acc, 252)
    b = _jerk(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of FCF growth dispersion ratio short/long (-> 21d 2nd diff)
def f25ft_f25_fcf_trajectory_fcfgrdispratio_jerk_v085_signal(fcf):
    g = _f25_growth(fcf, 21)
    base = _std(g, 63) / _std(g, 252).replace(0, np.nan)
    b = _jerk(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of FCF level z over 252d (-> 21d 2nd diff)
def f25ft_f25_fcf_trajectory_fcflevelz_252d_jerk_v086_signal(fcf):
    base = _z(fcf, 252)
    b = _jerk(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of ncfo level z over 252d (-> 21d 2nd diff)
def f25ft_f25_fcf_trajectory_ncfolevelz_252d_jerk_v087_signal(ncfo):
    base = _z(ncfo, 252)
    b = _jerk(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of FCF margin trend-vol risk-adjusted (252d -> 63d 2nd diff)
def f25ft_f25_fcf_trajectory_fcfmargtrendvol_252d_jerk_v088_signal(fcf, revenue):
    m = _f25_fcf_margin(fcf, revenue)
    base = _slope(m, 252) / _std(m, 252).replace(0, np.nan)
    b = _jerk(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of FCF margin level interacted with trend sign (-> 21d 2nd diff)
def f25ft_f25_fcf_trajectory_fcfmarglvltrend_jerk_v089_signal(fcf, revenue):
    m = _f25_fcf_margin(fcf, revenue)
    base = _mean(m, 63) * np.sign(_slope(m, 252))
    b = _jerk(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of FCF half-year-vs-two-year growth spread (-> 21d 2nd diff)
def f25ft_f25_fcf_trajectory_fcfgrspread_jerk_v090_signal(fcf):
    base = _f25_growth(fcf, 126) - _f25_growth(fcf, 504)
    b = _jerk(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of ncfo growth spread (-> 21d 2nd diff)
def f25ft_f25_fcf_trajectory_ncfogrspread_jerk_v091_signal(ncfo):
    base = _f25_growth(ncfo, 126) - _f25_growth(ncfo, 504)
    b = _jerk(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of FCF margin change-63d (-> 21d 2nd diff)
def f25ft_f25_fcf_trajectory_fcfmargchg63_jerk_v092_signal(fcf, revenue):
    m = _f25_fcf_margin(fcf, revenue)
    base = m - m.shift(63)
    b = _jerk(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of FCF quarterly sequential growth ranked (-> 21d 2nd diff)
def f25ft_f25_fcf_trajectory_fcfseqgr_63d_jerk_v093_signal(fcf):
    base = _rank(_f25_growth(fcf, 63), 252)
    b = _jerk(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of FCF level rank momentum (504d rank diff -> 21d 2nd diff)
def f25ft_f25_fcf_trajectory_fcfrankmom_504d_jerk_v094_signal(fcf):
    r = _rank(fcf, 504)
    base = r - r.shift(252)
    b = _jerk(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of ncfo rank momentum (-> 21d 2nd diff)
def f25ft_f25_fcf_trajectory_ncforankmom_504d_jerk_v095_signal(ncfo):
    r = _rank(ncfo, 504)
    base = r - r.shift(252)
    b = _jerk(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of trend comovement (-> 63d 2nd diff)
def f25ft_f25_fcf_trajectory_trendcomove_252d_jerk_v096_signal(ncfo, fcf):
    sn = np.tanh(_slope(ncfo, 252) / _mean(ncfo, 252).abs().replace(0, np.nan))
    sf = np.tanh(_slope(fcf, 252) / _mean(fcf, 252).abs().replace(0, np.nan))
    base = sn * sf
    b = _jerk(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of FCF-per-share trend per revenue scale (-> 63d 2nd diff)
def f25ft_f25_fcf_trajectory_fcfpstrendrev_jerk_v097_signal(fcfps, revenue):
    ratio = fcfps / (revenue / 1e8).replace(0, np.nan)
    base = _slope(ratio, 252)
    b = _jerk(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of FCF margin year-over-year acceleration (-> 21d 2nd diff)
def f25ft_f25_fcf_trajectory_fcfmargyoyacc_jerk_v098_signal(fcf, revenue):
    m = _f25_fcf_margin(fcf, revenue)
    chg = m - m.shift(126)
    base = chg - chg.shift(252)
    b = _jerk(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of FCF breadth (504d -> 63d 2nd diff)
def f25ft_f25_fcf_trajectory_fcfbreadth_504d_jerk_v099_signal(fcf):
    chg = fcf - fcf.shift(63)
    base = ((chg > 0).astype(float) - (chg < 0).astype(float)).rolling(504, min_periods=252).mean()
    b = _jerk(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of FCF margin hit-rate magnitude-weighted (-> 21d 2nd diff)
def f25ft_f25_fcf_trajectory_fcfhitmag_252d_jerk_v100_signal(fcf):
    up = (fcf > fcf.shift(63)).astype(float)
    rate = up.rolling(252, min_periods=126).mean()
    mag = _f25_growth(fcf, 63).abs().rolling(252, min_periods=126).mean()
    base = rate * mag
    b = _jerk(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of FCF margin trend tanh (-> 21d 2nd diff)
def f25ft_f25_fcf_trajectory_fcfmargtanh_jerk_v101_signal(fcf, revenue):
    base = np.tanh(200.0 * _f25_margin_trend(fcf, revenue, 252))
    b = _jerk(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of FCF growth tanh (252d -> 21d 2nd diff)
def f25ft_f25_fcf_trajectory_fcfgrtanh_jerk_v102_signal(fcf):
    base = np.tanh(2.0 * _f25_growth(fcf, 252))
    b = _jerk(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of ncfo up-rate, smoothed (126d -> 21d 2nd diff)
def f25ft_f25_fcf_trajectory_ncfouprate_126d_jerk_v103_signal(ncfo):
    base = (ncfo.diff() > 0).astype(float).rolling(126, min_periods=63).mean().ewm(span=21, min_periods=10).mean()
    b = _jerk(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of FCF consistency weighted by margin (-> 21d 2nd diff)
def f25ft_f25_fcf_trajectory_fcfconsistwt_252d_jerk_v104_signal(fcf, revenue):
    cons = _f25_consistency(fcf, 252)
    base = cons * _mean(_f25_fcf_margin(fcf, revenue), 252)
    b = _jerk(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of capex-drag (ncfo trend minus FCF trend -> 63d 2nd diff)
def f25ft_f25_fcf_trajectory_capexdrag_252d_jerk_v105_signal(ncfo, fcf):
    sn = _slope(ncfo, 252) / _mean(ncfo, 252).abs().replace(0, np.nan)
    sf = _slope(fcf, 252) / _mean(fcf, 252).abs().replace(0, np.nan)
    base = sn - sf
    b = _jerk(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of FCF margin trend cleaned by consistency (-> 21d 2nd diff)
def f25ft_f25_fcf_trajectory_fcfmargcleantr_jerk_v106_signal(fcf, revenue):
    base = np.tanh(50.0 * _f25_margin_trend(fcf, revenue, 252)) * _f25_consistency(fcf, 252)
    b = _jerk(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of FCF turnaround flag (-> 21d 2nd diff)
def f25ft_f25_fcf_trajectory_fcfturn_252d_jerk_v107_signal(fcf):
    recent = _f25_consistency(fcf, 63)
    prior = _f25_consistency(fcf, 252).shift(63)
    base = recent - prior
    b = _jerk(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of FCF margin improvement-streak fraction, smoothed (-> 21d 2nd diff)
def f25ft_f25_fcf_trajectory_fcfmargimprstreak_jerk_v108_signal(fcf, revenue):
    m = _f25_fcf_margin(fcf, revenue)
    impr = (m > m.shift(252)).astype(float)
    grp = (impr == 0).cumsum()
    base = (impr.groupby(grp).cumsum() / 252.0).ewm(span=21, min_periods=10).mean()
    b = _jerk(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of FCF inflection 252d (-> 21d 2nd diff)
def f25ft_f25_fcf_trajectory_fcfinflect_252d_jerk_v109_signal(fcf):
    base = _slope(fcf, 84) - _slope(fcf, 252)
    b = _jerk(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of ncfo inflection 126d (-> 21d 2nd diff)
def f25ft_f25_fcf_trajectory_ncfoinflect_126d_jerk_v110_signal(ncfo):
    base = _slope(ncfo, 42) - _slope(ncfo, 126)
    b = _jerk(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of FCF/revenue change z-scored (252d -> 21d 2nd diff)
def f25ft_f25_fcf_trajectory_fcfrevchgz_252d_jerk_v111_signal(fcf, revenue):
    m = _f25_fcf_margin(fcf, revenue)
    base = _z(m - m.shift(126), 252)
    b = _jerk(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of FCF margin acceleration (slope-of-slope -> 63d 2nd diff)
def f25ft_f25_fcf_trajectory_fcfmargaccel_252d_jerk_v112_signal(fcf, revenue):
    tr = _f25_margin_trend(fcf, revenue, 126)
    base = tr - tr.shift(63)
    b = _jerk(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of FCF acceleration (-> 21d 2nd diff)
def f25ft_f25_fcf_trajectory_fcfaccel_252d_jerk_v113_signal(fcf):
    g = _f25_growth(fcf, 252)
    base = g - g.shift(63)
    b = _jerk(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of ncfo acceleration (-> 21d 2nd diff)
def f25ft_f25_fcf_trajectory_ncfoaccel_252d_jerk_v114_signal(ncfo):
    g = _f25_growth(ncfo, 252)
    base = g - g.shift(63)
    b = _jerk(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of FCF-per-share scale-free trend (252d -> 63d 2nd diff)
def f25ft_f25_fcf_trajectory_fcfpstrend_252d_jerk_v115_signal(fcfps):
    base = _slope(fcfps, 252) / _mean(fcfps, 252).abs().replace(0, np.nan)
    b = _jerk(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of FCF margin trend x revenue growth (-> 21d 2nd diff)
def f25ft_f25_fcf_trajectory_marggrowthx_jerk_v116_signal(fcf, revenue):
    tr = np.tanh(200.0 * _f25_margin_trend(fcf, revenue, 252))
    gr = np.tanh(3.0 * _f25_growth(revenue, 252))
    base = tr * gr
    b = _jerk(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of FCF margin EMA-fast ranked (-> 21d 2nd diff)
def f25ft_f25_fcf_trajectory_fcfmargemafast_jerk_v117_signal(fcf, revenue):
    base = _rank(_f25_fcf_margin(fcf, revenue).ewm(span=42, min_periods=21).mean(), 252)
    b = _jerk(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of ncfo level z over half year (-> 21d 2nd diff)
def f25ft_f25_fcf_trajectory_ncfozhalf_jerk_v118_signal(ncfo):
    base = _z(ncfo, 126)
    b = _jerk(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of FCF margin trend-weighted rank (-> 21d 2nd diff)
def f25ft_f25_fcf_trajectory_fcfmargtrwt_jerk_v119_signal(fcf, revenue):
    tr = _f25_margin_trend(fcf, revenue, 252)
    base = _rank(tr, 504) * np.tanh(_f25_growth(fcf, 63))
    b = _jerk(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of FCF slope-acceleration (-> 21d 2nd diff)
def f25ft_f25_fcf_trajectory_fcfslopeacc_jerk_v120_signal(fcf):
    sl = _slope(fcf, 126) / _mean(fcf, 126).abs().replace(0, np.nan)
    base = sl - sl.shift(126)
    b = _jerk(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of ncfo margin trend (252d -> 63d 2nd diff)
def f25ft_f25_fcf_trajectory_ncfomargtrend_252d_jerk_v121_signal(ncfo, revenue):
    base = _slope(ncfo / revenue.replace(0, np.nan), 252)
    b = _jerk(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of FCF-per-share vs FCF growth spread (-> 21d 2nd diff)
def f25ft_f25_fcf_trajectory_fcfpsvsfcf_jerk_v122_signal(fcfps, fcf):
    base = _f25_growth(fcfps, 252) - _f25_growth(fcf, 252)
    b = _jerk(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of FCF growth surprise z (-> 21d 2nd diff)
def f25ft_f25_fcf_trajectory_fcfgrsurprisez_jerk_v123_signal(fcf):
    g = _f25_growth(fcf, 252)
    base = _z(g - _mean(g, 504), 252)
    b = _jerk(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of FCF margin trend-vol over half year (126d -> 21d 2nd diff)
def f25ft_f25_fcf_trajectory_fcfmargtrendvol_126d_jerk_v124_signal(fcf, revenue):
    m = _f25_fcf_margin(fcf, revenue)
    base = _slope(m, 126) / _std(m, 126).replace(0, np.nan)
    b = _jerk(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of ncfo growth asymmetry (252d -> 21d 2nd diff)
def f25ft_f25_fcf_trajectory_ncfograsym_252d_jerk_v125_signal(ncfo):
    g = _f25_growth(ncfo, 63)
    up = g.clip(lower=0).rolling(252, min_periods=126).mean()
    dn = (-g.clip(upper=0)).rolling(252, min_periods=126).mean()
    base = (up - dn) / (up + dn).replace(0, np.nan)
    b = _jerk(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of FCF margin Sharpe over half year (-> 21d 2nd diff)
def f25ft_f25_fcf_trajectory_fcfmargsharpe_126d_jerk_v126_signal(fcf, revenue):
    m = _f25_fcf_margin(fcf, revenue)
    base = _mean(m, 126) / _std(m, 126).replace(0, np.nan)
    b = _jerk(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of ncfo positive-quarters x growth sign (-> 63d 2nd diff)
def f25ft_f25_fcf_trajectory_ncfoposqtrs_504d_jerk_v127_signal(ncfo):
    qpos = (ncfo.rolling(63, min_periods=42).mean() > 0).astype(float)
    base = qpos.rolling(504, min_periods=252).mean() * np.sign(_f25_growth(ncfo, 252))
    b = _jerk(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of FCF/revenue change ranked momentum (-> 21d 2nd diff)
def f25ft_f25_fcf_trajectory_fcfrevchgrank_jerk_v128_signal(fcf, revenue):
    m = _f25_fcf_margin(fcf, revenue)
    base = _rank(m - m.shift(252), 504)
    b = _jerk(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of joint FCF+ncfo inflection (-> 21d 2nd diff)
def f25ft_f25_fcf_trajectory_jointinflect_jerk_v129_signal(fcf, ncfo):
    fi = _slope(fcf, 63) - _slope(fcf, 252)
    ni = _slope(ncfo, 63) - _slope(ncfo, 252)
    base = np.tanh(fi / _mean(fcf, 252).abs().replace(0, np.nan)) \
        + np.tanh(ni / _mean(ncfo, 252).abs().replace(0, np.nan))
    b = _jerk(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of capex-efficiency drift ranked (-> 21d 2nd diff)
def f25ft_f25_fcf_trajectory_capexefftrend_jerk_v130_signal(fcf, ncfo, revenue):
    spread = fcf / revenue.replace(0, np.nan) - ncfo / revenue.replace(0, np.nan)
    base = _rank(spread - spread.shift(252), 504)
    b = _jerk(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of FCF margin short trend de-meaned (-> 21d 2nd diff)
def f25ft_f25_fcf_trajectory_fcfmargtrqdm_jerk_v131_signal(fcf, revenue):
    tr = _f25_margin_trend(fcf, revenue, 63)
    base = tr - tr.ewm(span=63, min_periods=31).mean()
    b = _jerk(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of FCF growth momentum (126d growth diff -> 21d 2nd diff)
def f25ft_f25_fcf_trajectory_fcfgrmom_126d_jerk_v132_signal(fcf):
    g = _f25_growth(fcf, 126)
    base = g - g.shift(252)
    b = _jerk(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of ncfo drift smoothed (-> 63d 2nd diff)
def f25ft_f25_fcf_trajectory_ncfodrift_504d_jerk_v133_signal(ncfo):
    base = _f25_growth(ncfo, 504).ewm(span=63, min_periods=31).mean()
    b = _jerk(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of (fcf-ncfo)/revenue spread change (-> 21d 2nd diff)
def f25ft_f25_fcf_trajectory_fcfncfomarg_jerk_v134_signal(fcf, ncfo, revenue):
    spread = fcf / revenue.replace(0, np.nan) - ncfo / revenue.replace(0, np.nan)
    base = spread - spread.shift(252)
    b = _jerk(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of FCF efficiency (margin up in shrinking revenue -> 21d 2nd diff)
def f25ft_f25_fcf_trajectory_fcfefficiency_jerk_v135_signal(fcf, revenue):
    mtr = np.tanh(200.0 * _f25_margin_trend(fcf, revenue, 252))
    base = mtr * np.sign(-_f25_growth(revenue, 252))
    b = _jerk(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of FCF growth z x consistency (-> 21d 2nd diff)
def f25ft_f25_fcf_trajectory_fcfgrzcons_jerk_v136_signal(fcf):
    base = _z(_f25_growth(fcf, 126), 252) * _f25_consistency(fcf, 252)
    b = _jerk(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of FCF margin z fast (-> 5d 2nd diff)
def f25ft_f25_fcf_trajectory_fcfmarginzfast_jerk_v137_signal(fcf, revenue):
    base = _z(_f25_fcf_margin(fcf, revenue), 252)
    b = _jerk(base, 5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of ncfo margin z fast (-> 5d 2nd diff)
def f25ft_f25_fcf_trajectory_ncfomarginzfast_jerk_v138_signal(ncfo, revenue):
    base = _z(ncfo / revenue.replace(0, np.nan), 252)
    b = _jerk(base, 5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of FCF quarterly growth ranked fast (-> 5d 2nd diff)
def f25ft_f25_fcf_trajectory_fcfqgr_fast_jerk_v139_signal(fcf):
    base = _rank(_f25_growth(fcf, 63), 252)
    b = _jerk(base, 5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of FCF margin change x revenue rank (-> 21d 2nd diff)
def f25ft_f25_fcf_trajectory_fcfmargchgscale_jerk_v140_signal(fcf, revenue):
    m = _f25_fcf_margin(fcf, revenue)
    base = (m - m.shift(252)) * (_rank(revenue, 504) + 0.5)
    b = _jerk(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of FCF net-direction (quarter window -> 21d 2nd diff)
def f25ft_f25_fcf_trajectory_fcfnetdir_fast_jerk_v141_signal(fcf):
    base = (np.sign(fcf.diff())).rolling(63, min_periods=31).mean()
    b = _jerk(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of FCF margin residual fast (-> 5d 2nd diff)
def f25ft_f25_fcf_trajectory_fcfmargresidfast_jerk_v142_signal(fcf, revenue):
    m = _f25_fcf_margin(fcf, revenue)
    base = m - m.ewm(span=63, min_periods=31).mean()
    b = _jerk(base, 5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of FCF conversion trend (252d -> 21d 2nd diff)
def f25ft_f25_fcf_trajectory_convtrend_252d_jerk_v143_signal(fcf, ncfo):
    conv = fcf / ncfo.replace(0, np.nan)
    base = _slope(conv, 252)
    b = _jerk(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of FCF margin above-median fraction over half year (-> 21d 2nd diff)
def f25ft_f25_fcf_trajectory_fcfmargabovemed126_jerk_v144_signal(fcf, revenue):
    m = _f25_fcf_margin(fcf, revenue)
    med = m.rolling(126, min_periods=63).median()
    base = (m > med).astype(float).rolling(126, min_periods=63).mean().ewm(span=21, min_periods=10).mean()
    b = _jerk(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of FCF growth dispersion across short windows (-> 21d 2nd diff)
def f25ft_f25_fcf_trajectory_fcfgrdisp126_jerk_v145_signal(fcf):
    g1 = _f25_growth(fcf, 42)
    g2 = _f25_growth(fcf, 84)
    g3 = _f25_growth(fcf, 126)
    base = pd.concat([g1, g2, g3], axis=1).std(axis=1)
    b = _jerk(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of ncfo margin Sharpe-like (-> 21d 2nd diff)
def f25ft_f25_fcf_trajectory_ncfomargsharpe_jerk_v146_signal(ncfo, revenue):
    nm = ncfo / revenue.replace(0, np.nan)
    base = _mean(nm, 252) / _std(nm, 252).replace(0, np.nan)
    b = _jerk(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of FCF consistency over half year, smoothed (-> 21d 2nd diff)
def f25ft_f25_fcf_trajectory_fcfconsist126_jerk_v147_signal(fcf):
    base = _f25_consistency(fcf, 126).ewm(span=21, min_periods=10).mean()
    b = _jerk(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of FCF margin trend long-span ranked (504d -> 63d 2nd diff)
def f25ft_f25_fcf_trajectory_fcfmargtrend504rk_jerk_v148_signal(fcf, revenue):
    base = _rank(_f25_margin_trend(fcf, revenue, 504), 252)
    b = _jerk(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of FCF level rank over a year (252d rank -> 21d 2nd diff)
def f25ft_f25_fcf_trajectory_fcfrank252_jerk_v149_signal(fcf):
    base = _rank(fcf, 252)
    b = _jerk(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of composite cash trajectory (blended trends -> 21d 2nd diff)
def f25ft_f25_fcf_trajectory_cashtrajcomp_jerk_v150_signal(fcf, ncfo, revenue):
    tf = np.tanh(_slope(fcf, 252) / _mean(fcf, 252).abs().replace(0, np.nan))
    tn = np.tanh(_slope(ncfo, 252) / _mean(ncfo, 252).abs().replace(0, np.nan))
    tm = np.tanh(200.0 * _f25_margin_trend(fcf, revenue, 252))
    base = tf + tn + tm
    b = _jerk(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f25ft_f25_fcf_trajectory_fcfgr_252d_jerk_v001_signal,
    f25ft_f25_fcf_trajectory_fcfgr_126d_jerk_v002_signal,
    f25ft_f25_fcf_trajectory_ncfogr_252d_jerk_v003_signal,
    f25ft_f25_fcf_trajectory_fcfpsgr_252d_jerk_v004_signal,
    f25ft_f25_fcf_trajectory_fcfmargin_jerk_v005_signal,
    f25ft_f25_fcf_trajectory_fcfmargtrend_252d_jerk_v006_signal,
    f25ft_f25_fcf_trajectory_fcfmargtrend_126d_jerk_v007_signal,
    f25ft_f25_fcf_trajectory_fcfconsist_252d_jerk_v008_signal,
    f25ft_f25_fcf_trajectory_ncfoconsist_126d_jerk_v009_signal,
    f25ft_f25_fcf_trajectory_conv_jerk_v010_signal,
    f25ft_f25_fcf_trajectory_fcflevelz_504d_jerk_v011_signal,
    f25ft_f25_fcf_trajectory_ncfolevelrank_504d_jerk_v012_signal,
    f25ft_f25_fcf_trajectory_fcfmargrngpos_504d_jerk_v013_signal,
    f25ft_f25_fcf_trajectory_fcfdrawdown_504d_jerk_v014_signal,
    f25ft_f25_fcf_trajectory_fcfgrrank_504d_jerk_v015_signal,
    f25ft_f25_fcf_trajectory_ncfotrend_252d_jerk_v016_signal,
    f25ft_f25_fcf_trajectory_fcftrendnorm_252d_jerk_v017_signal,
    f25ft_f25_fcf_trajectory_fcfmargchg_252d_jerk_v018_signal,
    f25ft_f25_fcf_trajectory_fcfmargsharpe_252d_jerk_v019_signal,
    f25ft_f25_fcf_trajectory_ncfomargin_jerk_v020_signal,
    f25ft_f25_fcf_trajectory_fcfpsdisp_126d_jerk_v021_signal,
    f25ft_f25_fcf_trajectory_fcflvldisp_252d_jerk_v022_signal,
    f25ft_f25_fcf_trajectory_convconsist_252d_jerk_v023_signal,
    f25ft_f25_fcf_trajectory_fcfmargabovemed_252d_jerk_v024_signal,
    f25ft_f25_fcf_trajectory_fcfuprate_252d_jerk_v025_signal,
    f25ft_f25_fcf_trajectory_fcfmargvol_252d_jerk_v026_signal,
    f25ft_f25_fcf_trajectory_fcfgrdisp_jerk_v027_signal,
    f25ft_f25_fcf_trajectory_fcfpsgr_126d_jerk_v028_signal,
    f25ft_f25_fcf_trajectory_ncfogr_63d_jerk_v029_signal,
    f25ft_f25_fcf_trajectory_fcfmargemacross_jerk_v030_signal,
    f25ft_f25_fcf_trajectory_fcfmargrecbase_jerk_v031_signal,
    f25ft_f25_fcf_trajectory_fcfrecovpos_504d_jerk_v032_signal,
    f25ft_f25_fcf_trajectory_ncforecovpos_504d_jerk_v033_signal,
    f25ft_f25_fcf_trajectory_fcfmargrank_504d_jerk_v034_signal,
    f25ft_f25_fcf_trajectory_fcfgrema_126d_jerk_v035_signal,
    f25ft_f25_fcf_trajectory_ncfogrema_252d_jerk_v036_signal,
    f25ft_f25_fcf_trajectory_ncfogrsharpe_252d_jerk_v037_signal,
    f25ft_f25_fcf_trajectory_fcfmargtrendrank_jerk_v038_signal,
    f25ft_f25_fcf_trajectory_fcfposema_jerk_v039_signal,
    f25ft_f25_fcf_trajectory_ncfomargchg_252d_jerk_v040_signal,
    f25ft_f25_fcf_trajectory_fcfgrasym_252d_jerk_v041_signal,
    f25ft_f25_fcf_trajectory_fcfmargdisp_252d_jerk_v042_signal,
    f25ft_f25_fcf_trajectory_fcfrevnormchg_jerk_v043_signal,
    f25ft_f25_fcf_trajectory_fcfmargwidth_504d_jerk_v044_signal,
    f25ft_f25_fcf_trajectory_fcfmarghit_252d_jerk_v045_signal,
    f25ft_f25_fcf_trajectory_ncforecbase_jerk_v046_signal,
    f25ft_f25_fcf_trajectory_fcfmargtrend_63d_jerk_v047_signal,
    f25ft_f25_fcf_trajectory_fcfstabscore_504d_jerk_v048_signal,
    f25ft_f25_fcf_trajectory_ncfostabscore_252d_jerk_v049_signal,
    f25ft_f25_fcf_trajectory_fcftroughrecov_504d_jerk_v050_signal,
    f25ft_f25_fcf_trajectory_fcfgrsurprise_jerk_v051_signal,
    f25ft_f25_fcf_trajectory_ncfogrsurprise_jerk_v052_signal,
    f25ft_f25_fcf_trajectory_fcfslopecln_126d_jerk_v053_signal,
    f25ft_f25_fcf_trajectory_ncfoslopecln_126d_jerk_v054_signal,
    f25ft_f25_fcf_trajectory_fcfpsgrstab_252d_jerk_v055_signal,
    f25ft_f25_fcf_trajectory_fcfmargaccema_jerk_v056_signal,
    f25ft_f25_fcf_trajectory_ncfofcfzdiv_504d_jerk_v057_signal,
    f25ft_f25_fcf_trajectory_fcfnetdir_126d_jerk_v058_signal,
    f25ft_f25_fcf_trajectory_fcfposqtrs_504d_jerk_v059_signal,
    f25ft_f25_fcf_trajectory_fcfmargcompress_jerk_v060_signal,
    f25ft_f25_fcf_trajectory_fcfrank_504d_jerk_v061_signal,
    f25ft_f25_fcf_trajectory_fcfpsrank_504d_jerk_v062_signal,
    f25ft_f25_fcf_trajectory_fcfmargresid_252d_jerk_v063_signal,
    f25ft_f25_fcf_trajectory_fcfmargseq_jerk_v064_signal,
    f25ft_f25_fcf_trajectory_convtrendlvl_252d_jerk_v065_signal,
    f25ft_f25_fcf_trajectory_fcfmargin63_jerk_v066_signal,
    f25ft_f25_fcf_trajectory_ncfomargin63_jerk_v067_signal,
    f25ft_f25_fcf_trajectory_fcfgrflip_252d_jerk_v068_signal,
    f25ft_f25_fcf_trajectory_fcfmargtrendema_jerk_v069_signal,
    f25ft_f25_fcf_trajectory_ncfotrendrev_252d_jerk_v070_signal,
    f25ft_f25_fcf_trajectory_ncfoemacross_jerk_v071_signal,
    f25ft_f25_fcf_trajectory_fcfdeltarev_252d_jerk_v072_signal,
    f25ft_f25_fcf_trajectory_ncfodeltarev_126d_jerk_v073_signal,
    f25ft_f25_fcf_trajectory_fcfmargabovestrk_jerk_v074_signal,
    f25ft_f25_fcf_trajectory_fcfmargcurv_jerk_v075_signal,
    f25ft_f25_fcf_trajectory_fcfcurv_252d_jerk_v076_signal,
    f25ft_f25_fcf_trajectory_ncfocurv_252d_jerk_v077_signal,
    f25ft_f25_fcf_trajectory_fcfmargtrend_504d_jerk_v078_signal,
    f25ft_f25_fcf_trajectory_fcfgr_504d_jerk_v079_signal,
    f25ft_f25_fcf_trajectory_ncfogrrk_504d_jerk_v080_signal,
    f25ft_f25_fcf_trajectory_fcfgrtilt_jerk_v081_signal,
    f25ft_f25_fcf_trajectory_ncfogrtilt_jerk_v082_signal,
    f25ft_f25_fcf_trajectory_convchg_252d_jerk_v083_signal,
    f25ft_f25_fcf_trajectory_fcfmargaccrank_jerk_v084_signal,
    f25ft_f25_fcf_trajectory_fcfgrdispratio_jerk_v085_signal,
    f25ft_f25_fcf_trajectory_fcflevelz_252d_jerk_v086_signal,
    f25ft_f25_fcf_trajectory_ncfolevelz_252d_jerk_v087_signal,
    f25ft_f25_fcf_trajectory_fcfmargtrendvol_252d_jerk_v088_signal,
    f25ft_f25_fcf_trajectory_fcfmarglvltrend_jerk_v089_signal,
    f25ft_f25_fcf_trajectory_fcfgrspread_jerk_v090_signal,
    f25ft_f25_fcf_trajectory_ncfogrspread_jerk_v091_signal,
    f25ft_f25_fcf_trajectory_fcfmargchg63_jerk_v092_signal,
    f25ft_f25_fcf_trajectory_fcfseqgr_63d_jerk_v093_signal,
    f25ft_f25_fcf_trajectory_fcfrankmom_504d_jerk_v094_signal,
    f25ft_f25_fcf_trajectory_ncforankmom_504d_jerk_v095_signal,
    f25ft_f25_fcf_trajectory_trendcomove_252d_jerk_v096_signal,
    f25ft_f25_fcf_trajectory_fcfpstrendrev_jerk_v097_signal,
    f25ft_f25_fcf_trajectory_fcfmargyoyacc_jerk_v098_signal,
    f25ft_f25_fcf_trajectory_fcfbreadth_504d_jerk_v099_signal,
    f25ft_f25_fcf_trajectory_fcfhitmag_252d_jerk_v100_signal,
    f25ft_f25_fcf_trajectory_fcfmargtanh_jerk_v101_signal,
    f25ft_f25_fcf_trajectory_fcfgrtanh_jerk_v102_signal,
    f25ft_f25_fcf_trajectory_ncfouprate_126d_jerk_v103_signal,
    f25ft_f25_fcf_trajectory_fcfconsistwt_252d_jerk_v104_signal,
    f25ft_f25_fcf_trajectory_capexdrag_252d_jerk_v105_signal,
    f25ft_f25_fcf_trajectory_fcfmargcleantr_jerk_v106_signal,
    f25ft_f25_fcf_trajectory_fcfturn_252d_jerk_v107_signal,
    f25ft_f25_fcf_trajectory_fcfmargimprstreak_jerk_v108_signal,
    f25ft_f25_fcf_trajectory_fcfinflect_252d_jerk_v109_signal,
    f25ft_f25_fcf_trajectory_ncfoinflect_126d_jerk_v110_signal,
    f25ft_f25_fcf_trajectory_fcfrevchgz_252d_jerk_v111_signal,
    f25ft_f25_fcf_trajectory_fcfmargaccel_252d_jerk_v112_signal,
    f25ft_f25_fcf_trajectory_fcfaccel_252d_jerk_v113_signal,
    f25ft_f25_fcf_trajectory_ncfoaccel_252d_jerk_v114_signal,
    f25ft_f25_fcf_trajectory_fcfpstrend_252d_jerk_v115_signal,
    f25ft_f25_fcf_trajectory_marggrowthx_jerk_v116_signal,
    f25ft_f25_fcf_trajectory_fcfmargemafast_jerk_v117_signal,
    f25ft_f25_fcf_trajectory_ncfozhalf_jerk_v118_signal,
    f25ft_f25_fcf_trajectory_fcfmargtrwt_jerk_v119_signal,
    f25ft_f25_fcf_trajectory_fcfslopeacc_jerk_v120_signal,
    f25ft_f25_fcf_trajectory_ncfomargtrend_252d_jerk_v121_signal,
    f25ft_f25_fcf_trajectory_fcfpsvsfcf_jerk_v122_signal,
    f25ft_f25_fcf_trajectory_fcfgrsurprisez_jerk_v123_signal,
    f25ft_f25_fcf_trajectory_fcfmargtrendvol_126d_jerk_v124_signal,
    f25ft_f25_fcf_trajectory_ncfograsym_252d_jerk_v125_signal,
    f25ft_f25_fcf_trajectory_fcfmargsharpe_126d_jerk_v126_signal,
    f25ft_f25_fcf_trajectory_ncfoposqtrs_504d_jerk_v127_signal,
    f25ft_f25_fcf_trajectory_fcfrevchgrank_jerk_v128_signal,
    f25ft_f25_fcf_trajectory_jointinflect_jerk_v129_signal,
    f25ft_f25_fcf_trajectory_capexefftrend_jerk_v130_signal,
    f25ft_f25_fcf_trajectory_fcfmargtrqdm_jerk_v131_signal,
    f25ft_f25_fcf_trajectory_fcfgrmom_126d_jerk_v132_signal,
    f25ft_f25_fcf_trajectory_ncfodrift_504d_jerk_v133_signal,
    f25ft_f25_fcf_trajectory_fcfncfomarg_jerk_v134_signal,
    f25ft_f25_fcf_trajectory_fcfefficiency_jerk_v135_signal,
    f25ft_f25_fcf_trajectory_fcfgrzcons_jerk_v136_signal,
    f25ft_f25_fcf_trajectory_fcfmarginzfast_jerk_v137_signal,
    f25ft_f25_fcf_trajectory_ncfomarginzfast_jerk_v138_signal,
    f25ft_f25_fcf_trajectory_fcfqgr_fast_jerk_v139_signal,
    f25ft_f25_fcf_trajectory_fcfmargchgscale_jerk_v140_signal,
    f25ft_f25_fcf_trajectory_fcfnetdir_fast_jerk_v141_signal,
    f25ft_f25_fcf_trajectory_fcfmargresidfast_jerk_v142_signal,
    f25ft_f25_fcf_trajectory_convtrend_252d_jerk_v143_signal,
    f25ft_f25_fcf_trajectory_fcfmargabovemed126_jerk_v144_signal,
    f25ft_f25_fcf_trajectory_fcfgrdisp126_jerk_v145_signal,
    f25ft_f25_fcf_trajectory_ncfomargsharpe_jerk_v146_signal,
    f25ft_f25_fcf_trajectory_fcfconsist126_jerk_v147_signal,
    f25ft_f25_fcf_trajectory_fcfmargtrend504rk_jerk_v148_signal,
    f25ft_f25_fcf_trajectory_fcfrank252_jerk_v149_signal,
    f25ft_f25_fcf_trajectory_cashtrajcomp_jerk_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F25_FCF_TRAJECTORY_REGISTRY_JERK_001_150 = REGISTRY


def _fund(seed, n, base=1e8, drift=0.02, vol=0.05, allow_neg=False):
    g = np.random.default_rng(seed)
    steps = np.repeat(g.normal(drift, vol, n // 63 + 1), 63)[:n]
    s = base * np.exp(np.cumsum(steps / 63))
    if allow_neg:
        s = s - base * 0.3
    return pd.Series(s, name=None)


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    fcf = _fund(3, n, base=8e7, drift=0.0, vol=0.55, allow_neg=True).rename("fcf")
    fcfps = _fund(5, n, base=3.0, drift=0.0, vol=0.55, allow_neg=True).rename("fcfps")
    ncfo = _fund(7, n, base=1.2e8, drift=0.0, vol=0.55, allow_neg=True).rename("ncfo")
    revenue = _fund(4, n, base=5e8, drift=0.01, vol=0.30).rename("revenue")

    cols = {"fcf": fcf, "fcfps": fcfps, "ncfo": ncfo, "revenue": revenue}

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
        assert q.nunique() > 50, "%s nunique=%d" % (name, q.nunique())
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

    print("OK f25_fcf_trajectory_3rd_derivatives_001_150_claude: %d features pass" % n_features)
