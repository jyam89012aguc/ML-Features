import inspect
import numpy as np
import pandas as pd

TRADING_DAYS_YEAR = 252
TRADING_DAYS_TWOYEAR = 504
TRADING_DAYS_HALF = 126
TRADING_DAYS_QUARTER = 63
TRADING_DAYS_MONTH = 21
TRADING_DAYS_WEEK = 5


# ===== generic helpers =====
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


def _rmax(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).max()


def _rmin(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).min()


def _rank(s, w):
    return s.rolling(w, min_periods=max(2, w // 2)).rank(pct=True) - 0.5


# ===== family ownership-mix primitives (sf3a holder-type composition, concentration, put/call skew) =====
def _f51_share(num, den):
    # composition share of one holder-type value within the aggregate
    return num / den.replace(0, np.nan)


def _f51_herf(a, b, c):
    # Herfindahl concentration across three value shares (sum of squared shares)
    tot = (a + b + c).replace(0, np.nan)
    sa = a / tot
    sb = b / tot
    sc = c / tot
    return sa * sa + sb * sb + sc * sc


def _f51_skew(put, cll):
    # put-vs-call holder/value skew: bearish/hedge proxy in [0,1]
    return put / (put + cll).replace(0, np.nan)


def _f51_growth(s, w):
    # log growth of an ownership level over w days
    return np.log(s.replace(0, np.nan) / s.shift(w).replace(0, np.nan))


def _f51_roc(s, w):
    # simple rate-of-change of an ownership level
    return s / s.shift(w).replace(0, np.nan) - 1.0


def _f51_logratio(a, b):
    # log of breadth/value ratio between two holder pools
    return np.log(a.replace(0, np.nan) / b.replace(0, np.nan))


# ============================================================
# --- institutional (fund) value share of total ownership: level ---
def f51om_f51_ownership_mix_concentration_fndshare_lvl_base_v001_signal(fndvalue, totalvalue):
    b = _f51_share(fndvalue, totalvalue)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fund value share, smoothed over a quarter (persistent institutional tilt)
def f51om_f51_ownership_mix_concentration_fndshare_sm63_base_v002_signal(fndvalue, totalvalue):
    s = _f51_share(fndvalue, totalvalue)
    b = s.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fund value share, z-scored vs its own 252d history (de-trended composition)
def f51om_f51_ownership_mix_concentration_fndshare_z252_base_v003_signal(fndvalue, totalvalue):
    s = _f51_share(fndvalue, totalvalue)
    b = _z(s, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fund value share trajectory: change over a quarter (institutional rotation in)
def f51om_f51_ownership_mix_concentration_fndshare_chg63_base_v004_signal(fndvalue, totalvalue):
    s = _f51_share(fndvalue, totalvalue)
    b = s - s.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fund value share trajectory: change over a year (slow institutional drift)
def f51om_f51_ownership_mix_concentration_fndshare_chg252_base_v005_signal(fndvalue, totalvalue):
    s = _f51_share(fndvalue, totalvalue)
    b = s - s.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- retail/other (undisclosed) value share of total: level ---
def f51om_f51_ownership_mix_concentration_undshare_lvl_base_v006_signal(undvalue, totalvalue):
    b = _f51_share(undvalue, totalvalue)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# retail/other share, percentile-ranked vs its own 252d history
def f51om_f51_ownership_mix_concentration_undshare_rank252_base_v007_signal(undvalue, totalvalue):
    s = _f51_share(undvalue, totalvalue)
    b = _rank(s, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# retail/other share momentum: change over a quarter (retail crowding proxy)
def f51om_f51_ownership_mix_concentration_undshare_chg63_base_v008_signal(undvalue, totalvalue):
    s = _f51_share(undvalue, totalvalue)
    b = s - s.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# retail/other value-share z-scored vs its own 252d history (de-trended retail crowding extremity)
def f51om_f51_ownership_mix_concentration_fndund_logr_base_v009_signal(undvalue, totalvalue):
    s = _f51_share(undvalue, totalvalue)
    b = _z(s, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# institutional-vs-retail tilt momentum: change in log ratio over a quarter
def f51om_f51_ownership_mix_concentration_fndund_logrchg63_base_v010_signal(fndvalue, undvalue):
    r = _f51_logratio(fndvalue, undvalue)
    b = r - r.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# institutional-vs-retail tilt, z-scored vs 126d (de-trended rotation)
def f51om_f51_ownership_mix_concentration_fndund_logrz126_base_v011_signal(fndvalue, undvalue):
    r = _f51_logratio(fndvalue, undvalue)
    b = _z(r, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- holder-type value concentration: Herfindahl across fnd/und residual-prf shares ---
# imbalance of the non-fund pool: |und - prf| value normalized by their sum (residual tilt)
def f51om_f51_ownership_mix_concentration_herf_lvl_base_v012_signal(fndvalue, undvalue, totalvalue):
    prf = (totalvalue - fndvalue - undvalue).clip(lower=0)
    b = (undvalue - prf).abs() / (undvalue + prf).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# holder-COUNT concentration (count-Herfindahl), smoothed over a quarter (breadth concentration)
def f51om_f51_ownership_mix_concentration_herf_sm63_base_v013_signal(fndholders, undholders, prfholders):
    h = _f51_herf(fndholders, undholders, prfholders)
    b = h.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# value-concentration consolidation: change over a year in non-fund-pool imbalance (und vs prf)
def f51om_f51_ownership_mix_concentration_herf_chg252_base_v014_signal(fndvalue, undvalue, totalvalue):
    prf = (totalvalue - fndvalue - undvalue).clip(lower=0)
    imb = (undvalue - prf).abs() / (undvalue + prf).replace(0, np.nan)
    b = imb - imb.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# holder-COUNT concentration z-scored vs 252d history (breadth concentration extremity)
def f51om_f51_ownership_mix_concentration_herf_z252_base_v015_signal(fndholders, undholders, prfholders):
    h = _f51_herf(fndholders, undholders, prfholders)
    b = _z(h, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# value-vs-count effective-N ratio: how much more concentrated value is than breadth
def f51om_f51_ownership_mix_concentration_effn_lvl_base_v016_signal(fndvalue, undvalue, totalvalue, fndholders, undholders, prfholders):
    prf = (totalvalue - fndvalue - undvalue).clip(lower=0)
    hv = _f51_herf(fndvalue, undvalue, prf)
    hc = _f51_herf(fndholders, undholders, prfholders)
    effv = 1.0 / hv.replace(0, np.nan)
    effc = 1.0 / hc.replace(0, np.nan)
    b = effv / effc.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- holder-count concentration ---
# non-fund breadth imbalance: |und - prf| holder counts normalized by their sum (residual breadth tilt)
def f51om_f51_ownership_mix_concentration_herfcnt_lvl_base_v017_signal(undholders, prfholders):
    b = (undholders - prfholders).abs() / (undholders + prfholders).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# non-fund breadth-imbalance momentum: QoQ change in |und - prf| count tilt
def f51om_f51_ownership_mix_concentration_herfcnt_chg63_base_v018_signal(undholders, prfholders):
    imb = (undholders - prfholders).abs() / (undholders + prfholders).replace(0, np.nan)
    b = imb - imb.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# holder-COUNT concentration change over a year (breadth consolidation trend)
def f51om_f51_ownership_mix_concentration_herfgap_base_v019_signal(fndholders, undholders, prfholders):
    h = _f51_herf(fndholders, undholders, prfholders)
    b = h - h.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- fund-holder count breadth (accumulation breadth, distinct from f45 inst-count level) ---
# fund-holder count as a fraction of total holder breadth (institutional breadth share)
def f51om_f51_ownership_mix_concentration_fndcntshare_lvl_base_v020_signal(fndholders, undholders, prfholders):
    tot = (fndholders + undholders + prfholders).replace(0, np.nan)
    b = fndholders / tot
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fund-holder breadth share momentum over a quarter
def f51om_f51_ownership_mix_concentration_fndcntshare_chg63_base_v021_signal(fndholders, undholders, prfholders):
    tot = (fndholders + undholders + prfholders).replace(0, np.nan)
    s = fndholders / tot
    b = s - s.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fund-holder count QoQ change (accumulation breadth, raw rate-of-change)
def f51om_f51_ownership_mix_concentration_fndcnt_roc63_base_v022_signal(fndholders):
    b = _f51_roc(fndholders, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fund-holder count YoY log growth (breadth accumulation over a year)
def f51om_f51_ownership_mix_concentration_fndcnt_grow252_base_v023_signal(fndholders):
    b = _f51_growth(fndholders, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fund-holder breadth vs retail breadth: log ratio of holder counts
def f51om_f51_ownership_mix_concentration_fndundcnt_logr_base_v024_signal(fndholders, undholders):
    b = _f51_logratio(fndholders, undholders)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fund-holder breadth vs retail breadth momentum over a quarter
def f51om_f51_ownership_mix_concentration_fndundcnt_logrchg63_base_v025_signal(fndholders, undholders):
    r = _f51_logratio(fndholders, undholders)
    b = r - r.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# average fund position size: fund value per fund holder (smart-money ticket size)
def f51om_f51_ownership_mix_concentration_fndticket_lvl_base_v026_signal(fndvalue, fndholders):
    b = fndvalue / fndholders.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fund ticket-size momentum: log growth over a quarter (position deepening)
def f51om_f51_ownership_mix_concentration_fndticket_grow63_base_v027_signal(fndvalue, fndholders):
    t = fndvalue / fndholders.replace(0, np.nan)
    b = _f51_growth(t, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fund ticket vs retail ticket: who writes bigger checks (log ratio of avg position)
def f51om_f51_ownership_mix_concentration_ticketspread_base_v028_signal(fndvalue, fndholders, undvalue, undholders):
    tf = fndvalue / fndholders.replace(0, np.nan)
    tu = undvalue / undholders.replace(0, np.nan)
    b = _f51_logratio(tf, tu)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- put-vs-call holder skew (bearish/hedge proxy) ---
# put share of options value: putvalue/(putvalue+cllvalue)
def f51om_f51_ownership_mix_concentration_putskew_lvl_base_v029_signal(putvalue, cllvalue):
    b = _f51_skew(putvalue, cllvalue)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# put-value skew, smoothed over a quarter (persistent hedging tilt)
def f51om_f51_ownership_mix_concentration_putskew_sm63_base_v030_signal(putvalue, cllvalue):
    s = _f51_skew(putvalue, cllvalue)
    b = s.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# put-value skew z-scored vs 252d (de-trended bearish positioning)
def f51om_f51_ownership_mix_concentration_putskew_z252_base_v031_signal(putvalue, cllvalue):
    s = _f51_skew(putvalue, cllvalue)
    b = _z(s, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# put-value skew momentum: change over a quarter (hedging build-up)
def f51om_f51_ownership_mix_concentration_putskew_chg63_base_v032_signal(putvalue, cllvalue):
    s = _f51_skew(putvalue, cllvalue)
    b = s - s.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# put-vs-call HOLDER skew: putholders/(putholders+cllholders) (bearish breadth)
def f51om_f51_ownership_mix_concentration_putcntskew_lvl_base_v033_signal(putholders, cllholders):
    b = _f51_skew(putholders, cllholders)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# put-holder skew momentum over a quarter
def f51om_f51_ownership_mix_concentration_putcntskew_chg63_base_v034_signal(putholders, cllholders):
    s = _f51_skew(putholders, cllholders)
    b = s - s.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# value-skew vs holder-skew gap: are big puts concentrated in few hands?
def f51om_f51_ownership_mix_concentration_putskewgap_base_v035_signal(putvalue, cllvalue, putholders, cllholders):
    sv = _f51_skew(putvalue, cllvalue)
    sc = _f51_skew(putholders, cllholders)
    b = sv - sc
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# average put ticket size growth over a quarter (deepening hedge conviction per holder)
def f51om_f51_ownership_mix_concentration_putcallticket_base_v036_signal(putvalue, putholders):
    tp = putvalue / putholders.replace(0, np.nan)
    b = _f51_growth(tp, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- options-holder breadth vs equity-holder breadth ---
# options breadth = (put+call holders) relative to equity (shr) holder breadth
def f51om_f51_ownership_mix_concentration_optbreadth_lvl_base_v037_signal(putholders, cllholders, shrholders):
    opt = putholders + cllholders
    b = opt / shrholders.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# options-vs-equity breadth momentum over a quarter (derivatives interest building)
def f51om_f51_ownership_mix_concentration_optbreadth_chg63_base_v038_signal(putholders, cllholders, shrholders):
    opt = putholders + cllholders
    r = opt / shrholders.replace(0, np.nan)
    b = r - r.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# options-vs-equity breadth z-scored vs 252d
def f51om_f51_ownership_mix_concentration_optbreadth_z252_base_v039_signal(putholders, cllholders, shrholders):
    opt = putholders + cllholders
    r = opt / shrholders.replace(0, np.nan)
    b = _z(r, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# call-holder breadth relative to equity holders (bullish derivatives breadth)
def f51om_f51_ownership_mix_concentration_callbreadth_lvl_base_v040_signal(cllholders, shrholders):
    b = cllholders / shrholders.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# put-holder breadth relative to equity holders, z-scored vs 252d (de-trended hedging breadth)
def f51om_f51_ownership_mix_concentration_putbreadth_lvl_base_v041_signal(putholders, shrholders):
    r = putholders / shrholders.replace(0, np.nan)
    b = _z(r, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- percentoftotal trajectory ---
# percentoftotal level smoothed (this ticker's share of an investor's portfolio aggregate)
def f51om_f51_ownership_mix_concentration_pot_sm63_base_v042_signal(percentoftotal):
    b = percentoftotal.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# percentoftotal momentum: change over a quarter (conviction-weighting trajectory)
def f51om_f51_ownership_mix_concentration_pot_chg63_base_v043_signal(percentoftotal):
    b = percentoftotal - percentoftotal.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# percentoftotal z-scored vs 252d (de-trended portfolio weighting)
def f51om_f51_ownership_mix_concentration_pot_z252_base_v044_signal(percentoftotal):
    b = _z(percentoftotal, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# percentoftotal percentile-rank vs 504d history
def f51om_f51_ownership_mix_concentration_pot_rank504_base_v045_signal(percentoftotal):
    b = _rank(percentoftotal, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# percentoftotal YoY log growth (slow conviction accumulation)
def f51om_f51_ownership_mix_concentration_pot_grow252_base_v046_signal(percentoftotal):
    b = _f51_growth(percentoftotal, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# conviction interaction: percentoftotal x fund value share (institutional conviction weight)
def f51om_f51_ownership_mix_concentration_potfnd_inter_base_v047_signal(percentoftotal, fndvalue, totalvalue):
    s = _f51_share(fndvalue, totalvalue)
    b = percentoftotal * s
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- holder-type rotation (composite drift across types) ---
# rotation magnitude: combined absolute QoQ change of fnd & und value shares
def f51om_f51_ownership_mix_concentration_rotmag_base_v048_signal(fndvalue, undvalue, totalvalue):
    sf = _f51_share(fndvalue, totalvalue)
    su = _f51_share(undvalue, totalvalue)
    b = (sf - sf.shift(63)).abs() + (su - su.shift(63)).abs()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net rotation balance: (fund-share gain minus retail-share gain) normalized by total absolute rotation
def f51om_f51_ownership_mix_concentration_netrot_base_v049_signal(fndvalue, undvalue, totalvalue):
    sf = _f51_share(fndvalue, totalvalue)
    su = _f51_share(undvalue, totalvalue)
    df = sf - sf.shift(63)
    du = su - su.shift(63)
    b = (df - du) / (df.abs() + du.abs()).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# rotation persistence: sign-agreement of fund-share change over 63d vs 126d
def f51om_f51_ownership_mix_concentration_rotpersist_base_v050_signal(fndvalue, totalvalue):
    sf = _f51_share(fndvalue, totalvalue)
    c1 = sf - sf.shift(63)
    c2 = sf - sf.shift(126)
    b = np.sign(c1) * np.sign(c2) * (c1.abs() + c2.abs())
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- additional composition / concentration facets ---
# fund value share dispersion (instability of institutional tilt) over 126d
def f51om_f51_ownership_mix_concentration_fndshare_disp126_base_v051_signal(fndvalue, totalvalue):
    s = _f51_share(fndvalue, totalvalue)
    b = _std(s, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# put-skew dispersion (volatility of hedging tilt) over 126d
def f51om_f51_ownership_mix_concentration_putskew_disp126_base_v052_signal(putvalue, cllvalue):
    s = _f51_skew(putvalue, cllvalue)
    b = _std(s, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# concentration regime distance: Herfindahl minus its own 252d median band
def f51om_f51_ownership_mix_concentration_herf_regdist_base_v053_signal(fndvalue, undvalue, totalvalue):
    prf = (totalvalue - fndvalue - undvalue).clip(lower=0)
    h = _f51_herf(fndvalue, undvalue, prf)
    med = h.rolling(252, min_periods=63).median()
    b = h - med
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fund-share extension above its 252d max band (new institutional dominance)
def f51om_f51_ownership_mix_concentration_fndshare_ext_base_v054_signal(fndvalue, totalvalue):
    s = _f51_share(fndvalue, totalvalue)
    hi = _rmax(s, 252)
    b = s / hi.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# put-skew extension above 252d max (hedging spike vs own history)
def f51om_f51_ownership_mix_concentration_putskew_ext_base_v055_signal(putvalue, cllvalue):
    s = _f51_skew(putvalue, cllvalue)
    hi = _rmax(s, 252)
    b = s / hi.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# institutional-share streak: fraction of last year fund-share rose QoQ
def f51om_f51_ownership_mix_concentration_fndshare_streak_base_v056_signal(fndvalue, totalvalue):
    s = _f51_share(fndvalue, totalvalue)
    up = (s > s.shift(21)).astype(float)
    b = up.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# put-skew regime: fraction of last year put-skew sat above its own 252d median (bearish persistence)
def f51om_f51_ownership_mix_concentration_putregime_base_v057_signal(putvalue, cllvalue):
    s = _f51_skew(putvalue, cllvalue)
    med = s.rolling(252, min_periods=63).median()
    bear = (s > med).astype(float)
    b = bear.rolling(126, min_periods=42).mean() * (s - med)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# options-tilt: net call-vs-put value as a share of total ownership value (sentiment scale)
def f51om_f51_ownership_mix_concentration_optnetshare_base_v058_signal(cllvalue, putvalue, totalvalue):
    b = (cllvalue - putvalue) / totalvalue.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# options value footprint: (call+put value) as a share of total ownership value
def f51om_f51_ownership_mix_concentration_optfootprint_base_v059_signal(cllvalue, putvalue, totalvalue):
    b = (cllvalue + putvalue) / totalvalue.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# options footprint momentum over a quarter (derivatives value building vs equity)
def f51om_f51_ownership_mix_concentration_optfootprint_chg63_base_v060_signal(cllvalue, putvalue, totalvalue):
    r = (cllvalue + putvalue) / totalvalue.replace(0, np.nan)
    b = r - r.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# prf (residual/other) value share level — non-fund non-retail pool
def f51om_f51_ownership_mix_concentration_prfshare_lvl_base_v061_signal(fndvalue, undvalue, totalvalue):
    prf = (totalvalue - fndvalue - undvalue).clip(lower=0)
    b = prf / totalvalue.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# prf-holder breadth share momentum: YoY change in prf fraction of total holder count
def f51om_f51_ownership_mix_concentration_prfcntshare_base_v062_signal(fndholders, undholders, prfholders):
    tot = (fndholders + undholders + prfholders).replace(0, np.nan)
    s = prfholders / tot
    b = s - s.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fund per-holder heaviness MOMENTUM: QoQ change in (fund value share / fund count share)
def f51om_f51_ownership_mix_concentration_fndheavy_base_v063_signal(fndvalue, totalvalue, fndholders, undholders, prfholders):
    vs = _f51_share(fndvalue, totalvalue)
    cs = fndholders / (fndholders + undholders + prfholders).replace(0, np.nan)
    heavy = vs / cs.replace(0, np.nan)
    b = heavy - heavy.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# retail per-holder heaviness: und value share divided by und count share
def f51om_f51_ownership_mix_concentration_undheavy_base_v064_signal(undvalue, totalvalue, fndholders, undholders, prfholders):
    vs = _f51_share(undvalue, totalvalue)
    cs = undholders / (fndholders + undholders + prfholders).replace(0, np.nan)
    b = vs / cs.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# non-fund (retail+other) holder breadth log growth over a quarter (retail broadening)
def f51om_f51_ownership_mix_concentration_totbreadth_grow63_base_v065_signal(undholders, prfholders):
    nonfund = undholders + prfholders
    b = _f51_growth(nonfund, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# shrholders (13F equity holder) breadth growth vs fund-holder growth (who is adding)
def f51om_f51_ownership_mix_concentration_shrfnd_growspread_base_v066_signal(shrholders, fndholders):
    gs = _f51_growth(shrholders, 63)
    gf = _f51_growth(fndholders, 63)
    b = gs - gf
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# co-movement of institutional tilt and hedging: product of fund-share QoQ change and put-skew QoQ change
def f51om_f51_ownership_mix_concentration_fndputinter_base_v067_signal(fndvalue, totalvalue, putvalue, cllvalue):
    fs = _f51_share(fndvalue, totalvalue)
    ps = _f51_skew(putvalue, cllvalue)
    dfs = fs - fs.shift(63)
    dps = ps - ps.shift(63)
    b = np.sign(dfs * dps) * (dfs.abs() + dps.abs())
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# composition entropy: Shannon entropy across fnd/und/prf HOLDER-COUNT shares (breadth diversity)
def f51om_f51_ownership_mix_concentration_entropy_base_v068_signal(fndholders, undholders, prfholders):
    tot = (fndholders + undholders + prfholders).replace(0, np.nan)
    sa = (fndholders / tot).clip(lower=1e-9)
    sb = (undholders / tot).clip(lower=1e-9)
    sc = (prfholders / tot).clip(lower=1e-9)
    b = -(sa * np.log(sa) + sb * np.log(sb) + sc * np.log(sc))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# composition entropy momentum over a year: VALUE-share entropy change minus COUNT-share entropy change
def f51om_f51_ownership_mix_concentration_entropy_chg252_base_v069_signal(fndvalue, undvalue, totalvalue, fndholders, undholders, prfholders):
    prf = (totalvalue - fndvalue - undvalue).clip(lower=0)
    tv = (fndvalue + undvalue + prf).replace(0, np.nan)
    va = (fndvalue / tv).clip(lower=1e-9)
    vb = (undvalue / tv).clip(lower=1e-9)
    vc = (prf / tv).clip(lower=1e-9)
    ev = -(va * np.log(va) + vb * np.log(vb) + vc * np.log(vc))
    tc = (fndholders + undholders + prfholders).replace(0, np.nan)
    ca = (fndholders / tc).clip(lower=1e-9)
    cb = (undholders / tc).clip(lower=1e-9)
    cc = (prfholders / tc).clip(lower=1e-9)
    ec = -(ca * np.log(ca) + cb * np.log(cb) + cc * np.log(cc))
    diff = ev - ec
    b = diff - diff.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dominant-type breadth gap: largest minus second-largest HOLDER-COUNT share (breadth leadership)
def f51om_f51_ownership_mix_concentration_domgap_base_v070_signal(fndholders, undholders, prfholders):
    tot = (fndholders + undholders + prfholders).replace(0, np.nan)
    stacked = pd.concat([fndholders / tot, undholders / tot, prfholders / tot], axis=1)
    srt = pd.DataFrame(np.sort(stacked.values, axis=1), index=stacked.index)
    b = srt.iloc[:, 2] - srt.iloc[:, 1]
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# put-skew acceleration vs fund-share (divergence: hedging up while institutions leave)
def f51om_f51_ownership_mix_concentration_diverge_base_v071_signal(putvalue, cllvalue, fndvalue, totalvalue):
    ps = _f51_skew(putvalue, cllvalue)
    fs = _f51_share(fndvalue, totalvalue)
    b = (ps - ps.shift(63)) - (fs - fs.shift(63))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# options value-vs-breadth gap: options value share of total minus options holder share of total
def f51om_f51_ownership_mix_concentration_optfrac_base_v072_signal(cllvalue, putvalue, totalvalue, cllholders, putholders, shrholders):
    vshare = (cllvalue + putvalue) / totalvalue.replace(0, np.nan)
    cshare = (cllholders + putholders) / (cllholders + putholders + shrholders).replace(0, np.nan)
    b = vshare - cshare
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fund-share mean-reversion: current share minus its slow EMA (composition displacement)
def f51om_f51_ownership_mix_concentration_fndshare_disp_base_v073_signal(fndvalue, totalvalue):
    s = _f51_share(fndvalue, totalvalue)
    b = s - s.ewm(span=126, min_periods=42).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# put-skew mean-reversion: current skew minus its slow EMA (hedging displacement)
def f51om_f51_ownership_mix_concentration_putskew_disp_base_v074_signal(putvalue, cllvalue):
    s = _f51_skew(putvalue, cllvalue)
    b = s - s.ewm(span=126, min_periods=42).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# composite ownership-quality: fund-share x (1 - put-skew) x percentoftotal trajectory
def f51om_f51_ownership_mix_concentration_quality_base_v075_signal(fndvalue, totalvalue, putvalue, cllvalue, percentoftotal):
    fs = _f51_share(fndvalue, totalvalue)
    ps = _f51_skew(putvalue, cllvalue)
    potz = _z(percentoftotal, 126)
    b = fs * (1.0 - ps) + 0.25 * potz
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f51om_f51_ownership_mix_concentration_fndshare_lvl_base_v001_signal,
    f51om_f51_ownership_mix_concentration_fndshare_sm63_base_v002_signal,
    f51om_f51_ownership_mix_concentration_fndshare_z252_base_v003_signal,
    f51om_f51_ownership_mix_concentration_fndshare_chg63_base_v004_signal,
    f51om_f51_ownership_mix_concentration_fndshare_chg252_base_v005_signal,
    f51om_f51_ownership_mix_concentration_undshare_lvl_base_v006_signal,
    f51om_f51_ownership_mix_concentration_undshare_rank252_base_v007_signal,
    f51om_f51_ownership_mix_concentration_undshare_chg63_base_v008_signal,
    f51om_f51_ownership_mix_concentration_fndund_logr_base_v009_signal,
    f51om_f51_ownership_mix_concentration_fndund_logrchg63_base_v010_signal,
    f51om_f51_ownership_mix_concentration_fndund_logrz126_base_v011_signal,
    f51om_f51_ownership_mix_concentration_herf_lvl_base_v012_signal,
    f51om_f51_ownership_mix_concentration_herf_sm63_base_v013_signal,
    f51om_f51_ownership_mix_concentration_herf_chg252_base_v014_signal,
    f51om_f51_ownership_mix_concentration_herf_z252_base_v015_signal,
    f51om_f51_ownership_mix_concentration_effn_lvl_base_v016_signal,
    f51om_f51_ownership_mix_concentration_herfcnt_lvl_base_v017_signal,
    f51om_f51_ownership_mix_concentration_herfcnt_chg63_base_v018_signal,
    f51om_f51_ownership_mix_concentration_herfgap_base_v019_signal,
    f51om_f51_ownership_mix_concentration_fndcntshare_lvl_base_v020_signal,
    f51om_f51_ownership_mix_concentration_fndcntshare_chg63_base_v021_signal,
    f51om_f51_ownership_mix_concentration_fndcnt_roc63_base_v022_signal,
    f51om_f51_ownership_mix_concentration_fndcnt_grow252_base_v023_signal,
    f51om_f51_ownership_mix_concentration_fndundcnt_logr_base_v024_signal,
    f51om_f51_ownership_mix_concentration_fndundcnt_logrchg63_base_v025_signal,
    f51om_f51_ownership_mix_concentration_fndticket_lvl_base_v026_signal,
    f51om_f51_ownership_mix_concentration_fndticket_grow63_base_v027_signal,
    f51om_f51_ownership_mix_concentration_ticketspread_base_v028_signal,
    f51om_f51_ownership_mix_concentration_putskew_lvl_base_v029_signal,
    f51om_f51_ownership_mix_concentration_putskew_sm63_base_v030_signal,
    f51om_f51_ownership_mix_concentration_putskew_z252_base_v031_signal,
    f51om_f51_ownership_mix_concentration_putskew_chg63_base_v032_signal,
    f51om_f51_ownership_mix_concentration_putcntskew_lvl_base_v033_signal,
    f51om_f51_ownership_mix_concentration_putcntskew_chg63_base_v034_signal,
    f51om_f51_ownership_mix_concentration_putskewgap_base_v035_signal,
    f51om_f51_ownership_mix_concentration_putcallticket_base_v036_signal,
    f51om_f51_ownership_mix_concentration_optbreadth_lvl_base_v037_signal,
    f51om_f51_ownership_mix_concentration_optbreadth_chg63_base_v038_signal,
    f51om_f51_ownership_mix_concentration_optbreadth_z252_base_v039_signal,
    f51om_f51_ownership_mix_concentration_callbreadth_lvl_base_v040_signal,
    f51om_f51_ownership_mix_concentration_putbreadth_lvl_base_v041_signal,
    f51om_f51_ownership_mix_concentration_pot_sm63_base_v042_signal,
    f51om_f51_ownership_mix_concentration_pot_chg63_base_v043_signal,
    f51om_f51_ownership_mix_concentration_pot_z252_base_v044_signal,
    f51om_f51_ownership_mix_concentration_pot_rank504_base_v045_signal,
    f51om_f51_ownership_mix_concentration_pot_grow252_base_v046_signal,
    f51om_f51_ownership_mix_concentration_potfnd_inter_base_v047_signal,
    f51om_f51_ownership_mix_concentration_rotmag_base_v048_signal,
    f51om_f51_ownership_mix_concentration_netrot_base_v049_signal,
    f51om_f51_ownership_mix_concentration_rotpersist_base_v050_signal,
    f51om_f51_ownership_mix_concentration_fndshare_disp126_base_v051_signal,
    f51om_f51_ownership_mix_concentration_putskew_disp126_base_v052_signal,
    f51om_f51_ownership_mix_concentration_herf_regdist_base_v053_signal,
    f51om_f51_ownership_mix_concentration_fndshare_ext_base_v054_signal,
    f51om_f51_ownership_mix_concentration_putskew_ext_base_v055_signal,
    f51om_f51_ownership_mix_concentration_fndshare_streak_base_v056_signal,
    f51om_f51_ownership_mix_concentration_putregime_base_v057_signal,
    f51om_f51_ownership_mix_concentration_optnetshare_base_v058_signal,
    f51om_f51_ownership_mix_concentration_optfootprint_base_v059_signal,
    f51om_f51_ownership_mix_concentration_optfootprint_chg63_base_v060_signal,
    f51om_f51_ownership_mix_concentration_prfshare_lvl_base_v061_signal,
    f51om_f51_ownership_mix_concentration_prfcntshare_base_v062_signal,
    f51om_f51_ownership_mix_concentration_fndheavy_base_v063_signal,
    f51om_f51_ownership_mix_concentration_undheavy_base_v064_signal,
    f51om_f51_ownership_mix_concentration_totbreadth_grow63_base_v065_signal,
    f51om_f51_ownership_mix_concentration_shrfnd_growspread_base_v066_signal,
    f51om_f51_ownership_mix_concentration_fndputinter_base_v067_signal,
    f51om_f51_ownership_mix_concentration_entropy_base_v068_signal,
    f51om_f51_ownership_mix_concentration_entropy_chg252_base_v069_signal,
    f51om_f51_ownership_mix_concentration_domgap_base_v070_signal,
    f51om_f51_ownership_mix_concentration_diverge_base_v071_signal,
    f51om_f51_ownership_mix_concentration_optfrac_base_v072_signal,
    f51om_f51_ownership_mix_concentration_fndshare_disp_base_v073_signal,
    f51om_f51_ownership_mix_concentration_putskew_disp_base_v074_signal,
    f51om_f51_ownership_mix_concentration_quality_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F51_OWNERSHIP_MIX_CONCENTRATION_REGISTRY_001_075 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500

    ALLOW = {
        "open", "high", "low", "close", "closeadj", "volume",
        "revenue", "revenueusd", "deferredrev", "gp", "grossmargin", "opinc", "opex",
        "sgna", "cor", "rnd", "sbcomp", "ebit", "ebitda", "ebitdamargin", "netinc",
        "netinccmn", "netmargin", "eps", "epsdil", "fcf", "fcfps", "ncfo", "ncff",
        "ncfi", "ncfcommon", "ncfdebt", "ncfbus", "capex", "depamor", "sharesbas",
        "shareswa", "shareswadil", "assets", "assetsc", "tangibles", "intangibles",
        "ppnenet", "investments", "inventory", "receivables", "payables", "equity",
        "retearn", "workingcapital", "debt", "debtc", "debtnc", "liabilities",
        "liabilitiesc", "cashneq", "currentratio", "roic", "roe", "roa", "ros",
        "assetturnover", "invcap", "intexp", "taxexp", "ebt", "sps", "bvps", "tbvps",
        "de", "ncfdiv", "ncfinv", "dps", "divyield", "payoutratio", "prefdivis",
        "netincdis", "marketcap", "ev", "evebit", "evebitda", "pe", "pb", "ps",
        "shrholders", "shrvalue", "shrunits", "totalvalue", "percentoftotal",
        "fndholders", "undholders", "prfholders", "dbtholders", "putholders",
        "putvalue", "cllholders", "cllvalue", "wntholders", "wntvalue", "dbtvalue",
        "fndvalue", "undvalue", "prfvalue", "fndunits", "undunits",
    }

    def _fund(seed, base=1e8, drift=0.03, vol=0.07, allow_neg=False):
        g = np.random.default_rng(seed)
        steps = np.repeat(g.normal(drift, vol, n // 63 + 1), 63)[:n]
        s = base * np.exp(np.cumsum(steps / 63))
        if allow_neg:
            s = s - base * 0.6
        return pd.Series(s, name=None)

    # ownership columns: all positive; build totalvalue as a superset of the components
    fndvalue = _fund(201, base=5.0e8, drift=0.05, vol=0.10).rename("fndvalue")
    undvalue = _fund(202, base=2.5e8, drift=0.03, vol=0.12).rename("undvalue")
    prfvalue = _fund(203, base=1.2e8, drift=0.02, vol=0.13).rename("prfvalue")
    totalvalue = (fndvalue + undvalue + prfvalue
                  + _fund(204, base=1.0e8, drift=0.025, vol=0.09)).rename("totalvalue")
    fndholders = _fund(205, base=300.0, drift=0.05, vol=0.10).rename("fndholders")
    undholders = _fund(206, base=180.0, drift=0.03, vol=0.12).rename("undholders")
    prfholders = _fund(207, base=90.0, drift=0.02, vol=0.13).rename("prfholders")
    shrholders = _fund(208, base=420.0, drift=0.045, vol=0.10).rename("shrholders")
    cllholders = _fund(209, base=60.0, drift=0.04, vol=0.15).rename("cllholders")
    putholders = _fund(210, base=45.0, drift=0.035, vol=0.16).rename("putholders")
    cllvalue = _fund(211, base=8.0e7, drift=0.04, vol=0.16).rename("cllvalue")
    putvalue = _fund(212, base=6.0e7, drift=0.05, vol=0.17).rename("putvalue")
    # percentoftotal in (0,1)
    percentoftotal = (_fund(213, base=0.04, drift=0.02, vol=0.10)
                      .clip(upper=0.95)).rename("percentoftotal")

    cols = {
        "fndvalue": fndvalue, "undvalue": undvalue, "prfvalue": prfvalue,
        "totalvalue": totalvalue, "fndholders": fndholders, "undholders": undholders,
        "prfholders": prfholders, "shrholders": shrholders, "cllholders": cllholders,
        "putholders": putholders, "cllvalue": cllvalue, "putvalue": putvalue,
        "percentoftotal": percentoftotal,
    }

    n_features = 0
    nan_ok = 0
    results = {}
    for name, meta in REGISTRY.items():
        assert set(meta["inputs"]) <= ALLOW, "BAD INPUTS %s: %s" % (name, meta["inputs"])
        # every feature must consume >=1 ownership column
        own = {"shrholders", "shrvalue", "shrunits", "totalvalue", "percentoftotal",
               "fndholders", "undholders", "prfholders", "dbtholders", "putholders",
               "putvalue", "cllholders", "cllvalue", "wntholders", "wntvalue",
               "dbtvalue", "fndvalue", "undvalue", "prfvalue", "fndunits", "undunits"}
        assert len(set(meta["inputs"]) & own) >= 1, "NO OWNERSHIP COL %s" % name
        fn = meta["func"]
        args = [cols[c] for c in meta["inputs"]]
        y1 = fn(*args)
        y2 = fn(*args)
        pd.testing.assert_series_equal(y1, y2)
        q = y1.iloc[504:].dropna()
        assert len(q) > 0, name
        assert q.nunique() > 20, "%s nunique=%d" % (name, q.nunique())
        assert q.std() > 0, name
        assert not q.isna().all(), name
        nan_ratio = y1.iloc[504:].isna().mean()
        if nan_ratio < 0.5:
            nan_ok += 1
        results[name] = y1.iloc[504:]
        n_features += 1

    assert n_features == 75, n_features
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

    print("OK f51_ownership_mix_concentration_base_001_075_claude: %d features pass" % n_features)
