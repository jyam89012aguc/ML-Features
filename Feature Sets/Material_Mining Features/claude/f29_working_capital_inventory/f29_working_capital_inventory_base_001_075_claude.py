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
# inventory stockpile days (inventory/cor), log-compressed level
def f29wc_f29_working_capital_inventory_invdays_63d_base_v001_signal(inventory, cor):
    b = np.log1p((inventory / cor.replace(0, np.nan)).clip(lower=0))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# stockpile-days short-minus-long gap (acute restock vs structural level)
def f29wc_f29_working_capital_inventory_invdaysshortlong_63d_base_v002_signal(inventory, cor):
    r = np.log1p((inventory / cor.replace(0, np.nan)).clip(lower=0))
    short = r.rolling(21, min_periods=10).mean()
    long = r.rolling(126, min_periods=63).mean()
    b = short - long
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# stockpile days z-scored vs own 252d history (de-trended overstock level)
def f29wc_f29_working_capital_inventory_invdaysz_252d_base_v003_signal(inventory, cor):
    r = np.log1p((inventory / cor.replace(0, np.nan)).clip(lower=0))
    b = _z(r, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# stockpile-days percentile-rank vs 504d history (where in overstock band)
def f29wc_f29_working_capital_inventory_invdaysrank_504d_base_v004_signal(inventory, cor):
    r = np.log1p((inventory / cor.replace(0, np.nan)).clip(lower=0))
    b = _rank(r, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# stockpile-days drawdown from 252d peak (destocking off the top)
def f29wc_f29_working_capital_inventory_invdaysdd_252d_base_v005_signal(inventory, cor):
    r = np.log1p((inventory / cor.replace(0, np.nan)).clip(lower=0))
    peak = _rmax(r, 252)
    b = r - peak
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# days-sales-outstanding (receivables/revenue) smoothed over a quarter
def f29wc_f29_working_capital_inventory_dso_63d_base_v006_signal(receivables, revenue):
    b = (receivables / revenue.replace(0, np.nan)).rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# DSO z-scored vs 252d history (collection-stretch regime)
def f29wc_f29_working_capital_inventory_dsoz_252d_base_v007_signal(receivables, revenue):
    r = receivables / revenue.replace(0, np.nan)
    b = _z(r, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# DSO percentile-rank vs 504d (collection-stretch percentile)
def f29wc_f29_working_capital_inventory_dsorank_504d_base_v008_signal(receivables, revenue):
    r = receivables / revenue.replace(0, np.nan)
    b = _rank(r, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# DSO year-over-year change (collection deterioration/improvement)
def f29wc_f29_working_capital_inventory_dsoyoy_252d_base_v009_signal(receivables, revenue):
    r = receivables / revenue.replace(0, np.nan)
    b = r - r.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# days-payable-outstanding (payables/cor) smoothed (supplier-financing reliance)
def f29wc_f29_working_capital_inventory_dpo_63d_base_v010_signal(payables, cor):
    b = (payables / cor.replace(0, np.nan)).rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# DPO z-scored vs 252d (stretching suppliers regime)
def f29wc_f29_working_capital_inventory_dpoz_252d_base_v011_signal(payables, cor):
    r = payables / cor.replace(0, np.nan)
    b = _z(r, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# inventory-to-revenue intensity smoothed (overstock vs sales)
def f29wc_f29_working_capital_inventory_invrev_63d_base_v012_signal(inventory, revenue):
    b = (inventory / revenue.replace(0, np.nan)).rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# inventory/revenue z-scored vs 252d (inventory-glut regime)
def f29wc_f29_working_capital_inventory_invrevz_252d_base_v013_signal(inventory, revenue):
    r = inventory / revenue.replace(0, np.nan)
    b = _z(r, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# inventory/revenue year-over-year swing (inventory-to-revenue cyclicality)
def f29wc_f29_working_capital_inventory_invrevyoy_252d_base_v014_signal(inventory, revenue):
    r = inventory / revenue.replace(0, np.nan)
    b = r - r.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash-conversion-cycle proxy (inv-days + DSO - DPO), smoothed
def f29wc_f29_working_capital_inventory_ccc_63d_base_v015_signal(inventory, receivables, payables, revenue, cor):
    invd = inventory / cor.replace(0, np.nan)
    dso = receivables / revenue.replace(0, np.nan)
    dpo = payables / cor.replace(0, np.nan)
    b = (invd + dso - dpo).rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash-conversion-cycle z-scored vs 252d (working-capital-tie-up regime)
def f29wc_f29_working_capital_inventory_cccz_252d_base_v016_signal(inventory, receivables, payables, revenue, cor):
    invd = inventory / cor.replace(0, np.nan)
    dso = receivables / revenue.replace(0, np.nan)
    dpo = payables / cor.replace(0, np.nan)
    b = _z(invd + dso - dpo, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash-conversion-cycle percentile-rank vs 504d
def f29wc_f29_working_capital_inventory_cccrank_504d_base_v017_signal(inventory, receivables, payables, revenue, cor):
    invd = inventory / cor.replace(0, np.nan)
    dso = receivables / revenue.replace(0, np.nan)
    dpo = payables / cor.replace(0, np.nan)
    b = _rank(invd + dso - dpo, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash-conversion-cycle year-over-year change (working-capital cyclicality)
def f29wc_f29_working_capital_inventory_cccyoy_252d_base_v018_signal(inventory, receivables, payables, revenue, cor):
    invd = inventory / cor.replace(0, np.nan)
    dso = receivables / revenue.replace(0, np.nan)
    dpo = payables / cor.replace(0, np.nan)
    ccc = invd + dso - dpo
    b = ccc - ccc.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-working-capital intensity vs revenue, smoothed
def f29wc_f29_working_capital_inventory_wcint_63d_base_v019_signal(receivables, inventory, payables, revenue):
    nwc = receivables + inventory - payables
    b = (nwc / revenue.replace(0, np.nan)).rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# working-capital-intensity z-scored vs 252d (capital-tie-up regime)
def f29wc_f29_working_capital_inventory_wcintz_252d_base_v020_signal(receivables, inventory, payables, revenue):
    nwc = receivables + inventory - payables
    b = _z(nwc / revenue.replace(0, np.nan), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# working-capital/current-assets short-minus-long gap (acute vs structural)
def f29wc_f29_working_capital_inventory_wcassetsgap_63d_base_v021_signal(receivables, inventory, payables, assetsc):
    nwc = receivables + inventory - payables
    r = nwc / assetsc.replace(0, np.nan)
    short = r.rolling(21, min_periods=10).mean()
    long = r.rolling(126, min_periods=63).mean()
    b = short - long
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# working-capital/current-assets z-scored vs 252d
def f29wc_f29_working_capital_inventory_wcassetsz_252d_base_v022_signal(receivables, inventory, payables, assetsc):
    nwc = receivables + inventory - payables
    b = _z(nwc / assetsc.replace(0, np.nan), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# inventory build: log-inventory change over a quarter
def f29wc_f29_working_capital_inventory_invbuild_63d_base_v023_signal(inventory):
    li = np.log(inventory.replace(0, np.nan))
    b = li - li.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# inventory build: log-inventory change year-over-year
def f29wc_f29_working_capital_inventory_invbuild_252d_base_v024_signal(inventory):
    li = np.log(inventory.replace(0, np.nan))
    b = li - li.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# inventory drawdown from 252d peak (destocking depth)
def f29wc_f29_working_capital_inventory_invdd_252d_base_v025_signal(inventory):
    peak = _rmax(inventory, 252)
    b = inventory / peak.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# log-inventory z-scored vs 252d (inventory-level regime)
def f29wc_f29_working_capital_inventory_invz_252d_base_v026_signal(inventory):
    b = _z(np.log(inventory.replace(0, np.nan)), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# inventory percentile-rank vs 504d history
def f29wc_f29_working_capital_inventory_invrank_504d_base_v027_signal(inventory):
    b = _rank(inventory, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# inventory build minus throughput growth (excess accumulation)
def f29wc_f29_working_capital_inventory_buildvscor_63d_base_v028_signal(inventory, cor):
    li = np.log(inventory.replace(0, np.nan))
    lc = np.log(cor.replace(0, np.nan))
    b = (li - li.shift(63)) - (lc - lc.shift(63))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# inventory build minus revenue growth (sales not absorbing stock)
def f29wc_f29_working_capital_inventory_buildvsrev_63d_base_v029_signal(inventory, revenue):
    li = np.log(inventory.replace(0, np.nan))
    lr = np.log(revenue.replace(0, np.nan))
    b = (li - li.shift(63)) - (lr - lr.shift(63))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# receivables growth minus revenue growth (collection quality slippage)
def f29wc_f29_working_capital_inventory_recvsrev_63d_base_v030_signal(receivables, revenue):
    lx = np.log(receivables.replace(0, np.nan))
    lr = np.log(revenue.replace(0, np.nan))
    b = (lx - lx.shift(63)) - (lr - lr.shift(63))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# stockpile-days term ratio (recent vs structural inventory days)
def f29wc_f29_working_capital_inventory_invdaysterm_base_v031_signal(inventory, cor):
    r = inventory / cor.replace(0, np.nan)
    short = r.rolling(63, min_periods=21).mean()
    long = r.rolling(252, min_periods=126).mean()
    b = short / long.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# DSO term ratio (recent vs structural collection period)
def f29wc_f29_working_capital_inventory_dsoterm_base_v032_signal(receivables, revenue):
    r = receivables / revenue.replace(0, np.nan)
    short = r.rolling(63, min_periods=21).mean()
    long = r.rolling(252, min_periods=126).mean()
    b = short / long.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash-conversion-cycle term spread (recent vs structural)
def f29wc_f29_working_capital_inventory_cccterm_base_v033_signal(inventory, receivables, payables, revenue, cor):
    invd = inventory / cor.replace(0, np.nan)
    dso = receivables / revenue.replace(0, np.nan)
    dpo = payables / cor.replace(0, np.nan)
    ccc = invd + dso - dpo
    short = ccc.rolling(63, min_periods=21).mean()
    long = ccc.rolling(252, min_periods=126).mean()
    b = short - long
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# stockpile-days volatility over a half-year (erratic inventory mgmt)
def f29wc_f29_working_capital_inventory_invdaysvol_126d_base_v034_signal(inventory, cor):
    r = inventory / cor.replace(0, np.nan)
    b = r.rolling(126, min_periods=63).std()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash-conversion-cycle volatility over a year (working-capital instability)
def f29wc_f29_working_capital_inventory_cccvol_252d_base_v035_signal(inventory, receivables, payables, revenue, cor):
    invd = inventory / cor.replace(0, np.nan)
    dso = receivables / revenue.replace(0, np.nan)
    dpo = payables / cor.replace(0, np.nan)
    b = (invd + dso - dpo).rolling(252, min_periods=126).std()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# coefficient of variation of inventory/revenue over a year
def f29wc_f29_working_capital_inventory_invrevcv_252d_base_v036_signal(inventory, revenue):
    r = inventory / revenue.replace(0, np.nan)
    m = _mean(r, 252)
    sd = _std(r, 252)
    b = sd / m.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# inventory-to-revenue cycle-phase momentum (range-position change over a quarter)
def f29wc_f29_working_capital_inventory_invrevphase_252d_base_v037_signal(inventory, revenue):
    r = inventory / revenue.replace(0, np.nan)
    hi = _rmax(r, 252)
    lo = _rmin(r, 252)
    pos = (r - lo) / (hi - lo).replace(0, np.nan)
    b = pos - pos.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash-conversion-cycle swing amplitude over two years
def f29wc_f29_working_capital_inventory_cccswing_504d_base_v038_signal(inventory, receivables, payables, revenue, cor):
    invd = inventory / cor.replace(0, np.nan)
    dso = receivables / revenue.replace(0, np.nan)
    dpo = payables / cor.replace(0, np.nan)
    ccc = invd + dso - dpo
    hi = _rmax(ccc, 504)
    lo = _rmin(ccc, 504)
    b = hi - lo
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# stockpile-days position within its 252d range (cycle phase of stock)
def f29wc_f29_working_capital_inventory_invdaysrngpos_252d_base_v039_signal(inventory, cor):
    r = inventory / cor.replace(0, np.nan)
    hi = _rmax(r, 252)
    lo = _rmin(r, 252)
    b = (r - lo) / (hi - lo).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash-conversion-cycle position within its 504d range
def f29wc_f29_working_capital_inventory_cccrngpos_504d_base_v040_signal(inventory, receivables, payables, revenue, cor):
    invd = inventory / cor.replace(0, np.nan)
    dso = receivables / revenue.replace(0, np.nan)
    dpo = payables / cor.replace(0, np.nan)
    ccc = invd + dso - dpo
    hi = _rmax(ccc, 504)
    lo = _rmin(ccc, 504)
    b = (ccc - lo) / (hi - lo).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# inventory share of gross working-capital components, smoothed
def f29wc_f29_working_capital_inventory_invshare_63d_base_v041_signal(inventory, receivables, payables):
    nwc = (receivables + inventory + payables).replace(0, np.nan)
    b = (inventory / nwc).rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# receivables share of gross working-capital components, smoothed
def f29wc_f29_working_capital_inventory_recshare_63d_base_v042_signal(receivables, inventory, payables):
    nwc = (receivables + inventory + payables).replace(0, np.nan)
    b = (receivables / nwc).rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# inventory/current-assets fast-minus-slow z spread (illiquidity-mix shift)
def f29wc_f29_working_capital_inventory_invassetscz_252d_base_v043_signal(inventory, assetsc):
    r = inventory / assetsc.replace(0, np.nan)
    b = _z(r, 252) - _z(r.rolling(63, min_periods=21).mean(), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# receivables share of current assets, smoothed
def f29wc_f29_working_capital_inventory_recassetsc_63d_base_v044_signal(receivables, assetsc):
    b = (receivables / assetsc.replace(0, np.nan)).rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# log current-assets z-scored vs 252d (current-asset base regime)
def f29wc_f29_working_capital_inventory_assetscz_252d_base_v045_signal(assetsc):
    b = _z(np.log(assetsc.replace(0, np.nan)), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# stockpile-days trend over a quarter (building/destocking)
def f29wc_f29_working_capital_inventory_invdaystrend_63d_base_v046_signal(inventory, cor):
    r = np.log1p((inventory / cor.replace(0, np.nan)).clip(lower=0))
    b = r - r.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash-conversion-cycle change over a half-year
def f29wc_f29_working_capital_inventory_cccyoy2_126d_base_v047_signal(inventory, receivables, payables, revenue, cor):
    invd = inventory / cor.replace(0, np.nan)
    dso = receivables / revenue.replace(0, np.nan)
    dpo = payables / cor.replace(0, np.nan)
    ccc = invd + dso - dpo
    b = ccc - ccc.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# working-capital-intensity trend over a quarter
def f29wc_f29_working_capital_inventory_wcinttrend_63d_base_v048_signal(receivables, inventory, payables, revenue):
    nwc = receivables + inventory - payables
    wci = nwc / revenue.replace(0, np.nan)
    b = wci - wci.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# signed-root of cash-conversion-cycle deviation (compressed WC stress)
def f29wc_f29_working_capital_inventory_cccsignroot_63d_base_v049_signal(inventory, receivables, payables, revenue, cor):
    invd = inventory / cor.replace(0, np.nan)
    dso = receivables / revenue.replace(0, np.nan)
    dpo = payables / cor.replace(0, np.nan)
    ccc = (invd + dso - dpo)
    dev = ccc - ccc.rolling(252, min_periods=126).mean()
    b = np.sign(dev) * (dev.abs() ** 0.5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# tanh-squashed inventory-build momentum (bounded stocking change)
def f29wc_f29_working_capital_inventory_invbuildtanh_21d_base_v050_signal(inventory):
    li = np.log(inventory.replace(0, np.nan))
    chg = li - li.shift(21)
    b = np.tanh(8.0 * chg)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# glut-relief interaction: high inventory/revenue now actively destocking
def f29wc_f29_working_capital_inventory_glutreliefX_63d_base_v051_signal(inventory, revenue, cor):
    invrev = inventory / revenue.replace(0, np.nan)
    glut = (_rank(invrev, 252)).clip(lower=0)
    li = np.log(inventory.replace(0, np.nan))
    destock = (-(li - li.shift(21)).clip(upper=0))
    b = glut * np.tanh(20.0 * destock)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# working-capital-intensity deviation from its own 252d median (WC extremity)
def f29wc_f29_working_capital_inventory_wcintdev_252d_base_v052_signal(receivables, inventory, payables, revenue):
    wci = (receivables + inventory - payables) / revenue.replace(0, np.nan)
    b = wci - wci.rolling(252, min_periods=126).median()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# payables coverage of inventory (supplier-financed stockpile)
def f29wc_f29_working_capital_inventory_payvsinv_63d_base_v053_signal(payables, inventory):
    b = (payables / inventory.replace(0, np.nan)).rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# payables/inventory z-scored vs 252d (supplier-financing regime)
def f29wc_f29_working_capital_inventory_payvsinvz_252d_base_v054_signal(payables, inventory):
    r = payables / inventory.replace(0, np.nan)
    b = _z(r, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net trade balance (receivables - payables) over revenue, smoothed
def f29wc_f29_working_capital_inventory_nettrade_63d_base_v055_signal(receivables, payables, revenue):
    b = ((receivables - payables) / revenue.replace(0, np.nan)).rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-trade-balance z-scored vs 252d
def f29wc_f29_working_capital_inventory_nettradez_252d_base_v056_signal(receivables, payables, revenue):
    r = (receivables - payables) / revenue.replace(0, np.nan)
    b = _z(r, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fraction of last year CCC sat above its own median (chronic WC tie-up)
def f29wc_f29_working_capital_inventory_hicccTime_252d_base_v057_signal(inventory, receivables, payables, revenue, cor):
    invd = inventory / cor.replace(0, np.nan)
    dso = receivables / revenue.replace(0, np.nan)
    dpo = payables / cor.replace(0, np.nan)
    ccc = invd + dso - dpo
    med = ccc.rolling(252, min_periods=126).median()
    high = (ccc > med).astype(float)
    b = high.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# count of fresh inventory-build onsets over the last year (build tally)
def f29wc_f29_working_capital_inventory_buildonset_252d_base_v058_signal(inventory, cor):
    r = inventory / cor.replace(0, np.nan)
    building = (r > r.shift(21)).astype(float)
    entries = ((building == 1) & (building.shift(1) == 0)).astype(float)
    b = entries.rolling(252, min_periods=126).sum() + 0.3 * building.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# time inventory/revenue sat in top-quartile (glut regime) plus depth
def f29wc_f29_working_capital_inventory_glutTime_252d_base_v059_signal(inventory, revenue):
    r = inventory / revenue.replace(0, np.nan)
    p = _rank(r, 252) + 0.5
    glut = (p > 0.75).astype(float)
    frac = glut.rolling(252, min_periods=126).mean()
    depth = (p - 0.75).clip(lower=0).rolling(63, min_periods=21).mean()
    b = frac + 2.0 * depth
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# stockpile-days displacement: level minus slow EMA (acute vs chronic)
def f29wc_f29_working_capital_inventory_invdaysdisp_63d_base_v060_signal(inventory, cor):
    r = np.log1p((inventory / cor.replace(0, np.nan)).clip(lower=0))
    b = r - r.ewm(span=126, min_periods=42).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# DSO displacement: level minus slow EMA
def f29wc_f29_working_capital_inventory_dsodisp_63d_base_v061_signal(receivables, revenue):
    r = receivables / revenue.replace(0, np.nan)
    b = r - r.ewm(span=126, min_periods=42).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# DPO displacement vs slow EMA (acute supplier-stretch vs structural terms)
def f29wc_f29_working_capital_inventory_dpodispslow_126d_base_v062_signal(payables, cor):
    r = payables / cor.replace(0, np.nan)
    b = r - r.ewm(span=252, min_periods=84).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash-conversion-cycle displacement vs its slow EMA (acute WC vs structural)
def f29wc_f29_working_capital_inventory_cccdispslow_126d_base_v063_signal(inventory, receivables, payables, revenue, cor):
    invd = inventory / cor.replace(0, np.nan)
    dso = receivables / revenue.replace(0, np.nan)
    dpo = payables / cor.replace(0, np.nan)
    ccc = invd + dso - dpo
    b = ccc - ccc.ewm(span=252, min_periods=84).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# stockpile-days distance below its 126d peak as range fraction (destock progress)
def f29wc_f29_working_capital_inventory_invdaysfromtrough_126d_base_v064_signal(inventory, cor):
    r = np.log1p((inventory / cor.replace(0, np.nan)).clip(lower=0))
    hi = _rmax(r, 126)
    lo = _rmin(r, 126)
    b = (hi - r) / (hi - lo).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash-conversion-cycle position within its 126d range (WC cycle phase)
def f29wc_f29_working_capital_inventory_cccrngpos126_126d_base_v065_signal(inventory, receivables, payables, revenue, cor):
    invd = inventory / cor.replace(0, np.nan)
    dso = receivables / revenue.replace(0, np.nan)
    dpo = payables / cor.replace(0, np.nan)
    ccc = invd + dso - dpo
    hi = _rmax(ccc, 126)
    lo = _rmin(ccc, 126)
    b = (ccc - lo) / (hi - lo).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# stockpile-days disagreement across short/med/long windows
def f29wc_f29_working_capital_inventory_invdaysdispmulti_base_v066_signal(inventory, cor):
    r = np.log1p((inventory / cor.replace(0, np.nan)).clip(lower=0))
    a = r.rolling(63, min_periods=21).mean()
    b2 = r.rolling(126, min_periods=63).mean()
    c = r.rolling(252, min_periods=126).mean()
    b = pd.concat([a, b2, c], axis=1).std(axis=1)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# composite working-capital stress: z(inv-days)+z(DSO)+z(inv/rev)
def f29wc_f29_working_capital_inventory_wcstress_base_v067_signal(inventory, receivables, payables, revenue, cor):
    invd = np.log1p((inventory / cor.replace(0, np.nan)).clip(lower=0))
    dso = receivables / revenue.replace(0, np.nan)
    invrev = inventory / revenue.replace(0, np.nan)
    b = _z(invd, 252) + _z(dso, 252) + _z(invrev, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# DPO term ratio (recent vs structural payment period)
def f29wc_f29_working_capital_inventory_dpoterm_base_v068_signal(payables, cor):
    r = payables / cor.replace(0, np.nan)
    short = r.rolling(63, min_periods=21).mean()
    long = r.rolling(252, min_periods=126).mean()
    b = short / long.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# stockpile-days year-over-year change
def f29wc_f29_working_capital_inventory_invdaysyoy_252d_base_v069_signal(inventory, cor):
    r = np.log1p((inventory / cor.replace(0, np.nan)).clip(lower=0))
    b = r - r.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# working-capital/current-assets year-over-year change
def f29wc_f29_working_capital_inventory_wcassetsyoy_252d_base_v070_signal(receivables, inventory, payables, assetsc):
    nwc = receivables + inventory - payables
    r = nwc / assetsc.replace(0, np.nan)
    b = r - r.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# DSO volatility over a half-year (erratic collections)
def f29wc_f29_working_capital_inventory_dsovol_126d_base_v071_signal(receivables, revenue):
    r = receivables / revenue.replace(0, np.nan)
    b = r.rolling(126, min_periods=63).std()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# inventory/revenue drawdown from 252d peak (destock relief)
def f29wc_f29_working_capital_inventory_invrevdd_252d_base_v072_signal(inventory, revenue):
    r = inventory / revenue.replace(0, np.nan)
    peak = _rmax(r, 252)
    b = r / peak.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# inventory turnover (cor/inventory) smoothed (stock throughput speed)
def f29wc_f29_working_capital_inventory_corcov_63d_base_v073_signal(cor, inventory):
    b = (cor / inventory.replace(0, np.nan)).rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# inventory-turnover acceleration (base 2nd-difference of throughput speed)
def f29wc_f29_working_capital_inventory_corcovaccel_126d_base_v074_signal(cor, inventory):
    r = cor / inventory.replace(0, np.nan)
    d1 = r - r.shift(63)
    b = d1 - d1.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# current-asset turnover (revenue/current-assets), smoothed
def f29wc_f29_working_capital_inventory_revassetsc_63d_base_v075_signal(revenue, assetsc):
    b = (revenue / assetsc.replace(0, np.nan)).rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f29wc_f29_working_capital_inventory_invdays_63d_base_v001_signal,
    f29wc_f29_working_capital_inventory_invdaysshortlong_63d_base_v002_signal,
    f29wc_f29_working_capital_inventory_invdaysz_252d_base_v003_signal,
    f29wc_f29_working_capital_inventory_invdaysrank_504d_base_v004_signal,
    f29wc_f29_working_capital_inventory_invdaysdd_252d_base_v005_signal,
    f29wc_f29_working_capital_inventory_dso_63d_base_v006_signal,
    f29wc_f29_working_capital_inventory_dsoz_252d_base_v007_signal,
    f29wc_f29_working_capital_inventory_dsorank_504d_base_v008_signal,
    f29wc_f29_working_capital_inventory_dsoyoy_252d_base_v009_signal,
    f29wc_f29_working_capital_inventory_dpo_63d_base_v010_signal,
    f29wc_f29_working_capital_inventory_dpoz_252d_base_v011_signal,
    f29wc_f29_working_capital_inventory_invrev_63d_base_v012_signal,
    f29wc_f29_working_capital_inventory_invrevz_252d_base_v013_signal,
    f29wc_f29_working_capital_inventory_invrevyoy_252d_base_v014_signal,
    f29wc_f29_working_capital_inventory_ccc_63d_base_v015_signal,
    f29wc_f29_working_capital_inventory_cccz_252d_base_v016_signal,
    f29wc_f29_working_capital_inventory_cccrank_504d_base_v017_signal,
    f29wc_f29_working_capital_inventory_cccyoy_252d_base_v018_signal,
    f29wc_f29_working_capital_inventory_wcint_63d_base_v019_signal,
    f29wc_f29_working_capital_inventory_wcintz_252d_base_v020_signal,
    f29wc_f29_working_capital_inventory_wcassetsgap_63d_base_v021_signal,
    f29wc_f29_working_capital_inventory_wcassetsz_252d_base_v022_signal,
    f29wc_f29_working_capital_inventory_invbuild_63d_base_v023_signal,
    f29wc_f29_working_capital_inventory_invbuild_252d_base_v024_signal,
    f29wc_f29_working_capital_inventory_invdd_252d_base_v025_signal,
    f29wc_f29_working_capital_inventory_invz_252d_base_v026_signal,
    f29wc_f29_working_capital_inventory_invrank_504d_base_v027_signal,
    f29wc_f29_working_capital_inventory_buildvscor_63d_base_v028_signal,
    f29wc_f29_working_capital_inventory_buildvsrev_63d_base_v029_signal,
    f29wc_f29_working_capital_inventory_recvsrev_63d_base_v030_signal,
    f29wc_f29_working_capital_inventory_invdaysterm_base_v031_signal,
    f29wc_f29_working_capital_inventory_dsoterm_base_v032_signal,
    f29wc_f29_working_capital_inventory_cccterm_base_v033_signal,
    f29wc_f29_working_capital_inventory_invdaysvol_126d_base_v034_signal,
    f29wc_f29_working_capital_inventory_cccvol_252d_base_v035_signal,
    f29wc_f29_working_capital_inventory_invrevcv_252d_base_v036_signal,
    f29wc_f29_working_capital_inventory_invrevphase_252d_base_v037_signal,
    f29wc_f29_working_capital_inventory_cccswing_504d_base_v038_signal,
    f29wc_f29_working_capital_inventory_invdaysrngpos_252d_base_v039_signal,
    f29wc_f29_working_capital_inventory_cccrngpos_504d_base_v040_signal,
    f29wc_f29_working_capital_inventory_invshare_63d_base_v041_signal,
    f29wc_f29_working_capital_inventory_recshare_63d_base_v042_signal,
    f29wc_f29_working_capital_inventory_invassetscz_252d_base_v043_signal,
    f29wc_f29_working_capital_inventory_recassetsc_63d_base_v044_signal,
    f29wc_f29_working_capital_inventory_assetscz_252d_base_v045_signal,
    f29wc_f29_working_capital_inventory_invdaystrend_63d_base_v046_signal,
    f29wc_f29_working_capital_inventory_cccyoy2_126d_base_v047_signal,
    f29wc_f29_working_capital_inventory_wcinttrend_63d_base_v048_signal,
    f29wc_f29_working_capital_inventory_cccsignroot_63d_base_v049_signal,
    f29wc_f29_working_capital_inventory_invbuildtanh_21d_base_v050_signal,
    f29wc_f29_working_capital_inventory_glutreliefX_63d_base_v051_signal,
    f29wc_f29_working_capital_inventory_wcintdev_252d_base_v052_signal,
    f29wc_f29_working_capital_inventory_payvsinv_63d_base_v053_signal,
    f29wc_f29_working_capital_inventory_payvsinvz_252d_base_v054_signal,
    f29wc_f29_working_capital_inventory_nettrade_63d_base_v055_signal,
    f29wc_f29_working_capital_inventory_nettradez_252d_base_v056_signal,
    f29wc_f29_working_capital_inventory_hicccTime_252d_base_v057_signal,
    f29wc_f29_working_capital_inventory_buildonset_252d_base_v058_signal,
    f29wc_f29_working_capital_inventory_glutTime_252d_base_v059_signal,
    f29wc_f29_working_capital_inventory_invdaysdisp_63d_base_v060_signal,
    f29wc_f29_working_capital_inventory_dsodisp_63d_base_v061_signal,
    f29wc_f29_working_capital_inventory_dpodispslow_126d_base_v062_signal,
    f29wc_f29_working_capital_inventory_cccdispslow_126d_base_v063_signal,
    f29wc_f29_working_capital_inventory_invdaysfromtrough_126d_base_v064_signal,
    f29wc_f29_working_capital_inventory_cccrngpos126_126d_base_v065_signal,
    f29wc_f29_working_capital_inventory_invdaysdispmulti_base_v066_signal,
    f29wc_f29_working_capital_inventory_wcstress_base_v067_signal,
    f29wc_f29_working_capital_inventory_dpoterm_base_v068_signal,
    f29wc_f29_working_capital_inventory_invdaysyoy_252d_base_v069_signal,
    f29wc_f29_working_capital_inventory_wcassetsyoy_252d_base_v070_signal,
    f29wc_f29_working_capital_inventory_dsovol_126d_base_v071_signal,
    f29wc_f29_working_capital_inventory_invrevdd_252d_base_v072_signal,
    f29wc_f29_working_capital_inventory_corcov_63d_base_v073_signal,
    f29wc_f29_working_capital_inventory_corcovaccel_126d_base_v074_signal,
    f29wc_f29_working_capital_inventory_revassetsc_63d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F29_WORKING_CAPITAL_INVENTORY_REGISTRY_001_075 = REGISTRY


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

    print("OK f29_working_capital_inventory_base_001_075_claude: %d features pass" % n_features)
