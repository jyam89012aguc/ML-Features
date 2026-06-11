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


# 63d z-score of price_yoy
def f086dmt_f086_daily_market_metrics_price_yoy_z_63d_base_v076_signal(close, closeadj):
    base = _f086_priceyoy(close)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of price_yoy
def f086dmt_f086_daily_market_metrics_price_yoy_z_126d_base_v077_signal(close, closeadj):
    base = _f086_priceyoy(close)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of price_yoy
def f086dmt_f086_daily_market_metrics_price_yoy_z_252d_base_v078_signal(close, closeadj):
    base = _f086_priceyoy(close)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of price_yoy
def f086dmt_f086_daily_market_metrics_price_yoy_z_504d_base_v079_signal(close, closeadj):
    base = _f086_priceyoy(close)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of ev_yoy
def f086dmt_f086_daily_market_metrics_ev_yoy_z_63d_base_v080_signal(ev, closeadj):
    base = ev.pct_change(periods=252)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of ev_yoy
def f086dmt_f086_daily_market_metrics_ev_yoy_z_126d_base_v081_signal(ev, closeadj):
    base = ev.pct_change(periods=252)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of ev_yoy
def f086dmt_f086_daily_market_metrics_ev_yoy_z_252d_base_v082_signal(ev, closeadj):
    base = ev.pct_change(periods=252)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of ev_yoy
def f086dmt_f086_daily_market_metrics_ev_yoy_z_504d_base_v083_signal(ev, closeadj):
    base = ev.pct_change(periods=252)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of pb_yoy_chg
def f086dmt_f086_daily_market_metrics_pb_yoy_chg_z_63d_base_v084_signal(pb, closeadj):
    base = pb.diff(periods=252)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of pb_yoy_chg
def f086dmt_f086_daily_market_metrics_pb_yoy_chg_z_126d_base_v085_signal(pb, closeadj):
    base = pb.diff(periods=252)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of pb_yoy_chg
def f086dmt_f086_daily_market_metrics_pb_yoy_chg_z_252d_base_v086_signal(pb, closeadj):
    base = pb.diff(periods=252)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of pb_yoy_chg
def f086dmt_f086_daily_market_metrics_pb_yoy_chg_z_504d_base_v087_signal(pb, closeadj):
    base = pb.diff(periods=252)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of pe_yoy_chg
def f086dmt_f086_daily_market_metrics_pe_yoy_chg_z_63d_base_v088_signal(pe, closeadj):
    base = pe.diff(periods=252)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of pe_yoy_chg
def f086dmt_f086_daily_market_metrics_pe_yoy_chg_z_126d_base_v089_signal(pe, closeadj):
    base = pe.diff(periods=252)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of pe_yoy_chg
def f086dmt_f086_daily_market_metrics_pe_yoy_chg_z_252d_base_v090_signal(pe, closeadj):
    base = pe.diff(periods=252)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of pe_yoy_chg
def f086dmt_f086_daily_market_metrics_pe_yoy_chg_z_504d_base_v091_signal(pe, closeadj):
    base = pe.diff(periods=252)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of ps_yoy_chg
def f086dmt_f086_daily_market_metrics_ps_yoy_chg_z_63d_base_v092_signal(ps, closeadj):
    base = ps.diff(periods=252)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of ps_yoy_chg
def f086dmt_f086_daily_market_metrics_ps_yoy_chg_z_126d_base_v093_signal(ps, closeadj):
    base = ps.diff(periods=252)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of ps_yoy_chg
def f086dmt_f086_daily_market_metrics_ps_yoy_chg_z_252d_base_v094_signal(ps, closeadj):
    base = ps.diff(periods=252)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of ps_yoy_chg
def f086dmt_f086_daily_market_metrics_ps_yoy_chg_z_504d_base_v095_signal(ps, closeadj):
    base = ps.diff(periods=252)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of mcap_rank_proxy
def f086dmt_f086_daily_market_metrics_mcap_rank_proxy_z_63d_base_v096_signal(marketcap, closeadj):
    base = marketcap.rolling(252, min_periods=63).rank(pct=True)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of mcap_rank_proxy
def f086dmt_f086_daily_market_metrics_mcap_rank_proxy_z_126d_base_v097_signal(marketcap, closeadj):
    base = marketcap.rolling(252, min_periods=63).rank(pct=True)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of mcap_rank_proxy
def f086dmt_f086_daily_market_metrics_mcap_rank_proxy_z_252d_base_v098_signal(marketcap, closeadj):
    base = marketcap.rolling(252, min_periods=63).rank(pct=True)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of mcap_rank_proxy
def f086dmt_f086_daily_market_metrics_mcap_rank_proxy_z_504d_base_v099_signal(marketcap, closeadj):
    base = marketcap.rolling(252, min_periods=63).rank(pct=True)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of daily_mult_dispersion
