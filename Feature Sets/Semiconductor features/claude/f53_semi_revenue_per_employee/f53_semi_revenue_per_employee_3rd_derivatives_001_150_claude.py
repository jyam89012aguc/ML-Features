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


def _max(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).max()


def _min(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).min()


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


def _slope_diff_norm(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)


def _curvature(s, w):
    sl = s.diff(periods=w) / s.abs().replace(0, np.nan)
    return sl.diff(periods=w) / sl.abs().replace(0, np.nan)


# ===== folder domain primitives =====
def _f53rp_rev_opex(rev, opex):
    return rev / opex.replace(0, np.nan)


def _f53rp_rev_ppne(rev, ppne):
    return rev / ppne.replace(0, np.nan)


def _f53rp_rev_assets(rev, assets):
    return rev / assets.replace(0, np.nan)


def _f53rp_align(q, idx):
    return q.reindex(idx).ffill()


# 5d curv of 21d level of revopex
def f53rp_f53_semi_revenue_per_employee_revopex_level_21d_curv_v001_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_opex(revenue, opex), closeadj.index)
    base = m - _mean(m, 21)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 21d level of revopex
def f53rp_f53_semi_revenue_per_employee_revopex_level_21d_curv_v002_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_opex(revenue, opex), closeadj.index)
    base = m - _mean(m, 21)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 21d level of revopex
def f53rp_f53_semi_revenue_per_employee_revopex_level_21d_curv_v003_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_opex(revenue, opex), closeadj.index)
    base = m - _mean(m, 21)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 21d level of revopex
def f53rp_f53_semi_revenue_per_employee_revopex_level_21d_curv_v004_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_opex(revenue, opex), closeadj.index)
    base = m - _mean(m, 21)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 21d level of revopex
def f53rp_f53_semi_revenue_per_employee_revopex_level_21d_curv_v005_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_opex(revenue, opex), closeadj.index)
    base = m - _mean(m, 21)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 63d level of revppne
def f53rp_f53_semi_revenue_per_employee_revppne_level_63d_curv_v006_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_ppne(revenue, ppnenet), closeadj.index)
    base = m - _mean(m, 63)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 63d level of revppne
def f53rp_f53_semi_revenue_per_employee_revppne_level_63d_curv_v007_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_ppne(revenue, ppnenet), closeadj.index)
    base = m - _mean(m, 63)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 63d level of revppne
def f53rp_f53_semi_revenue_per_employee_revppne_level_63d_curv_v008_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_ppne(revenue, ppnenet), closeadj.index)
    base = m - _mean(m, 63)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 63d level of revppne
def f53rp_f53_semi_revenue_per_employee_revppne_level_63d_curv_v009_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_ppne(revenue, ppnenet), closeadj.index)
    base = m - _mean(m, 63)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 63d level of revppne
def f53rp_f53_semi_revenue_per_employee_revppne_level_63d_curv_v010_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_ppne(revenue, ppnenet), closeadj.index)
    base = m - _mean(m, 63)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 126d level of revassets
def f53rp_f53_semi_revenue_per_employee_revassets_level_126d_curv_v011_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_assets(revenue, assets), closeadj.index)
    base = m - _mean(m, 126)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 126d level of revassets
def f53rp_f53_semi_revenue_per_employee_revassets_level_126d_curv_v012_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_assets(revenue, assets), closeadj.index)
    base = m - _mean(m, 126)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 126d level of revassets
def f53rp_f53_semi_revenue_per_employee_revassets_level_126d_curv_v013_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_assets(revenue, assets), closeadj.index)
    base = m - _mean(m, 126)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 126d level of revassets
def f53rp_f53_semi_revenue_per_employee_revassets_level_126d_curv_v014_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_assets(revenue, assets), closeadj.index)
    base = m - _mean(m, 126)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 126d level of revassets
def f53rp_f53_semi_revenue_per_employee_revassets_level_126d_curv_v015_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_assets(revenue, assets), closeadj.index)
    base = m - _mean(m, 126)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 252d level of revopex
