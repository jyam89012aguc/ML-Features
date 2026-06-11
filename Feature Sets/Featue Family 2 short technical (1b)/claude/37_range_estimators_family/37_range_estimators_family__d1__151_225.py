"""range_estimators_family d1 features 151-225 — Pipeline 1b-technical.

Gap-filling extension to family 37. 75 distinct hypotheses NOT covered by
the original 150 features. Sources for the canonical indicators added here:

  - Choppiness Index (CHOP): Bill Dreiss
  - Vertical Horizontal Filter (VHF): Adam White 1991
  - Mass Index: Donald Dorsey
  - NR4 / NR7 narrow range patterns: Toby Crabel, "Day Trading with Short-Term Price Patterns"
  - Donchian width: Richard Donchian
  - Wilder Directional Movement (+DM / -DM / +DI / -DI / DX): J. Welles Wilder 1978
  - Bipower from range (adaptation of Barndorff-Nielsen & Shephard BPV to log H/L)
  - Range Hurst exponent: R/S analysis applied to the range time series

Buckets in this file:
  BB Choppiness Index (151-156)
  CC Vertical Horizontal Filter (157-161)
  DD Mass Index (162-165)
  EE NR4 / NR7 / WR4 / WR7 narrow- and wide-range patterns (166-172)
  FF Inside / Outside bars (173-177)
  GG Donchian width multi-horizon (178-184)
  HH Multi-day rolling range vs additive (185-188)
  II Hi-Lo midpoint position (189-192)
  JJ Gap fill rate (193-196)
  KK Open-to-high vs Open-to-low asymmetry (197-200)
  LL Wilder DM+ / DM- / DI+ / DI- / DX (201-206)
  MM Range Hurst / variance ratio (207-210)
  NN Bipower range (jump-robust) (211-214)
  OO Range distribution moments at multi horizons (215-218)
  PP Range autocorrelation at multi lags (219-222)
  QQ TR-breakout + persistent expansion/compression composites (223-225)

Inputs: SEP OHLCV only. PIT-clean: right-anchored, explicit min_periods,
no centered windows, no .shift(N). Self-contained helpers — no cross-
family imports.
"""
import numpy as np
import pandas as pd

YDAYS = 252
QDAYS = 63
MDAYS = 21
WDAYS = 5
DDAYS_2Y = 504
DDAYS_3Y = 756
DDAYS_5Y = 1260


# ---------------------------- helpers ----------------------------

def _safe_log(s, eps=1e-12):
    return np.log(s.where(s > eps, np.nan))


def _safe_div(num, den):
    if isinstance(den, pd.Series):
        d = den.replace(0, np.nan)
    else:
        d = np.where(den == 0, np.nan, den)
    out = num / d
    if isinstance(out, pd.Series):
        return out.replace([np.inf, -np.inf], np.nan)
    idx = num.index if hasattr(num, "index") else None
    return pd.Series(out, index=idx).replace([np.inf, -np.inf], np.nan)