def f086dmt_f086_daily_market_metrics_daily_mult_dispersion_z_63d_base_v100_signal(pe, ps, pb, closeadj):
    base = (pe + ps + pb) / 3
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of daily_mult_dispersion
def f086dmt_f086_daily_market_metrics_daily_mult_dispersion_z_126d_base_v101_signal(pe, ps, pb, closeadj):
    base = (pe + ps + pb) / 3
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of daily_mult_dispersion
def f086dmt_f086_daily_market_metrics_daily_mult_dispersion_z_252d_base_v102_signal(pe, ps, pb, closeadj):
    base = (pe + ps + pb) / 3
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of daily_mult_dispersion
def f086dmt_f086_daily_market_metrics_daily_mult_dispersion_z_504d_base_v103_signal(pe, ps, pb, closeadj):
    base = (pe + ps + pb) / 3
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of price_yoy
def f086dmt_f086_daily_market_metrics_price_yoy_distmax_252d_base_v104_signal(close, closeadj):
    base = _f086_priceyoy(close)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of price_yoy
def f086dmt_f086_daily_market_metrics_price_yoy_distmax_504d_base_v105_signal(close, closeadj):
    base = _f086_priceyoy(close)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of ev_yoy
def f086dmt_f086_daily_market_metrics_ev_yoy_distmax_252d_base_v106_signal(ev, closeadj):
    base = ev.pct_change(periods=252)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of ev_yoy
def f086dmt_f086_daily_market_metrics_ev_yoy_distmax_504d_base_v107_signal(ev, closeadj):
    base = ev.pct_change(periods=252)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of pb_yoy_chg
def f086dmt_f086_daily_market_metrics_pb_yoy_chg_distmax_252d_base_v108_signal(pb, closeadj):
    base = pb.diff(periods=252)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of pb_yoy_chg
def f086dmt_f086_daily_market_metrics_pb_yoy_chg_distmax_504d_base_v109_signal(pb, closeadj):
    base = pb.diff(periods=252)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of pe_yoy_chg
def f086dmt_f086_daily_market_metrics_pe_yoy_chg_distmax_252d_base_v110_signal(pe, closeadj):
    base = pe.diff(periods=252)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of pe_yoy_chg
def f086dmt_f086_daily_market_metrics_pe_yoy_chg_distmax_504d_base_v111_signal(pe, closeadj):
    base = pe.diff(periods=252)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of ps_yoy_chg
def f086dmt_f086_daily_market_metrics_ps_yoy_chg_distmax_252d_base_v112_signal(ps, closeadj):
    base = ps.diff(periods=252)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of ps_yoy_chg
def f086dmt_f086_daily_market_metrics_ps_yoy_chg_distmax_504d_base_v113_signal(ps, closeadj):
    base = ps.diff(periods=252)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of mcap_rank_proxy
def f086dmt_f086_daily_market_metrics_mcap_rank_proxy_distmax_252d_base_v114_signal(marketcap, closeadj):
    base = marketcap.rolling(252, min_periods=63).rank(pct=True)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of mcap_rank_proxy
def f086dmt_f086_daily_market_metrics_mcap_rank_proxy_distmax_504d_base_v115_signal(marketcap, closeadj):
    base = marketcap.rolling(252, min_periods=63).rank(pct=True)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of daily_mult_dispersion
def f086dmt_f086_daily_market_metrics_daily_mult_dispersion_distmax_252d_base_v116_signal(pe, ps, pb, closeadj):
    base = (pe + ps + pb) / 3
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of daily_mult_dispersion
def f086dmt_f086_daily_market_metrics_daily_mult_dispersion_distmax_504d_base_v117_signal(pe, ps, pb, closeadj):
    base = (pe + ps + pb) / 3
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of price_yoy
def f086dmt_f086_daily_market_metrics_price_yoy_distmed_126d_base_v118_signal(close, closeadj):
    base = _f086_priceyoy(close)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of price_yoy
def f086dmt_f086_daily_market_metrics_price_yoy_distmed_252d_base_v119_signal(close, closeadj):
    base = _f086_priceyoy(close)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of price_yoy
def f086dmt_f086_daily_market_metrics_price_yoy_distmed_504d_base_v120_signal(close, closeadj):
    base = _f086_priceyoy(close)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of ev_yoy
def f086dmt_f086_daily_market_metrics_ev_yoy_distmed_126d_base_v121_signal(ev, closeadj):
    base = ev.pct_change(periods=252)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of ev_yoy
def f086dmt_f086_daily_market_metrics_ev_yoy_distmed_252d_base_v122_signal(ev, closeadj):
    base = ev.pct_change(periods=252)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of ev_yoy
def f086dmt_f086_daily_market_metrics_ev_yoy_distmed_504d_base_v123_signal(ev, closeadj):
    base = ev.pct_change(periods=252)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of pb_yoy_chg
def f086dmt_f086_daily_market_metrics_pb_yoy_chg_distmed_126d_base_v124_signal(pb, closeadj):
    base = pb.diff(periods=252)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of pb_yoy_chg
def f086dmt_f086_daily_market_metrics_pb_yoy_chg_distmed_252d_base_v125_signal(pb, closeadj):
    base = pb.diff(periods=252)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of pb_yoy_chg
def f086dmt_f086_daily_market_metrics_pb_yoy_chg_distmed_504d_base_v126_signal(pb, closeadj):
    base = pb.diff(periods=252)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of pe_yoy_chg