def f53rp_f53_semi_revenue_per_employee_revopex_level_252d_curv_v016_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_opex(revenue, opex), closeadj.index)
    base = m - _mean(m, 252)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 252d level of revopex
def f53rp_f53_semi_revenue_per_employee_revopex_level_252d_curv_v017_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_opex(revenue, opex), closeadj.index)
    base = m - _mean(m, 252)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 252d level of revopex
def f53rp_f53_semi_revenue_per_employee_revopex_level_252d_curv_v018_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_opex(revenue, opex), closeadj.index)
    base = m - _mean(m, 252)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 252d level of revopex
def f53rp_f53_semi_revenue_per_employee_revopex_level_252d_curv_v019_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_opex(revenue, opex), closeadj.index)
    base = m - _mean(m, 252)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 252d level of revopex
def f53rp_f53_semi_revenue_per_employee_revopex_level_252d_curv_v020_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_opex(revenue, opex), closeadj.index)
    base = m - _mean(m, 252)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 504d level of revppne
def f53rp_f53_semi_revenue_per_employee_revppne_level_504d_curv_v021_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_ppne(revenue, ppnenet), closeadj.index)
    base = m - _mean(m, 504)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 504d level of revppne
def f53rp_f53_semi_revenue_per_employee_revppne_level_504d_curv_v022_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_ppne(revenue, ppnenet), closeadj.index)
    base = m - _mean(m, 504)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 504d level of revppne
def f53rp_f53_semi_revenue_per_employee_revppne_level_504d_curv_v023_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_ppne(revenue, ppnenet), closeadj.index)
    base = m - _mean(m, 504)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 504d level of revppne
def f53rp_f53_semi_revenue_per_employee_revppne_level_504d_curv_v024_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_ppne(revenue, ppnenet), closeadj.index)
    base = m - _mean(m, 504)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 504d level of revppne
def f53rp_f53_semi_revenue_per_employee_revppne_level_504d_curv_v025_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_ppne(revenue, ppnenet), closeadj.index)
    base = m - _mean(m, 504)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 21d z of revassets
def f53rp_f53_semi_revenue_per_employee_revassets_z_21d_curv_v026_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_assets(revenue, assets), closeadj.index)
    base = _z(m, 21)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 21d z of revassets
def f53rp_f53_semi_revenue_per_employee_revassets_z_21d_curv_v027_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_assets(revenue, assets), closeadj.index)
    base = _z(m, 21)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 21d z of revassets
def f53rp_f53_semi_revenue_per_employee_revassets_z_21d_curv_v028_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_assets(revenue, assets), closeadj.index)
    base = _z(m, 21)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 21d z of revassets
def f53rp_f53_semi_revenue_per_employee_revassets_z_21d_curv_v029_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_assets(revenue, assets), closeadj.index)
    base = _z(m, 21)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 21d z of revassets
def f53rp_f53_semi_revenue_per_employee_revassets_z_21d_curv_v030_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_assets(revenue, assets), closeadj.index)
    base = _z(m, 21)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 63d z of revopex
def f53rp_f53_semi_revenue_per_employee_revopex_z_63d_curv_v031_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_opex(revenue, opex), closeadj.index)
    base = _z(m, 63)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 63d z of revopex
def f53rp_f53_semi_revenue_per_employee_revopex_z_63d_curv_v032_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_opex(revenue, opex), closeadj.index)
    base = _z(m, 63)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 63d z of revopex
def f53rp_f53_semi_revenue_per_employee_revopex_z_63d_curv_v033_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_opex(revenue, opex), closeadj.index)
    base = _z(m, 63)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 63d z of revopex
def f53rp_f53_semi_revenue_per_employee_revopex_z_63d_curv_v034_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_opex(revenue, opex), closeadj.index)
    base = _z(m, 63)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 63d z of revopex
def f53rp_f53_semi_revenue_per_employee_revopex_z_63d_curv_v035_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_opex(revenue, opex), closeadj.index)
    base = _z(m, 63)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 126d z of revppne
