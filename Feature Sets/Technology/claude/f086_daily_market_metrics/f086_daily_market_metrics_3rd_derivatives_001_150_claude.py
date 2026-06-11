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


# 21d acceleration of price_yoy
def f086dmt_f086_daily_market_metrics_price_yoy_accel_21d_3d_v001_signal(close, closeadj):
    base = _f086_priceyoy(close)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of price_yoy
def f086dmt_f086_daily_market_metrics_price_yoy_accel_63d_3d_v002_signal(close, closeadj):
    base = _f086_priceyoy(close)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of price_yoy
def f086dmt_f086_daily_market_metrics_price_yoy_accel_126d_3d_v003_signal(close, closeadj):
    base = _f086_priceyoy(close)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of price_yoy
def f086dmt_f086_daily_market_metrics_price_yoy_accel_252d_3d_v004_signal(close, closeadj):
    base = _f086_priceyoy(close)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of ev_yoy
def f086dmt_f086_daily_market_metrics_ev_yoy_accel_21d_3d_v005_signal(ev, closeadj):
    base = ev.pct_change(periods=252)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of ev_yoy
def f086dmt_f086_daily_market_metrics_ev_yoy_accel_63d_3d_v006_signal(ev, closeadj):
    base = ev.pct_change(periods=252)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of ev_yoy
def f086dmt_f086_daily_market_metrics_ev_yoy_accel_126d_3d_v007_signal(ev, closeadj):
    base = ev.pct_change(periods=252)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of ev_yoy
def f086dmt_f086_daily_market_metrics_ev_yoy_accel_252d_3d_v008_signal(ev, closeadj):
    base = ev.pct_change(periods=252)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of pb_yoy_chg
def f086dmt_f086_daily_market_metrics_pb_yoy_chg_accel_21d_3d_v009_signal(pb, closeadj):
    base = pb.diff(periods=252)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of pb_yoy_chg
def f086dmt_f086_daily_market_metrics_pb_yoy_chg_accel_63d_3d_v010_signal(pb, closeadj):
    base = pb.diff(periods=252)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of pb_yoy_chg
def f086dmt_f086_daily_market_metrics_pb_yoy_chg_accel_126d_3d_v011_signal(pb, closeadj):
    base = pb.diff(periods=252)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of pb_yoy_chg
def f086dmt_f086_daily_market_metrics_pb_yoy_chg_accel_252d_3d_v012_signal(pb, closeadj):
    base = pb.diff(periods=252)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of pe_yoy_chg
def f086dmt_f086_daily_market_metrics_pe_yoy_chg_accel_21d_3d_v013_signal(pe, closeadj):
    base = pe.diff(periods=252)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of pe_yoy_chg
def f086dmt_f086_daily_market_metrics_pe_yoy_chg_accel_63d_3d_v014_signal(pe, closeadj):
    base = pe.diff(periods=252)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of pe_yoy_chg
def f086dmt_f086_daily_market_metrics_pe_yoy_chg_accel_126d_3d_v015_signal(pe, closeadj):
    base = pe.diff(periods=252)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of pe_yoy_chg
def f086dmt_f086_daily_market_metrics_pe_yoy_chg_accel_252d_3d_v016_signal(pe, closeadj):
    base = pe.diff(periods=252)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of ps_yoy_chg
def f086dmt_f086_daily_market_metrics_ps_yoy_chg_accel_21d_3d_v017_signal(ps, closeadj):
    base = ps.diff(periods=252)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of ps_yoy_chg
def f086dmt_f086_daily_market_metrics_ps_yoy_chg_accel_63d_3d_v018_signal(ps, closeadj):
    base = ps.diff(periods=252)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of ps_yoy_chg
def f086dmt_f086_daily_market_metrics_ps_yoy_chg_accel_126d_3d_v019_signal(ps, closeadj):
    base = ps.diff(periods=252)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of ps_yoy_chg
def f086dmt_f086_daily_market_metrics_ps_yoy_chg_accel_252d_3d_v020_signal(ps, closeadj):
    base = ps.diff(periods=252)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of mcap_rank_proxy
