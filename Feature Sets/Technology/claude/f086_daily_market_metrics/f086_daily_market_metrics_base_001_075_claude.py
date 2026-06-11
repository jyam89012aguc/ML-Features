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


def _pct_change(s, n):
    return s.pct_change(periods=n)


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


# ===== folder domain primitives =====
def _f086_priceyoy(close):
    return close.pct_change(periods=252)


# 21d mean of price_yoy scaled by closeadj
def f086dmt_f086_daily_market_metrics_price_yoy_mean_21d_base_v001_signal(close, closeadj):
    base = _f086_priceyoy(close)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of price_yoy scaled by closeadj
def f086dmt_f086_daily_market_metrics_price_yoy_mean_63d_base_v002_signal(close, closeadj):
    base = _f086_priceyoy(close)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of price_yoy scaled by closeadj
def f086dmt_f086_daily_market_metrics_price_yoy_mean_126d_base_v003_signal(close, closeadj):
    base = _f086_priceyoy(close)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of price_yoy scaled by closeadj
def f086dmt_f086_daily_market_metrics_price_yoy_mean_252d_base_v004_signal(close, closeadj):
    base = _f086_priceyoy(close)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of price_yoy scaled by closeadj
def f086dmt_f086_daily_market_metrics_price_yoy_mean_504d_base_v005_signal(close, closeadj):
    base = _f086_priceyoy(close)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of ev_yoy scaled by closeadj
def f086dmt_f086_daily_market_metrics_ev_yoy_mean_21d_base_v006_signal(ev, closeadj):
    base = ev.pct_change(periods=252)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of ev_yoy scaled by closeadj
def f086dmt_f086_daily_market_metrics_ev_yoy_mean_63d_base_v007_signal(ev, closeadj):
    base = ev.pct_change(periods=252)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of ev_yoy scaled by closeadj
def f086dmt_f086_daily_market_metrics_ev_yoy_mean_126d_base_v008_signal(ev, closeadj):
    base = ev.pct_change(periods=252)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of ev_yoy scaled by closeadj
def f086dmt_f086_daily_market_metrics_ev_yoy_mean_252d_base_v009_signal(ev, closeadj):
    base = ev.pct_change(periods=252)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of ev_yoy scaled by closeadj
def f086dmt_f086_daily_market_metrics_ev_yoy_mean_504d_base_v010_signal(ev, closeadj):
    base = ev.pct_change(periods=252)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of pb_yoy_chg scaled by closeadj
def f086dmt_f086_daily_market_metrics_pb_yoy_chg_mean_21d_base_v011_signal(pb, closeadj):
    base = pb.diff(periods=252)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of pb_yoy_chg scaled by closeadj
def f086dmt_f086_daily_market_metrics_pb_yoy_chg_mean_63d_base_v012_signal(pb, closeadj):
    base = pb.diff(periods=252)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of pb_yoy_chg scaled by closeadj
def f086dmt_f086_daily_market_metrics_pb_yoy_chg_mean_126d_base_v013_signal(pb, closeadj):
    base = pb.diff(periods=252)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of pb_yoy_chg scaled by closeadj
def f086dmt_f086_daily_market_metrics_pb_yoy_chg_mean_252d_base_v014_signal(pb, closeadj):
    base = pb.diff(periods=252)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of pb_yoy_chg scaled by closeadj
def f086dmt_f086_daily_market_metrics_pb_yoy_chg_mean_504d_base_v015_signal(pb, closeadj):
    base = pb.diff(periods=252)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of pe_yoy_chg scaled by closeadj
def f086dmt_f086_daily_market_metrics_pe_yoy_chg_mean_21d_base_v016_signal(pe, closeadj):
    base = pe.diff(periods=252)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of pe_yoy_chg scaled by closeadj
def f086dmt_f086_daily_market_metrics_pe_yoy_chg_mean_63d_base_v017_signal(pe, closeadj):
    base = pe.diff(periods=252)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of pe_yoy_chg scaled by closeadj
def f086dmt_f086_daily_market_metrics_pe_yoy_chg_mean_126d_base_v018_signal(pe, closeadj):
    base = pe.diff(periods=252)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of pe_yoy_chg scaled by closeadj
