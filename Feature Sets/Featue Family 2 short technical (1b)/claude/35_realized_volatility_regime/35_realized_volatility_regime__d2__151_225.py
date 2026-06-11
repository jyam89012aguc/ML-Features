"""realized_volatility_regime d2 features 151-225 — Pipeline 1b-technical.

Gap-filling extension to family 35. 75 distinct hypotheses NOT covered by
__base__001_075.py or __base__076_150.py. Sources for the canonical
estimators added here:

  - Bipower variation (BPV): Barndorff-Nielsen & Shephard 2004
  - MedRV / MinRV: Andersen, Dobrev, Schaumburg 2012 (nearest-neighbor truncation)
  - Truncated RV (TRV) and jump component (RV - BPV): Andersen-Bollerslev-Diebold 2007
  - HAR-RV / HAR-RV-J: Corsi 2009; Andersen-Bollerslev-Diebold 2007
  - Realized quarticity (RQ): Barndorff-Nielsen & Shephard 2002; HAR-Q models
  - EWMA / RiskMetrics: J.P. Morgan RiskMetrics 1996 (lambda=0.94)
  - Long-memory vol: Andersen-Bollerslev-Diebold-Labys 2001

Buckets in this file:
  AA Bipower variation (151-157)
  BB MedRV / MinRV jump-robust (158-163)
  CC Truncated RV (164-167)
  DD Jump component RV-BPV (168-173)
  EE Continuous variation share (174-177)
  FF HAR-RV daily/weekly/monthly components (178-184)
  GG Realized quarticity (185-188)
  HH EWMA / RiskMetrics (189-194)
  II Long-memory vol (195-198)
  JJ Vol regime duration (199-202)
  KK True vol-of-vol on RV series (203-206)
  LL Vol crash / sudden drop indicators (207-210)
  MM Spectral / cycle (211-214)
  NN MIDAS-style weighted RV (215-218)
  OO RV autocorrelation multi-lag (219-222)
  PP HAR-RV-J & regime composites (223-225)

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


def _log_returns(close: pd.Series) -> pd.Series:
    return _safe_log(close).diff()


# Bipower-variation scaling constant: mu_1 = E[|Z|] for Z ~ N(0,1) = sqrt(2/pi)
MU1 = np.sqrt(2.0 / np.pi)
MU1_SQ_INV = 1.0 / (MU1 * MU1)   # = pi/2


def _bpv_series(r: pd.Series) -> pd.Series:
    """Per-bar BPV contribution: (pi/2) * |r_t| * |r_{t-1}|. Sum-aggregate to get window BPV."""
    return (np.pi / 2.0) * r.abs() * r.shift(1).abs()


# ============================================================
# Bucket AA — Bipower Variation (jump-robust integrated variance) (151-157)
# Barndorff-Nielsen & Shephard 2004: BPV is consistent for the continuous
# component of QV even when jumps are present.
# ============================================================

def f35_rvre_151_bpv_21d(close: pd.Series) -> pd.Series:
    """Bipower variation (pi/2 * sum |r_t||r_{t-1}|) over trailing 21d — jump-robust monthly variance."""
    r = _log_returns(close)
    return _bpv_series(r).rolling(MDAYS, min_periods=WDAYS).sum()


def f35_rvre_152_bpv_63d(close: pd.Series) -> pd.Series:
    """Bipower variation over trailing 63d — jump-robust quarterly variance."""
    r = _log_returns(close)
    return _bpv_series(r).rolling(QDAYS, min_periods=MDAYS).sum()


def f35_rvre_153_bpv_252d(close: pd.Series) -> pd.Series:
    """Bipower variation over trailing 252d — jump-robust annual variance."""
    r = _log_returns(close)
    return _bpv_series(r).rolling(YDAYS, min_periods=QDAYS).sum()


def f35_rvre_154_log_bpv_252d(close: pd.Series) -> pd.Series:
    """log(BPV + eps) at 252d — heavy-tail-friendly scale, distinct hypothesis."""
    r = _log_returns(close)
    b = _bpv_series(r).rolling(YDAYS, min_periods=QDAYS).sum()
    return np.log(b + 1e-12).where(b > 0, np.nan)


def f35_rvre_155_bpv_sigma_annualized_21d(close: pd.Series) -> pd.Series:
    """sqrt(BPV/N)*sqrt(252) annualized at 21d — jump-robust annualized vol estimate."""
    r = _log_returns(close)
    b = _bpv_series(r).rolling(MDAYS, min_periods=WDAYS).sum()
    return np.sqrt(b / float(MDAYS)) * np.sqrt(252.0)


def f35_rvre_156_bpv_sigma_annualized_252d(close: pd.Series) -> pd.Series:
    """sqrt(BPV/N)*sqrt(252) annualized at 252d — jump-robust annualized vol."""
    r = _log_returns(close)
    b = _bpv_series(r).rolling(YDAYS, min_periods=QDAYS).sum()
    return np.sqrt(b / float(YDAYS)) * np.sqrt(252.0)


def f35_rvre_157_bpv_5d(close: pd.Series) -> pd.Series:
    """Bipower variation over trailing 5d — jump-robust weekly variance."""
    r = _log_returns(close)
    return _bpv_series(r).rolling(WDAYS, min_periods=2).sum()


# ============================================================
# Bucket BB — MedRV / MinRV (nearest-neighbor truncation) (158-163)
# Andersen, Dobrev, Schaumburg 2012. Robust to jumps AND to zero-returns.
# MedRV: scaled sum of median(|r_{t-1}|, |r_t|, |r_{t+1}|)^2.
# MinRV: scaled sum of min(|r_{t-1}|, |r_t|)^2.
# We use right-aligned (causal) median-of-3 with window [t-2, t-1, t] to
# preserve PIT discipline (no peeking forward).
# ============================================================

# Scaling constants from ADS2012:
# MinRV scale: pi / (pi - 2)  ≈ 2.75
# MedRV scale: pi / (6 - 4*sqrt(3) + pi)  ≈ 2.96
MINRV_SCALE = np.pi / (np.pi - 2.0)
MEDRV_SCALE = np.pi / (6.0 - 4.0 * np.sqrt(3.0) + np.pi)


def _minrv_series(r: pd.Series) -> pd.Series:
    """Per-bar contribution: MINRV_SCALE * (N/(N-1)) * min(|r_t|, |r_{t-1}|)^2. We absorb the N/(N-1) into the rolling-sum aggregator."""
    a = r.abs()
    return MINRV_SCALE * np.minimum(a, a.shift(1)) ** 2


def _medrv_series(r: pd.Series) -> pd.Series:
    """Per-bar contribution: MEDRV_SCALE * (N/(N-2)) * median(|r_{t-2}|, |r_{t-1}|, |r_t|)^2. (causal 3-point median to preserve PIT)."""
    a = r.abs()
    triple = pd.concat([a.shift(2).rename("m2"), a.shift(1).rename("m1"), a.rename("m0")], axis=1)
    med = triple.median(axis=1)
    return MEDRV_SCALE * med ** 2


def f35_rvre_158_medrv_21d(close: pd.Series) -> pd.Series:
    """MedRV (median-of-3 nearest-neighbor truncation, ADS2012) over 21d — jump-robust monthly."""
    r = _log_returns(close)
    return _medrv_series(r).rolling(MDAYS, min_periods=WDAYS).sum()


def f35_rvre_159_medrv_63d(close: pd.Series) -> pd.Series:
    """MedRV over 63d — jump-robust quarterly."""
    r = _log_returns(close)
    return _medrv_series(r).rolling(QDAYS, min_periods=MDAYS).sum()


def f35_rvre_160_medrv_252d(close: pd.Series) -> pd.Series:
    """MedRV over 252d — jump-robust annual."""
    r = _log_returns(close)
    return _medrv_series(r).rolling(YDAYS, min_periods=QDAYS).sum()


def f35_rvre_161_minrv_21d(close: pd.Series) -> pd.Series:
    """MinRV (min-of-2 nearest-neighbor truncation, ADS2012) over 21d — jump-robust monthly."""
    r = _log_returns(close)
    return _minrv_series(r).rolling(MDAYS, min_periods=WDAYS).sum()


def f35_rvre_162_minrv_63d(close: pd.Series) -> pd.Series:
    """MinRV over 63d — jump-robust quarterly."""
    r = _log_returns(close)
    return _minrv_series(r).rolling(QDAYS, min_periods=MDAYS).sum()


def f35_rvre_163_minrv_252d(close: pd.Series) -> pd.Series:
    """MinRV over 252d — jump-robust annual."""
    r = _log_returns(close)
    return _minrv_series(r).rolling(YDAYS, min_periods=QDAYS).sum()


# ============================================================
# Bucket CC — Truncated RV (164-167)
# TRV: sum r_t^2 * 1{|r_t| <= threshold}. Threshold here is k * trailing-21d
# realized std, with k=3 — a standard choice in the jump-diffusion literature.
# ============================================================

def _trv_series(r: pd.Series, k: float, vol_lookback: int) -> pd.Series:
    sigma = r.rolling(vol_lookback, min_periods=max(vol_lookback // 3, 2)).std()
    thr = k * sigma.shift(1)   # use lagged sigma so threshold is PIT-clean
    keep = r.abs() <= thr
    return (r ** 2).where(keep, 0.0)


def f35_rvre_164_trv_21d_k3(close: pd.Series) -> pd.Series:
    """Truncated RV (threshold = 3 * lagged 21d std) over 21d — jumps removed via threshold filter."""
    r = _log_returns(close)
    return _trv_series(r, 3.0, MDAYS).rolling(MDAYS, min_periods=WDAYS).sum()


def f35_rvre_165_trv_63d_k3(close: pd.Series) -> pd.Series:
    """Truncated RV (threshold = 3 * lagged 21d std) over 63d."""
    r = _log_returns(close)
    return _trv_series(r, 3.0, MDAYS).rolling(QDAYS, min_periods=MDAYS).sum()


def f35_rvre_166_trv_252d_k3(close: pd.Series) -> pd.Series:
    """Truncated RV over 252d — annual jump-removed variance."""
    r = _log_returns(close)
    return _trv_series(r, 3.0, MDAYS).rolling(YDAYS, min_periods=QDAYS).sum()


def f35_rvre_167_truncation_rate_252d(close: pd.Series) -> pd.Series:
    """Fraction of returns in trailing 252d that exceed the 3*lagged-21d-sigma jump threshold — direct jump-intensity measure."""
    r = _log_returns(close)
    sigma = r.rolling(MDAYS, min_periods=WDAYS).std()
    thr = 3.0 * sigma.shift(1)
    flag = (r.abs() > thr).astype(float).where(thr.notna(), np.nan)
    return flag.rolling(YDAYS, min_periods=QDAYS).mean()


# ============================================================
# Bucket DD — Jump component (RV - BPV) (168-173)
# Andersen-Bollerslev-Diebold 2007: significant jump variation = max(0, RV - BPV).
# ============================================================

def _rv_window_sum_sq(r: pd.Series, n: int, mp: int) -> pd.Series:
    return (r ** 2).rolling(n, min_periods=mp).sum()


def f35_rvre_168_jump_var_21d(close: pd.Series) -> pd.Series:
    """max(0, RV - BPV) at 21d — direct jump-variance proxy, monthly."""
    r = _log_returns(close)
    rv = _rv_window_sum_sq(r, MDAYS, WDAYS)
    bpv = _bpv_series(r).rolling(MDAYS, min_periods=WDAYS).sum()
    return (rv - bpv).clip(lower=0.0)


def f35_rvre_169_jump_var_252d(close: pd.Series) -> pd.Series:
    """max(0, RV - BPV) at 252d — annual jump variation."""
    r = _log_returns(close)
    rv = _rv_window_sum_sq(r, YDAYS, QDAYS)
    bpv = _bpv_series(r).rolling(YDAYS, min_periods=QDAYS).sum()
    return (rv - bpv).clip(lower=0.0)


def f35_rvre_170_log_jump_var_252d(close: pd.Series) -> pd.Series:
    """log(jump_var + eps) at 252d — scale-compressed jump variance."""
    r = _log_returns(close)
    rv = _rv_window_sum_sq(r, YDAYS, QDAYS)
    bpv = _bpv_series(r).rolling(YDAYS, min_periods=QDAYS).sum()
    jv = (rv - bpv).clip(lower=0.0)
    return np.log(jv + 1e-12).where(jv > 0, np.nan)


def f35_rvre_171_significant_jump_indicator_21d(close: pd.Series) -> pd.Series:
    """Indicator that (RV-BPV)/RV at 21d exceeds 5% — significant-jump-day-cluster flag (Jiang-Oomen proxy)."""
    r = _log_returns(close)
    rv = _rv_window_sum_sq(r, MDAYS, WDAYS)
    bpv = _bpv_series(r).rolling(MDAYS, min_periods=WDAYS).sum()
    share = _safe_div((rv - bpv).clip(lower=0.0), rv)
    return (share > 0.05).astype(float).where(share.notna(), np.nan)


def f35_rvre_172_count_jump_days_in_21d(close: pd.Series) -> pd.Series:
    """Count of bars in trailing 21d where |r_t| > 3*lagged-21d-sigma — jump-day count, short."""
    r = _log_returns(close)
    sigma = r.rolling(MDAYS, min_periods=WDAYS).std()
    thr = 3.0 * sigma.shift(1)
    flag = (r.abs() > thr).astype(float).where(thr.notna(), np.nan)
    return flag.rolling(MDAYS, min_periods=WDAYS).sum()


def f35_rvre_173_count_jump_days_in_252d(close: pd.Series) -> pd.Series:
    """Count of bars in trailing 252d where |r_t| > 3*lagged-21d-sigma — jump-day count, annual."""
    r = _log_returns(close)
    sigma = r.rolling(MDAYS, min_periods=WDAYS).std()
    thr = 3.0 * sigma.shift(1)
    flag = (r.abs() > thr).astype(float).where(thr.notna(), np.nan)
    return flag.rolling(YDAYS, min_periods=QDAYS).sum()


# ============================================================
# Bucket EE — Continuous variation share (174-177)
# BPV / RV: share of total variance attributable to the continuous (no-jump) component.
# ============================================================

def f35_rvre_174_continuous_var_share_21d(close: pd.Series) -> pd.Series:
    """BPV / RV at 21d — share of monthly variance attributable to continuous part."""
    r = _log_returns(close)
    rv = _rv_window_sum_sq(r, MDAYS, WDAYS)
    bpv = _bpv_series(r).rolling(MDAYS, min_periods=WDAYS).sum()
    return _safe_div(bpv, rv)


def f35_rvre_175_continuous_var_share_252d(close: pd.Series) -> pd.Series:
    """BPV / RV at 252d — annual continuous-variation share."""
    r = _log_returns(close)
    rv = _rv_window_sum_sq(r, YDAYS, QDAYS)
    bpv = _bpv_series(r).rolling(YDAYS, min_periods=QDAYS).sum()
    return _safe_div(bpv, rv)


def f35_rvre_176_jump_share_21d(close: pd.Series) -> pd.Series:
    """1 - BPV/RV at 21d (clipped at 0) — share of monthly variance attributable to jumps."""
    r = _log_returns(close)
    rv = _rv_window_sum_sq(r, MDAYS, WDAYS)
    bpv = _bpv_series(r).rolling(MDAYS, min_periods=WDAYS).sum()
    return (1.0 - _safe_div(bpv, rv)).clip(lower=0.0)


def f35_rvre_177_jump_share_252d(close: pd.Series) -> pd.Series:
    """1 - BPV/RV at 252d (clipped at 0) — annual jump share."""
    r = _log_returns(close)
    rv = _rv_window_sum_sq(r, YDAYS, QDAYS)
    bpv = _bpv_series(r).rolling(YDAYS, min_periods=QDAYS).sum()
    return (1.0 - _safe_div(bpv, rv)).clip(lower=0.0)


# ============================================================
# Bucket FF — HAR-RV daily/weekly/monthly components (178-184)
# Corsi 2009 HAR model: RV_t+h = b0 + b_d * RV_d + b_w * RV_w + b_m * RV_m.
# We expose each component (each is the *mean daily* RV at the indicated horizon).
# ============================================================

def f35_rvre_178_har_rv_daily_component(close: pd.Series) -> pd.Series:
    """Today's squared log return — daily HAR-RV component (RV_d, single-day variance)."""
    r = _log_returns(close)
    return r ** 2