def f086dmt_f086_daily_market_metrics_mcap_rank_proxy_accel_21d_3d_v021_signal(marketcap, closeadj):
    base = marketcap.rolling(252, min_periods=63).rank(pct=True)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of mcap_rank_proxy
def f086dmt_f086_daily_market_metrics_mcap_rank_proxy_accel_63d_3d_v022_signal(marketcap, closeadj):
    base = marketcap.rolling(252, min_periods=63).rank(pct=True)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of mcap_rank_proxy
def f086dmt_f086_daily_market_metrics_mcap_rank_proxy_accel_126d_3d_v023_signal(marketcap, closeadj):
    base = marketcap.rolling(252, min_periods=63).rank(pct=True)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of mcap_rank_proxy
def f086dmt_f086_daily_market_metrics_mcap_rank_proxy_accel_252d_3d_v024_signal(marketcap, closeadj):
    base = marketcap.rolling(252, min_periods=63).rank(pct=True)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of daily_mult_dispersion
def f086dmt_f086_daily_market_metrics_daily_mult_dispersion_accel_21d_3d_v025_signal(pe, ps, pb, closeadj):
    base = (pe + ps + pb) / 3
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of daily_mult_dispersion
def f086dmt_f086_daily_market_metrics_daily_mult_dispersion_accel_63d_3d_v026_signal(pe, ps, pb, closeadj):
    base = (pe + ps + pb) / 3
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of daily_mult_dispersion
def f086dmt_f086_daily_market_metrics_daily_mult_dispersion_accel_126d_3d_v027_signal(pe, ps, pb, closeadj):
    base = (pe + ps + pb) / 3
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of daily_mult_dispersion
def f086dmt_f086_daily_market_metrics_daily_mult_dispersion_accel_252d_3d_v028_signal(pe, ps, pb, closeadj):
    base = (pe + ps + pb) / 3
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of price_yoy
def f086dmt_f086_daily_market_metrics_price_yoy_slopez_21d_z126_3d_v029_signal(close, closeadj):
    base = _f086_priceyoy(close)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of price_yoy
def f086dmt_f086_daily_market_metrics_price_yoy_slopez_63d_z252_3d_v030_signal(close, closeadj):
    base = _f086_priceyoy(close)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of price_yoy
def f086dmt_f086_daily_market_metrics_price_yoy_slopez_126d_z252_3d_v031_signal(close, closeadj):
    base = _f086_priceyoy(close)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of price_yoy
def f086dmt_f086_daily_market_metrics_price_yoy_slopez_252d_z504_3d_v032_signal(close, closeadj):
    base = _f086_priceyoy(close)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of ev_yoy
def f086dmt_f086_daily_market_metrics_ev_yoy_slopez_21d_z126_3d_v033_signal(ev, closeadj):
    base = ev.pct_change(periods=252)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of ev_yoy
def f086dmt_f086_daily_market_metrics_ev_yoy_slopez_63d_z252_3d_v034_signal(ev, closeadj):
    base = ev.pct_change(periods=252)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of ev_yoy
def f086dmt_f086_daily_market_metrics_ev_yoy_slopez_126d_z252_3d_v035_signal(ev, closeadj):
    base = ev.pct_change(periods=252)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of ev_yoy
def f086dmt_f086_daily_market_metrics_ev_yoy_slopez_252d_z504_3d_v036_signal(ev, closeadj):
    base = ev.pct_change(periods=252)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of pb_yoy_chg
def f086dmt_f086_daily_market_metrics_pb_yoy_chg_slopez_21d_z126_3d_v037_signal(pb, closeadj):
    base = pb.diff(periods=252)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of pb_yoy_chg
def f086dmt_f086_daily_market_metrics_pb_yoy_chg_slopez_63d_z252_3d_v038_signal(pb, closeadj):
    base = pb.diff(periods=252)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of pb_yoy_chg
def f086dmt_f086_daily_market_metrics_pb_yoy_chg_slopez_126d_z252_3d_v039_signal(pb, closeadj):
    base = pb.diff(periods=252)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of pb_yoy_chg
def f086dmt_f086_daily_market_metrics_pb_yoy_chg_slopez_252d_z504_3d_v040_signal(pb, closeadj):
    base = pb.diff(periods=252)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of pe_yoy_chg