def f086dmt_f086_daily_market_metrics_pe_yoy_chg_mean_252d_base_v019_signal(pe, closeadj):
    base = pe.diff(periods=252)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of pe_yoy_chg scaled by closeadj
def f086dmt_f086_daily_market_metrics_pe_yoy_chg_mean_504d_base_v020_signal(pe, closeadj):
    base = pe.diff(periods=252)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of ps_yoy_chg scaled by closeadj
def f086dmt_f086_daily_market_metrics_ps_yoy_chg_mean_21d_base_v021_signal(ps, closeadj):
    base = ps.diff(periods=252)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of ps_yoy_chg scaled by closeadj
def f086dmt_f086_daily_market_metrics_ps_yoy_chg_mean_63d_base_v022_signal(ps, closeadj):
    base = ps.diff(periods=252)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of ps_yoy_chg scaled by closeadj
def f086dmt_f086_daily_market_metrics_ps_yoy_chg_mean_126d_base_v023_signal(ps, closeadj):
    base = ps.diff(periods=252)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of ps_yoy_chg scaled by closeadj
def f086dmt_f086_daily_market_metrics_ps_yoy_chg_mean_252d_base_v024_signal(ps, closeadj):
    base = ps.diff(periods=252)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of ps_yoy_chg scaled by closeadj
def f086dmt_f086_daily_market_metrics_ps_yoy_chg_mean_504d_base_v025_signal(ps, closeadj):
    base = ps.diff(periods=252)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of mcap_rank_proxy scaled by closeadj
def f086dmt_f086_daily_market_metrics_mcap_rank_proxy_mean_21d_base_v026_signal(marketcap, closeadj):
    base = marketcap.rolling(252, min_periods=63).rank(pct=True)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of mcap_rank_proxy scaled by closeadj
def f086dmt_f086_daily_market_metrics_mcap_rank_proxy_mean_63d_base_v027_signal(marketcap, closeadj):
    base = marketcap.rolling(252, min_periods=63).rank(pct=True)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of mcap_rank_proxy scaled by closeadj
def f086dmt_f086_daily_market_metrics_mcap_rank_proxy_mean_126d_base_v028_signal(marketcap, closeadj):
    base = marketcap.rolling(252, min_periods=63).rank(pct=True)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of mcap_rank_proxy scaled by closeadj
def f086dmt_f086_daily_market_metrics_mcap_rank_proxy_mean_252d_base_v029_signal(marketcap, closeadj):
    base = marketcap.rolling(252, min_periods=63).rank(pct=True)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of mcap_rank_proxy scaled by closeadj
def f086dmt_f086_daily_market_metrics_mcap_rank_proxy_mean_504d_base_v030_signal(marketcap, closeadj):
    base = marketcap.rolling(252, min_periods=63).rank(pct=True)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of daily_mult_dispersion scaled by closeadj
def f086dmt_f086_daily_market_metrics_daily_mult_dispersion_mean_21d_base_v031_signal(pe, ps, pb, closeadj):
    base = (pe + ps + pb) / 3
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of daily_mult_dispersion scaled by closeadj
def f086dmt_f086_daily_market_metrics_daily_mult_dispersion_mean_63d_base_v032_signal(pe, ps, pb, closeadj):
    base = (pe + ps + pb) / 3
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of daily_mult_dispersion scaled by closeadj
def f086dmt_f086_daily_market_metrics_daily_mult_dispersion_mean_126d_base_v033_signal(pe, ps, pb, closeadj):
    base = (pe + ps + pb) / 3
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of daily_mult_dispersion scaled by closeadj
def f086dmt_f086_daily_market_metrics_daily_mult_dispersion_mean_252d_base_v034_signal(pe, ps, pb, closeadj):
    base = (pe + ps + pb) / 3
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of daily_mult_dispersion scaled by closeadj
def f086dmt_f086_daily_market_metrics_daily_mult_dispersion_mean_504d_base_v035_signal(pe, ps, pb, closeadj):
    base = (pe + ps + pb) / 3
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of price_yoy
def f086dmt_f086_daily_market_metrics_price_yoy_median_63d_base_v036_signal(close, closeadj):
    base = _f086_priceyoy(close)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of price_yoy