def f53rp_f53_semi_revenue_per_employee_revppne_z_126d_curv_v036_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_ppne(revenue, ppnenet), closeadj.index)
    base = _z(m, 126)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 126d z of revppne
def f53rp_f53_semi_revenue_per_employee_revppne_z_126d_curv_v037_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_ppne(revenue, ppnenet), closeadj.index)
    base = _z(m, 126)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 126d z of revppne
def f53rp_f53_semi_revenue_per_employee_revppne_z_126d_curv_v038_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_ppne(revenue, ppnenet), closeadj.index)
    base = _z(m, 126)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 126d z of revppne
def f53rp_f53_semi_revenue_per_employee_revppne_z_126d_curv_v039_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_ppne(revenue, ppnenet), closeadj.index)
    base = _z(m, 126)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 126d z of revppne
def f53rp_f53_semi_revenue_per_employee_revppne_z_126d_curv_v040_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_ppne(revenue, ppnenet), closeadj.index)
    base = _z(m, 126)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 252d z of revassets
def f53rp_f53_semi_revenue_per_employee_revassets_z_252d_curv_v041_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_assets(revenue, assets), closeadj.index)
    base = _z(m, 252)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 252d z of revassets
def f53rp_f53_semi_revenue_per_employee_revassets_z_252d_curv_v042_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_assets(revenue, assets), closeadj.index)
    base = _z(m, 252)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 252d z of revassets
def f53rp_f53_semi_revenue_per_employee_revassets_z_252d_curv_v043_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_assets(revenue, assets), closeadj.index)
    base = _z(m, 252)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 252d z of revassets
def f53rp_f53_semi_revenue_per_employee_revassets_z_252d_curv_v044_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_assets(revenue, assets), closeadj.index)
    base = _z(m, 252)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 252d z of revassets
def f53rp_f53_semi_revenue_per_employee_revassets_z_252d_curv_v045_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_assets(revenue, assets), closeadj.index)
    base = _z(m, 252)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 504d z of revopex
def f53rp_f53_semi_revenue_per_employee_revopex_z_504d_curv_v046_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_opex(revenue, opex), closeadj.index)
    base = _z(m, 504)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 504d z of revopex
def f53rp_f53_semi_revenue_per_employee_revopex_z_504d_curv_v047_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_opex(revenue, opex), closeadj.index)
    base = _z(m, 504)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 504d z of revopex
def f53rp_f53_semi_revenue_per_employee_revopex_z_504d_curv_v048_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_opex(revenue, opex), closeadj.index)
    base = _z(m, 504)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 504d z of revopex
def f53rp_f53_semi_revenue_per_employee_revopex_z_504d_curv_v049_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_opex(revenue, opex), closeadj.index)
    base = _z(m, 504)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 504d z of revopex
def f53rp_f53_semi_revenue_per_employee_revopex_z_504d_curv_v050_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_opex(revenue, opex), closeadj.index)
    base = _z(m, 504)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 21d max of revppne
def f53rp_f53_semi_revenue_per_employee_revppne_max_21d_curv_v051_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_ppne(revenue, ppnenet), closeadj.index)
    base = _max(m, 21)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 21d max of revppne
def f53rp_f53_semi_revenue_per_employee_revppne_max_21d_curv_v052_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_ppne(revenue, ppnenet), closeadj.index)
    base = _max(m, 21)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 21d max of revppne
def f53rp_f53_semi_revenue_per_employee_revppne_max_21d_curv_v053_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_ppne(revenue, ppnenet), closeadj.index)
    base = _max(m, 21)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 21d max of revppne
def f53rp_f53_semi_revenue_per_employee_revppne_max_21d_curv_v054_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_ppne(revenue, ppnenet), closeadj.index)
    base = _max(m, 21)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 21d max of revppne
def f53rp_f53_semi_revenue_per_employee_revppne_max_21d_curv_v055_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_ppne(revenue, ppnenet), closeadj.index)
    base = _max(m, 21)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 63d max of revassets