def f086dmt_f086_daily_market_metrics_pe_yoy_chg_slopez_21d_z126_3d_v041_signal(pe, closeadj):
    base = pe.diff(periods=252)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of pe_yoy_chg
def f086dmt_f086_daily_market_metrics_pe_yoy_chg_slopez_63d_z252_3d_v042_signal(pe, closeadj):
    base = pe.diff(periods=252)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of pe_yoy_chg
def f086dmt_f086_daily_market_metrics_pe_yoy_chg_slopez_126d_z252_3d_v043_signal(pe, closeadj):
    base = pe.diff(periods=252)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of pe_yoy_chg
def f086dmt_f086_daily_market_metrics_pe_yoy_chg_slopez_252d_z504_3d_v044_signal(pe, closeadj):
    base = pe.diff(periods=252)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of ps_yoy_chg
def f086dmt_f086_daily_market_metrics_ps_yoy_chg_slopez_21d_z126_3d_v045_signal(ps, closeadj):
    base = ps.diff(periods=252)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of ps_yoy_chg
def f086dmt_f086_daily_market_metrics_ps_yoy_chg_slopez_63d_z252_3d_v046_signal(ps, closeadj):
    base = ps.diff(periods=252)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of ps_yoy_chg
def f086dmt_f086_daily_market_metrics_ps_yoy_chg_slopez_126d_z252_3d_v047_signal(ps, closeadj):
    base = ps.diff(periods=252)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of ps_yoy_chg
def f086dmt_f086_daily_market_metrics_ps_yoy_chg_slopez_252d_z504_3d_v048_signal(ps, closeadj):
    base = ps.diff(periods=252)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of mcap_rank_proxy
def f086dmt_f086_daily_market_metrics_mcap_rank_proxy_slopez_21d_z126_3d_v049_signal(marketcap, closeadj):
    base = marketcap.rolling(252, min_periods=63).rank(pct=True)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of mcap_rank_proxy
def f086dmt_f086_daily_market_metrics_mcap_rank_proxy_slopez_63d_z252_3d_v050_signal(marketcap, closeadj):
    base = marketcap.rolling(252, min_periods=63).rank(pct=True)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of mcap_rank_proxy
def f086dmt_f086_daily_market_metrics_mcap_rank_proxy_slopez_126d_z252_3d_v051_signal(marketcap, closeadj):
    base = marketcap.rolling(252, min_periods=63).rank(pct=True)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of mcap_rank_proxy
def f086dmt_f086_daily_market_metrics_mcap_rank_proxy_slopez_252d_z504_3d_v052_signal(marketcap, closeadj):
    base = marketcap.rolling(252, min_periods=63).rank(pct=True)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of daily_mult_dispersion
def f086dmt_f086_daily_market_metrics_daily_mult_dispersion_slopez_21d_z126_3d_v053_signal(pe, ps, pb, closeadj):
    base = (pe + ps + pb) / 3
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of daily_mult_dispersion
def f086dmt_f086_daily_market_metrics_daily_mult_dispersion_slopez_63d_z252_3d_v054_signal(pe, ps, pb, closeadj):
    base = (pe + ps + pb) / 3
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of daily_mult_dispersion
def f086dmt_f086_daily_market_metrics_daily_mult_dispersion_slopez_126d_z252_3d_v055_signal(pe, ps, pb, closeadj):
    base = (pe + ps + pb) / 3
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of daily_mult_dispersion
def f086dmt_f086_daily_market_metrics_daily_mult_dispersion_slopez_252d_z504_3d_v056_signal(pe, ps, pb, closeadj):
    base = (pe + ps + pb) / 3
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of price_yoy
def f086dmt_f086_daily_market_metrics_price_yoy_jerk_21d_3d_v057_signal(close, closeadj):
    base = _f086_priceyoy(close)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of price_yoy
def f086dmt_f086_daily_market_metrics_price_yoy_jerk_63d_3d_v058_signal(close, closeadj):
    base = _f086_priceyoy(close)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of price_yoy
