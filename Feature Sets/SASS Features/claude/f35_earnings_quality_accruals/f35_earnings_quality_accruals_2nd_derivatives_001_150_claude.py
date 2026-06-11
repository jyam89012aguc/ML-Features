import inspect
import numpy as np
import pandas as pd

TRADING_DAYS_YEAR = 252
TRADING_DAYS_TWOYEAR = 504
TRADING_DAYS_FIVEYEAR = 1260
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


def _roc(s, w):
    return s - s.shift(w)


def _sloan(netinc, ncfo, assets):
    return (netinc - ncfo) / assets.replace(0, np.nan)


def _cespread(ncfo, netinc, assets):
    return (ncfo - netinc) / assets.replace(0, np.nan)


def _conv(ncfo, netinc):
    return (ncfo / netinc.replace(0, np.nan)).clip(-10, 10)


def _dwc(workingcapital, assets, k):
    return (workingcapital - workingcapital.shift(k)) / assets.replace(0, np.nan)


def _dso(receivables, revenue):
    return receivables / revenue.replace(0, np.nan)


def _wcint(workingcapital, assets):
    return workingcapital / assets.replace(0, np.nan)


def _cfmargin(ncfo, revenue):
    return ncfo / revenue.replace(0, np.nan)


def _recvrev(receivables, revenue, k):
    rg = receivables / receivables.shift(k).replace(0, np.nan) - 1.0
    sg = revenue / revenue.shift(k).replace(0, np.nan) - 1.0
    return rg - sg