def f53rp_f53_semi_revenue_per_employee_revassets_max_63d_curv_v056_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_assets(revenue, assets), closeadj.index)
    base = _max(m, 63)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 63d max of revassets
def f53rp_f53_semi_revenue_per_employee_revassets_max_63d_curv_v057_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_assets(revenue, assets), closeadj.index)
    base = _max(m, 63)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 63d max of revassets
def f53rp_f53_semi_revenue_per_employee_revassets_max_63d_curv_v058_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_assets(revenue, assets), closeadj.index)
    base = _max(m, 63)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 63d max of revassets
def f53rp_f53_semi_revenue_per_employee_revassets_max_63d_curv_v059_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_assets(revenue, assets), closeadj.index)
    base = _max(m, 63)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 63d max of revassets
def f53rp_f53_semi_revenue_per_employee_revassets_max_63d_curv_v060_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_assets(revenue, assets), closeadj.index)
    base = _max(m, 63)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 126d max of revopex
def f53rp_f53_semi_revenue_per_employee_revopex_max_126d_curv_v061_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_opex(revenue, opex), closeadj.index)
    base = _max(m, 126)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 126d max of revopex
def f53rp_f53_semi_revenue_per_employee_revopex_max_126d_curv_v062_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_opex(revenue, opex), closeadj.index)
    base = _max(m, 126)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 126d max of revopex
def f53rp_f53_semi_revenue_per_employee_revopex_max_126d_curv_v063_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_opex(revenue, opex), closeadj.index)
    base = _max(m, 126)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 126d max of revopex
def f53rp_f53_semi_revenue_per_employee_revopex_max_126d_curv_v064_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_opex(revenue, opex), closeadj.index)
    base = _max(m, 126)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 126d max of revopex
def f53rp_f53_semi_revenue_per_employee_revopex_max_126d_curv_v065_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_opex(revenue, opex), closeadj.index)
    base = _max(m, 126)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 252d max of revppne
def f53rp_f53_semi_revenue_per_employee_revppne_max_252d_curv_v066_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_ppne(revenue, ppnenet), closeadj.index)
    base = _max(m, 252)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 252d max of revppne
def f53rp_f53_semi_revenue_per_employee_revppne_max_252d_curv_v067_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_ppne(revenue, ppnenet), closeadj.index)
    base = _max(m, 252)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 252d max of revppne
def f53rp_f53_semi_revenue_per_employee_revppne_max_252d_curv_v068_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_ppne(revenue, ppnenet), closeadj.index)
    base = _max(m, 252)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 252d max of revppne
def f53rp_f53_semi_revenue_per_employee_revppne_max_252d_curv_v069_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_ppne(revenue, ppnenet), closeadj.index)
    base = _max(m, 252)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 252d max of revppne
def f53rp_f53_semi_revenue_per_employee_revppne_max_252d_curv_v070_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_ppne(revenue, ppnenet), closeadj.index)
    base = _max(m, 252)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 504d max of revassets
def f53rp_f53_semi_revenue_per_employee_revassets_max_504d_curv_v071_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_assets(revenue, assets), closeadj.index)
    base = _max(m, 504)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 504d max of revassets
def f53rp_f53_semi_revenue_per_employee_revassets_max_504d_curv_v072_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_assets(revenue, assets), closeadj.index)
    base = _max(m, 504)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 504d max of revassets
def f53rp_f53_semi_revenue_per_employee_revassets_max_504d_curv_v073_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_assets(revenue, assets), closeadj.index)
    base = _max(m, 504)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 504d max of revassets
def f53rp_f53_semi_revenue_per_employee_revassets_max_504d_curv_v074_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_assets(revenue, assets), closeadj.index)
    base = _max(m, 504)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 504d max of revassets
def f53rp_f53_semi_revenue_per_employee_revassets_max_504d_curv_v075_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_assets(revenue, assets), closeadj.index)
    base = _max(m, 504)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 21d min of revopex
def f53rp_f53_semi_revenue_per_employee_revopex_min_21d_curv_v076_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_opex(revenue, opex), closeadj.index)
    base = _min(m, 21)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 21d min of revopex
