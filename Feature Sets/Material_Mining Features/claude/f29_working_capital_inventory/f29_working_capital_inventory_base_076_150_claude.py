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
    return s.rolling(w, min_periods=max(1, w // 4)).rank(pct=True) - 0.5


def _slope(s, w):
    # 1st math derivative: rate of change over w trading days
    return (s - s.shift(w)) / float(w)


# ===== folder domain primitives (working capital / inventory) =====
def _f29_invdays(inventory, cor):
    # commodity stockpile days: inventory relative to cost-of-revenue throughput
    return inventory / cor.replace(0, np.nan)


def _f29_dso(receivables, revenue):
    # days-sales-outstanding proxy: receivables relative to revenue
    return receivables / revenue.replace(0, np.nan)


def _f29_dpo(payables, cor):
    # days-payable-outstanding proxy: payables relative to cost-of-revenue
    return payables / cor.replace(0, np.nan)


def _f29_invrev(inventory, revenue):
    # inventory-to-revenue intensity
    return inventory / revenue.replace(0, np.nan)


def _f29_nwc(receivables, inventory, payables):
    # net working capital = receivables + inventory - payables
    return receivables + inventory - payables


def _f29_ccc(inventory, receivables, payables, revenue, cor):
    # cash-conversion-cycle proxy = inv-days + dso - dpo
    invd = inventory / cor.replace(0, np.nan)
    dso = receivables / revenue.replace(0, np.nan)
    dpo = payables / cor.replace(0, np.nan)
    return invd + dso - dpo


def _f29_wcint(receivables, inventory, payables, revenue):
    # working-capital intensity vs revenue
    nwc = receivables + inventory - payables
    return nwc / revenue.replace(0, np.nan)


def _f29_wcassets(receivables, inventory, payables, assetsc):
    # working-capital share of current assets
    nwc = receivables + inventory - payables
    return nwc / assetsc.replace(0, np.nan)



# ============================================================
# net-working-capital growth over a quarter (capital absorption)
def f29wc_f29_working_capital_inventory_nwcgrowth_63d_base_v076_signal(receivables, inventory, payables):
    nwc = (receivables + inventory - payables)
    ln = np.log(nwc.clip(lower=1.0))
    b = ln - ln.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-working-capital growth year-over-year (cyclical WC build)
def f29wc_f29_working_capital_inventory_nwcgrowth252_252d_base_v077_signal(receivables, inventory, payables):
    nwc = (receivables + inventory - payables)
    ln = np.log(nwc.clip(lower=1.0))
    b = ln - ln.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# stockpile-days position within its 504d range (multi-year stock phase)
def f29wc_f29_working_capital_inventory_invdaysrngpos504_504d_base_v078_signal(inventory, cor):
    r = inventory / cor.replace(0, np.nan)
    hi = _rmax(r, 504)
    lo = _rmin(r, 504)
    b = (r - lo) / (hi - lo).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# DSO position within its 252d range
def f29wc_f29_working_capital_inventory_dsorngpos_252d_base_v079_signal(receivables, revenue):
    r = receivables / revenue.replace(0, np.nan)
    hi = _rmax(r, 252)
    lo = _rmin(r, 252)
    b = (r - lo) / (hi - lo).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# working-capital-intensity percentile-rank vs 504d
def f29wc_f29_working_capital_inventory_wcintrank_504d_base_v080_signal(receivables, inventory, payables, revenue):
    nwc = receivables + inventory - payables
    b = _rank(nwc / revenue.replace(0, np.nan), 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# inventory/revenue percentile-rank vs 504d
def f29wc_f29_working_capital_inventory_invrevrank_504d_base_v081_signal(inventory, revenue):
    b = _rank(inventory / revenue.replace(0, np.nan), 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# stockpile days smoothed over a year (very structural inventory level)
def f29wc_f29_working_capital_inventory_invdayssm252_252d_base_v082_signal(inventory, cor):
    r = np.log1p((inventory / cor.replace(0, np.nan)).clip(lower=0))
    b = r.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# stockpile-days year-scale acceleration (base 2nd-difference over half-years)
def f29wc_f29_working_capital_inventory_invdaysyoyacc_252d_base_v083_signal(inventory, cor):
    r = np.log1p((inventory / cor.replace(0, np.nan)).clip(lower=0))
    d1 = r - r.shift(126)
    b = d1 - d1.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# stockpile-days z-scored vs 126d history
def f29wc_f29_working_capital_inventory_invdaysz126_126d_base_v084_signal(inventory, cor):
    r = np.log1p((inventory / cor.replace(0, np.nan)).clip(lower=0))
    b = _z(r, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# change in stockpile-days swing amplitude (overstock-cyclicality intensifying)
def f29wc_f29_working_capital_inventory_invdaysswing_504d_base_v085_signal(inventory, cor):
    r = np.log1p((inventory / cor.replace(0, np.nan)).clip(lower=0))
    hi = _rmax(r, 252)
    lo = _rmin(r, 252)
    amp = (hi - lo)
    b = amp - amp.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# stockpile-days build off its 504d trough (restocking from lean)
def f29wc_f29_working_capital_inventory_invdaysmindd_504d_base_v086_signal(inventory, cor):
    r = np.log1p((inventory / cor.replace(0, np.nan)).clip(lower=0))
    trough = _rmin(r, 504)
    b = r - trough
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# DSO swing amplitude over a year (collection-period cyclicality)
def f29wc_f29_working_capital_inventory_dsoswing_252d_base_v087_signal(receivables, revenue):
    r = receivables / revenue.replace(0, np.nan)
    hi = _rmax(r, 252)
    lo = _rmin(r, 252)
    b = (hi - lo) / r.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# DSO z-scored vs 126d
def f29wc_f29_working_capital_inventory_dsoz126_126d_base_v088_signal(receivables, revenue):
    r = receivables / revenue.replace(0, np.nan)
    b = _z(r, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# DSO drawdown from 252d peak (collection improvement off worst)
def f29wc_f29_working_capital_inventory_dsodd_252d_base_v089_signal(receivables, revenue):
    r = receivables / revenue.replace(0, np.nan)
    peak = _rmax(r, 252)
    b = r / peak.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# DSO position within its 504d range (multi-year collection-cycle phase)
def f29wc_f29_working_capital_inventory_dsorngpos504_504d_base_v090_signal(receivables, revenue):
    r = receivables / revenue.replace(0, np.nan)
    hi = _rmax(r, 504)
    lo = _rmin(r, 504)
    b = (r - lo) / (hi - lo).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# DPO smoothed over a half-year (structural payment period)
def f29wc_f29_working_capital_inventory_dposm126_126d_base_v091_signal(payables, cor):
    r = payables / cor.replace(0, np.nan)
    b = r.rolling(126, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# DPO percentile-rank vs 504d (supplier-stretch percentile)
def f29wc_f29_working_capital_inventory_dporank_504d_base_v092_signal(payables, cor):
    r = payables / cor.replace(0, np.nan)
    b = _rank(r, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# DPO year-over-year change (lengthening/shortening supplier terms)
def f29wc_f29_working_capital_inventory_dpoyoy_252d_base_v093_signal(payables, cor):
    r = payables / cor.replace(0, np.nan)
    b = r - r.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# inventory/revenue swing amplitude over two years (overstock cyclicality)
def f29wc_f29_working_capital_inventory_invrevswing504_504d_base_v094_signal(inventory, revenue):
    r = inventory / revenue.replace(0, np.nan)
    hi = _rmax(r, 504)
    lo = _rmin(r, 504)
    b = (hi - lo) / r.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# inventory/revenue EMA-smoothed
def f29wc_f29_working_capital_inventory_invrevema_63d_base_v095_signal(inventory, revenue):
    r = inventory / revenue.replace(0, np.nan)
    b = r.ewm(span=63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# inventory/revenue displacement vs slow EMA (acute glut vs chronic)
def f29wc_f29_working_capital_inventory_invrevdisp_63d_base_v096_signal(inventory, revenue):
    r = inventory / revenue.replace(0, np.nan)
    b = r - r.ewm(span=126, min_periods=42).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# inventory/revenue z-scored vs 126d
def f29wc_f29_working_capital_inventory_invrevz126_126d_base_v097_signal(inventory, revenue):
    r = inventory / revenue.replace(0, np.nan)
    b = _z(r, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# change in cash-conversion-cycle swing amplitude (WC cyclicality intensifying)
def f29wc_f29_working_capital_inventory_cccrangeamp_504d_base_v098_signal(inventory, receivables, payables, revenue, cor):
    invd = inventory / cor.replace(0, np.nan)
    dso = receivables / revenue.replace(0, np.nan)
    dpo = payables / cor.replace(0, np.nan)
    ccc = invd + dso - dpo
    amp = _rmax(ccc, 252) - _rmin(ccc, 252)
    b = amp - amp.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash-conversion-cycle EMA-smoothed
def f29wc_f29_working_capital_inventory_cccema_63d_base_v099_signal(inventory, receivables, payables, revenue, cor):
    invd = inventory / cor.replace(0, np.nan)
    dso = receivables / revenue.replace(0, np.nan)
    dpo = payables / cor.replace(0, np.nan)
    b = (invd + dso - dpo).ewm(span=63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash-conversion-cycle z-scored vs 126d
def f29wc_f29_working_capital_inventory_cccz126_126d_base_v100_signal(inventory, receivables, payables, revenue, cor):
    invd = inventory / cor.replace(0, np.nan)
    dso = receivables / revenue.replace(0, np.nan)
    dpo = payables / cor.replace(0, np.nan)
    b = _z(invd + dso - dpo, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash-conversion-cycle build off its 252d trough (WC re-tightening)
def f29wc_f29_working_capital_inventory_cccdd_252d_base_v101_signal(inventory, receivables, payables, revenue, cor):
    invd = inventory / cor.replace(0, np.nan)
    dso = receivables / revenue.replace(0, np.nan)
    dpo = payables / cor.replace(0, np.nan)
    ccc = invd + dso - dpo
    trough = _rmin(ccc, 252)
    b = ccc - trough
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash-conversion-cycle displacement vs slow EMA
def f29wc_f29_working_capital_inventory_cccdisp_63d_base_v102_signal(inventory, receivables, payables, revenue, cor):
    invd = inventory / cor.replace(0, np.nan)
    dso = receivables / revenue.replace(0, np.nan)
    dpo = payables / cor.replace(0, np.nan)
    ccc = invd + dso - dpo
    b = ccc - ccc.ewm(span=126, min_periods=42).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# working-capital-intensity position within its 252d range (WC cycle phase)
def f29wc_f29_working_capital_inventory_wcintrngpos_252d_base_v103_signal(receivables, inventory, payables, revenue):
    nwc = receivables + inventory - payables
    wci = nwc / revenue.replace(0, np.nan)
    hi = _rmax(wci, 252)
    lo = _rmin(wci, 252)
    b = (wci - lo) / (hi - lo).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# working-capital-intensity year-over-year change
def f29wc_f29_working_capital_inventory_wcintyoy_252d_base_v104_signal(receivables, inventory, payables, revenue):
    nwc = receivables + inventory - payables
    wci = nwc / revenue.replace(0, np.nan)
    b = wci - wci.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# working-capital-intensity volatility over a year
def f29wc_f29_working_capital_inventory_wcintvol_252d_base_v105_signal(receivables, inventory, payables, revenue):
    nwc = receivables + inventory - payables
    wci = nwc / revenue.replace(0, np.nan)
    b = wci.rolling(252, min_periods=126).std()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# working-capital/current-assets percentile-rank vs 504d
def f29wc_f29_working_capital_inventory_wcassetsrank_504d_base_v106_signal(receivables, inventory, payables, assetsc):
    nwc = receivables + inventory - payables
    b = _rank(nwc / assetsc.replace(0, np.nan), 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# working-capital/current-assets displacement vs slow EMA
def f29wc_f29_working_capital_inventory_wcassetsdisp_63d_base_v107_signal(receivables, inventory, payables, assetsc):
    nwc = receivables + inventory - payables
    r = nwc / assetsc.replace(0, np.nan)
    b = r - r.ewm(span=126, min_periods=42).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# inventory build: log-inventory change over a half-year
def f29wc_f29_working_capital_inventory_invbuild126_126d_base_v108_signal(inventory):
    li = np.log(inventory.replace(0, np.nan))
    b = li - li.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed inventory-build momentum (persistent stocking trend)
def f29wc_f29_working_capital_inventory_invbuildema_63d_base_v109_signal(inventory):
    li = np.log(inventory.replace(0, np.nan))
    chg = li - li.shift(63)
    b = chg.ewm(span=63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# inventory percentile-rank vs 252d
def f29wc_f29_working_capital_inventory_invrank252_252d_base_v110_signal(inventory):
    b = _rank(inventory, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# coefficient of variation of inventory over a year (stock instability)
def f29wc_f29_working_capital_inventory_invcv_252d_base_v111_signal(inventory):
    m = _mean(inventory, 252)
    sd = _std(inventory, 252)
    b = sd / m.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# inventory swing amplitude over two years (cyclical stocking range)
def f29wc_f29_working_capital_inventory_invswing_504d_base_v112_signal(inventory):
    hi = _rmax(inventory, 504)
    lo = _rmin(inventory, 504)
    b = (hi - lo) / inventory.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# inventory turnover smoothed over a half-year (structural throughput)
def f29wc_f29_working_capital_inventory_turnsm126_126d_base_v113_signal(cor, inventory):
    r = cor / inventory.replace(0, np.nan)
    b = r.rolling(126, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# inventory-turnover swing amplitude over a year (throughput-speed cyclicality)
def f29wc_f29_working_capital_inventory_turnswing_504d_base_v114_signal(cor, inventory):
    r = cor / inventory.replace(0, np.nan)
    hi = _rmax(r, 252)
    lo = _rmin(r, 252)
    b = (hi - lo) / r.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# inventory-turnover trend over a quarter (speeding/slowing throughput)
def f29wc_f29_working_capital_inventory_turntrend_63d_base_v115_signal(cor, inventory):
    r = cor / inventory.replace(0, np.nan)
    b = r - r.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# receivables-turnover trend over a quarter (collection-speed change)
def f29wc_f29_working_capital_inventory_recturntrend_63d_base_v116_signal(revenue, receivables):
    r = revenue / receivables.replace(0, np.nan)
    b = r - r.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# receivables-turnover z-scored vs 252d
def f29wc_f29_working_capital_inventory_recturnz_252d_base_v117_signal(revenue, receivables):
    r = revenue / receivables.replace(0, np.nan)
    b = _z(r, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# payables turnover (cor/payables), smoothed
def f29wc_f29_working_capital_inventory_payturn_63d_base_v118_signal(cor, payables):
    b = (cor / payables.replace(0, np.nan)).rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# inventory build minus throughput growth year-over-year (chronic glut)
def f29wc_f29_working_capital_inventory_buildvscor252_252d_base_v119_signal(inventory, cor):
    li = np.log(inventory.replace(0, np.nan))
    lc = np.log(cor.replace(0, np.nan))
    b = (li - li.shift(252)) - (lc - lc.shift(252))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# inventory build minus revenue growth over a half-year
def f29wc_f29_working_capital_inventory_buildvsrev126_126d_base_v120_signal(inventory, revenue):
    li = np.log(inventory.replace(0, np.nan))
    lr = np.log(revenue.replace(0, np.nan))
    b = (li - li.shift(126)) - (lr - lr.shift(126))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# receivables growth minus revenue growth over a half-year
def f29wc_f29_working_capital_inventory_recvsrev126_126d_base_v121_signal(receivables, revenue):
    lx = np.log(receivables.replace(0, np.nan))
    lr = np.log(revenue.replace(0, np.nan))
    b = (lx - lx.shift(126)) - (lr - lr.shift(126))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# payables growth minus cost growth (supplier-term stretching)
def f29wc_f29_working_capital_inventory_payvscor_63d_base_v122_signal(payables, cor):
    lp = np.log(payables.replace(0, np.nan))
    lc = np.log(cor.replace(0, np.nan))
    b = (lp - lp.shift(63)) - (lc - lc.shift(63))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# inventory share of (inventory+receivables) trade assets, smoothed
def f29wc_f29_working_capital_inventory_invshareassets_63d_base_v123_signal(inventory, receivables, assetsc):
    b = (inventory / (inventory + receivables).replace(0, np.nan)).rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# payables share of gross WC components, smoothed
def f29wc_f29_working_capital_inventory_payshare_63d_base_v124_signal(payables, receivables, inventory):
    g = (receivables + inventory + payables).replace(0, np.nan)
    b = (payables / g).rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# inventory-vs-receivables mix z-scored vs 252d
def f29wc_f29_working_capital_inventory_invmixz_252d_base_v125_signal(inventory, receivables):
    mix = inventory / (inventory + receivables).replace(0, np.nan)
    b = _z(mix, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net trade balance over current assets, smoothed
def f29wc_f29_working_capital_inventory_nettradeassets_63d_base_v126_signal(receivables, payables, assetsc):
    b = ((receivables - payables) / assetsc.replace(0, np.nan)).rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-trade-balance percentile-rank vs 504d
def f29wc_f29_working_capital_inventory_nettraderank_504d_base_v127_signal(receivables, payables, revenue):
    r = (receivables - payables) / revenue.replace(0, np.nan)
    b = _rank(r, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-trade-balance year-over-year change
def f29wc_f29_working_capital_inventory_nettradeyoy_252d_base_v128_signal(receivables, payables, revenue):
    r = (receivables - payables) / revenue.replace(0, np.nan)
    b = r - r.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# payables/inventory smoothed over half-year (supplier-financed stockpile)
def f29wc_f29_working_capital_inventory_payvsinvsm126_126d_base_v129_signal(payables, inventory):
    r = payables / inventory.replace(0, np.nan)
    b = r.rolling(126, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# payables/inventory trend over a quarter
def f29wc_f29_working_capital_inventory_payvsinvtrend_63d_base_v130_signal(payables, inventory):
    r = payables / inventory.replace(0, np.nan)
    b = r - r.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# trend in payables coverage of trade assets (supplier-financing shift)
def f29wc_f29_working_capital_inventory_payvswctrend_126d_base_v131_signal(payables, receivables, inventory):
    nwc = (receivables + inventory).replace(0, np.nan)
    r = payables / nwc
    b = r - r.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# current-assets growth over a quarter
def f29wc_f29_working_capital_inventory_assetscgrowth_63d_base_v132_signal(assetsc):
    la = np.log(assetsc.replace(0, np.nan))
    b = la - la.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# current-assets drawdown from 252d peak (liquidity erosion)
def f29wc_f29_working_capital_inventory_assetscdd_252d_base_v133_signal(assetsc):
    peak = _rmax(assetsc, 252)
    b = assetsc / peak.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# current-asset-turnover z-scored vs 252d
def f29wc_f29_working_capital_inventory_revassetscz_252d_base_v134_signal(revenue, assetsc):
    r = revenue / assetsc.replace(0, np.nan)
    b = _z(r, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# trend in trade-asset share of current assets (current-asset illiquidity shift)
def f29wc_f29_working_capital_inventory_illiquidassetstrend_126d_base_v135_signal(inventory, receivables, assetsc):
    r = (inventory + receivables) / assetsc.replace(0, np.nan)
    b = r - r.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# inventory/revenue term ratio (recent vs structural)
def f29wc_f29_working_capital_inventory_invrevterm_base_v136_signal(inventory, revenue):
    r = inventory / revenue.replace(0, np.nan)
    short = r.rolling(63, min_periods=21).mean()
    long = r.rolling(252, min_periods=126).mean()
    b = short / long.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# working-capital-intensity term spread (recent vs structural)
def f29wc_f29_working_capital_inventory_wcintterm_base_v137_signal(receivables, inventory, payables, revenue):
    nwc = receivables + inventory - payables
    r = nwc / revenue.replace(0, np.nan)
    short = r.rolling(63, min_periods=21).mean()
    long = r.rolling(252, min_periods=126).mean()
    b = short - long
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# inventory-turnover term ratio (recent vs structural throughput)
def f29wc_f29_working_capital_inventory_turnterm_base_v138_signal(cor, inventory):
    r = cor / inventory.replace(0, np.nan)
    short = r.rolling(63, min_periods=21).mean()
    long = r.rolling(252, min_periods=126).mean()
    b = short / long.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# DSO disagreement across short/med/long windows
def f29wc_f29_working_capital_inventory_dsodispmulti_base_v139_signal(receivables, revenue):
    r = receivables / revenue.replace(0, np.nan)
    a = r.rolling(63, min_periods=21).mean()
    b2 = r.rolling(126, min_periods=63).mean()
    c = r.rolling(252, min_periods=126).mean()
    b = pd.concat([a, b2, c], axis=1).std(axis=1)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# stockpile-days range amplitude over two years (overstock cyclicality)
def f29wc_f29_working_capital_inventory_invdaysrangeamp_504d_base_v140_signal(inventory, cor):
    r = np.log1p((inventory / cor.replace(0, np.nan)).clip(lower=0))
    hi = _rmax(r, 504)
    lo = _rmin(r, 504)
    b = hi - lo
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# signed-root of stockpile-days deviation (compressed overstock stress)
def f29wc_f29_working_capital_inventory_invdayssignroot_63d_base_v141_signal(inventory, cor):
    r = inventory / cor.replace(0, np.nan)
    dev = r - r.rolling(252, min_periods=126).mean()
    b = np.sign(dev) * (dev.abs() ** 0.5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# tanh-squashed DSO momentum (bounded collection-period change)
def f29wc_f29_working_capital_inventory_dsotanh_21d_base_v142_signal(receivables, revenue):
    r = receivables / revenue.replace(0, np.nan)
    chg = r - r.shift(21)
    b = np.tanh(15.0 * chg)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# signed-root of inventory/revenue vs typical (overstock extremity)
def f29wc_f29_working_capital_inventory_invrevsignmag_504d_base_v143_signal(inventory, revenue):
    r = inventory / revenue.replace(0, np.nan)
    typ = r.rolling(252, min_periods=126).mean()
    b = np.sign(r - typ) * ((r - typ).abs() ** 0.5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# DSO-to-DPO ratio (collect-slower-than-pay imbalance), smoothed
def f29wc_f29_working_capital_inventory_dsovsdpo_63d_base_v144_signal(receivables, revenue, payables, cor):
    dso = receivables / revenue.replace(0, np.nan)
    dpo = payables / cor.replace(0, np.nan)
    b = (dso / dpo.replace(0, np.nan)).rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# CCC-z x inventory-build interaction (tied-up AND still building)
def f29wc_f29_working_capital_inventory_cccXbuild_63d_base_v145_signal(inventory, receivables, payables, revenue, cor):
    invd = inventory / cor.replace(0, np.nan)
    dso = receivables / revenue.replace(0, np.nan)
    dpo = payables / cor.replace(0, np.nan)
    ccc = invd + dso - dpo
    li = np.log(inventory.replace(0, np.nan))
    build = (li - li.shift(63))
    b = (_z(ccc, 252) * build)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# glut x destock interaction (high inventory now being worked down)
def f29wc_f29_working_capital_inventory_glutXdestock_252d_base_v146_signal(inventory, revenue):
    r = inventory / revenue.replace(0, np.nan)
    glut = (_rank(r, 252)).clip(lower=0)
    li = np.log(inventory.replace(0, np.nan))
    destock = -(li - li.shift(63)).clip(upper=0)
    b = glut * destock
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# time DSO sat in top-quartile (collection-stretch regime) plus depth
def f29wc_f29_working_capital_inventory_dsostretchTime_252d_base_v147_signal(receivables, revenue):
    r = receivables / revenue.replace(0, np.nan)
    p = _rank(r, 252) + 0.5
    stretch = (p > 0.75).astype(float)
    frac = stretch.rolling(252, min_periods=126).mean()
    depth = (p - 0.75).clip(lower=0).rolling(63, min_periods=21).mean()
    b = frac + 2.0 * depth
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fraction of last half-year inventory was rising month-over-month (build streak)
def f29wc_f29_working_capital_inventory_buildstreak_126d_base_v148_signal(inventory):
    li = np.log(inventory.replace(0, np.nan))
    up = (li > li.shift(21)).astype(float)
    b = up.rolling(126, min_periods=42).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# time stockpile-days falling (destocking regime) plus destock depth
def f29wc_f29_working_capital_inventory_destockTime_252d_base_v149_signal(inventory, cor):
    r = inventory / cor.replace(0, np.nan)
    falling = (r < r.shift(21)).astype(float)
    frac = falling.rolling(252, min_periods=126).mean()
    li = np.log(inventory.replace(0, np.nan))
    depth = (-(li - li.shift(21)).clip(upper=0)).rolling(63, min_periods=21).mean()
    b = frac + 3.0 * depth
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fraction of last year working-capital-intensity was rising (tie-up onset)
def f29wc_f29_working_capital_inventory_wcTighteningTime_252d_base_v150_signal(receivables, inventory, payables, revenue):
    nwc = receivables + inventory - payables
    wci = nwc / revenue.replace(0, np.nan)
    tight = (wci > wci.shift(63)).astype(float)
    b = tight.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f29wc_f29_working_capital_inventory_nwcgrowth_63d_base_v076_signal,
    f29wc_f29_working_capital_inventory_nwcgrowth252_252d_base_v077_signal,
    f29wc_f29_working_capital_inventory_invdaysrngpos504_504d_base_v078_signal,
    f29wc_f29_working_capital_inventory_dsorngpos_252d_base_v079_signal,
    f29wc_f29_working_capital_inventory_wcintrank_504d_base_v080_signal,
    f29wc_f29_working_capital_inventory_invrevrank_504d_base_v081_signal,
    f29wc_f29_working_capital_inventory_invdayssm252_252d_base_v082_signal,
    f29wc_f29_working_capital_inventory_invdaysyoyacc_252d_base_v083_signal,
    f29wc_f29_working_capital_inventory_invdaysz126_126d_base_v084_signal,
    f29wc_f29_working_capital_inventory_invdaysswing_504d_base_v085_signal,
    f29wc_f29_working_capital_inventory_invdaysmindd_504d_base_v086_signal,
    f29wc_f29_working_capital_inventory_dsoswing_252d_base_v087_signal,
    f29wc_f29_working_capital_inventory_dsoz126_126d_base_v088_signal,
    f29wc_f29_working_capital_inventory_dsodd_252d_base_v089_signal,
    f29wc_f29_working_capital_inventory_dsorngpos504_504d_base_v090_signal,
    f29wc_f29_working_capital_inventory_dposm126_126d_base_v091_signal,
    f29wc_f29_working_capital_inventory_dporank_504d_base_v092_signal,
    f29wc_f29_working_capital_inventory_dpoyoy_252d_base_v093_signal,
    f29wc_f29_working_capital_inventory_invrevswing504_504d_base_v094_signal,
    f29wc_f29_working_capital_inventory_invrevema_63d_base_v095_signal,
    f29wc_f29_working_capital_inventory_invrevdisp_63d_base_v096_signal,
    f29wc_f29_working_capital_inventory_invrevz126_126d_base_v097_signal,
    f29wc_f29_working_capital_inventory_cccrangeamp_504d_base_v098_signal,
    f29wc_f29_working_capital_inventory_cccema_63d_base_v099_signal,
    f29wc_f29_working_capital_inventory_cccz126_126d_base_v100_signal,
    f29wc_f29_working_capital_inventory_cccdd_252d_base_v101_signal,
    f29wc_f29_working_capital_inventory_cccdisp_63d_base_v102_signal,
    f29wc_f29_working_capital_inventory_wcintrngpos_252d_base_v103_signal,
    f29wc_f29_working_capital_inventory_wcintyoy_252d_base_v104_signal,
    f29wc_f29_working_capital_inventory_wcintvol_252d_base_v105_signal,
    f29wc_f29_working_capital_inventory_wcassetsrank_504d_base_v106_signal,
    f29wc_f29_working_capital_inventory_wcassetsdisp_63d_base_v107_signal,
    f29wc_f29_working_capital_inventory_invbuild126_126d_base_v108_signal,
    f29wc_f29_working_capital_inventory_invbuildema_63d_base_v109_signal,
    f29wc_f29_working_capital_inventory_invrank252_252d_base_v110_signal,
    f29wc_f29_working_capital_inventory_invcv_252d_base_v111_signal,
    f29wc_f29_working_capital_inventory_invswing_504d_base_v112_signal,
    f29wc_f29_working_capital_inventory_turnsm126_126d_base_v113_signal,
    f29wc_f29_working_capital_inventory_turnswing_504d_base_v114_signal,
    f29wc_f29_working_capital_inventory_turntrend_63d_base_v115_signal,
    f29wc_f29_working_capital_inventory_recturntrend_63d_base_v116_signal,
    f29wc_f29_working_capital_inventory_recturnz_252d_base_v117_signal,
    f29wc_f29_working_capital_inventory_payturn_63d_base_v118_signal,
    f29wc_f29_working_capital_inventory_buildvscor252_252d_base_v119_signal,
    f29wc_f29_working_capital_inventory_buildvsrev126_126d_base_v120_signal,
    f29wc_f29_working_capital_inventory_recvsrev126_126d_base_v121_signal,
    f29wc_f29_working_capital_inventory_payvscor_63d_base_v122_signal,
    f29wc_f29_working_capital_inventory_invshareassets_63d_base_v123_signal,
    f29wc_f29_working_capital_inventory_payshare_63d_base_v124_signal,
    f29wc_f29_working_capital_inventory_invmixz_252d_base_v125_signal,
    f29wc_f29_working_capital_inventory_nettradeassets_63d_base_v126_signal,
    f29wc_f29_working_capital_inventory_nettraderank_504d_base_v127_signal,
    f29wc_f29_working_capital_inventory_nettradeyoy_252d_base_v128_signal,
    f29wc_f29_working_capital_inventory_payvsinvsm126_126d_base_v129_signal,
    f29wc_f29_working_capital_inventory_payvsinvtrend_63d_base_v130_signal,
    f29wc_f29_working_capital_inventory_payvswctrend_126d_base_v131_signal,
    f29wc_f29_working_capital_inventory_assetscgrowth_63d_base_v132_signal,
    f29wc_f29_working_capital_inventory_assetscdd_252d_base_v133_signal,
    f29wc_f29_working_capital_inventory_revassetscz_252d_base_v134_signal,
    f29wc_f29_working_capital_inventory_illiquidassetstrend_126d_base_v135_signal,
    f29wc_f29_working_capital_inventory_invrevterm_base_v136_signal,
    f29wc_f29_working_capital_inventory_wcintterm_base_v137_signal,
    f29wc_f29_working_capital_inventory_turnterm_base_v138_signal,
    f29wc_f29_working_capital_inventory_dsodispmulti_base_v139_signal,
    f29wc_f29_working_capital_inventory_invdaysrangeamp_504d_base_v140_signal,
    f29wc_f29_working_capital_inventory_invdayssignroot_63d_base_v141_signal,
    f29wc_f29_working_capital_inventory_dsotanh_21d_base_v142_signal,
    f29wc_f29_working_capital_inventory_invrevsignmag_504d_base_v143_signal,
    f29wc_f29_working_capital_inventory_dsovsdpo_63d_base_v144_signal,
    f29wc_f29_working_capital_inventory_cccXbuild_63d_base_v145_signal,
    f29wc_f29_working_capital_inventory_glutXdestock_252d_base_v146_signal,
    f29wc_f29_working_capital_inventory_dsostretchTime_252d_base_v147_signal,
    f29wc_f29_working_capital_inventory_buildstreak_126d_base_v148_signal,
    f29wc_f29_working_capital_inventory_destockTime_252d_base_v149_signal,
    f29wc_f29_working_capital_inventory_wcTighteningTime_252d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F29_WORKING_CAPITAL_INVENTORY_REGISTRY_076_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500

    def _fund(seed, base=1e8, drift=0.0, vol=0.08, allow_neg=False):
        g = np.random.default_rng(seed)
        steps = np.repeat(g.normal(drift, vol, n // 63 + 1), 63)[:n]
        s = base * np.exp(np.cumsum(steps / 63))
        if allow_neg:
            s = s - base * 0.5
        return pd.Series(s, name=None)

    # working-capital components swing cyclically (build/destock, collection/payment)
    inventory = _fund(2901, base=8e7, drift=0.01, vol=0.16).rename("inventory")
    receivables = _fund(2902, base=5e7, drift=0.005, vol=0.14).rename("receivables")
    payables = _fund(2903, base=4e7, drift=0.005, vol=0.15).rename("payables")
    revenue = _fund(2904, base=1.2e8, drift=0.01, vol=0.12).rename("revenue")
    cor = _fund(2905, base=9e7, drift=0.01, vol=0.11).rename("cor")
    assetsc = _fund(2906, base=2.0e8, drift=0.008, vol=0.09).rename("assetsc")

    cols = {"inventory": inventory, "receivables": receivables,
            "payables": payables, "revenue": revenue,
            "cor": cor, "assetsc": assetsc}

    n_features = 0
    nan_ok = 0
    results = {}
    for name, meta in REGISTRY.items():
        fn = meta["func"]
        args = [cols[c] for c in meta["inputs"]]
        assert any(c in ("inventory", "receivables", "payables", "revenue", "cor", "assetsc")
                   for c in meta["inputs"]), name
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

    print("OK f29_working_capital_inventory_base_076_150_claude: %d features pass" % n_features)
