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


# ===== folder domain primitives =====
def _f12_profitability_margin(num, denom):
    return num / denom.replace(0, np.nan).abs()


def _f12_margin_gross(gp, revenue):
    return gp / revenue.replace(0, np.nan).abs()


def _f12_margin_op(opinc, revenue):
    return opinc / revenue.replace(0, np.nan).abs()


def _f12_margin_net(netinc, revenue):
    return netinc / revenue.replace(0, np.nan).abs()


def _f12_profitability_roe(netinc, equity):
    return netinc / equity.replace(0, np.nan).abs()


def _f12_profitability_roa(netinc, assets):
    return netinc / assets.replace(0, np.nan).abs()


# 21d gross margin times closeadj
def f12ps_f12_profitability_snapshot_grossmargin_21d_base_v001_signal(gp, revenue, closeadj):
    result = _mean(_f12_margin_gross(gp, revenue), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d gross margin times closeadj
def f12ps_f12_profitability_snapshot_grossmargin_63d_base_v002_signal(gp, revenue, closeadj):
    result = _mean(_f12_margin_gross(gp, revenue), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d gross margin times closeadj
def f12ps_f12_profitability_snapshot_grossmargin_252d_base_v003_signal(gp, revenue, closeadj):
    result = _mean(_f12_margin_gross(gp, revenue), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d gross margin times closeadj
def f12ps_f12_profitability_snapshot_grossmargin_504d_base_v004_signal(gp, revenue, closeadj):
    result = _mean(_f12_margin_gross(gp, revenue), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d operating margin times closeadj
def f12ps_f12_profitability_snapshot_opmargin_21d_base_v005_signal(opinc, revenue, closeadj):
    result = _mean(_f12_margin_op(opinc, revenue), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d operating margin times closeadj
def f12ps_f12_profitability_snapshot_opmargin_63d_base_v006_signal(opinc, revenue, closeadj):
    result = _mean(_f12_margin_op(opinc, revenue), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d operating margin times closeadj
def f12ps_f12_profitability_snapshot_opmargin_252d_base_v007_signal(opinc, revenue, closeadj):
    result = _mean(_f12_margin_op(opinc, revenue), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d operating margin times closeadj
def f12ps_f12_profitability_snapshot_opmargin_504d_base_v008_signal(opinc, revenue, closeadj):
    result = _mean(_f12_margin_op(opinc, revenue), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d net margin times closeadj
def f12ps_f12_profitability_snapshot_netmargin_21d_base_v009_signal(netinc, revenue, closeadj):
    result = _mean(_f12_margin_net(netinc, revenue), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d net margin times closeadj
def f12ps_f12_profitability_snapshot_netmargin_63d_base_v010_signal(netinc, revenue, closeadj):
    result = _mean(_f12_margin_net(netinc, revenue), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d net margin times closeadj
def f12ps_f12_profitability_snapshot_netmargin_252d_base_v011_signal(netinc, revenue, closeadj):
    result = _mean(_f12_margin_net(netinc, revenue), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d net margin times closeadj
def f12ps_f12_profitability_snapshot_netmargin_504d_base_v012_signal(netinc, revenue, closeadj):
    result = _mean(_f12_margin_net(netinc, revenue), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d ROE times closeadj
def f12ps_f12_profitability_snapshot_roe_63d_base_v013_signal(netinc, equity, closeadj):
    result = _mean(_f12_profitability_roe(netinc, equity), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ROE times closeadj
def f12ps_f12_profitability_snapshot_roe_252d_base_v014_signal(netinc, equity, closeadj):
    result = _mean(_f12_profitability_roe(netinc, equity), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d ROE times closeadj
def f12ps_f12_profitability_snapshot_roe_504d_base_v015_signal(netinc, equity, closeadj):
    result = _mean(_f12_profitability_roe(netinc, equity), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d ROA times closeadj
def f12ps_f12_profitability_snapshot_roa_63d_base_v016_signal(netinc, assets, closeadj):
    result = _mean(_f12_profitability_roa(netinc, assets), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ROA times closeadj
def f12ps_f12_profitability_snapshot_roa_252d_base_v017_signal(netinc, assets, closeadj):
    result = _mean(_f12_profitability_roa(netinc, assets), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d ROA times closeadj
def f12ps_f12_profitability_snapshot_roa_504d_base_v018_signal(netinc, assets, closeadj):
    result = _mean(_f12_profitability_roa(netinc, assets), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# ebitda margin 63d times closeadj
def f12ps_f12_profitability_snapshot_ebitdamargin_63d_base_v019_signal(ebitda, revenue, closeadj):
    result = _mean(_f12_profitability_margin(ebitda, revenue), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# ebitda margin 252d times closeadj
def f12ps_f12_profitability_snapshot_ebitdamargin_252d_base_v020_signal(ebitda, revenue, closeadj):
    result = _mean(_f12_profitability_margin(ebitda, revenue), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# ebitda margin 504d times closeadj
def f12ps_f12_profitability_snapshot_ebitdamargin_504d_base_v021_signal(ebitda, revenue, closeadj):
    result = _mean(_f12_profitability_margin(ebitda, revenue), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d gross margin std times closeadj
def f12ps_f12_profitability_snapshot_grossmarginstd_63d_base_v022_signal(gp, revenue, closeadj):
    result = _std(_f12_margin_gross(gp, revenue), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d gross margin std times closeadj
def f12ps_f12_profitability_snapshot_grossmarginstd_252d_base_v023_signal(gp, revenue, closeadj):
    result = _std(_f12_margin_gross(gp, revenue), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d net margin std times closeadj
def f12ps_f12_profitability_snapshot_netmarginstd_252d_base_v024_signal(netinc, revenue, closeadj):
    result = _std(_f12_margin_net(netinc, revenue), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d operating margin std times closeadj
def f12ps_f12_profitability_snapshot_opmarginstd_252d_base_v025_signal(opinc, revenue, closeadj):
    result = _std(_f12_margin_op(opinc, revenue), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# zscore of gross margin over 252d
def f12ps_f12_profitability_snapshot_grossmarginz_252d_base_v026_signal(gp, revenue, closeadj):
    result = _z(_f12_margin_gross(gp, revenue), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# zscore of operating margin over 252d
def f12ps_f12_profitability_snapshot_opmarginz_252d_base_v027_signal(opinc, revenue, closeadj):
    result = _z(_f12_margin_op(opinc, revenue), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# zscore of net margin over 252d
def f12ps_f12_profitability_snapshot_netmarginz_252d_base_v028_signal(netinc, revenue, closeadj):
    result = _z(_f12_margin_net(netinc, revenue), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# zscore of ROE over 252d
def f12ps_f12_profitability_snapshot_roez_252d_base_v029_signal(netinc, equity, closeadj):
    result = _z(_f12_profitability_roe(netinc, equity), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# zscore of ROA over 252d
def f12ps_f12_profitability_snapshot_roaz_252d_base_v030_signal(netinc, assets, closeadj):
    result = _z(_f12_profitability_roa(netinc, assets), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# zscore of gross margin over 504d
def f12ps_f12_profitability_snapshot_grossmarginz_504d_base_v031_signal(gp, revenue, closeadj):
    result = _z(_f12_margin_gross(gp, revenue), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d gross margin x revenue (gp absolute level)
def f12ps_f12_profitability_snapshot_grossmarginxrev_63d_base_v032_signal(gp, revenue, closeadj):
    result = _mean(_f12_margin_gross(gp, revenue) * revenue, 63) * closeadj * 1e-6
    return result.replace([np.inf, -np.inf], np.nan)


# 63d op margin x revenue (op income absolute level)
def f12ps_f12_profitability_snapshot_opmarginxrev_63d_base_v033_signal(opinc, revenue, closeadj):
    result = _mean(_f12_margin_op(opinc, revenue) * revenue, 63) * closeadj * 1e-6
    return result.replace([np.inf, -np.inf], np.nan)


# 63d net margin x revenue (netinc absolute level)
def f12ps_f12_profitability_snapshot_netmarginxrev_63d_base_v034_signal(netinc, revenue, closeadj):
    result = _mean(_f12_margin_net(netinc, revenue) * revenue, 63) * closeadj * 1e-6
    return result.replace([np.inf, -np.inf], np.nan)


# 252d net margin x revenue
def f12ps_f12_profitability_snapshot_netmarginxrev_252d_base_v035_signal(netinc, revenue, closeadj):
    result = _mean(_f12_margin_net(netinc, revenue) * revenue, 252) * closeadj * 1e-6
    return result.replace([np.inf, -np.inf], np.nan)


# 21d net margin squared (severity emphasis) times closeadj
def f12ps_f12_profitability_snapshot_netmarginsq_63d_base_v036_signal(netinc, revenue, closeadj):
    nm = _f12_margin_net(netinc, revenue)
    result = _mean(nm * nm.abs(), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d net margin squared times closeadj
def f12ps_f12_profitability_snapshot_netmarginsq_252d_base_v037_signal(netinc, revenue, closeadj):
    nm = _f12_margin_net(netinc, revenue)
    result = _mean(nm * nm.abs(), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d gross margin squared times closeadj
def f12ps_f12_profitability_snapshot_grossmarginsq_252d_base_v038_signal(gp, revenue, closeadj):
    gm = _f12_margin_gross(gp, revenue)
    result = _mean(gm * gm.abs(), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ROE x assets composite
def f12ps_f12_profitability_snapshot_roexassets_252d_base_v039_signal(netinc, equity, assets, closeadj):
    result = _mean(_f12_profitability_roe(netinc, equity) * np.log(assets.abs().replace(0, np.nan)), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ROA x equity composite
def f12ps_f12_profitability_snapshot_roaxequity_252d_base_v040_signal(netinc, assets, equity, closeadj):
    result = _mean(_f12_profitability_roa(netinc, assets) * np.log(equity.abs().replace(0, np.nan)), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d ROE - ROA spread (financial leverage proxy) times closeadj
def f12ps_f12_profitability_snapshot_roeminusroa_63d_base_v041_signal(netinc, equity, assets, closeadj):
    result = _mean(_f12_profitability_roe(netinc, equity) - _f12_profitability_roa(netinc, assets), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ROE - ROA spread times closeadj
def f12ps_f12_profitability_snapshot_roeminusroa_252d_base_v042_signal(netinc, equity, assets, closeadj):
    result = _mean(_f12_profitability_roe(netinc, equity) - _f12_profitability_roa(netinc, assets), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# operating margin minus net margin (tax/interest gap) 63d
def f12ps_f12_profitability_snapshot_opminusnet_63d_base_v043_signal(opinc, netinc, revenue, closeadj):
    result = _mean(_f12_margin_op(opinc, revenue) - _f12_margin_net(netinc, revenue), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# operating margin minus net margin 252d
def f12ps_f12_profitability_snapshot_opminusnet_252d_base_v044_signal(opinc, netinc, revenue, closeadj):
    result = _mean(_f12_margin_op(opinc, revenue) - _f12_margin_net(netinc, revenue), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# gross margin minus operating margin (sg&a load) 63d
def f12ps_f12_profitability_snapshot_grossminusop_63d_base_v045_signal(gp, opinc, revenue, closeadj):
    result = _mean(_f12_margin_gross(gp, revenue) - _f12_margin_op(opinc, revenue), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# gross margin minus operating margin 252d
def f12ps_f12_profitability_snapshot_grossminusop_252d_base_v046_signal(gp, opinc, revenue, closeadj):
    result = _mean(_f12_margin_gross(gp, revenue) - _f12_margin_op(opinc, revenue), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d net income / marketcap (earnings yield) times closeadj
def f12ps_f12_profitability_snapshot_nitomc_252d_base_v047_signal(netinc, marketcap, closeadj):
    result = _mean(_f12_profitability_margin(netinc, marketcap), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d net income / marketcap
def f12ps_f12_profitability_snapshot_nitomc_63d_base_v048_signal(netinc, marketcap, closeadj):
    result = _mean(_f12_profitability_margin(netinc, marketcap), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ebitda / marketcap times closeadj
def f12ps_f12_profitability_snapshot_ebitdatomc_252d_base_v049_signal(ebitda, marketcap, closeadj):
    result = _mean(_f12_profitability_margin(ebitda, marketcap), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d gross profit / marketcap times closeadj
def f12ps_f12_profitability_snapshot_gptomc_252d_base_v050_signal(gp, marketcap, closeadj):
    result = _mean(_f12_profitability_margin(gp, marketcap), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d gross margin EMA times closeadj
def f12ps_f12_profitability_snapshot_grossmarginema_252d_base_v051_signal(gp, revenue, closeadj):
    base = _f12_margin_gross(gp, revenue)
    result = base.ewm(span=252, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d net margin EMA times closeadj
def f12ps_f12_profitability_snapshot_netmarginema_21d_base_v052_signal(netinc, revenue, closeadj):
    base = _f12_margin_net(netinc, revenue)
    result = base.ewm(span=21, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d operating margin EMA times closeadj
def f12ps_f12_profitability_snapshot_opmarginema_63d_base_v053_signal(opinc, revenue, closeadj):
    base = _f12_margin_op(opinc, revenue)
    result = base.ewm(span=63, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ROE EMA times closeadj
def f12ps_f12_profitability_snapshot_roeema_252d_base_v054_signal(netinc, equity, closeadj):
    base = _f12_profitability_roe(netinc, equity)
    result = base.ewm(span=252, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ROA EMA times closeadj
def f12ps_f12_profitability_snapshot_roaema_252d_base_v055_signal(netinc, assets, closeadj):
    base = _f12_profitability_roa(netinc, assets)
    result = base.ewm(span=252, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d gross margin median times closeadj
def f12ps_f12_profitability_snapshot_grossmarginmed_252d_base_v056_signal(gp, revenue, closeadj):
    base = _f12_margin_gross(gp, revenue)
    result = base.rolling(252, min_periods=63).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d net margin median times closeadj
def f12ps_f12_profitability_snapshot_netmarginmed_252d_base_v057_signal(netinc, revenue, closeadj):
    base = _f12_margin_net(netinc, revenue)
    result = base.rolling(252, min_periods=63).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ROE median times closeadj
def f12ps_f12_profitability_snapshot_roemed_252d_base_v058_signal(netinc, equity, closeadj):
    base = _f12_profitability_roe(netinc, equity)
    result = base.rolling(252, min_periods=63).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d gross margin IQR times closeadj
def f12ps_f12_profitability_snapshot_grossmarginiqr_252d_base_v059_signal(gp, revenue, closeadj):
    base = _f12_margin_gross(gp, revenue)
    q3 = base.rolling(252, min_periods=63).quantile(0.75)
    q1 = base.rolling(252, min_periods=63).quantile(0.25)
    result = (q3 - q1) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d net margin IQR times closeadj
def f12ps_f12_profitability_snapshot_netmarginiqr_252d_base_v060_signal(netinc, revenue, closeadj):
    base = _f12_margin_net(netinc, revenue)
    q3 = base.rolling(252, min_periods=63).quantile(0.75)
    q1 = base.rolling(252, min_periods=63).quantile(0.25)
    result = (q3 - q1) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d gross margin skew times closeadj
def f12ps_f12_profitability_snapshot_grossmarginskew_252d_base_v061_signal(gp, revenue, closeadj):
    base = _f12_margin_gross(gp, revenue)
    result = base.rolling(252, min_periods=63).skew() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d net margin skew times closeadj
def f12ps_f12_profitability_snapshot_netmarginskew_252d_base_v062_signal(netinc, revenue, closeadj):
    base = _f12_margin_net(netinc, revenue)
    result = base.rolling(252, min_periods=63).skew() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ROE skew times closeadj
def f12ps_f12_profitability_snapshot_roeskew_252d_base_v063_signal(netinc, equity, closeadj):
    base = _f12_profitability_roe(netinc, equity)
    result = base.rolling(252, min_periods=63).skew() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ROE kurtosis times closeadj
def f12ps_f12_profitability_snapshot_roekurt_252d_base_v064_signal(netinc, equity, closeadj):
    base = _f12_profitability_roe(netinc, equity)
    result = base.rolling(252, min_periods=63).kurt() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d gross margin rank times closeadj
def f12ps_f12_profitability_snapshot_grossmarginrank_252d_base_v065_signal(gp, revenue, closeadj):
    base = _f12_margin_gross(gp, revenue)
    result = base.rolling(252, min_periods=63).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d net margin rank times closeadj
def f12ps_f12_profitability_snapshot_netmarginrank_504d_base_v066_signal(netinc, revenue, closeadj):
    base = _f12_margin_net(netinc, revenue)
    result = base.rolling(504, min_periods=126).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d ROE rank times closeadj
def f12ps_f12_profitability_snapshot_roerank_504d_base_v067_signal(netinc, equity, closeadj):
    base = _f12_profitability_roe(netinc, equity)
    result = base.rolling(504, min_periods=126).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d net margin minus 504d mean (anomaly) times closeadj
def f12ps_f12_profitability_snapshot_netmarginanom_252d_base_v068_signal(netinc, revenue, closeadj):
    base = _f12_margin_net(netinc, revenue)
    result = (base - _mean(base, 504)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d gross margin minus 504d mean times closeadj
def f12ps_f12_profitability_snapshot_grossmarginanom_252d_base_v069_signal(gp, revenue, closeadj):
    base = _f12_margin_gross(gp, revenue)
    result = (base - _mean(base, 504)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# composite gross+op+net margin sum 63d times closeadj
def f12ps_f12_profitability_snapshot_marginsum_63d_base_v070_signal(gp, opinc, netinc, revenue, closeadj):
    s = _f12_margin_gross(gp, revenue) + _f12_margin_op(opinc, revenue) + _f12_margin_net(netinc, revenue)
    result = _mean(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# composite margin sum 252d times closeadj
def f12ps_f12_profitability_snapshot_marginsum_252d_base_v071_signal(gp, opinc, netinc, revenue, closeadj):
    s = _f12_margin_gross(gp, revenue) + _f12_margin_op(opinc, revenue) + _f12_margin_net(netinc, revenue)
    result = _mean(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d count of days where net margin > 0.05 over 252d times closeadj
def f12ps_f12_profitability_snapshot_netmarginabove5_252d_base_v072_signal(netinc, revenue, closeadj):
    base = _f12_margin_net(netinc, revenue)
    result = (base).rolling(252, min_periods=63).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# count of days net margin > 0.10 over 504d times closeadj
def f12ps_f12_profitability_snapshot_netmarginabove10_504d_base_v073_signal(netinc, revenue, closeadj):
    base = _f12_margin_net(netinc, revenue)
    result = (base).rolling(504, min_periods=126).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d mean ROE × closeadj (continuous)
def f12ps_f12_profitability_snapshot_roeabove10_504d_base_v074_signal(netinc, equity, closeadj):
    base = _f12_profitability_roe(netinc, equity)
    result = base.rolling(504, min_periods=126).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d net margin times sqrt(252) annualized times closeadj
def f12ps_f12_profitability_snapshot_netmarginann_252d_base_v075_signal(netinc, revenue, closeadj):
    base = _f12_margin_net(netinc, revenue)
    result = _mean(base, 252) * np.sqrt(252.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f12ps_f12_profitability_snapshot_grossmargin_21d_base_v001_signal,
    f12ps_f12_profitability_snapshot_grossmargin_63d_base_v002_signal,
    f12ps_f12_profitability_snapshot_grossmargin_252d_base_v003_signal,
    f12ps_f12_profitability_snapshot_grossmargin_504d_base_v004_signal,
    f12ps_f12_profitability_snapshot_opmargin_21d_base_v005_signal,
    f12ps_f12_profitability_snapshot_opmargin_63d_base_v006_signal,
    f12ps_f12_profitability_snapshot_opmargin_252d_base_v007_signal,
    f12ps_f12_profitability_snapshot_opmargin_504d_base_v008_signal,
    f12ps_f12_profitability_snapshot_netmargin_21d_base_v009_signal,
    f12ps_f12_profitability_snapshot_netmargin_63d_base_v010_signal,
    f12ps_f12_profitability_snapshot_netmargin_252d_base_v011_signal,
    f12ps_f12_profitability_snapshot_netmargin_504d_base_v012_signal,
    f12ps_f12_profitability_snapshot_roe_63d_base_v013_signal,
    f12ps_f12_profitability_snapshot_roe_252d_base_v014_signal,
    f12ps_f12_profitability_snapshot_roe_504d_base_v015_signal,
    f12ps_f12_profitability_snapshot_roa_63d_base_v016_signal,
    f12ps_f12_profitability_snapshot_roa_252d_base_v017_signal,
    f12ps_f12_profitability_snapshot_roa_504d_base_v018_signal,
    f12ps_f12_profitability_snapshot_ebitdamargin_63d_base_v019_signal,
    f12ps_f12_profitability_snapshot_ebitdamargin_252d_base_v020_signal,
    f12ps_f12_profitability_snapshot_ebitdamargin_504d_base_v021_signal,
    f12ps_f12_profitability_snapshot_grossmarginstd_63d_base_v022_signal,
    f12ps_f12_profitability_snapshot_grossmarginstd_252d_base_v023_signal,
    f12ps_f12_profitability_snapshot_netmarginstd_252d_base_v024_signal,
    f12ps_f12_profitability_snapshot_opmarginstd_252d_base_v025_signal,
    f12ps_f12_profitability_snapshot_grossmarginz_252d_base_v026_signal,
    f12ps_f12_profitability_snapshot_opmarginz_252d_base_v027_signal,
    f12ps_f12_profitability_snapshot_netmarginz_252d_base_v028_signal,
    f12ps_f12_profitability_snapshot_roez_252d_base_v029_signal,
    f12ps_f12_profitability_snapshot_roaz_252d_base_v030_signal,
    f12ps_f12_profitability_snapshot_grossmarginz_504d_base_v031_signal,
    f12ps_f12_profitability_snapshot_grossmarginxrev_63d_base_v032_signal,
    f12ps_f12_profitability_snapshot_opmarginxrev_63d_base_v033_signal,
    f12ps_f12_profitability_snapshot_netmarginxrev_63d_base_v034_signal,
    f12ps_f12_profitability_snapshot_netmarginxrev_252d_base_v035_signal,
    f12ps_f12_profitability_snapshot_netmarginsq_63d_base_v036_signal,
    f12ps_f12_profitability_snapshot_netmarginsq_252d_base_v037_signal,
    f12ps_f12_profitability_snapshot_grossmarginsq_252d_base_v038_signal,
    f12ps_f12_profitability_snapshot_roexassets_252d_base_v039_signal,
    f12ps_f12_profitability_snapshot_roaxequity_252d_base_v040_signal,
    f12ps_f12_profitability_snapshot_roeminusroa_63d_base_v041_signal,
    f12ps_f12_profitability_snapshot_roeminusroa_252d_base_v042_signal,
    f12ps_f12_profitability_snapshot_opminusnet_63d_base_v043_signal,
    f12ps_f12_profitability_snapshot_opminusnet_252d_base_v044_signal,
    f12ps_f12_profitability_snapshot_grossminusop_63d_base_v045_signal,
    f12ps_f12_profitability_snapshot_grossminusop_252d_base_v046_signal,
    f12ps_f12_profitability_snapshot_nitomc_252d_base_v047_signal,
    f12ps_f12_profitability_snapshot_nitomc_63d_base_v048_signal,
    f12ps_f12_profitability_snapshot_ebitdatomc_252d_base_v049_signal,
    f12ps_f12_profitability_snapshot_gptomc_252d_base_v050_signal,
    f12ps_f12_profitability_snapshot_grossmarginema_252d_base_v051_signal,
    f12ps_f12_profitability_snapshot_netmarginema_21d_base_v052_signal,
    f12ps_f12_profitability_snapshot_opmarginema_63d_base_v053_signal,
    f12ps_f12_profitability_snapshot_roeema_252d_base_v054_signal,
    f12ps_f12_profitability_snapshot_roaema_252d_base_v055_signal,
    f12ps_f12_profitability_snapshot_grossmarginmed_252d_base_v056_signal,
    f12ps_f12_profitability_snapshot_netmarginmed_252d_base_v057_signal,
    f12ps_f12_profitability_snapshot_roemed_252d_base_v058_signal,
    f12ps_f12_profitability_snapshot_grossmarginiqr_252d_base_v059_signal,
    f12ps_f12_profitability_snapshot_netmarginiqr_252d_base_v060_signal,
    f12ps_f12_profitability_snapshot_grossmarginskew_252d_base_v061_signal,
    f12ps_f12_profitability_snapshot_netmarginskew_252d_base_v062_signal,
    f12ps_f12_profitability_snapshot_roeskew_252d_base_v063_signal,
    f12ps_f12_profitability_snapshot_roekurt_252d_base_v064_signal,
    f12ps_f12_profitability_snapshot_grossmarginrank_252d_base_v065_signal,
    f12ps_f12_profitability_snapshot_netmarginrank_504d_base_v066_signal,
    f12ps_f12_profitability_snapshot_roerank_504d_base_v067_signal,
    f12ps_f12_profitability_snapshot_netmarginanom_252d_base_v068_signal,
    f12ps_f12_profitability_snapshot_grossmarginanom_252d_base_v069_signal,
    f12ps_f12_profitability_snapshot_marginsum_63d_base_v070_signal,
    f12ps_f12_profitability_snapshot_marginsum_252d_base_v071_signal,
    f12ps_f12_profitability_snapshot_netmarginabove5_252d_base_v072_signal,
    f12ps_f12_profitability_snapshot_netmarginabove10_504d_base_v073_signal,
    f12ps_f12_profitability_snapshot_roeabove10_504d_base_v074_signal,
    f12ps_f12_profitability_snapshot_netmarginann_252d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F12_PROFITABILITY_SNAPSHOT_REGISTRY_001_075 = REGISTRY


def _build_log_walk(seed_offset, base_val, drift, vol, n):
    rs = np.random.RandomState(42 + seed_offset)
    return base_val * np.exp(np.cumsum(rs.normal(drift, vol, n)))


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    revenue = pd.Series(_build_log_walk(0, 5e8, 0.0003, 0.005, n), name="revenue")
    netinc = pd.Series(_build_log_walk(1, 5e7, 0.0002, 0.008, n), name="netinc")
    fcf = pd.Series(_build_log_walk(2, 4e7, 0.0002, 0.009, n), name="fcf")
    ncfo = pd.Series(_build_log_walk(3, 6e7, 0.0002, 0.008, n), name="ncfo")
    equity = pd.Series(_build_log_walk(4, 1e9, 0.0002, 0.004, n), name="equity")
    debt = pd.Series(_build_log_walk(5, 4e8, 0.0001, 0.005, n), name="debt")
    assets = pd.Series(_build_log_walk(6, 2e9, 0.0002, 0.003, n), name="assets")
    ebitda = pd.Series(_build_log_walk(7, 1.2e8, 0.0002, 0.007, n), name="ebitda")
    capex = pd.Series(_build_log_walk(8, 3e7, 0.0002, 0.01, n), name="capex")
    eps = pd.Series(_build_log_walk(9, 2.0, 0.0002, 0.008, n), name="eps")
    sharesbas = pd.Series(_build_log_walk(10, 5e7, 0.0001, 0.002, n), name="sharesbas")
    opinc = pd.Series(_build_log_walk(11, 8e7, 0.0002, 0.007, n), name="opinc")
    gp = pd.Series(_build_log_walk(12, 2e8, 0.0002, 0.006, n), name="gp")
    workingcapital = pd.Series(_build_log_walk(13, 2e8, 0.0002, 0.006, n), name="workingcapital")
    currentratio = pd.Series(_build_log_walk(14, 1.8, 0.0001, 0.004, n), name="currentratio")
    retearn = pd.Series(_build_log_walk(15, 5e8, 0.0002, 0.005, n), name="retearn")
    intexp = pd.Series(_build_log_walk(17, 1e7, 0.0001, 0.008, n), name="intexp")
    liabilities = pd.Series(_build_log_walk(18, 1e9, 0.0001, 0.004, n), name="liabilities")
    closeadj = pd.Series(_build_log_walk(19, 100.0, 0.0005, 0.02, n), name="closeadj")
    marketcap = closeadj * 1e7
    marketcap.name = "marketcap"

    cols = {
        "revenue": revenue, "netinc": netinc, "fcf": fcf, "ncfo": ncfo,
        "equity": equity, "debt": debt, "assets": assets, "ebitda": ebitda,
        "capex": capex, "eps": eps, "sharesbas": sharesbas, "opinc": opinc,
        "gp": gp, "workingcapital": workingcapital, "currentratio": currentratio,
        "retearn": retearn, "intexp": intexp,
        "liabilities": liabilities, "closeadj": closeadj, "marketcap": marketcap,
    }

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f12_profitability_margin", "_f12_margin_gross", "_f12_margin_op",
                         "_f12_margin_net", "_f12_profitability_roe", "_f12_profitability_roa")
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
    print(f"OK f12_profitability_snapshot_base_001_075_claude: {n_features} features pass")