def f086dmt_f086_daily_market_metrics_pe_yoy_chg_distmed_126d_base_v127_signal(pe, closeadj):
    base = pe.diff(periods=252)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of pe_yoy_chg
def f086dmt_f086_daily_market_metrics_pe_yoy_chg_distmed_252d_base_v128_signal(pe, closeadj):
    base = pe.diff(periods=252)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of pe_yoy_chg
def f086dmt_f086_daily_market_metrics_pe_yoy_chg_distmed_504d_base_v129_signal(pe, closeadj):
    base = pe.diff(periods=252)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of ps_yoy_chg
def f086dmt_f086_daily_market_metrics_ps_yoy_chg_distmed_126d_base_v130_signal(ps, closeadj):
    base = ps.diff(periods=252)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of ps_yoy_chg
def f086dmt_f086_daily_market_metrics_ps_yoy_chg_distmed_252d_base_v131_signal(ps, closeadj):
    base = ps.diff(periods=252)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of ps_yoy_chg
def f086dmt_f086_daily_market_metrics_ps_yoy_chg_distmed_504d_base_v132_signal(ps, closeadj):
    base = ps.diff(periods=252)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of mcap_rank_proxy
def f086dmt_f086_daily_market_metrics_mcap_rank_proxy_distmed_126d_base_v133_signal(marketcap, closeadj):
    base = marketcap.rolling(252, min_periods=63).rank(pct=True)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of mcap_rank_proxy
def f086dmt_f086_daily_market_metrics_mcap_rank_proxy_distmed_252d_base_v134_signal(marketcap, closeadj):
    base = marketcap.rolling(252, min_periods=63).rank(pct=True)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of mcap_rank_proxy
def f086dmt_f086_daily_market_metrics_mcap_rank_proxy_distmed_504d_base_v135_signal(marketcap, closeadj):
    base = marketcap.rolling(252, min_periods=63).rank(pct=True)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of daily_mult_dispersion
def f086dmt_f086_daily_market_metrics_daily_mult_dispersion_distmed_126d_base_v136_signal(pe, ps, pb, closeadj):
    base = (pe + ps + pb) / 3
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of daily_mult_dispersion
def f086dmt_f086_daily_market_metrics_daily_mult_dispersion_distmed_252d_base_v137_signal(pe, ps, pb, closeadj):
    base = (pe + ps + pb) / 3
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of daily_mult_dispersion
def f086dmt_f086_daily_market_metrics_daily_mult_dispersion_distmed_504d_base_v138_signal(pe, ps, pb, closeadj):
    base = (pe + ps + pb) / 3
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in price_yoy
def f086dmt_f086_daily_market_metrics_price_yoy_chg_63d_base_v139_signal(close, closeadj):
    base = _f086_priceyoy(close)
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in price_yoy
def f086dmt_f086_daily_market_metrics_price_yoy_chg_252d_base_v140_signal(close, closeadj):
    base = _f086_priceyoy(close)
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in ev_yoy
def f086dmt_f086_daily_market_metrics_ev_yoy_chg_63d_base_v141_signal(ev, closeadj):
    base = ev.pct_change(periods=252)
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in ev_yoy
def f086dmt_f086_daily_market_metrics_ev_yoy_chg_252d_base_v142_signal(ev, closeadj):
    base = ev.pct_change(periods=252)
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in pb_yoy_chg
def f086dmt_f086_daily_market_metrics_pb_yoy_chg_chg_63d_base_v143_signal(pb, closeadj):
    base = pb.diff(periods=252)
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in pb_yoy_chg
def f086dmt_f086_daily_market_metrics_pb_yoy_chg_chg_252d_base_v144_signal(pb, closeadj):
    base = pb.diff(periods=252)
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in pe_yoy_chg
def f086dmt_f086_daily_market_metrics_pe_yoy_chg_chg_63d_base_v145_signal(pe, closeadj):
    base = pe.diff(periods=252)
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in pe_yoy_chg
def f086dmt_f086_daily_market_metrics_pe_yoy_chg_chg_252d_base_v146_signal(pe, closeadj):
    base = pe.diff(periods=252)
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in ps_yoy_chg
def f086dmt_f086_daily_market_metrics_ps_yoy_chg_chg_63d_base_v147_signal(ps, closeadj):
    base = ps.diff(periods=252)
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in ps_yoy_chg
def f086dmt_f086_daily_market_metrics_ps_yoy_chg_chg_252d_base_v148_signal(ps, closeadj):
    base = ps.diff(periods=252)
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in mcap_rank_proxy
def f086dmt_f086_daily_market_metrics_mcap_rank_proxy_chg_63d_base_v149_signal(marketcap, closeadj):
    base = marketcap.rolling(252, min_periods=63).rank(pct=True)
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in mcap_rank_proxy
def f086dmt_f086_daily_market_metrics_mcap_rank_proxy_chg_252d_base_v150_signal(marketcap, closeadj):
    base = marketcap.rolling(252, min_periods=63).rank(pct=True)
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