# slope (1st derivative): 63-bar ROC of the sloan_lvl base quantity
def f35eq_f35_earnings_quality_accruals_sloan_lvl_63d_slope_v001_signal(netinc, ncfo, assets):
    x = _mean(_sloan(netinc, ncfo, assets), 63)
    d = _roc(x, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# slope (1st derivative): 63-bar ROC of the sloanrev_lvl base quantity
def f35eq_f35_earnings_quality_accruals_sloanrev_lvl_63d_slope_v002_signal(netinc, ncfo, revenue):
    x = _mean((netinc - ncfo) / revenue.replace(0, np.nan), 126)
    d = _roc(x, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# slope (1st derivative): 63-bar ROC of the conv_lvl base quantity
def f35eq_f35_earnings_quality_accruals_conv_lvl_63d_slope_v003_signal(ncfo, netinc):
    x = _z(_mean(_conv(ncfo, netinc), 21), 252)
    d = _roc(x, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# slope (1st derivative): 63-bar ROC of the dwc_lvl base quantity
def f35eq_f35_earnings_quality_accruals_dwc_lvl_63d_slope_v004_signal(workingcapital, assets):
    x = _dwc(workingcapital, assets, 63)
    d = _roc(x, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# slope (1st derivative): 63-bar ROC of the wcint_lvl base quantity
def f35eq_f35_earnings_quality_accruals_wcint_lvl_63d_slope_v005_signal(workingcapital, assets):
    x = _wcint(workingcapital, assets)
    d = _roc(x, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# slope (1st derivative): 63-bar ROC of the wcrev_lvl base quantity
def f35eq_f35_earnings_quality_accruals_wcrev_lvl_63d_slope_v006_signal(workingcapital, revenue):
    x = workingcapital / revenue.replace(0, np.nan)
    d = _roc(x, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# slope (1st derivative): 63-bar ROC of the dso_lvl base quantity
def f35eq_f35_earnings_quality_accruals_dso_lvl_63d_slope_v007_signal(receivables, revenue):
    x = _dso(receivables, revenue)
    d = _roc(x, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# slope (1st derivative): 63-bar ROC of the recvassets_lvl base quantity
def f35eq_f35_earnings_quality_accruals_recvassets_lvl_63d_slope_v008_signal(receivables, assets):
    x = receivables / assets.replace(0, np.nan)
    d = _roc(x, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# slope (1st derivative): 63-bar ROC of the recvrev_lvl base quantity
def f35eq_f35_earnings_quality_accruals_recvrev_lvl_63d_slope_v009_signal(receivables, revenue):
    x = _recvrev(receivables, revenue, 63)
    d = _roc(x, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# slope (1st derivative): 63-bar ROC of the cfmargin_lvl base quantity
def f35eq_f35_earnings_quality_accruals_cfmargin_lvl_63d_slope_v010_signal(ncfo, revenue):
    x = _cfmargin(ncfo, revenue)
    d = _roc(x, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# slope (1st derivative): 63-bar ROC of the cfoa_lvl base quantity
def f35eq_f35_earnings_quality_accruals_cfoa_lvl_63d_slope_v011_signal(ncfo, assets):
    x = ncfo / assets.replace(0, np.nan)
    d = _roc(x, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# slope (1st derivative): 63-bar ROC of the roa_lvl base quantity
def f35eq_f35_earnings_quality_accruals_roa_lvl_63d_slope_v012_signal(netinc, assets):
    x = netinc / assets.replace(0, np.nan)
    d = _roc(x, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# slope (1st derivative): 63-bar ROC of the netmargin_lvl base quantity
def f35eq_f35_earnings_quality_accruals_netmargin_lvl_63d_slope_v013_signal(netinc, revenue):
    x = netinc / revenue.replace(0, np.nan)
    d = _roc(x, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# slope (1st derivative): 63-bar ROC of the turn_lvl base quantity
def f35eq_f35_earnings_quality_accruals_turn_lvl_63d_slope_v014_signal(revenue, assets):
    x = revenue / assets.replace(0, np.nan)
    d = _roc(x, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# slope (1st derivative): 63-bar ROC of the accvol_lvl base quantity
def f35eq_f35_earnings_quality_accruals_accvol_lvl_63d_slope_v015_signal(netinc, ncfo, assets):
    x = _std(_sloan(netinc, ncfo, assets), 126)
    d = _roc(x, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# slope (1st derivative): 63-bar ROC of the dsovol_lvl base quantity
def f35eq_f35_earnings_quality_accruals_dsovol_lvl_63d_slope_v016_signal(receivables, revenue):
    x = _std(_dso(receivables, revenue), 126)
    d = _roc(x, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# slope (1st derivative): 63-bar ROC of the convvol_lvl base quantity
def f35eq_f35_earnings_quality_accruals_convvol_lvl_63d_slope_v017_signal(ncfo, netinc):
    x = _std(_conv(ncfo, netinc), 126)
    d = _roc(x, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# slope (1st derivative): 63-bar ROC of the cfowc_lvl base quantity
def f35eq_f35_earnings_quality_accruals_cfowc_lvl_63d_slope_v018_signal(ncfo, workingcapital):
    x = (ncfo / workingcapital.replace(0, np.nan)).clip(-20, 20)
    d = _roc(x, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# slope (1st derivative): 63-bar ROC of the sloanz_lvl base quantity
def f35eq_f35_earnings_quality_accruals_sloanz_lvl_63d_slope_v019_signal(netinc, ncfo, assets):
    x = _z(_sloan(netinc, ncfo, assets), 126)
    d = _roc(x, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# slope (1st derivative): 63-bar ROC of the dsoz_lvl base quantity
def f35eq_f35_earnings_quality_accruals_dsoz_lvl_63d_slope_v020_signal(receivables, revenue):
    x = _z(_dso(receivables, revenue), 126)
    d = _roc(x, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# slope (1st derivative): 63-bar ROC of the wcintz_lvl base quantity
def f35eq_f35_earnings_quality_accruals_wcintz_lvl_63d_slope_v021_signal(workingcapital, assets):
    x = _z(_wcint(workingcapital, assets), 126)
    d = _roc(x, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# slope (1st derivative): 63-bar ROC of the cfmarginz_lvl base quantity
def f35eq_f35_earnings_quality_accruals_cfmarginz_lvl_63d_slope_v022_signal(ncfo, revenue):
    x = _z(_cfmargin(ncfo, revenue), 126)
    d = _roc(x, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# slope (1st derivative): 63-bar ROC of the recvrevh_lvl base quantity
def f35eq_f35_earnings_quality_accruals_recvrevh_lvl_63d_slope_v023_signal(receivables, revenue):
    x = _recvrev(receivables, revenue, 21)
    d = _roc(x, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# slope (1st derivative): 63-bar ROC of the dwch_lvl base quantity
def f35eq_f35_earnings_quality_accruals_dwch_lvl_63d_slope_v024_signal(workingcapital, assets):
    x = _dwc(workingcapital, assets, 21)
    d = _roc(x, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# slope (1st derivative): 63-bar ROC of the revqual_lvl base quantity
def f35eq_f35_earnings_quality_accruals_revqual_lvl_63d_slope_v025_signal(ncfo, revenue, receivables):
    x = _cfmargin(ncfo, revenue) - _z(_dso(receivables, revenue), 126) * _std(_cfmargin(ncfo, revenue), 126)
    d = _roc(x, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# slope (1st derivative): 63-bar ROC of the accrev_lvl base quantity
def f35eq_f35_earnings_quality_accruals_accrev_lvl_63d_slope_v026_signal(netinc, ncfo, revenue):
    x = _std((netinc - ncfo) / revenue.replace(0, np.nan), 126)
    d = _roc(x, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# slope (1st derivative): 63-bar ROC of the nivol_lvl base quantity
def f35eq_f35_earnings_quality_accruals_nivol_lvl_63d_slope_v027_signal(netinc, assets):
    x = _std(netinc / assets.replace(0, np.nan), 126)
    d = _roc(x, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# slope (1st derivative): 63-bar ROC of the cfvol_lvl base quantity
def f35eq_f35_earnings_quality_accruals_cfvol_lvl_63d_slope_v028_signal(ncfo, assets):
    x = _std(ncfo / assets.replace(0, np.nan), 126)
    d = _roc(x, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# slope (1st derivative): 63-bar ROC of the convturn_lvl base quantity
def f35eq_f35_earnings_quality_accruals_convturn_lvl_63d_slope_v029_signal(ncfo, netinc, revenue, assets):
    x = _mean(_conv(ncfo, netinc) * (revenue / assets.replace(0, np.nan)), 63)
    d = _roc(x, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# slope (1st derivative): 63-bar ROC of the wcinth_lvl base quantity
def f35eq_f35_earnings_quality_accruals_wcinth_lvl_63d_slope_v030_signal(workingcapital, assets):
    x = _mean(_wcint(workingcapital, assets), 21)
    d = _roc(x, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# slope (1st derivative): 63-bar ROC of the recvassetsh_lvl base quantity
def f35eq_f35_earnings_quality_accruals_recvassetsh_lvl_63d_slope_v031_signal(receivables, assets):
    x = _mean(receivables / assets.replace(0, np.nan), 21)
    d = _roc(x, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# slope (1st derivative): 63-bar ROC of the dsodelta_lvl base quantity
def f35eq_f35_earnings_quality_accruals_dsodelta_lvl_63d_slope_v032_signal(receivables, revenue):
    x = _roc(_mean(_dso(receivables, revenue), 21), 63)
    d = _roc(x, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# slope (1st derivative): 63-bar ROC of the sloandelta_lvl base quantity
def f35eq_f35_earnings_quality_accruals_sloandelta_lvl_63d_slope_v033_signal(netinc, ncfo, assets):
    x = _roc(_mean(_sloan(netinc, ncfo, assets), 21), 63)
    d = _roc(x, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# slope (1st derivative): 63-bar ROC of the wcdelta_lvl base quantity
def f35eq_f35_earnings_quality_accruals_wcdelta_lvl_63d_slope_v034_signal(workingcapital, assets):
    x = _roc(_mean(_wcint(workingcapital, assets), 21), 63)
    d = _roc(x, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# slope (1st derivative): 63-bar ROC of the smooth_lvl base quantity
def f35eq_f35_earnings_quality_accruals_smooth_lvl_63d_slope_v035_signal(netinc, ncfo):
    x = _std(netinc.pct_change(), 126) / _std(ncfo.pct_change(), 126).replace(0, np.nan)
    d = _roc(x, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# slope (1st derivative): 63-bar ROC of the nicfcorr_lvl base quantity
def f35eq_f35_earnings_quality_accruals_nicfcorr_lvl_63d_slope_v036_signal(netinc, ncfo):
    x = netinc.pct_change().rolling(126, min_periods=63).corr(ncfo.pct_change())
    d = _roc(x, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# slope (1st derivative): 63-bar ROC of the growthdso_lvl base quantity
def f35eq_f35_earnings_quality_accruals_growthdso_lvl_63d_slope_v037_signal(revenue, receivables):
    x = (revenue / revenue.shift(63).replace(0, np.nan) - 1.0) * _roc(_dso(receivables, revenue), 63)
    d = _roc(x, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# slope (1st derivative): 63-bar ROC of the growthwc_lvl base quantity
def f35eq_f35_earnings_quality_accruals_growthwc_lvl_63d_slope_v038_signal(revenue, workingcapital, assets):
    x = (revenue / revenue.shift(63).replace(0, np.nan) - 1.0).clip(-2, 2) * _dwc(workingcapital, assets, 63)
    d = _roc(x, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# slope (1st derivative): 63-bar ROC of the qroa_lvl base quantity
def f35eq_f35_earnings_quality_accruals_qroa_lvl_63d_slope_v039_signal(ncfo, netinc, assets):
    x = _mean(ncfo / assets.replace(0, np.nan) - _sloan(netinc, ncfo, assets).abs(), 63)
    d = _roc(x, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# slope (1st derivative): 63-bar ROC of the collrate_lvl base quantity
def f35eq_f35_earnings_quality_accruals_collrate_lvl_63d_slope_v040_signal(revenue, receivables):
    x = _mean(revenue / receivables.replace(0, np.nan), 63)
    d = _roc(x, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# slope (1st derivative): 63-bar ROC of the recvgrow_lvl base quantity
def f35eq_f35_earnings_quality_accruals_recvgrow_lvl_63d_slope_v041_signal(receivables):
    x = receivables / receivables.shift(63).replace(0, np.nan) - 1.0
    d = _roc(x, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# slope (1st derivative): 63-bar ROC of the revgrow_lvl base quantity
def f35eq_f35_earnings_quality_accruals_revgrow_lvl_63d_slope_v042_signal(revenue):
    x = revenue / revenue.shift(63).replace(0, np.nan) - 1.0
    d = _roc(x, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# slope (1st derivative): 63-bar ROC of the nigrow_lvl base quantity
def f35eq_f35_earnings_quality_accruals_nigrow_lvl_63d_slope_v043_signal(netinc):
    x = (netinc / netinc.shift(63).replace(0, np.nan) - 1.0).clip(-5, 5)
    d = _roc(x, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# slope (1st derivative): 63-bar ROC of the cfgrow_lvl base quantity
def f35eq_f35_earnings_quality_accruals_cfgrow_lvl_63d_slope_v044_signal(ncfo):
    x = (ncfo / ncfo.shift(63).replace(0, np.nan) - 1.0).clip(-5, 5)
    d = _roc(x, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# slope (1st derivative): 63-bar ROC of the assetgrow_lvl base quantity
def f35eq_f35_earnings_quality_accruals_assetgrow_lvl_63d_slope_v045_signal(assets):
    x = assets / assets.shift(63).replace(0, np.nan) - 1.0
    d = _roc(x, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# slope (1st derivative): 63-bar ROC of the cfcover_lvl base quantity
def f35eq_f35_earnings_quality_accruals_cfcover_lvl_63d_slope_v046_signal(ncfo, netinc):
    x = (ncfo.abs() / (netinc - ncfo).abs().replace(0, np.nan)).clip(0, 50)
    d = _roc(x, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# slope (1st derivative): 63-bar ROC of the dsorank_lvl base quantity
def f35eq_f35_earnings_quality_accruals_dsorank_lvl_63d_slope_v047_signal(receivables, revenue):
    x = _dso(receivables, revenue).rolling(252, min_periods=126).rank(pct=True) - 0.5
    d = _roc(x, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# slope (1st derivative): 63-bar ROC of the convrank_lvl base quantity
def f35eq_f35_earnings_quality_accruals_convrank_lvl_63d_slope_v048_signal(ncfo, netinc):
    x = _conv(ncfo, netinc).rolling(252, min_periods=126).rank(pct=True) - 0.5
    d = _roc(x, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# slope (1st derivative): 63-bar ROC of the cfmarginh_lvl base quantity
def f35eq_f35_earnings_quality_accruals_cfmarginh_lvl_63d_slope_v049_signal(ncfo, revenue):
    x = _mean(_cfmargin(ncfo, revenue), 21)
    d = _roc(x, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# slope (1st derivative): 63-bar ROC of the recvassetz_lvl base quantity
def f35eq_f35_earnings_quality_accruals_recvassetz_lvl_63d_slope_v050_signal(receivables, assets):
    x = _z(receivables / assets.replace(0, np.nan), 126)
    d = _roc(x, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# slope (1st derivative): 21-bar ROC of the sloan_z base quantity
def f35eq_f35_earnings_quality_accruals_sloan_z_21d_slope_v051_signal(netinc, ncfo, assets):
    x = _mean(_sloan(netinc, ncfo, assets), 63)
    x = _z(x, 126)
    d = _roc(x, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# slope (1st derivative): 21-bar ROC of the sloanrev_z base quantity
def f35eq_f35_earnings_quality_accruals_sloanrev_z_21d_slope_v052_signal(netinc, ncfo, revenue):
    x = _mean((netinc - ncfo) / revenue.replace(0, np.nan), 126)
    x = _z(x, 126)
    d = _roc(x, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# slope (1st derivative): 21-bar ROC of the conv_z base quantity
def f35eq_f35_earnings_quality_accruals_conv_z_21d_slope_v053_signal(ncfo, netinc):
    x = _z(_mean(_conv(ncfo, netinc), 21), 252)
    x = _z(x, 126)
    d = _roc(x, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# slope (1st derivative): 21-bar ROC of the dwc_z base quantity
def f35eq_f35_earnings_quality_accruals_dwc_z_21d_slope_v054_signal(workingcapital, assets):
    x = _dwc(workingcapital, assets, 63)
    x = _z(x, 126)
    d = _roc(x, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# slope (1st derivative): 21-bar ROC of the wcint_z base quantity
def f35eq_f35_earnings_quality_accruals_wcint_z_21d_slope_v055_signal(workingcapital, assets):
    x = _wcint(workingcapital, assets)
    x = _z(x, 126)
    d = _roc(x, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# slope (1st derivative): 21-bar ROC of the wcrev_z base quantity
def f35eq_f35_earnings_quality_accruals_wcrev_z_21d_slope_v056_signal(workingcapital, revenue):
    x = workingcapital / revenue.replace(0, np.nan)
    x = _z(x, 126)
    d = _roc(x, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# slope (1st derivative): 21-bar ROC of the dso_z base quantity
def f35eq_f35_earnings_quality_accruals_dso_z_21d_slope_v057_signal(receivables, revenue):
    x = _dso(receivables, revenue)
    x = _z(x, 126)
    d = _roc(x, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# slope (1st derivative): 21-bar ROC of the recvassets_z base quantity
def f35eq_f35_earnings_quality_accruals_recvassets_z_21d_slope_v058_signal(receivables, assets):
    x = receivables / assets.replace(0, np.nan)
    x = _z(x, 126)
    d = _roc(x, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# slope (1st derivative): 21-bar ROC of the recvrev_z base quantity
def f35eq_f35_earnings_quality_accruals_recvrev_z_21d_slope_v059_signal(receivables, revenue):
    x = _recvrev(receivables, revenue, 63)
    x = _z(x, 126)
    d = _roc(x, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# slope (1st derivative): 21-bar ROC of the cfmargin_z base quantity
def f35eq_f35_earnings_quality_accruals_cfmargin_z_21d_slope_v060_signal(ncfo, revenue):
    x = _cfmargin(ncfo, revenue)
    x = _z(x, 126)
    d = _roc(x, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# slope (1st derivative): 21-bar ROC of the cfoa_z base quantity
def f35eq_f35_earnings_quality_accruals_cfoa_z_21d_slope_v061_signal(ncfo, assets):
    x = ncfo / assets.replace(0, np.nan)
    x = _z(x, 126)
    d = _roc(x, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# slope (1st derivative): 21-bar ROC of the roa_z base quantity
def f35eq_f35_earnings_quality_accruals_roa_z_21d_slope_v062_signal(netinc, assets):
    x = netinc / assets.replace(0, np.nan)
    x = _z(x, 126)
    d = _roc(x, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# slope (1st derivative): 21-bar ROC of the netmargin_z base quantity
def f35eq_f35_earnings_quality_accruals_netmargin_z_21d_slope_v063_signal(netinc, revenue):
    x = netinc / revenue.replace(0, np.nan)
    x = _z(x, 126)
    d = _roc(x, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# slope (1st derivative): 21-bar ROC of the turn_z base quantity
def f35eq_f35_earnings_quality_accruals_turn_z_21d_slope_v064_signal(revenue, assets):
    x = revenue / assets.replace(0, np.nan)
    x = _z(x, 126)
    d = _roc(x, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# slope (1st derivative): 21-bar ROC of the accvol_z base quantity
def f35eq_f35_earnings_quality_accruals_accvol_z_21d_slope_v065_signal(netinc, ncfo, assets):
    x = _std(_sloan(netinc, ncfo, assets), 126)
    x = _z(x, 126)
    d = _roc(x, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# slope (1st derivative): 21-bar ROC of the dsovol_z base quantity
def f35eq_f35_earnings_quality_accruals_dsovol_z_21d_slope_v066_signal(receivables, revenue):
    x = _std(_dso(receivables, revenue), 126)
    x = _z(x, 126)
    d = _roc(x, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# slope (1st derivative): 21-bar ROC of the convvol_z base quantity
def f35eq_f35_earnings_quality_accruals_convvol_z_21d_slope_v067_signal(ncfo, netinc):
    x = _std(_conv(ncfo, netinc), 126)
    x = _z(x, 126)
    d = _roc(x, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# slope (1st derivative): 21-bar ROC of the cfowc_z base quantity
def f35eq_f35_earnings_quality_accruals_cfowc_z_21d_slope_v068_signal(ncfo, workingcapital):
    x = (ncfo / workingcapital.replace(0, np.nan)).clip(-20, 20)
    x = _z(x, 126)
    d = _roc(x, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# slope (1st derivative): 21-bar ROC of the sloanz_z base quantity
def f35eq_f35_earnings_quality_accruals_sloanz_z_21d_slope_v069_signal(netinc, ncfo, assets):
    x = _z(_sloan(netinc, ncfo, assets), 126)
    x = _z(x, 126)
    d = _roc(x, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# slope (1st derivative): 21-bar ROC of the dsoz_z base quantity
def f35eq_f35_earnings_quality_accruals_dsoz_z_21d_slope_v070_signal(receivables, revenue):
    x = _z(_dso(receivables, revenue), 126)
    x = _z(x, 126)
    d = _roc(x, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# slope (1st derivative): 21-bar ROC of the wcintz_z base quantity
def f35eq_f35_earnings_quality_accruals_wcintz_z_21d_slope_v071_signal(workingcapital, assets):
    x = _z(_wcint(workingcapital, assets), 126)
    x = _z(x, 126)
    d = _roc(x, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# slope (1st derivative): 21-bar ROC of the cfmarginz_z base quantity
def f35eq_f35_earnings_quality_accruals_cfmarginz_z_21d_slope_v072_signal(ncfo, revenue):
    x = _z(_cfmargin(ncfo, revenue), 126)
    x = _z(x, 126)
    d = _roc(x, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# slope (1st derivative): 21-bar ROC of the recvrevh_z base quantity
def f35eq_f35_earnings_quality_accruals_recvrevh_z_21d_slope_v073_signal(receivables, revenue):
    x = _recvrev(receivables, revenue, 21)
    x = _z(x, 126)
    d = _roc(x, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# slope (1st derivative): 21-bar ROC of the dwch_z base quantity
def f35eq_f35_earnings_quality_accruals_dwch_z_21d_slope_v074_signal(workingcapital, assets):
    x = _dwc(workingcapital, assets, 21)
    x = _z(x, 126)
    d = _roc(x, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# slope (1st derivative): 21-bar ROC of the revqual_z base quantity
def f35eq_f35_earnings_quality_accruals_revqual_z_21d_slope_v075_signal(ncfo, revenue, receivables):
    x = _cfmargin(ncfo, revenue) - _z(_dso(receivables, revenue), 126) * _std(_cfmargin(ncfo, revenue), 126)
    x = _z(x, 126)
    d = _roc(x, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# slope (1st derivative): 21-bar ROC of the accrev_z base quantity
def f35eq_f35_earnings_quality_accruals_accrev_z_21d_slope_v076_signal(netinc, ncfo, revenue):
    x = _std((netinc - ncfo) / revenue.replace(0, np.nan), 126)
    x = _z(x, 126)
    d = _roc(x, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# slope (1st derivative): 21-bar ROC of the nivol_z base quantity
def f35eq_f35_earnings_quality_accruals_nivol_z_21d_slope_v077_signal(netinc, assets):
    x = _std(netinc / assets.replace(0, np.nan), 126)
    x = _z(x, 126)
    d = _roc(x, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# slope (1st derivative): 21-bar ROC of the cfvol_z base quantity
def f35eq_f35_earnings_quality_accruals_cfvol_z_21d_slope_v078_signal(ncfo, assets):
    x = _std(ncfo / assets.replace(0, np.nan), 126)
    x = _z(x, 126)
    d = _roc(x, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# slope (1st derivative): 21-bar ROC of the convturn_z base quantity
def f35eq_f35_earnings_quality_accruals_convturn_z_21d_slope_v079_signal(ncfo, netinc, revenue, assets):
    x = _mean(_conv(ncfo, netinc) * (revenue / assets.replace(0, np.nan)), 63)
    x = _z(x, 126)
    d = _roc(x, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# slope (1st derivative): 21-bar ROC of the wcinth_z base quantity
def f35eq_f35_earnings_quality_accruals_wcinth_z_21d_slope_v080_signal(workingcapital, assets):
    x = _mean(_wcint(workingcapital, assets), 21)
    x = _z(x, 126)
    d = _roc(x, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# slope (1st derivative): 21-bar ROC of the recvassetsh_z base quantity
def f35eq_f35_earnings_quality_accruals_recvassetsh_z_21d_slope_v081_signal(receivables, assets):
    x = _mean(receivables / assets.replace(0, np.nan), 21)
    x = _z(x, 126)
    d = _roc(x, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# slope (1st derivative): 21-bar ROC of the dsodelta_z base quantity
def f35eq_f35_earnings_quality_accruals_dsodelta_z_21d_slope_v082_signal(receivables, revenue):
    x = _roc(_mean(_dso(receivables, revenue), 21), 63)
    x = _z(x, 126)
    d = _roc(x, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# slope (1st derivative): 21-bar ROC of the sloandelta_z base quantity
def f35eq_f35_earnings_quality_accruals_sloandelta_z_21d_slope_v083_signal(netinc, ncfo, assets):
    x = _roc(_mean(_sloan(netinc, ncfo, assets), 21), 63)
    x = _z(x, 126)
    d = _roc(x, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# slope (1st derivative): 21-bar ROC of the wcdelta_z base quantity
def f35eq_f35_earnings_quality_accruals_wcdelta_z_21d_slope_v084_signal(workingcapital, assets):
    x = _roc(_mean(_wcint(workingcapital, assets), 21), 63)
    x = _z(x, 126)
    d = _roc(x, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# slope (1st derivative): 21-bar ROC of the smooth_z base quantity
def f35eq_f35_earnings_quality_accruals_smooth_z_21d_slope_v085_signal(netinc, ncfo):
    x = _std(netinc.pct_change(), 126) / _std(ncfo.pct_change(), 126).replace(0, np.nan)
    x = _z(x, 126)
    d = _roc(x, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# slope (1st derivative): 21-bar ROC of the nicfcorr_z base quantity
def f35eq_f35_earnings_quality_accruals_nicfcorr_z_21d_slope_v086_signal(netinc, ncfo):
    x = netinc.pct_change().rolling(126, min_periods=63).corr(ncfo.pct_change())
    x = _z(x, 126)
    d = _roc(x, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# slope (1st derivative): 21-bar ROC of the growthdso_z base quantity
def f35eq_f35_earnings_quality_accruals_growthdso_z_21d_slope_v087_signal(revenue, receivables):
    x = (revenue / revenue.shift(63).replace(0, np.nan) - 1.0) * _roc(_dso(receivables, revenue), 63)
    x = _z(x, 126)
    d = _roc(x, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# slope (1st derivative): 21-bar ROC of the growthwc_z base quantity
def f35eq_f35_earnings_quality_accruals_growthwc_z_21d_slope_v088_signal(revenue, workingcapital, assets):
    x = (revenue / revenue.shift(63).replace(0, np.nan) - 1.0).clip(-2, 2) * _dwc(workingcapital, assets, 63)
    x = _z(x, 126)
    d = _roc(x, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# slope (1st derivative): 21-bar ROC of the qroa_z base quantity
def f35eq_f35_earnings_quality_accruals_qroa_z_21d_slope_v089_signal(ncfo, netinc, assets):
    x = _mean(ncfo / assets.replace(0, np.nan) - _sloan(netinc, ncfo, assets).abs(), 63)
    x = _z(x, 126)
    d = _roc(x, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# slope (1st derivative): 21-bar ROC of the collrate_z base quantity
def f35eq_f35_earnings_quality_accruals_collrate_z_21d_slope_v090_signal(revenue, receivables):
    x = _mean(revenue / receivables.replace(0, np.nan), 63)
    x = _z(x, 126)
    d = _roc(x, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# slope (1st derivative): 21-bar ROC of the recvgrow_z base quantity
def f35eq_f35_earnings_quality_accruals_recvgrow_z_21d_slope_v091_signal(receivables):
    x = receivables / receivables.shift(63).replace(0, np.nan) - 1.0
    x = _z(x, 126)
    d = _roc(x, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# slope (1st derivative): 21-bar ROC of the revgrow_z base quantity
def f35eq_f35_earnings_quality_accruals_revgrow_z_21d_slope_v092_signal(revenue):
    x = revenue / revenue.shift(63).replace(0, np.nan) - 1.0
    x = _z(x, 126)
    d = _roc(x, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# slope (1st derivative): 21-bar ROC of the nigrow_z base quantity
def f35eq_f35_earnings_quality_accruals_nigrow_z_21d_slope_v093_signal(netinc):
    x = (netinc / netinc.shift(63).replace(0, np.nan) - 1.0).clip(-5, 5)
    x = _z(x, 126)
    d = _roc(x, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# slope (1st derivative): 21-bar ROC of the cfgrow_z base quantity
def f35eq_f35_earnings_quality_accruals_cfgrow_z_21d_slope_v094_signal(ncfo):
    x = (ncfo / ncfo.shift(63).replace(0, np.nan) - 1.0).clip(-5, 5)
    x = _z(x, 126)
    d = _roc(x, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# slope (1st derivative): 21-bar ROC of the assetgrow_z base quantity
def f35eq_f35_earnings_quality_accruals_assetgrow_z_21d_slope_v095_signal(assets):
    x = assets / assets.shift(63).replace(0, np.nan) - 1.0
    x = _z(x, 126)
    d = _roc(x, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# slope (1st derivative): 21-bar ROC of the cfcover_z base quantity
def f35eq_f35_earnings_quality_accruals_cfcover_z_21d_slope_v096_signal(ncfo, netinc):
    x = (ncfo.abs() / (netinc - ncfo).abs().replace(0, np.nan)).clip(0, 50)
    x = _z(x, 126)
    d = _roc(x, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# slope (1st derivative): 21-bar ROC of the dsorank_z base quantity
def f35eq_f35_earnings_quality_accruals_dsorank_z_21d_slope_v097_signal(receivables, revenue):
    x = _dso(receivables, revenue).rolling(252, min_periods=126).rank(pct=True) - 0.5
    x = _z(x, 126)
    d = _roc(x, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# slope (1st derivative): 21-bar ROC of the convrank_z base quantity
def f35eq_f35_earnings_quality_accruals_convrank_z_21d_slope_v098_signal(ncfo, netinc):
    x = _conv(ncfo, netinc).rolling(252, min_periods=126).rank(pct=True) - 0.5
    x = _z(x, 126)
    d = _roc(x, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# slope (1st derivative): 21-bar ROC of the cfmarginh_z base quantity
def f35eq_f35_earnings_quality_accruals_cfmarginh_z_21d_slope_v099_signal(ncfo, revenue):
    x = _mean(_cfmargin(ncfo, revenue), 21)
    x = _z(x, 126)
    d = _roc(x, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# slope (1st derivative): 21-bar ROC of the recvassetz_z base quantity
def f35eq_f35_earnings_quality_accruals_recvassetz_z_21d_slope_v100_signal(receivables, assets):
    x = _z(receivables / assets.replace(0, np.nan), 126)
    x = _z(x, 126)
    d = _roc(x, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# slope (1st derivative): 5-bar ROC of the sloan_rk base quantity
def f35eq_f35_earnings_quality_accruals_sloan_rk_5d_slope_v101_signal(netinc, ncfo, assets):
    x = _mean(_sloan(netinc, ncfo, assets), 63)
    x = x.rolling(252, min_periods=126).rank(pct=True) - 0.5
    d = _roc(x, 5)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# slope (1st derivative): 5-bar ROC of the sloanrev_rk base quantity
def f35eq_f35_earnings_quality_accruals_sloanrev_rk_5d_slope_v102_signal(netinc, ncfo, revenue):
    x = _mean((netinc - ncfo) / revenue.replace(0, np.nan), 126)
    x = x.rolling(252, min_periods=126).rank(pct=True) - 0.5
    d = _roc(x, 5)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# slope (1st derivative): 5-bar ROC of the conv_rk base quantity
def f35eq_f35_earnings_quality_accruals_conv_rk_5d_slope_v103_signal(ncfo, netinc):
    x = _z(_mean(_conv(ncfo, netinc), 21), 252)
    x = x.rolling(252, min_periods=126).rank(pct=True) - 0.5
    d = _roc(x, 5)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# slope (1st derivative): 5-bar ROC of the dwc_rk base quantity
def f35eq_f35_earnings_quality_accruals_dwc_rk_5d_slope_v104_signal(workingcapital, assets):
    x = _dwc(workingcapital, assets, 63)
    x = x.rolling(252, min_periods=126).rank(pct=True) - 0.5
    d = _roc(x, 5)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# slope (1st derivative): 5-bar ROC of the wcint_rk base quantity
def f35eq_f35_earnings_quality_accruals_wcint_rk_5d_slope_v105_signal(workingcapital, assets):
    x = _wcint(workingcapital, assets)
    x = x.rolling(252, min_periods=126).rank(pct=True) - 0.5
    d = _roc(x, 5)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# slope (1st derivative): 5-bar ROC of the wcrev_rk base quantity
def f35eq_f35_earnings_quality_accruals_wcrev_rk_5d_slope_v106_signal(workingcapital, revenue):
    x = workingcapital / revenue.replace(0, np.nan)
    x = x.rolling(252, min_periods=126).rank(pct=True) - 0.5
    d = _roc(x, 5)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# slope (1st derivative): 5-bar ROC of the dso_rk base quantity
def f35eq_f35_earnings_quality_accruals_dso_rk_5d_slope_v107_signal(receivables, revenue):
    x = _dso(receivables, revenue)
    x = x.rolling(252, min_periods=126).rank(pct=True) - 0.5
    d = _roc(x, 5)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# slope (1st derivative): 5-bar ROC of the recvassets_rk base quantity
def f35eq_f35_earnings_quality_accruals_recvassets_rk_5d_slope_v108_signal(receivables, assets):
    x = receivables / assets.replace(0, np.nan)
    x = x.rolling(252, min_periods=126).rank(pct=True) - 0.5
    d = _roc(x, 5)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# slope (1st derivative): 5-bar ROC of the recvrev_rk base quantity
def f35eq_f35_earnings_quality_accruals_recvrev_rk_5d_slope_v109_signal(receivables, revenue):
    x = _recvrev(receivables, revenue, 63)
    x = x.rolling(252, min_periods=126).rank(pct=True) - 0.5
    d = _roc(x, 5)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# slope (1st derivative): 5-bar ROC of the cfmargin_rk base quantity
def f35eq_f35_earnings_quality_accruals_cfmargin_rk_5d_slope_v110_signal(ncfo, revenue):
    x = _cfmargin(ncfo, revenue)
    x = x.rolling(252, min_periods=126).rank(pct=True) - 0.5
    d = _roc(x, 5)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# slope (1st derivative): 5-bar ROC of the cfoa_rk base quantity
def f35eq_f35_earnings_quality_accruals_cfoa_rk_5d_slope_v111_signal(ncfo, assets):
    x = ncfo / assets.replace(0, np.nan)
    x = x.rolling(252, min_periods=126).rank(pct=True) - 0.5
    d = _roc(x, 5)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# slope (1st derivative): 5-bar ROC of the roa_rk base quantity
def f35eq_f35_earnings_quality_accruals_roa_rk_5d_slope_v112_signal(netinc, assets):
    x = netinc / assets.replace(0, np.nan)
    x = x.rolling(252, min_periods=126).rank(pct=True) - 0.5
    d = _roc(x, 5)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# slope (1st derivative): 5-bar ROC of the netmargin_rk base quantity
def f35eq_f35_earnings_quality_accruals_netmargin_rk_5d_slope_v113_signal(netinc, revenue):
    x = netinc / revenue.replace(0, np.nan)
    x = x.rolling(252, min_periods=126).rank(pct=True) - 0.5
    d = _roc(x, 5)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# slope (1st derivative): 5-bar ROC of the turn_rk base quantity
def f35eq_f35_earnings_quality_accruals_turn_rk_5d_slope_v114_signal(revenue, assets):
    x = revenue / assets.replace(0, np.nan)
    x = x.rolling(252, min_periods=126).rank(pct=True) - 0.5
    d = _roc(x, 5)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# slope (1st derivative): 5-bar ROC of the accvol_rk base quantity
def f35eq_f35_earnings_quality_accruals_accvol_rk_5d_slope_v115_signal(netinc, ncfo, assets):
    x = _std(_sloan(netinc, ncfo, assets), 126)
    x = x.rolling(252, min_periods=126).rank(pct=True) - 0.5
    d = _roc(x, 5)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# slope (1st derivative): 5-bar ROC of the dsovol_rk base quantity
def f35eq_f35_earnings_quality_accruals_dsovol_rk_5d_slope_v116_signal(receivables, revenue):
    x = _std(_dso(receivables, revenue), 126)
    x = x.rolling(252, min_periods=126).rank(pct=True) - 0.5
    d = _roc(x, 5)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# slope (1st derivative): 5-bar ROC of the convvol_rk base quantity
def f35eq_f35_earnings_quality_accruals_convvol_rk_5d_slope_v117_signal(ncfo, netinc):
    x = _std(_conv(ncfo, netinc), 126)
    x = x.rolling(252, min_periods=126).rank(pct=True) - 0.5
    d = _roc(x, 5)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# slope (1st derivative): 5-bar ROC of the cfowc_rk base quantity
def f35eq_f35_earnings_quality_accruals_cfowc_rk_5d_slope_v118_signal(ncfo, workingcapital):
    x = (ncfo / workingcapital.replace(0, np.nan)).clip(-20, 20)
    x = x.rolling(252, min_periods=126).rank(pct=True) - 0.5
    d = _roc(x, 5)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# slope (1st derivative): 5-bar ROC of the sloanz_rk base quantity
def f35eq_f35_earnings_quality_accruals_sloanz_rk_5d_slope_v119_signal(netinc, ncfo, assets):
    x = _z(_sloan(netinc, ncfo, assets), 126)
    x = x.rolling(252, min_periods=126).rank(pct=True) - 0.5
    d = _roc(x, 5)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# slope (1st derivative): 5-bar ROC of the dsoz_rk base quantity
def f35eq_f35_earnings_quality_accruals_dsoz_rk_5d_slope_v120_signal(receivables, revenue):
    x = _z(_dso(receivables, revenue), 126)
    x = x.rolling(252, min_periods=126).rank(pct=True) - 0.5
    d = _roc(x, 5)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# slope (1st derivative): 5-bar ROC of the wcintz_rk base quantity
def f35eq_f35_earnings_quality_accruals_wcintz_rk_5d_slope_v121_signal(workingcapital, assets):
    x = _z(_wcint(workingcapital, assets), 126)
    x = x.rolling(252, min_periods=126).rank(pct=True) - 0.5
    d = _roc(x, 5)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# slope (1st derivative): 5-bar ROC of the cfmarginz_rk base quantity
def f35eq_f35_earnings_quality_accruals_cfmarginz_rk_5d_slope_v122_signal(ncfo, revenue):
    x = _z(_cfmargin(ncfo, revenue), 126)
    x = x.rolling(252, min_periods=126).rank(pct=True) - 0.5
    d = _roc(x, 5)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# slope (1st derivative): 5-bar ROC of the recvrevh_rk base quantity
def f35eq_f35_earnings_quality_accruals_recvrevh_rk_5d_slope_v123_signal(receivables, revenue):
    x = _recvrev(receivables, revenue, 21)
    x = x.rolling(252, min_periods=126).rank(pct=True) - 0.5
    d = _roc(x, 5)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# slope (1st derivative): 5-bar ROC of the dwch_rk base quantity
def f35eq_f35_earnings_quality_accruals_dwch_rk_5d_slope_v124_signal(workingcapital, assets):
    x = _dwc(workingcapital, assets, 21)
    x = x.rolling(252, min_periods=126).rank(pct=True) - 0.5
    d = _roc(x, 5)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# slope (1st derivative): 5-bar ROC of the revqual_rk base quantity
def f35eq_f35_earnings_quality_accruals_revqual_rk_5d_slope_v125_signal(ncfo, revenue, receivables):
    x = _cfmargin(ncfo, revenue) - _z(_dso(receivables, revenue), 126) * _std(_cfmargin(ncfo, revenue), 126)
    x = x.rolling(252, min_periods=126).rank(pct=True) - 0.5
    d = _roc(x, 5)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# slope (1st derivative): 5-bar ROC of the accrev_rk base quantity
def f35eq_f35_earnings_quality_accruals_accrev_rk_5d_slope_v126_signal(netinc, ncfo, revenue):
    x = _std((netinc - ncfo) / revenue.replace(0, np.nan), 126)
    x = x.rolling(252, min_periods=126).rank(pct=True) - 0.5
    d = _roc(x, 5)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# slope (1st derivative): 5-bar ROC of the nivol_rk base quantity
def f35eq_f35_earnings_quality_accruals_nivol_rk_5d_slope_v127_signal(netinc, assets):
    x = _std(netinc / assets.replace(0, np.nan), 126)
    x = x.rolling(252, min_periods=126).rank(pct=True) - 0.5
    d = _roc(x, 5)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# slope (1st derivative): 5-bar ROC of the cfvol_rk base quantity
def f35eq_f35_earnings_quality_accruals_cfvol_rk_5d_slope_v128_signal(ncfo, assets):
    x = _std(ncfo / assets.replace(0, np.nan), 126)
    x = x.rolling(252, min_periods=126).rank(pct=True) - 0.5
    d = _roc(x, 5)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# slope (1st derivative): 5-bar ROC of the convturn_rk base quantity
def f35eq_f35_earnings_quality_accruals_convturn_rk_5d_slope_v129_signal(ncfo, netinc, revenue, assets):
    x = _mean(_conv(ncfo, netinc) * (revenue / assets.replace(0, np.nan)), 63)
    x = x.rolling(252, min_periods=126).rank(pct=True) - 0.5
    d = _roc(x, 5)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# slope (1st derivative): 5-bar ROC of the wcinth_rk base quantity
def f35eq_f35_earnings_quality_accruals_wcinth_rk_5d_slope_v130_signal(workingcapital, assets):
    x = _mean(_wcint(workingcapital, assets), 21)
    x = x.rolling(252, min_periods=126).rank(pct=True) - 0.5
    d = _roc(x, 5)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# slope (1st derivative): 5-bar ROC of the recvassetsh_rk base quantity
def f35eq_f35_earnings_quality_accruals_recvassetsh_rk_5d_slope_v131_signal(receivables, assets):
    x = _mean(receivables / assets.replace(0, np.nan), 21)
    x = x.rolling(252, min_periods=126).rank(pct=True) - 0.5
    d = _roc(x, 5)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# slope (1st derivative): 5-bar ROC of the dsodelta_rk base quantity
def f35eq_f35_earnings_quality_accruals_dsodelta_rk_5d_slope_v132_signal(receivables, revenue):
    x = _roc(_mean(_dso(receivables, revenue), 21), 63)
    x = x.rolling(252, min_periods=126).rank(pct=True) - 0.5
    d = _roc(x, 5)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# slope (1st derivative): 5-bar ROC of the sloandelta_rk base quantity
def f35eq_f35_earnings_quality_accruals_sloandelta_rk_5d_slope_v133_signal(netinc, ncfo, assets):
    x = _roc(_mean(_sloan(netinc, ncfo, assets), 21), 63)
    x = x.rolling(252, min_periods=126).rank(pct=True) - 0.5
    d = _roc(x, 5)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# slope (1st derivative): 5-bar ROC of the wcdelta_rk base quantity
def f35eq_f35_earnings_quality_accruals_wcdelta_rk_5d_slope_v134_signal(workingcapital, assets):
    x = _roc(_mean(_wcint(workingcapital, assets), 21), 63)
    x = x.rolling(252, min_periods=126).rank(pct=True) - 0.5
    d = _roc(x, 5)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# slope (1st derivative): 5-bar ROC of the smooth_rk base quantity
def f35eq_f35_earnings_quality_accruals_smooth_rk_5d_slope_v135_signal(netinc, ncfo):
    x = _std(netinc.pct_change(), 126) / _std(ncfo.pct_change(), 126).replace(0, np.nan)
    x = x.rolling(252, min_periods=126).rank(pct=True) - 0.5
    d = _roc(x, 5)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# slope (1st derivative): 5-bar ROC of the nicfcorr_rk base quantity
def f35eq_f35_earnings_quality_accruals_nicfcorr_rk_5d_slope_v136_signal(netinc, ncfo):
    x = netinc.pct_change().rolling(126, min_periods=63).corr(ncfo.pct_change())
    x = x.rolling(252, min_periods=126).rank(pct=True) - 0.5
    d = _roc(x, 5)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# slope (1st derivative): 5-bar ROC of the growthdso_rk base quantity
def f35eq_f35_earnings_quality_accruals_growthdso_rk_5d_slope_v137_signal(revenue, receivables):
    x = (revenue / revenue.shift(63).replace(0, np.nan) - 1.0) * _roc(_dso(receivables, revenue), 63)
    x = x.rolling(252, min_periods=126).rank(pct=True) - 0.5
    d = _roc(x, 5)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# slope (1st derivative): 5-bar ROC of the growthwc_rk base quantity
def f35eq_f35_earnings_quality_accruals_growthwc_rk_5d_slope_v138_signal(revenue, workingcapital, assets):
    x = (revenue / revenue.shift(63).replace(0, np.nan) - 1.0).clip(-2, 2) * _dwc(workingcapital, assets, 63)
    x = x.rolling(252, min_periods=126).rank(pct=True) - 0.5
    d = _roc(x, 5)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# slope (1st derivative): 5-bar ROC of the qroa_rk base quantity
def f35eq_f35_earnings_quality_accruals_qroa_rk_5d_slope_v139_signal(ncfo, netinc, assets):
    x = _mean(ncfo / assets.replace(0, np.nan) - _sloan(netinc, ncfo, assets).abs(), 63)
    x = x.rolling(252, min_periods=126).rank(pct=True) - 0.5
    d = _roc(x, 5)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# slope (1st derivative): 5-bar ROC of the collrate_rk base quantity
def f35eq_f35_earnings_quality_accruals_collrate_rk_5d_slope_v140_signal(revenue, receivables):
    x = _mean(revenue / receivables.replace(0, np.nan), 63)
    x = x.rolling(252, min_periods=126).rank(pct=True) - 0.5
    d = _roc(x, 5)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# slope (1st derivative): 5-bar ROC of the recvgrow_rk base quantity
def f35eq_f35_earnings_quality_accruals_recvgrow_rk_5d_slope_v141_signal(receivables):
    x = receivables / receivables.shift(63).replace(0, np.nan) - 1.0
    x = x.rolling(252, min_periods=126).rank(pct=True) - 0.5
    d = _roc(x, 5)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# slope (1st derivative): 5-bar ROC of the revgrow_rk base quantity
def f35eq_f35_earnings_quality_accruals_revgrow_rk_5d_slope_v142_signal(revenue):
    x = revenue / revenue.shift(63).replace(0, np.nan) - 1.0
    x = x.rolling(252, min_periods=126).rank(pct=True) - 0.5
    d = _roc(x, 5)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# slope (1st derivative): 5-bar ROC of the nigrow_rk base quantity
def f35eq_f35_earnings_quality_accruals_nigrow_rk_5d_slope_v143_signal(netinc):
    x = (netinc / netinc.shift(63).replace(0, np.nan) - 1.0).clip(-5, 5)
    x = x.rolling(252, min_periods=126).rank(pct=True) - 0.5
    d = _roc(x, 5)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# slope (1st derivative): 5-bar ROC of the cfgrow_rk base quantity
def f35eq_f35_earnings_quality_accruals_cfgrow_rk_5d_slope_v144_signal(ncfo):
    x = (ncfo / ncfo.shift(63).replace(0, np.nan) - 1.0).clip(-5, 5)
    x = x.rolling(252, min_periods=126).rank(pct=True) - 0.5
    d = _roc(x, 5)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# slope (1st derivative): 5-bar ROC of the assetgrow_rk base quantity
def f35eq_f35_earnings_quality_accruals_assetgrow_rk_5d_slope_v145_signal(assets):
    x = assets / assets.shift(63).replace(0, np.nan) - 1.0
    x = x.rolling(252, min_periods=126).rank(pct=True) - 0.5
    d = _roc(x, 5)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# slope (1st derivative): 5-bar ROC of the cfcover_rk base quantity
def f35eq_f35_earnings_quality_accruals_cfcover_rk_5d_slope_v146_signal(ncfo, netinc):
    x = (ncfo.abs() / (netinc - ncfo).abs().replace(0, np.nan)).clip(0, 50)
    x = x.rolling(252, min_periods=126).rank(pct=True) - 0.5
    d = _roc(x, 5)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# slope (1st derivative): 5-bar ROC of the dsorank_rk base quantity
def f35eq_f35_earnings_quality_accruals_dsorank_rk_5d_slope_v147_signal(receivables, revenue):
    x = _dso(receivables, revenue).rolling(252, min_periods=126).rank(pct=True) - 0.5
    x = x.rolling(252, min_periods=126).rank(pct=True) - 0.5
    d = _roc(x, 5)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# slope (1st derivative): 5-bar ROC of the convrank_rk base quantity
def f35eq_f35_earnings_quality_accruals_convrank_rk_5d_slope_v148_signal(ncfo, netinc):
    x = _conv(ncfo, netinc).rolling(252, min_periods=126).rank(pct=True) - 0.5
    x = x.rolling(252, min_periods=126).rank(pct=True) - 0.5
    d = _roc(x, 5)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# slope (1st derivative): 5-bar ROC of the cfmarginh_rk base quantity
def f35eq_f35_earnings_quality_accruals_cfmarginh_rk_5d_slope_v149_signal(ncfo, revenue):
    x = _mean(_cfmargin(ncfo, revenue), 21)
    x = x.rolling(252, min_periods=126).rank(pct=True) - 0.5
    d = _roc(x, 5)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# slope (1st derivative): 5-bar ROC of the recvassetz_rk base quantity
def f35eq_f35_earnings_quality_accruals_recvassetz_rk_5d_slope_v150_signal(receivables, assets):
    x = _z(receivables / assets.replace(0, np.nan), 126)
    x = x.rolling(252, min_periods=126).rank(pct=True) - 0.5
    d = _roc(x, 5)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

_FEATURES = [
    f35eq_f35_earnings_quality_accruals_sloan_lvl_63d_slope_v001_signal,
    f35eq_f35_earnings_quality_accruals_sloanrev_lvl_63d_slope_v002_signal,
    f35eq_f35_earnings_quality_accruals_conv_lvl_63d_slope_v003_signal,
    f35eq_f35_earnings_quality_accruals_dwc_lvl_63d_slope_v004_signal,
    f35eq_f35_earnings_quality_accruals_wcint_lvl_63d_slope_v005_signal,
    f35eq_f35_earnings_quality_accruals_wcrev_lvl_63d_slope_v006_signal,
    f35eq_f35_earnings_quality_accruals_dso_lvl_63d_slope_v007_signal,
    f35eq_f35_earnings_quality_accruals_recvassets_lvl_63d_slope_v008_signal,
    f35eq_f35_earnings_quality_accruals_recvrev_lvl_63d_slope_v009_signal,
    f35eq_f35_earnings_quality_accruals_cfmargin_lvl_63d_slope_v010_signal,
    f35eq_f35_earnings_quality_accruals_cfoa_lvl_63d_slope_v011_signal,
    f35eq_f35_earnings_quality_accruals_roa_lvl_63d_slope_v012_signal,
    f35eq_f35_earnings_quality_accruals_netmargin_lvl_63d_slope_v013_signal,
    f35eq_f35_earnings_quality_accruals_turn_lvl_63d_slope_v014_signal,
    f35eq_f35_earnings_quality_accruals_accvol_lvl_63d_slope_v015_signal,
    f35eq_f35_earnings_quality_accruals_dsovol_lvl_63d_slope_v016_signal,
    f35eq_f35_earnings_quality_accruals_convvol_lvl_63d_slope_v017_signal,
    f35eq_f35_earnings_quality_accruals_cfowc_lvl_63d_slope_v018_signal,
    f35eq_f35_earnings_quality_accruals_sloanz_lvl_63d_slope_v019_signal,
    f35eq_f35_earnings_quality_accruals_dsoz_lvl_63d_slope_v020_signal,
    f35eq_f35_earnings_quality_accruals_wcintz_lvl_63d_slope_v021_signal,
    f35eq_f35_earnings_quality_accruals_cfmarginz_lvl_63d_slope_v022_signal,
    f35eq_f35_earnings_quality_accruals_recvrevh_lvl_63d_slope_v023_signal,
    f35eq_f35_earnings_quality_accruals_dwch_lvl_63d_slope_v024_signal,
    f35eq_f35_earnings_quality_accruals_revqual_lvl_63d_slope_v025_signal,
    f35eq_f35_earnings_quality_accruals_accrev_lvl_63d_slope_v026_signal,
    f35eq_f35_earnings_quality_accruals_nivol_lvl_63d_slope_v027_signal,
    f35eq_f35_earnings_quality_accruals_cfvol_lvl_63d_slope_v028_signal,
    f35eq_f35_earnings_quality_accruals_convturn_lvl_63d_slope_v029_signal,
    f35eq_f35_earnings_quality_accruals_wcinth_lvl_63d_slope_v030_signal,
    f35eq_f35_earnings_quality_accruals_recvassetsh_lvl_63d_slope_v031_signal,
    f35eq_f35_earnings_quality_accruals_dsodelta_lvl_63d_slope_v032_signal,
    f35eq_f35_earnings_quality_accruals_sloandelta_lvl_63d_slope_v033_signal,
    f35eq_f35_earnings_quality_accruals_wcdelta_lvl_63d_slope_v034_signal,
    f35eq_f35_earnings_quality_accruals_smooth_lvl_63d_slope_v035_signal,
    f35eq_f35_earnings_quality_accruals_nicfcorr_lvl_63d_slope_v036_signal,
    f35eq_f35_earnings_quality_accruals_growthdso_lvl_63d_slope_v037_signal,
    f35eq_f35_earnings_quality_accruals_growthwc_lvl_63d_slope_v038_signal,
    f35eq_f35_earnings_quality_accruals_qroa_lvl_63d_slope_v039_signal,
    f35eq_f35_earnings_quality_accruals_collrate_lvl_63d_slope_v040_signal,
    f35eq_f35_earnings_quality_accruals_recvgrow_lvl_63d_slope_v041_signal,
    f35eq_f35_earnings_quality_accruals_revgrow_lvl_63d_slope_v042_signal,
    f35eq_f35_earnings_quality_accruals_nigrow_lvl_63d_slope_v043_signal,
    f35eq_f35_earnings_quality_accruals_cfgrow_lvl_63d_slope_v044_signal,
    f35eq_f35_earnings_quality_accruals_assetgrow_lvl_63d_slope_v045_signal,
    f35eq_f35_earnings_quality_accruals_cfcover_lvl_63d_slope_v046_signal,
    f35eq_f35_earnings_quality_accruals_dsorank_lvl_63d_slope_v047_signal,
    f35eq_f35_earnings_quality_accruals_convrank_lvl_63d_slope_v048_signal,
    f35eq_f35_earnings_quality_accruals_cfmarginh_lvl_63d_slope_v049_signal,
    f35eq_f35_earnings_quality_accruals_recvassetz_lvl_63d_slope_v050_signal,
    f35eq_f35_earnings_quality_accruals_sloan_z_21d_slope_v051_signal,
    f35eq_f35_earnings_quality_accruals_sloanrev_z_21d_slope_v052_signal,
    f35eq_f35_earnings_quality_accruals_conv_z_21d_slope_v053_signal,
    f35eq_f35_earnings_quality_accruals_dwc_z_21d_slope_v054_signal,
    f35eq_f35_earnings_quality_accruals_wcint_z_21d_slope_v055_signal,
    f35eq_f35_earnings_quality_accruals_wcrev_z_21d_slope_v056_signal,
    f35eq_f35_earnings_quality_accruals_dso_z_21d_slope_v057_signal,
    f35eq_f35_earnings_quality_accruals_recvassets_z_21d_slope_v058_signal,
    f35eq_f35_earnings_quality_accruals_recvrev_z_21d_slope_v059_signal,
    f35eq_f35_earnings_quality_accruals_cfmargin_z_21d_slope_v060_signal,
    f35eq_f35_earnings_quality_accruals_cfoa_z_21d_slope_v061_signal,
    f35eq_f35_earnings_quality_accruals_roa_z_21d_slope_v062_signal,
    f35eq_f35_earnings_quality_accruals_netmargin_z_21d_slope_v063_signal,
    f35eq_f35_earnings_quality_accruals_turn_z_21d_slope_v064_signal,
    f35eq_f35_earnings_quality_accruals_accvol_z_21d_slope_v065_signal,
    f35eq_f35_earnings_quality_accruals_dsovol_z_21d_slope_v066_signal,
    f35eq_f35_earnings_quality_accruals_convvol_z_21d_slope_v067_signal,
    f35eq_f35_earnings_quality_accruals_cfowc_z_21d_slope_v068_signal,
    f35eq_f35_earnings_quality_accruals_sloanz_z_21d_slope_v069_signal,
    f35eq_f35_earnings_quality_accruals_dsoz_z_21d_slope_v070_signal,
    f35eq_f35_earnings_quality_accruals_wcintz_z_21d_slope_v071_signal,
    f35eq_f35_earnings_quality_accruals_cfmarginz_z_21d_slope_v072_signal,
    f35eq_f35_earnings_quality_accruals_recvrevh_z_21d_slope_v073_signal,
    f35eq_f35_earnings_quality_accruals_dwch_z_21d_slope_v074_signal,
    f35eq_f35_earnings_quality_accruals_revqual_z_21d_slope_v075_signal,
    f35eq_f35_earnings_quality_accruals_accrev_z_21d_slope_v076_signal,
    f35eq_f35_earnings_quality_accruals_nivol_z_21d_slope_v077_signal,
    f35eq_f35_earnings_quality_accruals_cfvol_z_21d_slope_v078_signal,
    f35eq_f35_earnings_quality_accruals_convturn_z_21d_slope_v079_signal,
    f35eq_f35_earnings_quality_accruals_wcinth_z_21d_slope_v080_signal,
    f35eq_f35_earnings_quality_accruals_recvassetsh_z_21d_slope_v081_signal,
    f35eq_f35_earnings_quality_accruals_dsodelta_z_21d_slope_v082_signal,
    f35eq_f35_earnings_quality_accruals_sloandelta_z_21d_slope_v083_signal,
    f35eq_f35_earnings_quality_accruals_wcdelta_z_21d_slope_v084_signal,
    f35eq_f35_earnings_quality_accruals_smooth_z_21d_slope_v085_signal,
    f35eq_f35_earnings_quality_accruals_nicfcorr_z_21d_slope_v086_signal,
    f35eq_f35_earnings_quality_accruals_growthdso_z_21d_slope_v087_signal,
    f35eq_f35_earnings_quality_accruals_growthwc_z_21d_slope_v088_signal,
    f35eq_f35_earnings_quality_accruals_qroa_z_21d_slope_v089_signal,
    f35eq_f35_earnings_quality_accruals_collrate_z_21d_slope_v090_signal,
    f35eq_f35_earnings_quality_accruals_recvgrow_z_21d_slope_v091_signal,
    f35eq_f35_earnings_quality_accruals_revgrow_z_21d_slope_v092_signal,
    f35eq_f35_earnings_quality_accruals_nigrow_z_21d_slope_v093_signal,
    f35eq_f35_earnings_quality_accruals_cfgrow_z_21d_slope_v094_signal,
    f35eq_f35_earnings_quality_accruals_assetgrow_z_21d_slope_v095_signal,
    f35eq_f35_earnings_quality_accruals_cfcover_z_21d_slope_v096_signal,
    f35eq_f35_earnings_quality_accruals_dsorank_z_21d_slope_v097_signal,
    f35eq_f35_earnings_quality_accruals_convrank_z_21d_slope_v098_signal,
    f35eq_f35_earnings_quality_accruals_cfmarginh_z_21d_slope_v099_signal,
    f35eq_f35_earnings_quality_accruals_recvassetz_z_21d_slope_v100_signal,
    f35eq_f35_earnings_quality_accruals_sloan_rk_5d_slope_v101_signal,
    f35eq_f35_earnings_quality_accruals_sloanrev_rk_5d_slope_v102_signal,
    f35eq_f35_earnings_quality_accruals_conv_rk_5d_slope_v103_signal,
    f35eq_f35_earnings_quality_accruals_dwc_rk_5d_slope_v104_signal,
    f35eq_f35_earnings_quality_accruals_wcint_rk_5d_slope_v105_signal,
    f35eq_f35_earnings_quality_accruals_wcrev_rk_5d_slope_v106_signal,
    f35eq_f35_earnings_quality_accruals_dso_rk_5d_slope_v107_signal,
    f35eq_f35_earnings_quality_accruals_recvassets_rk_5d_slope_v108_signal,
    f35eq_f35_earnings_quality_accruals_recvrev_rk_5d_slope_v109_signal,
    f35eq_f35_earnings_quality_accruals_cfmargin_rk_5d_slope_v110_signal,
    f35eq_f35_earnings_quality_accruals_cfoa_rk_5d_slope_v111_signal,
    f35eq_f35_earnings_quality_accruals_roa_rk_5d_slope_v112_signal,
    f35eq_f35_earnings_quality_accruals_netmargin_rk_5d_slope_v113_signal,
    f35eq_f35_earnings_quality_accruals_turn_rk_5d_slope_v114_signal,
    f35eq_f35_earnings_quality_accruals_accvol_rk_5d_slope_v115_signal,
    f35eq_f35_earnings_quality_accruals_dsovol_rk_5d_slope_v116_signal,
    f35eq_f35_earnings_quality_accruals_convvol_rk_5d_slope_v117_signal,
    f35eq_f35_earnings_quality_accruals_cfowc_rk_5d_slope_v118_signal,
    f35eq_f35_earnings_quality_accruals_sloanz_rk_5d_slope_v119_signal,
    f35eq_f35_earnings_quality_accruals_dsoz_rk_5d_slope_v120_signal,
    f35eq_f35_earnings_quality_accruals_wcintz_rk_5d_slope_v121_signal,
    f35eq_f35_earnings_quality_accruals_cfmarginz_rk_5d_slope_v122_signal,
    f35eq_f35_earnings_quality_accruals_recvrevh_rk_5d_slope_v123_signal,
    f35eq_f35_earnings_quality_accruals_dwch_rk_5d_slope_v124_signal,
    f35eq_f35_earnings_quality_accruals_revqual_rk_5d_slope_v125_signal,
    f35eq_f35_earnings_quality_accruals_accrev_rk_5d_slope_v126_signal,
    f35eq_f35_earnings_quality_accruals_nivol_rk_5d_slope_v127_signal,
    f35eq_f35_earnings_quality_accruals_cfvol_rk_5d_slope_v128_signal,
    f35eq_f35_earnings_quality_accruals_convturn_rk_5d_slope_v129_signal,
    f35eq_f35_earnings_quality_accruals_wcinth_rk_5d_slope_v130_signal,
    f35eq_f35_earnings_quality_accruals_recvassetsh_rk_5d_slope_v131_signal,
    f35eq_f35_earnings_quality_accruals_dsodelta_rk_5d_slope_v132_signal,
    f35eq_f35_earnings_quality_accruals_sloandelta_rk_5d_slope_v133_signal,
    f35eq_f35_earnings_quality_accruals_wcdelta_rk_5d_slope_v134_signal,
    f35eq_f35_earnings_quality_accruals_smooth_rk_5d_slope_v135_signal,
    f35eq_f35_earnings_quality_accruals_nicfcorr_rk_5d_slope_v136_signal,
    f35eq_f35_earnings_quality_accruals_growthdso_rk_5d_slope_v137_signal,
    f35eq_f35_earnings_quality_accruals_growthwc_rk_5d_slope_v138_signal,
    f35eq_f35_earnings_quality_accruals_qroa_rk_5d_slope_v139_signal,
    f35eq_f35_earnings_quality_accruals_collrate_rk_5d_slope_v140_signal,
    f35eq_f35_earnings_quality_accruals_recvgrow_rk_5d_slope_v141_signal,
    f35eq_f35_earnings_quality_accruals_revgrow_rk_5d_slope_v142_signal,
    f35eq_f35_earnings_quality_accruals_nigrow_rk_5d_slope_v143_signal,
    f35eq_f35_earnings_quality_accruals_cfgrow_rk_5d_slope_v144_signal,
    f35eq_f35_earnings_quality_accruals_assetgrow_rk_5d_slope_v145_signal,
    f35eq_f35_earnings_quality_accruals_cfcover_rk_5d_slope_v146_signal,
    f35eq_f35_earnings_quality_accruals_dsorank_rk_5d_slope_v147_signal,
    f35eq_f35_earnings_quality_accruals_convrank_rk_5d_slope_v148_signal,
    f35eq_f35_earnings_quality_accruals_cfmarginh_rk_5d_slope_v149_signal,
    f35eq_f35_earnings_quality_accruals_recvassetz_rk_5d_slope_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F35_EARNINGS_QUALITY_ACCRUALS_REGISTRY_001_150 = REGISTRY


def _fund(seed, n, base=1e8, drift=0.02, vol=0.05, allow_neg=False):
    g = np.random.default_rng(seed)
    steps = np.repeat(g.normal(drift, vol, n // 63 + 1), 63)[:n]
    s = base * np.exp(np.cumsum(steps / 63))
    if allow_neg:
        s = s - base * 0.3
    return pd.Series(s, name=None)


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    netinc = _fund(101, n, base=2e7, drift=0.02, vol=0.06, allow_neg=True).rename("netinc")
    ncfo = _fund(102, n, base=2.5e7, drift=0.02, vol=0.05, allow_neg=True).rename("ncfo")
    assets = _fund(103, n, base=5e8, drift=0.015, vol=0.03).rename("assets")
    receivables = _fund(104, n, base=8e7, drift=0.02, vol=0.05).rename("receivables")
    revenue = _fund(105, n, base=3e8, drift=0.02, vol=0.04).rename("revenue")
    workingcapital = _fund(106, n, base=6e7, drift=0.015, vol=0.06, allow_neg=True).rename("workingcapital")

    cols = {"netinc": netinc, "ncfo": ncfo, "assets": assets,
            "receivables": receivables, "revenue": revenue,
            "workingcapital": workingcapital}

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

    print("OK f35_earnings_quality_accruals_2nd_derivatives_001_150_claude: %d features pass" % n_features)
