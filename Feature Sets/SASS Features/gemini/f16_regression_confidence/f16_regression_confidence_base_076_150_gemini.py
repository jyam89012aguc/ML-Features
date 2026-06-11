# f16_regression_confidence — REAL indicator: rolling linear-regression trend confidence
# Core: rolling OLS of log(closeadj) on a time index over a window.
# This file (076-150) extends the facet set: percentile ranks, regime threshold distances,
#   cross-window R^2 / t-stat spreads, channel breakouts, slope*confidence interactions,
#   residual dispersion, and acceleration variants. All from the same rolling-OLS core.
import numpy as np
import pandas as pd

ANN = 252.0


def _logc(df):
    return np.log(df['closeadj'].replace(0.0, np.nan))


def _ols(y, w):
    """Vectorized rolling OLS of y on a fixed time index t = 0..w-1 (see file 001_075)."""
    n = float(w)
    t = np.arange(w, dtype='float64')
    mt = t.mean()
    var_t = ((t - mt) ** 2).sum() / n
    sxx = ((t - mt) ** 2).sum()

    my = y.rolling(w).mean()
    myy = (y * y).rolling(w).mean()
    var_y = (myy - my * my).clip(lower=0.0)

    ty_mean = y.rolling(w).apply(lambda a: np.dot(t, a) / n, raw=True)
    cov_ty = ty_mean - mt * my

    slope = cov_ty / var_t
    intercept = my - slope * mt

    denom = (var_t * var_y).replace(0.0, np.nan)
    r2 = ((cov_ty * cov_ty) / denom).clip(lower=0.0, upper=1.0)

    sse = (n * var_y * (1.0 - r2)).clip(lower=0.0)
    mse = sse / (n - 2.0)
    se_slope = np.sqrt(mse / sxx)
    tstat = slope / se_slope.replace(0.0, np.nan)

    fitted_last = intercept + slope * (w - 1.0)
    resid_last = y - fitted_last
    resid_std = np.sqrt(mse)

    return {
        'slope': slope, 'intercept': intercept, 'r2': r2, 'sse': sse,
        'se_slope': se_slope, 'tstat': tstat, 'fitted_last': fitted_last,
        'resid_last': resid_last, 'resid_std': resid_std, 'var_y': var_y, 'n': n,
    }


def _z(s, w):
    return (s - s.rolling(w).mean()) / s.rolling(w).std()


def _rank(s, w):
    # rolling percentile rank of the last point within the window (0..1)
    return s.rolling(w).apply(lambda a: (a[-1] >= a).mean(), raw=True)


def _clean(s):
    return s.replace([np.inf, -np.inf], np.nan)


