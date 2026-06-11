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


def _z(s, w):
    m = s.rolling(w, min_periods=max(1, w // 2)).mean()
    sd = s.rolling(w, min_periods=max(1, w // 2)).std()
    return (s - m) / sd.replace(0, np.nan)


def _mean(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def _std(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).std()


def _rmax(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).max()


def _rmin(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).min()


def _rank(s, w):
    return s.rolling(w, min_periods=max(1, w // 4)).rank(pct=True) - 0.5


def _dilution(sharesbas, w):
    return np.log(sharesbas.replace(0, np.nan) / sharesbas.shift(w).replace(0, np.nan))


def _antidilution(sharesbas, w):
    return -np.log(sharesbas.replace(0, np.nan) / sharesbas.shift(w).replace(0, np.nan))


def _fcf_margin(fcf, revenue):
    return fcf / revenue.replace(0, np.nan)


def _fcf_per_share(fcf, sharesbas):
    return fcf / sharesbas.replace(0, np.nan)


def _bvps(equity, sharesbas):
    return equity / sharesbas.replace(0, np.nan)


def _pos_frac(s, w):
    pos = (s > 0).astype(float)
    return pos.rolling(w, min_periods=max(1, w // 2)).mean()


def _equity_growth(equity, w):
    return np.log(equity.replace(0, np.nan) / equity.shift(w).replace(0, np.nan))


def _rev_growth(revenue, w):
    return np.log(revenue.replace(0, np.nan) / revenue.shift(w).replace(0, np.nan))


def _roic_stability(roic, w):
    m = roic.rolling(w, min_periods=max(1, w // 2)).mean()
    sd = roic.rolling(w, min_periods=max(1, w // 2)).std()
    return m / sd.replace(0, np.nan)


def _quality(roic, fcf, revenue):
    fm = fcf / revenue.replace(0, np.nan)
    return np.tanh(3.0 * roic) + np.tanh(3.0 * fm)


def f37pq_f37_producer_quality_compounder_qmd_126d_jerk_v001_signal(roic, sharesbas):
    base = np.tanh(_roic_stability(roic, 126)) - 5.0 * _dilution(sharesbas, 126)
    d = base.diff(21).diff(21) / float(21 * 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f37pq_f37_producer_quality_compounder_qmdx_126d_jerk_v002_signal(roic, sharesbas):
    raw = np.tanh(_roic_stability(roic, 126)) - 5.0 * _dilution(sharesbas, 126)
    base = _mean(raw, 21)
    d = base.diff(42).diff(42) / float(42 * 42)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f37pq_f37_producer_quality_compounder_qmd_252d_jerk_v003_signal(roic, sharesbas):
    base = np.tanh(_roic_stability(roic, 252)) - 5.0 * _dilution(sharesbas, 252)
    d = base.diff(21).diff(21) / float(21 * 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f37pq_f37_producer_quality_compounder_qmdx_252d_jerk_v004_signal(roic, sharesbas):
    raw = np.tanh(_roic_stability(roic, 252)) - 5.0 * _dilution(sharesbas, 252)
    base = _z(raw, 252)
    d = base.diff(63).diff(63) / float(63 * 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f37pq_f37_producer_quality_compounder_qmd_504d_jerk_v005_signal(roic, sharesbas):
    base = np.tanh(_roic_stability(roic, 504)) - 5.0 * _dilution(sharesbas, 504)
    d = base.diff(63).diff(63) / float(63 * 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f37pq_f37_producer_quality_compounder_qmdx_504d_jerk_v006_signal(roic, sharesbas):
    raw = np.tanh(_roic_stability(roic, 504)) - 5.0 * _dilution(sharesbas, 504)
    base = np.tanh(raw)
    d = base.diff(126).diff(126) / float(126 * 126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f37pq_f37_producer_quality_compounder_fcfdil_126d_jerk_v007_signal(fcf, revenue, sharesbas):
    base = np.tanh(3.0 * _mean(_fcf_margin(fcf, revenue), 63)) * (1.0 + np.tanh(8.0 * _antidilution(sharesbas, 126)))
    d = base.diff(21).diff(21) / float(21 * 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f37pq_f37_producer_quality_compounder_fcfdilx_126d_jerk_v008_signal(fcf, revenue, sharesbas):
    raw = np.tanh(3.0 * _mean(_fcf_margin(fcf, revenue), 63)) * (1.0 + np.tanh(8.0 * _antidilution(sharesbas, 126)))
    base = _mean(raw, 21)
    d = base.diff(42).diff(42) / float(42 * 42)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f37pq_f37_producer_quality_compounder_fcfdil_252d_jerk_v009_signal(fcf, revenue, sharesbas):
    base = np.tanh(3.0 * _mean(_fcf_margin(fcf, revenue), 63)) * (1.0 + np.tanh(8.0 * _antidilution(sharesbas, 252)))
    d = base.diff(21).diff(21) / float(21 * 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f37pq_f37_producer_quality_compounder_fcfdilx_252d_jerk_v010_signal(fcf, revenue, sharesbas):
    raw = np.tanh(3.0 * _mean(_fcf_margin(fcf, revenue), 63)) * (1.0 + np.tanh(8.0 * _antidilution(sharesbas, 252)))
    base = _z(raw, 252)
    d = base.diff(63).diff(63) / float(63 * 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f37pq_f37_producer_quality_compounder_fcfdil_504d_jerk_v011_signal(fcf, revenue, sharesbas):
    base = np.tanh(3.0 * _mean(_fcf_margin(fcf, revenue), 63)) * (1.0 + np.tanh(8.0 * _antidilution(sharesbas, 504)))
    d = base.diff(63).diff(63) / float(63 * 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f37pq_f37_producer_quality_compounder_fcfdilx_504d_jerk_v012_signal(fcf, revenue, sharesbas):
    raw = np.tanh(3.0 * _mean(_fcf_margin(fcf, revenue), 63)) * (1.0 + np.tanh(8.0 * _antidilution(sharesbas, 504)))
    base = np.tanh(raw)
    d = base.diff(126).diff(126) / float(126 * 126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f37pq_f37_producer_quality_compounder_durable_126d_jerk_v013_signal(roic, fcf):
    base = _pos_frac(roic, 126) * _pos_frac(fcf, 126)
    d = base.diff(21).diff(21) / float(21 * 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f37pq_f37_producer_quality_compounder_durablex_126d_jerk_v014_signal(roic, fcf):
    raw = _pos_frac(roic, 126) * _pos_frac(fcf, 126)
    base = _mean(raw, 21)
    d = base.diff(42).diff(42) / float(42 * 42)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f37pq_f37_producer_quality_compounder_durable_252d_jerk_v015_signal(roic, fcf):
    base = _pos_frac(roic, 252) * _pos_frac(fcf, 252)
    d = base.diff(21).diff(21) / float(21 * 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f37pq_f37_producer_quality_compounder_durablex_252d_jerk_v016_signal(roic, fcf):
    raw = _pos_frac(roic, 252) * _pos_frac(fcf, 252)
    base = _z(raw, 252)
    d = base.diff(63).diff(63) / float(63 * 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f37pq_f37_producer_quality_compounder_durable_504d_jerk_v017_signal(roic, fcf):
    base = _pos_frac(roic, 504) * _pos_frac(fcf, 504)
    d = base.diff(63).diff(63) / float(63 * 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f37pq_f37_producer_quality_compounder_durablex_504d_jerk_v018_signal(roic, fcf):
    raw = _pos_frac(roic, 504) * _pos_frac(fcf, 504)
    base = np.tanh(raw)
    d = base.diff(126).diff(126) / float(126 * 126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f37pq_f37_producer_quality_compounder_qual_126d_jerk_v019_signal(roic, fcf, revenue):
    base = _mean(np.tanh(3.0 * roic) * _fcf_margin(fcf, revenue), 126)
    d = base.diff(21).diff(21) / float(21 * 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f37pq_f37_producer_quality_compounder_qualx_126d_jerk_v020_signal(roic, fcf, revenue):
    raw = _mean(np.tanh(3.0 * roic) * _fcf_margin(fcf, revenue), 126)
    base = _mean(raw, 21)
    d = base.diff(42).diff(42) / float(42 * 42)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f37pq_f37_producer_quality_compounder_qual_252d_jerk_v021_signal(roic, fcf, revenue):
    base = _mean(np.tanh(3.0 * roic) * _fcf_margin(fcf, revenue), 252)
    d = base.diff(21).diff(21) / float(21 * 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f37pq_f37_producer_quality_compounder_qualx_252d_jerk_v022_signal(roic, fcf, revenue):
    raw = _mean(np.tanh(3.0 * roic) * _fcf_margin(fcf, revenue), 252)
    base = _z(raw, 252)
    d = base.diff(63).diff(63) / float(63 * 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f37pq_f37_producer_quality_compounder_qual_504d_jerk_v023_signal(roic, fcf, revenue):
    base = _mean(np.tanh(3.0 * roic) * _fcf_margin(fcf, revenue), 504)
    d = base.diff(63).diff(63) / float(63 * 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f37pq_f37_producer_quality_compounder_qualx_504d_jerk_v024_signal(roic, fcf, revenue):
    raw = _mean(np.tanh(3.0 * roic) * _fcf_margin(fcf, revenue), 504)
    base = np.tanh(raw)
    d = base.diff(126).diff(126) / float(126 * 126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f37pq_f37_producer_quality_compounder_bvpsg_126d_jerk_v025_signal(equity, sharesbas):
    base = np.log(_bvps(equity, sharesbas).replace(0, np.nan) / _bvps(equity, sharesbas).shift(126).replace(0, np.nan))
    d = base.diff(21).diff(21) / float(21 * 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f37pq_f37_producer_quality_compounder_bvpsgx_126d_jerk_v026_signal(equity, sharesbas):
    raw = np.log(_bvps(equity, sharesbas).replace(0, np.nan) / _bvps(equity, sharesbas).shift(126).replace(0, np.nan))
    base = _mean(raw, 21)
    d = base.diff(42).diff(42) / float(42 * 42)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f37pq_f37_producer_quality_compounder_bvpsg_252d_jerk_v027_signal(equity, sharesbas):
    base = np.log(_bvps(equity, sharesbas).replace(0, np.nan) / _bvps(equity, sharesbas).shift(252).replace(0, np.nan))
    d = base.diff(21).diff(21) / float(21 * 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f37pq_f37_producer_quality_compounder_bvpsgx_252d_jerk_v028_signal(equity, sharesbas):
    raw = np.log(_bvps(equity, sharesbas).replace(0, np.nan) / _bvps(equity, sharesbas).shift(252).replace(0, np.nan))
    base = _z(raw, 252)
    d = base.diff(63).diff(63) / float(63 * 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f37pq_f37_producer_quality_compounder_bvpsg_504d_jerk_v029_signal(equity, sharesbas):
    base = np.log(_bvps(equity, sharesbas).replace(0, np.nan) / _bvps(equity, sharesbas).shift(504).replace(0, np.nan))
    d = base.diff(63).diff(63) / float(63 * 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f37pq_f37_producer_quality_compounder_bvpsgx_504d_jerk_v030_signal(equity, sharesbas):
    raw = np.log(_bvps(equity, sharesbas).replace(0, np.nan) / _bvps(equity, sharesbas).shift(504).replace(0, np.nan))
    base = np.tanh(raw)
    d = base.diff(126).diff(126) / float(126 * 126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f37pq_f37_producer_quality_compounder_roicz_126d_jerk_v031_signal(roic, netmargin):
    base = _z(roic, 126) * np.tanh(5.0 * netmargin)
    d = base.diff(21).diff(21) / float(21 * 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f37pq_f37_producer_quality_compounder_roiczx_126d_jerk_v032_signal(roic, netmargin):
    raw = _z(roic, 126) * np.tanh(5.0 * netmargin)
    base = _mean(raw, 21)
    d = base.diff(42).diff(42) / float(42 * 42)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f37pq_f37_producer_quality_compounder_roicz_252d_jerk_v033_signal(roic, netmargin):
    base = _z(roic, 252) * np.tanh(5.0 * netmargin)
    d = base.diff(21).diff(21) / float(21 * 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f37pq_f37_producer_quality_compounder_roiczx_252d_jerk_v034_signal(roic, netmargin):
    raw = _z(roic, 252) * np.tanh(5.0 * netmargin)
    base = _z(raw, 252)
    d = base.diff(63).diff(63) / float(63 * 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f37pq_f37_producer_quality_compounder_roicz_504d_jerk_v035_signal(roic, netmargin):
    base = _z(roic, 504) * np.tanh(5.0 * netmargin)
    d = base.diff(63).diff(63) / float(63 * 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f37pq_f37_producer_quality_compounder_roiczx_504d_jerk_v036_signal(roic, netmargin):
    raw = _z(roic, 504) * np.tanh(5.0 * netmargin)
    base = np.tanh(raw)
    d = base.diff(126).diff(126) / float(126 * 126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f37pq_f37_producer_quality_compounder_profgrow_126d_jerk_v037_signal(revenue, fcf):
    base = _rev_growth(revenue, 126) * np.tanh(3.0 * _fcf_margin(fcf, revenue))
    d = base.diff(21).diff(21) / float(21 * 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f37pq_f37_producer_quality_compounder_profgrowx_126d_jerk_v038_signal(revenue, fcf):
    raw = _rev_growth(revenue, 126) * np.tanh(3.0 * _fcf_margin(fcf, revenue))
    base = _mean(raw, 21)
    d = base.diff(42).diff(42) / float(42 * 42)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f37pq_f37_producer_quality_compounder_profgrow_252d_jerk_v039_signal(revenue, fcf):
    base = _rev_growth(revenue, 252) * np.tanh(3.0 * _fcf_margin(fcf, revenue))
    d = base.diff(21).diff(21) / float(21 * 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f37pq_f37_producer_quality_compounder_profgrowx_252d_jerk_v040_signal(revenue, fcf):
    raw = _rev_growth(revenue, 252) * np.tanh(3.0 * _fcf_margin(fcf, revenue))
    base = _z(raw, 252)
    d = base.diff(63).diff(63) / float(63 * 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f37pq_f37_producer_quality_compounder_profgrow_504d_jerk_v041_signal(revenue, fcf):
    base = _rev_growth(revenue, 504) * np.tanh(3.0 * _fcf_margin(fcf, revenue))
    d = base.diff(63).diff(63) / float(63 * 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f37pq_f37_producer_quality_compounder_profgrowx_504d_jerk_v042_signal(revenue, fcf):
    raw = _rev_growth(revenue, 504) * np.tanh(3.0 * _fcf_margin(fcf, revenue))
    base = np.tanh(raw)
    d = base.diff(126).diff(126) / float(126 * 126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f37pq_f37_producer_quality_compounder_nmstabdil_126d_jerk_v043_signal(netmargin, sharesbas):
    base = np.tanh(_mean(netmargin, 126) / _std(netmargin, 126).replace(0, np.nan)) + 4.0 * _antidilution(sharesbas, 126)
    d = base.diff(21).diff(21) / float(21 * 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f37pq_f37_producer_quality_compounder_nmstabdilx_126d_jerk_v044_signal(netmargin, sharesbas):
    raw = np.tanh(_mean(netmargin, 126) / _std(netmargin, 126).replace(0, np.nan)) + 4.0 * _antidilution(sharesbas, 126)
    base = _mean(raw, 21)
    d = base.diff(42).diff(42) / float(42 * 42)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f37pq_f37_producer_quality_compounder_nmstabdil_252d_jerk_v045_signal(netmargin, sharesbas):
    base = np.tanh(_mean(netmargin, 252) / _std(netmargin, 252).replace(0, np.nan)) + 4.0 * _antidilution(sharesbas, 252)
    d = base.diff(21).diff(21) / float(21 * 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f37pq_f37_producer_quality_compounder_nmstabdilx_252d_jerk_v046_signal(netmargin, sharesbas):
    raw = np.tanh(_mean(netmargin, 252) / _std(netmargin, 252).replace(0, np.nan)) + 4.0 * _antidilution(sharesbas, 252)
    base = _z(raw, 252)
    d = base.diff(63).diff(63) / float(63 * 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f37pq_f37_producer_quality_compounder_nmstabdil_504d_jerk_v047_signal(netmargin, sharesbas):
    base = np.tanh(_mean(netmargin, 504) / _std(netmargin, 504).replace(0, np.nan)) + 4.0 * _antidilution(sharesbas, 504)
    d = base.diff(63).diff(63) / float(63 * 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f37pq_f37_producer_quality_compounder_nmstabdilx_504d_jerk_v048_signal(netmargin, sharesbas):
    raw = np.tanh(_mean(netmargin, 504) / _std(netmargin, 504).replace(0, np.nan)) + 4.0 * _antidilution(sharesbas, 504)
    base = np.tanh(raw)
    d = base.diff(126).diff(126) / float(126 * 126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f37pq_f37_producer_quality_compounder_fcfmindil_126d_jerk_v049_signal(fcf, revenue, sharesbas):
    base = _fcf_margin(fcf, revenue) - _dilution(sharesbas, 126)
    d = base.diff(21).diff(21) / float(21 * 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f37pq_f37_producer_quality_compounder_fcfmindilx_126d_jerk_v050_signal(fcf, revenue, sharesbas):
    raw = _fcf_margin(fcf, revenue) - _dilution(sharesbas, 126)
    base = _mean(raw, 21)
    d = base.diff(42).diff(42) / float(42 * 42)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f37pq_f37_producer_quality_compounder_fcfmindil_252d_jerk_v051_signal(fcf, revenue, sharesbas):
    base = _fcf_margin(fcf, revenue) - _dilution(sharesbas, 252)
    d = base.diff(21).diff(21) / float(21 * 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f37pq_f37_producer_quality_compounder_fcfmindilx_252d_jerk_v052_signal(fcf, revenue, sharesbas):
    raw = _fcf_margin(fcf, revenue) - _dilution(sharesbas, 252)
    base = _z(raw, 252)
    d = base.diff(63).diff(63) / float(63 * 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f37pq_f37_producer_quality_compounder_fcfmindil_504d_jerk_v053_signal(fcf, revenue, sharesbas):
    base = _fcf_margin(fcf, revenue) - _dilution(sharesbas, 504)
    d = base.diff(63).diff(63) / float(63 * 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f37pq_f37_producer_quality_compounder_fcfmindilx_504d_jerk_v054_signal(fcf, revenue, sharesbas):
    raw = _fcf_margin(fcf, revenue) - _dilution(sharesbas, 504)
    base = np.tanh(raw)
    d = base.diff(126).diff(126) / float(126 * 126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f37pq_f37_producer_quality_compounder_zblend_126d_jerk_v055_signal(roic, fcf, revenue, sharesbas):
    base = _z(roic, 126) + _z(_fcf_margin(fcf, revenue), 126) - _z(_dilution(sharesbas, 126), 126)
    d = base.diff(21).diff(21) / float(21 * 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f37pq_f37_producer_quality_compounder_zblendx_126d_jerk_v056_signal(roic, fcf, revenue, sharesbas):
    raw = _z(roic, 126) + _z(_fcf_margin(fcf, revenue), 126) - _z(_dilution(sharesbas, 126), 126)
    base = _mean(raw, 21)
    d = base.diff(42).diff(42) / float(42 * 42)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f37pq_f37_producer_quality_compounder_zblend_252d_jerk_v057_signal(roic, fcf, revenue, sharesbas):
    base = _z(roic, 252) + _z(_fcf_margin(fcf, revenue), 252) - _z(_dilution(sharesbas, 252), 252)
    d = base.diff(21).diff(21) / float(21 * 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f37pq_f37_producer_quality_compounder_zblendx_252d_jerk_v058_signal(roic, fcf, revenue, sharesbas):
    raw = _z(roic, 252) + _z(_fcf_margin(fcf, revenue), 252) - _z(_dilution(sharesbas, 252), 252)
    base = _z(raw, 252)
    d = base.diff(63).diff(63) / float(63 * 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f37pq_f37_producer_quality_compounder_zblend_504d_jerk_v059_signal(roic, fcf, revenue, sharesbas):
    base = _z(roic, 504) + _z(_fcf_margin(fcf, revenue), 504) - _z(_dilution(sharesbas, 504), 504)
    d = base.diff(63).diff(63) / float(63 * 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f37pq_f37_producer_quality_compounder_zblendx_504d_jerk_v060_signal(roic, fcf, revenue, sharesbas):
    raw = _z(roic, 504) + _z(_fcf_margin(fcf, revenue), 504) - _z(_dilution(sharesbas, 504), 504)
    base = np.tanh(raw)
    d = base.diff(126).diff(126) / float(126 * 126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f37pq_f37_producer_quality_compounder_marbreadth_126d_jerk_v061_signal(netmargin, roic):
    base = _pos_frac(netmargin, 126) * _pos_frac(roic, 126)
    d = base.diff(21).diff(21) / float(21 * 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f37pq_f37_producer_quality_compounder_marbreadthx_126d_jerk_v062_signal(netmargin, roic):
    raw = _pos_frac(netmargin, 126) * _pos_frac(roic, 126)
    base = _mean(raw, 21)
    d = base.diff(42).diff(42) / float(42 * 42)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f37pq_f37_producer_quality_compounder_marbreadth_252d_jerk_v063_signal(netmargin, roic):
    base = _pos_frac(netmargin, 252) * _pos_frac(roic, 252)
    d = base.diff(21).diff(21) / float(21 * 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f37pq_f37_producer_quality_compounder_marbreadthx_252d_jerk_v064_signal(netmargin, roic):
    raw = _pos_frac(netmargin, 252) * _pos_frac(roic, 252)
    base = _z(raw, 252)
    d = base.diff(63).diff(63) / float(63 * 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f37pq_f37_producer_quality_compounder_marbreadth_504d_jerk_v065_signal(netmargin, roic):
    base = _pos_frac(netmargin, 504) * _pos_frac(roic, 504)
    d = base.diff(63).diff(63) / float(63 * 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f37pq_f37_producer_quality_compounder_marbreadthx_504d_jerk_v066_signal(netmargin, roic):
    raw = _pos_frac(netmargin, 504) * _pos_frac(roic, 504)
    base = np.tanh(raw)
    d = base.diff(126).diff(126) / float(126 * 126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f37pq_f37_producer_quality_compounder_fcfyld_126d_jerk_v067_signal(fcf, sharesbas):
    base = _z(_fcf_per_share(fcf, sharesbas), 126)
    d = base.diff(21).diff(21) / float(21 * 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f37pq_f37_producer_quality_compounder_fcfyldx_126d_jerk_v068_signal(fcf, sharesbas):
    raw = _z(_fcf_per_share(fcf, sharesbas), 126)
    base = _mean(raw, 21)
    d = base.diff(42).diff(42) / float(42 * 42)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f37pq_f37_producer_quality_compounder_fcfyld_252d_jerk_v069_signal(fcf, sharesbas):
    base = _z(_fcf_per_share(fcf, sharesbas), 252)
    d = base.diff(21).diff(21) / float(21 * 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f37pq_f37_producer_quality_compounder_fcfyldx_252d_jerk_v070_signal(fcf, sharesbas):
    raw = _z(_fcf_per_share(fcf, sharesbas), 252)
    base = _z(raw, 252)
    d = base.diff(63).diff(63) / float(63 * 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f37pq_f37_producer_quality_compounder_fcfyld_504d_jerk_v071_signal(fcf, sharesbas):
    base = _z(_fcf_per_share(fcf, sharesbas), 504)
    d = base.diff(63).diff(63) / float(63 * 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f37pq_f37_producer_quality_compounder_fcfyldx_504d_jerk_v072_signal(fcf, sharesbas):
    raw = _z(_fcf_per_share(fcf, sharesbas), 504)
    base = np.tanh(raw)
    d = base.diff(126).diff(126) / float(126 * 126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f37pq_f37_producer_quality_compounder_cashqual_126d_jerk_v073_signal(netmargin, fcf, revenue):
    base = _mean(np.tanh(4.0 * netmargin) * np.tanh(4.0 * _fcf_margin(fcf, revenue)), 126)
    d = base.diff(21).diff(21) / float(21 * 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f37pq_f37_producer_quality_compounder_cashqualx_126d_jerk_v074_signal(netmargin, fcf, revenue):
    raw = _mean(np.tanh(4.0 * netmargin) * np.tanh(4.0 * _fcf_margin(fcf, revenue)), 126)
    base = _mean(raw, 21)
    d = base.diff(42).diff(42) / float(42 * 42)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f37pq_f37_producer_quality_compounder_cashqual_252d_jerk_v075_signal(netmargin, fcf, revenue):
    base = _mean(np.tanh(4.0 * netmargin) * np.tanh(4.0 * _fcf_margin(fcf, revenue)), 252)
    d = base.diff(21).diff(21) / float(21 * 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f37pq_f37_producer_quality_compounder_cashqualx_252d_jerk_v076_signal(netmargin, fcf, revenue):
    raw = _mean(np.tanh(4.0 * netmargin) * np.tanh(4.0 * _fcf_margin(fcf, revenue)), 252)
    base = _z(raw, 252)
    d = base.diff(63).diff(63) / float(63 * 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f37pq_f37_producer_quality_compounder_cashqual_504d_jerk_v077_signal(netmargin, fcf, revenue):
    base = _mean(np.tanh(4.0 * netmargin) * np.tanh(4.0 * _fcf_margin(fcf, revenue)), 504)
    d = base.diff(63).diff(63) / float(63 * 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f37pq_f37_producer_quality_compounder_cashqualx_504d_jerk_v078_signal(netmargin, fcf, revenue):
    raw = _mean(np.tanh(4.0 * netmargin) * np.tanh(4.0 * _fcf_margin(fcf, revenue)), 504)
    base = np.tanh(raw)
    d = base.diff(126).diff(126) / float(126 * 126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f37pq_f37_producer_quality_compounder_eqnetdil_126d_jerk_v079_signal(equity, sharesbas):
    base = np.tanh(_equity_growth(equity, 126) / (_dilution(sharesbas, 126).abs() + 0.02)) * np.sign(_equity_growth(equity, 126))
    d = base.diff(21).diff(21) / float(21 * 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f37pq_f37_producer_quality_compounder_eqnetdilx_126d_jerk_v080_signal(equity, sharesbas):
    raw = np.tanh(_equity_growth(equity, 126) / (_dilution(sharesbas, 126).abs() + 0.02)) * np.sign(_equity_growth(equity, 126))
    base = _mean(raw, 21)
    d = base.diff(42).diff(42) / float(42 * 42)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f37pq_f37_producer_quality_compounder_eqnetdil_252d_jerk_v081_signal(equity, sharesbas):
    base = np.tanh(_equity_growth(equity, 252) / (_dilution(sharesbas, 252).abs() + 0.02)) * np.sign(_equity_growth(equity, 252))
    d = base.diff(21).diff(21) / float(21 * 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f37pq_f37_producer_quality_compounder_eqnetdilx_252d_jerk_v082_signal(equity, sharesbas):
    raw = np.tanh(_equity_growth(equity, 252) / (_dilution(sharesbas, 252).abs() + 0.02)) * np.sign(_equity_growth(equity, 252))
    base = _z(raw, 252)
    d = base.diff(63).diff(63) / float(63 * 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f37pq_f37_producer_quality_compounder_eqnetdil_504d_jerk_v083_signal(equity, sharesbas):
    base = np.tanh(_equity_growth(equity, 504) / (_dilution(sharesbas, 504).abs() + 0.02)) * np.sign(_equity_growth(equity, 504))
    d = base.diff(63).diff(63) / float(63 * 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f37pq_f37_producer_quality_compounder_eqnetdilx_504d_jerk_v084_signal(equity, sharesbas):
    raw = np.tanh(_equity_growth(equity, 504) / (_dilution(sharesbas, 504).abs() + 0.02)) * np.sign(_equity_growth(equity, 504))
    base = np.tanh(raw)
    d = base.diff(126).diff(126) / float(126 * 126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f37pq_f37_producer_quality_compounder_revps_126d_jerk_v085_signal(revenue, sharesbas):
    base = np.log((revenue / sharesbas.replace(0, np.nan)).replace(0, np.nan) / (revenue / sharesbas.replace(0, np.nan)).shift(126).replace(0, np.nan))
    d = base.diff(21).diff(21) / float(21 * 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f37pq_f37_producer_quality_compounder_revpsx_126d_jerk_v086_signal(revenue, sharesbas):
    raw = np.log((revenue / sharesbas.replace(0, np.nan)).replace(0, np.nan) / (revenue / sharesbas.replace(0, np.nan)).shift(126).replace(0, np.nan))
    base = _mean(raw, 21)
    d = base.diff(42).diff(42) / float(42 * 42)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f37pq_f37_producer_quality_compounder_revps_252d_jerk_v087_signal(revenue, sharesbas):
    base = np.log((revenue / sharesbas.replace(0, np.nan)).replace(0, np.nan) / (revenue / sharesbas.replace(0, np.nan)).shift(252).replace(0, np.nan))
    d = base.diff(21).diff(21) / float(21 * 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f37pq_f37_producer_quality_compounder_revpsx_252d_jerk_v088_signal(revenue, sharesbas):
    raw = np.log((revenue / sharesbas.replace(0, np.nan)).replace(0, np.nan) / (revenue / sharesbas.replace(0, np.nan)).shift(252).replace(0, np.nan))
    base = _z(raw, 252)
    d = base.diff(63).diff(63) / float(63 * 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f37pq_f37_producer_quality_compounder_revps_504d_jerk_v089_signal(revenue, sharesbas):
    base = np.log((revenue / sharesbas.replace(0, np.nan)).replace(0, np.nan) / (revenue / sharesbas.replace(0, np.nan)).shift(504).replace(0, np.nan))
    d = base.diff(63).diff(63) / float(63 * 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f37pq_f37_producer_quality_compounder_revpsx_504d_jerk_v090_signal(revenue, sharesbas):
    raw = np.log((revenue / sharesbas.replace(0, np.nan)).replace(0, np.nan) / (revenue / sharesbas.replace(0, np.nan)).shift(504).replace(0, np.nan))
    base = np.tanh(raw)
    d = base.diff(126).diff(126) / float(126 * 126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f37pq_f37_producer_quality_compounder_qlevel_126d_jerk_v091_signal(roic, fcf, revenue, netmargin):
    base = _mean(np.tanh(3.0 * roic) + np.tanh(3.0 * _fcf_margin(fcf, revenue)) + np.tanh(4.0 * netmargin), 126)
    d = base.diff(21).diff(21) / float(21 * 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f37pq_f37_producer_quality_compounder_qlevelx_126d_jerk_v092_signal(roic, fcf, revenue, netmargin):
    raw = _mean(np.tanh(3.0 * roic) + np.tanh(3.0 * _fcf_margin(fcf, revenue)) + np.tanh(4.0 * netmargin), 126)
    base = _mean(raw, 21)
    d = base.diff(42).diff(42) / float(42 * 42)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f37pq_f37_producer_quality_compounder_qlevel_252d_jerk_v093_signal(roic, fcf, revenue, netmargin):
    base = _mean(np.tanh(3.0 * roic) + np.tanh(3.0 * _fcf_margin(fcf, revenue)) + np.tanh(4.0 * netmargin), 252)
    d = base.diff(21).diff(21) / float(21 * 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f37pq_f37_producer_quality_compounder_qlevelx_252d_jerk_v094_signal(roic, fcf, revenue, netmargin):
    raw = _mean(np.tanh(3.0 * roic) + np.tanh(3.0 * _fcf_margin(fcf, revenue)) + np.tanh(4.0 * netmargin), 252)
    base = _z(raw, 252)
    d = base.diff(63).diff(63) / float(63 * 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f37pq_f37_producer_quality_compounder_qlevel_504d_jerk_v095_signal(roic, fcf, revenue, netmargin):
    base = _mean(np.tanh(3.0 * roic) + np.tanh(3.0 * _fcf_margin(fcf, revenue)) + np.tanh(4.0 * netmargin), 504)
    d = base.diff(63).diff(63) / float(63 * 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f37pq_f37_producer_quality_compounder_qlevelx_504d_jerk_v096_signal(roic, fcf, revenue, netmargin):
    raw = _mean(np.tanh(3.0 * roic) + np.tanh(3.0 * _fcf_margin(fcf, revenue)) + np.tanh(4.0 * netmargin), 504)
    base = np.tanh(raw)
    d = base.diff(126).diff(126) / float(126 * 126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f37pq_f37_producer_quality_compounder_croe_126d_jerk_v097_signal(fcf, equity):
    base = _mean(fcf / equity.replace(0, np.nan), 126) / (1.0 + _std(fcf / equity.replace(0, np.nan), 126))
    d = base.diff(21).diff(21) / float(21 * 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f37pq_f37_producer_quality_compounder_croex_126d_jerk_v098_signal(fcf, equity):
    raw = _mean(fcf / equity.replace(0, np.nan), 126) / (1.0 + _std(fcf / equity.replace(0, np.nan), 126))
    base = _mean(raw, 21)
    d = base.diff(42).diff(42) / float(42 * 42)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f37pq_f37_producer_quality_compounder_croe_252d_jerk_v099_signal(fcf, equity):
    base = _mean(fcf / equity.replace(0, np.nan), 252) / (1.0 + _std(fcf / equity.replace(0, np.nan), 252))
    d = base.diff(21).diff(21) / float(21 * 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f37pq_f37_producer_quality_compounder_croex_252d_jerk_v100_signal(fcf, equity):
    raw = _mean(fcf / equity.replace(0, np.nan), 252) / (1.0 + _std(fcf / equity.replace(0, np.nan), 252))
    base = _z(raw, 252)
    d = base.diff(63).diff(63) / float(63 * 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f37pq_f37_producer_quality_compounder_croe_504d_jerk_v101_signal(fcf, equity):
    base = _mean(fcf / equity.replace(0, np.nan), 504) / (1.0 + _std(fcf / equity.replace(0, np.nan), 504))
    d = base.diff(63).diff(63) / float(63 * 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f37pq_f37_producer_quality_compounder_croex_504d_jerk_v102_signal(fcf, equity):
    raw = _mean(fcf / equity.replace(0, np.nan), 504) / (1.0 + _std(fcf / equity.replace(0, np.nan), 504))
    base = np.tanh(raw)
    d = base.diff(126).diff(126) / float(126 * 126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f37pq_f37_producer_quality_compounder_nmgrow_126d_jerk_v103_signal(netmargin, revenue):
    base = np.tanh(4.0 * netmargin) * _rev_growth(revenue, 126)
    d = base.diff(21).diff(21) / float(21 * 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f37pq_f37_producer_quality_compounder_nmgrowx_126d_jerk_v104_signal(netmargin, revenue):
    raw = np.tanh(4.0 * netmargin) * _rev_growth(revenue, 126)
    base = _mean(raw, 21)
    d = base.diff(42).diff(42) / float(42 * 42)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f37pq_f37_producer_quality_compounder_nmgrow_252d_jerk_v105_signal(netmargin, revenue):
    base = np.tanh(4.0 * netmargin) * _rev_growth(revenue, 252)
    d = base.diff(21).diff(21) / float(21 * 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f37pq_f37_producer_quality_compounder_nmgrowx_252d_jerk_v106_signal(netmargin, revenue):
    raw = np.tanh(4.0 * netmargin) * _rev_growth(revenue, 252)
    base = _z(raw, 252)
    d = base.diff(63).diff(63) / float(63 * 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f37pq_f37_producer_quality_compounder_nmgrow_504d_jerk_v107_signal(netmargin, revenue):
    base = np.tanh(4.0 * netmargin) * _rev_growth(revenue, 504)
    d = base.diff(63).diff(63) / float(63 * 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f37pq_f37_producer_quality_compounder_nmgrowx_504d_jerk_v108_signal(netmargin, revenue):
    raw = np.tanh(4.0 * netmargin) * _rev_growth(revenue, 504)
    base = np.tanh(raw)
    d = base.diff(126).diff(126) / float(126 * 126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f37pq_f37_producer_quality_compounder_capeff_126d_jerk_v109_signal(roic, equity):
    base = np.tanh(3.0 * _mean(roic, 63)) * _equity_growth(equity, 126)
    d = base.diff(21).diff(21) / float(21 * 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f37pq_f37_producer_quality_compounder_capeffx_126d_jerk_v110_signal(roic, equity):
    raw = np.tanh(3.0 * _mean(roic, 63)) * _equity_growth(equity, 126)
    base = _mean(raw, 21)
    d = base.diff(42).diff(42) / float(42 * 42)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f37pq_f37_producer_quality_compounder_capeff_252d_jerk_v111_signal(roic, equity):
    base = np.tanh(3.0 * _mean(roic, 63)) * _equity_growth(equity, 252)
    d = base.diff(21).diff(21) / float(21 * 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f37pq_f37_producer_quality_compounder_capeffx_252d_jerk_v112_signal(roic, equity):
    raw = np.tanh(3.0 * _mean(roic, 63)) * _equity_growth(equity, 252)
    base = _z(raw, 252)
    d = base.diff(63).diff(63) / float(63 * 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f37pq_f37_producer_quality_compounder_capeff_504d_jerk_v113_signal(roic, equity):
    base = np.tanh(3.0 * _mean(roic, 63)) * _equity_growth(equity, 504)
    d = base.diff(63).diff(63) / float(63 * 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f37pq_f37_producer_quality_compounder_capeffx_504d_jerk_v114_signal(roic, equity):
    raw = np.tanh(3.0 * _mean(roic, 63)) * _equity_growth(equity, 504)
    base = np.tanh(raw)
    d = base.diff(126).diff(126) / float(126 * 126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f37pq_f37_producer_quality_compounder_stableroic_126d_jerk_v115_signal(roic):
    base = _pos_frac(roic, 126) * (1.0 - np.tanh(_std(roic, 126) / _mean(roic.abs(), 126).replace(0, np.nan)))
    d = base.diff(21).diff(21) / float(21 * 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f37pq_f37_producer_quality_compounder_stableroicx_126d_jerk_v116_signal(roic):
    raw = _pos_frac(roic, 126) * (1.0 - np.tanh(_std(roic, 126) / _mean(roic.abs(), 126).replace(0, np.nan)))
    base = _mean(raw, 21)
    d = base.diff(42).diff(42) / float(42 * 42)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f37pq_f37_producer_quality_compounder_stableroic_252d_jerk_v117_signal(roic):
    base = _pos_frac(roic, 252) * (1.0 - np.tanh(_std(roic, 252) / _mean(roic.abs(), 252).replace(0, np.nan)))
    d = base.diff(21).diff(21) / float(21 * 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f37pq_f37_producer_quality_compounder_stableroicx_252d_jerk_v118_signal(roic):
    raw = _pos_frac(roic, 252) * (1.0 - np.tanh(_std(roic, 252) / _mean(roic.abs(), 252).replace(0, np.nan)))
    base = _z(raw, 252)
    d = base.diff(63).diff(63) / float(63 * 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f37pq_f37_producer_quality_compounder_stableroic_504d_jerk_v119_signal(roic):
    base = _pos_frac(roic, 504) * (1.0 - np.tanh(_std(roic, 504) / _mean(roic.abs(), 504).replace(0, np.nan)))
    d = base.diff(63).diff(63) / float(63 * 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f37pq_f37_producer_quality_compounder_stableroicx_504d_jerk_v120_signal(roic):
    raw = _pos_frac(roic, 504) * (1.0 - np.tanh(_std(roic, 504) / _mean(roic.abs(), 504).replace(0, np.nan)))
    base = np.tanh(raw)
    d = base.diff(126).diff(126) / float(126 * 126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f37pq_f37_producer_quality_compounder_antiroic_126d_jerk_v121_signal(roic, sharesbas):
    base = np.tanh(3.0 * _mean(roic, 63)) * (1.0 + np.tanh(8.0 * _antidilution(sharesbas, 126)))
    d = base.diff(21).diff(21) / float(21 * 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f37pq_f37_producer_quality_compounder_antiroicx_126d_jerk_v122_signal(roic, sharesbas):
    raw = np.tanh(3.0 * _mean(roic, 63)) * (1.0 + np.tanh(8.0 * _antidilution(sharesbas, 126)))
    base = _mean(raw, 21)
    d = base.diff(42).diff(42) / float(42 * 42)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f37pq_f37_producer_quality_compounder_antiroic_252d_jerk_v123_signal(roic, sharesbas):
    base = np.tanh(3.0 * _mean(roic, 63)) * (1.0 + np.tanh(8.0 * _antidilution(sharesbas, 252)))
    d = base.diff(21).diff(21) / float(21 * 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f37pq_f37_producer_quality_compounder_antiroicx_252d_jerk_v124_signal(roic, sharesbas):
    raw = np.tanh(3.0 * _mean(roic, 63)) * (1.0 + np.tanh(8.0 * _antidilution(sharesbas, 252)))
    base = _z(raw, 252)
    d = base.diff(63).diff(63) / float(63 * 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f37pq_f37_producer_quality_compounder_antiroic_504d_jerk_v125_signal(roic, sharesbas):
    base = np.tanh(3.0 * _mean(roic, 63)) * (1.0 + np.tanh(8.0 * _antidilution(sharesbas, 504)))
    d = base.diff(63).diff(63) / float(63 * 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f37pq_f37_producer_quality_compounder_antiroicx_504d_jerk_v126_signal(roic, sharesbas):
    raw = np.tanh(3.0 * _mean(roic, 63)) * (1.0 + np.tanh(8.0 * _antidilution(sharesbas, 504)))
    base = np.tanh(raw)
    d = base.diff(126).diff(126) / float(126 * 126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f37pq_f37_producer_quality_compounder_eps_126d_jerk_v127_signal(netmargin, revenue, sharesbas):
    base = _z(netmargin * revenue / sharesbas.replace(0, np.nan), 126)
    d = base.diff(21).diff(21) / float(21 * 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f37pq_f37_producer_quality_compounder_epsx_126d_jerk_v128_signal(netmargin, revenue, sharesbas):
    raw = _z(netmargin * revenue / sharesbas.replace(0, np.nan), 126)
    base = _mean(raw, 21)
    d = base.diff(42).diff(42) / float(42 * 42)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f37pq_f37_producer_quality_compounder_eps_252d_jerk_v129_signal(netmargin, revenue, sharesbas):
    base = _z(netmargin * revenue / sharesbas.replace(0, np.nan), 252)
    d = base.diff(21).diff(21) / float(21 * 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f37pq_f37_producer_quality_compounder_epsx_252d_jerk_v130_signal(netmargin, revenue, sharesbas):
    raw = _z(netmargin * revenue / sharesbas.replace(0, np.nan), 252)
    base = _z(raw, 252)
    d = base.diff(63).diff(63) / float(63 * 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f37pq_f37_producer_quality_compounder_eps_504d_jerk_v131_signal(netmargin, revenue, sharesbas):
    base = _z(netmargin * revenue / sharesbas.replace(0, np.nan), 504)
    d = base.diff(63).diff(63) / float(63 * 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f37pq_f37_producer_quality_compounder_epsx_504d_jerk_v132_signal(netmargin, revenue, sharesbas):
    raw = _z(netmargin * revenue / sharesbas.replace(0, np.nan), 504)
    base = np.tanh(raw)
    d = base.diff(126).diff(126) / float(126 * 126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f37pq_f37_producer_quality_compounder_caplight_126d_jerk_v133_signal(roic, revenue, equity):
    base = np.tanh(3.0 * _mean(roic, 126)) * np.tanh(_mean(revenue / equity.replace(0, np.nan), 126))
    d = base.diff(21).diff(21) / float(21 * 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f37pq_f37_producer_quality_compounder_caplightx_126d_jerk_v134_signal(roic, revenue, equity):
    raw = np.tanh(3.0 * _mean(roic, 126)) * np.tanh(_mean(revenue / equity.replace(0, np.nan), 126))
    base = _mean(raw, 21)
    d = base.diff(42).diff(42) / float(42 * 42)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f37pq_f37_producer_quality_compounder_caplight_252d_jerk_v135_signal(roic, revenue, equity):
    base = np.tanh(3.0 * _mean(roic, 252)) * np.tanh(_mean(revenue / equity.replace(0, np.nan), 252))
    d = base.diff(21).diff(21) / float(21 * 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f37pq_f37_producer_quality_compounder_caplightx_252d_jerk_v136_signal(roic, revenue, equity):
    raw = np.tanh(3.0 * _mean(roic, 252)) * np.tanh(_mean(revenue / equity.replace(0, np.nan), 252))
    base = _z(raw, 252)
    d = base.diff(63).diff(63) / float(63 * 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f37pq_f37_producer_quality_compounder_caplight_504d_jerk_v137_signal(roic, revenue, equity):
    base = np.tanh(3.0 * _mean(roic, 504)) * np.tanh(_mean(revenue / equity.replace(0, np.nan), 504))
    d = base.diff(63).diff(63) / float(63 * 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f37pq_f37_producer_quality_compounder_caplightx_504d_jerk_v138_signal(roic, revenue, equity):
    raw = np.tanh(3.0 * _mean(roic, 504)) * np.tanh(_mean(revenue / equity.replace(0, np.nan), 504))
    base = np.tanh(raw)
    d = base.diff(126).diff(126) / float(126 * 126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f37pq_f37_producer_quality_compounder_susgrow_126d_jerk_v139_signal(roic, revenue):
    base = np.tanh(3.0 * _mean(roic, 63)) - _rev_growth(revenue, 126)
    d = base.diff(21).diff(21) / float(21 * 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f37pq_f37_producer_quality_compounder_susgrowx_126d_jerk_v140_signal(roic, revenue):
    raw = np.tanh(3.0 * _mean(roic, 63)) - _rev_growth(revenue, 126)
    base = _mean(raw, 21)
    d = base.diff(42).diff(42) / float(42 * 42)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f37pq_f37_producer_quality_compounder_susgrow_252d_jerk_v141_signal(roic, revenue):
    base = np.tanh(3.0 * _mean(roic, 63)) - _rev_growth(revenue, 252)
    d = base.diff(21).diff(21) / float(21 * 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f37pq_f37_producer_quality_compounder_susgrowx_252d_jerk_v142_signal(roic, revenue):
    raw = np.tanh(3.0 * _mean(roic, 63)) - _rev_growth(revenue, 252)
    base = _z(raw, 252)
    d = base.diff(63).diff(63) / float(63 * 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f37pq_f37_producer_quality_compounder_susgrow_504d_jerk_v143_signal(roic, revenue):
    base = np.tanh(3.0 * _mean(roic, 63)) - _rev_growth(revenue, 504)
    d = base.diff(63).diff(63) / float(63 * 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f37pq_f37_producer_quality_compounder_susgrowx_504d_jerk_v144_signal(roic, revenue):
    raw = np.tanh(3.0 * _mean(roic, 63)) - _rev_growth(revenue, 504)
    base = np.tanh(raw)
    d = base.diff(126).diff(126) / float(126 * 126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f37pq_f37_producer_quality_compounder_marqual_126d_jerk_v145_signal(netmargin, fcf):
    base = (_mean(netmargin, 126) - _std(netmargin, 126)) * _pos_frac(fcf, 126)
    d = base.diff(21).diff(21) / float(21 * 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f37pq_f37_producer_quality_compounder_marqualx_126d_jerk_v146_signal(netmargin, fcf):
    raw = (_mean(netmargin, 126) - _std(netmargin, 126)) * _pos_frac(fcf, 126)
    base = _mean(raw, 21)
    d = base.diff(42).diff(42) / float(42 * 42)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f37pq_f37_producer_quality_compounder_marqual_252d_jerk_v147_signal(netmargin, fcf):
    base = (_mean(netmargin, 252) - _std(netmargin, 252)) * _pos_frac(fcf, 252)
    d = base.diff(21).diff(21) / float(21 * 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f37pq_f37_producer_quality_compounder_marqualx_252d_jerk_v148_signal(netmargin, fcf):
    raw = (_mean(netmargin, 252) - _std(netmargin, 252)) * _pos_frac(fcf, 252)
    base = _z(raw, 252)
    d = base.diff(63).diff(63) / float(63 * 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f37pq_f37_producer_quality_compounder_marqual_504d_jerk_v149_signal(netmargin, fcf):
    base = (_mean(netmargin, 504) - _std(netmargin, 504)) * _pos_frac(fcf, 504)
    d = base.diff(63).diff(63) / float(63 * 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f37pq_f37_producer_quality_compounder_marqualx_504d_jerk_v150_signal(netmargin, fcf):
    raw = (_mean(netmargin, 504) - _std(netmargin, 504)) * _pos_frac(fcf, 504)
    base = np.tanh(raw)
    d = base.diff(126).diff(126) / float(126 * 126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f37pq_f37_producer_quality_compounder_qmd_126d_jerk_v001_signal,
    f37pq_f37_producer_quality_compounder_qmdx_126d_jerk_v002_signal,
    f37pq_f37_producer_quality_compounder_qmd_252d_jerk_v003_signal,
    f37pq_f37_producer_quality_compounder_qmdx_252d_jerk_v004_signal,
    f37pq_f37_producer_quality_compounder_qmd_504d_jerk_v005_signal,
    f37pq_f37_producer_quality_compounder_qmdx_504d_jerk_v006_signal,
    f37pq_f37_producer_quality_compounder_fcfdil_126d_jerk_v007_signal,
    f37pq_f37_producer_quality_compounder_fcfdilx_126d_jerk_v008_signal,
    f37pq_f37_producer_quality_compounder_fcfdil_252d_jerk_v009_signal,
    f37pq_f37_producer_quality_compounder_fcfdilx_252d_jerk_v010_signal,
    f37pq_f37_producer_quality_compounder_fcfdil_504d_jerk_v011_signal,
    f37pq_f37_producer_quality_compounder_fcfdilx_504d_jerk_v012_signal,
    f37pq_f37_producer_quality_compounder_durable_126d_jerk_v013_signal,
    f37pq_f37_producer_quality_compounder_durablex_126d_jerk_v014_signal,
    f37pq_f37_producer_quality_compounder_durable_252d_jerk_v015_signal,
    f37pq_f37_producer_quality_compounder_durablex_252d_jerk_v016_signal,
    f37pq_f37_producer_quality_compounder_durable_504d_jerk_v017_signal,
    f37pq_f37_producer_quality_compounder_durablex_504d_jerk_v018_signal,
    f37pq_f37_producer_quality_compounder_qual_126d_jerk_v019_signal,
    f37pq_f37_producer_quality_compounder_qualx_126d_jerk_v020_signal,
    f37pq_f37_producer_quality_compounder_qual_252d_jerk_v021_signal,
    f37pq_f37_producer_quality_compounder_qualx_252d_jerk_v022_signal,
    f37pq_f37_producer_quality_compounder_qual_504d_jerk_v023_signal,
    f37pq_f37_producer_quality_compounder_qualx_504d_jerk_v024_signal,
    f37pq_f37_producer_quality_compounder_bvpsg_126d_jerk_v025_signal,
    f37pq_f37_producer_quality_compounder_bvpsgx_126d_jerk_v026_signal,
    f37pq_f37_producer_quality_compounder_bvpsg_252d_jerk_v027_signal,
    f37pq_f37_producer_quality_compounder_bvpsgx_252d_jerk_v028_signal,
    f37pq_f37_producer_quality_compounder_bvpsg_504d_jerk_v029_signal,
    f37pq_f37_producer_quality_compounder_bvpsgx_504d_jerk_v030_signal,
    f37pq_f37_producer_quality_compounder_roicz_126d_jerk_v031_signal,
    f37pq_f37_producer_quality_compounder_roiczx_126d_jerk_v032_signal,
    f37pq_f37_producer_quality_compounder_roicz_252d_jerk_v033_signal,
    f37pq_f37_producer_quality_compounder_roiczx_252d_jerk_v034_signal,
    f37pq_f37_producer_quality_compounder_roicz_504d_jerk_v035_signal,
    f37pq_f37_producer_quality_compounder_roiczx_504d_jerk_v036_signal,
    f37pq_f37_producer_quality_compounder_profgrow_126d_jerk_v037_signal,
    f37pq_f37_producer_quality_compounder_profgrowx_126d_jerk_v038_signal,
    f37pq_f37_producer_quality_compounder_profgrow_252d_jerk_v039_signal,
    f37pq_f37_producer_quality_compounder_profgrowx_252d_jerk_v040_signal,
    f37pq_f37_producer_quality_compounder_profgrow_504d_jerk_v041_signal,
    f37pq_f37_producer_quality_compounder_profgrowx_504d_jerk_v042_signal,
    f37pq_f37_producer_quality_compounder_nmstabdil_126d_jerk_v043_signal,
    f37pq_f37_producer_quality_compounder_nmstabdilx_126d_jerk_v044_signal,
    f37pq_f37_producer_quality_compounder_nmstabdil_252d_jerk_v045_signal,
    f37pq_f37_producer_quality_compounder_nmstabdilx_252d_jerk_v046_signal,
    f37pq_f37_producer_quality_compounder_nmstabdil_504d_jerk_v047_signal,
    f37pq_f37_producer_quality_compounder_nmstabdilx_504d_jerk_v048_signal,
    f37pq_f37_producer_quality_compounder_fcfmindil_126d_jerk_v049_signal,
    f37pq_f37_producer_quality_compounder_fcfmindilx_126d_jerk_v050_signal,
    f37pq_f37_producer_quality_compounder_fcfmindil_252d_jerk_v051_signal,
    f37pq_f37_producer_quality_compounder_fcfmindilx_252d_jerk_v052_signal,
    f37pq_f37_producer_quality_compounder_fcfmindil_504d_jerk_v053_signal,
    f37pq_f37_producer_quality_compounder_fcfmindilx_504d_jerk_v054_signal,
    f37pq_f37_producer_quality_compounder_zblend_126d_jerk_v055_signal,
    f37pq_f37_producer_quality_compounder_zblendx_126d_jerk_v056_signal,
    f37pq_f37_producer_quality_compounder_zblend_252d_jerk_v057_signal,
    f37pq_f37_producer_quality_compounder_zblendx_252d_jerk_v058_signal,
    f37pq_f37_producer_quality_compounder_zblend_504d_jerk_v059_signal,
    f37pq_f37_producer_quality_compounder_zblendx_504d_jerk_v060_signal,
    f37pq_f37_producer_quality_compounder_marbreadth_126d_jerk_v061_signal,
    f37pq_f37_producer_quality_compounder_marbreadthx_126d_jerk_v062_signal,
    f37pq_f37_producer_quality_compounder_marbreadth_252d_jerk_v063_signal,
    f37pq_f37_producer_quality_compounder_marbreadthx_252d_jerk_v064_signal,
    f37pq_f37_producer_quality_compounder_marbreadth_504d_jerk_v065_signal,
    f37pq_f37_producer_quality_compounder_marbreadthx_504d_jerk_v066_signal,
    f37pq_f37_producer_quality_compounder_fcfyld_126d_jerk_v067_signal,
    f37pq_f37_producer_quality_compounder_fcfyldx_126d_jerk_v068_signal,
    f37pq_f37_producer_quality_compounder_fcfyld_252d_jerk_v069_signal,
    f37pq_f37_producer_quality_compounder_fcfyldx_252d_jerk_v070_signal,
    f37pq_f37_producer_quality_compounder_fcfyld_504d_jerk_v071_signal,
    f37pq_f37_producer_quality_compounder_fcfyldx_504d_jerk_v072_signal,
    f37pq_f37_producer_quality_compounder_cashqual_126d_jerk_v073_signal,
    f37pq_f37_producer_quality_compounder_cashqualx_126d_jerk_v074_signal,
    f37pq_f37_producer_quality_compounder_cashqual_252d_jerk_v075_signal,
    f37pq_f37_producer_quality_compounder_cashqualx_252d_jerk_v076_signal,
    f37pq_f37_producer_quality_compounder_cashqual_504d_jerk_v077_signal,
    f37pq_f37_producer_quality_compounder_cashqualx_504d_jerk_v078_signal,
    f37pq_f37_producer_quality_compounder_eqnetdil_126d_jerk_v079_signal,
    f37pq_f37_producer_quality_compounder_eqnetdilx_126d_jerk_v080_signal,
    f37pq_f37_producer_quality_compounder_eqnetdil_252d_jerk_v081_signal,
    f37pq_f37_producer_quality_compounder_eqnetdilx_252d_jerk_v082_signal,
    f37pq_f37_producer_quality_compounder_eqnetdil_504d_jerk_v083_signal,
    f37pq_f37_producer_quality_compounder_eqnetdilx_504d_jerk_v084_signal,
    f37pq_f37_producer_quality_compounder_revps_126d_jerk_v085_signal,
    f37pq_f37_producer_quality_compounder_revpsx_126d_jerk_v086_signal,
    f37pq_f37_producer_quality_compounder_revps_252d_jerk_v087_signal,
    f37pq_f37_producer_quality_compounder_revpsx_252d_jerk_v088_signal,
    f37pq_f37_producer_quality_compounder_revps_504d_jerk_v089_signal,
    f37pq_f37_producer_quality_compounder_revpsx_504d_jerk_v090_signal,
    f37pq_f37_producer_quality_compounder_qlevel_126d_jerk_v091_signal,
    f37pq_f37_producer_quality_compounder_qlevelx_126d_jerk_v092_signal,
    f37pq_f37_producer_quality_compounder_qlevel_252d_jerk_v093_signal,
    f37pq_f37_producer_quality_compounder_qlevelx_252d_jerk_v094_signal,
    f37pq_f37_producer_quality_compounder_qlevel_504d_jerk_v095_signal,
    f37pq_f37_producer_quality_compounder_qlevelx_504d_jerk_v096_signal,
    f37pq_f37_producer_quality_compounder_croe_126d_jerk_v097_signal,
    f37pq_f37_producer_quality_compounder_croex_126d_jerk_v098_signal,
    f37pq_f37_producer_quality_compounder_croe_252d_jerk_v099_signal,
    f37pq_f37_producer_quality_compounder_croex_252d_jerk_v100_signal,
    f37pq_f37_producer_quality_compounder_croe_504d_jerk_v101_signal,
    f37pq_f37_producer_quality_compounder_croex_504d_jerk_v102_signal,
    f37pq_f37_producer_quality_compounder_nmgrow_126d_jerk_v103_signal,
    f37pq_f37_producer_quality_compounder_nmgrowx_126d_jerk_v104_signal,
    f37pq_f37_producer_quality_compounder_nmgrow_252d_jerk_v105_signal,
    f37pq_f37_producer_quality_compounder_nmgrowx_252d_jerk_v106_signal,
    f37pq_f37_producer_quality_compounder_nmgrow_504d_jerk_v107_signal,
    f37pq_f37_producer_quality_compounder_nmgrowx_504d_jerk_v108_signal,
    f37pq_f37_producer_quality_compounder_capeff_126d_jerk_v109_signal,
    f37pq_f37_producer_quality_compounder_capeffx_126d_jerk_v110_signal,
    f37pq_f37_producer_quality_compounder_capeff_252d_jerk_v111_signal,
    f37pq_f37_producer_quality_compounder_capeffx_252d_jerk_v112_signal,
    f37pq_f37_producer_quality_compounder_capeff_504d_jerk_v113_signal,
    f37pq_f37_producer_quality_compounder_capeffx_504d_jerk_v114_signal,
    f37pq_f37_producer_quality_compounder_stableroic_126d_jerk_v115_signal,
    f37pq_f37_producer_quality_compounder_stableroicx_126d_jerk_v116_signal,
    f37pq_f37_producer_quality_compounder_stableroic_252d_jerk_v117_signal,
    f37pq_f37_producer_quality_compounder_stableroicx_252d_jerk_v118_signal,
    f37pq_f37_producer_quality_compounder_stableroic_504d_jerk_v119_signal,
    f37pq_f37_producer_quality_compounder_stableroicx_504d_jerk_v120_signal,
    f37pq_f37_producer_quality_compounder_antiroic_126d_jerk_v121_signal,
    f37pq_f37_producer_quality_compounder_antiroicx_126d_jerk_v122_signal,
    f37pq_f37_producer_quality_compounder_antiroic_252d_jerk_v123_signal,
    f37pq_f37_producer_quality_compounder_antiroicx_252d_jerk_v124_signal,
    f37pq_f37_producer_quality_compounder_antiroic_504d_jerk_v125_signal,
    f37pq_f37_producer_quality_compounder_antiroicx_504d_jerk_v126_signal,
    f37pq_f37_producer_quality_compounder_eps_126d_jerk_v127_signal,
    f37pq_f37_producer_quality_compounder_epsx_126d_jerk_v128_signal,
    f37pq_f37_producer_quality_compounder_eps_252d_jerk_v129_signal,
    f37pq_f37_producer_quality_compounder_epsx_252d_jerk_v130_signal,
    f37pq_f37_producer_quality_compounder_eps_504d_jerk_v131_signal,
    f37pq_f37_producer_quality_compounder_epsx_504d_jerk_v132_signal,
    f37pq_f37_producer_quality_compounder_caplight_126d_jerk_v133_signal,
    f37pq_f37_producer_quality_compounder_caplightx_126d_jerk_v134_signal,
    f37pq_f37_producer_quality_compounder_caplight_252d_jerk_v135_signal,
    f37pq_f37_producer_quality_compounder_caplightx_252d_jerk_v136_signal,
    f37pq_f37_producer_quality_compounder_caplight_504d_jerk_v137_signal,
    f37pq_f37_producer_quality_compounder_caplightx_504d_jerk_v138_signal,
    f37pq_f37_producer_quality_compounder_susgrow_126d_jerk_v139_signal,
    f37pq_f37_producer_quality_compounder_susgrowx_126d_jerk_v140_signal,
    f37pq_f37_producer_quality_compounder_susgrow_252d_jerk_v141_signal,
    f37pq_f37_producer_quality_compounder_susgrowx_252d_jerk_v142_signal,
    f37pq_f37_producer_quality_compounder_susgrow_504d_jerk_v143_signal,
    f37pq_f37_producer_quality_compounder_susgrowx_504d_jerk_v144_signal,
    f37pq_f37_producer_quality_compounder_marqual_126d_jerk_v145_signal,
    f37pq_f37_producer_quality_compounder_marqualx_126d_jerk_v146_signal,
    f37pq_f37_producer_quality_compounder_marqual_252d_jerk_v147_signal,
    f37pq_f37_producer_quality_compounder_marqualx_252d_jerk_v148_signal,
    f37pq_f37_producer_quality_compounder_marqual_504d_jerk_v149_signal,
    f37pq_f37_producer_quality_compounder_marqualx_504d_jerk_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F37_PRODUCER_QUALITY_COMPOUNDER_REGISTRY_001_150 = REGISTRY


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

    roic = _fund(3, base=0.12, drift=-0.01, vol=0.55, allow_neg=True).rename("roic")
    fcf = _fund(5, base=5e7, drift=-0.01, vol=0.55, allow_neg=True).rename("fcf")
    sharesbas = _fund(103, base=2e8, drift=0.03, vol=0.04).rename("sharesbas")
    netmargin = _fund(14, base=0.10, drift=-0.01, vol=0.55, allow_neg=True).rename("netmargin")
    revenue = _fund(105, base=3e8, drift=0.02, vol=0.10).rename("revenue")
    equity = _fund(106, base=4e8, drift=0.02, vol=0.08).rename("equity")

    cols = {"roic": roic, "fcf": fcf, "sharesbas": sharesbas,
            "netmargin": netmargin, "revenue": revenue, "equity": equity}

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

    print("OK f37_producer_quality_compounder_3rd_derivatives_001_150_claude: %d features pass" % n_features)
