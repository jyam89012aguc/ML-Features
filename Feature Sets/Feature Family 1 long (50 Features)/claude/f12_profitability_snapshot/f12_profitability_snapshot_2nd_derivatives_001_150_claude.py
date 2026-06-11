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


def _slope_diff_norm(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)


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


# 5d slope of 21d gross margin x closeadj
def f12ps_f12_profitability_snapshot_grossmargin_21d_slope_v001_signal(gp, revenue, closeadj):
    base = _mean(_f12_margin_gross(gp, revenue), 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d gross margin x closeadj
def f12ps_f12_profitability_snapshot_grossmargin_21d_slope_v002_signal(gp, revenue, closeadj):
    base = _mean(_f12_margin_gross(gp, revenue), 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d gross margin x closeadj
def f12ps_f12_profitability_snapshot_grossmargin_63d_slope_v003_signal(gp, revenue, closeadj):
    base = _mean(_f12_margin_gross(gp, revenue), 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d gross margin x closeadj
def f12ps_f12_profitability_snapshot_grossmargin_63d_slope_v004_signal(gp, revenue, closeadj):
    base = _mean(_f12_margin_gross(gp, revenue), 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d gross margin x closeadj
def f12ps_f12_profitability_snapshot_grossmargin_252d_slope_v005_signal(gp, revenue, closeadj):
    base = _mean(_f12_margin_gross(gp, revenue), 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d gross margin x closeadj
def f12ps_f12_profitability_snapshot_grossmargin_252d_slope_v006_signal(gp, revenue, closeadj):
    base = _mean(_f12_margin_gross(gp, revenue), 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d gross margin x closeadj
def f12ps_f12_profitability_snapshot_grossmargin_504d_slope_v007_signal(gp, revenue, closeadj):
    base = _mean(_f12_margin_gross(gp, revenue), 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d operating margin x closeadj
def f12ps_f12_profitability_snapshot_opmargin_21d_slope_v008_signal(opinc, revenue, closeadj):
    base = _mean(_f12_margin_op(opinc, revenue), 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d operating margin x closeadj
def f12ps_f12_profitability_snapshot_opmargin_21d_slope_v009_signal(opinc, revenue, closeadj):
    base = _mean(_f12_margin_op(opinc, revenue), 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d operating margin x closeadj
def f12ps_f12_profitability_snapshot_opmargin_63d_slope_v010_signal(opinc, revenue, closeadj):
    base = _mean(_f12_margin_op(opinc, revenue), 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d operating margin x closeadj
def f12ps_f12_profitability_snapshot_opmargin_252d_slope_v011_signal(opinc, revenue, closeadj):
    base = _mean(_f12_margin_op(opinc, revenue), 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d operating margin x closeadj
def f12ps_f12_profitability_snapshot_opmargin_504d_slope_v012_signal(opinc, revenue, closeadj):
    base = _mean(_f12_margin_op(opinc, revenue), 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d net margin x closeadj
def f12ps_f12_profitability_snapshot_netmargin_21d_slope_v013_signal(netinc, revenue, closeadj):
    base = _mean(_f12_margin_net(netinc, revenue), 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d net margin x closeadj
def f12ps_f12_profitability_snapshot_netmargin_21d_slope_v014_signal(netinc, revenue, closeadj):
    base = _mean(_f12_margin_net(netinc, revenue), 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d net margin x closeadj
def f12ps_f12_profitability_snapshot_netmargin_63d_slope_v015_signal(netinc, revenue, closeadj):
    base = _mean(_f12_margin_net(netinc, revenue), 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d net margin x closeadj
def f12ps_f12_profitability_snapshot_netmargin_252d_slope_v016_signal(netinc, revenue, closeadj):
    base = _mean(_f12_margin_net(netinc, revenue), 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d net margin x closeadj
def f12ps_f12_profitability_snapshot_netmargin_504d_slope_v017_signal(netinc, revenue, closeadj):
    base = _mean(_f12_margin_net(netinc, revenue), 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d ROE x closeadj
def f12ps_f12_profitability_snapshot_roe_63d_slope_v018_signal(netinc, equity, closeadj):
    base = _mean(_f12_profitability_roe(netinc, equity), 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d ROE x closeadj
def f12ps_f12_profitability_snapshot_roe_252d_slope_v019_signal(netinc, equity, closeadj):
    base = _mean(_f12_profitability_roe(netinc, equity), 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d ROE x closeadj
def f12ps_f12_profitability_snapshot_roe_504d_slope_v020_signal(netinc, equity, closeadj):
    base = _mean(_f12_profitability_roe(netinc, equity), 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d ROA x closeadj
def f12ps_f12_profitability_snapshot_roa_63d_slope_v021_signal(netinc, assets, closeadj):
    base = _mean(_f12_profitability_roa(netinc, assets), 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d ROA x closeadj
def f12ps_f12_profitability_snapshot_roa_252d_slope_v022_signal(netinc, assets, closeadj):
    base = _mean(_f12_profitability_roa(netinc, assets), 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d ROA x closeadj
def f12ps_f12_profitability_snapshot_roa_504d_slope_v023_signal(netinc, assets, closeadj):
    base = _mean(_f12_profitability_roa(netinc, assets), 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d ebitda margin x closeadj
def f12ps_f12_profitability_snapshot_ebitdamargin_63d_slope_v024_signal(ebitda, revenue, closeadj):
    base = _mean(_f12_profitability_margin(ebitda, revenue), 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d ebitda margin x closeadj
def f12ps_f12_profitability_snapshot_ebitdamargin_252d_slope_v025_signal(ebitda, revenue, closeadj):
    base = _mean(_f12_profitability_margin(ebitda, revenue), 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d ebitda margin x closeadj
def f12ps_f12_profitability_snapshot_ebitdamargin_504d_slope_v026_signal(ebitda, revenue, closeadj):
    base = _mean(_f12_profitability_margin(ebitda, revenue), 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d gross margin std x closeadj
def f12ps_f12_profitability_snapshot_grossmarginstd_63d_slope_v027_signal(gp, revenue, closeadj):
    base = _std(_f12_margin_gross(gp, revenue), 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d gross margin std x closeadj
def f12ps_f12_profitability_snapshot_grossmarginstd_252d_slope_v028_signal(gp, revenue, closeadj):
    base = _std(_f12_margin_gross(gp, revenue), 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d net margin std x closeadj
def f12ps_f12_profitability_snapshot_netmarginstd_252d_slope_v029_signal(netinc, revenue, closeadj):
    base = _std(_f12_margin_net(netinc, revenue), 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d operating margin std x closeadj
def f12ps_f12_profitability_snapshot_opmarginstd_252d_slope_v030_signal(opinc, revenue, closeadj):
    base = _std(_f12_margin_op(opinc, revenue), 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of gross margin z 252d x closeadj
def f12ps_f12_profitability_snapshot_grossmarginz_252d_slope_v031_signal(gp, revenue, closeadj):
    base = _z(_f12_margin_gross(gp, revenue), 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of operating margin z 252d x closeadj
def f12ps_f12_profitability_snapshot_opmarginz_252d_slope_v032_signal(opinc, revenue, closeadj):
    base = _z(_f12_margin_op(opinc, revenue), 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of net margin z 252d x closeadj
def f12ps_f12_profitability_snapshot_netmarginz_252d_slope_v033_signal(netinc, revenue, closeadj):
    base = _z(_f12_margin_net(netinc, revenue), 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of ROE z 252d x closeadj
def f12ps_f12_profitability_snapshot_roez_252d_slope_v034_signal(netinc, equity, closeadj):
    base = _z(_f12_profitability_roe(netinc, equity), 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of ROA z 252d x closeadj
def f12ps_f12_profitability_snapshot_roaz_252d_slope_v035_signal(netinc, assets, closeadj):
    base = _z(_f12_profitability_roa(netinc, assets), 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of gross margin z 504d x closeadj
def f12ps_f12_profitability_snapshot_grossmarginz_504d_slope_v036_signal(gp, revenue, closeadj):
    base = _z(_f12_margin_gross(gp, revenue), 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of gross margin x rev 63d
def f12ps_f12_profitability_snapshot_grossmarginxrev_63d_slope_v037_signal(gp, revenue, closeadj):
    base = _mean(_f12_margin_gross(gp, revenue) * revenue, 63) * closeadj * 1e-6
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of op margin x rev 63d
def f12ps_f12_profitability_snapshot_opmarginxrev_63d_slope_v038_signal(opinc, revenue, closeadj):
    base = _mean(_f12_margin_op(opinc, revenue) * revenue, 63) * closeadj * 1e-6
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of net margin x rev 63d
def f12ps_f12_profitability_snapshot_netmarginxrev_63d_slope_v039_signal(netinc, revenue, closeadj):
    base = _mean(_f12_margin_net(netinc, revenue) * revenue, 63) * closeadj * 1e-6
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of net margin x rev 252d
def f12ps_f12_profitability_snapshot_netmarginxrev_252d_slope_v040_signal(netinc, revenue, closeadj):
    base = _mean(_f12_margin_net(netinc, revenue) * revenue, 252) * closeadj * 1e-6
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of net margin sq 63d
def f12ps_f12_profitability_snapshot_netmarginsq_63d_slope_v041_signal(netinc, revenue, closeadj):
    nm = _f12_margin_net(netinc, revenue)
    base = _mean(nm * nm.abs(), 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of net margin sq 252d
def f12ps_f12_profitability_snapshot_netmarginsq_252d_slope_v042_signal(netinc, revenue, closeadj):
    nm = _f12_margin_net(netinc, revenue)
    base = _mean(nm * nm.abs(), 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of gross margin sq 252d
def f12ps_f12_profitability_snapshot_grossmarginsq_252d_slope_v043_signal(gp, revenue, closeadj):
    gm = _f12_margin_gross(gp, revenue)
    base = _mean(gm * gm.abs(), 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of ROE x assets 252d
def f12ps_f12_profitability_snapshot_roexassets_252d_slope_v044_signal(netinc, equity, assets, closeadj):
    base = _mean(_f12_profitability_roe(netinc, equity) * np.log(assets.abs().replace(0, np.nan)), 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of ROA x equity 252d
def f12ps_f12_profitability_snapshot_roaxequity_252d_slope_v045_signal(netinc, assets, equity, closeadj):
    base = _mean(_f12_profitability_roa(netinc, assets) * np.log(equity.abs().replace(0, np.nan)), 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of ROE-ROA spread 63d
def f12ps_f12_profitability_snapshot_roeminusroa_63d_slope_v046_signal(netinc, equity, assets, closeadj):
    base = _mean(_f12_profitability_roe(netinc, equity) - _f12_profitability_roa(netinc, assets), 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of ROE-ROA spread 252d
def f12ps_f12_profitability_snapshot_roeminusroa_252d_slope_v047_signal(netinc, equity, assets, closeadj):
    base = _mean(_f12_profitability_roe(netinc, equity) - _f12_profitability_roa(netinc, assets), 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of op-net spread 63d
def f12ps_f12_profitability_snapshot_opminusnet_63d_slope_v048_signal(opinc, netinc, revenue, closeadj):
    base = _mean(_f12_margin_op(opinc, revenue) - _f12_margin_net(netinc, revenue), 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of op-net spread 252d
def f12ps_f12_profitability_snapshot_opminusnet_252d_slope_v049_signal(opinc, netinc, revenue, closeadj):
    base = _mean(_f12_margin_op(opinc, revenue) - _f12_margin_net(netinc, revenue), 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of gross-op spread 63d
def f12ps_f12_profitability_snapshot_grossminusop_63d_slope_v050_signal(gp, opinc, revenue, closeadj):
    base = _mean(_f12_margin_gross(gp, revenue) - _f12_margin_op(opinc, revenue), 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of gross-op spread 252d
def f12ps_f12_profitability_snapshot_grossminusop_252d_slope_v051_signal(gp, opinc, revenue, closeadj):
    base = _mean(_f12_margin_gross(gp, revenue) - _f12_margin_op(opinc, revenue), 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of ni/mc 252d
def f12ps_f12_profitability_snapshot_nitomc_252d_slope_v052_signal(netinc, marketcap, closeadj):
    base = _mean(_f12_profitability_margin(netinc, marketcap), 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of ni/mc 63d
def f12ps_f12_profitability_snapshot_nitomc_63d_slope_v053_signal(netinc, marketcap, closeadj):
    base = _mean(_f12_profitability_margin(netinc, marketcap), 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of ebitda/mc 252d
def f12ps_f12_profitability_snapshot_ebitdatomc_252d_slope_v054_signal(ebitda, marketcap, closeadj):
    base = _mean(_f12_profitability_margin(ebitda, marketcap), 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of gp/mc 252d
def f12ps_f12_profitability_snapshot_gptomc_252d_slope_v055_signal(gp, marketcap, closeadj):
    base = _mean(_f12_profitability_margin(gp, marketcap), 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of gross margin EMA 252d x closeadj
def f12ps_f12_profitability_snapshot_grossmarginema_252d_slope_v056_signal(gp, revenue, closeadj):
    base = _f12_margin_gross(gp, revenue).ewm(span=252, adjust=False).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of net margin EMA 21d x closeadj
def f12ps_f12_profitability_snapshot_netmarginema_21d_slope_v057_signal(netinc, revenue, closeadj):
    base = _f12_margin_net(netinc, revenue).ewm(span=21, adjust=False).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of op margin EMA 63d x closeadj
def f12ps_f12_profitability_snapshot_opmarginema_63d_slope_v058_signal(opinc, revenue, closeadj):
    base = _f12_margin_op(opinc, revenue).ewm(span=63, adjust=False).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of ROE EMA 252d x closeadj
def f12ps_f12_profitability_snapshot_roeema_252d_slope_v059_signal(netinc, equity, closeadj):
    base = _f12_profitability_roe(netinc, equity).ewm(span=252, adjust=False).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of ROA EMA 252d x closeadj
def f12ps_f12_profitability_snapshot_roaema_252d_slope_v060_signal(netinc, assets, closeadj):
    base = _f12_profitability_roa(netinc, assets).ewm(span=252, adjust=False).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of gross margin median 252d x closeadj
def f12ps_f12_profitability_snapshot_grossmarginmed_252d_slope_v061_signal(gp, revenue, closeadj):
    base = _f12_margin_gross(gp, revenue).rolling(252, min_periods=63).median() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of net margin median 252d x closeadj
def f12ps_f12_profitability_snapshot_netmarginmed_252d_slope_v062_signal(netinc, revenue, closeadj):
    base = _f12_margin_net(netinc, revenue).rolling(252, min_periods=63).median() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of ROE median 252d x closeadj
def f12ps_f12_profitability_snapshot_roemed_252d_slope_v063_signal(netinc, equity, closeadj):
    base = _f12_profitability_roe(netinc, equity).rolling(252, min_periods=63).median() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of gross margin IQR 252d x closeadj
def f12ps_f12_profitability_snapshot_grossmarginiqr_252d_slope_v064_signal(gp, revenue, closeadj):
    base = _f12_margin_gross(gp, revenue)
    q3 = base.rolling(252, min_periods=63).quantile(0.75)
    q1 = base.rolling(252, min_periods=63).quantile(0.25)
    b = (q3 - q1) * closeadj
    result = _slope_diff_norm(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of net margin IQR 252d x closeadj
def f12ps_f12_profitability_snapshot_netmarginiqr_252d_slope_v065_signal(netinc, revenue, closeadj):
    base = _f12_margin_net(netinc, revenue)
    q3 = base.rolling(252, min_periods=63).quantile(0.75)
    q1 = base.rolling(252, min_periods=63).quantile(0.25)
    b = (q3 - q1) * closeadj
    result = _slope_diff_norm(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of gross margin skew 252d x closeadj
def f12ps_f12_profitability_snapshot_grossmarginskew_252d_slope_v066_signal(gp, revenue, closeadj):
    base = _f12_margin_gross(gp, revenue).rolling(252, min_periods=63).skew() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of net margin skew 252d x closeadj
def f12ps_f12_profitability_snapshot_netmarginskew_252d_slope_v067_signal(netinc, revenue, closeadj):
    base = _f12_margin_net(netinc, revenue).rolling(252, min_periods=63).skew() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of ROE skew 252d x closeadj
def f12ps_f12_profitability_snapshot_roeskew_252d_slope_v068_signal(netinc, equity, closeadj):
    base = _f12_profitability_roe(netinc, equity).rolling(252, min_periods=63).skew() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of ROE kurt 252d x closeadj
def f12ps_f12_profitability_snapshot_roekurt_252d_slope_v069_signal(netinc, equity, closeadj):
    base = _f12_profitability_roe(netinc, equity).rolling(252, min_periods=63).kurt() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of gross margin rank 252d x closeadj
def f12ps_f12_profitability_snapshot_grossmarginrank_252d_slope_v070_signal(gp, revenue, closeadj):
    base = _f12_margin_gross(gp, revenue).rolling(252, min_periods=63).rank(pct=True) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of net margin rank 504d x closeadj
def f12ps_f12_profitability_snapshot_netmarginrank_504d_slope_v071_signal(netinc, revenue, closeadj):
    base = _f12_margin_net(netinc, revenue).rolling(504, min_periods=126).rank(pct=True) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of ROE rank 504d x closeadj
def f12ps_f12_profitability_snapshot_roerank_504d_slope_v072_signal(netinc, equity, closeadj):
    base = _f12_profitability_roe(netinc, equity).rolling(504, min_periods=126).rank(pct=True) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of net margin anomaly 252d
def f12ps_f12_profitability_snapshot_netmarginanom_252d_slope_v073_signal(netinc, revenue, closeadj):
    base = _f12_margin_net(netinc, revenue)
    b = (base - _mean(base, 504)) * closeadj
    result = _slope_diff_norm(b, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of gross margin anomaly 252d
def f12ps_f12_profitability_snapshot_grossmarginanom_252d_slope_v074_signal(gp, revenue, closeadj):
    base = _f12_margin_gross(gp, revenue)
    b = (base - _mean(base, 504)) * closeadj
    result = _slope_diff_norm(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of margin sum 63d
def f12ps_f12_profitability_snapshot_marginsum_63d_slope_v075_signal(gp, opinc, netinc, revenue, closeadj):
    s = _f12_margin_gross(gp, revenue) + _f12_margin_op(opinc, revenue) + _f12_margin_net(netinc, revenue)
    base = _mean(s, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of margin sum 252d
def f12ps_f12_profitability_snapshot_marginsum_252d_slope_v076_signal(gp, opinc, netinc, revenue, closeadj):
    s = _f12_margin_gross(gp, revenue) + _f12_margin_op(opinc, revenue) + _f12_margin_net(netinc, revenue)
    base = _mean(s, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of count net margin > 5pct 252d
def f12ps_f12_profitability_snapshot_netmarginabove5_252d_slope_v077_signal(netinc, revenue, closeadj):
    base = _f12_margin_net(netinc, revenue)
    flag = (base > 0.05).astype(float)
    b = flag.rolling(252, min_periods=63).sum() * closeadj
    result = _slope_diff_norm(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of count net margin > 10pct 504d
def f12ps_f12_profitability_snapshot_netmarginabove10_504d_slope_v078_signal(netinc, revenue, closeadj):
    base = _f12_margin_net(netinc, revenue)
    flag = (base > 0.10).astype(float)
    b = flag.rolling(504, min_periods=126).sum() * closeadj
    result = _slope_diff_norm(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of mean ROE × close (504d window)
def f12ps_f12_profitability_snapshot_roeabove10_504d_slope_v079_signal(netinc, equity, closeadj):
    base = _f12_profitability_roe(netinc, equity)
    b = base.rolling(504, min_periods=126).mean() * closeadj
    result = _slope_diff_norm(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of net margin annualized 252d
def f12ps_f12_profitability_snapshot_netmarginann_252d_slope_v080_signal(netinc, revenue, closeadj):
    base = _f12_margin_net(netinc, revenue)
    b = _mean(base, 252) * np.sqrt(252.0) * closeadj
    result = _slope_diff_norm(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of ebitda margin EMA 252d x closeadj
def f12ps_f12_profitability_snapshot_ebitdamarginema_252d_slope_v081_signal(ebitda, revenue, closeadj):
    base = _f12_profitability_margin(ebitda, revenue).ewm(span=252, adjust=False).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of ebitda margin std 63d x closeadj
def f12ps_f12_profitability_snapshot_ebitdamarginstd_63d_slope_v082_signal(ebitda, revenue, closeadj):
    base = _std(_f12_profitability_margin(ebitda, revenue), 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of ebitda margin std 252d x closeadj
def f12ps_f12_profitability_snapshot_ebitdamarginstd_252d_slope_v083_signal(ebitda, revenue, closeadj):
    base = _std(_f12_profitability_margin(ebitda, revenue), 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of ebitda margin z 252d x closeadj
def f12ps_f12_profitability_snapshot_ebitdamarginz_252d_slope_v084_signal(ebitda, revenue, closeadj):
    base = _z(_f12_profitability_margin(ebitda, revenue), 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of ROE std 252d x closeadj
def f12ps_f12_profitability_snapshot_roestd_252d_slope_v085_signal(netinc, equity, closeadj):
    base = _std(_f12_profitability_roe(netinc, equity), 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of ROA std 252d x closeadj
def f12ps_f12_profitability_snapshot_roastd_252d_slope_v086_signal(netinc, assets, closeadj):
    base = _std(_f12_profitability_roa(netinc, assets), 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of ROE z 504d x closeadj
def f12ps_f12_profitability_snapshot_roez_504d_slope_v087_signal(netinc, equity, closeadj):
    base = _z(_f12_profitability_roe(netinc, equity), 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of ROA z 504d x closeadj
def f12ps_f12_profitability_snapshot_roaz_504d_slope_v088_signal(netinc, assets, closeadj):
    base = _z(_f12_profitability_roa(netinc, assets), 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of net margin EMA 252d x closeadj
def f12ps_f12_profitability_snapshot_netmarginema_252d_slope_v089_signal(netinc, revenue, closeadj):
    base = _f12_margin_net(netinc, revenue).ewm(span=252, adjust=False).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of gross margin EMA 21d x closeadj
def f12ps_f12_profitability_snapshot_grossmarginema_21d_slope_v090_signal(gp, revenue, closeadj):
    base = _f12_margin_gross(gp, revenue).ewm(span=21, adjust=False).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of op margin EMA 252d x closeadj
def f12ps_f12_profitability_snapshot_opmarginema_252d_slope_v091_signal(opinc, revenue, closeadj):
    base = _f12_margin_op(opinc, revenue).ewm(span=252, adjust=False).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of ROE EMA 21d x closeadj
def f12ps_f12_profitability_snapshot_roeema_21d_slope_v092_signal(netinc, equity, closeadj):
    base = _f12_profitability_roe(netinc, equity).ewm(span=21, adjust=False).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of ROE EMA 63d x closeadj
def f12ps_f12_profitability_snapshot_roeema_63d_slope_v093_signal(netinc, equity, closeadj):
    base = _f12_profitability_roe(netinc, equity).ewm(span=63, adjust=False).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of ROA EMA 21d x closeadj
def f12ps_f12_profitability_snapshot_roaema_21d_slope_v094_signal(netinc, assets, closeadj):
    base = _f12_profitability_roa(netinc, assets).ewm(span=21, adjust=False).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of ROA EMA 63d x closeadj
def f12ps_f12_profitability_snapshot_roaema_63d_slope_v095_signal(netinc, assets, closeadj):
    base = _f12_profitability_roa(netinc, assets).ewm(span=63, adjust=False).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of gross margin x mc 252d
def f12ps_f12_profitability_snapshot_grossmarginxmc_252d_slope_v096_signal(gp, revenue, marketcap, closeadj):
    base = _mean(_f12_margin_gross(gp, revenue) * np.log(marketcap.abs().replace(0, np.nan)), 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of net margin x mc 252d
def f12ps_f12_profitability_snapshot_netmarginxmc_252d_slope_v097_signal(netinc, revenue, marketcap, closeadj):
    base = _mean(_f12_margin_net(netinc, revenue) * np.log(marketcap.abs().replace(0, np.nan)), 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of ROE x equity 252d
def f12ps_f12_profitability_snapshot_roexequity_252d_slope_v098_signal(netinc, equity, closeadj):
    base = _mean(_f12_profitability_roe(netinc, equity) * np.log(equity.abs().replace(0, np.nan)), 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of ROA x assets 252d
def f12ps_f12_profitability_snapshot_roaxassets_252d_slope_v099_signal(netinc, assets, closeadj):
    base = _mean(_f12_profitability_roa(netinc, assets) * np.log(assets.abs().replace(0, np.nan)), 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of expanding ROE x closeadj
def f12ps_f12_profitability_snapshot_roeexp_slope_v100_signal(netinc, equity, closeadj):
    base = _f12_profitability_roe(netinc, equity).expanding(min_periods=63).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of expanding net margin x closeadj
def f12ps_f12_profitability_snapshot_netmarginexp_slope_v101_signal(netinc, revenue, closeadj):
    base = _f12_margin_net(netinc, revenue).expanding(min_periods=63).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of expanding gross margin x closeadj
def f12ps_f12_profitability_snapshot_grossmarginexp_slope_v102_signal(gp, revenue, closeadj):
    base = _f12_margin_gross(gp, revenue).expanding(min_periods=63).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of gross margin x rev 252d
def f12ps_f12_profitability_snapshot_grossmarginxrev_252d_slope_v103_signal(gp, revenue, closeadj):
    base = _mean(_f12_margin_gross(gp, revenue) * revenue, 252) * closeadj * 1e-6
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of op margin x rev 252d
def f12ps_f12_profitability_snapshot_opmarginxrev_252d_slope_v104_signal(opinc, revenue, closeadj):
    base = _mean(_f12_margin_op(opinc, revenue) * revenue, 252) * closeadj * 1e-6
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of net margin min 63d x closeadj
def f12ps_f12_profitability_snapshot_netmarginmin_63d_slope_v105_signal(netinc, revenue, closeadj):
    base = _f12_margin_net(netinc, revenue).rolling(63, min_periods=21).min() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of net margin max 252d x closeadj
def f12ps_f12_profitability_snapshot_netmarginmax_252d_slope_v106_signal(netinc, revenue, closeadj):
    base = _f12_margin_net(netinc, revenue).rolling(252, min_periods=63).max() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of gross margin min 252d x closeadj
def f12ps_f12_profitability_snapshot_grossmarginmin_252d_slope_v107_signal(gp, revenue, closeadj):
    base = _f12_margin_gross(gp, revenue).rolling(252, min_periods=63).min() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of op margin max 252d x closeadj
def f12ps_f12_profitability_snapshot_opmarginmax_252d_slope_v108_signal(opinc, revenue, closeadj):
    base = _f12_margin_op(opinc, revenue).rolling(252, min_periods=63).max() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of ROE max 252d x closeadj
def f12ps_f12_profitability_snapshot_roemax_252d_slope_v109_signal(netinc, equity, closeadj):
    base = _f12_profitability_roe(netinc, equity).rolling(252, min_periods=63).max() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of ROA max 252d x closeadj
def f12ps_f12_profitability_snapshot_roamax_252d_slope_v110_signal(netinc, assets, closeadj):
    base = _f12_profitability_roa(netinc, assets).rolling(252, min_periods=63).max() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of ROE min 252d x closeadj
def f12ps_f12_profitability_snapshot_roemin_252d_slope_v111_signal(netinc, equity, closeadj):
    base = _f12_profitability_roe(netinc, equity).rolling(252, min_periods=63).min() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of count op margin > 10pct 504d
def f12ps_f12_profitability_snapshot_opmarginabove10_504d_slope_v112_signal(opinc, revenue, closeadj):
    base = _f12_margin_op(opinc, revenue)
    flag = (base > 0.10).astype(float)
    b = flag.rolling(504, min_periods=126).sum() * closeadj
    result = _slope_diff_norm(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of count gross margin > 30pct 504d
def f12ps_f12_profitability_snapshot_grossmarginabove30_504d_slope_v113_signal(gp, revenue, closeadj):
    base = _f12_margin_gross(gp, revenue)
    flag = (base > 0.30).astype(float)
    b = flag.rolling(504, min_periods=126).sum() * closeadj
    result = _slope_diff_norm(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of count ROA > 5pct 252d
def f12ps_f12_profitability_snapshot_roaabove5_252d_slope_v114_signal(netinc, assets, closeadj):
    base = _f12_profitability_roa(netinc, assets)
    b = base.rolling(252, min_periods=63).mean() * closeadj
    result = _slope_diff_norm(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of count net margin > rolling mean 252d
def f12ps_f12_profitability_snapshot_netmarginabovemean_252d_slope_v115_signal(netinc, revenue, closeadj):
    base = _f12_margin_net(netinc, revenue)
    flag = (base > _mean(base, 252)).astype(float)
    b = flag.rolling(252, min_periods=63).sum() * closeadj
    result = _slope_diff_norm(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of ebitda margin 21d x closeadj
def f12ps_f12_profitability_snapshot_ebitdamargin_21d_slope_v116_signal(ebitda, revenue, closeadj):
    base = _mean(_f12_profitability_margin(ebitda, revenue), 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of gp/equity 252d x closeadj
def f12ps_f12_profitability_snapshot_gpeq_252d_slope_v117_signal(gp, equity, closeadj):
    base = _mean(_f12_profitability_margin(gp, equity), 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of gp/assets 252d x closeadj
def f12ps_f12_profitability_snapshot_gpa_252d_slope_v118_signal(gp, assets, closeadj):
    base = _mean(_f12_profitability_margin(gp, assets), 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of opinc/equity 252d x closeadj
def f12ps_f12_profitability_snapshot_opincequity_252d_slope_v119_signal(opinc, equity, closeadj):
    base = _mean(_f12_profitability_margin(opinc, equity), 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of opinc/assets 252d x closeadj
def f12ps_f12_profitability_snapshot_opincassets_252d_slope_v120_signal(opinc, assets, closeadj):
    base = _mean(_f12_profitability_margin(opinc, assets), 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of ebitda/assets 252d x closeadj
def f12ps_f12_profitability_snapshot_ebitdaassets_252d_slope_v121_signal(ebitda, assets, closeadj):
    base = _mean(_f12_profitability_margin(ebitda, assets), 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of ebitda/equity 252d x closeadj
def f12ps_f12_profitability_snapshot_ebitdaequity_252d_slope_v122_signal(ebitda, equity, closeadj):
    base = _mean(_f12_profitability_margin(ebitda, equity), 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of ROE z annualized 252d
def f12ps_f12_profitability_snapshot_roezann_252d_slope_v123_signal(netinc, equity, closeadj):
    base = _z(_f12_profitability_roe(netinc, equity), 252) * np.sqrt(252.0) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of ROA z annualized 252d
def f12ps_f12_profitability_snapshot_roazann_252d_slope_v124_signal(netinc, assets, closeadj):
    base = _z(_f12_profitability_roa(netinc, assets), 252) * np.sqrt(252.0) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of gross margin annualized 252d
def f12ps_f12_profitability_snapshot_grossmarginann_252d_slope_v125_signal(gp, revenue, closeadj):
    base = _mean(_f12_margin_gross(gp, revenue), 252) * np.sqrt(252.0) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of net margin median 504d
def f12ps_f12_profitability_snapshot_netmarginmed_504d_slope_v126_signal(netinc, revenue, closeadj):
    base = _f12_margin_net(netinc, revenue).rolling(504, min_periods=126).median() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of ROE median 504d
def f12ps_f12_profitability_snapshot_roemed_504d_slope_v127_signal(netinc, equity, closeadj):
    base = _f12_profitability_roe(netinc, equity).rolling(504, min_periods=126).median() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of ROA median 504d
def f12ps_f12_profitability_snapshot_roamed_504d_slope_v128_signal(netinc, assets, closeadj):
    base = _f12_profitability_roa(netinc, assets).rolling(504, min_periods=126).median() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of nm x em 252d
def f12ps_f12_profitability_snapshot_nmxem_252d_slope_v129_signal(netinc, ebitda, revenue, closeadj):
    nm = _f12_margin_net(netinc, revenue)
    em = _f12_profitability_margin(ebitda, revenue)
    base = _mean(nm * em, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of gm x em 252d
def f12ps_f12_profitability_snapshot_gmxem_252d_slope_v130_signal(gp, ebitda, revenue, closeadj):
    gm = _f12_margin_gross(gp, revenue)
    em = _f12_profitability_margin(ebitda, revenue)
    base = _mean(gm * em, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of ROE x ROA 63d
def f12ps_f12_profitability_snapshot_roexroa_63d_slope_v131_signal(netinc, equity, assets, closeadj):
    base = _mean(_f12_profitability_roe(netinc, equity) * _f12_profitability_roa(netinc, assets), 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of ROE x ROA 252d
def f12ps_f12_profitability_snapshot_roexroa_252d_slope_v132_signal(netinc, equity, assets, closeadj):
    base = _mean(_f12_profitability_roe(netinc, equity) * _f12_profitability_roa(netinc, assets), 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of gross margin EMA 504d x closeadj
def f12ps_f12_profitability_snapshot_grossmarginema_504d_slope_v133_signal(gp, revenue, closeadj):
    base = _f12_margin_gross(gp, revenue).ewm(span=504, adjust=False).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of net margin EMA 504d x closeadj
def f12ps_f12_profitability_snapshot_netmarginema_504d_slope_v134_signal(netinc, revenue, closeadj):
    base = _f12_margin_net(netinc, revenue).ewm(span=504, adjust=False).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of op margin EMA 504d x closeadj
def f12ps_f12_profitability_snapshot_opmarginema_504d_slope_v135_signal(opinc, revenue, closeadj):
    base = _f12_margin_op(opinc, revenue).ewm(span=504, adjust=False).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of ROE EMA 504d x closeadj
def f12ps_f12_profitability_snapshot_roeema_504d_slope_v136_signal(netinc, equity, closeadj):
    base = _f12_profitability_roe(netinc, equity).ewm(span=504, adjust=False).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of ROA EMA 504d x closeadj
def f12ps_f12_profitability_snapshot_roaema_504d_slope_v137_signal(netinc, assets, closeadj):
    base = _f12_profitability_roa(netinc, assets).ewm(span=504, adjust=False).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of eps proxy 252d
def f12ps_f12_profitability_snapshot_eps_252d_slope_v138_signal(netinc, sharesbas, closeadj):
    base = _mean(_f12_profitability_margin(netinc, sharesbas), 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of eps proxy 21d
def f12ps_f12_profitability_snapshot_eps_21d_slope_v139_signal(netinc, sharesbas, closeadj):
    base = _mean(_f12_profitability_margin(netinc, sharesbas), 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of ni/debt 63d
def f12ps_f12_profitability_snapshot_nidebt_63d_slope_v140_signal(netinc, debt, closeadj):
    base = _mean(_f12_profitability_margin(netinc, debt), 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of ni/debt 252d
def f12ps_f12_profitability_snapshot_nidebt_252d_slope_v141_signal(netinc, debt, closeadj):
    base = _mean(_f12_profitability_margin(netinc, debt), 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of ebitda/debt 252d
def f12ps_f12_profitability_snapshot_ebitdadebt_252d_slope_v142_signal(ebitda, debt, closeadj):
    base = _mean(_f12_profitability_margin(ebitda, debt), 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of ebitda/liab 252d
def f12ps_f12_profitability_snapshot_ebitdaliab_252d_slope_v143_signal(ebitda, liabilities, closeadj):
    base = _mean(_f12_profitability_margin(ebitda, liabilities), 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of ROE x rev 63d
def f12ps_f12_profitability_snapshot_roexrev_63d_slope_v144_signal(netinc, equity, revenue, closeadj):
    base = _mean(_f12_profitability_roe(netinc, equity) * np.log(revenue.abs().replace(0, np.nan)), 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of ROE x rev 252d
def f12ps_f12_profitability_snapshot_roexrev_252d_slope_v145_signal(netinc, equity, revenue, closeadj):
    base = _mean(_f12_profitability_roe(netinc, equity) * np.log(revenue.abs().replace(0, np.nan)), 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of ROA x rev 252d
def f12ps_f12_profitability_snapshot_roaxrev_252d_slope_v146_signal(netinc, assets, revenue, closeadj):
    base = _mean(_f12_profitability_roa(netinc, assets) * np.log(revenue.abs().replace(0, np.nan)), 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of net minus gross 63d
def f12ps_f12_profitability_snapshot_netminusgross_63d_slope_v147_signal(netinc, gp, revenue, closeadj):
    base = _mean(_f12_margin_net(netinc, revenue) - _f12_margin_gross(gp, revenue), 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of net minus gross 252d
def f12ps_f12_profitability_snapshot_netminusgross_252d_slope_v148_signal(netinc, gp, revenue, closeadj):
    base = _mean(_f12_margin_net(netinc, revenue) - _f12_margin_gross(gp, revenue), 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of gm x roe 252d
def f12ps_f12_profitability_snapshot_gmxroe_252d_slope_v149_signal(gp, revenue, netinc, equity, closeadj):
    gm = _f12_margin_gross(gp, revenue)
    roe = _f12_profitability_roe(netinc, equity)
    base = _mean(gm * roe, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of gm x roa 252d
def f12ps_f12_profitability_snapshot_gmxroa_252d_slope_v150_signal(gp, revenue, netinc, assets, closeadj):
    gm = _f12_margin_gross(gp, revenue)
    roa = _f12_profitability_roa(netinc, assets)
    base = _mean(gm * roa, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f12ps_f12_profitability_snapshot_grossmargin_21d_slope_v001_signal,
    f12ps_f12_profitability_snapshot_grossmargin_21d_slope_v002_signal,
    f12ps_f12_profitability_snapshot_grossmargin_63d_slope_v003_signal,
    f12ps_f12_profitability_snapshot_grossmargin_63d_slope_v004_signal,
    f12ps_f12_profitability_snapshot_grossmargin_252d_slope_v005_signal,
    f12ps_f12_profitability_snapshot_grossmargin_252d_slope_v006_signal,
    f12ps_f12_profitability_snapshot_grossmargin_504d_slope_v007_signal,
    f12ps_f12_profitability_snapshot_opmargin_21d_slope_v008_signal,
    f12ps_f12_profitability_snapshot_opmargin_21d_slope_v009_signal,
    f12ps_f12_profitability_snapshot_opmargin_63d_slope_v010_signal,
    f12ps_f12_profitability_snapshot_opmargin_252d_slope_v011_signal,
    f12ps_f12_profitability_snapshot_opmargin_504d_slope_v012_signal,
    f12ps_f12_profitability_snapshot_netmargin_21d_slope_v013_signal,
    f12ps_f12_profitability_snapshot_netmargin_21d_slope_v014_signal,
    f12ps_f12_profitability_snapshot_netmargin_63d_slope_v015_signal,
    f12ps_f12_profitability_snapshot_netmargin_252d_slope_v016_signal,
    f12ps_f12_profitability_snapshot_netmargin_504d_slope_v017_signal,
    f12ps_f12_profitability_snapshot_roe_63d_slope_v018_signal,
    f12ps_f12_profitability_snapshot_roe_252d_slope_v019_signal,
    f12ps_f12_profitability_snapshot_roe_504d_slope_v020_signal,
    f12ps_f12_profitability_snapshot_roa_63d_slope_v021_signal,
    f12ps_f12_profitability_snapshot_roa_252d_slope_v022_signal,
    f12ps_f12_profitability_snapshot_roa_504d_slope_v023_signal,
    f12ps_f12_profitability_snapshot_ebitdamargin_63d_slope_v024_signal,
    f12ps_f12_profitability_snapshot_ebitdamargin_252d_slope_v025_signal,
    f12ps_f12_profitability_snapshot_ebitdamargin_504d_slope_v026_signal,
    f12ps_f12_profitability_snapshot_grossmarginstd_63d_slope_v027_signal,
    f12ps_f12_profitability_snapshot_grossmarginstd_252d_slope_v028_signal,
    f12ps_f12_profitability_snapshot_netmarginstd_252d_slope_v029_signal,
    f12ps_f12_profitability_snapshot_opmarginstd_252d_slope_v030_signal,
    f12ps_f12_profitability_snapshot_grossmarginz_252d_slope_v031_signal,
    f12ps_f12_profitability_snapshot_opmarginz_252d_slope_v032_signal,
    f12ps_f12_profitability_snapshot_netmarginz_252d_slope_v033_signal,
    f12ps_f12_profitability_snapshot_roez_252d_slope_v034_signal,
    f12ps_f12_profitability_snapshot_roaz_252d_slope_v035_signal,
    f12ps_f12_profitability_snapshot_grossmarginz_504d_slope_v036_signal,
    f12ps_f12_profitability_snapshot_grossmarginxrev_63d_slope_v037_signal,
    f12ps_f12_profitability_snapshot_opmarginxrev_63d_slope_v038_signal,
    f12ps_f12_profitability_snapshot_netmarginxrev_63d_slope_v039_signal,
    f12ps_f12_profitability_snapshot_netmarginxrev_252d_slope_v040_signal,
    f12ps_f12_profitability_snapshot_netmarginsq_63d_slope_v041_signal,
    f12ps_f12_profitability_snapshot_netmarginsq_252d_slope_v042_signal,
    f12ps_f12_profitability_snapshot_grossmarginsq_252d_slope_v043_signal,
    f12ps_f12_profitability_snapshot_roexassets_252d_slope_v044_signal,
    f12ps_f12_profitability_snapshot_roaxequity_252d_slope_v045_signal,
    f12ps_f12_profitability_snapshot_roeminusroa_63d_slope_v046_signal,
    f12ps_f12_profitability_snapshot_roeminusroa_252d_slope_v047_signal,
    f12ps_f12_profitability_snapshot_opminusnet_63d_slope_v048_signal,
    f12ps_f12_profitability_snapshot_opminusnet_252d_slope_v049_signal,
    f12ps_f12_profitability_snapshot_grossminusop_63d_slope_v050_signal,
    f12ps_f12_profitability_snapshot_grossminusop_252d_slope_v051_signal,
    f12ps_f12_profitability_snapshot_nitomc_252d_slope_v052_signal,
    f12ps_f12_profitability_snapshot_nitomc_63d_slope_v053_signal,
    f12ps_f12_profitability_snapshot_ebitdatomc_252d_slope_v054_signal,
    f12ps_f12_profitability_snapshot_gptomc_252d_slope_v055_signal,
    f12ps_f12_profitability_snapshot_grossmarginema_252d_slope_v056_signal,
    f12ps_f12_profitability_snapshot_netmarginema_21d_slope_v057_signal,
    f12ps_f12_profitability_snapshot_opmarginema_63d_slope_v058_signal,
    f12ps_f12_profitability_snapshot_roeema_252d_slope_v059_signal,
    f12ps_f12_profitability_snapshot_roaema_252d_slope_v060_signal,
    f12ps_f12_profitability_snapshot_grossmarginmed_252d_slope_v061_signal,
    f12ps_f12_profitability_snapshot_netmarginmed_252d_slope_v062_signal,
    f12ps_f12_profitability_snapshot_roemed_252d_slope_v063_signal,
    f12ps_f12_profitability_snapshot_grossmarginiqr_252d_slope_v064_signal,
    f12ps_f12_profitability_snapshot_netmarginiqr_252d_slope_v065_signal,
    f12ps_f12_profitability_snapshot_grossmarginskew_252d_slope_v066_signal,
    f12ps_f12_profitability_snapshot_netmarginskew_252d_slope_v067_signal,
    f12ps_f12_profitability_snapshot_roeskew_252d_slope_v068_signal,
    f12ps_f12_profitability_snapshot_roekurt_252d_slope_v069_signal,
    f12ps_f12_profitability_snapshot_grossmarginrank_252d_slope_v070_signal,
    f12ps_f12_profitability_snapshot_netmarginrank_504d_slope_v071_signal,
    f12ps_f12_profitability_snapshot_roerank_504d_slope_v072_signal,
    f12ps_f12_profitability_snapshot_netmarginanom_252d_slope_v073_signal,
    f12ps_f12_profitability_snapshot_grossmarginanom_252d_slope_v074_signal,
    f12ps_f12_profitability_snapshot_marginsum_63d_slope_v075_signal,
    f12ps_f12_profitability_snapshot_marginsum_252d_slope_v076_signal,
    f12ps_f12_profitability_snapshot_netmarginabove5_252d_slope_v077_signal,
    f12ps_f12_profitability_snapshot_netmarginabove10_504d_slope_v078_signal,
    f12ps_f12_profitability_snapshot_roeabove10_504d_slope_v079_signal,
    f12ps_f12_profitability_snapshot_netmarginann_252d_slope_v080_signal,
    f12ps_f12_profitability_snapshot_ebitdamarginema_252d_slope_v081_signal,
    f12ps_f12_profitability_snapshot_ebitdamarginstd_63d_slope_v082_signal,
    f12ps_f12_profitability_snapshot_ebitdamarginstd_252d_slope_v083_signal,
    f12ps_f12_profitability_snapshot_ebitdamarginz_252d_slope_v084_signal,
    f12ps_f12_profitability_snapshot_roestd_252d_slope_v085_signal,
    f12ps_f12_profitability_snapshot_roastd_252d_slope_v086_signal,
    f12ps_f12_profitability_snapshot_roez_504d_slope_v087_signal,
    f12ps_f12_profitability_snapshot_roaz_504d_slope_v088_signal,
    f12ps_f12_profitability_snapshot_netmarginema_252d_slope_v089_signal,
    f12ps_f12_profitability_snapshot_grossmarginema_21d_slope_v090_signal,
    f12ps_f12_profitability_snapshot_opmarginema_252d_slope_v091_signal,
    f12ps_f12_profitability_snapshot_roeema_21d_slope_v092_signal,
    f12ps_f12_profitability_snapshot_roeema_63d_slope_v093_signal,
    f12ps_f12_profitability_snapshot_roaema_21d_slope_v094_signal,
    f12ps_f12_profitability_snapshot_roaema_63d_slope_v095_signal,
    f12ps_f12_profitability_snapshot_grossmarginxmc_252d_slope_v096_signal,
    f12ps_f12_profitability_snapshot_netmarginxmc_252d_slope_v097_signal,
    f12ps_f12_profitability_snapshot_roexequity_252d_slope_v098_signal,
    f12ps_f12_profitability_snapshot_roaxassets_252d_slope_v099_signal,
    f12ps_f12_profitability_snapshot_roeexp_slope_v100_signal,
    f12ps_f12_profitability_snapshot_netmarginexp_slope_v101_signal,
    f12ps_f12_profitability_snapshot_grossmarginexp_slope_v102_signal,
    f12ps_f12_profitability_snapshot_grossmarginxrev_252d_slope_v103_signal,
    f12ps_f12_profitability_snapshot_opmarginxrev_252d_slope_v104_signal,
    f12ps_f12_profitability_snapshot_netmarginmin_63d_slope_v105_signal,
    f12ps_f12_profitability_snapshot_netmarginmax_252d_slope_v106_signal,
    f12ps_f12_profitability_snapshot_grossmarginmin_252d_slope_v107_signal,
    f12ps_f12_profitability_snapshot_opmarginmax_252d_slope_v108_signal,
    f12ps_f12_profitability_snapshot_roemax_252d_slope_v109_signal,
    f12ps_f12_profitability_snapshot_roamax_252d_slope_v110_signal,
    f12ps_f12_profitability_snapshot_roemin_252d_slope_v111_signal,
    f12ps_f12_profitability_snapshot_opmarginabove10_504d_slope_v112_signal,
    f12ps_f12_profitability_snapshot_grossmarginabove30_504d_slope_v113_signal,
    f12ps_f12_profitability_snapshot_roaabove5_252d_slope_v114_signal,
    f12ps_f12_profitability_snapshot_netmarginabovemean_252d_slope_v115_signal,
    f12ps_f12_profitability_snapshot_ebitdamargin_21d_slope_v116_signal,
    f12ps_f12_profitability_snapshot_gpeq_252d_slope_v117_signal,
    f12ps_f12_profitability_snapshot_gpa_252d_slope_v118_signal,
    f12ps_f12_profitability_snapshot_opincequity_252d_slope_v119_signal,
    f12ps_f12_profitability_snapshot_opincassets_252d_slope_v120_signal,
    f12ps_f12_profitability_snapshot_ebitdaassets_252d_slope_v121_signal,
    f12ps_f12_profitability_snapshot_ebitdaequity_252d_slope_v122_signal,
    f12ps_f12_profitability_snapshot_roezann_252d_slope_v123_signal,
    f12ps_f12_profitability_snapshot_roazann_252d_slope_v124_signal,
    f12ps_f12_profitability_snapshot_grossmarginann_252d_slope_v125_signal,
    f12ps_f12_profitability_snapshot_netmarginmed_504d_slope_v126_signal,
    f12ps_f12_profitability_snapshot_roemed_504d_slope_v127_signal,
    f12ps_f12_profitability_snapshot_roamed_504d_slope_v128_signal,
    f12ps_f12_profitability_snapshot_nmxem_252d_slope_v129_signal,
    f12ps_f12_profitability_snapshot_gmxem_252d_slope_v130_signal,
    f12ps_f12_profitability_snapshot_roexroa_63d_slope_v131_signal,
    f12ps_f12_profitability_snapshot_roexroa_252d_slope_v132_signal,
    f12ps_f12_profitability_snapshot_grossmarginema_504d_slope_v133_signal,
    f12ps_f12_profitability_snapshot_netmarginema_504d_slope_v134_signal,
    f12ps_f12_profitability_snapshot_opmarginema_504d_slope_v135_signal,
    f12ps_f12_profitability_snapshot_roeema_504d_slope_v136_signal,
    f12ps_f12_profitability_snapshot_roaema_504d_slope_v137_signal,
    f12ps_f12_profitability_snapshot_eps_252d_slope_v138_signal,
    f12ps_f12_profitability_snapshot_eps_21d_slope_v139_signal,
    f12ps_f12_profitability_snapshot_nidebt_63d_slope_v140_signal,
    f12ps_f12_profitability_snapshot_nidebt_252d_slope_v141_signal,
    f12ps_f12_profitability_snapshot_ebitdadebt_252d_slope_v142_signal,
    f12ps_f12_profitability_snapshot_ebitdaliab_252d_slope_v143_signal,
    f12ps_f12_profitability_snapshot_roexrev_63d_slope_v144_signal,
    f12ps_f12_profitability_snapshot_roexrev_252d_slope_v145_signal,
    f12ps_f12_profitability_snapshot_roaxrev_252d_slope_v146_signal,
    f12ps_f12_profitability_snapshot_netminusgross_63d_slope_v147_signal,
    f12ps_f12_profitability_snapshot_netminusgross_252d_slope_v148_signal,
    f12ps_f12_profitability_snapshot_gmxroe_252d_slope_v149_signal,
    f12ps_f12_profitability_snapshot_gmxroa_252d_slope_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F12_PROFITABILITY_SNAPSHOT_REGISTRY_SLOPE = REGISTRY


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
    assert n_features == 150, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print(f"OK f12_profitability_snapshot_2nd_derivatives_001_150_claude: {n_features} features pass")