def f35_rvre_179_har_rv_weekly_component(close: pd.Series) -> pd.Series:
    """Mean daily RV over trailing 5d — weekly HAR-RV component (RV_w)."""
    r = _log_returns(close)
    return (r ** 2).rolling(WDAYS, min_periods=2).mean()


def f35_rvre_180_har_rv_monthly_component(close: pd.Series) -> pd.Series:
    """Mean daily RV over trailing 22d — monthly HAR-RV component (RV_m, Corsi standard)."""
    r = _log_returns(close)
    return (r ** 2).rolling(22, min_periods=WDAYS).mean()


def f35_rvre_181_har_weekly_minus_daily(close: pd.Series) -> pd.Series:
    """RV_w - RV_d — short-term reversion direction; positive = today below weekly avg."""
    r = _log_returns(close)
    rvd = r ** 2
    rvw = rvd.rolling(WDAYS, min_periods=2).mean()
    return rvw - rvd


def f35_rvre_182_har_monthly_minus_weekly(close: pd.Series) -> pd.Series:
    """RV_m - RV_w — medium-term divergence; positive = weekly below monthly avg."""
    r = _log_returns(close)
    rvd = r ** 2
    rvw = rvd.rolling(WDAYS, min_periods=2).mean()
    rvm = rvd.rolling(22, min_periods=WDAYS).mean()
    return rvm - rvw


