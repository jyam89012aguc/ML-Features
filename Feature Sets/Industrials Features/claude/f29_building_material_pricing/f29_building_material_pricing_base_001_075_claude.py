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
def _f29_gp_lift(gp, revenue, w):
    # Gross profit lift: ratio change of gp / revenue over window
    gpm = gp / revenue.replace(0, np.nan)
    return gpm.diff(periods=w)


def _f29_pricing_pass_through(grossmargin, cor, revenue, w):
    # Pricing pass-through: gross margin change vs cor/revenue change
    cor_share = cor / revenue.replace(0, np.nan)
    return grossmargin.diff(periods=w) / (cor_share.diff(periods=w).abs() + 1e-6)


def _f29_margin_recovery(grossmargin, w):
    # Margin recovery: gross margin minus its trailing trough
    trough = grossmargin.rolling(w, min_periods=max(1, w // 2)).min()
    return grossmargin - trough


def f29bmp_building_material_pricing_gplift_5d_base_v001_signal(gp, revenue, closeadj):
    result = (_f29_gp_lift(gp, revenue, 5)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f29bmp_building_material_pricing_gplift_10d_base_v002_signal(gp, revenue, closeadj):
    result = (_f29_gp_lift(gp, revenue, 10)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f29bmp_building_material_pricing_gplift_21d_base_v003_signal(gp, revenue, closeadj):
    result = (_f29_gp_lift(gp, revenue, 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f29bmp_building_material_pricing_gplift_42d_base_v004_signal(gp, revenue, closeadj):
    result = (_f29_gp_lift(gp, revenue, 42)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f29bmp_building_material_pricing_gplift_63d_base_v005_signal(gp, revenue, closeadj):
    result = (_f29_gp_lift(gp, revenue, 63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f29bmp_building_material_pricing_gplift_126d_base_v006_signal(gp, revenue, closeadj):
    result = (_f29_gp_lift(gp, revenue, 126)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f29bmp_building_material_pricing_gplift_189d_base_v007_signal(gp, revenue, closeadj):
    result = (_f29_gp_lift(gp, revenue, 189)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f29bmp_building_material_pricing_gplift_252d_base_v008_signal(gp, revenue, closeadj):
    result = (_f29_gp_lift(gp, revenue, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f29bmp_building_material_pricing_gplift_378d_base_v009_signal(gp, revenue, closeadj):
    result = (_f29_gp_lift(gp, revenue, 378)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f29bmp_building_material_pricing_gplift_504d_base_v010_signal(gp, revenue, closeadj):
    result = (_f29_gp_lift(gp, revenue, 504)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f29bmp_building_material_pricing_gplift_ma21d_base_v011_signal(gp, revenue, closeadj):
    result = (_mean(_f29_gp_lift(gp, revenue, 21), 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f29bmp_building_material_pricing_gplift_ma63d_base_v012_signal(gp, revenue, closeadj):
    result = (_mean(_f29_gp_lift(gp, revenue, 63), 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f29bmp_building_material_pricing_gplift_ma126d_base_v013_signal(gp, revenue, closeadj):
    result = (_mean(_f29_gp_lift(gp, revenue, 126), 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f29bmp_building_material_pricing_gplift_ma252d_base_v014_signal(gp, revenue, closeadj):
    result = (_mean(_f29_gp_lift(gp, revenue, 252), 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f29bmp_building_material_pricing_gplift_std63d_base_v015_signal(gp, revenue, closeadj):
    result = (_std(_f29_gp_lift(gp, revenue, 63), 63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f29bmp_building_material_pricing_gplift_std252d_base_v016_signal(gp, revenue, closeadj):
    result = (_std(_f29_gp_lift(gp, revenue, 252), 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f29bmp_building_material_pricing_gplift_z63d_base_v017_signal(gp, revenue, closeadj):
    result = (_z(_f29_gp_lift(gp, revenue, 63), 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f29bmp_building_material_pricing_gplift_z252d_base_v018_signal(gp, revenue, closeadj):
    result = (_z(_f29_gp_lift(gp, revenue, 252), 504)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f29bmp_building_material_pricing_gplift_ema21d_base_v019_signal(gp, revenue, closeadj):
    result = (_f29_gp_lift(gp, revenue, 21).ewm(span=21, adjust=False).mean()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f29bmp_building_material_pricing_gplift_ema63d_base_v020_signal(gp, revenue, closeadj):
    result = (_f29_gp_lift(gp, revenue, 63).ewm(span=63, adjust=False).mean()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f29bmp_building_material_pricing_gplift_ema252d_base_v021_signal(gp, revenue, closeadj):
    result = (_f29_gp_lift(gp, revenue, 252).ewm(span=252, adjust=False).mean()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f29bmp_building_material_pricing_gplift_rank252d_base_v022_signal(gp, revenue, closeadj):
    result = (_f29_gp_lift(gp, revenue, 63).rolling(252, min_periods=63).rank(pct=True)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f29bmp_building_material_pricing_gplift_rank504d_base_v023_signal(gp, revenue, closeadj):
    result = (_f29_gp_lift(gp, revenue, 63).rolling(504, min_periods=126).rank(pct=True)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f29bmp_building_material_pricing_gplift_abs_base_v024_signal(gp, revenue, closeadj):
    result = (_f29_gp_lift(gp, revenue, 63).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f29bmp_building_material_pricing_gplift_sq_base_v025_signal(gp, revenue, closeadj):
    result = (_f29_gp_lift(gp, revenue, 63) * _f29_gp_lift(gp, revenue, 63).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f29bmp_building_material_pricing_gplift_dev252_base_v026_signal(gp, revenue, closeadj):
    result = ((_f29_gp_lift(gp, revenue, 252) - _mean(_f29_gp_lift(gp, revenue, 252), 252))) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f29bmp_building_material_pricing_gplift_var252_base_v027_signal(gp, revenue, closeadj):
    result = (_f29_gp_lift(gp, revenue, 252).rolling(252, min_periods=63).var() * 100.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f29bmp_building_material_pricing_gplift_xlogpx_252_base_v028_signal(gp, revenue, closeadj):
    result = (_f29_gp_lift(gp, revenue, 252) * np.log(closeadj.replace(0, np.nan).abs())) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f29bmp_building_material_pricing_gplift_xpxgap_252_base_v029_signal(gp, revenue, closeadj):
    result = (_f29_gp_lift(gp, revenue, 252) * (closeadj - _mean(closeadj, 252))) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f29bmp_building_material_pricing_gplift_xpxdet_252_base_v030_signal(gp, revenue, closeadj):
    result = (_f29_gp_lift(gp, revenue, 252) * (closeadj / _mean(closeadj, 252).replace(0, np.nan) - 1.0)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f29bmp_building_material_pricing_gplift_xpkgap_252_base_v031_signal(gp, revenue, closeadj):
    result = (_f29_gp_lift(gp, revenue, 252) * ((closeadj - closeadj.rolling(252, min_periods=63).max()) / closeadj.rolling(252, min_periods=63).max().replace(0, np.nan).abs())) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f29bmp_building_material_pricing_gplift_xrange_252_base_v032_signal(gp, revenue, closeadj):
    result = (_f29_gp_lift(gp, revenue, 252) * (closeadj.rolling(252, min_periods=63).max() - closeadj.rolling(252, min_periods=63).min()) / closeadj) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f29bmp_building_material_pricing_gplift_xvolz_252_base_v033_signal(gp, revenue, closeadj):
    result = (_f29_gp_lift(gp, revenue, 252) * _z(closeadj, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f29bmp_building_material_pricing_gplift_xrevg_252_base_v034_signal(gp, revenue, closeadj):
    result = (_f29_gp_lift(gp, revenue, 252) * revenue.pct_change(252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f29bmp_building_material_pricing_gplift_xpxchg_63_base_v035_signal(gp, revenue, closeadj):
    result = (_f29_gp_lift(gp, revenue, 63) * closeadj.pct_change(63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f29bmp_building_material_pricing_gplift_xpxchg_252_base_v036_signal(gp, revenue, closeadj):
    result = (_f29_gp_lift(gp, revenue, 252) * closeadj.pct_change(252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f29bmp_building_material_pricing_gplift_xlogrev_252_base_v037_signal(gp, revenue, closeadj):
    result = (_f29_gp_lift(gp, revenue, 252) * np.log(revenue.replace(0, np.nan).abs())) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f29bmp_building_material_pricing_gplift_xloggp_252_base_v038_signal(gp, revenue, closeadj):
    result = (_f29_gp_lift(gp, revenue, 252) * np.log(gp.replace(0, np.nan).abs())) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f29bmp_building_material_pricing_gplift_diff63_base_v039_signal(gp, revenue, closeadj):
    result = (_f29_gp_lift(gp, revenue, 63).diff(21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f29bmp_building_material_pricing_gplift_diff252_base_v040_signal(gp, revenue, closeadj):
    result = (_f29_gp_lift(gp, revenue, 252).diff(63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f29bmp_building_material_pricing_gplift_sign_base_v041_signal(gp, revenue, closeadj):
    result = (np.sign(_f29_gp_lift(gp, revenue, 63)) * closeadj.pct_change(63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f29bmp_building_material_pricing_gplift_zema252_base_v042_signal(gp, revenue, closeadj):
    result = (_z(_f29_gp_lift(gp, revenue, 252), 504).ewm(span=63, adjust=False).mean()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f29bmp_building_material_pricing_pricept_5d_base_v043_signal(grossmargin, cor, revenue, closeadj):
    result = (_f29_pricing_pass_through(grossmargin, cor, revenue, 5)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f29bmp_building_material_pricing_pricept_10d_base_v044_signal(grossmargin, cor, revenue, closeadj):
    result = (_f29_pricing_pass_through(grossmargin, cor, revenue, 10)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f29bmp_building_material_pricing_pricept_21d_base_v045_signal(grossmargin, cor, revenue, closeadj):
    result = (_f29_pricing_pass_through(grossmargin, cor, revenue, 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f29bmp_building_material_pricing_pricept_42d_base_v046_signal(grossmargin, cor, revenue, closeadj):
    result = (_f29_pricing_pass_through(grossmargin, cor, revenue, 42)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f29bmp_building_material_pricing_pricept_63d_base_v047_signal(grossmargin, cor, revenue, closeadj):
    result = (_f29_pricing_pass_through(grossmargin, cor, revenue, 63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f29bmp_building_material_pricing_pricept_126d_base_v048_signal(grossmargin, cor, revenue, closeadj):
    result = (_f29_pricing_pass_through(grossmargin, cor, revenue, 126)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f29bmp_building_material_pricing_pricept_189d_base_v049_signal(grossmargin, cor, revenue, closeadj):
    result = (_f29_pricing_pass_through(grossmargin, cor, revenue, 189)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f29bmp_building_material_pricing_pricept_252d_base_v050_signal(grossmargin, cor, revenue, closeadj):
    result = (_f29_pricing_pass_through(grossmargin, cor, revenue, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f29bmp_building_material_pricing_pricept_378d_base_v051_signal(grossmargin, cor, revenue, closeadj):
    result = (_f29_pricing_pass_through(grossmargin, cor, revenue, 378)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f29bmp_building_material_pricing_pricept_504d_base_v052_signal(grossmargin, cor, revenue, closeadj):
    result = (_f29_pricing_pass_through(grossmargin, cor, revenue, 504)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f29bmp_building_material_pricing_pricept_ma21d_base_v053_signal(grossmargin, cor, revenue, closeadj):
    result = (_mean(_f29_pricing_pass_through(grossmargin, cor, revenue, 21), 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f29bmp_building_material_pricing_pricept_ma63d_base_v054_signal(grossmargin, cor, revenue, closeadj):
    result = (_mean(_f29_pricing_pass_through(grossmargin, cor, revenue, 63), 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f29bmp_building_material_pricing_pricept_ma252d_base_v055_signal(grossmargin, cor, revenue, closeadj):
    result = (_mean(_f29_pricing_pass_through(grossmargin, cor, revenue, 252), 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f29bmp_building_material_pricing_pricept_std63d_base_v056_signal(grossmargin, cor, revenue, closeadj):
    result = (_std(_f29_pricing_pass_through(grossmargin, cor, revenue, 63), 63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f29bmp_building_material_pricing_pricept_std252d_base_v057_signal(grossmargin, cor, revenue, closeadj):
    result = (_std(_f29_pricing_pass_through(grossmargin, cor, revenue, 252), 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f29bmp_building_material_pricing_pricept_z63d_base_v058_signal(grossmargin, cor, revenue, closeadj):
    result = (_z(_f29_pricing_pass_through(grossmargin, cor, revenue, 63), 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f29bmp_building_material_pricing_pricept_z252d_base_v059_signal(grossmargin, cor, revenue, closeadj):
    result = (_z(_f29_pricing_pass_through(grossmargin, cor, revenue, 252), 504)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f29bmp_building_material_pricing_pricept_ema21d_base_v060_signal(grossmargin, cor, revenue, closeadj):
    result = (_f29_pricing_pass_through(grossmargin, cor, revenue, 21).ewm(span=21, adjust=False).mean()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f29bmp_building_material_pricing_pricept_ema63d_base_v061_signal(grossmargin, cor, revenue, closeadj):
    result = (_f29_pricing_pass_through(grossmargin, cor, revenue, 63).ewm(span=63, adjust=False).mean()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f29bmp_building_material_pricing_pricept_ema252d_base_v062_signal(grossmargin, cor, revenue, closeadj):
    result = (_f29_pricing_pass_through(grossmargin, cor, revenue, 252).ewm(span=252, adjust=False).mean()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f29bmp_building_material_pricing_pricept_rank252d_base_v063_signal(grossmargin, cor, revenue, closeadj):
    result = (_f29_pricing_pass_through(grossmargin, cor, revenue, 63).rolling(252, min_periods=63).rank(pct=True)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f29bmp_building_material_pricing_pricept_rank504d_base_v064_signal(grossmargin, cor, revenue, closeadj):
    result = (_f29_pricing_pass_through(grossmargin, cor, revenue, 63).rolling(504, min_periods=126).rank(pct=True)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f29bmp_building_material_pricing_pricept_abs_base_v065_signal(grossmargin, cor, revenue, closeadj):
    result = (_f29_pricing_pass_through(grossmargin, cor, revenue, 63).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f29bmp_building_material_pricing_pricept_sq_base_v066_signal(grossmargin, cor, revenue, closeadj):
    result = (_f29_pricing_pass_through(grossmargin, cor, revenue, 63) * _f29_pricing_pass_through(grossmargin, cor, revenue, 63).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f29bmp_building_material_pricing_pricept_dev252_base_v067_signal(grossmargin, cor, revenue, closeadj):
    result = ((_f29_pricing_pass_through(grossmargin, cor, revenue, 252) - _mean(_f29_pricing_pass_through(grossmargin, cor, revenue, 252), 252))) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f29bmp_building_material_pricing_pricept_var252_base_v068_signal(grossmargin, cor, revenue, closeadj):
    result = (_f29_pricing_pass_through(grossmargin, cor, revenue, 252).rolling(252, min_periods=63).var() * 100.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f29bmp_building_material_pricing_pricept_xlogpx_252_base_v069_signal(grossmargin, cor, revenue, closeadj):
    result = (_f29_pricing_pass_through(grossmargin, cor, revenue, 252) * np.log(closeadj.replace(0, np.nan).abs())) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f29bmp_building_material_pricing_pricept_xpxgap_252_base_v070_signal(grossmargin, cor, revenue, closeadj):
    result = (_f29_pricing_pass_through(grossmargin, cor, revenue, 252) * (closeadj - _mean(closeadj, 252))) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f29bmp_building_material_pricing_pricept_xpxdet_252_base_v071_signal(grossmargin, cor, revenue, closeadj):
    result = (_f29_pricing_pass_through(grossmargin, cor, revenue, 252) * (closeadj / _mean(closeadj, 252).replace(0, np.nan) - 1.0)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f29bmp_building_material_pricing_pricept_xpkgap_252_base_v072_signal(grossmargin, cor, revenue, closeadj):
    result = (_f29_pricing_pass_through(grossmargin, cor, revenue, 252) * ((closeadj - closeadj.rolling(252, min_periods=63).max()) / closeadj.rolling(252, min_periods=63).max().replace(0, np.nan).abs())) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f29bmp_building_material_pricing_pricept_xrange_252_base_v073_signal(grossmargin, cor, revenue, closeadj):
    result = (_f29_pricing_pass_through(grossmargin, cor, revenue, 252) * (closeadj.rolling(252, min_periods=63).max() - closeadj.rolling(252, min_periods=63).min()) / closeadj) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f29bmp_building_material_pricing_pricept_xvolz_252_base_v074_signal(grossmargin, cor, revenue, closeadj):
    result = (_f29_pricing_pass_through(grossmargin, cor, revenue, 252) * _z(closeadj, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f29bmp_building_material_pricing_pricept_xrevg_252_base_v075_signal(grossmargin, cor, revenue, closeadj):
    result = (_f29_pricing_pass_through(grossmargin, cor, revenue, 252) * revenue.pct_change(252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f29bmp_building_material_pricing_gplift_5d_base_v001_signal,
    f29bmp_building_material_pricing_gplift_10d_base_v002_signal,
    f29bmp_building_material_pricing_gplift_21d_base_v003_signal,
    f29bmp_building_material_pricing_gplift_42d_base_v004_signal,
    f29bmp_building_material_pricing_gplift_63d_base_v005_signal,
    f29bmp_building_material_pricing_gplift_126d_base_v006_signal,
    f29bmp_building_material_pricing_gplift_189d_base_v007_signal,
    f29bmp_building_material_pricing_gplift_252d_base_v008_signal,
    f29bmp_building_material_pricing_gplift_378d_base_v009_signal,
    f29bmp_building_material_pricing_gplift_504d_base_v010_signal,
    f29bmp_building_material_pricing_gplift_ma21d_base_v011_signal,
    f29bmp_building_material_pricing_gplift_ma63d_base_v012_signal,
    f29bmp_building_material_pricing_gplift_ma126d_base_v013_signal,
    f29bmp_building_material_pricing_gplift_ma252d_base_v014_signal,
    f29bmp_building_material_pricing_gplift_std63d_base_v015_signal,
    f29bmp_building_material_pricing_gplift_std252d_base_v016_signal,
    f29bmp_building_material_pricing_gplift_z63d_base_v017_signal,
    f29bmp_building_material_pricing_gplift_z252d_base_v018_signal,
    f29bmp_building_material_pricing_gplift_ema21d_base_v019_signal,
    f29bmp_building_material_pricing_gplift_ema63d_base_v020_signal,
    f29bmp_building_material_pricing_gplift_ema252d_base_v021_signal,
    f29bmp_building_material_pricing_gplift_rank252d_base_v022_signal,
    f29bmp_building_material_pricing_gplift_rank504d_base_v023_signal,
    f29bmp_building_material_pricing_gplift_abs_base_v024_signal,
    f29bmp_building_material_pricing_gplift_sq_base_v025_signal,
    f29bmp_building_material_pricing_gplift_dev252_base_v026_signal,
    f29bmp_building_material_pricing_gplift_var252_base_v027_signal,
    f29bmp_building_material_pricing_gplift_xlogpx_252_base_v028_signal,
    f29bmp_building_material_pricing_gplift_xpxgap_252_base_v029_signal,
    f29bmp_building_material_pricing_gplift_xpxdet_252_base_v030_signal,
    f29bmp_building_material_pricing_gplift_xpkgap_252_base_v031_signal,
    f29bmp_building_material_pricing_gplift_xrange_252_base_v032_signal,
    f29bmp_building_material_pricing_gplift_xvolz_252_base_v033_signal,
    f29bmp_building_material_pricing_gplift_xrevg_252_base_v034_signal,
    f29bmp_building_material_pricing_gplift_xpxchg_63_base_v035_signal,
    f29bmp_building_material_pricing_gplift_xpxchg_252_base_v036_signal,
    f29bmp_building_material_pricing_gplift_xlogrev_252_base_v037_signal,
    f29bmp_building_material_pricing_gplift_xloggp_252_base_v038_signal,
    f29bmp_building_material_pricing_gplift_diff63_base_v039_signal,
    f29bmp_building_material_pricing_gplift_diff252_base_v040_signal,
    f29bmp_building_material_pricing_gplift_sign_base_v041_signal,
    f29bmp_building_material_pricing_gplift_zema252_base_v042_signal,
    f29bmp_building_material_pricing_pricept_5d_base_v043_signal,
    f29bmp_building_material_pricing_pricept_10d_base_v044_signal,
    f29bmp_building_material_pricing_pricept_21d_base_v045_signal,
    f29bmp_building_material_pricing_pricept_42d_base_v046_signal,
    f29bmp_building_material_pricing_pricept_63d_base_v047_signal,
    f29bmp_building_material_pricing_pricept_126d_base_v048_signal,
    f29bmp_building_material_pricing_pricept_189d_base_v049_signal,
    f29bmp_building_material_pricing_pricept_252d_base_v050_signal,
    f29bmp_building_material_pricing_pricept_378d_base_v051_signal,
    f29bmp_building_material_pricing_pricept_504d_base_v052_signal,
    f29bmp_building_material_pricing_pricept_ma21d_base_v053_signal,
    f29bmp_building_material_pricing_pricept_ma63d_base_v054_signal,
    f29bmp_building_material_pricing_pricept_ma252d_base_v055_signal,
    f29bmp_building_material_pricing_pricept_std63d_base_v056_signal,
    f29bmp_building_material_pricing_pricept_std252d_base_v057_signal,
    f29bmp_building_material_pricing_pricept_z63d_base_v058_signal,
    f29bmp_building_material_pricing_pricept_z252d_base_v059_signal,
    f29bmp_building_material_pricing_pricept_ema21d_base_v060_signal,
    f29bmp_building_material_pricing_pricept_ema63d_base_v061_signal,
    f29bmp_building_material_pricing_pricept_ema252d_base_v062_signal,
    f29bmp_building_material_pricing_pricept_rank252d_base_v063_signal,
    f29bmp_building_material_pricing_pricept_rank504d_base_v064_signal,
    f29bmp_building_material_pricing_pricept_abs_base_v065_signal,
    f29bmp_building_material_pricing_pricept_sq_base_v066_signal,
    f29bmp_building_material_pricing_pricept_dev252_base_v067_signal,
    f29bmp_building_material_pricing_pricept_var252_base_v068_signal,
    f29bmp_building_material_pricing_pricept_xlogpx_252_base_v069_signal,
    f29bmp_building_material_pricing_pricept_xpxgap_252_base_v070_signal,
    f29bmp_building_material_pricing_pricept_xpxdet_252_base_v071_signal,
    f29bmp_building_material_pricing_pricept_xpkgap_252_base_v072_signal,
    f29bmp_building_material_pricing_pricept_xrange_252_base_v073_signal,
    f29bmp_building_material_pricing_pricept_xvolz_252_base_v074_signal,
    f29bmp_building_material_pricing_pricept_xrevg_252_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F29_BUILDING_MATERIAL_PRICING_REGISTRY_001_075 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    revenue = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="revenue")
    gp = pd.Series(3.5e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="gp")
    cor = pd.Series(6e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="cor")
    grossmargin = pd.Series(0.30 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="grossmargin")

    cols = {
        "closeadj": closeadj, "revenue": revenue, "gp": gp, "cor": cor, "grossmargin": grossmargin,
    }


    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f29_gp_lift", "_f29_pricing_pass_through", "_f29_margin_recovery")
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
    print(f"OK f29_building_material_pricing_base_001_075_claude: {n_features} features pass")