def get_f16_regression_confidence_base_076_150(df):
    y = _logc(df)
    windows = [21, 63, 126, 252]
    reg = {w: _ols(y, w) for w in windows}

    f = {}

    def put(i, series):
        f[f'f16_regression_confidence_{i:03d}'] = _clean(series)

    i = 76
    # --- Percentile rank of R^2 within window --------------------------------
    for w in windows:
        put(i, _rank(reg[w]['r2'], w)); i += 1                     # 76-79
    # --- Percentile rank of slope --------------------------------------------
    for w in windows:
        put(i, _rank(reg[w]['slope'], w)); i += 1                  # 80-83
    # --- Percentile rank of |t-stat| -----------------------------------------
    for w in windows:
        put(i, _rank(reg[w]['tstat'].abs(), w)); i += 1            # 84-87
    # --- R^2 threshold distance: R^2 - 0.5 (regime: trending vs noise) -------
    for w in windows:
        put(i, reg[w]['r2'] - 0.5); i += 1                         # 88-91
    # --- |t-stat| threshold distance vs 1.96 (slope significance) -----------
    for w in windows:
        put(i, reg[w]['tstat'].abs() - 1.96); i += 1              # 92-95
    # --- Cross-window R^2 spread (short - long) ------------------------------
    put(i, reg[21]['r2'] - reg[63]['r2']); i += 1                 # 96
    put(i, reg[21]['r2'] - reg[126]['r2']); i += 1                # 97
    put(i, reg[21]['r2'] - reg[252]['r2']); i += 1                # 98
    put(i, reg[63]['r2'] - reg[126]['r2']); i += 1               # 99
    put(i, reg[63]['r2'] - reg[252]['r2']); i += 1               # 100
    put(i, reg[126]['r2'] - reg[252]['r2']); i += 1              # 101
    # --- Cross-window t-stat spread ------------------------------------------
    put(i, reg[21]['tstat'] - reg[63]['tstat']); i += 1          # 102
    put(i, reg[21]['tstat'] - reg[252]['tstat']); i += 1         # 103
    put(i, reg[63]['tstat'] - reg[252]['tstat']); i += 1         # 104
    # --- Channel breakout flag: |resid| > 2*resid_std ------------------------
    for w in windows:
        rr = reg[w]['resid_last'] / reg[w]['resid_std'].replace(0.0, np.nan)
        put(i, (rr.abs() - 2.0)); i += 1                          # 105-108
    # --- Channel position change (resid z-score Δ) ---------------------------
    for w in windows:
        rr = reg[w]['resid_last'] / reg[w]['resid_std'].replace(0.0, np.nan)
        put(i, rr - rr.shift(1)); i += 1                          # 109-112
    # --- Slope * t-stat (confidence-weighted trend) --------------------------
    for w in windows:
        put(i, reg[w]['slope'] * ANN * np.sign(reg[w]['tstat']) * reg[w]['tstat'].abs().clip(upper=10)); i += 1  # 113-116
    # --- Trend-strength (slope*R^2) percentile rank --------------------------
    for w in windows:
        ts = reg[w]['slope'] * ANN * reg[w]['r2']
        put(i, _rank(ts, w)); i += 1                              # 117-120
    # --- R^2 acceleration: ΔR^2 over window ----------------------------------
    for w in windows:
        put(i, reg[w]['r2'] - reg[w]['r2'].shift(w)); i += 1      # 121-124
    # --- t-stat z-score ------------------------------------------------------
    for w in windows:
        put(i, _z(reg[w]['tstat'], w)); i += 1                    # 125-128
    # --- Residual dispersion: rolling std of resid z-score -------------------
    for w in windows:
        rr = reg[w]['resid_last'] / reg[w]['resid_std'].replace(0.0, np.nan)
        put(i, rr.rolling(w).std()); i += 1                       # 129-132
    # --- Slope CI width relative to |slope| (precision ratio) ----------------
    for w in windows:
        ci = 2.0 * 1.96 * reg[w]['se_slope']
        put(i, ci / reg[w]['slope'].abs().replace(0.0, np.nan)); i += 1  # 133-136
    # --- Signed R^2 (sign of slope * R^2) regime distance --------------------
    for w in windows:
        sr2 = np.sign(reg[w]['slope']) * reg[w]['r2']
        put(i, sr2 - sr2.rolling(w).mean()); i += 1               # 137-140
    # --- Residual mean-reversion: corr(resid, -Δprice) proxy (lag-1 autocorr Δ) ---
    for w in windows:
        r = reg[w]['resid_last']
        put(i, r.rolling(w).corr(r.shift(1)) - 0.0); i += 1       # 141-144
    # --- Short vs long R^2 ratio ---------------------------------------------
    put(i, reg[21]['r2'] / reg[252]['r2'].replace(0.0, np.nan)); i += 1   # 145
    put(i, reg[63]['r2'] / reg[252]['r2'].replace(0.0, np.nan)); i += 1   # 146
    # --- Slope acceleration z-score ------------------------------------------
    put(i, _z((reg[63]['slope'] - reg[63]['slope'].shift(63)), 63)); i += 1   # 147
    put(i, _z((reg[126]['slope'] - reg[126]['slope'].shift(126)), 126)); i += 1  # 148
    # --- Composite trend confidence: R^2 * |t| / CI-width proxy --------------
    put(i, reg[63]['r2'] * reg[63]['tstat'].abs()); i += 1        # 149
    put(i, reg[126]['r2'] * reg[126]['tstat'].abs()); i += 1      # 150

    out = pd.DataFrame(f)
    cols = [f'f16_regression_confidence_{k:03d}' for k in range(76, 151)]
    return out[cols]
