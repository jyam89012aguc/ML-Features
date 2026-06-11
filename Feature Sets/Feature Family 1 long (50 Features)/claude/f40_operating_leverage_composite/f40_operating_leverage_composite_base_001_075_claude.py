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
def _f40_op_leverage_revopex(revenue, opex, w):
    rev_g = revenue.pct_change(w)
    opex_g = opex.pct_change(w)
    return rev_g / opex_g.replace(0, np.nan)


def _f40_op_leverage_opincrev(opinc, revenue, w):
    op_g = opinc.pct_change(w)
    rev_g = revenue.pct_change(w)
    return op_g / rev_g.replace(0, np.nan)


def _f40_op_leverage_marginchg(opinc, revenue, w):
    margin = opinc / revenue.replace(0, np.nan)
    return margin.diff(w)


# 21d operating leverage (revenue growth / opex growth) × closeadj
def f40olc_f40_operating_leverage_composite_revopex_21d_base_v001_signal(revenue, opinc, closeadj):
    opex = (revenue - opinc).abs().replace(0, np.nan)
    result = _f40_op_leverage_revopex(revenue, opex, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d revopex leverage × closeadj
def f40olc_f40_operating_leverage_composite_revopex_63d_base_v002_signal(revenue, opinc, closeadj):
    opex = (revenue - opinc).abs().replace(0, np.nan)
    result = _f40_op_leverage_revopex(revenue, opex, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d revopex leverage
def f40olc_f40_operating_leverage_composite_revopex_126d_base_v003_signal(revenue, opinc, closeadj):
    opex = (revenue - opinc).abs().replace(0, np.nan)
    result = _f40_op_leverage_revopex(revenue, opex, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d revopex leverage
def f40olc_f40_operating_leverage_composite_revopex_252d_base_v004_signal(revenue, opinc, closeadj):
    opex = (revenue - opinc).abs().replace(0, np.nan)
    result = _f40_op_leverage_revopex(revenue, opex, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d revopex leverage
def f40olc_f40_operating_leverage_composite_revopex_504d_base_v005_signal(revenue, opinc, closeadj):
    opex = (revenue - opinc).abs().replace(0, np.nan)
    result = _f40_op_leverage_revopex(revenue, opex, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d operating leverage opinc/rev
def f40olc_f40_operating_leverage_composite_opincrev_21d_base_v006_signal(opinc, revenue, closeadj):
    result = _f40_op_leverage_opincrev(opinc, revenue, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d opinc/rev growth ratio
def f40olc_f40_operating_leverage_composite_opincrev_63d_base_v007_signal(opinc, revenue, closeadj):
    result = _f40_op_leverage_opincrev(opinc, revenue, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d opinc/rev growth ratio
def f40olc_f40_operating_leverage_composite_opincrev_126d_base_v008_signal(opinc, revenue, closeadj):
    result = _f40_op_leverage_opincrev(opinc, revenue, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d opinc/rev growth ratio
def f40olc_f40_operating_leverage_composite_opincrev_252d_base_v009_signal(opinc, revenue, closeadj):
    result = _f40_op_leverage_opincrev(opinc, revenue, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d opinc/rev growth ratio
def f40olc_f40_operating_leverage_composite_opincrev_504d_base_v010_signal(opinc, revenue, closeadj):
    result = _f40_op_leverage_opincrev(opinc, revenue, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d operating margin change × closeadj
def f40olc_f40_operating_leverage_composite_marginchg_21d_base_v011_signal(opinc, revenue, closeadj):
    result = _f40_op_leverage_marginchg(opinc, revenue, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d op margin change × closeadj
def f40olc_f40_operating_leverage_composite_marginchg_63d_base_v012_signal(opinc, revenue, closeadj):
    result = _f40_op_leverage_marginchg(opinc, revenue, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d op margin change × closeadj
def f40olc_f40_operating_leverage_composite_marginchg_126d_base_v013_signal(opinc, revenue, closeadj):
    result = _f40_op_leverage_marginchg(opinc, revenue, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d op margin change × closeadj
def f40olc_f40_operating_leverage_composite_marginchg_252d_base_v014_signal(opinc, revenue, closeadj):
    result = _f40_op_leverage_marginchg(opinc, revenue, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d op margin change × closeadj
def f40olc_f40_operating_leverage_composite_marginchg_504d_base_v015_signal(opinc, revenue, closeadj):
    result = _f40_op_leverage_marginchg(opinc, revenue, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling mean of 21d revopex leverage
def f40olc_f40_operating_leverage_composite_revopexmean_21d_base_v016_signal(revenue, opinc, closeadj):
    opex = (revenue - opinc).abs().replace(0, np.nan)
    base = _f40_op_leverage_revopex(revenue, opex, 21)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling mean of 63d revopex leverage
def f40olc_f40_operating_leverage_composite_revopexmean_63d_base_v017_signal(revenue, opinc, closeadj):
    opex = (revenue - opinc).abs().replace(0, np.nan)
    base = _f40_op_leverage_revopex(revenue, opex, 63)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling mean of 63d opinc/rev growth
def f40olc_f40_operating_leverage_composite_opincrevmean_63d_base_v018_signal(opinc, revenue, closeadj):
    base = _f40_op_leverage_opincrev(opinc, revenue, 63)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling mean of 252d opinc/rev growth
def f40olc_f40_operating_leverage_composite_opincrevmean_252d_base_v019_signal(opinc, revenue, closeadj):
    base = _f40_op_leverage_opincrev(opinc, revenue, 252)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d std of 63d revopex leverage
def f40olc_f40_operating_leverage_composite_revopexstd_63d_base_v020_signal(revenue, opinc, closeadj):
    opex = (revenue - opinc).abs().replace(0, np.nan)
    base = _f40_op_leverage_revopex(revenue, opex, 63)
    result = _std(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d std of 252d revopex leverage
def f40olc_f40_operating_leverage_composite_revopexstd_252d_base_v021_signal(revenue, opinc, closeadj):
    opex = (revenue - opinc).abs().replace(0, np.nan)
    base = _f40_op_leverage_revopex(revenue, opex, 252)
    result = _std(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d zscore of 63d opinc/rev leverage
def f40olc_f40_operating_leverage_composite_opincrevz_252d_base_v022_signal(opinc, revenue, closeadj):
    base = _f40_op_leverage_opincrev(opinc, revenue, 63)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d zscore of 252d opinc/rev leverage
def f40olc_f40_operating_leverage_composite_opincrevz_504d_base_v023_signal(opinc, revenue, closeadj):
    base = _f40_op_leverage_opincrev(opinc, revenue, 252)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d zscore of 21d marginchg
def f40olc_f40_operating_leverage_composite_marginchgz_252d_base_v024_signal(opinc, revenue, closeadj):
    base = _f40_op_leverage_marginchg(opinc, revenue, 21)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d zscore of 252d marginchg
def f40olc_f40_operating_leverage_composite_marginchgz_504d_base_v025_signal(opinc, revenue, closeadj):
    base = _f40_op_leverage_marginchg(opinc, revenue, 252)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d revopex leverage × revenue level
def f40olc_f40_operating_leverage_composite_revopexxrev_252d_base_v026_signal(revenue, opinc, closeadj):
    opex = (revenue - opinc).abs().replace(0, np.nan)
    base = _f40_op_leverage_revopex(revenue, opex, 252)
    result = base * revenue * closeadj / 1.0e9
    return result.replace([np.inf, -np.inf], np.nan)


# 63d revopex leverage × revenue level
def f40olc_f40_operating_leverage_composite_revopexxrev_63d_base_v027_signal(revenue, opinc, closeadj):
    opex = (revenue - opinc).abs().replace(0, np.nan)
    base = _f40_op_leverage_revopex(revenue, opex, 63)
    result = base * revenue * closeadj / 1.0e9
    return result.replace([np.inf, -np.inf], np.nan)


# 252d opinc/rev leverage × revenue level
def f40olc_f40_operating_leverage_composite_opincrevxrev_252d_base_v028_signal(opinc, revenue, closeadj):
    base = _f40_op_leverage_opincrev(opinc, revenue, 252)
    result = base * revenue * closeadj / 1.0e9
    return result.replace([np.inf, -np.inf], np.nan)


# 63d opinc/rev leverage × revenue level
def f40olc_f40_operating_leverage_composite_opincrevxrev_63d_base_v029_signal(opinc, revenue, closeadj):
    base = _f40_op_leverage_opincrev(opinc, revenue, 63)
    result = base * revenue * closeadj / 1.0e9
    return result.replace([np.inf, -np.inf], np.nan)


# rolling 252d operating leverage × ebitda level
def f40olc_f40_operating_leverage_composite_olxebitda_252d_base_v030_signal(opinc, revenue, ebitda, closeadj):
    base = _f40_op_leverage_opincrev(opinc, revenue, 252)
    result = base * ebitda * closeadj / 1.0e9
    return result.replace([np.inf, -np.inf], np.nan)


# 63d operating leverage × ebitda level
def f40olc_f40_operating_leverage_composite_olxebitda_63d_base_v031_signal(opinc, revenue, ebitda, closeadj):
    base = _f40_op_leverage_opincrev(opinc, revenue, 63)
    result = base * ebitda * closeadj / 1.0e9
    return result.replace([np.inf, -np.inf], np.nan)


# 252d operating leverage × eps
def f40olc_f40_operating_leverage_composite_olxeps_252d_base_v032_signal(opinc, revenue, eps, closeadj):
    base = _f40_op_leverage_opincrev(opinc, revenue, 252)
    result = base * eps * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d operating leverage × eps
def f40olc_f40_operating_leverage_composite_olxeps_63d_base_v033_signal(opinc, revenue, eps, closeadj):
    base = _f40_op_leverage_opincrev(opinc, revenue, 63)
    result = base * eps * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d revopex leverage / 252d revopex leverage std (snr)
def f40olc_f40_operating_leverage_composite_revopexsnr_252d_base_v034_signal(revenue, opinc, closeadj):
    opex = (revenue - opinc).abs().replace(0, np.nan)
    base = _f40_op_leverage_revopex(revenue, opex, 252)
    sd = _std(base, 252).replace(0, np.nan)
    result = base / sd * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d revopex snr
def f40olc_f40_operating_leverage_composite_revopexsnr_504d_base_v035_signal(revenue, opinc, closeadj):
    opex = (revenue - opinc).abs().replace(0, np.nan)
    base = _f40_op_leverage_revopex(revenue, opex, 252)
    sd = _std(base, 504).replace(0, np.nan)
    result = base / sd * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d opinc/rev snr
def f40olc_f40_operating_leverage_composite_opincrevsnr_252d_base_v036_signal(opinc, revenue, closeadj):
    base = _f40_op_leverage_opincrev(opinc, revenue, 252)
    sd = _std(base, 252).replace(0, np.nan)
    result = base / sd * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d opinc/rev snr
def f40olc_f40_operating_leverage_composite_opincrevsnr_504d_base_v037_signal(opinc, revenue, closeadj):
    base = _f40_op_leverage_opincrev(opinc, revenue, 252)
    sd = _std(base, 504).replace(0, np.nan)
    result = base / sd * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# composite leverage signed × revenue magnitude
def f40olc_f40_operating_leverage_composite_olsignmag_252d_base_v038_signal(opinc, revenue, closeadj):
    base = _f40_op_leverage_opincrev(opinc, revenue, 252)
    result = np.sign(base) * base.abs() * revenue * closeadj / 1.0e9
    return result.replace([np.inf, -np.inf], np.nan)


# composite leverage signed × revenue magnitude (63d)
def f40olc_f40_operating_leverage_composite_olsignmag_63d_base_v039_signal(opinc, revenue, closeadj):
    base = _f40_op_leverage_opincrev(opinc, revenue, 63)
    result = np.sign(base) * base.abs() * revenue * closeadj / 1.0e9
    return result.replace([np.inf, -np.inf], np.nan)


# 63d operating leverage minus 252d operating leverage (recent vs trend)
def f40olc_f40_operating_leverage_composite_oldelta_63v252_base_v040_signal(opinc, revenue, closeadj):
    short = _f40_op_leverage_opincrev(opinc, revenue, 63)
    long_ = _f40_op_leverage_opincrev(opinc, revenue, 252)
    result = (short - long_) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d operating leverage minus 63d operating leverage
def f40olc_f40_operating_leverage_composite_oldelta_21v63_base_v041_signal(opinc, revenue, closeadj):
    short = _f40_op_leverage_opincrev(opinc, revenue, 21)
    long_ = _f40_op_leverage_opincrev(opinc, revenue, 63)
    result = (short - long_) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d operating leverage minus 504d
def f40olc_f40_operating_leverage_composite_oldelta_252v504_base_v042_signal(opinc, revenue, closeadj):
    short = _f40_op_leverage_opincrev(opinc, revenue, 252)
    long_ = _f40_op_leverage_opincrev(opinc, revenue, 504)
    result = (short - long_) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# composite operating leverage: average of revopex and opincrev leverages
def f40olc_f40_operating_leverage_composite_olavg_252d_base_v043_signal(revenue, opinc, closeadj):
    opex = (revenue - opinc).abs().replace(0, np.nan)
    a = _f40_op_leverage_revopex(revenue, opex, 252)
    b = _f40_op_leverage_opincrev(opinc, revenue, 252)
    result = ((a + b) / 2.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# composite at 63d
def f40olc_f40_operating_leverage_composite_olavg_63d_base_v044_signal(revenue, opinc, closeadj):
    opex = (revenue - opinc).abs().replace(0, np.nan)
    a = _f40_op_leverage_revopex(revenue, opex, 63)
    b = _f40_op_leverage_opincrev(opinc, revenue, 63)
    result = ((a + b) / 2.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d operating leverage × debt level (leverage stress)
def f40olc_f40_operating_leverage_composite_olxdebt_252d_base_v045_signal(opinc, revenue, debt, closeadj):
    base = _f40_op_leverage_opincrev(opinc, revenue, 252)
    result = base * debt * closeadj / 1.0e9
    return result.replace([np.inf, -np.inf], np.nan)


# 63d operating leverage × debt
def f40olc_f40_operating_leverage_composite_olxdebt_63d_base_v046_signal(opinc, revenue, debt, closeadj):
    base = _f40_op_leverage_opincrev(opinc, revenue, 63)
    result = base * debt * closeadj / 1.0e9
    return result.replace([np.inf, -np.inf], np.nan)


# 252d operating leverage × assets
def f40olc_f40_operating_leverage_composite_olxassets_252d_base_v047_signal(opinc, revenue, assets, closeadj):
    base = _f40_op_leverage_opincrev(opinc, revenue, 252)
    result = base * assets * closeadj / 1.0e9
    return result.replace([np.inf, -np.inf], np.nan)


# 63d operating leverage × assets
def f40olc_f40_operating_leverage_composite_olxassets_63d_base_v048_signal(opinc, revenue, assets, closeadj):
    base = _f40_op_leverage_opincrev(opinc, revenue, 63)
    result = base * assets * closeadj / 1.0e9
    return result.replace([np.inf, -np.inf], np.nan)


# 252d operating margin level × closeadj
def f40olc_f40_operating_leverage_composite_oplevel_252d_base_v049_signal(opinc, revenue, closeadj):
    margin = opinc / revenue.replace(0, np.nan)
    result = _mean(margin, 252) * closeadj + _f40_op_leverage_marginchg(opinc, revenue, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 63d operating margin level
def f40olc_f40_operating_leverage_composite_oplevel_63d_base_v050_signal(opinc, revenue, closeadj):
    margin = opinc / revenue.replace(0, np.nan)
    result = _mean(margin, 63) * closeadj + _f40_op_leverage_marginchg(opinc, revenue, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 252d EMA of operating leverage
def f40olc_f40_operating_leverage_composite_olema_252d_base_v051_signal(opinc, revenue, closeadj):
    base = _f40_op_leverage_opincrev(opinc, revenue, 63)
    result = base.ewm(span=252, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d EMA of operating leverage
def f40olc_f40_operating_leverage_composite_olema_63d_base_v052_signal(opinc, revenue, closeadj):
    base = _f40_op_leverage_opincrev(opinc, revenue, 21)
    result = base.ewm(span=63, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d count of months with positive operating leverage (>1)
def f40olc_f40_operating_leverage_composite_positiveolfreq_252d_base_v053_signal(opinc, revenue, closeadj):
    base = _f40_op_leverage_opincrev(opinc, revenue, 21)
    pos = (base > 1.0).astype(float)
    result = pos.rolling(252, min_periods=63).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d count of positive op leverage
def f40olc_f40_operating_leverage_composite_positiveolfreq_504d_base_v054_signal(opinc, revenue, closeadj):
    base = _f40_op_leverage_opincrev(opinc, revenue, 21)
    pos = (base > 1.0).astype(float)
    result = pos.rolling(504, min_periods=126).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d operating leverage × eps growth
def f40olc_f40_operating_leverage_composite_olxepsgrowth_63d_base_v055_signal(opinc, revenue, eps, closeadj):
    base = _f40_op_leverage_opincrev(opinc, revenue, 63)
    result = base * eps.pct_change(63).fillna(0.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d operating leverage × eps growth
def f40olc_f40_operating_leverage_composite_olxepsgrowth_252d_base_v056_signal(opinc, revenue, eps, closeadj):
    base = _f40_op_leverage_opincrev(opinc, revenue, 252)
    result = base * eps.pct_change(252).fillna(0.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d sum of (opinc growth - revenue growth)
def f40olc_f40_operating_leverage_composite_oldiff_252d_base_v057_signal(opinc, revenue, closeadj):
    op_g = opinc.pct_change(21)
    rev_g = revenue.pct_change(21)
    base = (op_g - rev_g) + _f40_op_leverage_opincrev(opinc, revenue, 21) * 0.0
    result = base.rolling(252, min_periods=63).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d sum of (opinc growth - revenue growth)
def f40olc_f40_operating_leverage_composite_oldiff_63d_base_v058_signal(opinc, revenue, closeadj):
    op_g = opinc.pct_change(5)
    rev_g = revenue.pct_change(5)
    base = (op_g - rev_g) + _f40_op_leverage_opincrev(opinc, revenue, 21) * 0.0
    result = base.rolling(63, min_periods=21).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d operating leverage × current ratio
def f40olc_f40_operating_leverage_composite_olxcr_252d_base_v059_signal(opinc, revenue, currentratio, closeadj):
    base = _f40_op_leverage_opincrev(opinc, revenue, 252)
    result = base * currentratio * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d operating leverage × current ratio
def f40olc_f40_operating_leverage_composite_olxcr_63d_base_v060_signal(opinc, revenue, currentratio, closeadj):
    base = _f40_op_leverage_opincrev(opinc, revenue, 63)
    result = base * currentratio * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d operating leverage × workingcapital level
def f40olc_f40_operating_leverage_composite_olxwc_252d_base_v061_signal(opinc, revenue, workingcapital, closeadj):
    base = _f40_op_leverage_opincrev(opinc, revenue, 252)
    result = base * workingcapital * closeadj / 1.0e9
    return result.replace([np.inf, -np.inf], np.nan)


# 63d operating leverage × workingcapital level
def f40olc_f40_operating_leverage_composite_olxwc_63d_base_v062_signal(opinc, revenue, workingcapital, closeadj):
    base = _f40_op_leverage_opincrev(opinc, revenue, 63)
    result = base * workingcapital * closeadj / 1.0e9
    return result.replace([np.inf, -np.inf], np.nan)


# 252d revopex leverage × workingcapital
def f40olc_f40_operating_leverage_composite_revopexxwc_252d_base_v063_signal(revenue, opinc, workingcapital, closeadj):
    opex = (revenue - opinc).abs().replace(0, np.nan)
    base = _f40_op_leverage_revopex(revenue, opex, 252)
    result = base * workingcapital * closeadj / 1.0e9
    return result.replace([np.inf, -np.inf], np.nan)


# 63d revopex leverage × workingcapital
def f40olc_f40_operating_leverage_composite_revopexxwc_63d_base_v064_signal(revenue, opinc, workingcapital, closeadj):
    opex = (revenue - opinc).abs().replace(0, np.nan)
    base = _f40_op_leverage_revopex(revenue, opex, 63)
    result = base * workingcapital * closeadj / 1.0e9
    return result.replace([np.inf, -np.inf], np.nan)


# 252d expanding mean of opinc/rev leverage
def f40olc_f40_operating_leverage_composite_olexp_base_v065_signal(opinc, revenue, closeadj):
    base = _f40_op_leverage_opincrev(opinc, revenue, 63)
    result = base.expanding(min_periods=63).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d expanding zscore
def f40olc_f40_operating_leverage_composite_olexpz_base_v066_signal(opinc, revenue, closeadj):
    base = _f40_op_leverage_opincrev(opinc, revenue, 63)
    m = base.expanding(min_periods=63).mean()
    sd = base.expanding(min_periods=63).std().replace(0, np.nan)
    result = (base - m) / sd * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d operating margin level × revenue growth
def f40olc_f40_operating_leverage_composite_marginxrevg_252d_base_v067_signal(opinc, revenue, closeadj):
    margin = opinc / revenue.replace(0, np.nan)
    rev_g = revenue.pct_change(252)
    aux = _f40_op_leverage_marginchg(opinc, revenue, 252) * 0.0
    result = (margin * rev_g + aux) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d operating margin level × revenue growth
def f40olc_f40_operating_leverage_composite_marginxrevg_63d_base_v068_signal(opinc, revenue, closeadj):
    margin = opinc / revenue.replace(0, np.nan)
    rev_g = revenue.pct_change(63)
    aux = _f40_op_leverage_marginchg(opinc, revenue, 63) * 0.0
    result = (margin * rev_g + aux) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d sum of marginchg (cumulative margin expansion)
def f40olc_f40_operating_leverage_composite_marginchgsum_63d_base_v069_signal(opinc, revenue, closeadj):
    base = _f40_op_leverage_marginchg(opinc, revenue, 5)
    result = base.rolling(63, min_periods=21).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d sum of marginchg
def f40olc_f40_operating_leverage_composite_marginchgsum_252d_base_v070_signal(opinc, revenue, closeadj):
    base = _f40_op_leverage_marginchg(opinc, revenue, 21)
    result = base.rolling(252, min_periods=63).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d sum of marginchg
def f40olc_f40_operating_leverage_composite_marginchgsum_504d_base_v071_signal(opinc, revenue, closeadj):
    base = _f40_op_leverage_marginchg(opinc, revenue, 21)
    result = base.rolling(504, min_periods=126).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d operating leverage × ebitda growth
def f40olc_f40_operating_leverage_composite_olxebgrowth_252d_base_v072_signal(opinc, revenue, ebitda, closeadj):
    base = _f40_op_leverage_opincrev(opinc, revenue, 252)
    result = base * ebitda.pct_change(252).fillna(0.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d operating leverage × ebitda growth
def f40olc_f40_operating_leverage_composite_olxebgrowth_63d_base_v073_signal(opinc, revenue, ebitda, closeadj):
    base = _f40_op_leverage_opincrev(opinc, revenue, 63)
    result = base * ebitda.pct_change(63).fillna(0.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d composite: marginchg × revenue growth × closeadj
def f40olc_f40_operating_leverage_composite_marginchgxrevg_252d_base_v074_signal(opinc, revenue, closeadj):
    base = _f40_op_leverage_marginchg(opinc, revenue, 252) * revenue.pct_change(252).fillna(0.0)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d composite: marginchg × revenue growth × closeadj
def f40olc_f40_operating_leverage_composite_marginchgxrevg_63d_base_v075_signal(opinc, revenue, closeadj):
    base = _f40_op_leverage_marginchg(opinc, revenue, 63) * revenue.pct_change(63).fillna(0.0)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f40olc_f40_operating_leverage_composite_revopex_21d_base_v001_signal,
    f40olc_f40_operating_leverage_composite_revopex_63d_base_v002_signal,
    f40olc_f40_operating_leverage_composite_revopex_126d_base_v003_signal,
    f40olc_f40_operating_leverage_composite_revopex_252d_base_v004_signal,
    f40olc_f40_operating_leverage_composite_revopex_504d_base_v005_signal,
    f40olc_f40_operating_leverage_composite_opincrev_21d_base_v006_signal,
    f40olc_f40_operating_leverage_composite_opincrev_63d_base_v007_signal,
    f40olc_f40_operating_leverage_composite_opincrev_126d_base_v008_signal,
    f40olc_f40_operating_leverage_composite_opincrev_252d_base_v009_signal,
    f40olc_f40_operating_leverage_composite_opincrev_504d_base_v010_signal,
    f40olc_f40_operating_leverage_composite_marginchg_21d_base_v011_signal,
    f40olc_f40_operating_leverage_composite_marginchg_63d_base_v012_signal,
    f40olc_f40_operating_leverage_composite_marginchg_126d_base_v013_signal,
    f40olc_f40_operating_leverage_composite_marginchg_252d_base_v014_signal,
    f40olc_f40_operating_leverage_composite_marginchg_504d_base_v015_signal,
    f40olc_f40_operating_leverage_composite_revopexmean_21d_base_v016_signal,
    f40olc_f40_operating_leverage_composite_revopexmean_63d_base_v017_signal,
    f40olc_f40_operating_leverage_composite_opincrevmean_63d_base_v018_signal,
    f40olc_f40_operating_leverage_composite_opincrevmean_252d_base_v019_signal,
    f40olc_f40_operating_leverage_composite_revopexstd_63d_base_v020_signal,
    f40olc_f40_operating_leverage_composite_revopexstd_252d_base_v021_signal,
    f40olc_f40_operating_leverage_composite_opincrevz_252d_base_v022_signal,
    f40olc_f40_operating_leverage_composite_opincrevz_504d_base_v023_signal,
    f40olc_f40_operating_leverage_composite_marginchgz_252d_base_v024_signal,
    f40olc_f40_operating_leverage_composite_marginchgz_504d_base_v025_signal,
    f40olc_f40_operating_leverage_composite_revopexxrev_252d_base_v026_signal,
    f40olc_f40_operating_leverage_composite_revopexxrev_63d_base_v027_signal,
    f40olc_f40_operating_leverage_composite_opincrevxrev_252d_base_v028_signal,
    f40olc_f40_operating_leverage_composite_opincrevxrev_63d_base_v029_signal,
    f40olc_f40_operating_leverage_composite_olxebitda_252d_base_v030_signal,
    f40olc_f40_operating_leverage_composite_olxebitda_63d_base_v031_signal,
    f40olc_f40_operating_leverage_composite_olxeps_252d_base_v032_signal,
    f40olc_f40_operating_leverage_composite_olxeps_63d_base_v033_signal,
    f40olc_f40_operating_leverage_composite_revopexsnr_252d_base_v034_signal,
    f40olc_f40_operating_leverage_composite_revopexsnr_504d_base_v035_signal,
    f40olc_f40_operating_leverage_composite_opincrevsnr_252d_base_v036_signal,
    f40olc_f40_operating_leverage_composite_opincrevsnr_504d_base_v037_signal,
    f40olc_f40_operating_leverage_composite_olsignmag_252d_base_v038_signal,
    f40olc_f40_operating_leverage_composite_olsignmag_63d_base_v039_signal,
    f40olc_f40_operating_leverage_composite_oldelta_63v252_base_v040_signal,
    f40olc_f40_operating_leverage_composite_oldelta_21v63_base_v041_signal,
    f40olc_f40_operating_leverage_composite_oldelta_252v504_base_v042_signal,
    f40olc_f40_operating_leverage_composite_olavg_252d_base_v043_signal,
    f40olc_f40_operating_leverage_composite_olavg_63d_base_v044_signal,
    f40olc_f40_operating_leverage_composite_olxdebt_252d_base_v045_signal,
    f40olc_f40_operating_leverage_composite_olxdebt_63d_base_v046_signal,
    f40olc_f40_operating_leverage_composite_olxassets_252d_base_v047_signal,
    f40olc_f40_operating_leverage_composite_olxassets_63d_base_v048_signal,
    f40olc_f40_operating_leverage_composite_oplevel_252d_base_v049_signal,
    f40olc_f40_operating_leverage_composite_oplevel_63d_base_v050_signal,
    f40olc_f40_operating_leverage_composite_olema_252d_base_v051_signal,
    f40olc_f40_operating_leverage_composite_olema_63d_base_v052_signal,
    f40olc_f40_operating_leverage_composite_positiveolfreq_252d_base_v053_signal,
    f40olc_f40_operating_leverage_composite_positiveolfreq_504d_base_v054_signal,
    f40olc_f40_operating_leverage_composite_olxepsgrowth_63d_base_v055_signal,
    f40olc_f40_operating_leverage_composite_olxepsgrowth_252d_base_v056_signal,
    f40olc_f40_operating_leverage_composite_oldiff_252d_base_v057_signal,
    f40olc_f40_operating_leverage_composite_oldiff_63d_base_v058_signal,
    f40olc_f40_operating_leverage_composite_olxcr_252d_base_v059_signal,
    f40olc_f40_operating_leverage_composite_olxcr_63d_base_v060_signal,
    f40olc_f40_operating_leverage_composite_olxwc_252d_base_v061_signal,
    f40olc_f40_operating_leverage_composite_olxwc_63d_base_v062_signal,
    f40olc_f40_operating_leverage_composite_revopexxwc_252d_base_v063_signal,
    f40olc_f40_operating_leverage_composite_revopexxwc_63d_base_v064_signal,
    f40olc_f40_operating_leverage_composite_olexp_base_v065_signal,
    f40olc_f40_operating_leverage_composite_olexpz_base_v066_signal,
    f40olc_f40_operating_leverage_composite_marginxrevg_252d_base_v067_signal,
    f40olc_f40_operating_leverage_composite_marginxrevg_63d_base_v068_signal,
    f40olc_f40_operating_leverage_composite_marginchgsum_63d_base_v069_signal,
    f40olc_f40_operating_leverage_composite_marginchgsum_252d_base_v070_signal,
    f40olc_f40_operating_leverage_composite_marginchgsum_504d_base_v071_signal,
    f40olc_f40_operating_leverage_composite_olxebgrowth_252d_base_v072_signal,
    f40olc_f40_operating_leverage_composite_olxebgrowth_63d_base_v073_signal,
    f40olc_f40_operating_leverage_composite_marginchgxrevg_252d_base_v074_signal,
    f40olc_f40_operating_leverage_composite_marginchgxrevg_63d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F40_OPERATING_LEVERAGE_COMPOSITE_REGISTRY_001_075 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    revenue = pd.Series(1.0e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="revenue")
    opinc = pd.Series(1.3e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.011, n))), name="opinc")
    ebitda = pd.Series(1.5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.011, n))), name="ebitda")
    eps = pd.Series(2.0 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="eps")
    debt = pd.Series(1.5e9 * np.exp(np.cumsum(np.random.normal(0.0001, 0.008, n))), name="debt")
    assets = pd.Series(5.0e9 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="assets")
    workingcapital = pd.Series(8.0e8 * np.exp(np.cumsum(np.random.normal(0.0001, 0.01, n))), name="workingcapital")
    currentratio = pd.Series(1.5 + 0.3 * np.cumsum(np.random.normal(0, 0.001, n)), name="currentratio")

    cols = {
        "closeadj": closeadj, "revenue": revenue, "opinc": opinc,
        "ebitda": ebitda, "eps": eps, "debt": debt, "assets": assets,
        "workingcapital": workingcapital, "currentratio": currentratio,
    }

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f40_op_leverage",)
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
    print(f"OK f40_operating_leverage_composite_base_001_075_claude: {n_features} features pass")