def f35_rvre_183_har_monthly_minus_daily(close: pd.Series) -> pd.Series:
    """RV_m - RV_d — long-vs-short divergence; positive = today below monthly avg."""
    r = _log_returns(close)
    rvd = r ** 2
    rvm = rvd.rolling(22, min_periods=WDAYS).mean()
    return rvm - rvd


def f35_rvre_184_har_ratio_weekly_over_monthly(close: pd.Series) -> pd.Series:
    """RV_w / RV_m — slope of vol term structure between weekly and monthly horizons."""
    r = _log_returns(close)
    rvd = r ** 2
    rvw = rvd.rolling(WDAYS, min_periods=2).mean()
    rvm = rvd.rolling(22, min_periods=WDAYS).mean()
    return _safe_div(rvw, rvm)


# ============================================================
# Bucket GG — Realized quarticity (185-188)
# RQ = (N/3) * sum r^4. Used in HAR-Q and as a noise estimator.
# ============================================================

def f35_rvre_185_realized_quarticity_21d(close: pd.Series) -> pd.Series:
    """Realized quarticity (N/3)*sum r^4 over 21d — fourth moment of returns, monthly."""
    r = _log_returns(close)
    n = MDAYS
    return (n / 3.0) * (r ** 4).rolling(n, min_periods=WDAYS).sum()


def f35_rvre_186_realized_quarticity_252d(close: pd.Series) -> pd.Series:
    """Realized quarticity at 252d — fourth-moment annual."""
    r = _log_returns(close)
    n = YDAYS
    return (n / 3.0) * (r ** 4).rolling(n, min_periods=QDAYS).sum()


def f35_rvre_187_log_realized_quarticity_252d(close: pd.Series) -> pd.Series:
    """log(realized quarticity + eps) at 252d — scale-compressed RQ."""
    r = _log_returns(close)
    n = YDAYS
    rq = (n / 3.0) * (r ** 4).rolling(n, min_periods=QDAYS).sum()
    return np.log(rq + 1e-24).where(rq > 0, np.nan)


def f35_rvre_188_har_q_noise_estimate_252d(close: pd.Series) -> pd.Series:
    """sqrt(RQ * 22) / RV at 252d — Andersen-Bollerslev-Meddahi HAR-Q noise-to-signal indicator."""
    r = _log_returns(close)
    n = YDAYS
    rq = (n / 3.0) * (r ** 4).rolling(n, min_periods=QDAYS).sum()
    rv = (r ** 2).rolling(n, min_periods=QDAYS).sum()
    return _safe_div(np.sqrt(rq * 22.0), rv)


# ============================================================
# Bucket HH — EWMA / RiskMetrics (189-194)
# JP Morgan RiskMetrics 1996: sigma^2_t = lambda * sigma^2_{t-1} + (1-lambda) * r^2_{t-1}.
# Standard daily lambda = 0.94. Implemented via .ewm(alpha=1-lambda).
# ============================================================

def f35_rvre_189_ewma_sigma_lambda094(close: pd.Series) -> pd.Series:
    """EWMA sigma with lambda=0.94 (RiskMetrics standard) — fast-decay vol estimate."""
    r = _log_returns(close)
    var = (r ** 2).ewm(alpha=1.0 - 0.94, adjust=False, min_periods=10).mean()
    return np.sqrt(var)


def f35_rvre_190_ewma_sigma_lambda097(close: pd.Series) -> pd.Series:
    """EWMA sigma with lambda=0.97 — slower-decay vol; longer effective memory."""
    r = _log_returns(close)
    var = (r ** 2).ewm(alpha=1.0 - 0.97, adjust=False, min_periods=20).mean()
    return np.sqrt(var)


def f35_rvre_191_ewma_sigma_lambda099(close: pd.Series) -> pd.Series:
    """EWMA sigma with lambda=0.99 — very slow decay; captures secular vol regime."""
    r = _log_returns(close)
    var = (r ** 2).ewm(alpha=1.0 - 0.99, adjust=False, min_periods=63).mean()
    return np.sqrt(var)


def f35_rvre_192_ewma094_var_minus_rv21(close: pd.Series) -> pd.Series:
    """EWMA(0.94) variance minus 21d simple realized variance — disagreement between weighting schemes."""
    r = _log_returns(close)
    ew = (r ** 2).ewm(alpha=1.0 - 0.94, adjust=False, min_periods=10).mean()
    sim = (r ** 2).rolling(MDAYS, min_periods=WDAYS).mean()
    return ew - sim


def f35_rvre_193_ratio_ewma094_over_rv21(close: pd.Series) -> pd.Series:
    """EWMA(0.94) sigma / sqrt(RV21/N) — ratio of fast-decay vol to rolling-mean vol."""
    r = _log_returns(close)
    ew = np.sqrt((r ** 2).ewm(alpha=1.0 - 0.94, adjust=False, min_periods=10).mean())
    sim = np.sqrt((r ** 2).rolling(MDAYS, min_periods=WDAYS).mean())
    return _safe_div(ew, sim)


def f35_rvre_194_ratio_ewma094_over_ewma097(close: pd.Series) -> pd.Series:
    """EWMA(0.94) sigma / EWMA(0.97) sigma — slope of EWMA term structure (fast vs slow)."""
    r = _log_returns(close)
    f1 = np.sqrt((r ** 2).ewm(alpha=1.0 - 0.94, adjust=False, min_periods=10).mean())
    f2 = np.sqrt((r ** 2).ewm(alpha=1.0 - 0.97, adjust=False, min_periods=20).mean())
    return _safe_div(f1, f2)


# ============================================================
# Bucket II — Long-memory vol (195-198)
# Andersen-Bollerslev-Diebold-Labys 2001: vol exhibits long memory (Hurst > 0.5).
# Here we apply the long-memory diagnostic to the ROLLING-RV series itself.
# ============================================================

def _hurst_rs(x: np.ndarray, min_n: int = 10) -> float:
    """Classical R/S Hurst-exponent estimator on a 1-D array (drops NaN)."""
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


def f35_rvre_195_hurst_on_rv21_series_504d(close: pd.Series) -> pd.Series:
    """Hurst exponent (R/S) of trailing 504d window of rolling-RV21 series — long memory in vol itself."""
    r = _log_returns(close)
    rv21 = (r ** 2).rolling(MDAYS, min_periods=WDAYS).sum()
    return rv21.rolling(DDAYS_2Y, min_periods=YDAYS).apply(_hurst_rs, raw=True)


def f35_rvre_196_ar1_log_rv21_252d(close: pd.Series) -> pd.Series:
    """AR(1) coefficient on log(RV21) over 252d — persistence parameter of log-volatility."""
    r = _log_returns(close)
    log_rv21 = np.log((r ** 2).rolling(MDAYS, min_periods=WDAYS).sum() + 1e-12)
    def _ar1(w):
        v = w[~np.isnan(w)]
        if v.size < 21:
            return np.nan
        a = v[:-1]; b = v[1:]
        if a.std() == 0 or b.std() == 0:
            return np.nan
        c = np.corrcoef(a, b)[0, 1]
        return float(c)
    return log_rv21.rolling(YDAYS, min_periods=QDAYS).apply(_ar1, raw=True)


def f35_rvre_197_variance_of_partial_sums_log_rv21_252d(close: pd.Series) -> pd.Series:
    """var(cumsum(log_rv21 - mean)) / N at 252d — long-memory diagnostic (scales differently for I(d) processes)."""
    r = _log_returns(close)
    log_rv21 = np.log((r ** 2).rolling(MDAYS, min_periods=WDAYS).sum() + 1e-12)
    def _vps(w):
        v = w[~np.isnan(w)]
        if v.size < 21:
            return np.nan
        d = v - v.mean()
        c = np.cumsum(d)
        return float(c.var(ddof=1) / v.size)
    return log_rv21.rolling(YDAYS, min_periods=QDAYS).apply(_vps, raw=True)


def f35_rvre_198_long_memory_ratio_rv252_vs_rwalk_252d(close: pd.Series) -> pd.Series:
    """sigma_252 (from sum r^2) / (sigma_1 * sqrt(252)) — deviation from random-walk scaling; 1.0 = no long memory."""
    r = _log_returns(close)
    sig252 = np.sqrt((r ** 2).rolling(YDAYS, min_periods=QDAYS).mean())
    sig1 = r.rolling(WDAYS, min_periods=2).std()   # local 1-bar sigma proxy
    return _safe_div(sig252, sig1)


