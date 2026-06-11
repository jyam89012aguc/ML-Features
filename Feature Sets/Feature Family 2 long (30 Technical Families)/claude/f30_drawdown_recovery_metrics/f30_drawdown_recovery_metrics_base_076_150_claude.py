"""f30_drawdown_recovery_metrics base features 076-150.

Domain: DRAWDOWN, RECOVERY, UNDERWATER dynamics. Each feature references a
drawdown construct. Structurally distinct from 001-075 (no shared expression
up to a window change). NaN policy: never fillna(<value>); only
replace([inf,-inf], nan) at the final return. Window > 21d uses closeadj.
"""
from __future__ import annotations

import numpy as np
import pandas as pd


# ---------------------------------------------------------------------------
# Features 076-150
# ---------------------------------------------------------------------------


# === Different-class DD-derived features ====================================


def f30dr_f30_drawdown_recovery_metrics_dd_15d_base_v076_signal(close):
    """DD vs 15d rolling high — short DD level not used in 001-075."""
    n = 15
    return (close / close.rolling(n, min_periods=n).max() - 1.0).replace([np.inf, -np.inf], np.nan)


def f30dr_f30_drawdown_recovery_metrics_dd_42d_base_v077_signal(closeadj):
    """DD vs 42d rolling high (between f001 DD20 and f002 DD63)."""
    n = 42
    return (closeadj / closeadj.rolling(n, min_periods=n).max() - 1.0).replace([np.inf, -np.inf], np.nan)


def f30dr_f30_drawdown_recovery_metrics_dd_378d_base_v078_signal(closeadj):
    """DD vs 378d rolling high — mid-range between DD252 and DD504."""
    n = 378
    return (closeadj / closeadj.rolling(n, min_periods=n).max() - 1.0).replace([np.inf, -np.inf], np.nan)


# === Drawup magnitudes at different windows ================================


def f30dr_f30_drawdown_recovery_metrics_drawup_40d_base_v079_signal(closeadj):
    """Drawup vs 40d rmin."""
    n = 40
    return (closeadj / closeadj.rolling(n, min_periods=n).min() - 1.0).replace([np.inf, -np.inf], np.nan)


def f30dr_f30_drawdown_recovery_metrics_drawup_252d_base_v080_signal(closeadj):
    """Drawup vs 252d rmin — annual recovery extent."""
    n = 252
    return (closeadj / closeadj.rolling(n, min_periods=n).min() - 1.0).replace([np.inf, -np.inf], np.nan)


# === Net dd = drawup + drawdown (asymmetry sum) ============================


def f30dr_f30_drawdown_recovery_metrics_net_du_dd_30d_base_v081_signal(close):
    """(DU30 + DD30) — net asymmetry: large = strong drift, near 0 = mean-reverting."""
    n = 30
    du = close / close.rolling(n, min_periods=n).min() - 1.0
    dd = close / close.rolling(n, min_periods=n).max() - 1.0
    return (du + dd).replace([np.inf, -np.inf], np.nan)


def f30dr_f30_drawdown_recovery_metrics_dd_du_product_150d_base_v082_signal(closeadj):
    """DU150 * |DD150| — joint magnitude of bull-and-bear extremes within window."""
    n = 150
    du = closeadj / closeadj.rolling(n, min_periods=n).min() - 1.0
    dd = closeadj / closeadj.rolling(n, min_periods=n).max() - 1.0
    return (du * dd.abs()).replace([np.inf, -np.inf], np.nan)


# === Drawdown convexity / shape ============================================


def f30dr_f30_drawdown_recovery_metrics_dd_curve_concavity_60d_base_v083_signal(closeadj):
    """Average of (dd_t + dd_{t-2*k} - 2*dd_{t-k})/k^2 over various lags k.
    Concavity proxy for DD curve over 60d horizon."""
    n = 60
    dd = closeadj / closeadj.rolling(n, min_periods=n).max() - 1.0
    c1 = (dd + dd.shift(20) - 2.0 * dd.shift(10)) / 100.0
    c2 = (dd + dd.shift(10) - 2.0 * dd.shift(5)) / 25.0
    return ((c1 + c2) / 2.0).replace([np.inf, -np.inf], np.nan)


# === Local-trough recurrence ===============================================


def f30dr_f30_drawdown_recovery_metrics_local_trough_count_120d_base_v084_signal(closeadj):
    """Count of distinct local 20d-troughs (close at 20d rmin) within trailing 120d."""
    n_rng = 120
    rmin20 = closeadj.rolling(20, min_periods=20).min()
    at_low = (closeadj <= rmin20 + 1e-12).astype(float).where(~rmin20.isna())

    def _episodes(x):
        c = 0; in_ep = False
        for v in x:
            if v >= 0.5:
                if not in_ep:
                    c += 1; in_ep = True
            else:
                in_ep = False
        return float(c)
    return at_low.rolling(n_rng, min_periods=n_rng).apply(_episodes, raw=True).replace([np.inf, -np.inf], np.nan)


# === Severe DD severity stats ==============================================


def f30dr_f30_drawdown_recovery_metrics_dd_q10_60d_base_v085_signal(closeadj):
    """10th-percentile of DD(60) over trailing 60d — worst-10% DD bound."""
    n = 60
    dd = closeadj / closeadj.rolling(n, min_periods=n).max() - 1.0
    return dd.rolling(n, min_periods=n).quantile(0.10).replace([np.inf, -np.inf], np.nan)


def f30dr_f30_drawdown_recovery_metrics_dd_iqr_100d_base_v086_signal(closeadj):
    """IQR of DD(100) series — DD dispersion within window."""
    n = 100
    dd = closeadj / closeadj.rolling(n, min_periods=n).max() - 1.0
    q75 = dd.rolling(n, min_periods=n).quantile(0.75)
    q25 = dd.rolling(n, min_periods=n).quantile(0.25)
    return (q75 - q25).replace([np.inf, -np.inf], np.nan)


# === Streaks of consecutive new highs / new lows ===========================


def f30dr_f30_drawdown_recovery_metrics_newhigh_streak_60d_base_v087_signal(closeadj):
    """Length of current consecutive at-60d-high streak (DD == 0 contiguous)."""
    n = 60
    rmax = closeadj.rolling(n, min_periods=n).max()
    at_high = (closeadj >= rmax - 1e-12).astype(float).where(~rmax.isna())
    out = pd.Series(np.nan, index=closeadj.index, dtype=float)
    cnt = np.nan
    av = at_high.values
    for i in range(len(closeadj)):
        if not np.isfinite(av[i]):
            continue
        if av[i] >= 0.5:
            cnt = (cnt + 1.0) if np.isfinite(cnt) else 1.0
        else:
            cnt = 0.0
        out.iat[i] = cnt
    return out.replace([np.inf, -np.inf], np.nan)


def f30dr_f30_drawdown_recovery_metrics_newlow_streak_45d_base_v088_signal(closeadj):
    """Length of current consecutive at-45d-low streak."""
    n = 45
    rmin = closeadj.rolling(n, min_periods=n).min()
    at_low = (closeadj <= rmin + 1e-12).astype(float).where(~rmin.isna())
    out = pd.Series(np.nan, index=closeadj.index, dtype=float)
    cnt = np.nan
    av = at_low.values
    for i in range(len(closeadj)):
        if not np.isfinite(av[i]):
            continue
        if av[i] >= 0.5:
            cnt = (cnt + 1.0) if np.isfinite(cnt) else 1.0
        else:
            cnt = 0.0
        out.iat[i] = cnt
    return out.replace([np.inf, -np.inf], np.nan)


# === DD vs ATR ratio (different windows) ===================================