def f086dmt_f086_daily_market_metrics_price_yoy_median_252d_base_v037_signal(close, closeadj):
    base = _f086_priceyoy(close)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of price_yoy
def f086dmt_f086_daily_market_metrics_price_yoy_median_504d_base_v038_signal(close, closeadj):
    base = _f086_priceyoy(close)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of ev_yoy
def f086dmt_f086_daily_market_metrics_ev_yoy_median_63d_base_v039_signal(ev, closeadj):
    base = ev.pct_change(periods=252)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of ev_yoy
def f086dmt_f086_daily_market_metrics_ev_yoy_median_252d_base_v040_signal(ev, closeadj):
    base = ev.pct_change(periods=252)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of ev_yoy
def f086dmt_f086_daily_market_metrics_ev_yoy_median_504d_base_v041_signal(ev, closeadj):
    base = ev.pct_change(periods=252)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of pb_yoy_chg
def f086dmt_f086_daily_market_metrics_pb_yoy_chg_median_63d_base_v042_signal(pb, closeadj):
    base = pb.diff(periods=252)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of pb_yoy_chg
def f086dmt_f086_daily_market_metrics_pb_yoy_chg_median_252d_base_v043_signal(pb, closeadj):
    base = pb.diff(periods=252)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of pb_yoy_chg
def f086dmt_f086_daily_market_metrics_pb_yoy_chg_median_504d_base_v044_signal(pb, closeadj):
    base = pb.diff(periods=252)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of pe_yoy_chg
def f086dmt_f086_daily_market_metrics_pe_yoy_chg_median_63d_base_v045_signal(pe, closeadj):
    base = pe.diff(periods=252)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of pe_yoy_chg
def f086dmt_f086_daily_market_metrics_pe_yoy_chg_median_252d_base_v046_signal(pe, closeadj):
    base = pe.diff(periods=252)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of pe_yoy_chg
def f086dmt_f086_daily_market_metrics_pe_yoy_chg_median_504d_base_v047_signal(pe, closeadj):
    base = pe.diff(periods=252)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of ps_yoy_chg
def f086dmt_f086_daily_market_metrics_ps_yoy_chg_median_63d_base_v048_signal(ps, closeadj):
    base = ps.diff(periods=252)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of ps_yoy_chg
def f086dmt_f086_daily_market_metrics_ps_yoy_chg_median_252d_base_v049_signal(ps, closeadj):
    base = ps.diff(periods=252)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of ps_yoy_chg
def f086dmt_f086_daily_market_metrics_ps_yoy_chg_median_504d_base_v050_signal(ps, closeadj):
    base = ps.diff(periods=252)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of mcap_rank_proxy
def f086dmt_f086_daily_market_metrics_mcap_rank_proxy_median_63d_base_v051_signal(marketcap, closeadj):
    base = marketcap.rolling(252, min_periods=63).rank(pct=True)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of mcap_rank_proxy
def f086dmt_f086_daily_market_metrics_mcap_rank_proxy_median_252d_base_v052_signal(marketcap, closeadj):
    base = marketcap.rolling(252, min_periods=63).rank(pct=True)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of mcap_rank_proxy
def f086dmt_f086_daily_market_metrics_mcap_rank_proxy_median_504d_base_v053_signal(marketcap, closeadj):
    base = marketcap.rolling(252, min_periods=63).rank(pct=True)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of daily_mult_dispersion