def f53rp_f53_semi_revenue_per_employee_revopex_min_21d_curv_v077_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_opex(revenue, opex), closeadj.index)
    base = _min(m, 21)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 21d min of revopex
def f53rp_f53_semi_revenue_per_employee_revopex_min_21d_curv_v078_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_opex(revenue, opex), closeadj.index)
    base = _min(m, 21)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 21d min of revopex
def f53rp_f53_semi_revenue_per_employee_revopex_min_21d_curv_v079_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_opex(revenue, opex), closeadj.index)
    base = _min(m, 21)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 21d min of revopex
def f53rp_f53_semi_revenue_per_employee_revopex_min_21d_curv_v080_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_opex(revenue, opex), closeadj.index)
    base = _min(m, 21)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 63d min of revppne
def f53rp_f53_semi_revenue_per_employee_revppne_min_63d_curv_v081_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_ppne(revenue, ppnenet), closeadj.index)
    base = _min(m, 63)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 63d min of revppne
def f53rp_f53_semi_revenue_per_employee_revppne_min_63d_curv_v082_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_ppne(revenue, ppnenet), closeadj.index)
    base = _min(m, 63)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 63d min of revppne
def f53rp_f53_semi_revenue_per_employee_revppne_min_63d_curv_v083_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_ppne(revenue, ppnenet), closeadj.index)
    base = _min(m, 63)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 63d min of revppne
def f53rp_f53_semi_revenue_per_employee_revppne_min_63d_curv_v084_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_ppne(revenue, ppnenet), closeadj.index)
    base = _min(m, 63)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 63d min of revppne
def f53rp_f53_semi_revenue_per_employee_revppne_min_63d_curv_v085_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_ppne(revenue, ppnenet), closeadj.index)
    base = _min(m, 63)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 126d min of revassets
def f53rp_f53_semi_revenue_per_employee_revassets_min_126d_curv_v086_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_assets(revenue, assets), closeadj.index)
    base = _min(m, 126)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 126d min of revassets
def f53rp_f53_semi_revenue_per_employee_revassets_min_126d_curv_v087_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_assets(revenue, assets), closeadj.index)
    base = _min(m, 126)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 126d min of revassets
def f53rp_f53_semi_revenue_per_employee_revassets_min_126d_curv_v088_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_assets(revenue, assets), closeadj.index)
    base = _min(m, 126)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 126d min of revassets
def f53rp_f53_semi_revenue_per_employee_revassets_min_126d_curv_v089_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_assets(revenue, assets), closeadj.index)
    base = _min(m, 126)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 126d min of revassets
def f53rp_f53_semi_revenue_per_employee_revassets_min_126d_curv_v090_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_assets(revenue, assets), closeadj.index)
    base = _min(m, 126)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 252d min of revopex
def f53rp_f53_semi_revenue_per_employee_revopex_min_252d_curv_v091_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_opex(revenue, opex), closeadj.index)
    base = _min(m, 252)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 252d min of revopex
def f53rp_f53_semi_revenue_per_employee_revopex_min_252d_curv_v092_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_opex(revenue, opex), closeadj.index)
    base = _min(m, 252)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 252d min of revopex
def f53rp_f53_semi_revenue_per_employee_revopex_min_252d_curv_v093_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_opex(revenue, opex), closeadj.index)
    base = _min(m, 252)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 252d min of revopex
def f53rp_f53_semi_revenue_per_employee_revopex_min_252d_curv_v094_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_opex(revenue, opex), closeadj.index)
    base = _min(m, 252)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 252d min of revopex
def f53rp_f53_semi_revenue_per_employee_revopex_min_252d_curv_v095_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_opex(revenue, opex), closeadj.index)
    base = _min(m, 252)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 504d min of revppne
def f53rp_f53_semi_revenue_per_employee_revppne_min_504d_curv_v096_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_ppne(revenue, ppnenet), closeadj.index)
    base = _min(m, 504)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 504d min of revppne