def f086dmt_f086_daily_market_metrics_price_yoy_jerk_126d_3d_v059_signal(close, closeadj):
    base = _f086_priceyoy(close)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of ev_yoy
def f086dmt_f086_daily_market_metrics_ev_yoy_jerk_21d_3d_v060_signal(ev, closeadj):
    base = ev.pct_change(periods=252)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of ev_yoy
def f086dmt_f086_daily_market_metrics_ev_yoy_jerk_63d_3d_v061_signal(ev, closeadj):
    base = ev.pct_change(periods=252)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of ev_yoy
def f086dmt_f086_daily_market_metrics_ev_yoy_jerk_126d_3d_v062_signal(ev, closeadj):
    base = ev.pct_change(periods=252)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of pb_yoy_chg
def f086dmt_f086_daily_market_metrics_pb_yoy_chg_jerk_21d_3d_v063_signal(pb, closeadj):
    base = pb.diff(periods=252)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of pb_yoy_chg
def f086dmt_f086_daily_market_metrics_pb_yoy_chg_jerk_63d_3d_v064_signal(pb, closeadj):
    base = pb.diff(periods=252)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of pb_yoy_chg
def f086dmt_f086_daily_market_metrics_pb_yoy_chg_jerk_126d_3d_v065_signal(pb, closeadj):
    base = pb.diff(periods=252)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of pe_yoy_chg
def f086dmt_f086_daily_market_metrics_pe_yoy_chg_jerk_21d_3d_v066_signal(pe, closeadj):
    base = pe.diff(periods=252)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of pe_yoy_chg
def f086dmt_f086_daily_market_metrics_pe_yoy_chg_jerk_63d_3d_v067_signal(pe, closeadj):
    base = pe.diff(periods=252)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of pe_yoy_chg
def f086dmt_f086_daily_market_metrics_pe_yoy_chg_jerk_126d_3d_v068_signal(pe, closeadj):
    base = pe.diff(periods=252)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of ps_yoy_chg
def f086dmt_f086_daily_market_metrics_ps_yoy_chg_jerk_21d_3d_v069_signal(ps, closeadj):
    base = ps.diff(periods=252)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of ps_yoy_chg
def f086dmt_f086_daily_market_metrics_ps_yoy_chg_jerk_63d_3d_v070_signal(ps, closeadj):
    base = ps.diff(periods=252)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of ps_yoy_chg
def f086dmt_f086_daily_market_metrics_ps_yoy_chg_jerk_126d_3d_v071_signal(ps, closeadj):
    base = ps.diff(periods=252)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of mcap_rank_proxy
def f086dmt_f086_daily_market_metrics_mcap_rank_proxy_jerk_21d_3d_v072_signal(marketcap, closeadj):
    base = marketcap.rolling(252, min_periods=63).rank(pct=True)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of mcap_rank_proxy
def f086dmt_f086_daily_market_metrics_mcap_rank_proxy_jerk_63d_3d_v073_signal(marketcap, closeadj):
    base = marketcap.rolling(252, min_periods=63).rank(pct=True)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of mcap_rank_proxy
def f086dmt_f086_daily_market_metrics_mcap_rank_proxy_jerk_126d_3d_v074_signal(marketcap, closeadj):
    base = marketcap.rolling(252, min_periods=63).rank(pct=True)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of daily_mult_dispersion
def f086dmt_f086_daily_market_metrics_daily_mult_dispersion_jerk_21d_3d_v075_signal(pe, ps, pb, closeadj):
    base = (pe + ps + pb) / 3
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of daily_mult_dispersion
def f086dmt_f086_daily_market_metrics_daily_mult_dispersion_jerk_63d_3d_v076_signal(pe, ps, pb, closeadj):
    base = (pe + ps + pb) / 3
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of daily_mult_dispersion
def f086dmt_f086_daily_market_metrics_daily_mult_dispersion_jerk_126d_3d_v077_signal(pe, ps, pb, closeadj):
    base = (pe + ps + pb) / 3
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of price_yoy smoothed over 252d
def f086dmt_f086_daily_market_metrics_price_yoy_smoothaccel_63d_sm252_3d_v078_signal(close, closeadj):
    base = _f086_priceyoy(close)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of price_yoy smoothed over 504d
