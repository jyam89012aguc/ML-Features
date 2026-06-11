# f16_regression_confidence — REAL indicator: rolling linear-regression trend confidence
# Core: rolling OLS of log(closeadj) on a time index over a window.
# Facets: slope (annualized), R^2 (trend confidence), t-stat, std-error, residual z-score,
#   regression-channel position, slope CI width, trend-strength (slope*R^2), slope acceleration,
#   R^2 regime distance, short-vs-long slope spread, residual autocorrelation.
import numpy as np
import pandas as pd

ANN = 252.0  # trading days per year for slope annualization


def _logc(df):
    # log of adjusted close; windows here are all > 21d so use closeadj
    return np.log(df['closeadj'].replace(0.0, np.nan))


def _ols(y, w):
    """Vectorized rolling OLS of y on a fixed time index t = 0..w-1.

    Returns a dict of rolling Series: slope, intercept, r2, sse, se_slope,
    tstat, fitted_last, resid_last, resid_std, var_y, n.
    All computed via rolling cov/var; t-moments are constants for a fixed window.
    """
    n = float(w)
    t = np.arange(w, dtype='float64')
    mt = t.mean()
    var_t = ((t - mt) ** 2).sum() / n          # population var of index
    sxx = ((t - mt) ** 2).sum()                # sum of squared deviations of t

    my = y.rolling(w).mean()
    myy = (y * y).rolling(w).mean()
    var_y = (myy - my * my).clip(lower=0.0)    # population var of y

    # E[t*y] via weighted rolling sum: sum(t_k * y_{last-w+1+k}) over the window.
    # Convolve y with the index weights using a rolling apply-free dot product.
    # cov(t,y) = mean(t*y) - mean(t)*mean(y)
    ty_mean = y.rolling(w).apply(lambda a: np.dot(t, a) / n, raw=True)
    cov_ty = ty_mean - mt * my

    slope = cov_ty / var_t
    intercept = my - slope * mt

    # R^2 = cov^2 / (var_t * var_y)
    denom = (var_t * var_y).replace(0.0, np.nan)
    r2 = (cov_ty * cov_ty) / denom
    r2 = r2.clip(lower=0.0, upper=1.0)

    # SSE = n*var_y*(1 - R^2);  SE(slope) = sqrt( (SSE/(n-2)) / sxx )
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


def _clean(s):
    return s.replace([np.inf, -np.inf], np.nan)


def get_f16_regression_confidence_base_001_075(df):
    y = _logc(df)
    windows = [21, 63, 126, 252]
    reg = {w: _ols(y, w) for w in windows}

    f = {}

    def put(i, series):
        f[f'f16_regression_confidence_{i:03d}'] = _clean(series)

    i = 1
    # --- Annualized slope (trend) per window ---------------------------------
    for w in windows:
        put(i, reg[w]['slope'] * ANN); i += 1                       # 1-4
    # --- R^2 (trend confidence / fit quality) --------------------------------
    for w in windows:
        put(i, reg[w]['r2']); i += 1                                # 5-8
    # --- t-statistic of slope ------------------------------------------------
    for w in windows:
        put(i, reg[w]['tstat']); i += 1                            # 9-12
    # --- Standard error of slope (annualized) --------------------------------
    for w in windows:
        put(i, reg[w]['se_slope'] * ANN); i += 1                   # 13-16
    # --- Residual z-score: distance from trend line in resid-std units -------
    for w in windows:
        put(i, reg[w]['resid_last'] / reg[w]['resid_std'].replace(0.0, np.nan)); i += 1  # 17-20
    # --- Regression-channel position: resid scaled by +/-2 sigma channel -----
    for w in windows:
        put(i, reg[w]['resid_last'] / (2.0 * reg[w]['resid_std'].replace(0.0, np.nan))); i += 1  # 21-24
    # --- Slope 95% CI width (annualized): 2 * 1.96 * SE ----------------------
    for w in windows:
        put(i, 2.0 * 1.96 * reg[w]['se_slope'] * ANN); i += 1      # 25-28
    # --- Trend-strength: slope (ann) * R^2 -----------------------------------
    for w in windows:
        put(i, reg[w]['slope'] * ANN * reg[w]['r2']); i += 1       # 29-32
    # --- Slope acceleration: slope of the slope over the window --------------
    for w in windows:
        put(i, (reg[w]['slope'] - reg[w]['slope'].shift(w)) * ANN); i += 1  # 33-36
    # --- R^2 regime distance: current R^2 minus its rolling median -----------
    for w in windows:
        put(i, reg[w]['r2'] - reg[w]['r2'].rolling(w).median()); i += 1     # 37-40
    # --- Short-vs-long annualized slope spread -------------------------------
    put(i, (reg[21]['slope'] - reg[63]['slope']) * ANN); i += 1   # 41
    put(i, (reg[21]['slope'] - reg[126]['slope']) * ANN); i += 1  # 42
    put(i, (reg[21]['slope'] - reg[252]['slope']) * ANN); i += 1  # 43
    put(i, (reg[63]['slope'] - reg[126]['slope']) * ANN); i += 1  # 44
    put(i, (reg[63]['slope'] - reg[252]['slope']) * ANN); i += 1  # 45
    put(i, (reg[126]['slope'] - reg[252]['slope']) * ANN); i += 1 # 46
    # --- Residual autocorrelation lag-1 of resid_last over window -----------
    for w in windows:
        r = reg[w]['resid_last']
        ac = r.rolling(w).corr(r.shift(1))
        put(i, ac); i += 1                                         # 47-50
    # --- z-score of slope (slope relative to its own rolling history) --------
    for w in windows:
        put(i, _z(reg[w]['slope'], w)); i += 1                     # 51-54
    # --- z-score of R^2 ------------------------------------------------------
    for w in windows:
        put(i, _z(reg[w]['r2'], w)); i += 1                        # 55-58
    # --- t-stat regime distance (vs rolling median) --------------------------
    for w in windows:
        put(i, reg[w]['tstat'] - reg[w]['tstat'].rolling(w).median()); i += 1  # 59-62
    # --- Trend-strength z-score ----------------------------------------------
    for w in windows:
        ts = reg[w]['slope'] * ANN * reg[w]['r2']
        put(i, _z(ts, w)); i += 1                                  # 63-66
    # --- Residual-std (channel width) annualized-ish, level ------------------
    for w in windows:
        put(i, reg[w]['resid_std']); i += 1                        # 67-70
    # --- Residual-std slope (channel widening/narrowing) ---------------------
    for w in windows:
        put(i, reg[w]['resid_std'] - reg[w]['resid_std'].shift(w)); i += 1  # 71-74
    # --- Signed trend confidence: sign(slope)*R^2 ----------------------------
    put(i, np.sign(reg[63]['slope']) * reg[63]['r2']); i += 1      # 75

    out = pd.DataFrame(f)
    cols = [f'f16_regression_confidence_{k:03d}' for k in range(1, 76)]
    return out[cols]