def f53rp_f53_semi_revenue_per_employee_revppne_min_504d_curv_v097_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_ppne(revenue, ppnenet), closeadj.index)
    base = _min(m, 504)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 504d min of revppne
def f53rp_f53_semi_revenue_per_employee_revppne_min_504d_curv_v098_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_ppne(revenue, ppnenet), closeadj.index)
    base = _min(m, 504)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 504d min of revppne
def f53rp_f53_semi_revenue_per_employee_revppne_min_504d_curv_v099_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_ppne(revenue, ppnenet), closeadj.index)
    base = _min(m, 504)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 504d min of revppne
def f53rp_f53_semi_revenue_per_employee_revppne_min_504d_curv_v100_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_ppne(revenue, ppnenet), closeadj.index)
    base = _min(m, 504)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 21d dd of revassets
def f53rp_f53_semi_revenue_per_employee_revassets_dd_21d_curv_v101_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_assets(revenue, assets), closeadj.index)
    peak = _max(m, 21)
    base = m - peak
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 21d dd of revassets
def f53rp_f53_semi_revenue_per_employee_revassets_dd_21d_curv_v102_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_assets(revenue, assets), closeadj.index)
    peak = _max(m, 21)
    base = m - peak
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 21d dd of revassets
def f53rp_f53_semi_revenue_per_employee_revassets_dd_21d_curv_v103_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_assets(revenue, assets), closeadj.index)
    peak = _max(m, 21)
    base = m - peak
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 21d dd of revassets
def f53rp_f53_semi_revenue_per_employee_revassets_dd_21d_curv_v104_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_assets(revenue, assets), closeadj.index)
    peak = _max(m, 21)
    base = m - peak
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 21d dd of revassets
def f53rp_f53_semi_revenue_per_employee_revassets_dd_21d_curv_v105_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_assets(revenue, assets), closeadj.index)
    peak = _max(m, 21)
    base = m - peak
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 63d dd of revopex
def f53rp_f53_semi_revenue_per_employee_revopex_dd_63d_curv_v106_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_opex(revenue, opex), closeadj.index)
    peak = _max(m, 63)
    base = m - peak
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 63d dd of revopex
def f53rp_f53_semi_revenue_per_employee_revopex_dd_63d_curv_v107_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_opex(revenue, opex), closeadj.index)
    peak = _max(m, 63)
    base = m - peak
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 63d dd of revopex
def f53rp_f53_semi_revenue_per_employee_revopex_dd_63d_curv_v108_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_opex(revenue, opex), closeadj.index)
    peak = _max(m, 63)
    base = m - peak
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 63d dd of revopex
def f53rp_f53_semi_revenue_per_employee_revopex_dd_63d_curv_v109_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_opex(revenue, opex), closeadj.index)
    peak = _max(m, 63)
    base = m - peak
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 63d dd of revopex
def f53rp_f53_semi_revenue_per_employee_revopex_dd_63d_curv_v110_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_opex(revenue, opex), closeadj.index)
    peak = _max(m, 63)
    base = m - peak
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 126d dd of revppne
def f53rp_f53_semi_revenue_per_employee_revppne_dd_126d_curv_v111_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_ppne(revenue, ppnenet), closeadj.index)
    peak = _max(m, 126)
    base = m - peak
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 126d dd of revppne
def f53rp_f53_semi_revenue_per_employee_revppne_dd_126d_curv_v112_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_ppne(revenue, ppnenet), closeadj.index)
    peak = _max(m, 126)
    base = m - peak
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 126d dd of revppne
def f53rp_f53_semi_revenue_per_employee_revppne_dd_126d_curv_v113_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_ppne(revenue, ppnenet), closeadj.index)
    peak = _max(m, 126)
    base = m - peak
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 126d dd of revppne
def f53rp_f53_semi_revenue_per_employee_revppne_dd_126d_curv_v114_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_ppne(revenue, ppnenet), closeadj.index)
    peak = _max(m, 126)
    base = m - peak
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 126d dd of revppne
def f53rp_f53_semi_revenue_per_employee_revppne_dd_126d_curv_v115_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_ppne(revenue, ppnenet), closeadj.index)
    peak = _max(m, 126)
    base = m - peak
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 252d dd of revassets
def f53rp_f53_semi_revenue_per_employee_revassets_dd_252d_curv_v116_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_assets(revenue, assets), closeadj.index)
    peak = _max(m, 252)
    base = m - peak
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 252d dd of revassets
def f53rp_f53_semi_revenue_per_employee_revassets_dd_252d_curv_v117_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_assets(revenue, assets), closeadj.index)
    peak = _max(m, 252)
    base = m - peak
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 252d dd of revassets
def f53rp_f53_semi_revenue_per_employee_revassets_dd_252d_curv_v118_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_assets(revenue, assets), closeadj.index)
    peak = _max(m, 252)
    base = m - peak
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 252d dd of revassets
def f53rp_f53_semi_revenue_per_employee_revassets_dd_252d_curv_v119_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_assets(revenue, assets), closeadj.index)
    peak = _max(m, 252)
    base = m - peak
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 252d dd of revassets
def f53rp_f53_semi_revenue_per_employee_revassets_dd_252d_curv_v120_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_assets(revenue, assets), closeadj.index)
    peak = _max(m, 252)
    base = m - peak
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 504d dd of revopex
def f53rp_f53_semi_revenue_per_employee_revopex_dd_504d_curv_v121_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_opex(revenue, opex), closeadj.index)
    peak = _max(m, 504)
    base = m - peak
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 504d dd of revopex
def f53rp_f53_semi_revenue_per_employee_revopex_dd_504d_curv_v122_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_opex(revenue, opex), closeadj.index)
    peak = _max(m, 504)
    base = m - peak
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 504d dd of revopex
def f53rp_f53_semi_revenue_per_employee_revopex_dd_504d_curv_v123_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_opex(revenue, opex), closeadj.index)
    peak = _max(m, 504)
    base = m - peak
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 504d dd of revopex
def f53rp_f53_semi_revenue_per_employee_revopex_dd_504d_curv_v124_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_opex(revenue, opex), closeadj.index)
    peak = _max(m, 504)
    base = m - peak
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 504d dd of revopex
def f53rp_f53_semi_revenue_per_employee_revopex_dd_504d_curv_v125_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_opex(revenue, opex), closeadj.index)
    peak = _max(m, 504)
    base = m - peak
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 21d rng of revppne
def f53rp_f53_semi_revenue_per_employee_revppne_rng_21d_curv_v126_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_ppne(revenue, ppnenet), closeadj.index)
    base = _max(m, 21) - _min(m, 21)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 21d rng of revppne
