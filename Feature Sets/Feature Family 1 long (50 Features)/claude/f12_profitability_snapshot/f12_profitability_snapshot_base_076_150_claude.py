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


# ebitda margin EMA 252d times closeadj
def f12ps_f12_profitability_snapshot_ebitdamarginema_252d_base_v076_signal(ebitda, revenue, closeadj):
    base = _f12_profitability_margin(ebitda, revenue)
    result = base.ewm(span=252, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d ebitda margin std times closeadj
def f12ps_f12_profitability_snapshot_ebitdamarginstd_63d_base_v077_signal(ebitda, revenue, closeadj):
    result = _std(_f12_profitability_margin(ebitda, revenue), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ebitda margin std times closeadj
def f12ps_f12_profitability_snapshot_ebitdamarginstd_252d_base_v078_signal(ebitda, revenue, closeadj):
    result = _std(_f12_profitability_margin(ebitda, revenue), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ebitda margin zscore times closeadj
def f12ps_f12_profitability_snapshot_ebitdamarginz_252d_base_v079_signal(ebitda, revenue, closeadj):
    result = _z(_f12_profitability_margin(ebitda, revenue), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ROE std times closeadj
def f12ps_f12_profitability_snapshot_roestd_252d_base_v080_signal(netinc, equity, closeadj):
    result = _std(_f12_profitability_roe(netinc, equity), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ROA std times closeadj
def f12ps_f12_profitability_snapshot_roastd_252d_base_v081_signal(netinc, assets, closeadj):
    result = _std(_f12_profitability_roa(netinc, assets), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d ROE z times closeadj
def f12ps_f12_profitability_snapshot_roez_504d_base_v082_signal(netinc, equity, closeadj):
    result = _z(_f12_profitability_roe(netinc, equity), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d ROA z times closeadj
def f12ps_f12_profitability_snapshot_roaz_504d_base_v083_signal(netinc, assets, closeadj):
    result = _z(_f12_profitability_roa(netinc, assets), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d net margin EMA times closeadj
def f12ps_f12_profitability_snapshot_netmarginema_252d_base_v084_signal(netinc, revenue, closeadj):
    base = _f12_margin_net(netinc, revenue)
    result = base.ewm(span=252, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d gross margin EMA times closeadj
def f12ps_f12_profitability_snapshot_grossmarginema_21d_base_v085_signal(gp, revenue, closeadj):
    base = _f12_margin_gross(gp, revenue)
    result = base.ewm(span=21, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d operating margin EMA times closeadj
def f12ps_f12_profitability_snapshot_opmarginema_252d_base_v086_signal(opinc, revenue, closeadj):
    base = _f12_margin_op(opinc, revenue)
    result = base.ewm(span=252, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d ROE EMA times closeadj
def f12ps_f12_profitability_snapshot_roeema_21d_base_v087_signal(netinc, equity, closeadj):
    base = _f12_profitability_roe(netinc, equity)
    result = base.ewm(span=21, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d ROE EMA times closeadj
def f12ps_f12_profitability_snapshot_roeema_63d_base_v088_signal(netinc, equity, closeadj):
    base = _f12_profitability_roe(netinc, equity)
    result = base.ewm(span=63, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d ROA EMA times closeadj
def f12ps_f12_profitability_snapshot_roaema_21d_base_v089_signal(netinc, assets, closeadj):
    base = _f12_profitability_roa(netinc, assets)
    result = base.ewm(span=21, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d ROA EMA times closeadj
def f12ps_f12_profitability_snapshot_roaema_63d_base_v090_signal(netinc, assets, closeadj):
    base = _f12_profitability_roa(netinc, assets)
    result = base.ewm(span=63, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d gross margin x marketcap composite times closeadj
def f12ps_f12_profitability_snapshot_grossmarginxmc_252d_base_v091_signal(gp, revenue, marketcap, closeadj):
    base = _f12_margin_gross(gp, revenue)
    result = _mean(base * np.log(marketcap.abs().replace(0, np.nan)), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d net margin x marketcap composite times closeadj
def f12ps_f12_profitability_snapshot_netmarginxmc_252d_base_v092_signal(netinc, revenue, marketcap, closeadj):
    base = _f12_margin_net(netinc, revenue)
    result = _mean(base * np.log(marketcap.abs().replace(0, np.nan)), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ROE x equity composite times closeadj
def f12ps_f12_profitability_snapshot_roexequity_252d_base_v093_signal(netinc, equity, closeadj):
    base = _f12_profitability_roe(netinc, equity)
    result = _mean(base * np.log(equity.abs().replace(0, np.nan)), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ROA x assets composite times closeadj
def f12ps_f12_profitability_snapshot_roaxassets_252d_base_v094_signal(netinc, assets, closeadj):
    base = _f12_profitability_roa(netinc, assets)
    result = _mean(base * np.log(assets.abs().replace(0, np.nan)), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ROE expanding mean times closeadj
def f12ps_f12_profitability_snapshot_roeexp_base_v095_signal(netinc, equity, closeadj):
    base = _f12_profitability_roe(netinc, equity)
    result = base.expanding(min_periods=63).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# net margin expanding mean times closeadj
def f12ps_f12_profitability_snapshot_netmarginexp_base_v096_signal(netinc, revenue, closeadj):
    base = _f12_margin_net(netinc, revenue)
    result = base.expanding(min_periods=63).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# gross margin expanding mean times closeadj
def f12ps_f12_profitability_snapshot_grossmarginexp_base_v097_signal(gp, revenue, closeadj):
    base = _f12_margin_gross(gp, revenue)
    result = base.expanding(min_periods=63).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d gross margin x revenue scale composite
def f12ps_f12_profitability_snapshot_grossmarginxrev_252d_base_v098_signal(gp, revenue, closeadj):
    result = _mean(_f12_margin_gross(gp, revenue) * revenue, 252) * closeadj * 1e-6
    return result.replace([np.inf, -np.inf], np.nan)


# 252d operating margin x revenue
def f12ps_f12_profitability_snapshot_opmarginxrev_252d_base_v099_signal(opinc, revenue, closeadj):
    result = _mean(_f12_margin_op(opinc, revenue) * revenue, 252) * closeadj * 1e-6
    return result.replace([np.inf, -np.inf], np.nan)


# net margin minimum 63d times closeadj
def f12ps_f12_profitability_snapshot_netmarginmin_63d_base_v100_signal(netinc, revenue, closeadj):
    base = _f12_margin_net(netinc, revenue)
    result = base.rolling(63, min_periods=21).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# net margin max 252d times closeadj
def f12ps_f12_profitability_snapshot_netmarginmax_252d_base_v101_signal(netinc, revenue, closeadj):
    base = _f12_margin_net(netinc, revenue)
    result = base.rolling(252, min_periods=63).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# gross margin minimum 252d times closeadj
def f12ps_f12_profitability_snapshot_grossmarginmin_252d_base_v102_signal(gp, revenue, closeadj):
    base = _f12_margin_gross(gp, revenue)
    result = base.rolling(252, min_periods=63).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# operating margin max 252d times closeadj
def f12ps_f12_profitability_snapshot_opmarginmax_252d_base_v103_signal(opinc, revenue, closeadj):
    base = _f12_margin_op(opinc, revenue)
    result = base.rolling(252, min_periods=63).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# ROE max 252d times closeadj
def f12ps_f12_profitability_snapshot_roemax_252d_base_v104_signal(netinc, equity, closeadj):
    base = _f12_profitability_roe(netinc, equity)
    result = base.rolling(252, min_periods=63).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# ROA max 252d times closeadj
def f12ps_f12_profitability_snapshot_roamax_252d_base_v105_signal(netinc, assets, closeadj):
    base = _f12_profitability_roa(netinc, assets)
    result = base.rolling(252, min_periods=63).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# ROE min 252d times closeadj
def f12ps_f12_profitability_snapshot_roemin_252d_base_v106_signal(netinc, equity, closeadj):
    base = _f12_profitability_roe(netinc, equity)
    result = base.rolling(252, min_periods=63).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# count days operating margin > 0.10 over 504d times closeadj
def f12ps_f12_profitability_snapshot_opmarginabove10_504d_base_v107_signal(opinc, revenue, closeadj):
    base = _f12_margin_op(opinc, revenue)
    result = (base).rolling(504, min_periods=126).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# count days gross margin > 0.30 over 504d times closeadj
def f12ps_f12_profitability_snapshot_grossmarginabove30_504d_base_v108_signal(gp, revenue, closeadj):
    base = _f12_margin_gross(gp, revenue)
    result = (base).rolling(504, min_periods=126).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean ROA × closeadj (continuous)
def f12ps_f12_profitability_snapshot_roaabove5_252d_base_v109_signal(netinc, assets, closeadj):
    base = _f12_profitability_roa(netinc, assets)
    result = base.rolling(252, min_periods=63).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# count days net margin > rolling mean 252d
def f12ps_f12_profitability_snapshot_netmarginabovemean_252d_base_v110_signal(netinc, revenue, closeadj):
    base = _f12_margin_net(netinc, revenue)
    flag = (base > _mean(base, 252)).astype(float)
    result = flag.rolling(252, min_periods=63).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d ebitda margin times closeadj
def f12ps_f12_profitability_snapshot_ebitdamargin_21d_base_v111_signal(ebitda, revenue, closeadj):
    result = _mean(_f12_profitability_margin(ebitda, revenue), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d gp/equity (gross profit return on equity) times closeadj
def f12ps_f12_profitability_snapshot_gpeq_252d_base_v112_signal(gp, equity, closeadj):
    result = _mean(_f12_profitability_margin(gp, equity), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d gp/assets (gross profit on assets) times closeadj
def f12ps_f12_profitability_snapshot_gpa_252d_base_v113_signal(gp, assets, closeadj):
    result = _mean(_f12_profitability_margin(gp, assets), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d operating income/equity times closeadj
def f12ps_f12_profitability_snapshot_opincequity_252d_base_v114_signal(opinc, equity, closeadj):
    result = _mean(_f12_profitability_margin(opinc, equity), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d operating income/assets times closeadj
def f12ps_f12_profitability_snapshot_opincassets_252d_base_v115_signal(opinc, assets, closeadj):
    result = _mean(_f12_profitability_margin(opinc, assets), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ebitda/assets times closeadj
def f12ps_f12_profitability_snapshot_ebitdaassets_252d_base_v116_signal(ebitda, assets, closeadj):
    result = _mean(_f12_profitability_margin(ebitda, assets), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ebitda/equity times closeadj
def f12ps_f12_profitability_snapshot_ebitdaequity_252d_base_v117_signal(ebitda, equity, closeadj):
    result = _mean(_f12_profitability_margin(ebitda, equity), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ROE z annualized times closeadj
def f12ps_f12_profitability_snapshot_roezann_252d_base_v118_signal(netinc, equity, closeadj):
    base = _f12_profitability_roe(netinc, equity)
    result = _z(base, 252) * np.sqrt(252.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ROA z annualized times closeadj
def f12ps_f12_profitability_snapshot_roazann_252d_base_v119_signal(netinc, assets, closeadj):
    base = _f12_profitability_roa(netinc, assets)
    result = _z(base, 252) * np.sqrt(252.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d gross margin times sqrt(252) annualized times closeadj
def f12ps_f12_profitability_snapshot_grossmarginann_252d_base_v120_signal(gp, revenue, closeadj):
    base = _f12_margin_gross(gp, revenue)
    result = _mean(base, 252) * np.sqrt(252.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d net margin median times closeadj
def f12ps_f12_profitability_snapshot_netmarginmed_504d_base_v121_signal(netinc, revenue, closeadj):
    base = _f12_margin_net(netinc, revenue)
    result = base.rolling(504, min_periods=126).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d ROE median times closeadj
def f12ps_f12_profitability_snapshot_roemed_504d_base_v122_signal(netinc, equity, closeadj):
    base = _f12_profitability_roe(netinc, equity)
    result = base.rolling(504, min_periods=126).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d ROA median times closeadj
def f12ps_f12_profitability_snapshot_roamed_504d_base_v123_signal(netinc, assets, closeadj):
    base = _f12_profitability_roa(netinc, assets)
    result = base.rolling(504, min_periods=126).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# net margin x ebitda margin composite 252d times closeadj
def f12ps_f12_profitability_snapshot_nmxem_252d_base_v124_signal(netinc, ebitda, revenue, closeadj):
    nm = _f12_margin_net(netinc, revenue)
    em = _f12_profitability_margin(ebitda, revenue)
    result = _mean(nm * em, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d gross margin x ebitda margin composite times closeadj
def f12ps_f12_profitability_snapshot_gmxem_252d_base_v125_signal(gp, ebitda, revenue, closeadj):
    gm = _f12_margin_gross(gp, revenue)
    em = _f12_profitability_margin(ebitda, revenue)
    result = _mean(gm * em, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d ROE x ROA composite times closeadj
def f12ps_f12_profitability_snapshot_roexroa_63d_base_v126_signal(netinc, equity, assets, closeadj):
    result = _mean(_f12_profitability_roe(netinc, equity) * _f12_profitability_roa(netinc, assets), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ROE x ROA composite times closeadj
def f12ps_f12_profitability_snapshot_roexroa_252d_base_v127_signal(netinc, equity, assets, closeadj):
    result = _mean(_f12_profitability_roe(netinc, equity) * _f12_profitability_roa(netinc, assets), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d gross margin EMA times closeadj
def f12ps_f12_profitability_snapshot_grossmarginema_504d_base_v128_signal(gp, revenue, closeadj):
    base = _f12_margin_gross(gp, revenue)
    result = base.ewm(span=504, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d net margin EMA times closeadj
def f12ps_f12_profitability_snapshot_netmarginema_504d_base_v129_signal(netinc, revenue, closeadj):
    base = _f12_margin_net(netinc, revenue)
    result = base.ewm(span=504, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d operating margin EMA times closeadj
def f12ps_f12_profitability_snapshot_opmarginema_504d_base_v130_signal(opinc, revenue, closeadj):
    base = _f12_margin_op(opinc, revenue)
    result = base.ewm(span=504, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d ROE EMA times closeadj
def f12ps_f12_profitability_snapshot_roeema_504d_base_v131_signal(netinc, equity, closeadj):
    base = _f12_profitability_roe(netinc, equity)
    result = base.ewm(span=504, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d ROA EMA times closeadj
def f12ps_f12_profitability_snapshot_roaema_504d_base_v132_signal(netinc, assets, closeadj):
    base = _f12_profitability_roa(netinc, assets)
    result = base.ewm(span=504, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# net income/sharesbas (eps proxy) 252d times closeadj
def f12ps_f12_profitability_snapshot_eps_252d_base_v133_signal(netinc, sharesbas, closeadj):
    result = _mean(_f12_profitability_margin(netinc, sharesbas), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d eps proxy times closeadj
def f12ps_f12_profitability_snapshot_eps_21d_base_v134_signal(netinc, sharesbas, closeadj):
    result = _mean(_f12_profitability_margin(netinc, sharesbas), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d net income / debt (return on debt) times closeadj
def f12ps_f12_profitability_snapshot_nidebt_63d_base_v135_signal(netinc, debt, closeadj):
    result = _mean(_f12_profitability_margin(netinc, debt), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d net income / debt times closeadj
def f12ps_f12_profitability_snapshot_nidebt_252d_base_v136_signal(netinc, debt, closeadj):
    result = _mean(_f12_profitability_margin(netinc, debt), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ebitda / debt (debt service capacity) times closeadj
def f12ps_f12_profitability_snapshot_ebitdadebt_252d_base_v137_signal(ebitda, debt, closeadj):
    result = _mean(_f12_profitability_margin(ebitda, debt), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ebitda / liabilities times closeadj
def f12ps_f12_profitability_snapshot_ebitdaliab_252d_base_v138_signal(ebitda, liabilities, closeadj):
    result = _mean(_f12_profitability_margin(ebitda, liabilities), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d ROE x revenue scale composite (productive capacity)
def f12ps_f12_profitability_snapshot_roexrev_63d_base_v139_signal(netinc, equity, revenue, closeadj):
    base = _f12_profitability_roe(netinc, equity)
    result = _mean(base * np.log(revenue.abs().replace(0, np.nan)), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ROE x revenue scale times closeadj
def f12ps_f12_profitability_snapshot_roexrev_252d_base_v140_signal(netinc, equity, revenue, closeadj):
    base = _f12_profitability_roe(netinc, equity)
    result = _mean(base * np.log(revenue.abs().replace(0, np.nan)), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ROA x revenue scale times closeadj
def f12ps_f12_profitability_snapshot_roaxrev_252d_base_v141_signal(netinc, assets, revenue, closeadj):
    base = _f12_profitability_roa(netinc, assets)
    result = _mean(base * np.log(revenue.abs().replace(0, np.nan)), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# net margin minus gross margin (cost burden) 63d times closeadj
def f12ps_f12_profitability_snapshot_netminusgross_63d_base_v142_signal(netinc, gp, revenue, closeadj):
    result = _mean(_f12_margin_net(netinc, revenue) - _f12_margin_gross(gp, revenue), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d net minus gross margin times closeadj
def f12ps_f12_profitability_snapshot_netminusgross_252d_base_v143_signal(netinc, gp, revenue, closeadj):
    result = _mean(_f12_margin_net(netinc, revenue) - _f12_margin_gross(gp, revenue), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d gross margin x ROE composite times closeadj
def f12ps_f12_profitability_snapshot_gmxroe_252d_base_v144_signal(gp, revenue, netinc, equity, closeadj):
    gm = _f12_margin_gross(gp, revenue)
    roe = _f12_profitability_roe(netinc, equity)
    result = _mean(gm * roe, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d gross margin x ROA composite times closeadj
def f12ps_f12_profitability_snapshot_gmxroa_252d_base_v145_signal(gp, revenue, netinc, assets, closeadj):
    gm = _f12_margin_gross(gp, revenue)
    roa = _f12_profitability_roa(netinc, assets)
    result = _mean(gm * roa, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ROE skew 504d times closeadj
def f12ps_f12_profitability_snapshot_roeskew_504d_base_v146_signal(netinc, equity, closeadj):
    base = _f12_profitability_roe(netinc, equity)
    result = base.rolling(504, min_periods=126).skew() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d net margin skew times closeadj
def f12ps_f12_profitability_snapshot_netmarginskew_504d_base_v147_signal(netinc, revenue, closeadj):
    base = _f12_margin_net(netinc, revenue)
    result = base.rolling(504, min_periods=126).skew() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d gross margin skew times closeadj
def f12ps_f12_profitability_snapshot_grossmarginskew_504d_base_v148_signal(gp, revenue, closeadj):
    base = _f12_margin_gross(gp, revenue)
    result = base.rolling(504, min_periods=126).skew() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d gross margin kurtosis times closeadj
def f12ps_f12_profitability_snapshot_grossmarginkurt_504d_base_v149_signal(gp, revenue, closeadj):
    base = _f12_margin_gross(gp, revenue)
    result = base.rolling(504, min_periods=126).kurt() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d net margin kurtosis times closeadj
def f12ps_f12_profitability_snapshot_netmarginkurt_504d_base_v150_signal(netinc, revenue, closeadj):
    base = _f12_margin_net(netinc, revenue)
    result = base.rolling(504, min_periods=126).kurt() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f12ps_f12_profitability_snapshot_ebitdamarginema_252d_base_v076_signal,
    f12ps_f12_profitability_snapshot_ebitdamarginstd_63d_base_v077_signal,
    f12ps_f12_profitability_snapshot_ebitdamarginstd_252d_base_v078_signal,
    f12ps_f12_profitability_snapshot_ebitdamarginz_252d_base_v079_signal,
    f12ps_f12_profitability_snapshot_roestd_252d_base_v080_signal,
    f12ps_f12_profitability_snapshot_roastd_252d_base_v081_signal,
    f12ps_f12_profitability_snapshot_roez_504d_base_v082_signal,
    f12ps_f12_profitability_snapshot_roaz_504d_base_v083_signal,
    f12ps_f12_profitability_snapshot_netmarginema_252d_base_v084_signal,
    f12ps_f12_profitability_snapshot_grossmarginema_21d_base_v085_signal,
    f12ps_f12_profitability_snapshot_opmarginema_252d_base_v086_signal,
    f12ps_f12_profitability_snapshot_roeema_21d_base_v087_signal,
    f12ps_f12_profitability_snapshot_roeema_63d_base_v088_signal,
    f12ps_f12_profitability_snapshot_roaema_21d_base_v089_signal,
    f12ps_f12_profitability_snapshot_roaema_63d_base_v090_signal,
    f12ps_f12_profitability_snapshot_grossmarginxmc_252d_base_v091_signal,
    f12ps_f12_profitability_snapshot_netmarginxmc_252d_base_v092_signal,
    f12ps_f12_profitability_snapshot_roexequity_252d_base_v093_signal,
    f12ps_f12_profitability_snapshot_roaxassets_252d_base_v094_signal,
    f12ps_f12_profitability_snapshot_roeexp_base_v095_signal,
    f12ps_f12_profitability_snapshot_netmarginexp_base_v096_signal,
    f12ps_f12_profitability_snapshot_grossmarginexp_base_v097_signal,
    f12ps_f12_profitability_snapshot_grossmarginxrev_252d_base_v098_signal,
    f12ps_f12_profitability_snapshot_opmarginxrev_252d_base_v099_signal,
    f12ps_f12_profitability_snapshot_netmarginmin_63d_base_v100_signal,
    f12ps_f12_profitability_snapshot_netmarginmax_252d_base_v101_signal,
    f12ps_f12_profitability_snapshot_grossmarginmin_252d_base_v102_signal,
    f12ps_f12_profitability_snapshot_opmarginmax_252d_base_v103_signal,
    f12ps_f12_profitability_snapshot_roemax_252d_base_v104_signal,
    f12ps_f12_profitability_snapshot_roamax_252d_base_v105_signal,
    f12ps_f12_profitability_snapshot_roemin_252d_base_v106_signal,
    f12ps_f12_profitability_snapshot_opmarginabove10_504d_base_v107_signal,
    f12ps_f12_profitability_snapshot_grossmarginabove30_504d_base_v108_signal,
    f12ps_f12_profitability_snapshot_roaabove5_252d_base_v109_signal,
    f12ps_f12_profitability_snapshot_netmarginabovemean_252d_base_v110_signal,
    f12ps_f12_profitability_snapshot_ebitdamargin_21d_base_v111_signal,
    f12ps_f12_profitability_snapshot_gpeq_252d_base_v112_signal,
    f12ps_f12_profitability_snapshot_gpa_252d_base_v113_signal,
    f12ps_f12_profitability_snapshot_opincequity_252d_base_v114_signal,
    f12ps_f12_profitability_snapshot_opincassets_252d_base_v115_signal,
    f12ps_f12_profitability_snapshot_ebitdaassets_252d_base_v116_signal,
    f12ps_f12_profitability_snapshot_ebitdaequity_252d_base_v117_signal,
    f12ps_f12_profitability_snapshot_roezann_252d_base_v118_signal,
    f12ps_f12_profitability_snapshot_roazann_252d_base_v119_signal,
    f12ps_f12_profitability_snapshot_grossmarginann_252d_base_v120_signal,
    f12ps_f12_profitability_snapshot_netmarginmed_504d_base_v121_signal,
    f12ps_f12_profitability_snapshot_roemed_504d_base_v122_signal,
    f12ps_f12_profitability_snapshot_roamed_504d_base_v123_signal,
    f12ps_f12_profitability_snapshot_nmxem_252d_base_v124_signal,
    f12ps_f12_profitability_snapshot_gmxem_252d_base_v125_signal,
    f12ps_f12_profitability_snapshot_roexroa_63d_base_v126_signal,
    f12ps_f12_profitability_snapshot_roexroa_252d_base_v127_signal,
    f12ps_f12_profitability_snapshot_grossmarginema_504d_base_v128_signal,
    f12ps_f12_profitability_snapshot_netmarginema_504d_base_v129_signal,
    f12ps_f12_profitability_snapshot_opmarginema_504d_base_v130_signal,
    f12ps_f12_profitability_snapshot_roeema_504d_base_v131_signal,
    f12ps_f12_profitability_snapshot_roaema_504d_base_v132_signal,
    f12ps_f12_profitability_snapshot_eps_252d_base_v133_signal,
    f12ps_f12_profitability_snapshot_eps_21d_base_v134_signal,
    f12ps_f12_profitability_snapshot_nidebt_63d_base_v135_signal,
    f12ps_f12_profitability_snapshot_nidebt_252d_base_v136_signal,
    f12ps_f12_profitability_snapshot_ebitdadebt_252d_base_v137_signal,
    f12ps_f12_profitability_snapshot_ebitdaliab_252d_base_v138_signal,
    f12ps_f12_profitability_snapshot_roexrev_63d_base_v139_signal,
    f12ps_f12_profitability_snapshot_roexrev_252d_base_v140_signal,
    f12ps_f12_profitability_snapshot_roaxrev_252d_base_v141_signal,
    f12ps_f12_profitability_snapshot_netminusgross_63d_base_v142_signal,
    f12ps_f12_profitability_snapshot_netminusgross_252d_base_v143_signal,
    f12ps_f12_profitability_snapshot_gmxroe_252d_base_v144_signal,
    f12ps_f12_profitability_snapshot_gmxroa_252d_base_v145_signal,
    f12ps_f12_profitability_snapshot_roeskew_504d_base_v146_signal,
    f12ps_f12_profitability_snapshot_netmarginskew_504d_base_v147_signal,
    f12ps_f12_profitability_snapshot_grossmarginskew_504d_base_v148_signal,
    f12ps_f12_profitability_snapshot_grossmarginkurt_504d_base_v149_signal,
    f12ps_f12_profitability_snapshot_netmarginkurt_504d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F12_PROFITABILITY_SNAPSHOT_REGISTRY_076_150 = REGISTRY


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
    print(f"OK f12_profitability_snapshot_base_076_150_claude: {n_features} features pass")
