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


def _slope_pct(s, w):
    return s.pct_change(periods=w)


def _slope_diff_norm(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)


def _accel(s, w):
    return s.diff(periods=w).diff(periods=w)


# ===== folder domain primitives =====
def _f086_priceyoy(close):
    return close.pct_change(periods=252)


# 21d slope of price_yoy
def f086dmt_f086_daily_market_metrics_price_yoy_slope_21d_2d_v001_signal(close, closeadj):
    base = _f086_priceyoy(close)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of price_yoy
def f086dmt_f086_daily_market_metrics_price_yoy_slope_63d_2d_v002_signal(close, closeadj):
    base = _f086_priceyoy(close)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of price_yoy
def f086dmt_f086_daily_market_metrics_price_yoy_slope_126d_2d_v003_signal(close, closeadj):
    base = _f086_priceyoy(close)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of price_yoy
def f086dmt_f086_daily_market_metrics_price_yoy_slope_252d_2d_v004_signal(close, closeadj):
    base = _f086_priceyoy(close)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of price_yoy
def f086dmt_f086_daily_market_metrics_price_yoy_slope_504d_2d_v005_signal(close, closeadj):
    base = _f086_priceyoy(close)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of ev_yoy
def f086dmt_f086_daily_market_metrics_ev_yoy_slope_21d_2d_v006_signal(ev, closeadj):
    base = ev.pct_change(periods=252)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of ev_yoy