def f53rp_f53_semi_revenue_per_employee_revppne_rng_21d_curv_v127_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_ppne(revenue, ppnenet), closeadj.index)
    base = _max(m, 21) - _min(m, 21)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 21d rng of revppne
def f53rp_f53_semi_revenue_per_employee_revppne_rng_21d_curv_v128_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_ppne(revenue, ppnenet), closeadj.index)
    base = _max(m, 21) - _min(m, 21)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 21d rng of revppne
def f53rp_f53_semi_revenue_per_employee_revppne_rng_21d_curv_v129_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_ppne(revenue, ppnenet), closeadj.index)
    base = _max(m, 21) - _min(m, 21)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 21d rng of revppne
def f53rp_f53_semi_revenue_per_employee_revppne_rng_21d_curv_v130_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_ppne(revenue, ppnenet), closeadj.index)
    base = _max(m, 21) - _min(m, 21)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 63d rng of revassets
def f53rp_f53_semi_revenue_per_employee_revassets_rng_63d_curv_v131_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_assets(revenue, assets), closeadj.index)
    base = _max(m, 63) - _min(m, 63)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 63d rng of revassets
def f53rp_f53_semi_revenue_per_employee_revassets_rng_63d_curv_v132_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_assets(revenue, assets), closeadj.index)
    base = _max(m, 63) - _min(m, 63)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 63d rng of revassets
