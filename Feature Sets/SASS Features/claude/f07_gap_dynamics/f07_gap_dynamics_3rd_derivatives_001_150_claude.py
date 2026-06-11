import inspect
import numpy as np
import pandas as pd

TRADING_DAYS_YEAR = 252
TRADING_DAYS_TWOYEAR = 504
TRADING_DAYS_HALF = 126
TRADING_DAYS_QUARTER = 63
TRADING_DAYS_MONTH = 21
TRADING_DAYS_WEEK = 5


def _z(s, w):
    m = s.rolling(w, min_periods=max(2, w // 2)).mean()
    sd = s.rolling(w, min_periods=max(2, w // 2)).std()
    return (s - m) / sd.replace(0, np.nan)


def _mean(s, w):
    return s.rolling(w, min_periods=max(2, w // 2)).mean()


def _std(s, w):
    return s.rolling(w, min_periods=max(2, w // 2)).std()


def _rank(s, w):
    return s.rolling(w, min_periods=max(2, w // 2)).rank(pct=True) - 0.5


def _roc(s, w):
    # discrete 1st derivative: change of s over w steps (the ROC the spec asks for)
    return s - s.shift(w)


def _gap(openp, close):
    pc = close.shift(1)
    return openp / pc.replace(0, np.nan) - 1.0


def _ovn(openp, close):
    pc = close.shift(1)
    return np.log(openp.replace(0, np.nan) / pc.replace(0, np.nan))


def _intr(openp, close):
    return close / openp.replace(0, np.nan) - 1.0


def _intrlog(openp, close):
    return np.log(close.replace(0, np.nan) / openp.replace(0, np.nan))


def _fill(openp, high, low, close):
    pc = close.shift(1)
    gap = openp - pc
    retrace = np.where(gap > 0, openp - low, high - openp)
    retrace = pd.Series(retrace, index=openp.index)
    return retrace / gap.abs().replace(0, np.nan)


def _tr(high, low, close):
    pc = close.shift(1)
    a = (high - low)
    b = (high - pc).abs()
    c = (low - pc).abs()
    return pd.concat([a, b, c], axis=1).max(axis=1)



def f07gd_f07_gap_dynamics_gaplvl_5d_jerk_v001_signal(open, close):
    core = _mean(_gap(open, close), 5)
    d1 = _roc(core, 5)
    result = _roc(d1, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f07gd_f07_gap_dynamics_gapz_21d_jerk_v002_signal(open, close):
    core = _z(_gap(open, close), 21)
    d1 = _roc(core, 5)
    result = _roc(d1, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f07gd_f07_gap_dynamics_gapz_63d_jerk_v003_signal(open, close):
    core = _z(_gap(open, close), 63)
    d1 = _roc(core, 21)
    result = _roc(d1, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f07gd_f07_gap_dynamics_gapabs_21d_jerk_v004_signal(open, close):
    core = _mean(_gap(open, close).abs(), 21)
    d1 = _roc(core, 5)
    result = _roc(d1, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f07gd_f07_gap_dynamics_gapabs_63d_jerk_v005_signal(open, close):
    core = _mean(_gap(open, close).abs(), 63)
    d1 = _roc(core, 21)
    result = _roc(d1, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f07gd_f07_gap_dynamics_ovn_21d_jerk_v006_signal(open, close):
    o = _ovn(open, close)
    core = _mean(o, 21) - _mean(o, 63)
    d1 = _roc(core, 5)
    result = _roc(d1, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f07gd_f07_gap_dynamics_ovncum_63d_jerk_v007_signal(open, close):
    o = _ovn(open, close); cum = o.cumsum()
    core = cum - cum.rolling(63, min_periods=21).min()
    d1 = _roc(core, 21)
    result = _roc(d1, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f07gd_f07_gap_dynamics_ovncum_252d_jerk_v008_signal(open, close):
    core = _ovn(open, close).rolling(252, min_periods=63).sum()
    d1 = _roc(core, 63)
    result = _roc(d1, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f07gd_f07_gap_dynamics_intr_21d_jerk_v009_signal(open, close):
    core = _mean(_intr(open, close), 21)
    d1 = _roc(core, 5)
    result = _roc(d1, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f07gd_f07_gap_dynamics_intr_63d_jerk_v010_signal(open, close):
    core = _mean(_intr(open, close), 63)
    d1 = _roc(core, 21)
    result = _roc(d1, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f07gd_f07_gap_dynamics_fill_21d_jerk_v011_signal(open, high, low, close):
    core = _mean(_fill(open, high, low, close).clip(-3, 3), 21)
    d1 = _roc(core, 5)
    result = _roc(d1, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f07gd_f07_gap_dynamics_fill_63d_jerk_v012_signal(open, high, low, close):
    core = _mean(_fill(open, high, low, close).clip(-3, 3), 63)
    d1 = _roc(core, 21)
    result = _roc(d1, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f07gd_f07_gap_dynamics_cont_21d_jerk_v013_signal(open, close):
    g = _gap(open, close)
    core = _mean(np.sign(g) * _intr(open, close), 21)
    d1 = _roc(core, 5)
    result = _roc(d1, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f07gd_f07_gap_dynamics_cont_63d_jerk_v014_signal(open, close):
    g = _gap(open, close)
    core = _mean(np.sign(g) * _intr(open, close), 63)
    d1 = _roc(core, 21)
    result = _roc(d1, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f07gd_f07_gap_dynamics_gapdisp_63d_jerk_v015_signal(open, close):
    core = _std(_gap(open, close), 63)
    d1 = _roc(core, 21)
    result = _roc(d1, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f07gd_f07_gap_dynamics_gapdisp_252d_jerk_v016_signal(open, close):
    core = _std(_gap(open, close), 252)
    d1 = _roc(core, 63)
    result = _roc(d1, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f07gd_f07_gap_dynamics_ovnshare_63d_jerk_v017_signal(open, close):
    o = _ovn(open, close).rolling(63, min_periods=21).sum()
    i = _intrlog(open, close).rolling(63, min_periods=21).sum()
    core = o / (o.abs() + i.abs()).replace(0, np.nan)
    d1 = _roc(core, 21)
    result = _roc(d1, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f07gd_f07_gap_dynamics_ovnvsintr_63d_jerk_v018_signal(open, close):
    o = _ovn(open, close); i = _intrlog(open, close)
    core = np.sign(_mean(o, 63)) * np.sign(_mean(i, 63)) * (_mean(o, 63).abs() + _mean(i, 63).abs()) * 1e2
    d1 = _roc(core, 21)
    result = _roc(d1, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f07gd_f07_gap_dynamics_absmag_126d_jerk_v019_signal(open, close):
    core = _mean(_gap(open, close).abs(), 126)
    d1 = _roc(core, 21)
    result = _roc(d1, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f07gd_f07_gap_dynamics_gapmed_126d_jerk_v020_signal(open, close):
    core = _gap(open, close).rolling(126, min_periods=42).median()
    d1 = _roc(core, 21)
    result = _roc(d1, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f07gd_f07_gap_dynamics_gapq75_63d_jerk_v021_signal(open, close):
    core = _gap(open, close).rolling(63, min_periods=21).quantile(0.75)
    d1 = _roc(core, 21)
    result = _roc(d1, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f07gd_f07_gap_dynamics_gapq25_63d_jerk_v022_signal(open, close):
    core = _gap(open, close).rolling(63, min_periods=21).quantile(0.25)
    d1 = _roc(core, 21)
    result = _roc(d1, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f07gd_f07_gap_dynamics_gapiqr_63d_jerk_v023_signal(open, close):
    g = _gap(open, close)
    core = (g.rolling(63, min_periods=21).quantile(0.75)
            - g.rolling(63, min_periods=21).quantile(0.25))
    d1 = _roc(core, 21)
    result = _roc(d1, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f07gd_f07_gap_dynamics_ovnsharpe_63d_jerk_v024_signal(open, close):
    o = _ovn(open, close); i = _intrlog(open, close)
    core = _std(o, 63) / _std(i, 63).replace(0, np.nan)
    d1 = _roc(core, 21)
    result = _roc(d1, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f07gd_f07_gap_dynamics_intrsharpe_63d_jerk_v025_signal(open, close):
    core = _intr(open, close).rolling(63, min_periods=21).skew()
    d1 = _roc(core, 21)
    result = _roc(d1, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f07gd_f07_gap_dynamics_gapskew_126d_jerk_v026_signal(open, close):
    core = _gap(open, close).rolling(126, min_periods=42).skew()
    d1 = _roc(core, 21)
    result = _roc(d1, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f07gd_f07_gap_dynamics_gapkurt_126d_jerk_v027_signal(open, close):
    core = _gap(open, close).rolling(126, min_periods=42).kurt()
    d1 = _roc(core, 21)
    result = _roc(d1, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f07gd_f07_gap_dynamics_ovnvol_21d_jerk_v028_signal(open, close):
    core = _std(_ovn(open, close), 21)
    d1 = _roc(core, 5)
    result = _roc(d1, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f07gd_f07_gap_dynamics_gapewm_21d_jerk_v029_signal(open, close):
    core = _gap(open, close).ewm(span=21, min_periods=10).mean()
    d1 = _roc(core, 5)
    result = _roc(d1, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f07gd_f07_gap_dynamics_signmag_21d_jerk_v030_signal(open, close):
    g = _gap(open, close)
    core = _mean(np.sign(g) * np.sqrt(g.abs()), 21)
    d1 = _roc(core, 5)
    result = _roc(d1, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f07gd_f07_gap_dynamics_gapatr_63d_jerk_v031_signal(open, high, low, close):
    g = (open - close.shift(1))
    core = _z(g / _tr(high, low, close).replace(0, np.nan), 63)
    d1 = _roc(core, 21)
    result = _roc(d1, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f07gd_f07_gap_dynamics_openloc_63d_jerk_v032_signal(open, high, low, close):
    pc = close.shift(1)
    rng = (high - low).replace(0, np.nan)
    core = _mean((open - pc) / rng, 63)
    d1 = _roc(core, 21)
    result = _roc(d1, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f07gd_f07_gap_dynamics_revstr_21d_jerk_v033_signal(open, close):
    g = _gap(open, close)
    core = _mean((-np.sign(g) * _intr(open, close)).clip(lower=0), 21)
    d1 = _roc(core, 5)
    result = _roc(d1, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f07gd_f07_gap_dynamics_revstr_126d_jerk_v034_signal(open, close):
    g = _gap(open, close)
    core = _mean((-np.sign(g) * _intr(open, close)).clip(lower=0), 126)
    d1 = _roc(core, 21)
    result = _roc(d1, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f07gd_f07_gap_dynamics_gapmotion_63d_jerk_v035_signal(open, close):
    core = _mean(_gap(open, close).abs(), 63) / _mean(_intr(open, close).abs(), 63).replace(0, np.nan)
    d1 = _roc(core, 21)
    result = _roc(d1, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f07gd_f07_gap_dynamics_varfrac_252d_jerk_v036_signal(open, close):
    o = _ovn(open, close); i = _intrlog(open, close)
    vo = o.rolling(252, min_periods=63).var()
    vi = i.rolling(252, min_periods=63).var()
    core = vo / (vo + vi).replace(0, np.nan)
    d1 = _roc(core, 63)
    result = _roc(d1, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f07gd_f07_gap_dynamics_gapvolr_63d_jerk_v037_signal(open, close):
    g = _gap(open, close)
    core = _std(g, 21) / _std(g, 126).replace(0, np.nan)
    d1 = _roc(core, 21)
    result = _roc(d1, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f07gd_f07_gap_dynamics_ovneff_63d_jerk_v038_signal(open, close):
    o = _ovn(open, close)
    core = (o.clip(upper=0) ** 2).rolling(63, min_periods=21).mean() / (o.clip(lower=0) ** 2).rolling(63, min_periods=21).mean().replace(0, np.nan)
    d1 = _roc(core, 21)
    result = _roc(d1, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f07gd_f07_gap_dynamics_gapconsist_63d_jerk_v039_signal(open, close):
    g = _gap(open, close)
    core = _mean(g, 63).abs() / _std(g, 63).replace(0, np.nan)
    d1 = _roc(core, 21)
    result = _roc(d1, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f07gd_f07_gap_dynamics_ovnconc_63d_jerk_v040_signal(open, close):
    o = _ovn(open, close).abs()
    core = o.rolling(63, min_periods=21).max() / o.rolling(63, min_periods=21).sum().replace(0, np.nan)
    d1 = _roc(core, 21)
    result = _roc(d1, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f07gd_f07_gap_dynamics_gapenergy_63d_jerk_v041_signal(open, close):
    g = _gap(open, close)
    core = (np.sign(g) * g ** 2).rolling(63, min_periods=21).sum() * 1e4
    d1 = _roc(core, 21)
    result = _roc(d1, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f07gd_f07_gap_dynamics_triangle_63d_jerk_v042_signal(open, high, low, close):
    ph = high.shift(1); pl = low.shift(1)
    net = ((open - ph).clip(lower=0) - (pl - open).clip(lower=0)) / close.shift(1).replace(0, np.nan)
    core = _mean(net, 63) * 1e2
    d1 = _roc(core, 21)
    result = _roc(d1, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f07gd_f07_gap_dynamics_gaprngfrac_63d_jerk_v043_signal(open, high, low, close):
    pc = close.shift(1)
    lo = pd.concat([low, pc], axis=1).min(axis=1)
    hi = pd.concat([high, pc], axis=1).max(axis=1)
    core = _std((open - pc) / (hi - lo).replace(0, np.nan), 63)
    d1 = _roc(core, 21)
    result = _roc(d1, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f07gd_f07_gap_dynamics_gapvolterm_63d_jerk_v044_signal(open, close):
    g = _gap(open, close)
    core = _std(g, 5) - _std(g, 63)
    d1 = _roc(core, 21)
    result = _roc(d1, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f07gd_f07_gap_dynamics_ovncomp_42d_jerk_v045_signal(open, close):
    o = _ovn(open, close)
    core = o.ewm(span=10, min_periods=5).mean() - o.ewm(span=63, min_periods=21).mean()
    d1 = _roc(core, 5)
    result = _roc(d1, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f07gd_f07_gap_dynamics_gapvov_63d_jerk_v046_signal(open, close):
    core = _std(_std(_gap(open, close), 10), 63)
    d1 = _roc(core, 21)
    result = _roc(d1, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f07gd_f07_gap_dynamics_gapmotion2_126d_jerk_v047_signal(open, high, low, close):
    g = _gap(open, close).abs()
    rng = (high - low) / close.replace(0, np.nan)
    core = _mean(g, 126) / _mean(rng, 126).replace(0, np.nan)
    d1 = _roc(core, 21)
    result = _roc(d1, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f07gd_f07_gap_dynamics_uptail_63d_jerk_v048_signal(open, close):
    g = _gap(open, close)
    q = g.rolling(63, min_periods=21).quantile(0.75)
    core = _mean((g - q).clip(lower=0), 63) * 1e2
    d1 = _roc(core, 21)
    result = _roc(d1, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f07gd_f07_gap_dynamics_lotail_63d_jerk_v049_signal(open, close):
    g = _gap(open, close)
    q = g.rolling(63, min_periods=21).quantile(0.25)
    core = _mean((q - g).clip(lower=0), 63) * 1e2
    d1 = _roc(core, 21)
    result = _roc(d1, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f07gd_f07_gap_dynamics_ovndrift_126d_jerk_v050_signal(open, close):
    o = _ovn(open, close); i = _intrlog(open, close)
    core = o.rolling(126, min_periods=42).sum() / (o.abs() + i.abs()).rolling(126, min_periods=42).sum().replace(0, np.nan)
    d1 = _roc(core, 21)
    result = _roc(d1, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f07gd_f07_gap_dynamics_gaplvl_21d_jerk_v051_signal(open, close):
    core = _mean(_gap(open, close), 21)
    d1 = _roc(core, 5)
    result = _roc(d1, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f07gd_f07_gap_dynamics_gaplvl_63d_jerk_v052_signal(open, close):
    core = _mean(_gap(open, close), 63)
    d1 = _roc(core, 21)
    result = _roc(d1, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f07gd_f07_gap_dynamics_wfill_126d_jerk_v053_signal(open, high, low, close):
    g = _gap(open, close); f = _fill(open, high, low, close).clip(-3, 3)
    w = g.abs()
    core = (f * w).rolling(126, min_periods=42).sum() / w.rolling(126, min_periods=42).sum().replace(0, np.nan)
    d1 = _roc(core, 21)
    result = _roc(d1, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f07gd_f07_gap_dynamics_ovnpremium_252d_jerk_v054_signal(open, close):
    o = _ovn(open, close); i = _intrlog(open, close)
    core = o.rolling(252, min_periods=63).sum() - i.rolling(252, min_periods=63).sum()
    d1 = _roc(core, 63)
    result = _roc(d1, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f07gd_f07_gap_dynamics_contmag_63d_jerk_v055_signal(open, close):
    g = _gap(open, close)
    core = _mean(np.sign(g) * _intr(open, close) * g.abs(), 63) * 1e3
    d1 = _roc(core, 21)
    result = _roc(d1, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f07gd_f07_gap_dynamics_polarity_63d_jerk_v056_signal(open, close):
    core = np.sign(_gap(open, close)).ewm(span=42, min_periods=21).mean()
    d1 = _roc(core, 21)
    result = _roc(d1, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f07gd_f07_gap_dynamics_gapmed_63d_jerk_v057_signal(open, close):
    core = _gap(open, close).rolling(63, min_periods=21).median()
    d1 = _roc(core, 21)
    result = _roc(d1, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f07gd_f07_gap_dynamics_fillewm_42d_jerk_v058_signal(open, high, low, close):
    core = _fill(open, high, low, close).clip(-3, 3).ewm(span=42, min_periods=21).mean()
    d1 = _roc(core, 5)
    result = _roc(d1, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f07gd_f07_gap_dynamics_absmag_252d_jerk_v059_signal(open, close):
    core = _mean(_gap(open, close).abs(), 252)
    d1 = _roc(core, 63)
    result = _roc(d1, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f07gd_f07_gap_dynamics_ovnvol_63d_jerk_v060_signal(open, high, low, close):
    o = _ovn(open, close); rng = (high - low) / close.replace(0, np.nan)
    core = _std(o, 63) - _std(rng, 63)
    d1 = _roc(core, 21)
    result = _roc(d1, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f07gd_f07_gap_dynamics_intrvol_63d_jerk_v061_signal(open, close):
    core = _std(_intr(open, close), 63)
    d1 = _roc(core, 21)
    result = _roc(d1, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f07gd_f07_gap_dynamics_gapskew_252d_jerk_v062_signal(open, close):
    core = _gap(open, close).rolling(252, min_periods=63).skew()
    d1 = _roc(core, 63)
    result = _roc(d1, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f07gd_f07_gap_dynamics_ovndd_252d_jerk_v063_signal(open, close):
    o = _ovn(open, close); cum = o.cumsum()
    core = cum - cum.rolling(252, min_periods=63).max()
    d1 = _roc(core, 63)
    result = _roc(d1, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f07gd_f07_gap_dynamics_gapmom_21d_jerk_v064_signal(open, close):
    g = _mean(_gap(open, close), 21)
    core = g - g.shift(21)
    d1 = _roc(core, 5)
    result = _roc(d1, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f07gd_f07_gap_dynamics_ovnwin_63d_jerk_v065_signal(open, close):
    o = _ovn(open, close); i = _intrlog(open, close)
    core = (o > 0).astype(float).ewm(span=63, min_periods=21).mean() - (i > 0).astype(float).ewm(span=63, min_periods=21).mean()
    d1 = _roc(core, 21)
    result = _roc(d1, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f07gd_f07_gap_dynamics_gaprank_252d_jerk_v066_signal(open, close):
    core = _rank(_gap(open, close).abs(), 252)
    d1 = _roc(core, 63)
    result = _roc(d1, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f07gd_f07_gap_dynamics_ovncalmar_126d_jerk_v067_signal(open, close):
    o = _ovn(open, close); cum = o.cumsum()
    maxdd = (cum - cum.rolling(126, min_periods=42).max()).rolling(126, min_periods=42).min().abs()
    core = o.rolling(126, min_periods=42).sum() / maxdd.replace(0, np.nan)
    d1 = _roc(core, 21)
    result = _roc(d1, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f07gd_f07_gap_dynamics_taildns_252d_jerk_v068_signal(open, close):
    g = _gap(open, close).abs()
    core = g.rolling(252, min_periods=63).quantile(0.95) / g.rolling(252, min_periods=63).quantile(0.50).replace(0, np.nan)
    d1 = _roc(core, 63)
    result = _roc(d1, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f07gd_f07_gap_dynamics_gapatr_5d_jerk_v069_signal(open, high, low, close):
    g = (open - close.shift(1))
    core = _mean(g / _tr(high, low, close).replace(0, np.nan), 5)
    d1 = _roc(core, 5)
    result = _roc(d1, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f07gd_f07_gap_dynamics_ovnskew_126d_jerk_v070_signal(open, close):
    o = _ovn(open, close); i = _intrlog(open, close)
    core = o.rolling(126, min_periods=42).skew() - i.rolling(126, min_periods=42).skew()
    d1 = _roc(core, 21)
    result = _roc(d1, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f07gd_f07_gap_dynamics_gapvolexp_21d_jerk_v071_signal(open, close):
    g = _gap(open, close).abs()
    core = g.ewm(span=10, min_periods=5).mean() / g.ewm(span=63, min_periods=21).mean().replace(0, np.nan) - 1.0
    d1 = _roc(core, 5)
    result = _roc(d1, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f07gd_f07_gap_dynamics_gapztanh_63d_jerk_v072_signal(open, close):
    core = np.tanh(_z(_gap(open, close), 63)).ewm(span=10, min_periods=5).mean()
    d1 = _roc(core, 21)
    result = _roc(d1, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f07gd_f07_gap_dynamics_dirbias_63d_jerk_v073_signal(open, close):
    g = _gap(open, close)
    core = ((g > 0.002).astype(float) - (g < -0.002).astype(float)).rolling(63, min_periods=21).mean() + 8.0 * _mean(g, 63)
    d1 = _roc(core, 21)
    result = _roc(d1, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f07gd_f07_gap_dynamics_gaprng_126d_jerk_v074_signal(open, high, low, close):
    g = (open - close.shift(1))
    core = _rank(g / _tr(high, low, close).replace(0, np.nan), 126)
    d1 = _roc(core, 21)
    result = _roc(d1, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f07gd_f07_gap_dynamics_ovnrank_252d_jerk_v075_signal(open, close):
    core = _rank(_ovn(open, close).rolling(21, min_periods=10).sum(), 252)
    d1 = _roc(core, 63)
    result = _roc(d1, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f07gd_f07_gap_dynamics_gapdz_63d_jerk_v076_signal(open, close):
    gm = _mean(_gap(open, close), 21)
    core = gm - gm.ewm(span=63, min_periods=21).mean()
    d1 = _roc(core, 21)
    result = _roc(d1, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f07gd_f07_gap_dynamics_ovndisp_126d_jerk_v077_signal(open, close):
    o = _ovn(open, close); i = _intrlog(open, close)
    om = _mean(o, 21) - _mean(i, 21)
    core = om - om.ewm(span=126, min_periods=42).mean()
    d1 = _roc(core, 21)
    result = _roc(d1, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f07gd_f07_gap_dynamics_contdz_63d_jerk_v078_signal(open, close):
    g = _gap(open, close); c = np.sign(g) * _intr(open, close)
    cm = _mean(c, 21)
    core = cm - cm.ewm(span=63, min_periods=21).mean()
    d1 = _roc(core, 21)
    result = _roc(d1, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f07gd_f07_gap_dynamics_filldz_63d_jerk_v079_signal(open, high, low, close):
    f = _mean(_fill(open, high, low, close).clip(-3, 3), 21)
    core = f - f.ewm(span=63, min_periods=21).mean()
    d1 = _roc(core, 21)
    result = _roc(d1, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f07gd_f07_gap_dynamics_gapabsz_126d_jerk_v080_signal(open, close):
    core = _z(_gap(open, close).abs(), 126)
    d1 = _roc(core, 21)
    result = _roc(d1, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f07gd_f07_gap_dynamics_ovnz_63d_jerk_v081_signal(open, close):
    core = _z(_ovn(open, close).rolling(21, min_periods=10).sum(), 63)
    d1 = _roc(core, 21)
    result = _roc(d1, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f07gd_f07_gap_dynamics_intrz_63d_jerk_v082_signal(open, close):
    core = _z(_intr(open, close), 63)
    d1 = _roc(core, 21)
    result = _roc(d1, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f07gd_f07_gap_dynamics_gapacf_126d_jerk_v083_signal(open, close):
    g = _gap(open, close); gm = g - _mean(g, 126)
    core = (gm * gm.shift(1)).rolling(126, min_periods=42).mean() / (gm ** 2).rolling(126, min_periods=42).mean().replace(0, np.nan)
    d1 = _roc(core, 21)
    result = _roc(d1, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f07gd_f07_gap_dynamics_ovnac_126d_jerk_v084_signal(open, close):
    o = _ovn(open, close); om = o - _mean(o, 126)
    core = (om * om.shift(2)).rolling(126, min_periods=42).mean() / (om ** 2).rolling(126, min_periods=42).mean().replace(0, np.nan)
    d1 = _roc(core, 21)
    result = _roc(d1, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f07gd_f07_gap_dynamics_gapclust_63d_jerk_v085_signal(open, close):
    g = _gap(open, close).abs(); gm = g - _mean(g, 63)
    core = (gm * gm.shift(1)).rolling(63, min_periods=21).mean() / (gm ** 2).rolling(63, min_periods=21).mean().replace(0, np.nan)
    d1 = _roc(core, 21)
    result = _roc(d1, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f07gd_f07_gap_dynamics_ovnsemi_126d_jerk_v086_signal(open, close):
    o = _ovn(open, close)
    core = (o.clip(upper=0) ** 2).rolling(126, min_periods=42).mean() / (o.clip(lower=0) ** 2).rolling(126, min_periods=42).mean().replace(0, np.nan)
    d1 = _roc(core, 21)
    result = _roc(d1, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f07gd_f07_gap_dynamics_gapprc_252d_jerk_v087_signal(open, close):
    core = _gap(open, close).rolling(252, min_periods=63).quantile(0.9)
    d1 = _roc(core, 63)
    result = _roc(d1, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f07gd_f07_gap_dynamics_gapprc10_252d_jerk_v088_signal(open, close):
    core = _gap(open, close).rolling(252, min_periods=63).quantile(0.1)
    d1 = _roc(core, 63)
    result = _roc(d1, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f07gd_f07_gap_dynamics_ovntrend_126d_jerk_v089_signal(open, close):
    o = _ovn(open, close); cum = o.cumsum()
    core = cum - cum.shift(21)
    d1 = _roc(core, 21)
    result = _roc(d1, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f07gd_f07_gap_dynamics_gaprat_63d_jerk_v090_signal(open, close):
    g = _gap(open, close)
    core = _mean(g.clip(lower=0), 63) / (-_mean(g.clip(upper=0), 63)).replace(0, np.nan)
    d1 = _roc(core, 21)
    result = _roc(d1, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f07gd_f07_gap_dynamics_ovncorr_126d_jerk_v091_signal(open, close):
    o = _ovn(open, close); i = _intrlog(open, close).shift(1)
    core = o.rolling(126, min_periods=42).corr(i)
    d1 = _roc(core, 21)
    result = _roc(d1, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f07gd_f07_gap_dynamics_gapcorr_126d_jerk_v092_signal(open, high, low, close):
    g = _gap(open, close).abs(); rng = (high - low) / close.replace(0, np.nan)
    core = g.rolling(126, min_periods=42).corr(rng)
    d1 = _roc(core, 21)
    result = _roc(d1, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f07gd_f07_gap_dynamics_fillrat_126d_jerk_v093_signal(open, high, low, close):
    f = _fill(open, high, low, close).clip(-3, 3)
    core = (f > 0.5).astype(float).ewm(span=63, min_periods=21).mean() - 0.5
    d1 = _roc(core, 21)
    result = _roc(d1, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f07gd_f07_gap_dynamics_ovnwm_252d_jerk_v094_signal(open, close):
    o = _ovn(open, close)
    core = (o > 0).astype(float).ewm(span=126, min_periods=42).mean() - 0.5
    d1 = _roc(core, 63)
    result = _roc(d1, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f07gd_f07_gap_dynamics_gapsd_63d_jerk_v095_signal(open, close):
    g = _gap(open, close)
    core = (g - g.rolling(63, min_periods=21).median()).abs().rolling(63, min_periods=21).median()
    d1 = _roc(core, 21)
    result = _roc(d1, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f07gd_f07_gap_dynamics_ovncum2_126d_jerk_v096_signal(open, close):
    o = _ovn(open, close); cum = o.cumsum()
    core = cum - cum.rolling(126, min_periods=42).mean()
    d1 = _roc(core, 21)
    result = _roc(d1, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f07gd_f07_gap_dynamics_intrcum_126d_jerk_v097_signal(open, close):
    core = _intrlog(open, close).rolling(126, min_periods=42).sum()
    d1 = _roc(core, 21)
    result = _roc(d1, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f07gd_f07_gap_dynamics_gapmag_5d_jerk_v098_signal(open, close):
    core = _mean(_gap(open, close).abs(), 5)
    d1 = _roc(core, 5)
    result = _roc(d1, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f07gd_f07_gap_dynamics_ovn5_5d_jerk_v099_signal(open, close):
    o = _ovn(open, close); i = _intrlog(open, close)
    core = _mean(o, 5) - _mean(i, 5)
    d1 = _roc(core, 5)
    result = _roc(d1, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f07gd_f07_gap_dynamics_intr5_5d_jerk_v100_signal(open, high, low, close):
    rng = (high - low) / close.replace(0, np.nan)
    core = _mean(rng, 5)
    d1 = _roc(core, 5)
    result = _roc(d1, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f07gd_f07_gap_dynamics_cont5_5d_jerk_v101_signal(open, close):
    g = _gap(open, close)
    core = _mean(np.sign(g) * _intr(open, close), 5)
    d1 = _roc(core, 5)
    result = _roc(d1, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f07gd_f07_gap_dynamics_fill5_5d_jerk_v102_signal(open, high, low, close):
    core = _mean(_fill(open, high, low, close).clip(-3, 3), 5)
    d1 = _roc(core, 5)
    result = _roc(d1, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f07gd_f07_gap_dynamics_gapwk_5d_jerk_v103_signal(open, close):
    g = _gap(open, close)
    core = g.rolling(5, min_periods=3).max() - g.rolling(5, min_periods=3).min()
    d1 = _roc(core, 5)
    result = _roc(d1, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f07gd_f07_gap_dynamics_ovnwk_5d_jerk_v104_signal(open, high, low, close):
    f = _fill(open, high, low, close).clip(-3, 3)
    core = _std(f, 5)
    d1 = _roc(core, 5)
    result = _roc(d1, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f07gd_f07_gap_dynamics_gapsignwk_5d_jerk_v105_signal(open, close):
    g = _gap(open, close)
    core = (np.sign(g) * np.sqrt(g.abs())).rolling(5, min_periods=3).mean()
    d1 = _roc(core, 5)
    result = _roc(d1, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f07gd_f07_gap_dynamics_gaplo_21d_jerk_v106_signal(open, close):
    g = _gap(open, close)
    core = _mean(g.clip(upper=0), 21)
    d1 = _roc(core, 5)
    result = _roc(d1, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f07gd_f07_gap_dynamics_gaphi_21d_jerk_v107_signal(open, close):
    g = _gap(open, close)
    core = _mean(g.clip(lower=0), 21)
    d1 = _roc(core, 5)
    result = _roc(d1, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f07gd_f07_gap_dynamics_ovnup_63d_jerk_v108_signal(open, close):
    o = _ovn(open, close)
    core = o.clip(lower=0).rolling(63, min_periods=21).sum()
    d1 = _roc(core, 21)
    result = _roc(d1, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f07gd_f07_gap_dynamics_ovndn_63d_jerk_v109_signal(open, close):
    o = _ovn(open, close)
    core = (-o.clip(upper=0)).rolling(63, min_periods=21).sum()
    d1 = _roc(core, 21)
    result = _roc(d1, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f07gd_f07_gap_dynamics_gapxvol_63d_jerk_v110_signal(open, close):
    g = _gap(open, close)
    core = _std(g, 63) * np.sign(_mean(g, 63))
    d1 = _roc(core, 21)
    result = _roc(d1, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f07gd_f07_gap_dynamics_ovnxintr_63d_jerk_v111_signal(open, close):
    o = _ovn(open, close); i = _intrlog(open, close)
    core = o.rolling(63, min_periods=21).corr(i)
    d1 = _roc(core, 21)
    result = _roc(d1, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f07gd_f07_gap_dynamics_gapmom2_63d_jerk_v112_signal(open, close):
    g = _mean(_gap(open, close), 21)
    core = g - g.shift(63)
    d1 = _roc(core, 21)
    result = _roc(d1, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f07gd_f07_gap_dynamics_ovnmom_63d_jerk_v113_signal(open, close):
    o = _ovn(open, close).rolling(63, min_periods=21).sum()
    core = o - o.shift(63)
    d1 = _roc(core, 21)
    result = _roc(d1, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f07gd_f07_gap_dynamics_contmom_63d_jerk_v114_signal(open, close):
    g = _gap(open, close); c = _mean(np.sign(g) * _intr(open, close), 21)
    core = c - c.shift(63)
    d1 = _roc(core, 21)
    result = _roc(d1, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f07gd_f07_gap_dynamics_fillmom_63d_jerk_v115_signal(open, high, low, close):
    f = _mean(_fill(open, high, low, close).clip(-3, 3), 21)
    core = f - f.shift(63)
    d1 = _roc(core, 21)
    result = _roc(d1, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f07gd_f07_gap_dynamics_gapsq_63d_jerk_v116_signal(open, close):
    g = _gap(open, close)
    core = _mean(np.sign(g) * np.sqrt(g.abs()), 63) - np.sign(_mean(g, 63)) * np.sqrt(_mean(g, 63).abs())
    d1 = _roc(core, 21)
    result = _roc(d1, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f07gd_f07_gap_dynamics_ovnsq_63d_jerk_v117_signal(open, close):
    o = _ovn(open, close); i = _intrlog(open, close)
    core = _mean(np.sign(o) * np.sqrt(o.abs()), 63) - _mean(np.sign(i) * np.sqrt(i.abs()), 63)
    d1 = _roc(core, 21)
    result = _roc(d1, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f07gd_f07_gap_dynamics_gapfold_63d_jerk_v118_signal(open, close):
    g = _gap(open, close)
    core = _mean((g - _mean(g, 63)).abs(), 63) / _std(g, 63).replace(0, np.nan)
    d1 = _roc(core, 21)
    result = _roc(d1, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f07gd_f07_gap_dynamics_ovnfold_63d_jerk_v119_signal(open, close):
    o = _ovn(open, close); i = _intrlog(open, close)
    core = _mean((o - _mean(o, 63)).abs(), 63) - _mean((i - _mean(i, 63)).abs(), 63)
    d1 = _roc(core, 21)
    result = _roc(d1, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f07gd_f07_gap_dynamics_gaprr_252d_jerk_v120_signal(open, close):
    g = _gap(open, close).abs()
    core = g.rolling(252, min_periods=63).quantile(0.99) - g.rolling(252, min_periods=63).quantile(0.80)
    d1 = _roc(core, 63)
    result = _roc(d1, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f07gd_f07_gap_dynamics_ovnrr_252d_jerk_v121_signal(open, close):
    o = _ovn(open, close).abs()
    core = o.rolling(252, min_periods=63).quantile(0.9) / o.rolling(252, min_periods=63).quantile(0.5).replace(0, np.nan)
    d1 = _roc(core, 63)
    result = _roc(d1, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f07gd_f07_gap_dynamics_gapcv_126d_jerk_v122_signal(open, close):
    g = _gap(open, close)
    core = _std(g, 126) / _mean(g.abs(), 126).replace(0, np.nan)
    d1 = _roc(core, 21)
    result = _roc(d1, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f07gd_f07_gap_dynamics_ovncv_126d_jerk_v123_signal(open, high, low, close):
    o = _ovn(open, close); rng = (high - low) / close.replace(0, np.nan)
    core = _std(o, 126) / _mean(rng, 126).replace(0, np.nan)
    d1 = _roc(core, 21)
    result = _roc(d1, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f07gd_f07_gap_dynamics_gapxrng_63d_jerk_v124_signal(open, high, low, close):
    g = _gap(open, close).abs(); tr = _tr(high, low, close) / close.shift(1).replace(0, np.nan)
    core = _mean(g, 63) / _mean(tr, 63).replace(0, np.nan)
    d1 = _roc(core, 21)
    result = _roc(d1, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f07gd_f07_gap_dynamics_openlocz_63d_jerk_v125_signal(open, high, low, close):
    pc = close.shift(1); rng = (high - low).replace(0, np.nan)
    core = ((open - pc) / rng).rolling(63, min_periods=21).skew()
    d1 = _roc(core, 21)
    result = _roc(d1, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f07gd_f07_gap_dynamics_gapskewq_63d_jerk_v126_signal(open, close):
    core = _gap(open, close).rolling(63, min_periods=21).skew()
    d1 = _roc(core, 21)
    result = _roc(d1, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f07gd_f07_gap_dynamics_ovnskewq_63d_jerk_v127_signal(open, high, low, close):
    o = _ovn(open, close); rng = (high - low) / close.replace(0, np.nan)
    core = o.rolling(63, min_periods=21).skew() - rng.rolling(63, min_periods=21).skew()
    d1 = _roc(core, 21)
    result = _roc(d1, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f07gd_f07_gap_dynamics_intrskew_126d_jerk_v128_signal(open, close):
    core = _intr(open, close).rolling(126, min_periods=42).skew()
    d1 = _roc(core, 21)
    result = _roc(d1, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f07gd_f07_gap_dynamics_gapkurtq_63d_jerk_v129_signal(open, close):
    core = _gap(open, close).rolling(63, min_periods=21).kurt()
    d1 = _roc(core, 21)
    result = _roc(d1, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f07gd_f07_gap_dynamics_gapewmL_63d_jerk_v130_signal(open, close):
    core = _gap(open, close).ewm(span=63, min_periods=21).mean()
    d1 = _roc(core, 21)
    result = _roc(d1, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f07gd_f07_gap_dynamics_ovnewm_21d_jerk_v131_signal(open, close):
    o = _ovn(open, close); i = _intrlog(open, close)
    core = o.ewm(span=21, min_periods=10).mean() - i.ewm(span=21, min_periods=10).mean()
    d1 = _roc(core, 5)
    result = _roc(d1, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f07gd_f07_gap_dynamics_contewmL_63d_jerk_v132_signal(open, close):
    g = _gap(open, close)
    core = (np.sign(g) * _intr(open, close)).ewm(span=42, min_periods=21).mean()
    d1 = _roc(core, 21)
    result = _roc(d1, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f07gd_f07_gap_dynamics_gapprctl_126d_jerk_v133_signal(open, close):
    core = _rank(_gap(open, close).abs(), 126)
    d1 = _roc(core, 21)
    result = _roc(d1, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f07gd_f07_gap_dynamics_ovnprctl_126d_jerk_v134_signal(open, close):
    core = _rank(_ovn(open, close).rolling(21, min_periods=10).sum(), 126)
    d1 = _roc(core, 21)
    result = _roc(d1, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f07gd_f07_gap_dynamics_gapwin_126d_jerk_v135_signal(open, close):
    g = _gap(open, close)
    core = (g > 0).astype(float).ewm(span=126, min_periods=42).mean() - 0.5
    d1 = _roc(core, 21)
    result = _roc(d1, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f07gd_f07_gap_dynamics_ovnentropy_63d_jerk_v136_signal(open, close):
    o = _ovn(open, close); p = (o > 0).astype(float).ewm(span=63, min_periods=21).mean().clip(1e-6, 1 - 1e-6)
    core = -(p * np.log(p) + (1 - p) * np.log(1 - p))
    d1 = _roc(core, 21)
    result = _roc(d1, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f07gd_f07_gap_dynamics_gapextend_63d_jerk_v137_signal(open, close):
    g = _gap(open, close); i = _intr(open, close)
    core = _mean((i / g.abs().replace(0, np.nan)).clip(-5, 5), 63)
    d1 = _roc(core, 21)
    result = _roc(d1, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f07gd_f07_gap_dynamics_ovnbeta2_126d_jerk_v138_signal(open, close):
    i = _intr(open, close); o = _ovn(open, close).shift(1)
    cov = (i * o).rolling(126, min_periods=42).mean() - _mean(i, 126) * _mean(o, 126)
    core = cov / o.rolling(126, min_periods=42).var().replace(0, np.nan)
    d1 = _roc(core, 21)
    result = _roc(d1, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f07gd_f07_gap_dynamics_intrbeta2_126d_jerk_v139_signal(open, close):
    g = _gap(open, close); i = _intr(open, close)
    cov = (g * i).rolling(126, min_periods=42).mean() - _mean(g, 126) * _mean(i, 126)
    core = cov / g.rolling(126, min_periods=42).var().replace(0, np.nan)
    d1 = _roc(core, 21)
    result = _roc(d1, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f07gd_f07_gap_dynamics_gapddnorm_252d_jerk_v140_signal(open, close):
    o = _ovn(open, close); cum = o.cumsum()
    dd = cum - cum.rolling(252, min_periods=63).max()
    core = dd.rolling(252, min_periods=63).min() - dd
    d1 = _roc(core, 63)
    result = _roc(d1, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f07gd_f07_gap_dynamics_gapenergyL_126d_jerk_v141_signal(open, close):
    g = _gap(open, close)
    core = (np.sign(g) * g ** 2).rolling(126, min_periods=42).sum() * 1e4
    d1 = _roc(core, 21)
    result = _roc(d1, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f07gd_f07_gap_dynamics_revmag2_63d_jerk_v142_signal(open, close):
    g = _gap(open, close); i = _intr(open, close)
    core = _mean((-np.sign(g) * i).clip(lower=0), 63) * 1e2
    d1 = _roc(core, 21)
    result = _roc(d1, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f07gd_f07_gap_dynamics_gapfillw_63d_jerk_v143_signal(open, high, low, close):
    g = _gap(open, close); f = _fill(open, high, low, close).clip(-3, 3); w = g.abs()
    core = (f * w).rolling(63, min_periods=21).sum() / w.rolling(63, min_periods=21).sum().replace(0, np.nan)
    d1 = _roc(core, 21)
    result = _roc(d1, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f07gd_f07_gap_dynamics_gapqs_63d_jerk_v144_signal(open, close):
    g = _gap(open, close)
    core = (g.rolling(63, min_periods=21).quantile(0.9) + g.rolling(63, min_periods=21).quantile(0.1))
    d1 = _roc(core, 21)
    result = _roc(d1, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f07gd_f07_gap_dynamics_ovnvol5_5d_jerk_v145_signal(open, close):
    o = _ovn(open, close)
    core = _mean(o, 5) - _mean(o, 10)
    d1 = _roc(core, 5)
    result = _roc(d1, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f07gd_f07_gap_dynamics_gapvol5_5d_jerk_v146_signal(open, high, low, close):
    g = _gap(open, close).abs(); rng = (high - low) / close.replace(0, np.nan)
    core = _mean(g, 5) / _mean(rng, 5).replace(0, np.nan)
    d1 = _roc(core, 5)
    result = _roc(d1, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f07gd_f07_gap_dynamics_gapmedL_252d_jerk_v147_signal(open, close):
    core = _gap(open, close).rolling(252, min_periods=63).median()
    d1 = _roc(core, 63)
    result = _roc(d1, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f07gd_f07_gap_dynamics_ovnmedL_252d_jerk_v148_signal(open, close):
    o = _ovn(open, close); i = _intrlog(open, close)
    core = o.rolling(252, min_periods=63).median() - i.rolling(252, min_periods=63).median()
    d1 = _roc(core, 63)
    result = _roc(d1, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f07gd_f07_gap_dynamics_gapiqrL_126d_jerk_v149_signal(open, close):
    g = _gap(open, close)
    core = (g.rolling(126, min_periods=42).quantile(0.75) - g.rolling(126, min_periods=42).quantile(0.25))
    d1 = _roc(core, 21)
    result = _roc(d1, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f07gd_f07_gap_dynamics_ovnconcL_126d_jerk_v150_signal(open, close):
    o = _ovn(open, close).abs()
    core = o.rolling(126, min_periods=42).max() / o.rolling(126, min_periods=42).sum().replace(0, np.nan)
    d1 = _roc(core, 21)
    result = _roc(d1, 21)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f07gd_f07_gap_dynamics_gaplvl_5d_jerk_v001_signal,
    f07gd_f07_gap_dynamics_gapz_21d_jerk_v002_signal,
    f07gd_f07_gap_dynamics_gapz_63d_jerk_v003_signal,
    f07gd_f07_gap_dynamics_gapabs_21d_jerk_v004_signal,
    f07gd_f07_gap_dynamics_gapabs_63d_jerk_v005_signal,
    f07gd_f07_gap_dynamics_ovn_21d_jerk_v006_signal,
    f07gd_f07_gap_dynamics_ovncum_63d_jerk_v007_signal,
    f07gd_f07_gap_dynamics_ovncum_252d_jerk_v008_signal,
    f07gd_f07_gap_dynamics_intr_21d_jerk_v009_signal,
    f07gd_f07_gap_dynamics_intr_63d_jerk_v010_signal,
    f07gd_f07_gap_dynamics_fill_21d_jerk_v011_signal,
    f07gd_f07_gap_dynamics_fill_63d_jerk_v012_signal,
    f07gd_f07_gap_dynamics_cont_21d_jerk_v013_signal,
    f07gd_f07_gap_dynamics_cont_63d_jerk_v014_signal,
    f07gd_f07_gap_dynamics_gapdisp_63d_jerk_v015_signal,
    f07gd_f07_gap_dynamics_gapdisp_252d_jerk_v016_signal,
    f07gd_f07_gap_dynamics_ovnshare_63d_jerk_v017_signal,
    f07gd_f07_gap_dynamics_ovnvsintr_63d_jerk_v018_signal,
    f07gd_f07_gap_dynamics_absmag_126d_jerk_v019_signal,
    f07gd_f07_gap_dynamics_gapmed_126d_jerk_v020_signal,
    f07gd_f07_gap_dynamics_gapq75_63d_jerk_v021_signal,
    f07gd_f07_gap_dynamics_gapq25_63d_jerk_v022_signal,
    f07gd_f07_gap_dynamics_gapiqr_63d_jerk_v023_signal,
    f07gd_f07_gap_dynamics_ovnsharpe_63d_jerk_v024_signal,
    f07gd_f07_gap_dynamics_intrsharpe_63d_jerk_v025_signal,
    f07gd_f07_gap_dynamics_gapskew_126d_jerk_v026_signal,
    f07gd_f07_gap_dynamics_gapkurt_126d_jerk_v027_signal,
    f07gd_f07_gap_dynamics_ovnvol_21d_jerk_v028_signal,
    f07gd_f07_gap_dynamics_gapewm_21d_jerk_v029_signal,
    f07gd_f07_gap_dynamics_signmag_21d_jerk_v030_signal,
    f07gd_f07_gap_dynamics_gapatr_63d_jerk_v031_signal,
    f07gd_f07_gap_dynamics_openloc_63d_jerk_v032_signal,
    f07gd_f07_gap_dynamics_revstr_21d_jerk_v033_signal,
    f07gd_f07_gap_dynamics_revstr_126d_jerk_v034_signal,
    f07gd_f07_gap_dynamics_gapmotion_63d_jerk_v035_signal,
    f07gd_f07_gap_dynamics_varfrac_252d_jerk_v036_signal,
    f07gd_f07_gap_dynamics_gapvolr_63d_jerk_v037_signal,
    f07gd_f07_gap_dynamics_ovneff_63d_jerk_v038_signal,
    f07gd_f07_gap_dynamics_gapconsist_63d_jerk_v039_signal,
    f07gd_f07_gap_dynamics_ovnconc_63d_jerk_v040_signal,
    f07gd_f07_gap_dynamics_gapenergy_63d_jerk_v041_signal,
    f07gd_f07_gap_dynamics_triangle_63d_jerk_v042_signal,
    f07gd_f07_gap_dynamics_gaprngfrac_63d_jerk_v043_signal,
    f07gd_f07_gap_dynamics_gapvolterm_63d_jerk_v044_signal,
    f07gd_f07_gap_dynamics_ovncomp_42d_jerk_v045_signal,
    f07gd_f07_gap_dynamics_gapvov_63d_jerk_v046_signal,
    f07gd_f07_gap_dynamics_gapmotion2_126d_jerk_v047_signal,
    f07gd_f07_gap_dynamics_uptail_63d_jerk_v048_signal,
    f07gd_f07_gap_dynamics_lotail_63d_jerk_v049_signal,
    f07gd_f07_gap_dynamics_ovndrift_126d_jerk_v050_signal,
    f07gd_f07_gap_dynamics_gaplvl_21d_jerk_v051_signal,
    f07gd_f07_gap_dynamics_gaplvl_63d_jerk_v052_signal,
    f07gd_f07_gap_dynamics_wfill_126d_jerk_v053_signal,
    f07gd_f07_gap_dynamics_ovnpremium_252d_jerk_v054_signal,
    f07gd_f07_gap_dynamics_contmag_63d_jerk_v055_signal,
    f07gd_f07_gap_dynamics_polarity_63d_jerk_v056_signal,
    f07gd_f07_gap_dynamics_gapmed_63d_jerk_v057_signal,
    f07gd_f07_gap_dynamics_fillewm_42d_jerk_v058_signal,
    f07gd_f07_gap_dynamics_absmag_252d_jerk_v059_signal,
    f07gd_f07_gap_dynamics_ovnvol_63d_jerk_v060_signal,
    f07gd_f07_gap_dynamics_intrvol_63d_jerk_v061_signal,
    f07gd_f07_gap_dynamics_gapskew_252d_jerk_v062_signal,
    f07gd_f07_gap_dynamics_ovndd_252d_jerk_v063_signal,
    f07gd_f07_gap_dynamics_gapmom_21d_jerk_v064_signal,
    f07gd_f07_gap_dynamics_ovnwin_63d_jerk_v065_signal,
    f07gd_f07_gap_dynamics_gaprank_252d_jerk_v066_signal,
    f07gd_f07_gap_dynamics_ovncalmar_126d_jerk_v067_signal,
    f07gd_f07_gap_dynamics_taildns_252d_jerk_v068_signal,
    f07gd_f07_gap_dynamics_gapatr_5d_jerk_v069_signal,
    f07gd_f07_gap_dynamics_ovnskew_126d_jerk_v070_signal,
    f07gd_f07_gap_dynamics_gapvolexp_21d_jerk_v071_signal,
    f07gd_f07_gap_dynamics_gapztanh_63d_jerk_v072_signal,
    f07gd_f07_gap_dynamics_dirbias_63d_jerk_v073_signal,
    f07gd_f07_gap_dynamics_gaprng_126d_jerk_v074_signal,
    f07gd_f07_gap_dynamics_ovnrank_252d_jerk_v075_signal,
    f07gd_f07_gap_dynamics_gapdz_63d_jerk_v076_signal,
    f07gd_f07_gap_dynamics_ovndisp_126d_jerk_v077_signal,
    f07gd_f07_gap_dynamics_contdz_63d_jerk_v078_signal,
    f07gd_f07_gap_dynamics_filldz_63d_jerk_v079_signal,
    f07gd_f07_gap_dynamics_gapabsz_126d_jerk_v080_signal,
    f07gd_f07_gap_dynamics_ovnz_63d_jerk_v081_signal,
    f07gd_f07_gap_dynamics_intrz_63d_jerk_v082_signal,
    f07gd_f07_gap_dynamics_gapacf_126d_jerk_v083_signal,
    f07gd_f07_gap_dynamics_ovnac_126d_jerk_v084_signal,
    f07gd_f07_gap_dynamics_gapclust_63d_jerk_v085_signal,
    f07gd_f07_gap_dynamics_ovnsemi_126d_jerk_v086_signal,
    f07gd_f07_gap_dynamics_gapprc_252d_jerk_v087_signal,
    f07gd_f07_gap_dynamics_gapprc10_252d_jerk_v088_signal,
    f07gd_f07_gap_dynamics_ovntrend_126d_jerk_v089_signal,
    f07gd_f07_gap_dynamics_gaprat_63d_jerk_v090_signal,
    f07gd_f07_gap_dynamics_ovncorr_126d_jerk_v091_signal,
    f07gd_f07_gap_dynamics_gapcorr_126d_jerk_v092_signal,
    f07gd_f07_gap_dynamics_fillrat_126d_jerk_v093_signal,
    f07gd_f07_gap_dynamics_ovnwm_252d_jerk_v094_signal,
    f07gd_f07_gap_dynamics_gapsd_63d_jerk_v095_signal,
    f07gd_f07_gap_dynamics_ovncum2_126d_jerk_v096_signal,
    f07gd_f07_gap_dynamics_intrcum_126d_jerk_v097_signal,
    f07gd_f07_gap_dynamics_gapmag_5d_jerk_v098_signal,
    f07gd_f07_gap_dynamics_ovn5_5d_jerk_v099_signal,
    f07gd_f07_gap_dynamics_intr5_5d_jerk_v100_signal,
    f07gd_f07_gap_dynamics_cont5_5d_jerk_v101_signal,
    f07gd_f07_gap_dynamics_fill5_5d_jerk_v102_signal,
    f07gd_f07_gap_dynamics_gapwk_5d_jerk_v103_signal,
    f07gd_f07_gap_dynamics_ovnwk_5d_jerk_v104_signal,
    f07gd_f07_gap_dynamics_gapsignwk_5d_jerk_v105_signal,
    f07gd_f07_gap_dynamics_gaplo_21d_jerk_v106_signal,
    f07gd_f07_gap_dynamics_gaphi_21d_jerk_v107_signal,
    f07gd_f07_gap_dynamics_ovnup_63d_jerk_v108_signal,
    f07gd_f07_gap_dynamics_ovndn_63d_jerk_v109_signal,
    f07gd_f07_gap_dynamics_gapxvol_63d_jerk_v110_signal,
    f07gd_f07_gap_dynamics_ovnxintr_63d_jerk_v111_signal,
    f07gd_f07_gap_dynamics_gapmom2_63d_jerk_v112_signal,
    f07gd_f07_gap_dynamics_ovnmom_63d_jerk_v113_signal,
    f07gd_f07_gap_dynamics_contmom_63d_jerk_v114_signal,
    f07gd_f07_gap_dynamics_fillmom_63d_jerk_v115_signal,
    f07gd_f07_gap_dynamics_gapsq_63d_jerk_v116_signal,
    f07gd_f07_gap_dynamics_ovnsq_63d_jerk_v117_signal,
    f07gd_f07_gap_dynamics_gapfold_63d_jerk_v118_signal,
    f07gd_f07_gap_dynamics_ovnfold_63d_jerk_v119_signal,
    f07gd_f07_gap_dynamics_gaprr_252d_jerk_v120_signal,
    f07gd_f07_gap_dynamics_ovnrr_252d_jerk_v121_signal,
    f07gd_f07_gap_dynamics_gapcv_126d_jerk_v122_signal,
    f07gd_f07_gap_dynamics_ovncv_126d_jerk_v123_signal,
    f07gd_f07_gap_dynamics_gapxrng_63d_jerk_v124_signal,
    f07gd_f07_gap_dynamics_openlocz_63d_jerk_v125_signal,
    f07gd_f07_gap_dynamics_gapskewq_63d_jerk_v126_signal,
    f07gd_f07_gap_dynamics_ovnskewq_63d_jerk_v127_signal,
    f07gd_f07_gap_dynamics_intrskew_126d_jerk_v128_signal,
    f07gd_f07_gap_dynamics_gapkurtq_63d_jerk_v129_signal,
    f07gd_f07_gap_dynamics_gapewmL_63d_jerk_v130_signal,
    f07gd_f07_gap_dynamics_ovnewm_21d_jerk_v131_signal,
    f07gd_f07_gap_dynamics_contewmL_63d_jerk_v132_signal,
    f07gd_f07_gap_dynamics_gapprctl_126d_jerk_v133_signal,
    f07gd_f07_gap_dynamics_ovnprctl_126d_jerk_v134_signal,
    f07gd_f07_gap_dynamics_gapwin_126d_jerk_v135_signal,
    f07gd_f07_gap_dynamics_ovnentropy_63d_jerk_v136_signal,
    f07gd_f07_gap_dynamics_gapextend_63d_jerk_v137_signal,
    f07gd_f07_gap_dynamics_ovnbeta2_126d_jerk_v138_signal,
    f07gd_f07_gap_dynamics_intrbeta2_126d_jerk_v139_signal,
    f07gd_f07_gap_dynamics_gapddnorm_252d_jerk_v140_signal,
    f07gd_f07_gap_dynamics_gapenergyL_126d_jerk_v141_signal,
    f07gd_f07_gap_dynamics_revmag2_63d_jerk_v142_signal,
    f07gd_f07_gap_dynamics_gapfillw_63d_jerk_v143_signal,
    f07gd_f07_gap_dynamics_gapqs_63d_jerk_v144_signal,
    f07gd_f07_gap_dynamics_ovnvol5_5d_jerk_v145_signal,
    f07gd_f07_gap_dynamics_gapvol5_5d_jerk_v146_signal,
    f07gd_f07_gap_dynamics_gapmedL_252d_jerk_v147_signal,
    f07gd_f07_gap_dynamics_ovnmedL_252d_jerk_v148_signal,
    f07gd_f07_gap_dynamics_gapiqrL_126d_jerk_v149_signal,
    f07gd_f07_gap_dynamics_ovnconcL_126d_jerk_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F07_GAP_DYNAMICS_REGISTRY_001_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    close = pd.Series(closeadj.values, name="close")
    openp = pd.Series(close.shift(1).fillna(close.iloc[0]).values
                      * (1 + np.random.normal(0, 0.005, n)), name="open")
    high = pd.Series(np.maximum(close, openp)
                     * (1 + np.abs(np.random.normal(0, 0.01, n))), name="high")
    low = pd.Series(np.minimum(close, openp)
                    * (1 - np.abs(np.random.normal(0, 0.01, n))), name="low")
    volume = pd.Series(np.abs(np.random.normal(1e6, 3e5, n)) + 1e5, name="volume")

    cols = {"closeadj": closeadj, "close": close, "open": openp,
            "high": high, "low": low, "volume": volume}

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

    print("OK %s: %d features pass" % ("f07_gap_dynamics_3rd_derivatives_001_150_claude", n_features))