def f086dmt_f086_daily_market_metrics_price_yoy_smoothaccel_252d_sm504_3d_v079_signal(close, closeadj):
    base = _f086_priceyoy(close)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of ev_yoy smoothed over 252d
def f086dmt_f086_daily_market_metrics_ev_yoy_smoothaccel_63d_sm252_3d_v080_signal(ev, closeadj):
    base = ev.pct_change(periods=252)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of ev_yoy smoothed over 504d
def f086dmt_f086_daily_market_metrics_ev_yoy_smoothaccel_252d_sm504_3d_v081_signal(ev, closeadj):
    base = ev.pct_change(periods=252)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of pb_yoy_chg smoothed over 252d
def f086dmt_f086_daily_market_metrics_pb_yoy_chg_smoothaccel_63d_sm252_3d_v082_signal(pb, closeadj):
    base = pb.diff(periods=252)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of pb_yoy_chg smoothed over 504d
def f086dmt_f086_daily_market_metrics_pb_yoy_chg_smoothaccel_252d_sm504_3d_v083_signal(pb, closeadj):
    base = pb.diff(periods=252)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of pe_yoy_chg smoothed over 252d
def f086dmt_f086_daily_market_metrics_pe_yoy_chg_smoothaccel_63d_sm252_3d_v084_signal(pe, closeadj):
    base = pe.diff(periods=252)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of pe_yoy_chg smoothed over 504d
def f086dmt_f086_daily_market_metrics_pe_yoy_chg_smoothaccel_252d_sm504_3d_v085_signal(pe, closeadj):
    base = pe.diff(periods=252)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of ps_yoy_chg smoothed over 252d
def f086dmt_f086_daily_market_metrics_ps_yoy_chg_smoothaccel_63d_sm252_3d_v086_signal(ps, closeadj):
    base = ps.diff(periods=252)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of ps_yoy_chg smoothed over 504d
def f086dmt_f086_daily_market_metrics_ps_yoy_chg_smoothaccel_252d_sm504_3d_v087_signal(ps, closeadj):
    base = ps.diff(periods=252)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of mcap_rank_proxy smoothed over 252d
def f086dmt_f086_daily_market_metrics_mcap_rank_proxy_smoothaccel_63d_sm252_3d_v088_signal(marketcap, closeadj):
    base = marketcap.rolling(252, min_periods=63).rank(pct=True)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of mcap_rank_proxy smoothed over 504d
def f086dmt_f086_daily_market_metrics_mcap_rank_proxy_smoothaccel_252d_sm504_3d_v089_signal(marketcap, closeadj):
    base = marketcap.rolling(252, min_periods=63).rank(pct=True)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of daily_mult_dispersion smoothed over 252d
def f086dmt_f086_daily_market_metrics_daily_mult_dispersion_smoothaccel_63d_sm252_3d_v090_signal(pe, ps, pb, closeadj):
    base = (pe + ps + pb) / 3
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of daily_mult_dispersion smoothed over 504d
def f086dmt_f086_daily_market_metrics_daily_mult_dispersion_smoothaccel_252d_sm504_3d_v091_signal(pe, ps, pb, closeadj):
    base = (pe + ps + pb) / 3
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of price_yoy
def f086dmt_f086_daily_market_metrics_price_yoy_accelz_21d_z252_3d_v092_signal(close, closeadj):
    base = _f086_priceyoy(close)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of price_yoy
def f086dmt_f086_daily_market_metrics_price_yoy_accelz_63d_z504_3d_v093_signal(close, closeadj):
    base = _f086_priceyoy(close)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of ev_yoy
def f086dmt_f086_daily_market_metrics_ev_yoy_accelz_21d_z252_3d_v094_signal(ev, closeadj):
    base = ev.pct_change(periods=252)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of ev_yoy
def f086dmt_f086_daily_market_metrics_ev_yoy_accelz_63d_z504_3d_v095_signal(ev, closeadj):
    base = ev.pct_change(periods=252)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of pb_yoy_chg