def f53rp_f53_semi_revenue_per_employee_revassets_rng_63d_curv_v133_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_assets(revenue, assets), closeadj.index)
    base = _max(m, 63) - _min(m, 63)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 63d rng of revassets
def f53rp_f53_semi_revenue_per_employee_revassets_rng_63d_curv_v134_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_assets(revenue, assets), closeadj.index)
    base = _max(m, 63) - _min(m, 63)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 63d rng of revassets
def f53rp_f53_semi_revenue_per_employee_revassets_rng_63d_curv_v135_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_assets(revenue, assets), closeadj.index)
    base = _max(m, 63) - _min(m, 63)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 126d rng of revopex
def f53rp_f53_semi_revenue_per_employee_revopex_rng_126d_curv_v136_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_opex(revenue, opex), closeadj.index)
    base = _max(m, 126) - _min(m, 126)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 126d rng of revopex
def f53rp_f53_semi_revenue_per_employee_revopex_rng_126d_curv_v137_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_opex(revenue, opex), closeadj.index)
    base = _max(m, 126) - _min(m, 126)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 126d rng of revopex
def f53rp_f53_semi_revenue_per_employee_revopex_rng_126d_curv_v138_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_opex(revenue, opex), closeadj.index)
    base = _max(m, 126) - _min(m, 126)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 126d rng of revopex
def f53rp_f53_semi_revenue_per_employee_revopex_rng_126d_curv_v139_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_opex(revenue, opex), closeadj.index)
    base = _max(m, 126) - _min(m, 126)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 126d rng of revopex
def f53rp_f53_semi_revenue_per_employee_revopex_rng_126d_curv_v140_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_opex(revenue, opex), closeadj.index)
    base = _max(m, 126) - _min(m, 126)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 252d rng of revppne
def f53rp_f53_semi_revenue_per_employee_revppne_rng_252d_curv_v141_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_ppne(revenue, ppnenet), closeadj.index)
    base = _max(m, 252) - _min(m, 252)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 252d rng of revppne
def f53rp_f53_semi_revenue_per_employee_revppne_rng_252d_curv_v142_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_ppne(revenue, ppnenet), closeadj.index)
    base = _max(m, 252) - _min(m, 252)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 252d rng of revppne
def f53rp_f53_semi_revenue_per_employee_revppne_rng_252d_curv_v143_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_ppne(revenue, ppnenet), closeadj.index)
    base = _max(m, 252) - _min(m, 252)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 252d rng of revppne
def f53rp_f53_semi_revenue_per_employee_revppne_rng_252d_curv_v144_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_ppne(revenue, ppnenet), closeadj.index)
    base = _max(m, 252) - _min(m, 252)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 252d rng of revppne
def f53rp_f53_semi_revenue_per_employee_revppne_rng_252d_curv_v145_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_ppne(revenue, ppnenet), closeadj.index)
    base = _max(m, 252) - _min(m, 252)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 504d rng of revassets
def f53rp_f53_semi_revenue_per_employee_revassets_rng_504d_curv_v146_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_assets(revenue, assets), closeadj.index)
    base = _max(m, 504) - _min(m, 504)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 504d rng of revassets
def f53rp_f53_semi_revenue_per_employee_revassets_rng_504d_curv_v147_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_assets(revenue, assets), closeadj.index)
    base = _max(m, 504) - _min(m, 504)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 504d rng of revassets
def f53rp_f53_semi_revenue_per_employee_revassets_rng_504d_curv_v148_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_assets(revenue, assets), closeadj.index)
    base = _max(m, 504) - _min(m, 504)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 504d rng of revassets
def f53rp_f53_semi_revenue_per_employee_revassets_rng_504d_curv_v149_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_assets(revenue, assets), closeadj.index)
    base = _max(m, 504) - _min(m, 504)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 504d rng of revassets
def f53rp_f53_semi_revenue_per_employee_revassets_rng_504d_curv_v150_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_assets(revenue, assets), closeadj.index)
    base = _max(m, 504) - _min(m, 504)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

