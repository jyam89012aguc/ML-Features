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
def _f17_revenue_per_asset(revenue, assets):
    return revenue / assets.replace(0, np.nan)


def _f17_lng_intensity(revenue, ppnenet, w):
    r = revenue.rolling(w, min_periods=max(1, w // 2)).mean()
    p = ppnenet.rolling(w, min_periods=max(1, w // 2)).mean().replace(0, np.nan)
    return r / p


def _f17_pricing_signal(revenue, assets, w):
    rpa = revenue / assets.replace(0, np.nan)
    m = rpa.rolling(w, min_periods=max(1, w // 2)).mean()
    sd = rpa.rolling(w, min_periods=max(1, w // 2)).std()
    return (rpa - m) / sd.replace(0, np.nan)

def f17lvp_f17_lng_volume_pricing_rpamean_5d189dclz63_base_v076_signal(revenue, assets, closeadj):
    result = _mean(_f17_revenue_per_asset(revenue, assets), 189) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f17lvp_f17_lng_volume_pricing_rpamean_5d189dclret21_base_v077_signal(revenue, assets, closeadj):
    result = _mean(_f17_revenue_per_asset(revenue, assets), 189) * closeadj.pct_change(21)
    return result.replace([np.inf, -np.inf], np.nan)


def f17lvp_f17_lng_volume_pricing_rpamean_5d189dclret63_base_v078_signal(revenue, assets, closeadj):
    result = _mean(_f17_revenue_per_asset(revenue, assets), 189) * closeadj.pct_change(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f17lvp_f17_lng_volume_pricing_rpamean_5d189dclsqr_base_v079_signal(revenue, assets, closeadj):
    result = _mean(_f17_revenue_per_asset(revenue, assets), 189) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17lvp_f17_lng_volume_pricing_rpamean_5d189dclema21_base_v080_signal(revenue, assets, closeadj):
    result = _mean(_f17_revenue_per_asset(revenue, assets), 189) * closeadj.ewm(span=21, min_periods=10).mean()
    return result.replace([np.inf, -np.inf], np.nan)


def f17lvp_f17_lng_volume_pricing_rpamean_5d252dcl_base_v081_signal(revenue, assets, closeadj):
    result = _mean(_f17_revenue_per_asset(revenue, assets), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17lvp_f17_lng_volume_pricing_rpamean_5d252dcl5_base_v082_signal(revenue, assets, closeadj):
    result = _mean(_f17_revenue_per_asset(revenue, assets), 252) * _mean(closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f17lvp_f17_lng_volume_pricing_rpamean_5d252dcl21_base_v083_signal(revenue, assets, closeadj):
    result = _mean(_f17_revenue_per_asset(revenue, assets), 252) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f17lvp_f17_lng_volume_pricing_rpamean_5d252dcl63_base_v084_signal(revenue, assets, closeadj):
    result = _mean(_f17_revenue_per_asset(revenue, assets), 252) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f17lvp_f17_lng_volume_pricing_rpamean_5d252dclz21_base_v085_signal(revenue, assets, closeadj):
    result = _mean(_f17_revenue_per_asset(revenue, assets), 252) * _z(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f17lvp_f17_lng_volume_pricing_rpamean_5d252dclz63_base_v086_signal(revenue, assets, closeadj):
    result = _mean(_f17_revenue_per_asset(revenue, assets), 252) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f17lvp_f17_lng_volume_pricing_rpamean_5d252dclret21_base_v087_signal(revenue, assets, closeadj):
    result = _mean(_f17_revenue_per_asset(revenue, assets), 252) * closeadj.pct_change(21)
    return result.replace([np.inf, -np.inf], np.nan)


def f17lvp_f17_lng_volume_pricing_rpamean_5d252dclret63_base_v088_signal(revenue, assets, closeadj):
    result = _mean(_f17_revenue_per_asset(revenue, assets), 252) * closeadj.pct_change(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f17lvp_f17_lng_volume_pricing_rpamean_5d252dclsqr_base_v089_signal(revenue, assets, closeadj):
    result = _mean(_f17_revenue_per_asset(revenue, assets), 252) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17lvp_f17_lng_volume_pricing_rpamean_5d252dclema21_base_v090_signal(revenue, assets, closeadj):
    result = _mean(_f17_revenue_per_asset(revenue, assets), 252) * closeadj.ewm(span=21, min_periods=10).mean()
    return result.replace([np.inf, -np.inf], np.nan)


def f17lvp_f17_lng_volume_pricing_rpamean_5d378dcl_base_v091_signal(revenue, assets, closeadj):
    result = _mean(_f17_revenue_per_asset(revenue, assets), 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17lvp_f17_lng_volume_pricing_rpamean_5d378dcl5_base_v092_signal(revenue, assets, closeadj):
    result = _mean(_f17_revenue_per_asset(revenue, assets), 378) * _mean(closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f17lvp_f17_lng_volume_pricing_rpamean_5d378dcl21_base_v093_signal(revenue, assets, closeadj):
    result = _mean(_f17_revenue_per_asset(revenue, assets), 378) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f17lvp_f17_lng_volume_pricing_rpamean_5d378dcl63_base_v094_signal(revenue, assets, closeadj):
    result = _mean(_f17_revenue_per_asset(revenue, assets), 378) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f17lvp_f17_lng_volume_pricing_rpamean_5d378dclz21_base_v095_signal(revenue, assets, closeadj):
    result = _mean(_f17_revenue_per_asset(revenue, assets), 378) * _z(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f17lvp_f17_lng_volume_pricing_rpamean_5d378dclz63_base_v096_signal(revenue, assets, closeadj):
    result = _mean(_f17_revenue_per_asset(revenue, assets), 378) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f17lvp_f17_lng_volume_pricing_rpamean_5d378dclret21_base_v097_signal(revenue, assets, closeadj):
    result = _mean(_f17_revenue_per_asset(revenue, assets), 378) * closeadj.pct_change(21)
    return result.replace([np.inf, -np.inf], np.nan)


def f17lvp_f17_lng_volume_pricing_rpamean_5d378dclret63_base_v098_signal(revenue, assets, closeadj):
    result = _mean(_f17_revenue_per_asset(revenue, assets), 378) * closeadj.pct_change(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f17lvp_f17_lng_volume_pricing_rpamean_5d378dclsqr_base_v099_signal(revenue, assets, closeadj):
    result = _mean(_f17_revenue_per_asset(revenue, assets), 378) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17lvp_f17_lng_volume_pricing_rpamean_5d378dclema21_base_v100_signal(revenue, assets, closeadj):
    result = _mean(_f17_revenue_per_asset(revenue, assets), 378) * closeadj.ewm(span=21, min_periods=10).mean()
    return result.replace([np.inf, -np.inf], np.nan)


def f17lvp_f17_lng_volume_pricing_rpamean_5d504dcl_base_v101_signal(revenue, assets, closeadj):
    result = _mean(_f17_revenue_per_asset(revenue, assets), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17lvp_f17_lng_volume_pricing_rpamean_5d504dcl5_base_v102_signal(revenue, assets, closeadj):
    result = _mean(_f17_revenue_per_asset(revenue, assets), 504) * _mean(closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f17lvp_f17_lng_volume_pricing_rpamean_5d504dcl21_base_v103_signal(revenue, assets, closeadj):
    result = _mean(_f17_revenue_per_asset(revenue, assets), 504) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f17lvp_f17_lng_volume_pricing_rpamean_5d504dcl63_base_v104_signal(revenue, assets, closeadj):
    result = _mean(_f17_revenue_per_asset(revenue, assets), 504) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f17lvp_f17_lng_volume_pricing_rpamean_5d504dclz21_base_v105_signal(revenue, assets, closeadj):
    result = _mean(_f17_revenue_per_asset(revenue, assets), 504) * _z(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f17lvp_f17_lng_volume_pricing_rpamean_5d504dclz63_base_v106_signal(revenue, assets, closeadj):
    result = _mean(_f17_revenue_per_asset(revenue, assets), 504) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f17lvp_f17_lng_volume_pricing_rpamean_5d504dclret21_base_v107_signal(revenue, assets, closeadj):
    result = _mean(_f17_revenue_per_asset(revenue, assets), 504) * closeadj.pct_change(21)
    return result.replace([np.inf, -np.inf], np.nan)


def f17lvp_f17_lng_volume_pricing_rpamean_5d504dclret63_base_v108_signal(revenue, assets, closeadj):
    result = _mean(_f17_revenue_per_asset(revenue, assets), 504) * closeadj.pct_change(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f17lvp_f17_lng_volume_pricing_rpamean_5d504dclsqr_base_v109_signal(revenue, assets, closeadj):
    result = _mean(_f17_revenue_per_asset(revenue, assets), 504) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17lvp_f17_lng_volume_pricing_rpamean_5d504dclema21_base_v110_signal(revenue, assets, closeadj):
    result = _mean(_f17_revenue_per_asset(revenue, assets), 504) * closeadj.ewm(span=21, min_periods=10).mean()
    return result.replace([np.inf, -np.inf], np.nan)


def f17lvp_f17_lng_volume_pricing_rpastd_5d5dcl_base_v111_signal(revenue, assets, closeadj):
    result = _std(_f17_revenue_per_asset(revenue, assets), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17lvp_f17_lng_volume_pricing_rpastd_5d5dcl5_base_v112_signal(revenue, assets, closeadj):
    result = _std(_f17_revenue_per_asset(revenue, assets), 5) * _mean(closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f17lvp_f17_lng_volume_pricing_rpastd_5d5dcl21_base_v113_signal(revenue, assets, closeadj):
    result = _std(_f17_revenue_per_asset(revenue, assets), 5) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f17lvp_f17_lng_volume_pricing_rpastd_5d5dcl63_base_v114_signal(revenue, assets, closeadj):
    result = _std(_f17_revenue_per_asset(revenue, assets), 5) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f17lvp_f17_lng_volume_pricing_rpastd_5d5dclz21_base_v115_signal(revenue, assets, closeadj):
    result = _std(_f17_revenue_per_asset(revenue, assets), 5) * _z(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f17lvp_f17_lng_volume_pricing_rpastd_5d5dclz63_base_v116_signal(revenue, assets, closeadj):
    result = _std(_f17_revenue_per_asset(revenue, assets), 5) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f17lvp_f17_lng_volume_pricing_rpastd_5d5dclret21_base_v117_signal(revenue, assets, closeadj):
    result = _std(_f17_revenue_per_asset(revenue, assets), 5) * closeadj.pct_change(21)
    return result.replace([np.inf, -np.inf], np.nan)


def f17lvp_f17_lng_volume_pricing_rpastd_5d5dclret63_base_v118_signal(revenue, assets, closeadj):
    result = _std(_f17_revenue_per_asset(revenue, assets), 5) * closeadj.pct_change(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f17lvp_f17_lng_volume_pricing_rpastd_5d5dclsqr_base_v119_signal(revenue, assets, closeadj):
    result = _std(_f17_revenue_per_asset(revenue, assets), 5) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17lvp_f17_lng_volume_pricing_rpastd_5d5dclema21_base_v120_signal(revenue, assets, closeadj):
    result = _std(_f17_revenue_per_asset(revenue, assets), 5) * closeadj.ewm(span=21, min_periods=10).mean()
    return result.replace([np.inf, -np.inf], np.nan)


def f17lvp_f17_lng_volume_pricing_rpastd_5d10dcl_base_v121_signal(revenue, assets, closeadj):
    result = _std(_f17_revenue_per_asset(revenue, assets), 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17lvp_f17_lng_volume_pricing_rpastd_5d10dcl5_base_v122_signal(revenue, assets, closeadj):
    result = _std(_f17_revenue_per_asset(revenue, assets), 10) * _mean(closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f17lvp_f17_lng_volume_pricing_rpastd_5d10dcl21_base_v123_signal(revenue, assets, closeadj):
    result = _std(_f17_revenue_per_asset(revenue, assets), 10) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f17lvp_f17_lng_volume_pricing_rpastd_5d10dcl63_base_v124_signal(revenue, assets, closeadj):
    result = _std(_f17_revenue_per_asset(revenue, assets), 10) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f17lvp_f17_lng_volume_pricing_rpastd_5d10dclz21_base_v125_signal(revenue, assets, closeadj):
    result = _std(_f17_revenue_per_asset(revenue, assets), 10) * _z(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f17lvp_f17_lng_volume_pricing_rpastd_5d10dclz63_base_v126_signal(revenue, assets, closeadj):
    result = _std(_f17_revenue_per_asset(revenue, assets), 10) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f17lvp_f17_lng_volume_pricing_rpastd_5d10dclret21_base_v127_signal(revenue, assets, closeadj):
    result = _std(_f17_revenue_per_asset(revenue, assets), 10) * closeadj.pct_change(21)
    return result.replace([np.inf, -np.inf], np.nan)


def f17lvp_f17_lng_volume_pricing_rpastd_5d10dclret63_base_v128_signal(revenue, assets, closeadj):
    result = _std(_f17_revenue_per_asset(revenue, assets), 10) * closeadj.pct_change(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f17lvp_f17_lng_volume_pricing_rpastd_5d10dclsqr_base_v129_signal(revenue, assets, closeadj):
    result = _std(_f17_revenue_per_asset(revenue, assets), 10) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17lvp_f17_lng_volume_pricing_rpastd_5d10dclema21_base_v130_signal(revenue, assets, closeadj):
    result = _std(_f17_revenue_per_asset(revenue, assets), 10) * closeadj.ewm(span=21, min_periods=10).mean()
    return result.replace([np.inf, -np.inf], np.nan)


def f17lvp_f17_lng_volume_pricing_rpastd_5d21dcl_base_v131_signal(revenue, assets, closeadj):
    result = _std(_f17_revenue_per_asset(revenue, assets), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17lvp_f17_lng_volume_pricing_rpastd_5d21dcl5_base_v132_signal(revenue, assets, closeadj):
    result = _std(_f17_revenue_per_asset(revenue, assets), 21) * _mean(closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f17lvp_f17_lng_volume_pricing_rpastd_5d21dcl21_base_v133_signal(revenue, assets, closeadj):
    result = _std(_f17_revenue_per_asset(revenue, assets), 21) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f17lvp_f17_lng_volume_pricing_rpastd_5d21dcl63_base_v134_signal(revenue, assets, closeadj):
    result = _std(_f17_revenue_per_asset(revenue, assets), 21) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f17lvp_f17_lng_volume_pricing_rpastd_5d21dclz21_base_v135_signal(revenue, assets, closeadj):
    result = _std(_f17_revenue_per_asset(revenue, assets), 21) * _z(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f17lvp_f17_lng_volume_pricing_rpastd_5d21dclz63_base_v136_signal(revenue, assets, closeadj):
    result = _std(_f17_revenue_per_asset(revenue, assets), 21) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f17lvp_f17_lng_volume_pricing_rpastd_5d21dclret21_base_v137_signal(revenue, assets, closeadj):
    result = _std(_f17_revenue_per_asset(revenue, assets), 21) * closeadj.pct_change(21)
    return result.replace([np.inf, -np.inf], np.nan)


def f17lvp_f17_lng_volume_pricing_rpastd_5d21dclret63_base_v138_signal(revenue, assets, closeadj):
    result = _std(_f17_revenue_per_asset(revenue, assets), 21) * closeadj.pct_change(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f17lvp_f17_lng_volume_pricing_rpastd_5d21dclsqr_base_v139_signal(revenue, assets, closeadj):
    result = _std(_f17_revenue_per_asset(revenue, assets), 21) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17lvp_f17_lng_volume_pricing_rpastd_5d21dclema21_base_v140_signal(revenue, assets, closeadj):
    result = _std(_f17_revenue_per_asset(revenue, assets), 21) * closeadj.ewm(span=21, min_periods=10).mean()
    return result.replace([np.inf, -np.inf], np.nan)


def f17lvp_f17_lng_volume_pricing_rpastd_5d42dcl_base_v141_signal(revenue, assets, closeadj):
    result = _std(_f17_revenue_per_asset(revenue, assets), 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17lvp_f17_lng_volume_pricing_rpastd_5d42dcl5_base_v142_signal(revenue, assets, closeadj):
    result = _std(_f17_revenue_per_asset(revenue, assets), 42) * _mean(closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f17lvp_f17_lng_volume_pricing_rpastd_5d42dcl21_base_v143_signal(revenue, assets, closeadj):
    result = _std(_f17_revenue_per_asset(revenue, assets), 42) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f17lvp_f17_lng_volume_pricing_rpastd_5d42dcl63_base_v144_signal(revenue, assets, closeadj):
    result = _std(_f17_revenue_per_asset(revenue, assets), 42) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f17lvp_f17_lng_volume_pricing_rpastd_5d42dclz21_base_v145_signal(revenue, assets, closeadj):
    result = _std(_f17_revenue_per_asset(revenue, assets), 42) * _z(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f17lvp_f17_lng_volume_pricing_rpastd_5d42dclz63_base_v146_signal(revenue, assets, closeadj):
    result = _std(_f17_revenue_per_asset(revenue, assets), 42) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f17lvp_f17_lng_volume_pricing_rpastd_5d42dclret21_base_v147_signal(revenue, assets, closeadj):
    result = _std(_f17_revenue_per_asset(revenue, assets), 42) * closeadj.pct_change(21)
    return result.replace([np.inf, -np.inf], np.nan)


def f17lvp_f17_lng_volume_pricing_rpastd_5d42dclret63_base_v148_signal(revenue, assets, closeadj):
    result = _std(_f17_revenue_per_asset(revenue, assets), 42) * closeadj.pct_change(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f17lvp_f17_lng_volume_pricing_rpastd_5d42dclsqr_base_v149_signal(revenue, assets, closeadj):
    result = _std(_f17_revenue_per_asset(revenue, assets), 42) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17lvp_f17_lng_volume_pricing_rpastd_5d42dclema21_base_v150_signal(revenue, assets, closeadj):
    result = _std(_f17_revenue_per_asset(revenue, assets), 42) * closeadj.ewm(span=21, min_periods=10).mean()
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f17lvp_f17_lng_volume_pricing_rpamean_5d189dclz63_base_v076_signal,
    f17lvp_f17_lng_volume_pricing_rpamean_5d189dclret21_base_v077_signal,
    f17lvp_f17_lng_volume_pricing_rpamean_5d189dclret63_base_v078_signal,
    f17lvp_f17_lng_volume_pricing_rpamean_5d189dclsqr_base_v079_signal,
    f17lvp_f17_lng_volume_pricing_rpamean_5d189dclema21_base_v080_signal,
    f17lvp_f17_lng_volume_pricing_rpamean_5d252dcl_base_v081_signal,
    f17lvp_f17_lng_volume_pricing_rpamean_5d252dcl5_base_v082_signal,
    f17lvp_f17_lng_volume_pricing_rpamean_5d252dcl21_base_v083_signal,
    f17lvp_f17_lng_volume_pricing_rpamean_5d252dcl63_base_v084_signal,
    f17lvp_f17_lng_volume_pricing_rpamean_5d252dclz21_base_v085_signal,
    f17lvp_f17_lng_volume_pricing_rpamean_5d252dclz63_base_v086_signal,
    f17lvp_f17_lng_volume_pricing_rpamean_5d252dclret21_base_v087_signal,
    f17lvp_f17_lng_volume_pricing_rpamean_5d252dclret63_base_v088_signal,
    f17lvp_f17_lng_volume_pricing_rpamean_5d252dclsqr_base_v089_signal,
    f17lvp_f17_lng_volume_pricing_rpamean_5d252dclema21_base_v090_signal,
    f17lvp_f17_lng_volume_pricing_rpamean_5d378dcl_base_v091_signal,
    f17lvp_f17_lng_volume_pricing_rpamean_5d378dcl5_base_v092_signal,
    f17lvp_f17_lng_volume_pricing_rpamean_5d378dcl21_base_v093_signal,
    f17lvp_f17_lng_volume_pricing_rpamean_5d378dcl63_base_v094_signal,
    f17lvp_f17_lng_volume_pricing_rpamean_5d378dclz21_base_v095_signal,
    f17lvp_f17_lng_volume_pricing_rpamean_5d378dclz63_base_v096_signal,
    f17lvp_f17_lng_volume_pricing_rpamean_5d378dclret21_base_v097_signal,
    f17lvp_f17_lng_volume_pricing_rpamean_5d378dclret63_base_v098_signal,
    f17lvp_f17_lng_volume_pricing_rpamean_5d378dclsqr_base_v099_signal,
    f17lvp_f17_lng_volume_pricing_rpamean_5d378dclema21_base_v100_signal,
    f17lvp_f17_lng_volume_pricing_rpamean_5d504dcl_base_v101_signal,
    f17lvp_f17_lng_volume_pricing_rpamean_5d504dcl5_base_v102_signal,
    f17lvp_f17_lng_volume_pricing_rpamean_5d504dcl21_base_v103_signal,
    f17lvp_f17_lng_volume_pricing_rpamean_5d504dcl63_base_v104_signal,
    f17lvp_f17_lng_volume_pricing_rpamean_5d504dclz21_base_v105_signal,
    f17lvp_f17_lng_volume_pricing_rpamean_5d504dclz63_base_v106_signal,
    f17lvp_f17_lng_volume_pricing_rpamean_5d504dclret21_base_v107_signal,
    f17lvp_f17_lng_volume_pricing_rpamean_5d504dclret63_base_v108_signal,
    f17lvp_f17_lng_volume_pricing_rpamean_5d504dclsqr_base_v109_signal,
    f17lvp_f17_lng_volume_pricing_rpamean_5d504dclema21_base_v110_signal,
    f17lvp_f17_lng_volume_pricing_rpastd_5d5dcl_base_v111_signal,
    f17lvp_f17_lng_volume_pricing_rpastd_5d5dcl5_base_v112_signal,
    f17lvp_f17_lng_volume_pricing_rpastd_5d5dcl21_base_v113_signal,
    f17lvp_f17_lng_volume_pricing_rpastd_5d5dcl63_base_v114_signal,
    f17lvp_f17_lng_volume_pricing_rpastd_5d5dclz21_base_v115_signal,
    f17lvp_f17_lng_volume_pricing_rpastd_5d5dclz63_base_v116_signal,
    f17lvp_f17_lng_volume_pricing_rpastd_5d5dclret21_base_v117_signal,
    f17lvp_f17_lng_volume_pricing_rpastd_5d5dclret63_base_v118_signal,
    f17lvp_f17_lng_volume_pricing_rpastd_5d5dclsqr_base_v119_signal,
    f17lvp_f17_lng_volume_pricing_rpastd_5d5dclema21_base_v120_signal,
    f17lvp_f17_lng_volume_pricing_rpastd_5d10dcl_base_v121_signal,
    f17lvp_f17_lng_volume_pricing_rpastd_5d10dcl5_base_v122_signal,
    f17lvp_f17_lng_volume_pricing_rpastd_5d10dcl21_base_v123_signal,
    f17lvp_f17_lng_volume_pricing_rpastd_5d10dcl63_base_v124_signal,
    f17lvp_f17_lng_volume_pricing_rpastd_5d10dclz21_base_v125_signal,
    f17lvp_f17_lng_volume_pricing_rpastd_5d10dclz63_base_v126_signal,
    f17lvp_f17_lng_volume_pricing_rpastd_5d10dclret21_base_v127_signal,
    f17lvp_f17_lng_volume_pricing_rpastd_5d10dclret63_base_v128_signal,
    f17lvp_f17_lng_volume_pricing_rpastd_5d10dclsqr_base_v129_signal,
    f17lvp_f17_lng_volume_pricing_rpastd_5d10dclema21_base_v130_signal,
    f17lvp_f17_lng_volume_pricing_rpastd_5d21dcl_base_v131_signal,
    f17lvp_f17_lng_volume_pricing_rpastd_5d21dcl5_base_v132_signal,
    f17lvp_f17_lng_volume_pricing_rpastd_5d21dcl21_base_v133_signal,
    f17lvp_f17_lng_volume_pricing_rpastd_5d21dcl63_base_v134_signal,
    f17lvp_f17_lng_volume_pricing_rpastd_5d21dclz21_base_v135_signal,
    f17lvp_f17_lng_volume_pricing_rpastd_5d21dclz63_base_v136_signal,
    f17lvp_f17_lng_volume_pricing_rpastd_5d21dclret21_base_v137_signal,
    f17lvp_f17_lng_volume_pricing_rpastd_5d21dclret63_base_v138_signal,
    f17lvp_f17_lng_volume_pricing_rpastd_5d21dclsqr_base_v139_signal,
    f17lvp_f17_lng_volume_pricing_rpastd_5d21dclema21_base_v140_signal,
    f17lvp_f17_lng_volume_pricing_rpastd_5d42dcl_base_v141_signal,
    f17lvp_f17_lng_volume_pricing_rpastd_5d42dcl5_base_v142_signal,
    f17lvp_f17_lng_volume_pricing_rpastd_5d42dcl21_base_v143_signal,
    f17lvp_f17_lng_volume_pricing_rpastd_5d42dcl63_base_v144_signal,
    f17lvp_f17_lng_volume_pricing_rpastd_5d42dclz21_base_v145_signal,
    f17lvp_f17_lng_volume_pricing_rpastd_5d42dclz63_base_v146_signal,
    f17lvp_f17_lng_volume_pricing_rpastd_5d42dclret21_base_v147_signal,
    f17lvp_f17_lng_volume_pricing_rpastd_5d42dclret63_base_v148_signal,
    f17lvp_f17_lng_volume_pricing_rpastd_5d42dclsqr_base_v149_signal,
    f17lvp_f17_lng_volume_pricing_rpastd_5d42dclema21_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F17_LNG_VOLUME_PRICING_REGISTRY_076_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    revenue = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="revenue")
    capex   = pd.Series(5e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.02, n))), name="capex")
    ppnenet = pd.Series(7e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="ppnenet")
    assets  = pd.Series(2e9 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="assets")
    deferredrev = pd.Series(1.0e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="deferredrev")

    cols = {"closeadj": closeadj, "revenue": revenue, "capex": capex,
            "ppnenet": ppnenet, "assets": assets, "deferredrev": deferredrev}

    n_features = 0
    nan_ok = 0
    domain_primitives = ('_f17_revenue_per_asset', '_f17_lng_intensity', '_f17_pricing_signal',)
    import hashlib
    seen_bodies = set()
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
        body = "\n".join(l.strip() for l in src.splitlines()
                          if l.strip() and not l.strip().startswith("#") and not l.strip().startswith("def "))
        h = hashlib.sha1(body.encode()).hexdigest()
        assert h not in seen_bodies, f"DUP body in {name}"
        seen_bodies.add(h)
        n_features += 1
    assert n_features == 75, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print(f"OK f17_lng_volume_pricing_076_150_claude: {n_features} features pass")