# ============================================================
# Bucket JJ — Vol regime duration (199-202)
# How long has the current vol-quintile regime been in force?
# ============================================================

def _vol_quintile_state(close: pd.Series, vol_n: int, hist_n: int) -> pd.Series:
    """1-5 quintile state of trailing vol_n RV inside its trailing hist_n distribution."""
    r = _log_returns(close)
    rv = r.rolling(vol_n, min_periods=max(vol_n // 3, 2)).std()
    q20 = rv.rolling(hist_n, min_periods=YDAYS).quantile(0.20)
    q40 = rv.rolling(hist_n, min_periods=YDAYS).quantile(0.40)
    q60 = rv.rolling(hist_n, min_periods=YDAYS).quantile(0.60)
    q80 = rv.rolling(hist_n, min_periods=YDAYS).quantile(0.80)
    s = pd.Series(np.nan, index=close.index)
    s = s.where(~(rv < q20), 1.0)
    s = s.where(~((rv >= q20) & (rv < q40)), 2.0)
    s = s.where(~((rv >= q40) & (rv < q60)), 3.0)
    s = s.where(~((rv >= q60) & (rv < q80)), 4.0)
    s = s.where(~(rv >= q80), 5.0)
    return s


def f35_rvre_199_bars_since_current_vol_quintile_started(close: pd.Series) -> pd.Series:
    """Bars since current vol-quintile (RV21 in 504d) state began — regime duration."""
    s = _vol_quintile_state(close, MDAYS, DDAYS_2Y).values
    n = s.size
    out = np.full(n, np.nan, dtype=float)
    streak = 0
    prev = np.nan
    for i in range(n):
        v = s[i]
        if np.isnan(v):
            streak = 0; prev = np.nan
            out[i] = np.nan
            continue
        if v == prev:
            streak += 1
        else:
            streak = 1; prev = v
        out[i] = float(streak)
    return pd.Series(out, index=close.index)


def f35_rvre_200_bars_since_last_high_vol_exit_504d(close: pd.Series) -> pd.Series:
    """Bars since last transition out of high-vol quintile (state==5 -> not 5) — recovery clock."""
    s = _vol_quintile_state(close, MDAYS, DDAYS_2Y).values
    n = s.size
    out = np.full(n, np.nan, dtype=float)
    last = -1
    for i in range(n):
        if i > 0 and not np.isnan(s[i]) and not np.isnan(s[i - 1]) and s[i - 1] == 5.0 and s[i] != 5.0:
            last = i
        if last >= 0:
            out[i] = float(i - last)
    return pd.Series(out, index=close.index)


def f35_rvre_201_bars_since_last_low_vol_entry_504d(close: pd.Series) -> pd.Series:
    """Bars since last transition into low-vol quintile (not 1 -> state==1) — low-vol arrival clock."""
    s = _vol_quintile_state(close, MDAYS, DDAYS_2Y).values
    n = s.size
    out = np.full(n, np.nan, dtype=float)
    last = -1
    for i in range(n):
        if i > 0 and not np.isnan(s[i]) and not np.isnan(s[i - 1]) and s[i - 1] != 1.0 and s[i] == 1.0:
            last = i
        if last >= 0:
            out[i] = float(i - last)
    return pd.Series(out, index=close.index)


def f35_rvre_202_vol_regime_change_rate_504d(close: pd.Series) -> pd.Series:
    """Number of vol-quintile state changes in trailing 504d divided by 504 — annualized regime-flip rate."""
    s = _vol_quintile_state(close, MDAYS, DDAYS_2Y)
    flips = (s.diff() != 0).astype(float).where(s.notna() & s.shift(1).notna(), np.nan)
    return flips.rolling(DDAYS_2Y, min_periods=YDAYS).sum() / float(DDAYS_2Y)


# ============================================================
# Bucket KK — True vol-of-vol on the RV series (203-206)
# Distinct from existing "vol of vol" which used ratios. Here we compute
# RV applied to the RV-time-series itself.
# ============================================================

def f35_rvre_203_realized_vol_of_log_rv21_252d(close: pd.Series) -> pd.Series:
    """Std of log(RV21) over 252d — true vol-of-vol in log-variance space."""
    r = _log_returns(close)
    log_rv21 = np.log((r ** 2).rolling(MDAYS, min_periods=WDAYS).sum() + 1e-12)
    return log_rv21.rolling(YDAYS, min_periods=QDAYS).std()


def f35_rvre_204_realized_variance_of_rv63_252d(close: pd.Series) -> pd.Series:
    """Var of RV63 series over 252d — second-moment of slow vol regime."""
    r = _log_returns(close)
    rv63 = (r ** 2).rolling(QDAYS, min_periods=MDAYS).sum()
    return rv63.rolling(YDAYS, min_periods=QDAYS).var()


def f35_rvre_205_ratio_vov_252_over_504(close: pd.Series) -> pd.Series:
    """vol-of-vol(252d) / vol-of-vol(504d) of log(RV21) — slope of vov term structure."""
    r = _log_returns(close)
    log_rv21 = np.log((r ** 2).rolling(MDAYS, min_periods=WDAYS).sum() + 1e-12)
    vov_s = log_rv21.rolling(YDAYS, min_periods=QDAYS).std()
    vov_l = log_rv21.rolling(DDAYS_2Y, min_periods=YDAYS).std()
    return _safe_div(vov_s, vov_l)


def f35_rvre_206_zscore_vov_in_504d(close: pd.Series) -> pd.Series:
    """Z-score of vov_252 (of log RV21) in its 504d distribution — vov-regime extremity."""
    r = _log_returns(close)
    log_rv21 = np.log((r ** 2).rolling(MDAYS, min_periods=WDAYS).sum() + 1e-12)
    vov = log_rv21.rolling(YDAYS, min_periods=QDAYS).std()
    return _rolling_zscore(vov, DDAYS_2Y, min_periods=YDAYS)


# ============================================================
# Bucket LL — Vol crash / sudden drop indicators (207-210)
# ============================================================

def f35_rvre_207_vol_crash_indicator_21d(close: pd.Series) -> pd.Series:
    """Indicator: RV21 < 0.3 * max(RV21)_252d — vol has crashed to <30% of recent peak."""
    r = _log_returns(close)
    rv21 = (r ** 2).rolling(MDAYS, min_periods=WDAYS).sum()
    rmax = rv21.rolling(YDAYS, min_periods=QDAYS).max()
    flag = (rv21 < 0.3 * rmax).astype(float).where(rmax.notna() & rv21.notna(), np.nan)
    return flag


def f35_rvre_208_vol_expansion_indicator_21d(close: pd.Series) -> pd.Series:
    """Indicator: RV21 > 3 * min(RV21)_252d — vol has expanded to >3x recent trough."""
    r = _log_returns(close)
    rv21 = (r ** 2).rolling(MDAYS, min_periods=WDAYS).sum()
    rmin = rv21.rolling(YDAYS, min_periods=QDAYS).min()
    flag = (rv21 > 3.0 * rmin).astype(float).where(rmin.notna() & rv21.notna(), np.nan)
    return flag


def f35_rvre_209_bars_since_last_vol_crash_252d(close: pd.Series) -> pd.Series:
    """Bars since last bar that satisfied the vol-crash indicator — recency of vol collapse."""
    r = _log_returns(close)
    rv21 = (r ** 2).rolling(MDAYS, min_periods=WDAYS).sum()
    rmax = rv21.rolling(YDAYS, min_periods=QDAYS).max()
    crash = (rv21 < 0.3 * rmax).values
    n = crash.size
    out = np.full(n, np.nan, dtype=float)
    last = -1
    for i in range(n):
        if crash[i]:
            last = i
        if last >= 0:
            out[i] = float(i - last)
    return pd.Series(out, index=close.index)


def f35_rvre_210_largest_rv21_drop_in_252d(close: pd.Series) -> pd.Series:
    """Largest single-step 21d drop in RV21 (in log units) over trailing 252d — biggest vol-down move."""
    r = _log_returns(close)
    rv21 = (r ** 2).rolling(MDAYS, min_periods=WDAYS).sum()
    drop = np.log(rv21 + 1e-12).diff(MDAYS)   # 21d change in log RV21
    return (-drop).rolling(YDAYS, min_periods=QDAYS).max()   # most negative -> max of -drop


# ============================================================
# Bucket MM — Spectral / cycle (211-214)
# Periodogram-based vol cycle detection on |r| or r^2.
# ============================================================

def _periodogram_peak_index(w: np.ndarray, min_n: int = 60) -> float:
    v = w[~np.isnan(w)]
    if v.size < min_n:
        return np.nan
    v = v - v.mean()
    f = np.fft.rfft(v)
    p = (f * f.conj()).real
    if p.size < 3:
        return np.nan
    # ignore DC (index 0); find peak in the rest
    pk = int(np.argmax(p[1:])) + 1
    return float(pk)


def _periodogram_at_freq(w: np.ndarray, freq_idx: int, min_n: int = 60) -> float:
    v = w[~np.isnan(w)]
    if v.size < min_n:
        return np.nan
    v = v - v.mean()
    f = np.fft.rfft(v)
    p = (f * f.conj()).real
    if freq_idx >= p.size:
        return np.nan
    return float(p[freq_idx])


def _spectral_entropy(w: np.ndarray, min_n: int = 60) -> float:
    v = w[~np.isnan(w)]
    if v.size < min_n:
        return np.nan
    v = v - v.mean()
    f = np.fft.rfft(v)
    p = (f * f.conj()).real
    p = p[1:]
    s = p.sum()
    if s <= 0:
        return np.nan
    pn = p / s
    pn = pn[pn > 0]
    return float(-(pn * np.log2(pn)).sum())


def f35_rvre_211_periodogram_peak_period_abs_r_252d(close: pd.Series) -> pd.Series:
    """Index of dominant frequency in periodogram of |r| over 252d — captures recurring vol-cycle length."""
    r = _log_returns(close)
    return r.abs().rolling(YDAYS, min_periods=QDAYS).apply(_periodogram_peak_index, raw=True)


def f35_rvre_212_periodogram_power_at_freq5_abs_r_252d(close: pd.Series) -> pd.Series:
    """Spectral power at FFT bin index = N/5 of |r| over 252d — weekly-cycle vol energy."""
    r = _log_returns(close)
    return r.abs().rolling(YDAYS, min_periods=QDAYS).apply(
        lambda w: _periodogram_at_freq(w, max(1, int(len(w) // 5))), raw=True
    )


def f35_rvre_213_periodogram_peak_period_rsq_504d(close: pd.Series) -> pd.Series:
    """Dominant frequency in periodogram of r^2 over 504d — long-window vol-cycle indicator."""
    r = _log_returns(close)
    return (r ** 2).rolling(DDAYS_2Y, min_periods=YDAYS).apply(_periodogram_peak_index, raw=True)


def f35_rvre_214_spectral_entropy_abs_r_252d(close: pd.Series) -> pd.Series:
    """Shannon entropy of normalized power spectrum of |r| over 252d — vol-spectrum diffuseness."""
    r = _log_returns(close)
    return r.abs().rolling(YDAYS, min_periods=QDAYS).apply(_spectral_entropy, raw=True)


# ============================================================
# Bucket NN — MIDAS-style weighted RV (215-218)
# Apply non-uniform weights inside the rolling window — different from
# simple .rolling().mean() (uniform) or EWMA (geometric-decay infinite memory).
# ============================================================

def _weighted_rv(r2: pd.Series, n: int, mp: int, weights: np.ndarray) -> pd.Series:
    weights = np.asarray(weights, dtype=float)
    def _f(wnd):
        valid = ~np.isnan(wnd)
        if valid.sum() < mp:
            return np.nan
        local_weights = weights[-len(wnd):]
        vw = local_weights[valid]
        if vw.sum() == 0:
            return np.nan
        return float(np.sum(wnd[valid] * vw) / np.sum(vw))
    return r2.rolling(n, min_periods=mp).apply(_f, raw=True)

def f35_rvre_215_midas_rv_geom_decay_63d(close: pd.Series) -> pd.Series:
    """MIDAS-RV with geometric weights w_i = 0.95^(N-1-i) over 63d — recency-biased weighted RV."""
    r = _log_returns(close)
    weights = np.array([0.95 ** (QDAYS - 1 - i) for i in range(QDAYS)], dtype=float)
    return _weighted_rv(r ** 2, QDAYS, MDAYS, weights)


def f35_rvre_216_midas_rv_exponential_63d(close: pd.Series) -> pd.Series:
    """MIDAS-RV with exponential weights exp(-0.05*(N-1-i)) over 63d — alternative recency profile."""
    r = _log_returns(close)
    lags = np.arange(QDAYS, dtype=float)
    weights = np.exp(-0.05 * (QDAYS - 1 - lags))
    return _weighted_rv(r ** 2, QDAYS, MDAYS, weights)


def f35_rvre_217_midas_rv_beta_weights_63d(close: pd.Series) -> pd.Series:
    """MIDAS-RV with beta(2,4) shape weights over 63d — Ghysels-Sinko-Valkanov style beta polynomial weighting."""
    r = _log_returns(close)
    x = (np.arange(QDAYS, dtype=float) + 1.0) / (QDAYS + 1.0)
    # Beta(2,4) pdf shape, no normalization needed (we normalize inside _weighted_rv)
    weights = (x ** 1) * ((1.0 - x) ** 3)
    return _weighted_rv(r ** 2, QDAYS, MDAYS, weights)


def f35_rvre_218_midas_rv_linear_decay_63d(close: pd.Series) -> pd.Series:
    """MIDAS-RV with linear weights (i+1) over 63d — naive recency-up-weighting."""
    r = _log_returns(close)
    weights = (np.arange(QDAYS, dtype=float) + 1.0)
    return _weighted_rv(r ** 2, QDAYS, MDAYS, weights)


# ============================================================
# Bucket OO — RV autocorrelation multi-lag (219-222)
# (We already have AR1 of r^2 at lag 1. These are autocorrelations of the
#  RV series itself at multiple lags — distinct concept.)
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


def f35_rvre_219_autocorr_rv21_lag1_252d(close: pd.Series) -> pd.Series:
    """Autocorrelation of RV21 series at lag 1 over 252d — RV persistence at daily lag."""
    r = _log_returns(close)
    rv21 = (r ** 2).rolling(MDAYS, min_periods=WDAYS).sum()
    return _autocorr_lag(rv21, 1, YDAYS, QDAYS)


def f35_rvre_220_autocorr_rv21_lag5_252d(close: pd.Series) -> pd.Series:
    """Autocorrelation of RV21 series at lag 5 over 252d — weekly-spaced RV correlation."""
    r = _log_returns(close)
    rv21 = (r ** 2).rolling(MDAYS, min_periods=WDAYS).sum()
    return _autocorr_lag(rv21, 5, YDAYS, QDAYS)


def f35_rvre_221_autocorr_rv21_lag21_504d(close: pd.Series) -> pd.Series:
    """Autocorrelation of RV21 series at lag 21 over 504d — monthly-spaced RV correlation."""
    r = _log_returns(close)
    rv21 = (r ** 2).rolling(MDAYS, min_periods=WDAYS).sum()
    return _autocorr_lag(rv21, 21, DDAYS_2Y, YDAYS)


def f35_rvre_222_partial_autocorr_rv21_lag1_252d(close: pd.Series) -> pd.Series:
    """Partial autocorrelation (Durbin-Levinson approx — equals corr(RV21_t, RV21_{t-1}|RV21_{t-2}) at lag 1) over 252d."""
    r = _log_returns(close)
    rv21 = (r ** 2).rolling(MDAYS, min_periods=WDAYS).sum()
    def _pac(w):
        v = w[~np.isnan(w)]
        if v.size < 30:
            return np.nan
        # Residual of regressing v_t and v_{t-1} on v_{t-2}, then correlation.
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
    return rv21.rolling(YDAYS, min_periods=QDAYS).apply(_pac, raw=True)


# ============================================================
# Bucket PP — HAR-RV-J & regime composites (223-225)
# ============================================================

def f35_rvre_223_har_rv_j_composite_score_252d(close: pd.Series) -> pd.Series:
    """Z-blend of RV_d, RV_w, RV_m, jump_var at 252d — HAR-RV-J style multi-component vol regime score."""
    r = _log_returns(close)
    rvd = r ** 2
    rvw = rvd.rolling(WDAYS, min_periods=2).mean()
    rvm = rvd.rolling(22, min_periods=WDAYS).mean()
    rv252 = rvd.rolling(YDAYS, min_periods=QDAYS).sum()
    bpv252 = _bpv_series(r).rolling(YDAYS, min_periods=QDAYS).sum()
    jv = (rv252 - bpv252).clip(lower=0.0)
    z_d = _rolling_zscore(rvd, DDAYS_2Y, min_periods=YDAYS)
    z_w = _rolling_zscore(rvw, DDAYS_2Y, min_periods=YDAYS)
    z_m = _rolling_zscore(rvm, DDAYS_2Y, min_periods=YDAYS)
    z_j = _rolling_zscore(jv, DDAYS_2Y, min_periods=YDAYS)
    return (z_d + z_w + z_m + z_j) / 4.0


def f35_rvre_224_jump_dominant_high_vol_indicator_252d(close: pd.Series) -> pd.Series:
    """Indicator: jump_share_252 > 0.3 AND RV252 > 80th-percentile in 1260d — jump-dominated high-vol regime."""
    r = _log_returns(close)
    rv252 = (r ** 2).rolling(YDAYS, min_periods=QDAYS).sum()
    bpv252 = _bpv_series(r).rolling(YDAYS, min_periods=QDAYS).sum()
    share = (1.0 - _safe_div(bpv252, rv252)).clip(lower=0.0)
    p80 = rv252.rolling(DDAYS_5Y, min_periods=YDAYS).quantile(0.80)
    flag = ((share > 0.30) & (rv252 > p80)).astype(float).where(p80.notna() & share.notna(), np.nan)
    return flag


def f35_rvre_225_vol_regime_severity_composite_252d(close: pd.Series) -> pd.Series:
    """Z-blend of vol-cone position, vol-of-vol, RV persistence — overall regime-severity composite."""
    r = _log_returns(close)
    rv21 = (r ** 2).rolling(MDAYS, min_periods=WDAYS).sum()
    rv21_in_504_rank = rv21.rolling(DDAYS_2Y, min_periods=YDAYS).rank(pct=True)
    log_rv21 = np.log(rv21 + 1e-12)
    vov = log_rv21.rolling(YDAYS, min_periods=QDAYS).std()
    pers = _autocorr_lag(rv21, 1, YDAYS, QDAYS)
    z_pos = _rolling_zscore(rv21_in_504_rank, DDAYS_2Y, min_periods=YDAYS)
    z_vov = _rolling_zscore(vov, DDAYS_2Y, min_periods=YDAYS)
    z_per = _rolling_zscore(pers, DDAYS_2Y, min_periods=YDAYS)
    return (z_pos + z_vov + z_per) / 3.0


# ============================================================
#                         REGISTRY 151-225
# ============================================================



def f35_rvre_151_bpv_21d_d2(close):
    return f35_rvre_151_bpv_21d(close).diff().diff()


def f35_rvre_152_bpv_63d_d2(close):
    return f35_rvre_152_bpv_63d(close).diff().diff()


def f35_rvre_153_bpv_252d_d2(close):
    return f35_rvre_153_bpv_252d(close).diff().diff()


def f35_rvre_154_log_bpv_252d_d2(close):
    return f35_rvre_154_log_bpv_252d(close).diff().diff()


def f35_rvre_155_bpv_sigma_annualized_21d_d2(close):
    return f35_rvre_155_bpv_sigma_annualized_21d(close).diff().diff()


def f35_rvre_156_bpv_sigma_annualized_252d_d2(close):
    return f35_rvre_156_bpv_sigma_annualized_252d(close).diff().diff()


def f35_rvre_157_bpv_5d_d2(close):
    return f35_rvre_157_bpv_5d(close).diff().diff()


def f35_rvre_158_medrv_21d_d2(close):
    return f35_rvre_158_medrv_21d(close).diff().diff()


def f35_rvre_159_medrv_63d_d2(close):
    return f35_rvre_159_medrv_63d(close).diff().diff()


def f35_rvre_160_medrv_252d_d2(close):
    return f35_rvre_160_medrv_252d(close).diff().diff()


def f35_rvre_161_minrv_21d_d2(close):
    return f35_rvre_161_minrv_21d(close).diff().diff()


def f35_rvre_162_minrv_63d_d2(close):
    return f35_rvre_162_minrv_63d(close).diff().diff()


def f35_rvre_163_minrv_252d_d2(close):
    return f35_rvre_163_minrv_252d(close).diff().diff()


def f35_rvre_164_trv_21d_k3_d2(close):
    return f35_rvre_164_trv_21d_k3(close).diff().diff()


def f35_rvre_165_trv_63d_k3_d2(close):
    return f35_rvre_165_trv_63d_k3(close).diff().diff()


def f35_rvre_166_trv_252d_k3_d2(close):
    return f35_rvre_166_trv_252d_k3(close).diff().diff()


def f35_rvre_167_truncation_rate_252d_d2(close):
    return f35_rvre_167_truncation_rate_252d(close).diff().diff()


def f35_rvre_168_jump_var_21d_d2(close):
    return f35_rvre_168_jump_var_21d(close).diff().diff()


def f35_rvre_169_jump_var_252d_d2(close):
    return f35_rvre_169_jump_var_252d(close).diff().diff()


def f35_rvre_170_log_jump_var_252d_d2(close):
    return f35_rvre_170_log_jump_var_252d(close).diff().diff()


def f35_rvre_171_significant_jump_indicator_21d_d2(close):
    return f35_rvre_171_significant_jump_indicator_21d(close).diff().diff()


def f35_rvre_172_count_jump_days_in_21d_d2(close):
    return f35_rvre_172_count_jump_days_in_21d(close).diff().diff()


def f35_rvre_173_count_jump_days_in_252d_d2(close):
    return f35_rvre_173_count_jump_days_in_252d(close).diff().diff()


def f35_rvre_174_continuous_var_share_21d_d2(close):
    return f35_rvre_174_continuous_var_share_21d(close).diff().diff()


def f35_rvre_175_continuous_var_share_252d_d2(close):
    return f35_rvre_175_continuous_var_share_252d(close).diff().diff()


def f35_rvre_176_jump_share_21d_d2(close):
    return f35_rvre_176_jump_share_21d(close).diff().diff()


def f35_rvre_177_jump_share_252d_d2(close):
    return f35_rvre_177_jump_share_252d(close).diff().diff()


def f35_rvre_178_har_rv_daily_component_d2(close):
    return f35_rvre_178_har_rv_daily_component(close).diff().diff()


def f35_rvre_179_har_rv_weekly_component_d2(close):
    return f35_rvre_179_har_rv_weekly_component(close).diff().diff()


def f35_rvre_180_har_rv_monthly_component_d2(close):
    return f35_rvre_180_har_rv_monthly_component(close).diff().diff()


def f35_rvre_181_har_weekly_minus_daily_d2(close):
    return f35_rvre_181_har_weekly_minus_daily(close).diff().diff()


def f35_rvre_182_har_monthly_minus_weekly_d2(close):
    return f35_rvre_182_har_monthly_minus_weekly(close).diff().diff()


def f35_rvre_183_har_monthly_minus_daily_d2(close):
    return f35_rvre_183_har_monthly_minus_daily(close).diff().diff()


def f35_rvre_184_har_ratio_weekly_over_monthly_d2(close):
    return f35_rvre_184_har_ratio_weekly_over_monthly(close).diff().diff()


def f35_rvre_185_realized_quarticity_21d_d2(close):
    return f35_rvre_185_realized_quarticity_21d(close).diff().diff()


def f35_rvre_186_realized_quarticity_252d_d2(close):
    return f35_rvre_186_realized_quarticity_252d(close).diff().diff()


def f35_rvre_187_log_realized_quarticity_252d_d2(close):
    return f35_rvre_187_log_realized_quarticity_252d(close).diff().diff()


def f35_rvre_188_har_q_noise_estimate_252d_d2(close):
    return f35_rvre_188_har_q_noise_estimate_252d(close).diff().diff()


def f35_rvre_189_ewma_sigma_lambda094_d2(close):
    return f35_rvre_189_ewma_sigma_lambda094(close).diff().diff()


def f35_rvre_190_ewma_sigma_lambda097_d2(close):
    return f35_rvre_190_ewma_sigma_lambda097(close).diff().diff()


def f35_rvre_191_ewma_sigma_lambda099_d2(close):
    return f35_rvre_191_ewma_sigma_lambda099(close).diff().diff()


def f35_rvre_192_ewma094_var_minus_rv21_d2(close):
    return f35_rvre_192_ewma094_var_minus_rv21(close).diff().diff()


def f35_rvre_193_ratio_ewma094_over_rv21_d2(close):
    return f35_rvre_193_ratio_ewma094_over_rv21(close).diff().diff()


def f35_rvre_194_ratio_ewma094_over_ewma097_d2(close):
    return f35_rvre_194_ratio_ewma094_over_ewma097(close).diff().diff()


def f35_rvre_195_hurst_on_rv21_series_504d_d2(close):
    return f35_rvre_195_hurst_on_rv21_series_504d(close).diff().diff()


def f35_rvre_196_ar1_log_rv21_252d_d2(close):
    return f35_rvre_196_ar1_log_rv21_252d(close).diff().diff()


def f35_rvre_197_variance_of_partial_sums_log_rv21_252d_d2(close):
    return f35_rvre_197_variance_of_partial_sums_log_rv21_252d(close).diff().diff()


def f35_rvre_198_long_memory_ratio_rv252_vs_rwalk_252d_d2(close):
    return f35_rvre_198_long_memory_ratio_rv252_vs_rwalk_252d(close).diff().diff()


def f35_rvre_199_bars_since_current_vol_quintile_started_d2(close):
    return f35_rvre_199_bars_since_current_vol_quintile_started(close).diff().diff()


def f35_rvre_200_bars_since_last_high_vol_exit_504d_d2(close):
    return f35_rvre_200_bars_since_last_high_vol_exit_504d(close).diff().diff()


def f35_rvre_201_bars_since_last_low_vol_entry_504d_d2(close):
    return f35_rvre_201_bars_since_last_low_vol_entry_504d(close).diff().diff()


def f35_rvre_202_vol_regime_change_rate_504d_d2(close):
    return f35_rvre_202_vol_regime_change_rate_504d(close).diff().diff()


def f35_rvre_203_realized_vol_of_log_rv21_252d_d2(close):
    return f35_rvre_203_realized_vol_of_log_rv21_252d(close).diff().diff()


def f35_rvre_204_realized_variance_of_rv63_252d_d2(close):
    return f35_rvre_204_realized_variance_of_rv63_252d(close).diff().diff()


def f35_rvre_205_ratio_vov_252_over_504_d2(close):
    return f35_rvre_205_ratio_vov_252_over_504(close).diff().diff()


def f35_rvre_206_zscore_vov_in_504d_d2(close):
    return f35_rvre_206_zscore_vov_in_504d(close).diff().diff()


def f35_rvre_207_vol_crash_indicator_21d_d2(close):
    return f35_rvre_207_vol_crash_indicator_21d(close).diff().diff()


def f35_rvre_208_vol_expansion_indicator_21d_d2(close):
    return f35_rvre_208_vol_expansion_indicator_21d(close).diff().diff()


def f35_rvre_209_bars_since_last_vol_crash_252d_d2(close):
    return f35_rvre_209_bars_since_last_vol_crash_252d(close).diff().diff()


def f35_rvre_210_largest_rv21_drop_in_252d_d2(close):
    return f35_rvre_210_largest_rv21_drop_in_252d(close).diff().diff()


def f35_rvre_211_periodogram_peak_period_abs_r_252d_d2(close):
    return f35_rvre_211_periodogram_peak_period_abs_r_252d(close).diff().diff()


def f35_rvre_212_periodogram_power_at_freq5_abs_r_252d_d2(close):
    return f35_rvre_212_periodogram_power_at_freq5_abs_r_252d(close).diff().diff()


def f35_rvre_213_periodogram_peak_period_rsq_504d_d2(close):
    return f35_rvre_213_periodogram_peak_period_rsq_504d(close).diff().diff()


def f35_rvre_214_spectral_entropy_abs_r_252d_d2(close):
    return f35_rvre_214_spectral_entropy_abs_r_252d(close).diff().diff()


def f35_rvre_215_midas_rv_geom_decay_63d_d2(close):
    return f35_rvre_215_midas_rv_geom_decay_63d(close).diff().diff()


def f35_rvre_216_midas_rv_exponential_63d_d2(close):
    return f35_rvre_216_midas_rv_exponential_63d(close).diff().diff()


def f35_rvre_217_midas_rv_beta_weights_63d_d2(close):
    return f35_rvre_217_midas_rv_beta_weights_63d(close).diff().diff()


def f35_rvre_218_midas_rv_linear_decay_63d_d2(close):
    return f35_rvre_218_midas_rv_linear_decay_63d(close).diff().diff()


def f35_rvre_219_autocorr_rv21_lag1_252d_d2(close):
    return f35_rvre_219_autocorr_rv21_lag1_252d(close).diff().diff()


def f35_rvre_220_autocorr_rv21_lag5_252d_d2(close):
    return f35_rvre_220_autocorr_rv21_lag5_252d(close).diff().diff()


def f35_rvre_221_autocorr_rv21_lag21_504d_d2(close):
    return f35_rvre_221_autocorr_rv21_lag21_504d(close).diff().diff()


def f35_rvre_222_partial_autocorr_rv21_lag1_252d_d2(close):
    return f35_rvre_222_partial_autocorr_rv21_lag1_252d(close).diff().diff()


def f35_rvre_223_har_rv_j_composite_score_252d_d2(close):
    return f35_rvre_223_har_rv_j_composite_score_252d(close).diff().diff()


def f35_rvre_224_jump_dominant_high_vol_indicator_252d_d2(close):
    return f35_rvre_224_jump_dominant_high_vol_indicator_252d(close).diff().diff()


def f35_rvre_225_vol_regime_severity_composite_252d_d2(close):
    return f35_rvre_225_vol_regime_severity_composite_252d(close).diff().diff()


REALIZED_VOLATILITY_REGIME_D2_REGISTRY_151_225 = {
    "f35_rvre_151_bpv_21d_d2": {"inputs": ["close"], "func": f35_rvre_151_bpv_21d_d2},
    "f35_rvre_152_bpv_63d_d2": {"inputs": ["close"], "func": f35_rvre_152_bpv_63d_d2},
    "f35_rvre_153_bpv_252d_d2": {"inputs": ["close"], "func": f35_rvre_153_bpv_252d_d2},
    "f35_rvre_154_log_bpv_252d_d2": {"inputs": ["close"], "func": f35_rvre_154_log_bpv_252d_d2},
    "f35_rvre_155_bpv_sigma_annualized_21d_d2": {"inputs": ["close"], "func": f35_rvre_155_bpv_sigma_annualized_21d_d2},
    "f35_rvre_156_bpv_sigma_annualized_252d_d2": {"inputs": ["close"], "func": f35_rvre_156_bpv_sigma_annualized_252d_d2},
    "f35_rvre_157_bpv_5d_d2": {"inputs": ["close"], "func": f35_rvre_157_bpv_5d_d2},
    "f35_rvre_158_medrv_21d_d2": {"inputs": ["close"], "func": f35_rvre_158_medrv_21d_d2},
    "f35_rvre_159_medrv_63d_d2": {"inputs": ["close"], "func": f35_rvre_159_medrv_63d_d2},
    "f35_rvre_160_medrv_252d_d2": {"inputs": ["close"], "func": f35_rvre_160_medrv_252d_d2},
    "f35_rvre_161_minrv_21d_d2": {"inputs": ["close"], "func": f35_rvre_161_minrv_21d_d2},
    "f35_rvre_162_minrv_63d_d2": {"inputs": ["close"], "func": f35_rvre_162_minrv_63d_d2},
    "f35_rvre_163_minrv_252d_d2": {"inputs": ["close"], "func": f35_rvre_163_minrv_252d_d2},
    "f35_rvre_164_trv_21d_k3_d2": {"inputs": ["close"], "func": f35_rvre_164_trv_21d_k3_d2},
    "f35_rvre_165_trv_63d_k3_d2": {"inputs": ["close"], "func": f35_rvre_165_trv_63d_k3_d2},
    "f35_rvre_166_trv_252d_k3_d2": {"inputs": ["close"], "func": f35_rvre_166_trv_252d_k3_d2},
    "f35_rvre_167_truncation_rate_252d_d2": {"inputs": ["close"], "func": f35_rvre_167_truncation_rate_252d_d2},
    "f35_rvre_168_jump_var_21d_d2": {"inputs": ["close"], "func": f35_rvre_168_jump_var_21d_d2},
    "f35_rvre_169_jump_var_252d_d2": {"inputs": ["close"], "func": f35_rvre_169_jump_var_252d_d2},
    "f35_rvre_170_log_jump_var_252d_d2": {"inputs": ["close"], "func": f35_rvre_170_log_jump_var_252d_d2},
    "f35_rvre_171_significant_jump_indicator_21d_d2": {"inputs": ["close"], "func": f35_rvre_171_significant_jump_indicator_21d_d2},
    "f35_rvre_172_count_jump_days_in_21d_d2": {"inputs": ["close"], "func": f35_rvre_172_count_jump_days_in_21d_d2},
    "f35_rvre_173_count_jump_days_in_252d_d2": {"inputs": ["close"], "func": f35_rvre_173_count_jump_days_in_252d_d2},
    "f35_rvre_174_continuous_var_share_21d_d2": {"inputs": ["close"], "func": f35_rvre_174_continuous_var_share_21d_d2},
    "f35_rvre_175_continuous_var_share_252d_d2": {"inputs": ["close"], "func": f35_rvre_175_continuous_var_share_252d_d2},
    "f35_rvre_176_jump_share_21d_d2": {"inputs": ["close"], "func": f35_rvre_176_jump_share_21d_d2},
    "f35_rvre_177_jump_share_252d_d2": {"inputs": ["close"], "func": f35_rvre_177_jump_share_252d_d2},
    "f35_rvre_178_har_rv_daily_component_d2": {"inputs": ["close"], "func": f35_rvre_178_har_rv_daily_component_d2},
    "f35_rvre_179_har_rv_weekly_component_d2": {"inputs": ["close"], "func": f35_rvre_179_har_rv_weekly_component_d2},
    "f35_rvre_180_har_rv_monthly_component_d2": {"inputs": ["close"], "func": f35_rvre_180_har_rv_monthly_component_d2},
    "f35_rvre_181_har_weekly_minus_daily_d2": {"inputs": ["close"], "func": f35_rvre_181_har_weekly_minus_daily_d2},
    "f35_rvre_182_har_monthly_minus_weekly_d2": {"inputs": ["close"], "func": f35_rvre_182_har_monthly_minus_weekly_d2},
    "f35_rvre_183_har_monthly_minus_daily_d2": {"inputs": ["close"], "func": f35_rvre_183_har_monthly_minus_daily_d2},
    "f35_rvre_184_har_ratio_weekly_over_monthly_d2": {"inputs": ["close"], "func": f35_rvre_184_har_ratio_weekly_over_monthly_d2},
    "f35_rvre_185_realized_quarticity_21d_d2": {"inputs": ["close"], "func": f35_rvre_185_realized_quarticity_21d_d2},
    "f35_rvre_186_realized_quarticity_252d_d2": {"inputs": ["close"], "func": f35_rvre_186_realized_quarticity_252d_d2},
    "f35_rvre_187_log_realized_quarticity_252d_d2": {"inputs": ["close"], "func": f35_rvre_187_log_realized_quarticity_252d_d2},
    "f35_rvre_188_har_q_noise_estimate_252d_d2": {"inputs": ["close"], "func": f35_rvre_188_har_q_noise_estimate_252d_d2},
    "f35_rvre_189_ewma_sigma_lambda094_d2": {"inputs": ["close"], "func": f35_rvre_189_ewma_sigma_lambda094_d2},
    "f35_rvre_190_ewma_sigma_lambda097_d2": {"inputs": ["close"], "func": f35_rvre_190_ewma_sigma_lambda097_d2},
    "f35_rvre_191_ewma_sigma_lambda099_d2": {"inputs": ["close"], "func": f35_rvre_191_ewma_sigma_lambda099_d2},
    "f35_rvre_192_ewma094_var_minus_rv21_d2": {"inputs": ["close"], "func": f35_rvre_192_ewma094_var_minus_rv21_d2},
    "f35_rvre_193_ratio_ewma094_over_rv21_d2": {"inputs": ["close"], "func": f35_rvre_193_ratio_ewma094_over_rv21_d2},
    "f35_rvre_194_ratio_ewma094_over_ewma097_d2": {"inputs": ["close"], "func": f35_rvre_194_ratio_ewma094_over_ewma097_d2},
    "f35_rvre_195_hurst_on_rv21_series_504d_d2": {"inputs": ["close"], "func": f35_rvre_195_hurst_on_rv21_series_504d_d2},
    "f35_rvre_196_ar1_log_rv21_252d_d2": {"inputs": ["close"], "func": f35_rvre_196_ar1_log_rv21_252d_d2},
    "f35_rvre_197_variance_of_partial_sums_log_rv21_252d_d2": {"inputs": ["close"], "func": f35_rvre_197_variance_of_partial_sums_log_rv21_252d_d2},
    "f35_rvre_198_long_memory_ratio_rv252_vs_rwalk_252d_d2": {"inputs": ["close"], "func": f35_rvre_198_long_memory_ratio_rv252_vs_rwalk_252d_d2},
    "f35_rvre_199_bars_since_current_vol_quintile_started_d2": {"inputs": ["close"], "func": f35_rvre_199_bars_since_current_vol_quintile_started_d2},
    "f35_rvre_200_bars_since_last_high_vol_exit_504d_d2": {"inputs": ["close"], "func": f35_rvre_200_bars_since_last_high_vol_exit_504d_d2},
    "f35_rvre_201_bars_since_last_low_vol_entry_504d_d2": {"inputs": ["close"], "func": f35_rvre_201_bars_since_last_low_vol_entry_504d_d2},
    "f35_rvre_202_vol_regime_change_rate_504d_d2": {"inputs": ["close"], "func": f35_rvre_202_vol_regime_change_rate_504d_d2},
    "f35_rvre_203_realized_vol_of_log_rv21_252d_d2": {"inputs": ["close"], "func": f35_rvre_203_realized_vol_of_log_rv21_252d_d2},
    "f35_rvre_204_realized_variance_of_rv63_252d_d2": {"inputs": ["close"], "func": f35_rvre_204_realized_variance_of_rv63_252d_d2},
    "f35_rvre_205_ratio_vov_252_over_504_d2": {"inputs": ["close"], "func": f35_rvre_205_ratio_vov_252_over_504_d2},
    "f35_rvre_206_zscore_vov_in_504d_d2": {"inputs": ["close"], "func": f35_rvre_206_zscore_vov_in_504d_d2},
    "f35_rvre_207_vol_crash_indicator_21d_d2": {"inputs": ["close"], "func": f35_rvre_207_vol_crash_indicator_21d_d2},
    "f35_rvre_208_vol_expansion_indicator_21d_d2": {"inputs": ["close"], "func": f35_rvre_208_vol_expansion_indicator_21d_d2},
    "f35_rvre_209_bars_since_last_vol_crash_252d_d2": {"inputs": ["close"], "func": f35_rvre_209_bars_since_last_vol_crash_252d_d2},
    "f35_rvre_210_largest_rv21_drop_in_252d_d2": {"inputs": ["close"], "func": f35_rvre_210_largest_rv21_drop_in_252d_d2},
    "f35_rvre_211_periodogram_peak_period_abs_r_252d_d2": {"inputs": ["close"], "func": f35_rvre_211_periodogram_peak_period_abs_r_252d_d2},
    "f35_rvre_212_periodogram_power_at_freq5_abs_r_252d_d2": {"inputs": ["close"], "func": f35_rvre_212_periodogram_power_at_freq5_abs_r_252d_d2},
    "f35_rvre_213_periodogram_peak_period_rsq_504d_d2": {"inputs": ["close"], "func": f35_rvre_213_periodogram_peak_period_rsq_504d_d2},
    "f35_rvre_214_spectral_entropy_abs_r_252d_d2": {"inputs": ["close"], "func": f35_rvre_214_spectral_entropy_abs_r_252d_d2},
    "f35_rvre_215_midas_rv_geom_decay_63d_d2": {"inputs": ["close"], "func": f35_rvre_215_midas_rv_geom_decay_63d_d2},
    "f35_rvre_216_midas_rv_exponential_63d_d2": {"inputs": ["close"], "func": f35_rvre_216_midas_rv_exponential_63d_d2},
    "f35_rvre_217_midas_rv_beta_weights_63d_d2": {"inputs": ["close"], "func": f35_rvre_217_midas_rv_beta_weights_63d_d2},
    "f35_rvre_218_midas_rv_linear_decay_63d_d2": {"inputs": ["close"], "func": f35_rvre_218_midas_rv_linear_decay_63d_d2},
    "f35_rvre_219_autocorr_rv21_lag1_252d_d2": {"inputs": ["close"], "func": f35_rvre_219_autocorr_rv21_lag1_252d_d2},
    "f35_rvre_220_autocorr_rv21_lag5_252d_d2": {"inputs": ["close"], "func": f35_rvre_220_autocorr_rv21_lag5_252d_d2},
    "f35_rvre_221_autocorr_rv21_lag21_504d_d2": {"inputs": ["close"], "func": f35_rvre_221_autocorr_rv21_lag21_504d_d2},
    "f35_rvre_222_partial_autocorr_rv21_lag1_252d_d2": {"inputs": ["close"], "func": f35_rvre_222_partial_autocorr_rv21_lag1_252d_d2},
    "f35_rvre_223_har_rv_j_composite_score_252d_d2": {"inputs": ["close"], "func": f35_rvre_223_har_rv_j_composite_score_252d_d2},
    "f35_rvre_224_jump_dominant_high_vol_indicator_252d_d2": {"inputs": ["close"], "func": f35_rvre_224_jump_dominant_high_vol_indicator_252d_d2},
    "f35_rvre_225_vol_regime_severity_composite_252d_d2": {"inputs": ["close"], "func": f35_rvre_225_vol_regime_severity_composite_252d_d2},
}