def f086dmt_f086_daily_market_metrics_ev_yoy_slope_63d_2d_v007_signal(ev, closeadj):
    base = ev.pct_change(periods=252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of ev_yoy
def f086dmt_f086_daily_market_metrics_ev_yoy_slope_126d_2d_v008_signal(ev, closeadj):
    base = ev.pct_change(periods=252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of ev_yoy
def f086dmt_f086_daily_market_metrics_ev_yoy_slope_252d_2d_v009_signal(ev, closeadj):
    base = ev.pct_change(periods=252)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of ev_yoy
def f086dmt_f086_daily_market_metrics_ev_yoy_slope_504d_2d_v010_signal(ev, closeadj):
    base = ev.pct_change(periods=252)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of pb_yoy_chg
def f086dmt_f086_daily_market_metrics_pb_yoy_chg_slope_21d_2d_v011_signal(pb, closeadj):
    base = pb.diff(periods=252)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of pb_yoy_chg
def f086dmt_f086_daily_market_metrics_pb_yoy_chg_slope_63d_2d_v012_signal(pb, closeadj):
    base = pb.diff(periods=252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of pb_yoy_chg
def f086dmt_f086_daily_market_metrics_pb_yoy_chg_slope_126d_2d_v013_signal(pb, closeadj):
    base = pb.diff(periods=252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of pb_yoy_chg
def f086dmt_f086_daily_market_metrics_pb_yoy_chg_slope_252d_2d_v014_signal(pb, closeadj):
    base = pb.diff(periods=252)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of pb_yoy_chg
def f086dmt_f086_daily_market_metrics_pb_yoy_chg_slope_504d_2d_v015_signal(pb, closeadj):
    base = pb.diff(periods=252)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of pe_yoy_chg
def f086dmt_f086_daily_market_metrics_pe_yoy_chg_slope_21d_2d_v016_signal(pe, closeadj):
    base = pe.diff(periods=252)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of pe_yoy_chg
def f086dmt_f086_daily_market_metrics_pe_yoy_chg_slope_63d_2d_v017_signal(pe, closeadj):
    base = pe.diff(periods=252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of pe_yoy_chg
def f086dmt_f086_daily_market_metrics_pe_yoy_chg_slope_126d_2d_v018_signal(pe, closeadj):
    base = pe.diff(periods=252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of pe_yoy_chg
def f086dmt_f086_daily_market_metrics_pe_yoy_chg_slope_252d_2d_v019_signal(pe, closeadj):
    base = pe.diff(periods=252)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of pe_yoy_chg
def f086dmt_f086_daily_market_metrics_pe_yoy_chg_slope_504d_2d_v020_signal(pe, closeadj):
    base = pe.diff(periods=252)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of ps_yoy_chg
def f086dmt_f086_daily_market_metrics_ps_yoy_chg_slope_21d_2d_v021_signal(ps, closeadj):
    base = ps.diff(periods=252)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of ps_yoy_chg
def f086dmt_f086_daily_market_metrics_ps_yoy_chg_slope_63d_2d_v022_signal(ps, closeadj):
    base = ps.diff(periods=252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of ps_yoy_chg
def f086dmt_f086_daily_market_metrics_ps_yoy_chg_slope_126d_2d_v023_signal(ps, closeadj):
    base = ps.diff(periods=252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of ps_yoy_chg
def f086dmt_f086_daily_market_metrics_ps_yoy_chg_slope_252d_2d_v024_signal(ps, closeadj):
    base = ps.diff(periods=252)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of ps_yoy_chg
def f086dmt_f086_daily_market_metrics_ps_yoy_chg_slope_504d_2d_v025_signal(ps, closeadj):
    base = ps.diff(periods=252)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of mcap_rank_proxy
def f086dmt_f086_daily_market_metrics_mcap_rank_proxy_slope_21d_2d_v026_signal(marketcap, closeadj):
    base = marketcap.rolling(252, min_periods=63).rank(pct=True)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of mcap_rank_proxy
def f086dmt_f086_daily_market_metrics_mcap_rank_proxy_slope_63d_2d_v027_signal(marketcap, closeadj):
    base = marketcap.rolling(252, min_periods=63).rank(pct=True)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of mcap_rank_proxy
def f086dmt_f086_daily_market_metrics_mcap_rank_proxy_slope_126d_2d_v028_signal(marketcap, closeadj):
    base = marketcap.rolling(252, min_periods=63).rank(pct=True)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of mcap_rank_proxy
def f086dmt_f086_daily_market_metrics_mcap_rank_proxy_slope_252d_2d_v029_signal(marketcap, closeadj):
    base = marketcap.rolling(252, min_periods=63).rank(pct=True)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of mcap_rank_proxy
def f086dmt_f086_daily_market_metrics_mcap_rank_proxy_slope_504d_2d_v030_signal(marketcap, closeadj):
    base = marketcap.rolling(252, min_periods=63).rank(pct=True)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of daily_mult_dispersion
def f086dmt_f086_daily_market_metrics_daily_mult_dispersion_slope_21d_2d_v031_signal(pe, ps, pb, closeadj):
    base = (pe + ps + pb) / 3
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of daily_mult_dispersion
def f086dmt_f086_daily_market_metrics_daily_mult_dispersion_slope_63d_2d_v032_signal(pe, ps, pb, closeadj):
    base = (pe + ps + pb) / 3
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of daily_mult_dispersion
def f086dmt_f086_daily_market_metrics_daily_mult_dispersion_slope_126d_2d_v033_signal(pe, ps, pb, closeadj):
    base = (pe + ps + pb) / 3
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of daily_mult_dispersion
def f086dmt_f086_daily_market_metrics_daily_mult_dispersion_slope_252d_2d_v034_signal(pe, ps, pb, closeadj):
    base = (pe + ps + pb) / 3
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of daily_mult_dispersion
def f086dmt_f086_daily_market_metrics_daily_mult_dispersion_slope_504d_2d_v035_signal(pe, ps, pb, closeadj):
    base = (pe + ps + pb) / 3
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of price_yoy
def f086dmt_f086_daily_market_metrics_price_yoy_sm21_sl21_2d_v036_signal(close, closeadj):
    base = _mean(_f086_priceyoy(close), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of price_yoy
def f086dmt_f086_daily_market_metrics_price_yoy_sm63_sl21_2d_v037_signal(close, closeadj):
    base = _mean(_f086_priceyoy(close), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of price_yoy
def f086dmt_f086_daily_market_metrics_price_yoy_sm63_sl63_2d_v038_signal(close, closeadj):
    base = _mean(_f086_priceyoy(close), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of price_yoy
def f086dmt_f086_daily_market_metrics_price_yoy_sm252_sl63_2d_v039_signal(close, closeadj):
    base = _mean(_f086_priceyoy(close), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of price_yoy
def f086dmt_f086_daily_market_metrics_price_yoy_sm252_sl126_2d_v040_signal(close, closeadj):
    base = _mean(_f086_priceyoy(close), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of ev_yoy
def f086dmt_f086_daily_market_metrics_ev_yoy_sm21_sl21_2d_v041_signal(ev, closeadj):
    base = _mean(ev.pct_change(periods=252), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of ev_yoy
def f086dmt_f086_daily_market_metrics_ev_yoy_sm63_sl21_2d_v042_signal(ev, closeadj):
    base = _mean(ev.pct_change(periods=252), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of ev_yoy
def f086dmt_f086_daily_market_metrics_ev_yoy_sm63_sl63_2d_v043_signal(ev, closeadj):
    base = _mean(ev.pct_change(periods=252), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of ev_yoy
def f086dmt_f086_daily_market_metrics_ev_yoy_sm252_sl63_2d_v044_signal(ev, closeadj):
    base = _mean(ev.pct_change(periods=252), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of ev_yoy
def f086dmt_f086_daily_market_metrics_ev_yoy_sm252_sl126_2d_v045_signal(ev, closeadj):
    base = _mean(ev.pct_change(periods=252), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of pb_yoy_chg
def f086dmt_f086_daily_market_metrics_pb_yoy_chg_sm21_sl21_2d_v046_signal(pb, closeadj):
    base = _mean(pb.diff(periods=252), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of pb_yoy_chg
def f086dmt_f086_daily_market_metrics_pb_yoy_chg_sm63_sl21_2d_v047_signal(pb, closeadj):
    base = _mean(pb.diff(periods=252), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of pb_yoy_chg
def f086dmt_f086_daily_market_metrics_pb_yoy_chg_sm63_sl63_2d_v048_signal(pb, closeadj):
    base = _mean(pb.diff(periods=252), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of pb_yoy_chg
def f086dmt_f086_daily_market_metrics_pb_yoy_chg_sm252_sl63_2d_v049_signal(pb, closeadj):
    base = _mean(pb.diff(periods=252), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of pb_yoy_chg
def f086dmt_f086_daily_market_metrics_pb_yoy_chg_sm252_sl126_2d_v050_signal(pb, closeadj):
    base = _mean(pb.diff(periods=252), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of pe_yoy_chg
def f086dmt_f086_daily_market_metrics_pe_yoy_chg_sm21_sl21_2d_v051_signal(pe, closeadj):
    base = _mean(pe.diff(periods=252), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of pe_yoy_chg
def f086dmt_f086_daily_market_metrics_pe_yoy_chg_sm63_sl21_2d_v052_signal(pe, closeadj):
    base = _mean(pe.diff(periods=252), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of pe_yoy_chg
def f086dmt_f086_daily_market_metrics_pe_yoy_chg_sm63_sl63_2d_v053_signal(pe, closeadj):
    base = _mean(pe.diff(periods=252), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of pe_yoy_chg
def f086dmt_f086_daily_market_metrics_pe_yoy_chg_sm252_sl63_2d_v054_signal(pe, closeadj):
    base = _mean(pe.diff(periods=252), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of pe_yoy_chg
def f086dmt_f086_daily_market_metrics_pe_yoy_chg_sm252_sl126_2d_v055_signal(pe, closeadj):
    base = _mean(pe.diff(periods=252), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of ps_yoy_chg
def f086dmt_f086_daily_market_metrics_ps_yoy_chg_sm21_sl21_2d_v056_signal(ps, closeadj):
    base = _mean(ps.diff(periods=252), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of ps_yoy_chg
def f086dmt_f086_daily_market_metrics_ps_yoy_chg_sm63_sl21_2d_v057_signal(ps, closeadj):
    base = _mean(ps.diff(periods=252), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of ps_yoy_chg
def f086dmt_f086_daily_market_metrics_ps_yoy_chg_sm63_sl63_2d_v058_signal(ps, closeadj):
    base = _mean(ps.diff(periods=252), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of ps_yoy_chg
def f086dmt_f086_daily_market_metrics_ps_yoy_chg_sm252_sl63_2d_v059_signal(ps, closeadj):
    base = _mean(ps.diff(periods=252), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of ps_yoy_chg
def f086dmt_f086_daily_market_metrics_ps_yoy_chg_sm252_sl126_2d_v060_signal(ps, closeadj):
    base = _mean(ps.diff(periods=252), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of mcap_rank_proxy
def f086dmt_f086_daily_market_metrics_mcap_rank_proxy_sm21_sl21_2d_v061_signal(marketcap, closeadj):
    base = _mean(marketcap.rolling(252, min_periods=63).rank(pct=True), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of mcap_rank_proxy
def f086dmt_f086_daily_market_metrics_mcap_rank_proxy_sm63_sl21_2d_v062_signal(marketcap, closeadj):
    base = _mean(marketcap.rolling(252, min_periods=63).rank(pct=True), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of mcap_rank_proxy
def f086dmt_f086_daily_market_metrics_mcap_rank_proxy_sm63_sl63_2d_v063_signal(marketcap, closeadj):
    base = _mean(marketcap.rolling(252, min_periods=63).rank(pct=True), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of mcap_rank_proxy
def f086dmt_f086_daily_market_metrics_mcap_rank_proxy_sm252_sl63_2d_v064_signal(marketcap, closeadj):
    base = _mean(marketcap.rolling(252, min_periods=63).rank(pct=True), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of mcap_rank_proxy
def f086dmt_f086_daily_market_metrics_mcap_rank_proxy_sm252_sl126_2d_v065_signal(marketcap, closeadj):
    base = _mean(marketcap.rolling(252, min_periods=63).rank(pct=True), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of daily_mult_dispersion
def f086dmt_f086_daily_market_metrics_daily_mult_dispersion_sm21_sl21_2d_v066_signal(pe, ps, pb, closeadj):
    base = _mean((pe + ps + pb) / 3, 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of daily_mult_dispersion
def f086dmt_f086_daily_market_metrics_daily_mult_dispersion_sm63_sl21_2d_v067_signal(pe, ps, pb, closeadj):
    base = _mean((pe + ps + pb) / 3, 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of daily_mult_dispersion
def f086dmt_f086_daily_market_metrics_daily_mult_dispersion_sm63_sl63_2d_v068_signal(pe, ps, pb, closeadj):
    base = _mean((pe + ps + pb) / 3, 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of daily_mult_dispersion
def f086dmt_f086_daily_market_metrics_daily_mult_dispersion_sm252_sl63_2d_v069_signal(pe, ps, pb, closeadj):
    base = _mean((pe + ps + pb) / 3, 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of daily_mult_dispersion
def f086dmt_f086_daily_market_metrics_daily_mult_dispersion_sm252_sl126_2d_v070_signal(pe, ps, pb, closeadj):
    base = _mean((pe + ps + pb) / 3, 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of price_yoy
def f086dmt_f086_daily_market_metrics_price_yoy_pctslope_21d_2d_v071_signal(close, closeadj):
    base = _f086_priceyoy(close)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of price_yoy
def f086dmt_f086_daily_market_metrics_price_yoy_pctslope_63d_2d_v072_signal(close, closeadj):
    base = _f086_priceyoy(close)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of price_yoy
def f086dmt_f086_daily_market_metrics_price_yoy_pctslope_252d_2d_v073_signal(close, closeadj):
    base = _f086_priceyoy(close)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of ev_yoy
def f086dmt_f086_daily_market_metrics_ev_yoy_pctslope_21d_2d_v074_signal(ev, closeadj):
    base = ev.pct_change(periods=252)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of ev_yoy
def f086dmt_f086_daily_market_metrics_ev_yoy_pctslope_63d_2d_v075_signal(ev, closeadj):
    base = ev.pct_change(periods=252)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of ev_yoy
def f086dmt_f086_daily_market_metrics_ev_yoy_pctslope_252d_2d_v076_signal(ev, closeadj):
    base = ev.pct_change(periods=252)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of pb_yoy_chg
def f086dmt_f086_daily_market_metrics_pb_yoy_chg_pctslope_21d_2d_v077_signal(pb, closeadj):
    base = pb.diff(periods=252)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of pb_yoy_chg
def f086dmt_f086_daily_market_metrics_pb_yoy_chg_pctslope_63d_2d_v078_signal(pb, closeadj):
    base = pb.diff(periods=252)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of pb_yoy_chg
def f086dmt_f086_daily_market_metrics_pb_yoy_chg_pctslope_252d_2d_v079_signal(pb, closeadj):
    base = pb.diff(periods=252)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of pe_yoy_chg
def f086dmt_f086_daily_market_metrics_pe_yoy_chg_pctslope_21d_2d_v080_signal(pe, closeadj):
    base = pe.diff(periods=252)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of pe_yoy_chg
def f086dmt_f086_daily_market_metrics_pe_yoy_chg_pctslope_63d_2d_v081_signal(pe, closeadj):
    base = pe.diff(periods=252)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of pe_yoy_chg
def f086dmt_f086_daily_market_metrics_pe_yoy_chg_pctslope_252d_2d_v082_signal(pe, closeadj):
    base = pe.diff(periods=252)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of ps_yoy_chg
def f086dmt_f086_daily_market_metrics_ps_yoy_chg_pctslope_21d_2d_v083_signal(ps, closeadj):
    base = ps.diff(periods=252)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of ps_yoy_chg
def f086dmt_f086_daily_market_metrics_ps_yoy_chg_pctslope_63d_2d_v084_signal(ps, closeadj):
    base = ps.diff(periods=252)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of ps_yoy_chg
def f086dmt_f086_daily_market_metrics_ps_yoy_chg_pctslope_252d_2d_v085_signal(ps, closeadj):
    base = ps.diff(periods=252)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of mcap_rank_proxy
def f086dmt_f086_daily_market_metrics_mcap_rank_proxy_pctslope_21d_2d_v086_signal(marketcap, closeadj):
    base = marketcap.rolling(252, min_periods=63).rank(pct=True)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of mcap_rank_proxy
def f086dmt_f086_daily_market_metrics_mcap_rank_proxy_pctslope_63d_2d_v087_signal(marketcap, closeadj):
    base = marketcap.rolling(252, min_periods=63).rank(pct=True)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of mcap_rank_proxy
def f086dmt_f086_daily_market_metrics_mcap_rank_proxy_pctslope_252d_2d_v088_signal(marketcap, closeadj):
    base = marketcap.rolling(252, min_periods=63).rank(pct=True)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of daily_mult_dispersion
def f086dmt_f086_daily_market_metrics_daily_mult_dispersion_pctslope_21d_2d_v089_signal(pe, ps, pb, closeadj):
    base = (pe + ps + pb) / 3
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of daily_mult_dispersion
def f086dmt_f086_daily_market_metrics_daily_mult_dispersion_pctslope_63d_2d_v090_signal(pe, ps, pb, closeadj):
    base = (pe + ps + pb) / 3
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of daily_mult_dispersion
def f086dmt_f086_daily_market_metrics_daily_mult_dispersion_pctslope_252d_2d_v091_signal(pe, ps, pb, closeadj):
    base = (pe + ps + pb) / 3
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of price_yoy
def f086dmt_f086_daily_market_metrics_price_yoy_sgnslope_21d_2d_v092_signal(close, closeadj):
    base = _f086_priceyoy(close)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of price_yoy
def f086dmt_f086_daily_market_metrics_price_yoy_sgnslope_63d_2d_v093_signal(close, closeadj):
    base = _f086_priceyoy(close)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of price_yoy
def f086dmt_f086_daily_market_metrics_price_yoy_sgnslope_252d_2d_v094_signal(close, closeadj):
    base = _f086_priceyoy(close)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of ev_yoy
def f086dmt_f086_daily_market_metrics_ev_yoy_sgnslope_21d_2d_v095_signal(ev, closeadj):
    base = ev.pct_change(periods=252)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of ev_yoy
def f086dmt_f086_daily_market_metrics_ev_yoy_sgnslope_63d_2d_v096_signal(ev, closeadj):
    base = ev.pct_change(periods=252)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of ev_yoy
def f086dmt_f086_daily_market_metrics_ev_yoy_sgnslope_252d_2d_v097_signal(ev, closeadj):
    base = ev.pct_change(periods=252)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of pb_yoy_chg
def f086dmt_f086_daily_market_metrics_pb_yoy_chg_sgnslope_21d_2d_v098_signal(pb, closeadj):
    base = pb.diff(periods=252)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of pb_yoy_chg
def f086dmt_f086_daily_market_metrics_pb_yoy_chg_sgnslope_63d_2d_v099_signal(pb, closeadj):
    base = pb.diff(periods=252)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of pb_yoy_chg
def f086dmt_f086_daily_market_metrics_pb_yoy_chg_sgnslope_252d_2d_v100_signal(pb, closeadj):
    base = pb.diff(periods=252)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of pe_yoy_chg
def f086dmt_f086_daily_market_metrics_pe_yoy_chg_sgnslope_21d_2d_v101_signal(pe, closeadj):
    base = pe.diff(periods=252)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of pe_yoy_chg
def f086dmt_f086_daily_market_metrics_pe_yoy_chg_sgnslope_63d_2d_v102_signal(pe, closeadj):
    base = pe.diff(periods=252)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of pe_yoy_chg
def f086dmt_f086_daily_market_metrics_pe_yoy_chg_sgnslope_252d_2d_v103_signal(pe, closeadj):
    base = pe.diff(periods=252)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of ps_yoy_chg
def f086dmt_f086_daily_market_metrics_ps_yoy_chg_sgnslope_21d_2d_v104_signal(ps, closeadj):
    base = ps.diff(periods=252)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of ps_yoy_chg
def f086dmt_f086_daily_market_metrics_ps_yoy_chg_sgnslope_63d_2d_v105_signal(ps, closeadj):
    base = ps.diff(periods=252)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of ps_yoy_chg
def f086dmt_f086_daily_market_metrics_ps_yoy_chg_sgnslope_252d_2d_v106_signal(ps, closeadj):
    base = ps.diff(periods=252)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of mcap_rank_proxy
def f086dmt_f086_daily_market_metrics_mcap_rank_proxy_sgnslope_21d_2d_v107_signal(marketcap, closeadj):
    base = marketcap.rolling(252, min_periods=63).rank(pct=True)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of mcap_rank_proxy
def f086dmt_f086_daily_market_metrics_mcap_rank_proxy_sgnslope_63d_2d_v108_signal(marketcap, closeadj):
    base = marketcap.rolling(252, min_periods=63).rank(pct=True)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of mcap_rank_proxy
def f086dmt_f086_daily_market_metrics_mcap_rank_proxy_sgnslope_252d_2d_v109_signal(marketcap, closeadj):
    base = marketcap.rolling(252, min_periods=63).rank(pct=True)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of daily_mult_dispersion
def f086dmt_f086_daily_market_metrics_daily_mult_dispersion_sgnslope_21d_2d_v110_signal(pe, ps, pb, closeadj):
    base = (pe + ps + pb) / 3
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of daily_mult_dispersion
def f086dmt_f086_daily_market_metrics_daily_mult_dispersion_sgnslope_63d_2d_v111_signal(pe, ps, pb, closeadj):
    base = (pe + ps + pb) / 3
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of daily_mult_dispersion
def f086dmt_f086_daily_market_metrics_daily_mult_dispersion_sgnslope_252d_2d_v112_signal(pe, ps, pb, closeadj):
    base = (pe + ps + pb) / 3
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of price_yoy
def f086dmt_f086_daily_market_metrics_price_yoy_logmagslope_21d_2d_v113_signal(close, closeadj):
    base = _f086_priceyoy(close)
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of price_yoy
def f086dmt_f086_daily_market_metrics_price_yoy_logmagslope_63d_2d_v114_signal(close, closeadj):
    base = _f086_priceyoy(close)
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of price_yoy
def f086dmt_f086_daily_market_metrics_price_yoy_logmagslope_252d_2d_v115_signal(close, closeadj):
    base = _f086_priceyoy(close)
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of ev_yoy
def f086dmt_f086_daily_market_metrics_ev_yoy_logmagslope_21d_2d_v116_signal(ev, closeadj):
    base = ev.pct_change(periods=252)
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of ev_yoy
def f086dmt_f086_daily_market_metrics_ev_yoy_logmagslope_63d_2d_v117_signal(ev, closeadj):
    base = ev.pct_change(periods=252)
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of ev_yoy
def f086dmt_f086_daily_market_metrics_ev_yoy_logmagslope_252d_2d_v118_signal(ev, closeadj):
    base = ev.pct_change(periods=252)
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of pb_yoy_chg
def f086dmt_f086_daily_market_metrics_pb_yoy_chg_logmagslope_21d_2d_v119_signal(pb, closeadj):
    base = pb.diff(periods=252)
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of pb_yoy_chg
def f086dmt_f086_daily_market_metrics_pb_yoy_chg_logmagslope_63d_2d_v120_signal(pb, closeadj):
    base = pb.diff(periods=252)
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of pb_yoy_chg
def f086dmt_f086_daily_market_metrics_pb_yoy_chg_logmagslope_252d_2d_v121_signal(pb, closeadj):
    base = pb.diff(periods=252)
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of pe_yoy_chg
def f086dmt_f086_daily_market_metrics_pe_yoy_chg_logmagslope_21d_2d_v122_signal(pe, closeadj):
    base = pe.diff(periods=252)
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of pe_yoy_chg
def f086dmt_f086_daily_market_metrics_pe_yoy_chg_logmagslope_63d_2d_v123_signal(pe, closeadj):
    base = pe.diff(periods=252)
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of pe_yoy_chg
def f086dmt_f086_daily_market_metrics_pe_yoy_chg_logmagslope_252d_2d_v124_signal(pe, closeadj):
    base = pe.diff(periods=252)
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of ps_yoy_chg
def f086dmt_f086_daily_market_metrics_ps_yoy_chg_logmagslope_21d_2d_v125_signal(ps, closeadj):
    base = ps.diff(periods=252)
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of ps_yoy_chg
def f086dmt_f086_daily_market_metrics_ps_yoy_chg_logmagslope_63d_2d_v126_signal(ps, closeadj):
    base = ps.diff(periods=252)
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of ps_yoy_chg
def f086dmt_f086_daily_market_metrics_ps_yoy_chg_logmagslope_252d_2d_v127_signal(ps, closeadj):
    base = ps.diff(periods=252)
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of mcap_rank_proxy
def f086dmt_f086_daily_market_metrics_mcap_rank_proxy_logmagslope_21d_2d_v128_signal(marketcap, closeadj):
    base = marketcap.rolling(252, min_periods=63).rank(pct=True)
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of mcap_rank_proxy
def f086dmt_f086_daily_market_metrics_mcap_rank_proxy_logmagslope_63d_2d_v129_signal(marketcap, closeadj):
    base = marketcap.rolling(252, min_periods=63).rank(pct=True)
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of mcap_rank_proxy
def f086dmt_f086_daily_market_metrics_mcap_rank_proxy_logmagslope_252d_2d_v130_signal(marketcap, closeadj):
    base = marketcap.rolling(252, min_periods=63).rank(pct=True)
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of daily_mult_dispersion
def f086dmt_f086_daily_market_metrics_daily_mult_dispersion_logmagslope_21d_2d_v131_signal(pe, ps, pb, closeadj):
    base = (pe + ps + pb) / 3
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of daily_mult_dispersion
def f086dmt_f086_daily_market_metrics_daily_mult_dispersion_logmagslope_63d_2d_v132_signal(pe, ps, pb, closeadj):
    base = (pe + ps + pb) / 3
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of daily_mult_dispersion
def f086dmt_f086_daily_market_metrics_daily_mult_dispersion_logmagslope_252d_2d_v133_signal(pe, ps, pb, closeadj):
    base = (pe + ps + pb) / 3
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|price_yoy|
def f086dmt_f086_daily_market_metrics_price_yoy_logslope_63d_2d_v134_signal(close, closeadj):
    base = np.log((_f086_priceyoy(close)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|price_yoy|
def f086dmt_f086_daily_market_metrics_price_yoy_logslope_252d_2d_v135_signal(close, closeadj):
    base = np.log((_f086_priceyoy(close)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|ev_yoy|
def f086dmt_f086_daily_market_metrics_ev_yoy_logslope_63d_2d_v136_signal(ev, closeadj):
    base = np.log((ev.pct_change(periods=252)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|ev_yoy|
def f086dmt_f086_daily_market_metrics_ev_yoy_logslope_252d_2d_v137_signal(ev, closeadj):
    base = np.log((ev.pct_change(periods=252)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|pb_yoy_chg|
def f086dmt_f086_daily_market_metrics_pb_yoy_chg_logslope_63d_2d_v138_signal(pb, closeadj):
    base = np.log((pb.diff(periods=252)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|pb_yoy_chg|
def f086dmt_f086_daily_market_metrics_pb_yoy_chg_logslope_252d_2d_v139_signal(pb, closeadj):
    base = np.log((pb.diff(periods=252)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|pe_yoy_chg|
def f086dmt_f086_daily_market_metrics_pe_yoy_chg_logslope_63d_2d_v140_signal(pe, closeadj):
    base = np.log((pe.diff(periods=252)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|pe_yoy_chg|
def f086dmt_f086_daily_market_metrics_pe_yoy_chg_logslope_252d_2d_v141_signal(pe, closeadj):
    base = np.log((pe.diff(periods=252)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|ps_yoy_chg|
def f086dmt_f086_daily_market_metrics_ps_yoy_chg_logslope_63d_2d_v142_signal(ps, closeadj):
    base = np.log((ps.diff(periods=252)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|ps_yoy_chg|
def f086dmt_f086_daily_market_metrics_ps_yoy_chg_logslope_252d_2d_v143_signal(ps, closeadj):
    base = np.log((ps.diff(periods=252)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|mcap_rank_proxy|
def f086dmt_f086_daily_market_metrics_mcap_rank_proxy_logslope_63d_2d_v144_signal(marketcap, closeadj):
    base = np.log((marketcap.rolling(252, min_periods=63).rank(pct=True)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|mcap_rank_proxy|
def f086dmt_f086_daily_market_metrics_mcap_rank_proxy_logslope_252d_2d_v145_signal(marketcap, closeadj):
    base = np.log((marketcap.rolling(252, min_periods=63).rank(pct=True)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|daily_mult_dispersion|
def f086dmt_f086_daily_market_metrics_daily_mult_dispersion_logslope_63d_2d_v146_signal(pe, ps, pb, closeadj):
    base = np.log(((pe + ps + pb) / 3).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|daily_mult_dispersion|
def f086dmt_f086_daily_market_metrics_daily_mult_dispersion_logslope_252d_2d_v147_signal(pe, ps, pb, closeadj):
    base = np.log(((pe + ps + pb) / 3).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