def f30dr_f30_drawdown_recovery_metrics_dd_atr_units_90d_base_v089_signal(high, low, closeadj):
    """Current DD(90) magnitude in ATR(30) units: |DD90| * close / ATR30."""
    n = 90
    dd_abs = (closeadj / closeadj.rolling(n, min_periods=n).max() - 1.0).abs()
    pc = closeadj.shift(1)
    tr = pd.concat([high - low, (high - pc).abs(), (low - pc).abs()], axis=1).max(axis=1)
    atr = tr.rolling(30, min_periods=30).mean()
    return (dd_abs * closeadj / atr.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# === DD vs realized-skew (does DD coincide with neg-skew return regime?) ===


def f30dr_f30_drawdown_recovery_metrics_dd_under_negskew_45d_base_v090_signal(closeadj):
    """|DD(45)| times indicator that 45d log-ret skew < 0. Picks out DDs in neg-skew regimes."""
    n = 45
    dd_abs = (closeadj / closeadj.rolling(n, min_periods=n).max() - 1.0).abs()
    r = np.log(closeadj / closeadj.shift(1))
    sk = r.rolling(n, min_periods=n).skew()
    flag = (sk < 0).astype(float).where(~sk.isna())
    return (dd_abs * flag).replace([np.inf, -np.inf], np.nan)


# === DD-conditional returns ================================================


def f30dr_f30_drawdown_recovery_metrics_ret_in_dd_60d_base_v091_signal(closeadj):
    """Avg log-return ONLY on bars where DD(60) <= -5%, over trailing 60d."""
    n = 60
    dd = closeadj / closeadj.rolling(n, min_periods=n).max() - 1.0
    r = np.log(closeadj / closeadj.shift(1))
    in_dd = (dd <= -0.05).astype(float).where(~dd.isna())
    num = (r * in_dd).rolling(n, min_periods=n).sum()
    den = in_dd.rolling(n, min_periods=n).sum().replace(0.0, np.nan)
    return (num / den).replace([np.inf, -np.inf], np.nan)


# === DD's correlation with volume ==========================================


def f30dr_f30_drawdown_recovery_metrics_corr_dd_volume_60d_base_v092_signal(closeadj, volume):
    """60d corr between DD(20) and log(volume). Negative DD with high volume = panic selling."""
    n = 60
    dd = closeadj / closeadj.rolling(20, min_periods=20).max() - 1.0
    lv = np.log(volume.replace(0.0, np.nan))
    return dd.rolling(n, min_periods=n).corr(lv).replace([np.inf, -np.inf], np.nan)


# === Recovery-trajectory shape (linear regression slope of DD-curve) =======


def f30dr_f30_drawdown_recovery_metrics_dd_regslope_30d_base_v093_signal(closeadj):
    """OLS slope of DD(30) over trailing 30 bars (vs time index). Recovery direction signed."""
    n = 30
    dd = closeadj / closeadj.rolling(n, min_periods=n).max() - 1.0
    t = np.arange(n, dtype=float); tm = t.mean(); td = t - tm; ss = float((td * td).sum())

    def _slope(x):
        return float(np.dot(x - x.mean(), td) / ss) if ss > 0 else np.nan
    return dd.rolling(n, min_periods=n).apply(_slope, raw=True).replace([np.inf, -np.inf], np.nan)


def f30dr_f30_drawdown_recovery_metrics_dd_regslope_120d_base_v094_signal(closeadj):
    """OLS slope of DD(120) over trailing 120 bars."""
    n = 120
    dd = closeadj / closeadj.rolling(n, min_periods=n).max() - 1.0
    t = np.arange(n, dtype=float); tm = t.mean(); td = t - tm; ss = float((td * td).sum())

    def _slope(x):
        return float(np.dot(x - x.mean(), td) / ss) if ss > 0 else np.nan
    return dd.rolling(n, min_periods=n).apply(_slope, raw=True).replace([np.inf, -np.inf], np.nan)


# === DD's R^2 vs time (linearity of underwater trajectory) =================


def f30dr_f30_drawdown_recovery_metrics_dd_rsq_time_60d_base_v095_signal(closeadj):
    """R^2 of DD(60) vs time over 60d (linearity of underwater path)."""
    n = 60
    dd = closeadj / closeadj.rolling(n, min_periods=n).max() - 1.0
    t = np.arange(n, dtype=float); tm = t.mean(); td = t - tm; ss = float((td * td).sum())

    def _rsq(x):
        if ss <= 0:
            return np.nan
        xm = x.mean(); xd = x - xm
        sst = float((xd * xd).sum())
        if sst <= 0:
            return np.nan
        b = float(np.dot(xd, td) / ss)
        return float((b * b * ss) / sst)
    return dd.rolling(n, min_periods=n).apply(_rsq, raw=True).replace([np.inf, -np.inf], np.nan)


# === DD-volatility ratio (DD-curve vol / price vol) ========================


def f30dr_f30_drawdown_recovery_metrics_dd_vol_ratio_75d_base_v096_signal(closeadj):
    """std(DD(75) curve diffs) / std(log-returns). Underwater path noisiness vs price noise."""
    n = 75
    dd = closeadj / closeadj.rolling(n, min_periods=n).max() - 1.0
    dd_vol = dd.diff().rolling(n, min_periods=n).std()
    r_vol = np.log(closeadj / closeadj.shift(1)).rolling(n, min_periods=n).std()
    return (dd_vol / r_vol.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# === Differential between recovery & drawdown phases =======================


def f30dr_f30_drawdown_recovery_metrics_phase_imbalance_45d_base_v097_signal(closeadj):
    """((bars with DD20-increasing) - (bars with DD20-decreasing)) / 45 over 45d."""
    n = 45
    dd = closeadj / closeadj.rolling(20, min_periods=20).max() - 1.0
    inc = (dd.diff() > 0).astype(float).where(~dd.diff().isna())
    dec = (dd.diff() < 0).astype(float).where(~dd.diff().isna())
    return ((inc.rolling(n, min_periods=n).sum() - dec.rolling(n, min_periods=n).sum()) / float(n)).replace([np.inf, -np.inf], np.nan)


# === Underwater integral vs drawup integral asymmetry ======================


def f30dr_f30_drawdown_recovery_metrics_uw_du_integral_diff_60d_base_v098_signal(closeadj):
    """sum(DU60) - sum(|DD60|) over 60d window. Net "above-low" vs "below-high" area."""
    n = 60
    du = closeadj / closeadj.rolling(n, min_periods=n).min() - 1.0
    dd_abs = (closeadj / closeadj.rolling(n, min_periods=n).max() - 1.0).abs()
    return (du.rolling(n, min_periods=n).sum() - dd_abs.rolling(n, min_periods=n).sum()).replace([np.inf, -np.inf], np.nan)


# === DD severity & duration combined =======================================


def f30dr_f30_drawdown_recovery_metrics_dd_severity_duration_60d_base_v099_signal(closeadj):
    """|DD(60)| * (bars since last 60d high). Compound severity-duration measure."""
    n = 60
    dd_abs = (closeadj / closeadj.rolling(n, min_periods=n).max() - 1.0).abs()
    rmax = closeadj.rolling(n, min_periods=n).max()
    at_high = (closeadj >= rmax - 1e-12).astype(float).where(~rmax.isna())
    bars = pd.Series(np.nan, index=closeadj.index, dtype=float)
    cnt = np.nan
    av = at_high.values
    for i in range(len(closeadj)):
        if not np.isfinite(av[i]):
            continue
        if av[i] >= 0.5:
            cnt = 0.0
        else:
            cnt = (cnt + 1.0) if np.isfinite(cnt) else np.nan
        bars.iat[i] = cnt
    return (dd_abs * bars).replace([np.inf, -np.inf], np.nan)


# === Fast vs slow underwater ===============================================


def f30dr_f30_drawdown_recovery_metrics_uw_30_vs_120_base_v100_signal(closeadj):
    """uw-frac(30) - uw-frac(120). Short vs long underwater spread."""
    rmax30 = closeadj.rolling(30, min_periods=30).max()
    below30 = (closeadj < rmax30 - 1e-12).astype(float).where(~rmax30.isna())
    f30 = below30.rolling(30, min_periods=30).mean()
    rmax120 = closeadj.rolling(120, min_periods=120).max()
    below120 = (closeadj < rmax120 - 1e-12).astype(float).where(~rmax120.isna())
    f120 = below120.rolling(120, min_periods=120).mean()
    return (f30 - f120).replace([np.inf, -np.inf], np.nan)


# === DD-windowed Sharpe complement =========================================


def f30dr_f30_drawdown_recovery_metrics_dd_sharpe_60d_base_v101_signal(closeadj):
    """In-DD log-return mean / in-DD log-return std (Sharpe of drawdown-phase returns)."""
    n = 60
    dd = closeadj / closeadj.rolling(n, min_periods=n).max() - 1.0
    r = np.log(closeadj / closeadj.shift(1)).where(dd < -0.01)
    return (r.rolling(n, min_periods=20).mean() / r.rolling(n, min_periods=20).std().replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# === DD reach: max DD scaled by time =======================================


def f30dr_f30_drawdown_recovery_metrics_max_dd_per_bar_180d_base_v102_signal(closeadj):
    """|min DD(180)| / 180 — DD severity per-bar."""
    n = 180
    dd = closeadj / closeadj.rolling(n, min_periods=n).max() - 1.0
    return (dd.rolling(n, min_periods=n).min().abs() / float(n)).replace([np.inf, -np.inf], np.nan)


# === Recovery completeness (post-trough) ===================================


def f30dr_f30_drawdown_recovery_metrics_recovery_completeness_60d_base_v103_signal(closeadj):
    """How much of DD(60)'s trough has been recovered, expressed as fraction:
    (close - rmin60) / (rmax60 - rmin60) clamped 0-1 only when DD < -1%."""
    n = 60
    rmax = closeadj.rolling(n, min_periods=n).max()
    rmin = closeadj.rolling(n, min_periods=n).min()
    dd = closeadj / rmax - 1.0
    rec = (closeadj - rmin) / (rmax - rmin).replace(0.0, np.nan)
    return rec.where(dd < -0.01).replace([np.inf, -np.inf], np.nan)


# === Skew of underwater bar counts within sub-windows ======================


def f30dr_f30_drawdown_recovery_metrics_uw_runs_skew_120d_base_v104_signal(closeadj):
    """Skew of underwater-run-length distribution within 120d."""
    n = 120
    rmax = closeadj.rolling(n, min_periods=n).max()
    below = (closeadj < rmax - 1e-12).astype(float).where(~rmax.isna())

    def _run_skew(x):
        runs = []; cur = 0
        for v in x:
            if v >= 0.5:
                cur += 1
            else:
                if cur > 0:
                    runs.append(cur); cur = 0
        if cur > 0:
            runs.append(cur)
        if len(runs) < 3:
            return np.nan
        arr = np.asarray(runs, dtype=float)
        m = arr.mean(); s = arr.std(ddof=0)
        if s <= 0:
            return np.nan
        return float(((arr - m) ** 3).mean() / (s ** 3))
    return below.rolling(n, min_periods=n).apply(_run_skew, raw=True).replace([np.inf, -np.inf], np.nan)


# === Ulcer-deflated return =================================================


def f30dr_f30_drawdown_recovery_metrics_martin_ratio_90d_base_v105_signal(closeadj):
    """Martin ratio: 90d total log-return / Ulcer Index(90)."""
    n = 90
    ret = np.log(closeadj / closeadj.shift(n))
    dd = closeadj / closeadj.rolling(n, min_periods=n).max() - 1.0
    ulcer = np.sqrt((dd ** 2).rolling(n, min_periods=n).mean())
    return (ret / ulcer.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# === DD's longest run weighted by its mean DD level ========================


def f30dr_f30_drawdown_recovery_metrics_max_run_dd_weighted_120d_base_v106_signal(closeadj):
    """For longest underwater run in 120d: avg |DD| over that run.
    Worst-episode-severity. If no run, 0."""
    n = 120
    rmax = closeadj.rolling(n, min_periods=n).max()
    dd = closeadj / rmax - 1.0
    below = (closeadj < rmax - 1e-12).astype(float).where(~rmax.isna())

    def _worst(below_arr, dd_arr):
        best_len = 0; best_sum = 0.0
        cur_len = 0; cur_sum = 0.0
        for v, d in zip(below_arr, dd_arr):
            if v >= 0.5 and np.isfinite(d):
                cur_len += 1; cur_sum += abs(d)
                if cur_len > best_len:
                    best_len = cur_len; best_sum = cur_sum
            else:
                cur_len = 0; cur_sum = 0.0
        return float(best_sum / best_len) if best_len > 0 else 0.0

    out = pd.Series(np.nan, index=closeadj.index, dtype=float)
    bv = below.values; dv = dd.values
    for i in range(n - 1, len(closeadj)):
        if np.isnan(bv[i]) or np.isnan(dv[i]):
            continue
        out.iat[i] = _worst(bv[i - n + 1: i + 1], dv[i - n + 1: i + 1])
    return out.replace([np.inf, -np.inf], np.nan)


# === Recovery-period return =================================================


def f30dr_f30_drawdown_recovery_metrics_dd_below_med_freq_50d_base_v107_signal(closeadj):
    """Frequency of bars where DD(50) is below its 50d-trailing median. Pain-distribution flag."""
    n = 50
    dd = closeadj / closeadj.rolling(n, min_periods=n).max() - 1.0
    md = dd.rolling(n, min_periods=n).median()
    flag = (dd < md).astype(float).where(~dd.isna() & ~md.isna())
    return flag.rolling(n, min_periods=n).mean().replace([np.inf, -np.inf], np.nan)


# === DD-asymmetry-weighted return ==========================================


def f30dr_f30_drawdown_recovery_metrics_recovery_weighted_return_75d_base_v108_signal(closeadj):
    """75d return weighted by recovery fraction at start vs end:
    log(close/close.shift(75)) * (1 - |DD(75)|)."""
    n = 75
    ret = np.log(closeadj / closeadj.shift(n))
    dd_abs = (closeadj / closeadj.rolling(n, min_periods=n).max() - 1.0).abs()
    return (ret * (1.0 - dd_abs)).replace([np.inf, -np.inf], np.nan)


# === DD's autocorrelation ==================================================


def f30dr_f30_drawdown_recovery_metrics_dd_autocorr_60d_base_v109_signal(closeadj):
    """Lag-5 autocorr of DD(20) over trailing 60 bars."""
    n_rng = 60
    dd = closeadj / closeadj.rolling(20, min_periods=20).max() - 1.0
    return dd.rolling(n_rng, min_periods=n_rng).corr(dd.shift(5)).replace([np.inf, -np.inf], np.nan)


# === DD's max-vs-mean ratio (concentration / outlier sensitivity) ==========


def f30dr_f30_drawdown_recovery_metrics_dd_max_mean_ratio_100d_base_v110_signal(closeadj):
    """|min DD(100)| / |mean DD(100)|. Concentration of pain in extreme bar."""
    n = 100
    dd = closeadj / closeadj.rolling(n, min_periods=n).max() - 1.0
    return (dd.rolling(n, min_periods=n).min().abs() / dd.rolling(n, min_periods=n).mean().abs().replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# === High-low channel DD (uses high & low intra-bar) ========================


def f30dr_f30_drawdown_recovery_metrics_dd_using_lows_25d_base_v111_signal(high, low):
    """DD using daily LOWS vs 25d max-of-highs: low/max(high,25) - 1. Intra-bar DD reach."""
    n = 25
    return (low / high.rolling(n, min_periods=n).max() - 1.0).replace([np.inf, -np.inf], np.nan)


def f30dr_f30_drawdown_recovery_metrics_intrabar_dd_minus_close_dd_100d_base_v112_signal(high, low, closeadj):
    """Intrabar DD (low/100d-max-high - 1) minus close DD (close/100d-max-close - 1).
    Highlights bars where lows extended DD beyond close-based DD."""
    n = 100
    intra = low / high.rolling(n, min_periods=n).max() - 1.0
    cl = closeadj / closeadj.rolling(n, min_periods=n).max() - 1.0
    return (intra - cl).replace([np.inf, -np.inf], np.nan)


# === Largest single-bar DD-step (worst negative return that contributed to DD) ===


def f30dr_f30_drawdown_recovery_metrics_max_dd_step_60d_base_v113_signal(closeadj):
    """Min of DD(60).diff() over 60d — largest single-bar deepening step."""
    n = 60
    dd = closeadj / closeadj.rolling(n, min_periods=n).max() - 1.0
    return dd.diff().rolling(n, min_periods=n).min().replace([np.inf, -np.inf], np.nan)


# === Largest single-bar recovery step ======================================


def f30dr_f30_drawdown_recovery_metrics_max_recovery_step_60d_base_v114_signal(closeadj):
    """Max of DD(60).diff() over 60d — largest single-bar recovery step."""
    n = 60
    dd = closeadj / closeadj.rolling(n, min_periods=n).max() - 1.0
    return dd.diff().rolling(n, min_periods=n).max().replace([np.inf, -np.inf], np.nan)


# === DD-deepening to recovery ratio (sum of negative diffs vs positive) ====


def f30dr_f30_drawdown_recovery_metrics_neg_pos_diff_ratio_50d_base_v115_signal(closeadj):
    """sum of negative DD-diffs vs positive DD-diffs over 50d. Imbalance of moves."""
    n = 50
    dd = closeadj / closeadj.rolling(n, min_periods=n).max() - 1.0
    d = dd.diff()
    neg = (-d.where(d < 0, 0.0)).rolling(n, min_periods=n).sum()
    pos = (d.where(d > 0, 0.0)).rolling(n, min_periods=n).sum()
    return (neg / (pos + neg).replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# === Tanh of severity-duration =============================================


def f30dr_f30_drawdown_recovery_metrics_tanh_dd_dur_75d_base_v116_signal(closeadj):
    """tanh of (|DD(75)| * underwater_bars / 75) — bounded compound DD-duration."""
    n = 75
    dd_abs = (closeadj / closeadj.rolling(n, min_periods=n).max() - 1.0).abs()
    rmax = closeadj.rolling(n, min_periods=n).max()
    at_high = (closeadj >= rmax - 1e-12).astype(float).where(~rmax.isna())
    bars = pd.Series(np.nan, index=closeadj.index, dtype=float)
    cnt = np.nan
    av = at_high.values
    for i in range(len(closeadj)):
        if not np.isfinite(av[i]):
            continue
        if av[i] >= 0.5:
            cnt = 0.0
        else:
            cnt = (cnt + 1.0) if np.isfinite(cnt) else np.nan
        bars.iat[i] = cnt
    return np.tanh(dd_abs * bars / float(n)).replace([np.inf, -np.inf], np.nan)


# === Conditional DD given high realized vol ================================


def f30dr_f30_drawdown_recovery_metrics_dd_in_highvol_45d_base_v117_signal(closeadj):
    """|DD(45)| * indicator (45d rv is in top quartile of trailing 180d)."""
    n = 45; n_rk = 180
    dd_abs = (closeadj / closeadj.rolling(n, min_periods=n).max() - 1.0).abs()
    rv = np.log(closeadj / closeadj.shift(1)).rolling(n, min_periods=n).std()
    rk = rv.rolling(n_rk, min_periods=n_rk).apply(
        lambda x: float((np.sum(x <= x[-1]) - 1) / max(1, (len(x) - 1))), raw=True
    )
    flag = (rk >= 0.75).astype(float).where(~rk.isna())
    return (dd_abs * flag).replace([np.inf, -np.inf], np.nan)


# === Cumulative recovery contribution ======================================


def f30dr_f30_drawdown_recovery_metrics_cum_recovery_50d_base_v118_signal(closeadj):
    """Sum of positive DD(50).diff() over 50d. Cumulative recovery contribution."""
    n = 50
    dd = closeadj / closeadj.rolling(n, min_periods=n).max() - 1.0
    pos = dd.diff().where(dd.diff() > 0, 0.0)
    return pos.rolling(n, min_periods=n).sum().replace([np.inf, -np.inf], np.nan)


# === Cumulative deepening ==================================================


def f30dr_f30_drawdown_recovery_metrics_cum_deepening_50d_base_v119_signal(closeadj):
    """Sum of |negative DD(50).diff()| over 50d. Cumulative deepening contribution."""
    n = 50
    dd = closeadj / closeadj.rolling(n, min_periods=n).max() - 1.0
    neg = (-dd.diff()).where(dd.diff() < 0, 0.0)
    return neg.rolling(n, min_periods=n).sum().replace([np.inf, -np.inf], np.nan)


# === DD percentile in rank-window using close ==============================


def f30dr_f30_drawdown_recovery_metrics_rank_dd_180d_base_v120_signal(closeadj):
    """Rank of DD(45) within trailing 180d using a different DD window than v018."""
    n_dd = 45; n_rk = 180
    dd = closeadj / closeadj.rolling(n_dd, min_periods=n_dd).max() - 1.0
    return dd.rolling(n_rk, min_periods=n_rk).apply(
        lambda x: float((np.sum(x <= x[-1]) - 1) / max(1, (len(x) - 1))), raw=True
    ).replace([np.inf, -np.inf], np.nan)


# === DD-difference: long-DD minus current DD (room left to drawdown) =======


def f30dr_f30_drawdown_recovery_metrics_dd_room_252d_base_v121_signal(closeadj):
    """DD(252) - min DD(252) — distance from current DD to historical worst."""
    n = 252
    dd = closeadj / closeadj.rolling(n, min_periods=n).max() - 1.0
    return (dd - dd.rolling(n, min_periods=n).min()).replace([np.inf, -np.inf], np.nan)


# === Volume-weighted DD ====================================================


def f30dr_f30_drawdown_recovery_metrics_vol_weighted_dd_60d_base_v122_signal(closeadj, volume):
    """Volume-weighted DD: sum(DD * vol) / sum(vol) over 60d, DD vs 60d rmax."""
    n = 60
    dd = closeadj / closeadj.rolling(n, min_periods=n).max() - 1.0
    num = (dd * volume).rolling(n, min_periods=n).sum()
    den = volume.rolling(n, min_periods=n).sum().replace(0.0, np.nan)
    return (num / den).replace([np.inf, -np.inf], np.nan)


# === DD episode median length ==============================================


def f30dr_f30_drawdown_recovery_metrics_uw_median_run_180d_base_v123_signal(closeadj):
    """Median length of underwater runs in trailing 180d."""
    n = 180
    rmax = closeadj.rolling(n, min_periods=n).max()
    below = (closeadj < rmax - 1e-12).astype(float).where(~rmax.isna())

    def _med_run(x):
        runs = []; cur = 0
        for v in x:
            if v >= 0.5:
                cur += 1
            else:
                if cur > 0:
                    runs.append(cur); cur = 0
        if cur > 0:
            runs.append(cur)
        return float(np.median(runs)) if runs else 0.0
    return below.rolling(n, min_periods=n).apply(_med_run, raw=True).replace([np.inf, -np.inf], np.nan)


# === DD distance from current trough =======================================


def f30dr_f30_drawdown_recovery_metrics_dd_above_q25_freq_90d_base_v124_signal(closeadj):
    """Fraction of 90d bars where DD(60) is above its 90d 25th-pct (i.e. less severe)."""
    n_dd = 60; n_rng = 90
    dd = closeadj / closeadj.rolling(n_dd, min_periods=n_dd).max() - 1.0
    q25 = dd.rolling(n_rng, min_periods=n_rng).quantile(0.25)
    flag = (dd > q25).astype(float).where(~q25.isna())
    return flag.rolling(n_rng, min_periods=n_rng).mean().replace([np.inf, -np.inf], np.nan)


# === DD curve smoothness (path length / direct distance) ==================


def f30dr_f30_drawdown_recovery_metrics_dd_path_directness_45d_base_v125_signal(closeadj):
    """|DD(45) - DD(45).shift(45)| / sum |DD(45).diff()|, 45d. Directness of DD path."""
    n = 45
    dd = closeadj / closeadj.rolling(n, min_periods=n).max() - 1.0
    direct = (dd - dd.shift(n)).abs()
    path = dd.diff().abs().rolling(n, min_periods=n).sum()
    return (direct / path.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# === Bars-since-trough relative to bars-since-peak =========================


def f30dr_f30_drawdown_recovery_metrics_peak_trough_age_ratio_120d_base_v126_signal(closeadj):
    """(bars since 120d high) - (bars since 120d low). Positive = trough is more recent."""
    n = 120
    rmax = closeadj.rolling(n, min_periods=n).max()
    rmin = closeadj.rolling(n, min_periods=n).min()
    at_high = (closeadj >= rmax - 1e-12).astype(float).where(~rmax.isna())
    at_low = (closeadj <= rmin + 1e-12).astype(float).where(~rmin.isna())

    def _cnt(av):
        out = pd.Series(np.nan, index=closeadj.index, dtype=float)
        cnt = np.nan
        v = av.values
        for i in range(len(closeadj)):
            if not np.isfinite(v[i]):
                continue
            if v[i] >= 0.5:
                cnt = 0.0
            else:
                cnt = (cnt + 1.0) if np.isfinite(cnt) else np.nan
            out.iat[i] = cnt
        return out
    bh = _cnt(at_high); bl = _cnt(at_low)
    return (bh - bl).replace([np.inf, -np.inf], np.nan)


# === DD's downside semivariance ============================================


def f30dr_f30_drawdown_recovery_metrics_dd_semivar_45d_base_v127_signal(closeadj):
    """Downside semivariance of log-returns conditional on being in DD(45) > 0.02."""
    n = 45
    dd_abs = (closeadj / closeadj.rolling(n, min_periods=n).max() - 1.0).abs()
    r = np.log(closeadj / closeadj.shift(1))
    rn = (r * r).where((dd_abs > 0.02) & (r < 0))
    return rn.rolling(n, min_periods=15).sum().replace([np.inf, -np.inf], np.nan)


# === DD-vs-cumret regression slope =========================================


def f30dr_f30_drawdown_recovery_metrics_dd_vs_cumret_corr_75d_base_v128_signal(closeadj):
    """75d corr between DD(60) and 60d cumulative log-ret. Recovery alignment with returns."""
    n_corr = 75
    dd = closeadj / closeadj.rolling(60, min_periods=60).max() - 1.0
    cr = np.log(closeadj).diff(60)
    return dd.rolling(n_corr, min_periods=n_corr).corr(cr).replace([np.inf, -np.inf], np.nan)


# === Mean DD on positive-return bars =======================================


def f30dr_f30_drawdown_recovery_metrics_dd_pos_vs_neg_ret_diff_60d_base_v129_signal(closeadj):
    """Mean |DD(60)| on positive-return bars MINUS mean |DD(60)| on negative-return bars.
    Differential structure decorrelates from vol-weighted DD."""
    n = 60
    dd_abs = (closeadj / closeadj.rolling(n, min_periods=n).max() - 1.0).abs()
    r = np.log(closeadj / closeadj.shift(1))
    pos = dd_abs.where(r > 0).rolling(n, min_periods=10).mean()
    neg = dd_abs.where(r < 0).rolling(n, min_periods=10).mean()
    return (pos - neg).replace([np.inf, -np.inf], np.nan)


# === DD recovery rate (per-bar) ===========================================


def f30dr_f30_drawdown_recovery_metrics_recovery_per_bar_120d_base_v130_signal(closeadj):
    """(log(close) - log(rmin120)) / (1 + bars since 120d trough). Recovery slope per bar."""
    n = 120
    rmin = closeadj.rolling(n, min_periods=n).min()
    at_low = (closeadj <= rmin + 1e-12).astype(float).where(~rmin.isna())
    bars = pd.Series(np.nan, index=closeadj.index, dtype=float)
    cnt = np.nan
    av = at_low.values
    for i in range(len(closeadj)):
        if not np.isfinite(av[i]):
            continue
        if av[i] >= 0.5:
            cnt = 0.0
        else:
            cnt = (cnt + 1.0) if np.isfinite(cnt) else np.nan
        bars.iat[i] = cnt
    return (np.log(closeadj / rmin.replace(0.0, np.nan)) / (bars + 1.0)).replace([np.inf, -np.inf], np.nan)


# === Reverse: drawup-rate per bar from peak ===============================


def f30dr_f30_drawdown_recovery_metrics_drawdown_rate_from_peak_80d_base_v131_signal(closeadj):
    """(log(rmax80) - log(close)) / (1 + bars since 80d peak). Drawdown speed."""
    n = 80
    rmax = closeadj.rolling(n, min_periods=n).max()
    at_high = (closeadj >= rmax - 1e-12).astype(float).where(~rmax.isna())
    bars = pd.Series(np.nan, index=closeadj.index, dtype=float)
    cnt = np.nan
    av = at_high.values
    for i in range(len(closeadj)):
        if not np.isfinite(av[i]):
            continue
        if av[i] >= 0.5:
            cnt = 0.0
        else:
            cnt = (cnt + 1.0) if np.isfinite(cnt) else np.nan
        bars.iat[i] = cnt
    return (np.log(rmax.replace(0.0, np.nan) / closeadj) / (bars + 1.0)).replace([np.inf, -np.inf], np.nan)


# === Frequency of recovery to new high in N ================================


def f30dr_f30_drawdown_recovery_metrics_rec_to_high_freq_180d_base_v132_signal(closeadj):
    """Count of bars in 180d where after a DD(20) <= -3%, next 10d sees new high.
    Recovery responsiveness."""
    n = 180
    dd = closeadj / closeadj.rolling(20, min_periods=20).max() - 1.0
    dip = (dd <= -0.03).astype(float).where(~dd.isna())
    rmax60 = closeadj.rolling(60, min_periods=60).max()
    new_high = (closeadj >= rmax60 - 1e-12).astype(float).where(~rmax60.isna())
    rec_within = (new_high.rolling(10, min_periods=10).max())
    flag = (dip > 0.5) & (rec_within.shift(-10) > 0.5)
    return flag.astype(float).rolling(n, min_periods=n).sum().replace([np.inf, -np.inf], np.nan)


# === Recovery quality slope normalization ==================================


def f30dr_f30_drawdown_recovery_metrics_recovery_quality_z_60d_base_v133_signal(closeadj):
    """Z-score of (close - rmin60)/(rmax60 - rmin60) within trailing 60d."""
    n = 60
    rmax = closeadj.rolling(n, min_periods=n).max()
    rmin = closeadj.rolling(n, min_periods=n).min()
    rec = (closeadj - rmin) / (rmax - rmin).replace(0.0, np.nan)
    return ((rec - rec.rolling(n, min_periods=n).mean()) / rec.rolling(n, min_periods=n).std().replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# === Difference between current DD and DD-percentile rank ==================


def f30dr_f30_drawdown_recovery_metrics_dd_z_long_240d_base_v134_signal(closeadj):
    """Z-score of DD(30) within trailing 240d."""
    n_dd = 30; n_rk = 240
    dd = closeadj / closeadj.rolling(n_dd, min_periods=n_dd).max() - 1.0
    mu = dd.rolling(n_rk, min_periods=n_rk).mean()
    sd = dd.rolling(n_rk, min_periods=n_rk).std()
    return ((dd - mu) / sd.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# === Underwater duration percentile rank ===================================


def f30dr_f30_drawdown_recovery_metrics_uw_days_rank_252d_base_v135_signal(closeadj):
    """Rank of current underwater-bars-count within trailing 252d's distribution."""
    n_uw = 90; n_rk = 252
    rmax = closeadj.rolling(n_uw, min_periods=n_uw).max()
    at_high = (closeadj >= rmax - 1e-12).astype(float).where(~rmax.isna())
    bars = pd.Series(np.nan, index=closeadj.index, dtype=float)
    cnt = np.nan
    av = at_high.values
    for i in range(len(closeadj)):
        if not np.isfinite(av[i]):
            continue
        if av[i] >= 0.5:
            cnt = 0.0
        else:
            cnt = (cnt + 1.0) if np.isfinite(cnt) else np.nan
        bars.iat[i] = cnt
    return bars.rolling(n_rk, min_periods=n_rk).apply(
        lambda x: float((np.sum(x <= x[-1]) - 1) / max(1, (len(x) - 1))), raw=True
    ).replace([np.inf, -np.inf], np.nan)


# === DD vs prior-window DD (regime change) ================================


def f30dr_f30_drawdown_recovery_metrics_dd_regime_change_60d_base_v136_signal(closeadj):
    """Mean |DD(30)| in last 60d - mean |DD(30)| in prior 60d. DD-severity regime shift."""
    n_dd = 30; n_rng = 60
    dd_abs = (closeadj / closeadj.rolling(n_dd, min_periods=n_dd).max() - 1.0).abs()
    recent = dd_abs.rolling(n_rng, min_periods=n_rng).mean()
    prior = recent.shift(n_rng)
    return (recent - prior).replace([np.inf, -np.inf], np.nan)


# === DD-curve range ========================================================


def f30dr_f30_drawdown_recovery_metrics_dd_range_75d_base_v137_signal(closeadj):
    """Range of DD(75) curve over trailing 75 bars: max(DD) - min(DD)."""
    n = 75
    dd = closeadj / closeadj.rolling(n, min_periods=n).max() - 1.0
    return (dd.rolling(n, min_periods=n).max() - dd.rolling(n, min_periods=n).min()).replace([np.inf, -np.inf], np.nan)


# === DD curve absolute integral / window length ============================


def f30dr_f30_drawdown_recovery_metrics_avg_dd_abs_25d_base_v138_signal(close):
    """Mean of |DD(25)| over 25 bars."""
    n = 25
    dd_abs = (close / close.rolling(n, min_periods=n).max() - 1.0).abs()
    return dd_abs.rolling(n, min_periods=n).mean().replace([np.inf, -np.inf], np.nan)


# === Recovery half-life proxy =============================================


def f30dr_f30_drawdown_recovery_metrics_recovery_halflife_proxy_60d_base_v139_signal(closeadj):
    """Bars within trailing 60d where DD(20) >= 0.5 * min(DD(20)) over 60d. Approx half-recovery."""
    n_dd = 20; n_rng = 60
    dd = closeadj / closeadj.rolling(n_dd, min_periods=n_dd).max() - 1.0
    mindd = dd.rolling(n_rng, min_periods=n_rng).min()
    flag = (dd >= 0.5 * mindd).astype(float).where(~mindd.isna())
    return flag.rolling(n_rng, min_periods=n_rng).sum().replace([np.inf, -np.inf], np.nan)


# === DD-trend persistence ==================================================


def f30dr_f30_drawdown_recovery_metrics_dd_trend_persistence_45d_base_v140_signal(closeadj):
    """Fraction of bars where DD(20).diff() has the same sign as the 45d-prior bar's diff."""
    n = 45
    dd_d = (closeadj / closeadj.rolling(20, min_periods=20).max() - 1.0).diff()
    same = (np.sign(dd_d) * np.sign(dd_d.shift(1)) > 0).astype(float).where(~dd_d.isna() & ~dd_d.shift(1).isna())
    return same.rolling(n, min_periods=n).mean().replace([np.inf, -np.inf], np.nan)


# === DD's distance from 0 (binary mild-DD indicator) =======================


def f30dr_f30_drawdown_recovery_metrics_mild_dd_15pct_freq_180d_base_v141_signal(closeadj):
    """Frequency of bars where DD(120) <= -15% in trailing 180d."""
    n_dd = 120; n_rng = 180
    dd = closeadj / closeadj.rolling(n_dd, min_periods=n_dd).max() - 1.0
    flag = (dd <= -0.15).astype(float).where(~dd.isna())
    return flag.rolling(n_rng, min_periods=n_rng).mean().replace([np.inf, -np.inf], np.nan)


# === DD-volatility (std of DD diffs) =======================================


def f30dr_f30_drawdown_recovery_metrics_dd_diff_std_50d_base_v142_signal(closeadj):
    """Std of DD(30).diff() over 50d — underwater path volatility."""
    n_dd = 30; n_rng = 50
    dd_d = (closeadj / closeadj.rolling(n_dd, min_periods=n_dd).max() - 1.0).diff()
    return dd_d.rolling(n_rng, min_periods=n_rng).std().replace([np.inf, -np.inf], np.nan)


# === Calmar-style with shorter window ======================================


def f30dr_f30_drawdown_recovery_metrics_calmar_60d_base_v143_signal(closeadj):
    """60d log-return / |max DD over 60d|."""
    n = 60
    ret = np.log(closeadj / closeadj.shift(n))
    dd = closeadj / closeadj.rolling(n, min_periods=n).max() - 1.0
    mdd = dd.rolling(n, min_periods=n).min().abs()
    return (ret / mdd.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# === DD-conditional volatility =============================================


def f30dr_f30_drawdown_recovery_metrics_realvol_in_dd_45d_base_v144_signal(closeadj):
    """Realized vol of returns ONLY on bars where DD(45) <= -2%, 45d window."""
    n = 45
    dd = closeadj / closeadj.rolling(n, min_periods=n).max() - 1.0
    r = np.log(closeadj / closeadj.shift(1)).where(dd <= -0.02)
    return r.rolling(n, min_periods=10).std().replace([np.inf, -np.inf], np.nan)


# === DD-shape sharpness (kurtosis of diffs) ================================


def f30dr_f30_drawdown_recovery_metrics_dd_diff_kurt_90d_base_v145_signal(closeadj):
    """Kurt of DD(45).diff() over 90 bars."""
    n_dd = 45; n_rng = 90
    dd_d = (closeadj / closeadj.rolling(n_dd, min_periods=n_dd).max() - 1.0).diff()
    return dd_d.rolling(n_rng, min_periods=n_rng).kurt().replace([np.inf, -np.inf], np.nan)


# === Drawup percentile rank ================================================


def f30dr_f30_drawdown_recovery_metrics_drawup_rank_120d_base_v146_signal(closeadj):
    """Rank of current DU(30) within trailing 120d drawup-distribution."""
    n_du = 30; n_rk = 120
    du = closeadj / closeadj.rolling(n_du, min_periods=n_du).min() - 1.0
    return du.rolling(n_rk, min_periods=n_rk).apply(
        lambda x: float((np.sum(x <= x[-1]) - 1) / max(1, (len(x) - 1))), raw=True
    ).replace([np.inf, -np.inf], np.nan)


# === DD's relationship to RSI-like indicator (use only DD framework) =======


def f30dr_f30_drawdown_recovery_metrics_dd_arctan_dur_45d_base_v147_signal(closeadj):
    """arctan((bars since 45d-high) / 15). Bounded UW-duration signal at 45d window."""
    n = 45
    rmax = closeadj.rolling(n, min_periods=n).max()
    at_high = (closeadj >= rmax - 1e-12).astype(float).where(~rmax.isna())
    bars = pd.Series(np.nan, index=closeadj.index, dtype=float)
    cnt = np.nan
    av = at_high.values
    for i in range(len(closeadj)):
        if not np.isfinite(av[i]):
            continue
        if av[i] >= 0.5:
            cnt = 0.0
        else:
            cnt = (cnt + 1.0) if np.isfinite(cnt) else np.nan
        bars.iat[i] = cnt
    return np.arctan(bars / 15.0).replace([np.inf, -np.inf], np.nan)


# === DD-and-volume composite ===============================================


def f30dr_f30_drawdown_recovery_metrics_dd_volume_z_45d_base_v148_signal(closeadj, volume):
    """45d Z-score of (|DD(45)| * log(volume)). Vol-weighted DD severity."""
    n = 45
    dd_abs = (closeadj / closeadj.rolling(n, min_periods=n).max() - 1.0).abs()
    x = dd_abs * np.log(volume.replace(0.0, np.nan))
    return ((x - x.rolling(n, min_periods=n).mean()) / x.rolling(n, min_periods=n).std().replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# === Recovery-symmetry index ==============================================


def f30dr_f30_drawdown_recovery_metrics_recovery_symmetry_75d_base_v149_signal(closeadj):
    """For trailing 75d window: (recovery-half bars) / (drawdown-half bars).
    Drawdown-half: bars where DD20 was deepening. Recovery-half: bars where DD20 was lifting."""
    n_dd = 20; n_rng = 75
    dd_d = (closeadj / closeadj.rolling(n_dd, min_periods=n_dd).max() - 1.0).diff()
    rec = (dd_d > 0).astype(float).where(~dd_d.isna())
    deep = (dd_d < 0).astype(float).where(~dd_d.isna())
    rs = rec.rolling(n_rng, min_periods=n_rng).sum()
    ds = deep.rolling(n_rng, min_periods=n_rng).sum()
    return (rs / ds.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# === DD-cross-time-bucket comparison =======================================


def f30dr_f30_drawdown_recovery_metrics_uw_bucket_diff_60d_base_v150_signal(closeadj):
    """UW-frac in trailing 30d minus UW-frac in prior 30d. UW-frequency change."""
    n_each = 30
    rmax = closeadj.rolling(n_each, min_periods=n_each).max()
    below = (closeadj < rmax - 1e-12).astype(float).where(~rmax.isna())
    recent = below.rolling(n_each, min_periods=n_each).mean()
    prior = recent.shift(n_each)
    return (recent - prior).replace([np.inf, -np.inf], np.nan)


# ---------------------------------------------------------------------------
# Registry
# ---------------------------------------------------------------------------


f30_drawdown_recovery_metrics_base_076_150_REGISTRY = {
    "f30dr_f30_drawdown_recovery_metrics_dd_15d_base_v076_signal": {"inputs": ["close"], "func": f30dr_f30_drawdown_recovery_metrics_dd_15d_base_v076_signal},
    "f30dr_f30_drawdown_recovery_metrics_dd_42d_base_v077_signal": {"inputs": ["closeadj"], "func": f30dr_f30_drawdown_recovery_metrics_dd_42d_base_v077_signal},
    "f30dr_f30_drawdown_recovery_metrics_dd_378d_base_v078_signal": {"inputs": ["closeadj"], "func": f30dr_f30_drawdown_recovery_metrics_dd_378d_base_v078_signal},
    "f30dr_f30_drawdown_recovery_metrics_drawup_40d_base_v079_signal": {"inputs": ["closeadj"], "func": f30dr_f30_drawdown_recovery_metrics_drawup_40d_base_v079_signal},
    "f30dr_f30_drawdown_recovery_metrics_drawup_252d_base_v080_signal": {"inputs": ["closeadj"], "func": f30dr_f30_drawdown_recovery_metrics_drawup_252d_base_v080_signal},
    "f30dr_f30_drawdown_recovery_metrics_net_du_dd_30d_base_v081_signal": {"inputs": ["close"], "func": f30dr_f30_drawdown_recovery_metrics_net_du_dd_30d_base_v081_signal},
    "f30dr_f30_drawdown_recovery_metrics_dd_du_product_150d_base_v082_signal": {"inputs": ["closeadj"], "func": f30dr_f30_drawdown_recovery_metrics_dd_du_product_150d_base_v082_signal},
    "f30dr_f30_drawdown_recovery_metrics_dd_curve_concavity_60d_base_v083_signal": {"inputs": ["closeadj"], "func": f30dr_f30_drawdown_recovery_metrics_dd_curve_concavity_60d_base_v083_signal},
    "f30dr_f30_drawdown_recovery_metrics_local_trough_count_120d_base_v084_signal": {"inputs": ["closeadj"], "func": f30dr_f30_drawdown_recovery_metrics_local_trough_count_120d_base_v084_signal},
    "f30dr_f30_drawdown_recovery_metrics_dd_q10_60d_base_v085_signal": {"inputs": ["closeadj"], "func": f30dr_f30_drawdown_recovery_metrics_dd_q10_60d_base_v085_signal},
    "f30dr_f30_drawdown_recovery_metrics_dd_iqr_100d_base_v086_signal": {"inputs": ["closeadj"], "func": f30dr_f30_drawdown_recovery_metrics_dd_iqr_100d_base_v086_signal},
    "f30dr_f30_drawdown_recovery_metrics_newhigh_streak_60d_base_v087_signal": {"inputs": ["closeadj"], "func": f30dr_f30_drawdown_recovery_metrics_newhigh_streak_60d_base_v087_signal},
    "f30dr_f30_drawdown_recovery_metrics_newlow_streak_45d_base_v088_signal": {"inputs": ["closeadj"], "func": f30dr_f30_drawdown_recovery_metrics_newlow_streak_45d_base_v088_signal},
    "f30dr_f30_drawdown_recovery_metrics_dd_atr_units_90d_base_v089_signal": {"inputs": ["high", "low", "closeadj"], "func": f30dr_f30_drawdown_recovery_metrics_dd_atr_units_90d_base_v089_signal},
    "f30dr_f30_drawdown_recovery_metrics_dd_under_negskew_45d_base_v090_signal": {"inputs": ["closeadj"], "func": f30dr_f30_drawdown_recovery_metrics_dd_under_negskew_45d_base_v090_signal},
    "f30dr_f30_drawdown_recovery_metrics_ret_in_dd_60d_base_v091_signal": {"inputs": ["closeadj"], "func": f30dr_f30_drawdown_recovery_metrics_ret_in_dd_60d_base_v091_signal},
    "f30dr_f30_drawdown_recovery_metrics_corr_dd_volume_60d_base_v092_signal": {"inputs": ["closeadj", "volume"], "func": f30dr_f30_drawdown_recovery_metrics_corr_dd_volume_60d_base_v092_signal},
    "f30dr_f30_drawdown_recovery_metrics_dd_regslope_30d_base_v093_signal": {"inputs": ["closeadj"], "func": f30dr_f30_drawdown_recovery_metrics_dd_regslope_30d_base_v093_signal},
    "f30dr_f30_drawdown_recovery_metrics_dd_regslope_120d_base_v094_signal": {"inputs": ["closeadj"], "func": f30dr_f30_drawdown_recovery_metrics_dd_regslope_120d_base_v094_signal},
    "f30dr_f30_drawdown_recovery_metrics_dd_rsq_time_60d_base_v095_signal": {"inputs": ["closeadj"], "func": f30dr_f30_drawdown_recovery_metrics_dd_rsq_time_60d_base_v095_signal},
    "f30dr_f30_drawdown_recovery_metrics_dd_vol_ratio_75d_base_v096_signal": {"inputs": ["closeadj"], "func": f30dr_f30_drawdown_recovery_metrics_dd_vol_ratio_75d_base_v096_signal},
    "f30dr_f30_drawdown_recovery_metrics_phase_imbalance_45d_base_v097_signal": {"inputs": ["closeadj"], "func": f30dr_f30_drawdown_recovery_metrics_phase_imbalance_45d_base_v097_signal},
    "f30dr_f30_drawdown_recovery_metrics_uw_du_integral_diff_60d_base_v098_signal": {"inputs": ["closeadj"], "func": f30dr_f30_drawdown_recovery_metrics_uw_du_integral_diff_60d_base_v098_signal},
    "f30dr_f30_drawdown_recovery_metrics_dd_severity_duration_60d_base_v099_signal": {"inputs": ["closeadj"], "func": f30dr_f30_drawdown_recovery_metrics_dd_severity_duration_60d_base_v099_signal},
    "f30dr_f30_drawdown_recovery_metrics_uw_30_vs_120_base_v100_signal": {"inputs": ["closeadj"], "func": f30dr_f30_drawdown_recovery_metrics_uw_30_vs_120_base_v100_signal},
    "f30dr_f30_drawdown_recovery_metrics_dd_sharpe_60d_base_v101_signal": {"inputs": ["closeadj"], "func": f30dr_f30_drawdown_recovery_metrics_dd_sharpe_60d_base_v101_signal},
    "f30dr_f30_drawdown_recovery_metrics_max_dd_per_bar_180d_base_v102_signal": {"inputs": ["closeadj"], "func": f30dr_f30_drawdown_recovery_metrics_max_dd_per_bar_180d_base_v102_signal},
    "f30dr_f30_drawdown_recovery_metrics_recovery_completeness_60d_base_v103_signal": {"inputs": ["closeadj"], "func": f30dr_f30_drawdown_recovery_metrics_recovery_completeness_60d_base_v103_signal},
    "f30dr_f30_drawdown_recovery_metrics_uw_runs_skew_120d_base_v104_signal": {"inputs": ["closeadj"], "func": f30dr_f30_drawdown_recovery_metrics_uw_runs_skew_120d_base_v104_signal},
    "f30dr_f30_drawdown_recovery_metrics_martin_ratio_90d_base_v105_signal": {"inputs": ["closeadj"], "func": f30dr_f30_drawdown_recovery_metrics_martin_ratio_90d_base_v105_signal},
    "f30dr_f30_drawdown_recovery_metrics_max_run_dd_weighted_120d_base_v106_signal": {"inputs": ["closeadj"], "func": f30dr_f30_drawdown_recovery_metrics_max_run_dd_weighted_120d_base_v106_signal},
    "f30dr_f30_drawdown_recovery_metrics_dd_below_med_freq_50d_base_v107_signal": {"inputs": ["closeadj"], "func": f30dr_f30_drawdown_recovery_metrics_dd_below_med_freq_50d_base_v107_signal},
    "f30dr_f30_drawdown_recovery_metrics_recovery_weighted_return_75d_base_v108_signal": {"inputs": ["closeadj"], "func": f30dr_f30_drawdown_recovery_metrics_recovery_weighted_return_75d_base_v108_signal},
    "f30dr_f30_drawdown_recovery_metrics_dd_autocorr_60d_base_v109_signal": {"inputs": ["closeadj"], "func": f30dr_f30_drawdown_recovery_metrics_dd_autocorr_60d_base_v109_signal},
    "f30dr_f30_drawdown_recovery_metrics_dd_max_mean_ratio_100d_base_v110_signal": {"inputs": ["closeadj"], "func": f30dr_f30_drawdown_recovery_metrics_dd_max_mean_ratio_100d_base_v110_signal},
    "f30dr_f30_drawdown_recovery_metrics_dd_using_lows_25d_base_v111_signal": {"inputs": ["high", "low"], "func": f30dr_f30_drawdown_recovery_metrics_dd_using_lows_25d_base_v111_signal},
    "f30dr_f30_drawdown_recovery_metrics_intrabar_dd_minus_close_dd_100d_base_v112_signal": {"inputs": ["high", "low", "closeadj"], "func": f30dr_f30_drawdown_recovery_metrics_intrabar_dd_minus_close_dd_100d_base_v112_signal},
    "f30dr_f30_drawdown_recovery_metrics_max_dd_step_60d_base_v113_signal": {"inputs": ["closeadj"], "func": f30dr_f30_drawdown_recovery_metrics_max_dd_step_60d_base_v113_signal},
    "f30dr_f30_drawdown_recovery_metrics_max_recovery_step_60d_base_v114_signal": {"inputs": ["closeadj"], "func": f30dr_f30_drawdown_recovery_metrics_max_recovery_step_60d_base_v114_signal},
    "f30dr_f30_drawdown_recovery_metrics_neg_pos_diff_ratio_50d_base_v115_signal": {"inputs": ["closeadj"], "func": f30dr_f30_drawdown_recovery_metrics_neg_pos_diff_ratio_50d_base_v115_signal},
    "f30dr_f30_drawdown_recovery_metrics_tanh_dd_dur_75d_base_v116_signal": {"inputs": ["closeadj"], "func": f30dr_f30_drawdown_recovery_metrics_tanh_dd_dur_75d_base_v116_signal},
    "f30dr_f30_drawdown_recovery_metrics_dd_in_highvol_45d_base_v117_signal": {"inputs": ["closeadj"], "func": f30dr_f30_drawdown_recovery_metrics_dd_in_highvol_45d_base_v117_signal},
    "f30dr_f30_drawdown_recovery_metrics_cum_recovery_50d_base_v118_signal": {"inputs": ["closeadj"], "func": f30dr_f30_drawdown_recovery_metrics_cum_recovery_50d_base_v118_signal},
    "f30dr_f30_drawdown_recovery_metrics_cum_deepening_50d_base_v119_signal": {"inputs": ["closeadj"], "func": f30dr_f30_drawdown_recovery_metrics_cum_deepening_50d_base_v119_signal},
    "f30dr_f30_drawdown_recovery_metrics_rank_dd_180d_base_v120_signal": {"inputs": ["closeadj"], "func": f30dr_f30_drawdown_recovery_metrics_rank_dd_180d_base_v120_signal},
    "f30dr_f30_drawdown_recovery_metrics_dd_room_252d_base_v121_signal": {"inputs": ["closeadj"], "func": f30dr_f30_drawdown_recovery_metrics_dd_room_252d_base_v121_signal},
    "f30dr_f30_drawdown_recovery_metrics_vol_weighted_dd_60d_base_v122_signal": {"inputs": ["closeadj", "volume"], "func": f30dr_f30_drawdown_recovery_metrics_vol_weighted_dd_60d_base_v122_signal},
    "f30dr_f30_drawdown_recovery_metrics_uw_median_run_180d_base_v123_signal": {"inputs": ["closeadj"], "func": f30dr_f30_drawdown_recovery_metrics_uw_median_run_180d_base_v123_signal},
    "f30dr_f30_drawdown_recovery_metrics_dd_above_q25_freq_90d_base_v124_signal": {"inputs": ["closeadj"], "func": f30dr_f30_drawdown_recovery_metrics_dd_above_q25_freq_90d_base_v124_signal},
    "f30dr_f30_drawdown_recovery_metrics_dd_path_directness_45d_base_v125_signal": {"inputs": ["closeadj"], "func": f30dr_f30_drawdown_recovery_metrics_dd_path_directness_45d_base_v125_signal},
    "f30dr_f30_drawdown_recovery_metrics_peak_trough_age_ratio_120d_base_v126_signal": {"inputs": ["closeadj"], "func": f30dr_f30_drawdown_recovery_metrics_peak_trough_age_ratio_120d_base_v126_signal},
    "f30dr_f30_drawdown_recovery_metrics_dd_semivar_45d_base_v127_signal": {"inputs": ["closeadj"], "func": f30dr_f30_drawdown_recovery_metrics_dd_semivar_45d_base_v127_signal},
    "f30dr_f30_drawdown_recovery_metrics_dd_vs_cumret_corr_75d_base_v128_signal": {"inputs": ["closeadj"], "func": f30dr_f30_drawdown_recovery_metrics_dd_vs_cumret_corr_75d_base_v128_signal},
    "f30dr_f30_drawdown_recovery_metrics_dd_pos_vs_neg_ret_diff_60d_base_v129_signal": {"inputs": ["closeadj"], "func": f30dr_f30_drawdown_recovery_metrics_dd_pos_vs_neg_ret_diff_60d_base_v129_signal},
    "f30dr_f30_drawdown_recovery_metrics_recovery_per_bar_120d_base_v130_signal": {"inputs": ["closeadj"], "func": f30dr_f30_drawdown_recovery_metrics_recovery_per_bar_120d_base_v130_signal},
    "f30dr_f30_drawdown_recovery_metrics_drawdown_rate_from_peak_80d_base_v131_signal": {"inputs": ["closeadj"], "func": f30dr_f30_drawdown_recovery_metrics_drawdown_rate_from_peak_80d_base_v131_signal},
    "f30dr_f30_drawdown_recovery_metrics_rec_to_high_freq_180d_base_v132_signal": {"inputs": ["closeadj"], "func": f30dr_f30_drawdown_recovery_metrics_rec_to_high_freq_180d_base_v132_signal},
    "f30dr_f30_drawdown_recovery_metrics_recovery_quality_z_60d_base_v133_signal": {"inputs": ["closeadj"], "func": f30dr_f30_drawdown_recovery_metrics_recovery_quality_z_60d_base_v133_signal},
    "f30dr_f30_drawdown_recovery_metrics_dd_z_long_240d_base_v134_signal": {"inputs": ["closeadj"], "func": f30dr_f30_drawdown_recovery_metrics_dd_z_long_240d_base_v134_signal},
    "f30dr_f30_drawdown_recovery_metrics_uw_days_rank_252d_base_v135_signal": {"inputs": ["closeadj"], "func": f30dr_f30_drawdown_recovery_metrics_uw_days_rank_252d_base_v135_signal},
    "f30dr_f30_drawdown_recovery_metrics_dd_regime_change_60d_base_v136_signal": {"inputs": ["closeadj"], "func": f30dr_f30_drawdown_recovery_metrics_dd_regime_change_60d_base_v136_signal},
    "f30dr_f30_drawdown_recovery_metrics_dd_range_75d_base_v137_signal": {"inputs": ["closeadj"], "func": f30dr_f30_drawdown_recovery_metrics_dd_range_75d_base_v137_signal},
    "f30dr_f30_drawdown_recovery_metrics_avg_dd_abs_25d_base_v138_signal": {"inputs": ["close"], "func": f30dr_f30_drawdown_recovery_metrics_avg_dd_abs_25d_base_v138_signal},
    "f30dr_f30_drawdown_recovery_metrics_recovery_halflife_proxy_60d_base_v139_signal": {"inputs": ["closeadj"], "func": f30dr_f30_drawdown_recovery_metrics_recovery_halflife_proxy_60d_base_v139_signal},
    "f30dr_f30_drawdown_recovery_metrics_dd_trend_persistence_45d_base_v140_signal": {"inputs": ["closeadj"], "func": f30dr_f30_drawdown_recovery_metrics_dd_trend_persistence_45d_base_v140_signal},
    "f30dr_f30_drawdown_recovery_metrics_mild_dd_15pct_freq_180d_base_v141_signal": {"inputs": ["closeadj"], "func": f30dr_f30_drawdown_recovery_metrics_mild_dd_15pct_freq_180d_base_v141_signal},
    "f30dr_f30_drawdown_recovery_metrics_dd_diff_std_50d_base_v142_signal": {"inputs": ["closeadj"], "func": f30dr_f30_drawdown_recovery_metrics_dd_diff_std_50d_base_v142_signal},
    "f30dr_f30_drawdown_recovery_metrics_calmar_60d_base_v143_signal": {"inputs": ["closeadj"], "func": f30dr_f30_drawdown_recovery_metrics_calmar_60d_base_v143_signal},
    "f30dr_f30_drawdown_recovery_metrics_realvol_in_dd_45d_base_v144_signal": {"inputs": ["closeadj"], "func": f30dr_f30_drawdown_recovery_metrics_realvol_in_dd_45d_base_v144_signal},
    "f30dr_f30_drawdown_recovery_metrics_dd_diff_kurt_90d_base_v145_signal": {"inputs": ["closeadj"], "func": f30dr_f30_drawdown_recovery_metrics_dd_diff_kurt_90d_base_v145_signal},
    "f30dr_f30_drawdown_recovery_metrics_drawup_rank_120d_base_v146_signal": {"inputs": ["closeadj"], "func": f30dr_f30_drawdown_recovery_metrics_drawup_rank_120d_base_v146_signal},
    "f30dr_f30_drawdown_recovery_metrics_dd_arctan_dur_45d_base_v147_signal": {"inputs": ["closeadj"], "func": f30dr_f30_drawdown_recovery_metrics_dd_arctan_dur_45d_base_v147_signal},
    "f30dr_f30_drawdown_recovery_metrics_dd_volume_z_45d_base_v148_signal": {"inputs": ["closeadj", "volume"], "func": f30dr_f30_drawdown_recovery_metrics_dd_volume_z_45d_base_v148_signal},
    "f30dr_f30_drawdown_recovery_metrics_recovery_symmetry_75d_base_v149_signal": {"inputs": ["closeadj"], "func": f30dr_f30_drawdown_recovery_metrics_recovery_symmetry_75d_base_v149_signal},
    "f30dr_f30_drawdown_recovery_metrics_uw_bucket_diff_60d_base_v150_signal": {"inputs": ["closeadj"], "func": f30dr_f30_drawdown_recovery_metrics_uw_bucket_diff_60d_base_v150_signal},
}


# ---------------------------------------------------------------------------
# Self-test
# ---------------------------------------------------------------------------


def _synthetic_inputs(n: int = 800, seed: int = 42) -> pd.DataFrame:
    rng = np.random.default_rng(seed)
    seg = n // 4
    rest = n - 3 * seg
    ret = np.concatenate([
        rng.normal(0.0012, 0.011, seg),
        rng.normal(-0.0005, 0.018, seg),
        rng.normal(-0.0010, 0.014, seg),
        rng.normal(0.0008, 0.012, rest),
    ])
    close = 50.0 * np.exp(np.cumsum(ret))
    adj_drift = rng.normal(0.0, 0.0003, size=n).cumsum()
    closeadj = close * np.exp(adj_drift)
    intraday = rng.normal(0.0, 0.008, size=n)
    open_ = close * np.exp(-intraday * 0.5)
    high = np.maximum(close, open_) * np.exp(np.abs(rng.normal(0.0, 0.006, size=n)))
    low = np.minimum(close, open_) * np.exp(-np.abs(rng.normal(0.0, 0.006, size=n)))
    volume = rng.lognormal(mean=13.0, sigma=0.6, size=n)
    idx = pd.RangeIndex(n)
    return pd.DataFrame({
        "open": pd.Series(open_, index=idx, dtype=float),
        "high": pd.Series(high, index=idx, dtype=float),
        "low": pd.Series(low, index=idx, dtype=float),
        "close": pd.Series(close, index=idx, dtype=float),
        "closeadj": pd.Series(closeadj, index=idx, dtype=float),
        "volume": pd.Series(volume, index=idx, dtype=float),
    })


def _self_test() -> None:
    df = _synthetic_inputs(n=800, seed=42)
    results: dict[str, pd.Series] = {}
    for name, entry in f30_drawdown_recovery_metrics_base_076_150_REGISTRY.items():
        args = [df[col] for col in entry["inputs"]]
        out = entry["func"](*args)
        assert isinstance(out, pd.Series), f"{name}: not a Series"
        assert len(out) == len(df), f"{name}: length mismatch"
        clean = out.dropna()
        assert len(clean) > 0, f"{name}: all NaN"
        assert float(clean.std()) > 0.0 or clean.nunique() > 1, f"{name}: constant/all-zero"
        results[name] = out

    warm = 252
    coverage_ok = sum(1 for s in results.values() if s.iloc[warm:].isna().mean() < 0.5)
    frac = coverage_ok / len(results)
    assert frac >= 0.80, f"NaN-coverage too low: {frac:.2%} have <50% NaN after warm-up"

    aligned = pd.concat({n: results[n] for n in results}, axis=1).iloc[warm:]
    aligned = aligned.replace([np.inf, -np.inf], np.nan)
    corr = aligned.corr(min_periods=50).abs()
    np.fill_diagonal(corr.values, 0.0)
    max_corr = float(corr.max().max())
    if max_corr > 0.95:
        print(f"FAILING max |corr| = {max_corr:.4f}. Top pairs:")
        for i, a in enumerate(corr.columns):
            for j, b in enumerate(corr.columns):
                if j > i and corr.iloc[i, j] > 0.94:
                    print(f"  {a}  vs  {b}  ->  {corr.iloc[i, j]:.4f}")
    assert max_corr <= 0.95 + 1e-9, f"max pairwise |corr|={max_corr:.4f} exceeds 0.95"
    print(f"OK base_076_150: {len(results)} features, max |corr|={max_corr:.4f}, coverage_ok={frac:.2%}")


if __name__ == "__main__":
    _self_test()