def _rolling_zscore(s, window, min_periods=None):
    if min_periods is None:
        min_periods = max(window // 3, 2)
    m = s.rolling(window, min_periods=min_periods).mean()
    sd = s.rolling(window, min_periods=min_periods).std()
    return (s - m) / sd.replace(0, np.nan)


def _true_range(high, low, close):
    pc = close.shift(1)
    return pd.concat([high - low, (high - pc).abs(), (low - pc).abs()], axis=1).max(axis=1)


def _atr(high, low, close, n=21):
    return _true_range(high, low, close).rolling(n, min_periods=max(n // 3, 2)).mean()


def _rolling_slope(s, n, min_periods=None):
    if min_periods is None:
        min_periods = max(n // 3, 2)
    def _slope(w):
        valid = ~np.isnan(w)
        if valid.sum() < min_periods:
            return np.nan
        x = np.arange(len(w), dtype=float)
        if valid.all():
            wv = w
        else:
            x = x[valid]
            wv = w[valid]
        xm = x.mean(); wm = wv.mean()
        num = ((x - xm) * (wv - wm)).sum()
        den = ((x - xm) ** 2).sum()
        return num / den if den != 0 else np.nan
    return s.rolling(n, min_periods=min_periods).apply(_slope, raw=True)


# ============================================================
# Bucket BB — Choppiness Index (CHOP) (151-156)
# CHOP = 100 * log10(sum(TR)_N / (max(H)_N - min(L)_N)) / log10(N).
# >62 = trending, <38 = ranging.
# ============================================================

def _chop(high: pd.Series, low: pd.Series, close: pd.Series, n: int) -> pd.Series:
    tr = _true_range(high, low, close)
    sum_tr = tr.rolling(n, min_periods=max(n // 2, 2)).sum()
    hi_n = high.rolling(n, min_periods=max(n // 2, 2)).max()
    lo_n = low.rolling(n, min_periods=max(n // 2, 2)).min()
    rng = hi_n - lo_n
    return 100.0 * np.log10(_safe_div(sum_tr, rng)) / np.log10(float(n))


def f37_rges_151_chop_14d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Choppiness Index over 14d (Dreiss standard) — trend (>62) vs range (<38) classifier."""
    return _chop(high, low, close, 14)


def f37_rges_152_chop_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Choppiness Index over 21d — monthly trend/range classifier."""
    return _chop(high, low, close, MDAYS)


def f37_rges_153_chop_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Choppiness Index over 63d — quarterly trend/range classifier."""
    return _chop(high, low, close, QDAYS)


def f37_rges_154_chop_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Choppiness Index over 252d — annual trend/range regime."""
    return _chop(high, low, close, YDAYS)


def f37_rges_155_chop_zscore_in_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Z-score of 21d CHOP within trailing 252d distribution — chop-regime extremity."""
    c = _chop(high, low, close, MDAYS)
    return _rolling_zscore(c, YDAYS, min_periods=QDAYS)


def f37_rges_156_chop_regime_indicator_14d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Indicator: 14d CHOP > 62 (trending) -> +1, < 38 (ranging) -> -1, else 0."""
    c = _chop(high, low, close, 14)
    out = pd.Series(0.0, index=close.index)
    out = out.where(~(c > 62.0), 1.0)
    out = out.where(~(c < 38.0), -1.0)
    return out.where(c.notna(), np.nan)


# ============================================================
# Bucket CC — Vertical Horizontal Filter (VHF) (157-161)
# VHF = (max(C)_N - min(C)_N) / sum(|delta C|)_N.
# High = trending, low = ranging.
# ============================================================

def _vhf(close: pd.Series, n: int) -> pd.Series:
    hi = close.rolling(n, min_periods=max(n // 2, 2)).max()
    lo = close.rolling(n, min_periods=max(n // 2, 2)).min()
    dc = close.diff().abs()
    sdc = dc.rolling(n, min_periods=max(n // 2, 2)).sum()
    return _safe_div(hi - lo, sdc)


def f37_rges_157_vhf_14d(close: pd.Series) -> pd.Series:
    """VHF over 14d (Adam White standard) — trend-vs-range strength."""
    return _vhf(close, 14)


def f37_rges_158_vhf_28d(close: pd.Series) -> pd.Series:
    """VHF over 28d — monthly trend-strength."""
    return _vhf(close, 28)


def f37_rges_159_vhf_63d(close: pd.Series) -> pd.Series:
    """VHF over 63d — quarterly trend-strength."""
    return _vhf(close, QDAYS)


def f37_rges_160_vhf_252d(close: pd.Series) -> pd.Series:
    """VHF over 252d — annual trend-strength regime."""
    return _vhf(close, YDAYS)


def f37_rges_161_vhf_zscore_in_252d(close: pd.Series) -> pd.Series:
    """Z-score of 28d VHF within trailing 252d distribution — trend-strength extremity."""
    v = _vhf(close, 28)
    return _rolling_zscore(v, YDAYS, min_periods=QDAYS)


# ============================================================
# Bucket DD — Mass Index (Dorsey) (162-165)
# Mass = sum_{i=0..N-1} of ( EMA9(H-L) / EMA9(EMA9(H-L)) ).
# Reversal bulge when Mass > 27 then drops below 26.5.
# ============================================================

def _mass_index(high: pd.Series, low: pd.Series, n: int) -> pd.Series:
    rng = high - low
    ema1 = rng.ewm(span=9, adjust=False, min_periods=5).mean()
    ema2 = ema1.ewm(span=9, adjust=False, min_periods=5).mean()
    ratio = _safe_div(ema1, ema2)
    return ratio.rolling(n, min_periods=max(n // 2, 2)).sum()


def f37_rges_162_mass_index_9d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Mass Index summed over 9 bars (short Dorsey window) — short-horizon reversal-bulge proxy."""
    return _mass_index(high, low, 9)


def f37_rges_163_mass_index_25d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Mass Index summed over 25 bars (Dorsey standard) — classical reversal bulge."""
    return _mass_index(high, low, 25)


def f37_rges_164_mass_index_63d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Mass Index summed over 63 bars — quarter-horizon reversal-bulge accumulation."""
    return _mass_index(high, low, QDAYS)


def f37_rges_165_mass_index_reversal_bulge_25d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Indicator: Mass(25) crossed above 27 in last 5 bars AND now <26.5 — Dorsey reversal-bulge signal."""
    m = _mass_index(high, low, 25)
    above27 = (m > 27.0).rolling(WDAYS, min_periods=2).max()  # any bar above 27 in last 5
    drop = (m < 26.5)
    return (above27.astype(float) * drop.astype(float)).where(m.notna(), np.nan)


# ============================================================
# Bucket EE — NR4 / NR7 / WR4 / WR7 narrow- and wide-range (166-172)
# Toby Crabel: NR4 = today's range is narrowest in last 4 days.
# NR7 = narrowest in last 7. WR variants are wide-range analogs.
# ============================================================

def f37_rges_166_nr4_indicator(high: pd.Series, low: pd.Series) -> pd.Series:
    """Indicator: today's H-L is the narrowest in last 4 bars (NR4 pattern, Crabel)."""
    rng = high - low
    rmin4 = rng.rolling(4, min_periods=4).min()
    return (rng <= rmin4).astype(float).where(rmin4.notna(), np.nan)


def f37_rges_167_nr7_indicator(high: pd.Series, low: pd.Series) -> pd.Series:
    """Indicator: today's H-L is the narrowest in last 7 bars (NR7 pattern)."""
    rng = high - low
    rmin7 = rng.rolling(7, min_periods=7).min()
    return (rng <= rmin7).astype(float).where(rmin7.notna(), np.nan)


def f37_rges_168_nr4_count_in_21d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of NR4 occurrences in trailing 21d — narrow-range cluster intensity."""
    rng = high - low
    rmin4 = rng.rolling(4, min_periods=4).min()
    nr4 = (rng <= rmin4).astype(float).where(rmin4.notna(), np.nan)
    return nr4.rolling(MDAYS, min_periods=WDAYS).sum()


def f37_rges_169_nr7_count_in_21d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of NR7 occurrences in trailing 21d."""
    rng = high - low
    rmin7 = rng.rolling(7, min_periods=7).min()
    nr7 = (rng <= rmin7).astype(float).where(rmin7.notna(), np.nan)
    return nr7.rolling(MDAYS, min_periods=WDAYS).sum()


def f37_rges_170_wr4_indicator(high: pd.Series, low: pd.Series) -> pd.Series:
    """Indicator: today's H-L is the widest in last 4 bars (WR4 expansion / exhaustion proxy)."""
    rng = high - low
    rmax4 = rng.rolling(4, min_periods=4).max()
    return (rng >= rmax4).astype(float).where(rmax4.notna(), np.nan)


def f37_rges_171_wr7_indicator(high: pd.Series, low: pd.Series) -> pd.Series:
    """Indicator: today's H-L is the widest in last 7 bars (WR7 expansion)."""
    rng = high - low
    rmax7 = rng.rolling(7, min_periods=7).max()
    return (rng >= rmax7).astype(float).where(rmax7.notna(), np.nan)


def f37_rges_172_wr7_count_in_21d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of WR7 occurrences in trailing 21d — wide-range cluster intensity."""
    rng = high - low
    rmax7 = rng.rolling(7, min_periods=7).max()
    wr7 = (rng >= rmax7).astype(float).where(rmax7.notna(), np.nan)
    return wr7.rolling(MDAYS, min_periods=WDAYS).sum()


# ============================================================
# Bucket FF — Inside / Outside bars (173-177)
# Inside bar: today's H <= yesterday's H AND today's L >= yesterday's L.
# Outside bar: today's H > yesterday's H AND today's L < yesterday's L.
# ============================================================

def f37_rges_173_inside_bar_indicator(high: pd.Series, low: pd.Series) -> pd.Series:
    """Indicator: today is an inside bar (H<=Hyesterday AND L>=Lyesterday) — compression / consolidation."""
    inside = (high <= high.shift(1)) & (low >= low.shift(1))
    return inside.astype(float).where(high.shift(1).notna() & low.shift(1).notna(), np.nan)


def f37_rges_174_outside_bar_indicator(high: pd.Series, low: pd.Series) -> pd.Series:
    """Indicator: today is an outside bar (H>Hyesterday AND L<Lyesterday) — expansion / engulfing."""
    outside = (high > high.shift(1)) & (low < low.shift(1))
    return outside.astype(float).where(high.shift(1).notna() & low.shift(1).notna(), np.nan)


def f37_rges_175_inside_bar_count_21d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of inside bars in trailing 21d — sustained compression."""
    inside = ((high <= high.shift(1)) & (low >= low.shift(1))).astype(float).where(
        high.shift(1).notna() & low.shift(1).notna(), np.nan
    )
    return inside.rolling(MDAYS, min_periods=WDAYS).sum()


def f37_rges_176_outside_bar_count_21d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of outside bars in trailing 21d — sustained expansion / breakouts."""
    outside = ((high > high.shift(1)) & (low < low.shift(1))).astype(float).where(
        high.shift(1).notna() & low.shift(1).notna(), np.nan
    )
    return outside.rolling(MDAYS, min_periods=WDAYS).sum()


def f37_rges_177_consecutive_inside_bar_streak(high: pd.Series, low: pd.Series) -> pd.Series:
    """Current consecutive inside-bar streak length — compression-streak counter."""
    inside = ((high <= high.shift(1)) & (low >= low.shift(1))).values
    n = len(inside)
    out = np.full(n, np.nan, dtype=float)
    streak = 0
    for i in range(n):
        if i == 0 or np.isnan(high.iloc[i]) or np.isnan(high.shift(1).iloc[i]):
            out[i] = np.nan; streak = 0
        else:
            streak = streak + 1 if inside[i] else 0
            out[i] = float(streak)
    return pd.Series(out, index=high.index)


# ============================================================
# Bucket GG — Donchian width multi-horizon (178-184)
# Donchian width = max(H)_N - min(L)_N. A range-channel concept distinct
# from sum-of-daily-ranges; captures multi-day expansion.
# ============================================================

def _donchian_width(high: pd.Series, low: pd.Series, n: int) -> pd.Series:
    return high.rolling(n, min_periods=max(n // 2, 2)).max() - low.rolling(n, min_periods=max(n // 2, 2)).min()


def f37_rges_178_donchian_width_21d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Donchian width over 21d — monthly high-low channel width."""
    return _donchian_width(high, low, MDAYS)


def f37_rges_179_donchian_width_63d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Donchian width over 63d — quarterly high-low channel width."""
    return _donchian_width(high, low, QDAYS)


def f37_rges_180_donchian_width_252d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Donchian width over 252d — annual high-low channel width."""
    return _donchian_width(high, low, YDAYS)


def f37_rges_181_donchian_width_norm_close_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Donchian width 21d / close — scale-free monthly channel width."""
    return _safe_div(_donchian_width(high, low, MDAYS), close)


def f37_rges_182_donchian_width_norm_close_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Donchian width 252d / close — scale-free annual channel width."""
    return _safe_div(_donchian_width(high, low, YDAYS), close)


def f37_rges_183_donchian_width_ratio_21d_over_252d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Donchian width 21d / Donchian width 252d — short-vs-long channel compression ratio."""
    return _safe_div(_donchian_width(high, low, MDAYS), _donchian_width(high, low, YDAYS))


def f37_rges_184_donchian_width_pct_rank_252d_in_504d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Percentile rank of 252d Donchian width within trailing 504d distribution — annual channel-width regime."""
    dw = _donchian_width(high, low, YDAYS)
    return dw.rolling(DDAYS_2Y, min_periods=YDAYS).rank(pct=True)


# ============================================================
# Bucket HH — Multi-day rolling range vs additive sum (185-188)
# Distinct from "sum of daily log H/L". This is "max H minus min L over k days"
# expressed in log units. The ratio to sum-of-daily-ranges measures trending
# (close to 1 = trending) vs ranging (much less than 1 = oscillating).
# ============================================================

def _log_multiday_range(high: pd.Series, low: pd.Series, n: int) -> pd.Series:
    hi = high.rolling(n, min_periods=max(n // 2, 2)).max()
    lo = low.rolling(n, min_periods=max(n // 2, 2)).min()
    return np.log(_safe_div(hi, lo))


def f37_rges_185_log_multiday_range_5d(high: pd.Series, low: pd.Series) -> pd.Series:
    """log(max H_5d / min L_5d) — weekly multi-day range in log units."""
    return _log_multiday_range(high, low, WDAYS)


def f37_rges_186_log_multiday_range_21d(high: pd.Series, low: pd.Series) -> pd.Series:
    """log(max H_21d / min L_21d) — monthly multi-day range in log units."""
    return _log_multiday_range(high, low, MDAYS)


def f37_rges_187_multiday_range_ratio_5d_over_21d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Weekly multi-day range / monthly multi-day range — short-vs-medium channel ratio."""
    return _safe_div(_log_multiday_range(high, low, WDAYS), _log_multiday_range(high, low, MDAYS))


def f37_rges_188_multiday_vs_sum_efficiency_5d(high: pd.Series, low: pd.Series) -> pd.Series:
    """log(H_5d/L_5d) / sum of log(H_t/L_t) over 5d — efficiency ratio: 1 = perfectly trending in same direction, <1 = oscillating."""
    md = _log_multiday_range(high, low, WDAYS)
    summed = np.log(_safe_div(high, low)).rolling(WDAYS, min_periods=2).sum()
    return _safe_div(md, summed)


# ============================================================
# Bucket II — Hi-Lo midpoint position (189-192)
# (H+L)/2 vs C: positive bias = closing above the midpoint (bullish bar),
# negative = below midpoint (bearish bar).
# ============================================================

def f37_rges_189_close_vs_midpoint_normalized_daily(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """(close - (H+L)/2) / (H-L) daily — normalized signed close-vs-midpoint bias."""
    mid = (high + low) / 2.0
    return _safe_div(close - mid, high - low)


def f37_rges_190_mean_close_vs_midpoint_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Mean (close - midpoint) / range over trailing 21d — short-horizon midpoint-bias regime."""
    mid = (high + low) / 2.0
    bias = _safe_div(close - mid, high - low)
    return bias.rolling(MDAYS, min_periods=WDAYS).mean()


def f37_rges_191_mean_close_vs_midpoint_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Mean (close - midpoint) / range over trailing 252d — annual midpoint-bias regime."""
    mid = (high + low) / 2.0
    bias = _safe_div(close - mid, high - low)
    return bias.rolling(YDAYS, min_periods=QDAYS).mean()


def f37_rges_192_fraction_close_above_midpoint_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Fraction of trailing 252d bars where close > midpoint — sustained bullish-bar bias."""
    mid = (high + low) / 2.0
    above = (close > mid).astype(float).where(mid.notna(), np.nan)
    return above.rolling(YDAYS, min_periods=QDAYS).mean()


# ============================================================
# Bucket JJ — Gap fill rate (193-196)
# A gap up is "filled" if a subsequent low <= prior close on the same day.
# A gap down is "filled" if a subsequent high >= prior close on the same day.
# Same-day fill is the standard intraday definition.
# ============================================================

def _gap_fill_indicators(open_: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series):
    pc = close.shift(1)
    gap_up = (open_ > pc)
    gap_down = (open_ < pc)
    fill_up = gap_up & (low <= pc)
    fill_down = gap_down & (high >= pc)
    return gap_up, gap_down, fill_up, fill_down


def f37_rges_193_gap_fill_indicator_daily(open_: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Indicator: today had a gap (up or down) AND it was filled intraday — daily gap-fill flag."""
    gu, gd, fu, fd = _gap_fill_indicators(open_, high, low, close)
    any_gap = (gu | gd)
    any_fill = (fu | fd)
    return (any_gap & any_fill).astype(float).where(close.shift(1).notna(), np.nan)


def f37_rges_194_gap_fill_rate_21d(open_: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Fraction of gap-days in trailing 21d that were filled intraday — short-horizon gap-fill rate."""
    gu, gd, fu, fd = _gap_fill_indicators(open_, high, low, close)
    any_gap = (gu | gd).astype(float).where(close.shift(1).notna(), np.nan)
    any_fill = (fu | fd).astype(float).where(close.shift(1).notna(), np.nan)
    ng = any_gap.rolling(MDAYS, min_periods=WDAYS).sum()
    nf = any_fill.rolling(MDAYS, min_periods=WDAYS).sum()
    return _safe_div(nf, ng)


def f37_rges_195_gap_fill_rate_252d(open_: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Fraction of gap-days in trailing 252d that were filled intraday — annual gap-fill rate."""
    gu, gd, fu, fd = _gap_fill_indicators(open_, high, low, close)
    any_gap = (gu | gd).astype(float).where(close.shift(1).notna(), np.nan)
    any_fill = (fu | fd).astype(float).where(close.shift(1).notna(), np.nan)
    ng = any_gap.rolling(YDAYS, min_periods=QDAYS).sum()
    nf = any_fill.rolling(YDAYS, min_periods=QDAYS).sum()
    return _safe_div(nf, ng)


def f37_rges_196_gap_fill_asymmetry_up_vs_down_252d(open_: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Up-gap fill rate - down-gap fill rate over 252d — asymmetry in gap-fill probability."""
    gu, gd, fu, fd = _gap_fill_indicators(open_, high, low, close)
    gu_f = gu.astype(float).where(close.shift(1).notna(), np.nan)
    gd_f = gd.astype(float).where(close.shift(1).notna(), np.nan)
    fu_f = fu.astype(float).where(close.shift(1).notna(), np.nan)
    fd_f = fd.astype(float).where(close.shift(1).notna(), np.nan)
    rate_up = _safe_div(fu_f.rolling(YDAYS, min_periods=QDAYS).sum(), gu_f.rolling(YDAYS, min_periods=QDAYS).sum())
    rate_dn = _safe_div(fd_f.rolling(YDAYS, min_periods=QDAYS).sum(), gd_f.rolling(YDAYS, min_periods=QDAYS).sum())
    return rate_up - rate_dn


# ============================================================
# Bucket KK — Open-to-high vs Open-to-low asymmetry (197-200)
# (H - O) vs (O - L): how much room did price stretch up after open vs
# stretch down after open? Captures intraday directional bias.
# ============================================================

def f37_rges_197_mean_oh_over_ol_21d(open_: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Mean (H-O) / (O-L) over trailing 21d — short-horizon intraday up-vs-down stretch bias."""
    return _safe_div(high - open_, open_ - low).rolling(MDAYS, min_periods=WDAYS).mean()


def f37_rges_198_mean_oh_over_ol_252d(open_: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Mean (H-O) / (O-L) over trailing 252d — annual intraday stretch-bias regime."""
    return _safe_div(high - open_, open_ - low).rolling(YDAYS, min_periods=QDAYS).mean()


def f37_rges_199_mean_log_oh_minus_log_ol_252d(open_: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Mean log(H/O) - log(O/L) over 252d — log-space intraday up-vs-down stretch asymmetry."""
    diff = np.log(_safe_div(high, open_)) - np.log(_safe_div(open_, low))
    return diff.rolling(YDAYS, min_periods=QDAYS).mean()


def f37_rges_200_fraction_oh_gt_ol_252d(open_: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Fraction of trailing 252d bars where (H-O) > (O-L) — sustained up-stretch bias."""
    flag = (high - open_ > open_ - low).astype(float).where(high.notna() & low.notna() & open_.notna(), np.nan)
    return flag.rolling(YDAYS, min_periods=QDAYS).mean()


# ============================================================
# Bucket LL — Wilder Directional Movement (201-206)
# +DM_t = max(H_t - H_{t-1}, 0) if (H_t - H_{t-1}) > (L_{t-1} - L_t) else 0
# -DM_t = max(L_{t-1} - L_t, 0) if (L_{t-1} - L_t) > (H_t - H_{t-1}) else 0
# +DI / -DI = 100 * smoothed +DM / -DM divided by smoothed TR.
# DX = 100 * |+DI - -DI| / (+DI + -DI). (ADX = smoothed DX, but here we expose DX.)
# ============================================================

def _wilder_smooth(s: pd.Series, n: int) -> pd.Series:
    """Wilder smoothing = EMA with alpha = 1/n, min_periods = n."""
    return s.ewm(alpha=1.0 / n, adjust=False, min_periods=n).mean()


def _dm_components(high: pd.Series, low: pd.Series):
    up_move = high.diff()
    down_move = -low.diff()
    plus_dm = np.where((up_move > down_move) & (up_move > 0), up_move, 0.0)
    minus_dm = np.where((down_move > up_move) & (down_move > 0), down_move, 0.0)
    return pd.Series(plus_dm, index=high.index), pd.Series(minus_dm, index=high.index)


def f37_rges_201_plus_dm_smoothed_14d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Wilder-smoothed +DM over 14d — upward directional movement strength."""
    pdm, _ = _dm_components(high, low)
    return _wilder_smooth(pdm, 14)


def f37_rges_202_minus_dm_smoothed_14d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Wilder-smoothed -DM over 14d — downward directional movement strength."""
    _, mdm = _dm_components(high, low)
    return _wilder_smooth(mdm, 14)


def f37_rges_203_plus_di_14d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """+DI(14) = 100 * smoothed +DM / smoothed TR — Wilder positive directional indicator."""
    pdm, _ = _dm_components(high, low)
    tr = _true_range(high, low, close)
    return 100.0 * _safe_div(_wilder_smooth(pdm, 14), _wilder_smooth(tr, 14))


def f37_rges_204_minus_di_14d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """-DI(14) = 100 * smoothed -DM / smoothed TR — Wilder negative directional indicator."""
    _, mdm = _dm_components(high, low)
    tr = _true_range(high, low, close)
    return 100.0 * _safe_div(_wilder_smooth(mdm, 14), _wilder_smooth(tr, 14))


def f37_rges_205_di_diff_14d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """+DI(14) - -DI(14) — directional bias; >0 = up bias, <0 = down bias."""
    pdm, mdm = _dm_components(high, low)
    tr = _true_range(high, low, close)
    pdi = 100.0 * _safe_div(_wilder_smooth(pdm, 14), _wilder_smooth(tr, 14))
    mdi = 100.0 * _safe_div(_wilder_smooth(mdm, 14), _wilder_smooth(tr, 14))
    return pdi - mdi


def f37_rges_206_dx_14d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """DX(14) = 100 * |+DI - -DI| / (+DI + -DI) — Wilder directional movement index (pre-ADX smoothing)."""
    pdm, mdm = _dm_components(high, low)
    tr = _true_range(high, low, close)
    pdi = 100.0 * _safe_div(_wilder_smooth(pdm, 14), _wilder_smooth(tr, 14))
    mdi = 100.0 * _safe_div(_wilder_smooth(mdm, 14), _wilder_smooth(tr, 14))
    return 100.0 * _safe_div((pdi - mdi).abs(), pdi + mdi)


# ============================================================
# Bucket MM — Range Hurst / variance ratio (207-210)
# Long memory / mean-reversion diagnostics applied to the range series.
# ============================================================

def _hurst_rs(x: np.ndarray, min_n: int = 10) -> float:
    v = x[~np.isnan(x)]
    n = v.size
    if n < min_n * 2:
        return np.nan
    mean = v.mean()
    devs = np.cumsum(v - mean)
    R = devs.max() - devs.min()
    S = v.std(ddof=1)
    if S == 0 or R == 0:
        return np.nan
    return float(np.log(R / S) / np.log(n))


def f37_rges_207_range_hurst_504d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Hurst exponent (R/S) of log(H/L) over 504d — long memory in range series."""
    log_hl = np.log(_safe_div(high, low))
    return log_hl.rolling(DDAYS_2Y, min_periods=YDAYS).apply(_hurst_rs, raw=True)


def f37_rges_208_range_variance_ratio_2_over_5_252d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Variance ratio var(log(H/L)_{t-2:t}) / var(log(H/L)) at 252d — mean-reversion test on range."""
    log_hl = np.log(_safe_div(high, low))
    def _vr(w):
        v = w[~np.isnan(w)]
        if v.size < 30:
            return np.nan
        # rolling-2 sum / rolling-5 sum variance ratio
        s2 = np.array([v[i] + v[i + 1] for i in range(len(v) - 1)])
        s5 = np.array([v[i:i + 5].sum() for i in range(len(v) - 4)])
        if len(s2) < 5 or len(s5) < 5:
            return np.nan
        v2 = s2.var(ddof=1) / 2.0
        v5 = s5.var(ddof=1) / 5.0
        if v5 == 0:
            return np.nan
        return float(v2 / v5)
    return log_hl.rolling(YDAYS, min_periods=QDAYS).apply(_vr, raw=True)


def f37_rges_209_range_lo_mackinlay_vr_test_252d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Lo-MacKinlay-style VR(5) of log(H/L) at 252d — (1/5) * var(5-sum) / var(1-bar)."""
    log_hl = np.log(_safe_div(high, low))
    def _vr5(w):
        v = w[~np.isnan(w)]
        if v.size < 30:
            return np.nan
        s5 = np.array([v[i:i + 5].sum() for i in range(len(v) - 4)])
        v5 = s5.var(ddof=1) / 5.0
        v1 = v.var(ddof=1)
        if v1 == 0:
            return np.nan
        return float(v5 / v1)
    return log_hl.rolling(YDAYS, min_periods=QDAYS).apply(_vr5, raw=True)


def f37_rges_210_range_hurst_1260d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Hurst exponent (R/S) of log(H/L) over 1260d (5y) — long-horizon range long-memory."""
    log_hl = np.log(_safe_div(high, low))
    return log_hl.rolling(DDAYS_5Y, min_periods=DDAYS_2Y).apply(_hurst_rs, raw=True)


# ============================================================
# Bucket NN — Bipower variation adapted to range (211-214)
# Adapt Barndorff-Nielsen-Shephard BPV to log H/L: sum of |log(H_t/L_t)| *
# |log(H_{t-1}/L_{t-1})|. Jump-robust range estimator.
# ============================================================

def _bipower_range_series(high: pd.Series, low: pd.Series) -> pd.Series:
    a = np.log(_safe_div(high, low)).abs()
    return (np.pi / 2.0) * a * a.shift(1)


def f37_rges_211_bipower_range_21d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Bipower-range estimator (pi/2 * sum |log(H/L)_t| * |log(H/L)_{t-1}|) over 21d — jump-robust monthly range."""
    return _bipower_range_series(high, low).rolling(MDAYS, min_periods=WDAYS).sum()


def f37_rges_212_bipower_range_63d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Bipower-range over 63d — jump-robust quarterly range."""
    return _bipower_range_series(high, low).rolling(QDAYS, min_periods=MDAYS).sum()


def f37_rges_213_bipower_range_252d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Bipower-range over 252d — jump-robust annual range."""
    return _bipower_range_series(high, low).rolling(YDAYS, min_periods=QDAYS).sum()


def f37_rges_214_range_jump_component_252d(high: pd.Series, low: pd.Series) -> pd.Series:
    """sum(log(H/L)^2)_252d - bipower-range_252d (clipped at 0) — direct range-jump component."""
    log_hl = np.log(_safe_div(high, low))
    p_var = (log_hl ** 2).rolling(YDAYS, min_periods=QDAYS).sum()
    bpr = _bipower_range_series(high, low).rolling(YDAYS, min_periods=QDAYS).sum()
    return (p_var - bpr).clip(lower=0.0)


# ============================================================
# Bucket OO — Range distribution moments at multiple horizons (215-218)
# (Family already has range skew/kurt at 63d; here we add 21d, 252d horizons.)
# ============================================================

def f37_rges_215_range_skewness_log_hl_21d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Skewness of log(H/L) distribution over 21d — monthly range-distribution asymmetry."""
    return np.log(_safe_div(high, low)).rolling(MDAYS, min_periods=WDAYS).skew()


def f37_rges_216_range_skewness_log_hl_252d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Skewness of log(H/L) over 252d — annual range-distribution asymmetry."""
    return np.log(_safe_div(high, low)).rolling(YDAYS, min_periods=QDAYS).skew()


def f37_rges_217_range_kurtosis_log_hl_21d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Excess kurtosis of log(H/L) over 21d — monthly range tail-thickness."""
    return np.log(_safe_div(high, low)).rolling(MDAYS, min_periods=WDAYS).kurt()


def f37_rges_218_range_kurtosis_log_hl_252d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Excess kurtosis of log(H/L) over 252d — annual range tail-thickness regime."""
    return np.log(_safe_div(high, low)).rolling(YDAYS, min_periods=QDAYS).kurt()


# ============================================================
# Bucket PP — Range autocorrelation at multiple lags (219-222)
# ============================================================

def _autocorr_lag(s: pd.Series, lag: int, win: int, mp: int) -> pd.Series:
    def _ac(w):
        v = w[~np.isnan(w)]
        if v.size < lag + 5:
            return np.nan
        a = v[:-lag]; b = v[lag:]
        if a.std() == 0 or b.std() == 0:
            return np.nan
        return float(np.corrcoef(a, b)[0, 1])
    return s.rolling(win, min_periods=mp).apply(_ac, raw=True)


def f37_rges_219_range_autocorr_lag5_252d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Autocorrelation of log(H/L) at lag 5 over 252d — weekly-spaced range persistence."""
    log_hl = np.log(_safe_div(high, low))
    return _autocorr_lag(log_hl, 5, YDAYS, QDAYS)


def f37_rges_220_range_autocorr_lag21_504d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Autocorrelation of log(H/L) at lag 21 over 504d — monthly-spaced range persistence."""
    log_hl = np.log(_safe_div(high, low))
    return _autocorr_lag(log_hl, 21, DDAYS_2Y, YDAYS)


def f37_rges_221_range_partial_autocorr_lag1_252d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Partial autocorr of log(H/L) at lag 1 over 252d — correlation after controlling for lag-2."""
    log_hl = np.log(_safe_div(high, low))
    def _pac(w):
        v = w[~np.isnan(w)]
        if v.size < 30:
            return np.nan
        a = v[2:]; b = v[1:-1]; c = v[:-2]
        if c.std() == 0:
            return np.nan
        beta_a = np.cov(a, c, bias=False)[0, 1] / c.var(ddof=1)
        beta_b = np.cov(b, c, bias=False)[0, 1] / c.var(ddof=1)
        ra = a - beta_a * c
        rb = b - beta_b * c
        if ra.std() == 0 or rb.std() == 0:
            return np.nan
        return float(np.corrcoef(ra, rb)[0, 1])
    return log_hl.rolling(YDAYS, min_periods=QDAYS).apply(_pac, raw=True)


def f37_rges_222_ljung_box_log_hl_252d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Ljung-Box Q-statistic up to lag 5 on log(H/L) over 252d — joint autocorrelation test stat."""
    log_hl = np.log(_safe_div(high, low))
    def _lb(w):
        v = w[~np.isnan(w)]
        n = v.size
        if n < 30:
            return np.nan
        v = v - v.mean()
        c0 = (v * v).sum()
        if c0 == 0:
            return np.nan
        q = 0.0
        for k in range(1, 6):
            ck = (v[k:] * v[:-k]).sum() / c0
            q += (ck * ck) / (n - k)
        return float(n * (n + 2) * q)
    return log_hl.rolling(YDAYS, min_periods=QDAYS).apply(_lb, raw=True)


# ============================================================
# Bucket QQ — TR-breakout + persistent expansion/compression composites (223-225)
# ============================================================

def f37_rges_223_tr_breakout_above_21d_high_indicator(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Indicator: today's true range > max TR of prior 21d — TR-breakout flag."""
    tr = _true_range(high, low, close)
    tr_max_prior = tr.shift(1).rolling(MDAYS, min_periods=WDAYS).max()
    return (tr > tr_max_prior).astype(float).where(tr_max_prior.notna(), np.nan)


def f37_rges_224_tr_breakout_count_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of TR-breakouts (TR > prior-21d-max-TR) in trailing 252d — annual breakout intensity."""
    tr = _true_range(high, low, close)
    tr_max_prior = tr.shift(1).rolling(MDAYS, min_periods=WDAYS).max()
    flag = (tr > tr_max_prior).astype(float).where(tr_max_prior.notna(), np.nan)
    return flag.rolling(YDAYS, min_periods=QDAYS).sum()


def f37_rges_225_persistent_expansion_compression_composite(high: pd.Series, low: pd.Series) -> pd.Series:
    """Sign indicator from 3-window agreement: +1 if Parkinson(5d) > Parkinson(21d) > Parkinson(63d) (expansion),
    -1 if Parkinson(5d) < Parkinson(21d) < Parkinson(63d) (compression), 0 otherwise."""
    lhl_sq = (np.log(_safe_div(high, low)) ** 2)
    K = 1.0 / (4.0 * np.log(2.0))   # Parkinson constant — irrelevant for ordering, but keeps semantics clear
    p5 = K * lhl_sq.rolling(WDAYS, min_periods=2).mean()
    p21 = K * lhl_sq.rolling(MDAYS, min_periods=WDAYS).mean()
    p63 = K * lhl_sq.rolling(QDAYS, min_periods=MDAYS).mean()
    expansion = (p5 > p21) & (p21 > p63)
    compression = (p5 < p21) & (p21 < p63)
    out = pd.Series(0.0, index=high.index)
    out = out.where(~expansion, 1.0)
    out = out.where(~compression, -1.0)
    return out.where(p5.notna() & p21.notna() & p63.notna(), np.nan)


# ============================================================
#                         REGISTRY 151-225
# ============================================================



def f37_rges_151_chop_14d_d1(high, low, close):
    return f37_rges_151_chop_14d(high, low, close).diff()


def f37_rges_152_chop_21d_d1(high, low, close):
    return f37_rges_152_chop_21d(high, low, close).diff()


def f37_rges_153_chop_63d_d1(high, low, close):
    return f37_rges_153_chop_63d(high, low, close).diff()


def f37_rges_154_chop_252d_d1(high, low, close):
    return f37_rges_154_chop_252d(high, low, close).diff()


def f37_rges_155_chop_zscore_in_252d_d1(high, low, close):
    return f37_rges_155_chop_zscore_in_252d(high, low, close).diff()


def f37_rges_156_chop_regime_indicator_14d_d1(high, low, close):
    return f37_rges_156_chop_regime_indicator_14d(high, low, close).diff()


def f37_rges_157_vhf_14d_d1(close):
    return f37_rges_157_vhf_14d(close).diff()


def f37_rges_158_vhf_28d_d1(close):
    return f37_rges_158_vhf_28d(close).diff()


def f37_rges_159_vhf_63d_d1(close):
    return f37_rges_159_vhf_63d(close).diff()


def f37_rges_160_vhf_252d_d1(close):
    return f37_rges_160_vhf_252d(close).diff()


def f37_rges_161_vhf_zscore_in_252d_d1(close):
    return f37_rges_161_vhf_zscore_in_252d(close).diff()


def f37_rges_162_mass_index_9d_d1(high, low):
    return f37_rges_162_mass_index_9d(high, low).diff()


def f37_rges_163_mass_index_25d_d1(high, low):
    return f37_rges_163_mass_index_25d(high, low).diff()


def f37_rges_164_mass_index_63d_d1(high, low):
    return f37_rges_164_mass_index_63d(high, low).diff()


def f37_rges_165_mass_index_reversal_bulge_25d_d1(high, low):
    return f37_rges_165_mass_index_reversal_bulge_25d(high, low).diff()


def f37_rges_166_nr4_indicator_d1(high, low):
    return f37_rges_166_nr4_indicator(high, low).diff()


def f37_rges_167_nr7_indicator_d1(high, low):
    return f37_rges_167_nr7_indicator(high, low).diff()


def f37_rges_168_nr4_count_in_21d_d1(high, low):
    return f37_rges_168_nr4_count_in_21d(high, low).diff()


def f37_rges_169_nr7_count_in_21d_d1(high, low):
    return f37_rges_169_nr7_count_in_21d(high, low).diff()


def f37_rges_170_wr4_indicator_d1(high, low):
    return f37_rges_170_wr4_indicator(high, low).diff()


def f37_rges_171_wr7_indicator_d1(high, low):
    return f37_rges_171_wr7_indicator(high, low).diff()


def f37_rges_172_wr7_count_in_21d_d1(high, low):
    return f37_rges_172_wr7_count_in_21d(high, low).diff()


def f37_rges_173_inside_bar_indicator_d1(high, low):
    return f37_rges_173_inside_bar_indicator(high, low).diff()


def f37_rges_174_outside_bar_indicator_d1(high, low):
    return f37_rges_174_outside_bar_indicator(high, low).diff()


def f37_rges_175_inside_bar_count_21d_d1(high, low):
    return f37_rges_175_inside_bar_count_21d(high, low).diff()


def f37_rges_176_outside_bar_count_21d_d1(high, low):
    return f37_rges_176_outside_bar_count_21d(high, low).diff()


def f37_rges_177_consecutive_inside_bar_streak_d1(high, low):
    return f37_rges_177_consecutive_inside_bar_streak(high, low).diff()


def f37_rges_178_donchian_width_21d_d1(high, low):
    return f37_rges_178_donchian_width_21d(high, low).diff()


def f37_rges_179_donchian_width_63d_d1(high, low):
    return f37_rges_179_donchian_width_63d(high, low).diff()


def f37_rges_180_donchian_width_252d_d1(high, low):
    return f37_rges_180_donchian_width_252d(high, low).diff()


def f37_rges_181_donchian_width_norm_close_21d_d1(high, low, close):
    return f37_rges_181_donchian_width_norm_close_21d(high, low, close).diff()


def f37_rges_182_donchian_width_norm_close_252d_d1(high, low, close):
    return f37_rges_182_donchian_width_norm_close_252d(high, low, close).diff()


def f37_rges_183_donchian_width_ratio_21d_over_252d_d1(high, low):
    return f37_rges_183_donchian_width_ratio_21d_over_252d(high, low).diff()


def f37_rges_184_donchian_width_pct_rank_252d_in_504d_d1(high, low):
    return f37_rges_184_donchian_width_pct_rank_252d_in_504d(high, low).diff()


def f37_rges_185_log_multiday_range_5d_d1(high, low):
    return f37_rges_185_log_multiday_range_5d(high, low).diff()


def f37_rges_186_log_multiday_range_21d_d1(high, low):
    return f37_rges_186_log_multiday_range_21d(high, low).diff()


def f37_rges_187_multiday_range_ratio_5d_over_21d_d1(high, low):
    return f37_rges_187_multiday_range_ratio_5d_over_21d(high, low).diff()


def f37_rges_188_multiday_vs_sum_efficiency_5d_d1(high, low):
    return f37_rges_188_multiday_vs_sum_efficiency_5d(high, low).diff()


def f37_rges_189_close_vs_midpoint_normalized_daily_d1(high, low, close):
    return f37_rges_189_close_vs_midpoint_normalized_daily(high, low, close).diff()


def f37_rges_190_mean_close_vs_midpoint_21d_d1(high, low, close):
    return f37_rges_190_mean_close_vs_midpoint_21d(high, low, close).diff()


def f37_rges_191_mean_close_vs_midpoint_252d_d1(high, low, close):
    return f37_rges_191_mean_close_vs_midpoint_252d(high, low, close).diff()


def f37_rges_192_fraction_close_above_midpoint_252d_d1(high, low, close):
    return f37_rges_192_fraction_close_above_midpoint_252d(high, low, close).diff()


def f37_rges_193_gap_fill_indicator_daily_d1(open_, high, low, close):
    return f37_rges_193_gap_fill_indicator_daily(open_, high, low, close).diff()


def f37_rges_194_gap_fill_rate_21d_d1(open_, high, low, close):
    return f37_rges_194_gap_fill_rate_21d(open_, high, low, close).diff()


def f37_rges_195_gap_fill_rate_252d_d1(open_, high, low, close):
    return f37_rges_195_gap_fill_rate_252d(open_, high, low, close).diff()


def f37_rges_196_gap_fill_asymmetry_up_vs_down_252d_d1(open_, high, low, close):
    return f37_rges_196_gap_fill_asymmetry_up_vs_down_252d(open_, high, low, close).diff()


def f37_rges_197_mean_oh_over_ol_21d_d1(open_, high, low):
    return f37_rges_197_mean_oh_over_ol_21d(open_, high, low).diff()


def f37_rges_198_mean_oh_over_ol_252d_d1(open_, high, low):
    return f37_rges_198_mean_oh_over_ol_252d(open_, high, low).diff()


def f37_rges_199_mean_log_oh_minus_log_ol_252d_d1(open_, high, low):
    return f37_rges_199_mean_log_oh_minus_log_ol_252d(open_, high, low).diff()


def f37_rges_200_fraction_oh_gt_ol_252d_d1(open_, high, low):
    return f37_rges_200_fraction_oh_gt_ol_252d(open_, high, low).diff()


def f37_rges_201_plus_dm_smoothed_14d_d1(high, low):
    return f37_rges_201_plus_dm_smoothed_14d(high, low).diff()


def f37_rges_202_minus_dm_smoothed_14d_d1(high, low):
    return f37_rges_202_minus_dm_smoothed_14d(high, low).diff()


def f37_rges_203_plus_di_14d_d1(high, low, close):
    return f37_rges_203_plus_di_14d(high, low, close).diff()


def f37_rges_204_minus_di_14d_d1(high, low, close):
    return f37_rges_204_minus_di_14d(high, low, close).diff()


def f37_rges_205_di_diff_14d_d1(high, low, close):
    return f37_rges_205_di_diff_14d(high, low, close).diff()


def f37_rges_206_dx_14d_d1(high, low, close):
    return f37_rges_206_dx_14d(high, low, close).diff()


def f37_rges_207_range_hurst_504d_d1(high, low):
    return f37_rges_207_range_hurst_504d(high, low).diff()


def f37_rges_208_range_variance_ratio_2_over_5_252d_d1(high, low):
    return f37_rges_208_range_variance_ratio_2_over_5_252d(high, low).diff()


def f37_rges_209_range_lo_mackinlay_vr_test_252d_d1(high, low):
    return f37_rges_209_range_lo_mackinlay_vr_test_252d(high, low).diff()


def f37_rges_210_range_hurst_1260d_d1(high, low):
    return f37_rges_210_range_hurst_1260d(high, low).diff()


def f37_rges_211_bipower_range_21d_d1(high, low):
    return f37_rges_211_bipower_range_21d(high, low).diff()


def f37_rges_212_bipower_range_63d_d1(high, low):
    return f37_rges_212_bipower_range_63d(high, low).diff()


def f37_rges_213_bipower_range_252d_d1(high, low):
    return f37_rges_213_bipower_range_252d(high, low).diff()


def f37_rges_214_range_jump_component_252d_d1(high, low):
    return f37_rges_214_range_jump_component_252d(high, low).diff()


def f37_rges_215_range_skewness_log_hl_21d_d1(high, low):
    return f37_rges_215_range_skewness_log_hl_21d(high, low).diff()


def f37_rges_216_range_skewness_log_hl_252d_d1(high, low):
    return f37_rges_216_range_skewness_log_hl_252d(high, low).diff()


def f37_rges_217_range_kurtosis_log_hl_21d_d1(high, low):
    return f37_rges_217_range_kurtosis_log_hl_21d(high, low).diff()


def f37_rges_218_range_kurtosis_log_hl_252d_d1(high, low):
    return f37_rges_218_range_kurtosis_log_hl_252d(high, low).diff()


def f37_rges_219_range_autocorr_lag5_252d_d1(high, low):
    return f37_rges_219_range_autocorr_lag5_252d(high, low).diff()


def f37_rges_220_range_autocorr_lag21_504d_d1(high, low):
    return f37_rges_220_range_autocorr_lag21_504d(high, low).diff()


def f37_rges_221_range_partial_autocorr_lag1_252d_d1(high, low):
    return f37_rges_221_range_partial_autocorr_lag1_252d(high, low).diff()


def f37_rges_222_ljung_box_log_hl_252d_d1(high, low):
    return f37_rges_222_ljung_box_log_hl_252d(high, low).diff()


def f37_rges_223_tr_breakout_above_21d_high_indicator_d1(high, low, close):
    return f37_rges_223_tr_breakout_above_21d_high_indicator(high, low, close).diff()


def f37_rges_224_tr_breakout_count_252d_d1(high, low, close):
    return f37_rges_224_tr_breakout_count_252d(high, low, close).diff()


def f37_rges_225_persistent_expansion_compression_composite_d1(high, low):
    return f37_rges_225_persistent_expansion_compression_composite(high, low).diff()


RANGE_ESTIMATORS_FAMILY_D1_REGISTRY_151_225 = {
    "f37_rges_151_chop_14d_d1": {"inputs": ["high", "low", "close"], "func": f37_rges_151_chop_14d_d1},
    "f37_rges_152_chop_21d_d1": {"inputs": ["high", "low", "close"], "func": f37_rges_152_chop_21d_d1},
    "f37_rges_153_chop_63d_d1": {"inputs": ["high", "low", "close"], "func": f37_rges_153_chop_63d_d1},
    "f37_rges_154_chop_252d_d1": {"inputs": ["high", "low", "close"], "func": f37_rges_154_chop_252d_d1},
    "f37_rges_155_chop_zscore_in_252d_d1": {"inputs": ["high", "low", "close"], "func": f37_rges_155_chop_zscore_in_252d_d1},
    "f37_rges_156_chop_regime_indicator_14d_d1": {"inputs": ["high", "low", "close"], "func": f37_rges_156_chop_regime_indicator_14d_d1},
    "f37_rges_157_vhf_14d_d1": {"inputs": ["close"], "func": f37_rges_157_vhf_14d_d1},
    "f37_rges_158_vhf_28d_d1": {"inputs": ["close"], "func": f37_rges_158_vhf_28d_d1},
    "f37_rges_159_vhf_63d_d1": {"inputs": ["close"], "func": f37_rges_159_vhf_63d_d1},
    "f37_rges_160_vhf_252d_d1": {"inputs": ["close"], "func": f37_rges_160_vhf_252d_d1},
    "f37_rges_161_vhf_zscore_in_252d_d1": {"inputs": ["close"], "func": f37_rges_161_vhf_zscore_in_252d_d1},
    "f37_rges_162_mass_index_9d_d1": {"inputs": ["high", "low"], "func": f37_rges_162_mass_index_9d_d1},
    "f37_rges_163_mass_index_25d_d1": {"inputs": ["high", "low"], "func": f37_rges_163_mass_index_25d_d1},
    "f37_rges_164_mass_index_63d_d1": {"inputs": ["high", "low"], "func": f37_rges_164_mass_index_63d_d1},
    "f37_rges_165_mass_index_reversal_bulge_25d_d1": {"inputs": ["high", "low"], "func": f37_rges_165_mass_index_reversal_bulge_25d_d1},
    "f37_rges_166_nr4_indicator_d1": {"inputs": ["high", "low"], "func": f37_rges_166_nr4_indicator_d1},
    "f37_rges_167_nr7_indicator_d1": {"inputs": ["high", "low"], "func": f37_rges_167_nr7_indicator_d1},
    "f37_rges_168_nr4_count_in_21d_d1": {"inputs": ["high", "low"], "func": f37_rges_168_nr4_count_in_21d_d1},
    "f37_rges_169_nr7_count_in_21d_d1": {"inputs": ["high", "low"], "func": f37_rges_169_nr7_count_in_21d_d1},
    "f37_rges_170_wr4_indicator_d1": {"inputs": ["high", "low"], "func": f37_rges_170_wr4_indicator_d1},
    "f37_rges_171_wr7_indicator_d1": {"inputs": ["high", "low"], "func": f37_rges_171_wr7_indicator_d1},
    "f37_rges_172_wr7_count_in_21d_d1": {"inputs": ["high", "low"], "func": f37_rges_172_wr7_count_in_21d_d1},
    "f37_rges_173_inside_bar_indicator_d1": {"inputs": ["high", "low"], "func": f37_rges_173_inside_bar_indicator_d1},
    "f37_rges_174_outside_bar_indicator_d1": {"inputs": ["high", "low"], "func": f37_rges_174_outside_bar_indicator_d1},
    "f37_rges_175_inside_bar_count_21d_d1": {"inputs": ["high", "low"], "func": f37_rges_175_inside_bar_count_21d_d1},
    "f37_rges_176_outside_bar_count_21d_d1": {"inputs": ["high", "low"], "func": f37_rges_176_outside_bar_count_21d_d1},
    "f37_rges_177_consecutive_inside_bar_streak_d1": {"inputs": ["high", "low"], "func": f37_rges_177_consecutive_inside_bar_streak_d1},
    "f37_rges_178_donchian_width_21d_d1": {"inputs": ["high", "low"], "func": f37_rges_178_donchian_width_21d_d1},
    "f37_rges_179_donchian_width_63d_d1": {"inputs": ["high", "low"], "func": f37_rges_179_donchian_width_63d_d1},
    "f37_rges_180_donchian_width_252d_d1": {"inputs": ["high", "low"], "func": f37_rges_180_donchian_width_252d_d1},
    "f37_rges_181_donchian_width_norm_close_21d_d1": {"inputs": ["high", "low", "close"], "func": f37_rges_181_donchian_width_norm_close_21d_d1},
    "f37_rges_182_donchian_width_norm_close_252d_d1": {"inputs": ["high", "low", "close"], "func": f37_rges_182_donchian_width_norm_close_252d_d1},
    "f37_rges_183_donchian_width_ratio_21d_over_252d_d1": {"inputs": ["high", "low"], "func": f37_rges_183_donchian_width_ratio_21d_over_252d_d1},
    "f37_rges_184_donchian_width_pct_rank_252d_in_504d_d1": {"inputs": ["high", "low"], "func": f37_rges_184_donchian_width_pct_rank_252d_in_504d_d1},
    "f37_rges_185_log_multiday_range_5d_d1": {"inputs": ["high", "low"], "func": f37_rges_185_log_multiday_range_5d_d1},
    "f37_rges_186_log_multiday_range_21d_d1": {"inputs": ["high", "low"], "func": f37_rges_186_log_multiday_range_21d_d1},
    "f37_rges_187_multiday_range_ratio_5d_over_21d_d1": {"inputs": ["high", "low"], "func": f37_rges_187_multiday_range_ratio_5d_over_21d_d1},
    "f37_rges_188_multiday_vs_sum_efficiency_5d_d1": {"inputs": ["high", "low"], "func": f37_rges_188_multiday_vs_sum_efficiency_5d_d1},
    "f37_rges_189_close_vs_midpoint_normalized_daily_d1": {"inputs": ["high", "low", "close"], "func": f37_rges_189_close_vs_midpoint_normalized_daily_d1},
    "f37_rges_190_mean_close_vs_midpoint_21d_d1": {"inputs": ["high", "low", "close"], "func": f37_rges_190_mean_close_vs_midpoint_21d_d1},
    "f37_rges_191_mean_close_vs_midpoint_252d_d1": {"inputs": ["high", "low", "close"], "func": f37_rges_191_mean_close_vs_midpoint_252d_d1},
    "f37_rges_192_fraction_close_above_midpoint_252d_d1": {"inputs": ["high", "low", "close"], "func": f37_rges_192_fraction_close_above_midpoint_252d_d1},
    "f37_rges_193_gap_fill_indicator_daily_d1": {"inputs": ["open", "high", "low", "close"], "func": f37_rges_193_gap_fill_indicator_daily_d1},
    "f37_rges_194_gap_fill_rate_21d_d1": {"inputs": ["open", "high", "low", "close"], "func": f37_rges_194_gap_fill_rate_21d_d1},
    "f37_rges_195_gap_fill_rate_252d_d1": {"inputs": ["open", "high", "low", "close"], "func": f37_rges_195_gap_fill_rate_252d_d1},
    "f37_rges_196_gap_fill_asymmetry_up_vs_down_252d_d1": {"inputs": ["open", "high", "low", "close"], "func": f37_rges_196_gap_fill_asymmetry_up_vs_down_252d_d1},
    "f37_rges_197_mean_oh_over_ol_21d_d1": {"inputs": ["open", "high", "low"], "func": f37_rges_197_mean_oh_over_ol_21d_d1},
    "f37_rges_198_mean_oh_over_ol_252d_d1": {"inputs": ["open", "high", "low"], "func": f37_rges_198_mean_oh_over_ol_252d_d1},
    "f37_rges_199_mean_log_oh_minus_log_ol_252d_d1": {"inputs": ["open", "high", "low"], "func": f37_rges_199_mean_log_oh_minus_log_ol_252d_d1},
    "f37_rges_200_fraction_oh_gt_ol_252d_d1": {"inputs": ["open", "high", "low"], "func": f37_rges_200_fraction_oh_gt_ol_252d_d1},
    "f37_rges_201_plus_dm_smoothed_14d_d1": {"inputs": ["high", "low"], "func": f37_rges_201_plus_dm_smoothed_14d_d1},
    "f37_rges_202_minus_dm_smoothed_14d_d1": {"inputs": ["high", "low"], "func": f37_rges_202_minus_dm_smoothed_14d_d1},
    "f37_rges_203_plus_di_14d_d1": {"inputs": ["high", "low", "close"], "func": f37_rges_203_plus_di_14d_d1},
    "f37_rges_204_minus_di_14d_d1": {"inputs": ["high", "low", "close"], "func": f37_rges_204_minus_di_14d_d1},
    "f37_rges_205_di_diff_14d_d1": {"inputs": ["high", "low", "close"], "func": f37_rges_205_di_diff_14d_d1},
    "f37_rges_206_dx_14d_d1": {"inputs": ["high", "low", "close"], "func": f37_rges_206_dx_14d_d1},
    "f37_rges_207_range_hurst_504d_d1": {"inputs": ["high", "low"], "func": f37_rges_207_range_hurst_504d_d1},
    "f37_rges_208_range_variance_ratio_2_over_5_252d_d1": {"inputs": ["high", "low"], "func": f37_rges_208_range_variance_ratio_2_over_5_252d_d1},
    "f37_rges_209_range_lo_mackinlay_vr_test_252d_d1": {"inputs": ["high", "low"], "func": f37_rges_209_range_lo_mackinlay_vr_test_252d_d1},
    "f37_rges_210_range_hurst_1260d_d1": {"inputs": ["high", "low"], "func": f37_rges_210_range_hurst_1260d_d1},
    "f37_rges_211_bipower_range_21d_d1": {"inputs": ["high", "low"], "func": f37_rges_211_bipower_range_21d_d1},
    "f37_rges_212_bipower_range_63d_d1": {"inputs": ["high", "low"], "func": f37_rges_212_bipower_range_63d_d1},
    "f37_rges_213_bipower_range_252d_d1": {"inputs": ["high", "low"], "func": f37_rges_213_bipower_range_252d_d1},
    "f37_rges_214_range_jump_component_252d_d1": {"inputs": ["high", "low"], "func": f37_rges_214_range_jump_component_252d_d1},
    "f37_rges_215_range_skewness_log_hl_21d_d1": {"inputs": ["high", "low"], "func": f37_rges_215_range_skewness_log_hl_21d_d1},
    "f37_rges_216_range_skewness_log_hl_252d_d1": {"inputs": ["high", "low"], "func": f37_rges_216_range_skewness_log_hl_252d_d1},
    "f37_rges_217_range_kurtosis_log_hl_21d_d1": {"inputs": ["high", "low"], "func": f37_rges_217_range_kurtosis_log_hl_21d_d1},
    "f37_rges_218_range_kurtosis_log_hl_252d_d1": {"inputs": ["high", "low"], "func": f37_rges_218_range_kurtosis_log_hl_252d_d1},
    "f37_rges_219_range_autocorr_lag5_252d_d1": {"inputs": ["high", "low"], "func": f37_rges_219_range_autocorr_lag5_252d_d1},
    "f37_rges_220_range_autocorr_lag21_504d_d1": {"inputs": ["high", "low"], "func": f37_rges_220_range_autocorr_lag21_504d_d1},
    "f37_rges_221_range_partial_autocorr_lag1_252d_d1": {"inputs": ["high", "low"], "func": f37_rges_221_range_partial_autocorr_lag1_252d_d1},
    "f37_rges_222_ljung_box_log_hl_252d_d1": {"inputs": ["high", "low"], "func": f37_rges_222_ljung_box_log_hl_252d_d1},
    "f37_rges_223_tr_breakout_above_21d_high_indicator_d1": {"inputs": ["high", "low", "close"], "func": f37_rges_223_tr_breakout_above_21d_high_indicator_d1},
    "f37_rges_224_tr_breakout_count_252d_d1": {"inputs": ["high", "low", "close"], "func": f37_rges_224_tr_breakout_count_252d_d1},
    "f37_rges_225_persistent_expansion_compression_composite_d1": {"inputs": ["high", "low"], "func": f37_rges_225_persistent_expansion_compression_composite_d1},
}