def f086dmt_f086_daily_market_metrics_pb_yoy_chg_accelz_21d_z252_3d_v096_signal(pb, closeadj):
    base = pb.diff(periods=252)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of pb_yoy_chg
def f086dmt_f086_daily_market_metrics_pb_yoy_chg_accelz_63d_z504_3d_v097_signal(pb, closeadj):
    base = pb.diff(periods=252)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of pe_yoy_chg
def f086dmt_f086_daily_market_metrics_pe_yoy_chg_accelz_21d_z252_3d_v098_signal(pe, closeadj):
    base = pe.diff(periods=252)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of pe_yoy_chg
def f086dmt_f086_daily_market_metrics_pe_yoy_chg_accelz_63d_z504_3d_v099_signal(pe, closeadj):
    base = pe.diff(periods=252)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of ps_yoy_chg
def f086dmt_f086_daily_market_metrics_ps_yoy_chg_accelz_21d_z252_3d_v100_signal(ps, closeadj):
    base = ps.diff(periods=252)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of ps_yoy_chg
def f086dmt_f086_daily_market_metrics_ps_yoy_chg_accelz_63d_z504_3d_v101_signal(ps, closeadj):
    base = ps.diff(periods=252)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of mcap_rank_proxy
def f086dmt_f086_daily_market_metrics_mcap_rank_proxy_accelz_21d_z252_3d_v102_signal(marketcap, closeadj):
    base = marketcap.rolling(252, min_periods=63).rank(pct=True)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of mcap_rank_proxy
def f086dmt_f086_daily_market_metrics_mcap_rank_proxy_accelz_63d_z504_3d_v103_signal(marketcap, closeadj):
    base = marketcap.rolling(252, min_periods=63).rank(pct=True)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of daily_mult_dispersion
def f086dmt_f086_daily_market_metrics_daily_mult_dispersion_accelz_21d_z252_3d_v104_signal(pe, ps, pb, closeadj):
    base = (pe + ps + pb) / 3
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of daily_mult_dispersion
def f086dmt_f086_daily_market_metrics_daily_mult_dispersion_accelz_63d_z504_3d_v105_signal(pe, ps, pb, closeadj):
    base = (pe + ps + pb) / 3
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in price_yoy (raw count, no price scaling)
def f086dmt_f086_daily_market_metrics_price_yoy_signflip_63d_3d_v106_signal(close, closeadj):
    base = _f086_priceyoy(close)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in price_yoy (raw count, no price scaling)
def f086dmt_f086_daily_market_metrics_price_yoy_signflip_252d_3d_v107_signal(close, closeadj):
    base = _f086_priceyoy(close)
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in ev_yoy (raw count, no price scaling)
def f086dmt_f086_daily_market_metrics_ev_yoy_signflip_63d_3d_v108_signal(ev, closeadj):
    base = ev.pct_change(periods=252)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in ev_yoy (raw count, no price scaling)
def f086dmt_f086_daily_market_metrics_ev_yoy_signflip_252d_3d_v109_signal(ev, closeadj):
    base = ev.pct_change(periods=252)
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in pb_yoy_chg (raw count, no price scaling)
def f086dmt_f086_daily_market_metrics_pb_yoy_chg_signflip_63d_3d_v110_signal(pb, closeadj):
    base = pb.diff(periods=252)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in pb_yoy_chg (raw count, no price scaling)
def f086dmt_f086_daily_market_metrics_pb_yoy_chg_signflip_252d_3d_v111_signal(pb, closeadj):
    base = pb.diff(periods=252)
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in pe_yoy_chg (raw count, no price scaling)
def f086dmt_f086_daily_market_metrics_pe_yoy_chg_signflip_63d_3d_v112_signal(pe, closeadj):
    base = pe.diff(periods=252)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in pe_yoy_chg (raw count, no price scaling)
def f086dmt_f086_daily_market_metrics_pe_yoy_chg_signflip_252d_3d_v113_signal(pe, closeadj):
    base = pe.diff(periods=252)
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in ps_yoy_chg (raw count, no price scaling)
def f086dmt_f086_daily_market_metrics_ps_yoy_chg_signflip_63d_3d_v114_signal(ps, closeadj):
    base = ps.diff(periods=252)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in ps_yoy_chg (raw count, no price scaling)