def f086dmt_f086_daily_market_metrics_daily_mult_dispersion_median_63d_base_v054_signal(pe, ps, pb, closeadj):
    base = (pe + ps + pb) / 3
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of daily_mult_dispersion
def f086dmt_f086_daily_market_metrics_daily_mult_dispersion_median_252d_base_v055_signal(pe, ps, pb, closeadj):
    base = (pe + ps + pb) / 3
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of daily_mult_dispersion
def f086dmt_f086_daily_market_metrics_daily_mult_dispersion_median_504d_base_v056_signal(pe, ps, pb, closeadj):
    base = (pe + ps + pb) / 3
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of price_yoy
def f086dmt_f086_daily_market_metrics_price_yoy_rmax_252d_base_v057_signal(close, closeadj):
    base = _f086_priceyoy(close)
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of price_yoy
def f086dmt_f086_daily_market_metrics_price_yoy_rmax_504d_base_v058_signal(close, closeadj):
    base = _f086_priceyoy(close)
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of ev_yoy
def f086dmt_f086_daily_market_metrics_ev_yoy_rmax_252d_base_v059_signal(ev, closeadj):
    base = ev.pct_change(periods=252)
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of ev_yoy
def f086dmt_f086_daily_market_metrics_ev_yoy_rmax_504d_base_v060_signal(ev, closeadj):
    base = ev.pct_change(periods=252)
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of pb_yoy_chg
def f086dmt_f086_daily_market_metrics_pb_yoy_chg_rmax_252d_base_v061_signal(pb, closeadj):
    base = pb.diff(periods=252)
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of pb_yoy_chg
def f086dmt_f086_daily_market_metrics_pb_yoy_chg_rmax_504d_base_v062_signal(pb, closeadj):
    base = pb.diff(periods=252)
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of pe_yoy_chg
def f086dmt_f086_daily_market_metrics_pe_yoy_chg_rmax_252d_base_v063_signal(pe, closeadj):
    base = pe.diff(periods=252)
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of pe_yoy_chg
def f086dmt_f086_daily_market_metrics_pe_yoy_chg_rmax_504d_base_v064_signal(pe, closeadj):
    base = pe.diff(periods=252)
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of ps_yoy_chg
def f086dmt_f086_daily_market_metrics_ps_yoy_chg_rmax_252d_base_v065_signal(ps, closeadj):
    base = ps.diff(periods=252)
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of ps_yoy_chg
def f086dmt_f086_daily_market_metrics_ps_yoy_chg_rmax_504d_base_v066_signal(ps, closeadj):
    base = ps.diff(periods=252)
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of mcap_rank_proxy
def f086dmt_f086_daily_market_metrics_mcap_rank_proxy_rmax_252d_base_v067_signal(marketcap, closeadj):
    base = marketcap.rolling(252, min_periods=63).rank(pct=True)
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of mcap_rank_proxy
def f086dmt_f086_daily_market_metrics_mcap_rank_proxy_rmax_504d_base_v068_signal(marketcap, closeadj):
    base = marketcap.rolling(252, min_periods=63).rank(pct=True)
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of daily_mult_dispersion
def f086dmt_f086_daily_market_metrics_daily_mult_dispersion_rmax_252d_base_v069_signal(pe, ps, pb, closeadj):
    base = (pe + ps + pb) / 3
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of daily_mult_dispersion
def f086dmt_f086_daily_market_metrics_daily_mult_dispersion_rmax_504d_base_v070_signal(pe, ps, pb, closeadj):
    base = (pe + ps + pb) / 3
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling min of price_yoy
def f086dmt_f086_daily_market_metrics_price_yoy_rmin_252d_base_v071_signal(close, closeadj):
    base = _f086_priceyoy(close)
    result = base.rolling(252, min_periods=max(1, 252//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling min of price_yoy
def f086dmt_f086_daily_market_metrics_price_yoy_rmin_504d_base_v072_signal(close, closeadj):
    base = _f086_priceyoy(close)
    result = base.rolling(504, min_periods=max(1, 504//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling min of ev_yoy
def f086dmt_f086_daily_market_metrics_ev_yoy_rmin_252d_base_v073_signal(ev, closeadj):
    base = ev.pct_change(periods=252)
    result = base.rolling(252, min_periods=max(1, 252//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling min of ev_yoy
def f086dmt_f086_daily_market_metrics_ev_yoy_rmin_504d_base_v074_signal(ev, closeadj):
    base = ev.pct_change(periods=252)
    result = base.rolling(504, min_periods=max(1, 504//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling min of pb_yoy_chg
def f086dmt_f086_daily_market_metrics_pb_yoy_chg_rmin_252d_base_v075_signal(pb, closeadj):
    base = pb.diff(periods=252)
    result = base.rolling(252, min_periods=max(1, 252//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