def f086dmt_f086_daily_market_metrics_ps_yoy_chg_signflip_252d_3d_v115_signal(ps, closeadj):
    base = ps.diff(periods=252)
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in mcap_rank_proxy (raw count, no price scaling)
def f086dmt_f086_daily_market_metrics_mcap_rank_proxy_signflip_63d_3d_v116_signal(marketcap, closeadj):
    base = marketcap.rolling(252, min_periods=63).rank(pct=True)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in mcap_rank_proxy (raw count, no price scaling)
def f086dmt_f086_daily_market_metrics_mcap_rank_proxy_signflip_252d_3d_v117_signal(marketcap, closeadj):
    base = marketcap.rolling(252, min_periods=63).rank(pct=True)
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in daily_mult_dispersion (raw count, no price scaling)
def f086dmt_f086_daily_market_metrics_daily_mult_dispersion_signflip_63d_3d_v118_signal(pe, ps, pb, closeadj):
    base = (pe + ps + pb) / 3
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in daily_mult_dispersion (raw count, no price scaling)
def f086dmt_f086_daily_market_metrics_daily_mult_dispersion_signflip_252d_3d_v119_signal(pe, ps, pb, closeadj):
    base = (pe + ps + pb) / 3
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of price_yoy normalized by 252d range
def f086dmt_f086_daily_market_metrics_price_yoy_rngaccel_63d_r252_3d_v120_signal(close, closeadj):
    base = _f086_priceyoy(close)
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of price_yoy normalized by 504d range
def f086dmt_f086_daily_market_metrics_price_yoy_rngaccel_252d_r504_3d_v121_signal(close, closeadj):
    base = _f086_priceyoy(close)
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of ev_yoy normalized by 252d range
def f086dmt_f086_daily_market_metrics_ev_yoy_rngaccel_63d_r252_3d_v122_signal(ev, closeadj):
    base = ev.pct_change(periods=252)
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of ev_yoy normalized by 504d range
def f086dmt_f086_daily_market_metrics_ev_yoy_rngaccel_252d_r504_3d_v123_signal(ev, closeadj):
    base = ev.pct_change(periods=252)
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of pb_yoy_chg normalized by 252d range
def f086dmt_f086_daily_market_metrics_pb_yoy_chg_rngaccel_63d_r252_3d_v124_signal(pb, closeadj):
    base = pb.diff(periods=252)
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of pb_yoy_chg normalized by 504d range
def f086dmt_f086_daily_market_metrics_pb_yoy_chg_rngaccel_252d_r504_3d_v125_signal(pb, closeadj):
    base = pb.diff(periods=252)
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of pe_yoy_chg normalized by 252d range
def f086dmt_f086_daily_market_metrics_pe_yoy_chg_rngaccel_63d_r252_3d_v126_signal(pe, closeadj):
    base = pe.diff(periods=252)
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of pe_yoy_chg normalized by 504d range
def f086dmt_f086_daily_market_metrics_pe_yoy_chg_rngaccel_252d_r504_3d_v127_signal(pe, closeadj):
    base = pe.diff(periods=252)
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of ps_yoy_chg normalized by 252d range
def f086dmt_f086_daily_market_metrics_ps_yoy_chg_rngaccel_63d_r252_3d_v128_signal(ps, closeadj):
    base = ps.diff(periods=252)
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of ps_yoy_chg normalized by 504d range
def f086dmt_f086_daily_market_metrics_ps_yoy_chg_rngaccel_252d_r504_3d_v129_signal(ps, closeadj):
    base = ps.diff(periods=252)
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of mcap_rank_proxy normalized by 252d range
def f086dmt_f086_daily_market_metrics_mcap_rank_proxy_rngaccel_63d_r252_3d_v130_signal(marketcap, closeadj):
    base = marketcap.rolling(252, min_periods=63).rank(pct=True)
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of mcap_rank_proxy normalized by 504d range
def f086dmt_f086_daily_market_metrics_mcap_rank_proxy_rngaccel_252d_r504_3d_v131_signal(marketcap, closeadj):
    base = marketcap.rolling(252, min_periods=63).rank(pct=True)
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of daily_mult_dispersion normalized by 252d range
def f086dmt_f086_daily_market_metrics_daily_mult_dispersion_rngaccel_63d_r252_3d_v132_signal(pe, ps, pb, closeadj):
    base = (pe + ps + pb) / 3
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of daily_mult_dispersion normalized by 504d range
def f086dmt_f086_daily_market_metrics_daily_mult_dispersion_rngaccel_252d_r504_3d_v133_signal(pe, ps, pb, closeadj):
    base = (pe + ps + pb) / 3
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of price_yoy
def f086dmt_f086_daily_market_metrics_price_yoy_cumslope_21d_3d_v134_signal(close, closeadj):
    base = _f086_priceyoy(close)
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of price_yoy
def f086dmt_f086_daily_market_metrics_price_yoy_cumslope_63d_3d_v135_signal(close, closeadj):
    base = _f086_priceyoy(close)
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of price_yoy
def f086dmt_f086_daily_market_metrics_price_yoy_cumslope_252d_3d_v136_signal(close, closeadj):
    base = _f086_priceyoy(close)
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of ev_yoy
def f086dmt_f086_daily_market_metrics_ev_yoy_cumslope_21d_3d_v137_signal(ev, closeadj):
    base = ev.pct_change(periods=252)
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of ev_yoy
def f086dmt_f086_daily_market_metrics_ev_yoy_cumslope_63d_3d_v138_signal(ev, closeadj):
    base = ev.pct_change(periods=252)
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of ev_yoy
def f086dmt_f086_daily_market_metrics_ev_yoy_cumslope_252d_3d_v139_signal(ev, closeadj):
    base = ev.pct_change(periods=252)
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of pb_yoy_chg
def f086dmt_f086_daily_market_metrics_pb_yoy_chg_cumslope_21d_3d_v140_signal(pb, closeadj):
    base = pb.diff(periods=252)
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of pb_yoy_chg
def f086dmt_f086_daily_market_metrics_pb_yoy_chg_cumslope_63d_3d_v141_signal(pb, closeadj):
    base = pb.diff(periods=252)
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of pb_yoy_chg
def f086dmt_f086_daily_market_metrics_pb_yoy_chg_cumslope_252d_3d_v142_signal(pb, closeadj):
    base = pb.diff(periods=252)
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of pe_yoy_chg
def f086dmt_f086_daily_market_metrics_pe_yoy_chg_cumslope_21d_3d_v143_signal(pe, closeadj):
    base = pe.diff(periods=252)
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of pe_yoy_chg
def f086dmt_f086_daily_market_metrics_pe_yoy_chg_cumslope_63d_3d_v144_signal(pe, closeadj):
    base = pe.diff(periods=252)
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of pe_yoy_chg
def f086dmt_f086_daily_market_metrics_pe_yoy_chg_cumslope_252d_3d_v145_signal(pe, closeadj):
    base = pe.diff(periods=252)
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of ps_yoy_chg
def f086dmt_f086_daily_market_metrics_ps_yoy_chg_cumslope_21d_3d_v146_signal(ps, closeadj):
    base = ps.diff(periods=252)
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of ps_yoy_chg
def f086dmt_f086_daily_market_metrics_ps_yoy_chg_cumslope_63d_3d_v147_signal(ps, closeadj):
    base = ps.diff(periods=252)
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of ps_yoy_chg
def f086dmt_f086_daily_market_metrics_ps_yoy_chg_cumslope_252d_3d_v148_signal(ps, closeadj):
    base = ps.diff(periods=252)
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of mcap_rank_proxy
def f086dmt_f086_daily_market_metrics_mcap_rank_proxy_cumslope_21d_3d_v149_signal(marketcap, closeadj):
    base = marketcap.rolling(252, min_periods=63).rank(pct=True)
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of mcap_rank_proxy
def f086dmt_f086_daily_market_metrics_mcap_rank_proxy_cumslope_63d_3d_v150_signal(marketcap, closeadj):
    base = marketcap.rolling(252, min_periods=63).rank(pct=True)
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

