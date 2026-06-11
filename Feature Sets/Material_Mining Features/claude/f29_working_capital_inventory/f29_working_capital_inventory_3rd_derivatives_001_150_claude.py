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
# jerk(21d) of inventory stockpile days
def f29wc_f29_working_capital_inventory_invdays_21d_jerk_v001_signal(inventory, cor):
    base = np.log1p((inventory / cor.replace(0, np.nan)).clip(lower=0))
    d1 = _slope(base, 21)
    b = _slope(d1, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk(21d) of stockpile-days short-minus-lon
def f29wc_f29_working_capital_inventory_invdaysshortlong_21d_jerk_v002_signal(inventory, cor):
    r = np.log1p((inventory / cor.replace(0, np.nan)).clip(lower=0))
    short = r.rolling(21, min_periods=10).mean()
    long = r.rolling(126, min_periods=63).mean()
    base = short - long
    d1 = _slope(base, 21)
    b = _slope(d1, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk(63d) of stockpile days z-scored vs own
def f29wc_f29_working_capital_inventory_invdaysz_63d_jerk_v003_signal(inventory, cor):
    r = np.log1p((inventory / cor.replace(0, np.nan)).clip(lower=0))
    base = _z(r, 252)
    d1 = _slope(base, 63)
    b = _slope(d1, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk(63d) of stockpile-days percentile-rank
def f29wc_f29_working_capital_inventory_invdaysrank_63d_jerk_v004_signal(inventory, cor):
    r = np.log1p((inventory / cor.replace(0, np.nan)).clip(lower=0))
    base = _rank(r, 504)
    d1 = _slope(base, 63)
    b = _slope(d1, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk(63d) of stockpile-days drawdown from 2
def f29wc_f29_working_capital_inventory_invdaysdd_63d_jerk_v005_signal(inventory, cor):
    r = np.log1p((inventory / cor.replace(0, np.nan)).clip(lower=0))
    peak = _rmax(r, 252)
    base = r - peak
    d1 = _slope(base, 63)
    b = _slope(d1, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk(21d) of days-sales-outstanding
def f29wc_f29_working_capital_inventory_dso_21d_jerk_v006_signal(receivables, revenue):
    base = (receivables / revenue.replace(0, np.nan)).rolling(63, min_periods=21).mean()
    d1 = _slope(base, 21)
    b = _slope(d1, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk(63d) of DSO z-scored vs 252d history
def f29wc_f29_working_capital_inventory_dsoz_63d_jerk_v007_signal(receivables, revenue):
    r = receivables / revenue.replace(0, np.nan)
    base = _z(r, 252)
    d1 = _slope(base, 63)
    b = _slope(d1, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk(63d) of DSO percentile-rank vs 504d
def f29wc_f29_working_capital_inventory_dsorank_63d_jerk_v008_signal(receivables, revenue):
    r = receivables / revenue.replace(0, np.nan)
    base = _rank(r, 504)
    d1 = _slope(base, 63)
    b = _slope(d1, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk(63d) of DSO year-over-year change
def f29wc_f29_working_capital_inventory_dsoyoy_63d_jerk_v009_signal(receivables, revenue):
    r = receivables / revenue.replace(0, np.nan)
    base = r - r.shift(252)
    d1 = _slope(base, 63)
    b = _slope(d1, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk(21d) of days-payable-outstanding
def f29wc_f29_working_capital_inventory_dpo_21d_jerk_v010_signal(payables, cor):
    base = (payables / cor.replace(0, np.nan)).rolling(63, min_periods=21).mean()
    d1 = _slope(base, 21)
    b = _slope(d1, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk(63d) of DPO z-scored vs 252d
def f29wc_f29_working_capital_inventory_dpoz_63d_jerk_v011_signal(payables, cor):
    r = payables / cor.replace(0, np.nan)
    base = _z(r, 252)
    d1 = _slope(base, 63)
    b = _slope(d1, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk(21d) of inventory-to-revenue intensity
def f29wc_f29_working_capital_inventory_invrev_21d_jerk_v012_signal(inventory, revenue):
    base = (inventory / revenue.replace(0, np.nan)).rolling(63, min_periods=21).mean()
    d1 = _slope(base, 21)
    b = _slope(d1, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk(63d) of inventory/revenue z-scored vs
def f29wc_f29_working_capital_inventory_invrevz_63d_jerk_v013_signal(inventory, revenue):
    r = inventory / revenue.replace(0, np.nan)
    base = _z(r, 252)
    d1 = _slope(base, 63)
    b = _slope(d1, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk(63d) of inventory/revenue year-over-ye
def f29wc_f29_working_capital_inventory_invrevyoy_63d_jerk_v014_signal(inventory, revenue):
    r = inventory / revenue.replace(0, np.nan)
    base = r - r.shift(252)
    d1 = _slope(base, 63)
    b = _slope(d1, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk(21d) of cash-conversion-cycle proxy
def f29wc_f29_working_capital_inventory_ccc_21d_jerk_v015_signal(inventory, receivables, payables, revenue, cor):
    ccc = _f29_ccc(inventory, receivables, payables, revenue, cor)
    base = (ccc).rolling(63, min_periods=21).mean()
    d1 = _slope(base, 21)
    b = _slope(d1, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk(63d) of cash-conversion-cycle z-scored
def f29wc_f29_working_capital_inventory_cccz_63d_jerk_v016_signal(inventory, receivables, payables, revenue, cor):
    ccc = _f29_ccc(inventory, receivables, payables, revenue, cor)
    base = _z(ccc, 252)
    d1 = _slope(base, 63)
    b = _slope(d1, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk(63d) of cash-conversion-cycle percenti
def f29wc_f29_working_capital_inventory_cccrank_63d_jerk_v017_signal(inventory, receivables, payables, revenue, cor):
    ccc = _f29_ccc(inventory, receivables, payables, revenue, cor)
    base = _rank(ccc, 504)
    d1 = _slope(base, 63)
    b = _slope(d1, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk(63d) of cash-conversion-cycle year-ove
def f29wc_f29_working_capital_inventory_cccyoy_63d_jerk_v018_signal(inventory, receivables, payables, revenue, cor):
    ccc = _f29_ccc(inventory, receivables, payables, revenue, cor)
    base = ccc - ccc.shift(252)
    d1 = _slope(base, 63)
    b = _slope(d1, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk(21d) of net-working-capital intensity
def f29wc_f29_working_capital_inventory_wcint_21d_jerk_v019_signal(receivables, inventory, payables, revenue):
    nwc = receivables + inventory - payables
    base = (nwc / revenue.replace(0, np.nan)).rolling(63, min_periods=21).mean()
    d1 = _slope(base, 21)
    b = _slope(d1, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk(63d) of working-capital-intensity z-sc
def f29wc_f29_working_capital_inventory_wcintz_63d_jerk_v020_signal(receivables, inventory, payables, revenue):
    nwc = receivables + inventory - payables
    base = _z(nwc / revenue.replace(0, np.nan), 252)
    d1 = _slope(base, 63)
    b = _slope(d1, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk(21d) of working-capital/current-assets
def f29wc_f29_working_capital_inventory_wcassetsgap_21d_jerk_v021_signal(receivables, inventory, payables, assetsc):
    nwc = receivables + inventory - payables
    r = nwc / assetsc.replace(0, np.nan)
    short = r.rolling(21, min_periods=10).mean()
    long = r.rolling(126, min_periods=63).mean()
    base = short - long
    d1 = _slope(base, 21)
    b = _slope(d1, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk(63d) of working-capital/current-assets
def f29wc_f29_working_capital_inventory_wcassetsz_63d_jerk_v022_signal(receivables, inventory, payables, assetsc):
    nwc = receivables + inventory - payables
    base = _z(nwc / assetsc.replace(0, np.nan), 252)
    d1 = _slope(base, 63)
    b = _slope(d1, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk(21d) of inventory build: log-inventory
def f29wc_f29_working_capital_inventory_invbuild_21d_jerk_v023_signal(inventory):
    li = np.log(inventory.replace(0, np.nan))
    base = li - li.shift(63)
    d1 = _slope(base, 21)
    b = _slope(d1, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk(63d) of inventory build: log-inventory
def f29wc_f29_working_capital_inventory_invbuild_63d_jerk_v024_signal(inventory):
    li = np.log(inventory.replace(0, np.nan))
    base = li - li.shift(252)
    d1 = _slope(base, 63)
    b = _slope(d1, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk(63d) of inventory drawdown from 252d p
def f29wc_f29_working_capital_inventory_invdd_63d_jerk_v025_signal(inventory):
    peak = _rmax(inventory, 252)
    base = inventory / peak.replace(0, np.nan) - 1.0
    d1 = _slope(base, 63)
    b = _slope(d1, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk(63d) of log-inventory z-scored vs 252d
def f29wc_f29_working_capital_inventory_invz_63d_jerk_v026_signal(inventory):
    base = _z(np.log(inventory.replace(0, np.nan)), 252)
    d1 = _slope(base, 63)
    b = _slope(d1, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk(63d) of inventory percentile-rank vs 5
def f29wc_f29_working_capital_inventory_invrank_63d_jerk_v027_signal(inventory):
    base = _rank(inventory, 504)
    d1 = _slope(base, 63)
    b = _slope(d1, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk(21d) of inventory build minus throughp
def f29wc_f29_working_capital_inventory_buildvscor_21d_jerk_v028_signal(inventory, cor):
    li = np.log(inventory.replace(0, np.nan))
    lc = np.log(cor.replace(0, np.nan))
    base = (li - li.shift(63)) - (lc - lc.shift(63))
    d1 = _slope(base, 21)
    b = _slope(d1, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk(21d) of inventory build minus revenue
def f29wc_f29_working_capital_inventory_buildvsrev_21d_jerk_v029_signal(inventory, revenue):
    li = np.log(inventory.replace(0, np.nan))
    lr = np.log(revenue.replace(0, np.nan))
    base = (li - li.shift(63)) - (lr - lr.shift(63))
    d1 = _slope(base, 21)
    b = _slope(d1, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk(21d) of receivables growth minus reven
def f29wc_f29_working_capital_inventory_recvsrev_21d_jerk_v030_signal(receivables, revenue):
    lx = np.log(receivables.replace(0, np.nan))
    lr = np.log(revenue.replace(0, np.nan))
    base = (lx - lx.shift(63)) - (lr - lr.shift(63))
    d1 = _slope(base, 21)
    b = _slope(d1, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk(21d) of stockpile-days term ratio
def f29wc_f29_working_capital_inventory_invdaysterm_21d_jerk_v031_signal(inventory, cor):
    r = inventory / cor.replace(0, np.nan)
    short = r.rolling(63, min_periods=21).mean()
    long = r.rolling(252, min_periods=126).mean()
    base = short / long.replace(0, np.nan) - 1.0
    d1 = _slope(base, 21)
    b = _slope(d1, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk(21d) of DSO term ratio
def f29wc_f29_working_capital_inventory_dsoterm_21d_jerk_v032_signal(receivables, revenue):
    r = receivables / revenue.replace(0, np.nan)
    short = r.rolling(63, min_periods=21).mean()
    long = r.rolling(252, min_periods=126).mean()
    base = short / long.replace(0, np.nan) - 1.0
    d1 = _slope(base, 21)
    b = _slope(d1, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk(21d) of cash-conversion-cycle term spr
def f29wc_f29_working_capital_inventory_cccterm_21d_jerk_v033_signal(inventory, receivables, payables, revenue, cor):
    ccc = _f29_ccc(inventory, receivables, payables, revenue, cor)
    short = ccc.rolling(63, min_periods=21).mean()
    long = ccc.rolling(252, min_periods=126).mean()
    base = short - long
    d1 = _slope(base, 21)
    b = _slope(d1, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk(21d) of stockpile-days volatility over
def f29wc_f29_working_capital_inventory_invdaysvol_21d_jerk_v034_signal(inventory, cor):
    r = inventory / cor.replace(0, np.nan)
    base = r.rolling(126, min_periods=63).std()
    d1 = _slope(base, 21)
    b = _slope(d1, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk(63d) of cash-conversion-cycle volatili
def f29wc_f29_working_capital_inventory_cccvol_63d_jerk_v035_signal(inventory, receivables, payables, revenue, cor):
    ccc = _f29_ccc(inventory, receivables, payables, revenue, cor)
    base = (ccc).rolling(252, min_periods=126).std()
    d1 = _slope(base, 63)
    b = _slope(d1, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk(63d) of coefficient of variation of in
def f29wc_f29_working_capital_inventory_invrevcv_63d_jerk_v036_signal(inventory, revenue):
    r = inventory / revenue.replace(0, np.nan)
    m = _mean(r, 252)
    sd = _std(r, 252)
    base = sd / m.replace(0, np.nan)
    d1 = _slope(base, 63)
    b = _slope(d1, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk(63d) of inventory-to-revenue cycle-pha
def f29wc_f29_working_capital_inventory_invrevphase_63d_jerk_v037_signal(inventory, revenue):
    r = inventory / revenue.replace(0, np.nan)
    hi = _rmax(r, 252)
    lo = _rmin(r, 252)
    pos = (r - lo) / (hi - lo).replace(0, np.nan)
    base = pos - pos.shift(63)
    d1 = _slope(base, 63)
    b = _slope(d1, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk(63d) of cash-conversion-cycle swing am
def f29wc_f29_working_capital_inventory_cccswing_63d_jerk_v038_signal(inventory, receivables, payables, revenue, cor):
    ccc = _f29_ccc(inventory, receivables, payables, revenue, cor)
    hi = _rmax(ccc, 504)
    lo = _rmin(ccc, 504)
    base = hi - lo
    d1 = _slope(base, 63)
    b = _slope(d1, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk(63d) of stockpile-days position within
def f29wc_f29_working_capital_inventory_invdaysrngpos_63d_jerk_v039_signal(inventory, cor):
    r = inventory / cor.replace(0, np.nan)
    hi = _rmax(r, 252)
    lo = _rmin(r, 252)
    base = (r - lo) / (hi - lo).replace(0, np.nan)
    d1 = _slope(base, 63)
    b = _slope(d1, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk(63d) of cash-conversion-cycle position
def f29wc_f29_working_capital_inventory_cccrngpos_63d_jerk_v040_signal(inventory, receivables, payables, revenue, cor):
    ccc = _f29_ccc(inventory, receivables, payables, revenue, cor)
    hi = _rmax(ccc, 504)
    lo = _rmin(ccc, 504)
    base = (ccc - lo) / (hi - lo).replace(0, np.nan)
    d1 = _slope(base, 63)
    b = _slope(d1, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk(21d) of inventory share of gross worki
def f29wc_f29_working_capital_inventory_invshare_21d_jerk_v041_signal(inventory, receivables, payables):
    nwc = (receivables + inventory + payables).replace(0, np.nan)
    base = (inventory / nwc).rolling(63, min_periods=21).mean()
    d1 = _slope(base, 21)
    b = _slope(d1, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk(21d) of receivables share of gross wor
def f29wc_f29_working_capital_inventory_recshare_21d_jerk_v042_signal(receivables, inventory, payables):
    nwc = (receivables + inventory + payables).replace(0, np.nan)
    base = (receivables / nwc).rolling(63, min_periods=21).mean()
    d1 = _slope(base, 21)
    b = _slope(d1, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk(63d) of inventory/current-assets fast-
def f29wc_f29_working_capital_inventory_invassetscz_63d_jerk_v043_signal(inventory, assetsc):
    r = inventory / assetsc.replace(0, np.nan)
    base = _z(r, 252) - _z(r.rolling(63, min_periods=21).mean(), 252)
    d1 = _slope(base, 63)
    b = _slope(d1, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk(21d) of receivables share of current a
def f29wc_f29_working_capital_inventory_recassetsc_21d_jerk_v044_signal(receivables, assetsc):
    base = (receivables / assetsc.replace(0, np.nan)).rolling(63, min_periods=21).mean()
    d1 = _slope(base, 21)
    b = _slope(d1, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk(63d) of log current-assets z-scored vs
def f29wc_f29_working_capital_inventory_assetscz_63d_jerk_v045_signal(assetsc):
    base = _z(np.log(assetsc.replace(0, np.nan)), 252)
    d1 = _slope(base, 63)
    b = _slope(d1, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk(21d) of stockpile-days trend over a qu
def f29wc_f29_working_capital_inventory_invdaystrend_21d_jerk_v046_signal(inventory, cor):
    r = np.log1p((inventory / cor.replace(0, np.nan)).clip(lower=0))
    base = r - r.shift(63)
    d1 = _slope(base, 21)
    b = _slope(d1, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk(21d) of cash-conversion-cycle change o
def f29wc_f29_working_capital_inventory_cccyoy2_21d_jerk_v047_signal(inventory, receivables, payables, revenue, cor):
    ccc = _f29_ccc(inventory, receivables, payables, revenue, cor)
    base = ccc - ccc.shift(126)
    d1 = _slope(base, 21)
    b = _slope(d1, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk(21d) of working-capital-intensity tren
def f29wc_f29_working_capital_inventory_wcinttrend_21d_jerk_v048_signal(receivables, inventory, payables, revenue):
    nwc = receivables + inventory - payables
    wci = nwc / revenue.replace(0, np.nan)
    base = wci - wci.shift(63)
    d1 = _slope(base, 21)
    b = _slope(d1, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk(21d) of signed-root of cash-conversion
def f29wc_f29_working_capital_inventory_cccsignroot_21d_jerk_v049_signal(inventory, receivables, payables, revenue, cor):
    ccc = _f29_ccc(inventory, receivables, payables, revenue, cor)
    ccc = (ccc)
    dev = ccc - ccc.rolling(252, min_periods=126).mean()
    base = np.sign(dev) * (dev.abs() ** 0.5)
    d1 = _slope(base, 21)
    b = _slope(d1, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk(5d) of tanh-squashed inventory-build
def f29wc_f29_working_capital_inventory_invbuildtanh_5d_jerk_v050_signal(inventory):
    li = np.log(inventory.replace(0, np.nan))
    chg = li - li.shift(21)
    base = np.tanh(8.0 * chg)
    d1 = _slope(base, 5)
    b = _slope(d1, 5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk(21d) of glut-relief interaction: high
def f29wc_f29_working_capital_inventory_glutreliefX_21d_jerk_v051_signal(inventory, revenue, cor):
    invrev = inventory / revenue.replace(0, np.nan)
    glut = (_rank(invrev, 252)).clip(lower=0)
    li = np.log(inventory.replace(0, np.nan))
    destock = (-(li - li.shift(21)).clip(upper=0))
    base = glut * np.tanh(20.0 * destock)
    d1 = _slope(base, 21)
    b = _slope(d1, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk(63d) of working-capital-intensity devi
def f29wc_f29_working_capital_inventory_wcintdev_63d_jerk_v052_signal(receivables, inventory, payables, revenue):
    wci = (receivables + inventory - payables) / revenue.replace(0, np.nan)
    base = wci - wci.rolling(252, min_periods=126).median()
    d1 = _slope(base, 63)
    b = _slope(d1, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk(21d) of payables coverage of inventory
def f29wc_f29_working_capital_inventory_payvsinv_21d_jerk_v053_signal(payables, inventory):
    base = (payables / inventory.replace(0, np.nan)).rolling(63, min_periods=21).mean()
    d1 = _slope(base, 21)
    b = _slope(d1, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk(63d) of payables/inventory z-scored vs
def f29wc_f29_working_capital_inventory_payvsinvz_63d_jerk_v054_signal(payables, inventory):
    r = payables / inventory.replace(0, np.nan)
    base = _z(r, 252)
    d1 = _slope(base, 63)
    b = _slope(d1, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk(21d) of net trade balance
def f29wc_f29_working_capital_inventory_nettrade_21d_jerk_v055_signal(receivables, payables, revenue):
    base = ((receivables - payables) / revenue.replace(0, np.nan)).rolling(63, min_periods=21).mean()
    d1 = _slope(base, 21)
    b = _slope(d1, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk(63d) of net-trade-balance z-scored vs
def f29wc_f29_working_capital_inventory_nettradez_63d_jerk_v056_signal(receivables, payables, revenue):
    r = (receivables - payables) / revenue.replace(0, np.nan)
    base = _z(r, 252)
    d1 = _slope(base, 63)
    b = _slope(d1, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk(63d) of fraction of last year CCC sat
def f29wc_f29_working_capital_inventory_hicccTime_63d_jerk_v057_signal(inventory, receivables, payables, revenue, cor):
    ccc = _f29_ccc(inventory, receivables, payables, revenue, cor)
    med = ccc.rolling(252, min_periods=126).median()
    high = (ccc > med).astype(float)
    base = high.rolling(252, min_periods=126).mean()
    d1 = _slope(base, 63)
    b = _slope(d1, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk(63d) of count of fresh inventory-build
def f29wc_f29_working_capital_inventory_buildonset_63d_jerk_v058_signal(inventory, cor):
    r = inventory / cor.replace(0, np.nan)
    building = (r > r.shift(21)).astype(float)
    entries = ((building == 1) & (building.shift(1) == 0)).astype(float)
    base = entries.rolling(252, min_periods=126).sum() + 0.3 * building.rolling(63, min_periods=21).mean()
    d1 = _slope(base, 63)
    b = _slope(d1, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk(63d) of time inventory/revenue sat in
def f29wc_f29_working_capital_inventory_glutTime_63d_jerk_v059_signal(inventory, revenue):
    r = inventory / revenue.replace(0, np.nan)
    p = _rank(r, 252) + 0.5
    glut = (p > 0.75).astype(float)
    frac = glut.rolling(252, min_periods=126).mean()
    depth = (p - 0.75).clip(lower=0).rolling(63, min_periods=21).mean()
    base = frac + 2.0 * depth
    d1 = _slope(base, 63)
    b = _slope(d1, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk(21d) of stockpile-days displacement: l
def f29wc_f29_working_capital_inventory_invdaysdisp_21d_jerk_v060_signal(inventory, cor):
    r = np.log1p((inventory / cor.replace(0, np.nan)).clip(lower=0))
    base = r - r.ewm(span=126, min_periods=42).mean()
    d1 = _slope(base, 21)
    b = _slope(d1, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk(21d) of DSO displacement: level minus
def f29wc_f29_working_capital_inventory_dsodisp_21d_jerk_v061_signal(receivables, revenue):
    r = receivables / revenue.replace(0, np.nan)
    base = r - r.ewm(span=126, min_periods=42).mean()
    d1 = _slope(base, 21)
    b = _slope(d1, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk(21d) of DPO displacement vs slow EMA
def f29wc_f29_working_capital_inventory_dpodispslow_21d_jerk_v062_signal(payables, cor):
    r = payables / cor.replace(0, np.nan)
    base = r - r.ewm(span=252, min_periods=84).mean()
    d1 = _slope(base, 21)
    b = _slope(d1, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk(21d) of cash-conversion-cycle displace
def f29wc_f29_working_capital_inventory_cccdispslow_21d_jerk_v063_signal(inventory, receivables, payables, revenue, cor):
    ccc = _f29_ccc(inventory, receivables, payables, revenue, cor)
    base = ccc - ccc.ewm(span=252, min_periods=84).mean()
    d1 = _slope(base, 21)
    b = _slope(d1, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk(21d) of stockpile-days distance below
def f29wc_f29_working_capital_inventory_invdaysfromtrough_21d_jerk_v064_signal(inventory, cor):
    r = np.log1p((inventory / cor.replace(0, np.nan)).clip(lower=0))
    hi = _rmax(r, 126)
    lo = _rmin(r, 126)
    base = (hi - r) / (hi - lo).replace(0, np.nan)
    d1 = _slope(base, 21)
    b = _slope(d1, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk(21d) of cash-conversion-cycle position
def f29wc_f29_working_capital_inventory_cccrngpos126_21d_jerk_v065_signal(inventory, receivables, payables, revenue, cor):
    ccc = _f29_ccc(inventory, receivables, payables, revenue, cor)
    hi = _rmax(ccc, 126)
    lo = _rmin(ccc, 126)
    base = (ccc - lo) / (hi - lo).replace(0, np.nan)
    d1 = _slope(base, 21)
    b = _slope(d1, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk(21d) of stockpile-days disagreement ac
def f29wc_f29_working_capital_inventory_invdaysdispmulti_21d_jerk_v066_signal(inventory, cor):
    r = np.log1p((inventory / cor.replace(0, np.nan)).clip(lower=0))
    a = r.rolling(63, min_periods=21).mean()
    b2 = r.rolling(126, min_periods=63).mean()
    c = r.rolling(252, min_periods=126).mean()
    base = pd.concat([a, b2, c], axis=1).std(axis=1)
    d1 = _slope(base, 21)
    b = _slope(d1, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk(21d) of composite working-capital stre
def f29wc_f29_working_capital_inventory_wcstress_21d_jerk_v067_signal(inventory, receivables, payables, revenue, cor):
    invd = np.log1p((inventory / cor.replace(0, np.nan)).clip(lower=0))
    dso = receivables / revenue.replace(0, np.nan)
    invrev = inventory / revenue.replace(0, np.nan)
    base = _z(invd, 252) + _z(dso, 252) + _z(invrev, 252)
    d1 = _slope(base, 21)
    b = _slope(d1, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk(21d) of DPO term ratio
def f29wc_f29_working_capital_inventory_dpoterm_21d_jerk_v068_signal(payables, cor):
    r = payables / cor.replace(0, np.nan)
    short = r.rolling(63, min_periods=21).mean()
    long = r.rolling(252, min_periods=126).mean()
    base = short / long.replace(0, np.nan) - 1.0
    d1 = _slope(base, 21)
    b = _slope(d1, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk(63d) of stockpile-days year-over-year
def f29wc_f29_working_capital_inventory_invdaysyoy_63d_jerk_v069_signal(inventory, cor):
    r = np.log1p((inventory / cor.replace(0, np.nan)).clip(lower=0))
    base = r - r.shift(252)
    d1 = _slope(base, 63)
    b = _slope(d1, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk(63d) of working-capital/current-assets
def f29wc_f29_working_capital_inventory_wcassetsyoy_63d_jerk_v070_signal(receivables, inventory, payables, assetsc):
    nwc = receivables + inventory - payables
    r = nwc / assetsc.replace(0, np.nan)
    base = r - r.shift(252)
    d1 = _slope(base, 63)
    b = _slope(d1, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk(21d) of DSO volatility over a half-yea
def f29wc_f29_working_capital_inventory_dsovol_21d_jerk_v071_signal(receivables, revenue):
    r = receivables / revenue.replace(0, np.nan)
    base = r.rolling(126, min_periods=63).std()
    d1 = _slope(base, 21)
    b = _slope(d1, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk(63d) of inventory/revenue drawdown fro
def f29wc_f29_working_capital_inventory_invrevdd_63d_jerk_v072_signal(inventory, revenue):
    r = inventory / revenue.replace(0, np.nan)
    peak = _rmax(r, 252)
    base = r / peak.replace(0, np.nan) - 1.0
    d1 = _slope(base, 63)
    b = _slope(d1, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk(21d) of inventory turnover
def f29wc_f29_working_capital_inventory_corcov_21d_jerk_v073_signal(cor, inventory):
    base = (cor / inventory.replace(0, np.nan)).rolling(63, min_periods=21).mean()
    d1 = _slope(base, 21)
    b = _slope(d1, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk(21d) of inventory-turnover acceleratio
def f29wc_f29_working_capital_inventory_corcovaccel_21d_jerk_v074_signal(cor, inventory):
    r = cor / inventory.replace(0, np.nan)
    d1 = r - r.shift(63)
    base = d1 - d1.shift(63)
    d1 = _slope(base, 21)
    b = _slope(d1, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk(21d) of current-asset turnover
def f29wc_f29_working_capital_inventory_revassetsc_21d_jerk_v075_signal(revenue, assetsc):
    base = (revenue / assetsc.replace(0, np.nan)).rolling(63, min_periods=21).mean()
    d1 = _slope(base, 21)
    b = _slope(d1, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk(21d) of net-working-capital growth ove
def f29wc_f29_working_capital_inventory_nwcgrowth_21d_jerk_v076_signal(receivables, inventory, payables):
    nwc = (receivables + inventory - payables)
    ln = np.log(nwc.clip(lower=1.0))
    base = ln - ln.shift(63)
    d1 = _slope(base, 21)
    b = _slope(d1, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk(63d) of net-working-capital growth yea
def f29wc_f29_working_capital_inventory_nwcgrowth252_63d_jerk_v077_signal(receivables, inventory, payables):
    nwc = (receivables + inventory - payables)
    ln = np.log(nwc.clip(lower=1.0))
    base = ln - ln.shift(252)
    d1 = _slope(base, 63)
    b = _slope(d1, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk(63d) of stockpile-days position within
def f29wc_f29_working_capital_inventory_invdaysrngpos504_63d_jerk_v078_signal(inventory, cor):
    r = inventory / cor.replace(0, np.nan)
    hi = _rmax(r, 504)
    lo = _rmin(r, 504)
    base = (r - lo) / (hi - lo).replace(0, np.nan)
    d1 = _slope(base, 63)
    b = _slope(d1, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk(63d) of DSO position within its 252d r
def f29wc_f29_working_capital_inventory_dsorngpos_63d_jerk_v079_signal(receivables, revenue):
    r = receivables / revenue.replace(0, np.nan)
    hi = _rmax(r, 252)
    lo = _rmin(r, 252)
    base = (r - lo) / (hi - lo).replace(0, np.nan)
    d1 = _slope(base, 63)
    b = _slope(d1, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk(63d) of working-capital-intensity perc
def f29wc_f29_working_capital_inventory_wcintrank_63d_jerk_v080_signal(receivables, inventory, payables, revenue):
    nwc = receivables + inventory - payables
    base = _rank(nwc / revenue.replace(0, np.nan), 504)
    d1 = _slope(base, 63)
    b = _slope(d1, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk(63d) of inventory/revenue percentile-r
def f29wc_f29_working_capital_inventory_invrevrank_63d_jerk_v081_signal(inventory, revenue):
    base = _rank(inventory / revenue.replace(0, np.nan), 504)
    d1 = _slope(base, 63)
    b = _slope(d1, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk(63d) of stockpile days smoothed over a
def f29wc_f29_working_capital_inventory_invdayssm252_63d_jerk_v082_signal(inventory, cor):
    r = np.log1p((inventory / cor.replace(0, np.nan)).clip(lower=0))
    base = r.rolling(252, min_periods=126).mean()
    d1 = _slope(base, 63)
    b = _slope(d1, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk(63d) of stockpile-days year-scale acce
def f29wc_f29_working_capital_inventory_invdaysyoyacc_63d_jerk_v083_signal(inventory, cor):
    r = np.log1p((inventory / cor.replace(0, np.nan)).clip(lower=0))
    d1 = r - r.shift(126)
    base = d1 - d1.shift(126)
    d1 = _slope(base, 63)
    b = _slope(d1, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk(21d) of stockpile-days z-scored vs 126
def f29wc_f29_working_capital_inventory_invdaysz126_21d_jerk_v084_signal(inventory, cor):
    r = np.log1p((inventory / cor.replace(0, np.nan)).clip(lower=0))
    base = _z(r, 126)
    d1 = _slope(base, 21)
    b = _slope(d1, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk(63d) of change in stockpile-days swing
def f29wc_f29_working_capital_inventory_invdaysswing_63d_jerk_v085_signal(inventory, cor):
    r = np.log1p((inventory / cor.replace(0, np.nan)).clip(lower=0))
    hi = _rmax(r, 252)
    lo = _rmin(r, 252)
    amp = (hi - lo)
    base = amp - amp.shift(126)
    d1 = _slope(base, 63)
    b = _slope(d1, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk(63d) of stockpile-days build off its 5
def f29wc_f29_working_capital_inventory_invdaysmindd_63d_jerk_v086_signal(inventory, cor):
    r = np.log1p((inventory / cor.replace(0, np.nan)).clip(lower=0))
    trough = _rmin(r, 504)
    base = r - trough
    d1 = _slope(base, 63)
    b = _slope(d1, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk(63d) of DSO swing amplitude over a yea
def f29wc_f29_working_capital_inventory_dsoswing_63d_jerk_v087_signal(receivables, revenue):
    r = receivables / revenue.replace(0, np.nan)
    hi = _rmax(r, 252)
    lo = _rmin(r, 252)
    base = (hi - lo) / r.replace(0, np.nan)
    d1 = _slope(base, 63)
    b = _slope(d1, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk(21d) of DSO z-scored vs 126d
def f29wc_f29_working_capital_inventory_dsoz126_21d_jerk_v088_signal(receivables, revenue):
    r = receivables / revenue.replace(0, np.nan)
    base = _z(r, 126)
    d1 = _slope(base, 21)
    b = _slope(d1, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk(63d) of DSO drawdown from 252d peak
def f29wc_f29_working_capital_inventory_dsodd_63d_jerk_v089_signal(receivables, revenue):
    r = receivables / revenue.replace(0, np.nan)
    peak = _rmax(r, 252)
    base = r / peak.replace(0, np.nan) - 1.0
    d1 = _slope(base, 63)
    b = _slope(d1, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk(63d) of DSO position within its 504d r
def f29wc_f29_working_capital_inventory_dsorngpos504_63d_jerk_v090_signal(receivables, revenue):
    r = receivables / revenue.replace(0, np.nan)
    hi = _rmax(r, 504)
    lo = _rmin(r, 504)
    base = (r - lo) / (hi - lo).replace(0, np.nan)
    d1 = _slope(base, 63)
    b = _slope(d1, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk(21d) of DPO smoothed over a half-year
def f29wc_f29_working_capital_inventory_dposm126_21d_jerk_v091_signal(payables, cor):
    r = payables / cor.replace(0, np.nan)
    base = r.rolling(126, min_periods=63).mean()
    d1 = _slope(base, 21)
    b = _slope(d1, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk(63d) of DPO percentile-rank vs 504d
def f29wc_f29_working_capital_inventory_dporank_63d_jerk_v092_signal(payables, cor):
    r = payables / cor.replace(0, np.nan)
    base = _rank(r, 504)
    d1 = _slope(base, 63)
    b = _slope(d1, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk(63d) of DPO year-over-year change
def f29wc_f29_working_capital_inventory_dpoyoy_63d_jerk_v093_signal(payables, cor):
    r = payables / cor.replace(0, np.nan)
    base = r - r.shift(252)
    d1 = _slope(base, 63)
    b = _slope(d1, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk(63d) of inventory/revenue swing amplit
def f29wc_f29_working_capital_inventory_invrevswing504_63d_jerk_v094_signal(inventory, revenue):
    r = inventory / revenue.replace(0, np.nan)
    hi = _rmax(r, 504)
    lo = _rmin(r, 504)
    base = (hi - lo) / r.replace(0, np.nan)
    d1 = _slope(base, 63)
    b = _slope(d1, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk(21d) of inventory/revenue EMA-smoothed
def f29wc_f29_working_capital_inventory_invrevema_21d_jerk_v095_signal(inventory, revenue):
    r = inventory / revenue.replace(0, np.nan)
    base = r.ewm(span=63, min_periods=21).mean()
    d1 = _slope(base, 21)
    b = _slope(d1, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk(21d) of inventory/revenue displacement
def f29wc_f29_working_capital_inventory_invrevdisp_21d_jerk_v096_signal(inventory, revenue):
    r = inventory / revenue.replace(0, np.nan)
    base = r - r.ewm(span=126, min_periods=42).mean()
    d1 = _slope(base, 21)
    b = _slope(d1, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk(21d) of inventory/revenue z-scored vs
def f29wc_f29_working_capital_inventory_invrevz126_21d_jerk_v097_signal(inventory, revenue):
    r = inventory / revenue.replace(0, np.nan)
    base = _z(r, 126)
    d1 = _slope(base, 21)
    b = _slope(d1, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk(63d) of change in cash-conversion-cycl
def f29wc_f29_working_capital_inventory_cccrangeamp_63d_jerk_v098_signal(inventory, receivables, payables, revenue, cor):
    ccc = _f29_ccc(inventory, receivables, payables, revenue, cor)
    amp = _rmax(ccc, 252) - _rmin(ccc, 252)
    base = amp - amp.shift(126)
    d1 = _slope(base, 63)
    b = _slope(d1, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk(21d) of operating-cycle minus double D
def f29wc_f29_working_capital_inventory_cccdpodiff_21d_jerk_v099_signal(inventory, receivables, payables, revenue, cor):
    invd = inventory / cor.replace(0, np.nan)
    dso = receivables / revenue.replace(0, np.nan)
    dpo = payables / cor.replace(0, np.nan)
    operating = invd + dso
    base = operating - 2.0 * dpo
    d1 = _slope(base, 21)
    b = _slope(d1, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk(21d) of cash-conversion-cycle z-scored
def f29wc_f29_working_capital_inventory_cccz126_21d_jerk_v100_signal(inventory, receivables, payables, revenue, cor):
    ccc = _f29_ccc(inventory, receivables, payables, revenue, cor)
    base = _z(ccc, 126)
    d1 = _slope(base, 21)
    b = _slope(d1, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk(63d) of cash-conversion-cycle build of
def f29wc_f29_working_capital_inventory_cccdd_63d_jerk_v101_signal(inventory, receivables, payables, revenue, cor):
    ccc = _f29_ccc(inventory, receivables, payables, revenue, cor)
    trough = _rmin(ccc, 252)
    base = ccc - trough
    d1 = _slope(base, 63)
    b = _slope(d1, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk(21d) of signed-root of cash-conversion
def f29wc_f29_working_capital_inventory_cccsignmag_21d_jerk_v102_signal(inventory, receivables, payables, revenue, cor):
    ccc = _f29_ccc(inventory, receivables, payables, revenue, cor)
    dev = ccc - ccc.rolling(126, min_periods=63).mean()
    base = np.sign(dev) * (dev.abs() ** 0.5)
    d1 = _slope(base, 21)
    b = _slope(d1, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk(63d) of working-capital-intensity posi
def f29wc_f29_working_capital_inventory_wcintrngpos_63d_jerk_v103_signal(receivables, inventory, payables, revenue):
    nwc = receivables + inventory - payables
    wci = nwc / revenue.replace(0, np.nan)
    hi = _rmax(wci, 252)
    lo = _rmin(wci, 252)
    base = (wci - lo) / (hi - lo).replace(0, np.nan)
    d1 = _slope(base, 63)
    b = _slope(d1, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk(63d) of working-capital-intensity year
def f29wc_f29_working_capital_inventory_wcintyoy_63d_jerk_v104_signal(receivables, inventory, payables, revenue):
    nwc = receivables + inventory - payables
    wci = nwc / revenue.replace(0, np.nan)
    base = wci - wci.shift(252)
    d1 = _slope(base, 63)
    b = _slope(d1, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk(63d) of working-capital-intensity vola
def f29wc_f29_working_capital_inventory_wcintvol_63d_jerk_v105_signal(receivables, inventory, payables, revenue):
    nwc = receivables + inventory - payables
    wci = nwc / revenue.replace(0, np.nan)
    base = wci.rolling(252, min_periods=126).std()
    d1 = _slope(base, 63)
    b = _slope(d1, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk(63d) of working-capital/current-assets
def f29wc_f29_working_capital_inventory_wcassetsrank_63d_jerk_v106_signal(receivables, inventory, payables, assetsc):
    nwc = receivables + inventory - payables
    base = _rank(nwc / assetsc.replace(0, np.nan), 504)
    d1 = _slope(base, 63)
    b = _slope(d1, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk(21d) of working-capital/current-assets
def f29wc_f29_working_capital_inventory_wcassetsdisp_21d_jerk_v107_signal(receivables, inventory, payables, assetsc):
    nwc = receivables + inventory - payables
    r = nwc / assetsc.replace(0, np.nan)
    base = r - r.ewm(span=126, min_periods=42).mean()
    d1 = _slope(base, 21)
    b = _slope(d1, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk(21d) of inventory build: log-inventory
def f29wc_f29_working_capital_inventory_invbuild126_21d_jerk_v108_signal(inventory):
    li = np.log(inventory.replace(0, np.nan))
    base = li - li.shift(126)
    d1 = _slope(base, 21)
    b = _slope(d1, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk(21d) of smoothed inventory-build momen
def f29wc_f29_working_capital_inventory_invbuildema_21d_jerk_v109_signal(inventory):
    li = np.log(inventory.replace(0, np.nan))
    chg = li - li.shift(63)
    base = chg.ewm(span=63, min_periods=21).mean()
    d1 = _slope(base, 21)
    b = _slope(d1, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk(63d) of inventory-days relative to its
def f29wc_f29_working_capital_inventory_invturndev_63d_jerk_v110_signal(inventory, cor):
    invd = inventory / cor.replace(0, np.nan)
    base = invd / invd.rolling(252, min_periods=126).mean() - 1.0
    d1 = _slope(base, 63)
    b = _slope(d1, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk(63d) of coefficient of variation of in
def f29wc_f29_working_capital_inventory_invcv_63d_jerk_v111_signal(inventory):
    m = _mean(inventory, 252)
    sd = _std(inventory, 252)
    base = sd / m.replace(0, np.nan)
    d1 = _slope(base, 63)
    b = _slope(d1, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk(63d) of inventory swing amplitude over
def f29wc_f29_working_capital_inventory_invswing_63d_jerk_v112_signal(inventory):
    hi = _rmax(inventory, 504)
    lo = _rmin(inventory, 504)
    base = (hi - lo) / inventory.replace(0, np.nan)
    d1 = _slope(base, 63)
    b = _slope(d1, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk(21d) of inventory turnover smoothed ov
def f29wc_f29_working_capital_inventory_turnsm126_21d_jerk_v113_signal(cor, inventory):
    r = cor / inventory.replace(0, np.nan)
    base = r.rolling(126, min_periods=63).mean()
    d1 = _slope(base, 21)
    b = _slope(d1, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk(63d) of inventory-turnover swing ampli
def f29wc_f29_working_capital_inventory_turnswing_63d_jerk_v114_signal(cor, inventory):
    r = cor / inventory.replace(0, np.nan)
    hi = _rmax(r, 252)
    lo = _rmin(r, 252)
    base = (hi - lo) / r.replace(0, np.nan)
    d1 = _slope(base, 63)
    b = _slope(d1, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk(21d) of inventory-turnover trend over
def f29wc_f29_working_capital_inventory_turntrend_21d_jerk_v115_signal(cor, inventory):
    r = cor / inventory.replace(0, np.nan)
    base = r - r.shift(63)
    d1 = _slope(base, 21)
    b = _slope(d1, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk(21d) of DSO minus inventory-days
def f29wc_f29_working_capital_inventory_recinvspread_21d_jerk_v116_signal(receivables, inventory, revenue, cor):
    dso = receivables / revenue.replace(0, np.nan)
    invd = inventory / cor.replace(0, np.nan)
    base = (dso - invd).rolling(63, min_periods=21).mean()
    d1 = _slope(base, 21)
    b = _slope(d1, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk(63d) of receivables-turnover minus pay
def f29wc_f29_working_capital_inventory_recturndpo_63d_jerk_v117_signal(revenue, receivables, payables, cor):
    rt = revenue / receivables.replace(0, np.nan)
    pt = cor / payables.replace(0, np.nan)
    base = rt - pt
    d1 = _slope(base, 63)
    b = _slope(d1, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk(21d) of payables turnover
def f29wc_f29_working_capital_inventory_payturn_21d_jerk_v118_signal(cor, payables):
    base = (cor / payables.replace(0, np.nan)).rolling(63, min_periods=21).mean()
    d1 = _slope(base, 21)
    b = _slope(d1, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk(63d) of inventory build minus throughp
def f29wc_f29_working_capital_inventory_buildvscor252_63d_jerk_v119_signal(inventory, cor):
    li = np.log(inventory.replace(0, np.nan))
    lc = np.log(cor.replace(0, np.nan))
    base = (li - li.shift(252)) - (lc - lc.shift(252))
    d1 = _slope(base, 63)
    b = _slope(d1, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk(21d) of inventory build minus revenue
def f29wc_f29_working_capital_inventory_buildvsrev126_21d_jerk_v120_signal(inventory, revenue):
    li = np.log(inventory.replace(0, np.nan))
    lr = np.log(revenue.replace(0, np.nan))
    base = (li - li.shift(126)) - (lr - lr.shift(126))
    d1 = _slope(base, 21)
    b = _slope(d1, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk(21d) of receivables growth minus reven
def f29wc_f29_working_capital_inventory_recvsrev126_21d_jerk_v121_signal(receivables, revenue):
    lx = np.log(receivables.replace(0, np.nan))
    lr = np.log(revenue.replace(0, np.nan))
    base = (lx - lx.shift(126)) - (lr - lr.shift(126))
    d1 = _slope(base, 21)
    b = _slope(d1, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk(21d) of payables growth minus cost gro
def f29wc_f29_working_capital_inventory_payvscor_21d_jerk_v122_signal(payables, cor):
    lp = np.log(payables.replace(0, np.nan))
    lc = np.log(cor.replace(0, np.nan))
    base = (lp - lp.shift(63)) - (lc - lc.shift(63))
    d1 = _slope(base, 21)
    b = _slope(d1, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk(21d) of inventory share of
def f29wc_f29_working_capital_inventory_invshareassets_21d_jerk_v123_signal(inventory, receivables, assetsc):
    base = (inventory / (inventory + receivables).replace(0, np.nan)).rolling(63, min_periods=21).mean()
    d1 = _slope(base, 21)
    b = _slope(d1, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk(21d) of DPO minus payables/revenue
def f29wc_f29_working_capital_inventory_paycorvsrev_21d_jerk_v124_signal(payables, cor, revenue):
    dpo = payables / cor.replace(0, np.nan)
    payrev = payables / revenue.replace(0, np.nan)
    base = (dpo - payrev).rolling(63, min_periods=21).mean()
    d1 = _slope(base, 21)
    b = _slope(d1, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk(63d) of inventory-vs-receivables mix z
def f29wc_f29_working_capital_inventory_invmixz_63d_jerk_v125_signal(inventory, receivables):
    mix = inventory / (inventory + receivables).replace(0, np.nan)
    base = _z(mix, 252)
    d1 = _slope(base, 63)
    b = _slope(d1, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk(21d) of payables-to-revenue intensity,
def f29wc_f29_working_capital_inventory_payrevint_21d_jerk_v126_signal(payables, revenue):
    base = (payables / revenue.replace(0, np.nan)).rolling(63, min_periods=21).mean()
    d1 = _slope(base, 21)
    b = _slope(d1, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk(63d) of net-trade-balance percentile-r
def f29wc_f29_working_capital_inventory_nettraderank_63d_jerk_v127_signal(receivables, payables, revenue):
    r = (receivables - payables) / revenue.replace(0, np.nan)
    base = _rank(r, 504)
    d1 = _slope(base, 63)
    b = _slope(d1, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk(63d) of net-trade-balance year-over-ye
def f29wc_f29_working_capital_inventory_nettradeyoy_63d_jerk_v128_signal(receivables, payables, revenue):
    r = (receivables - payables) / revenue.replace(0, np.nan)
    base = r - r.shift(252)
    d1 = _slope(base, 63)
    b = _slope(d1, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk(21d) of payables/inventory smoothed ov
def f29wc_f29_working_capital_inventory_payvsinvsm126_21d_jerk_v129_signal(payables, inventory):
    r = payables / inventory.replace(0, np.nan)
    base = r.rolling(126, min_periods=63).mean()
    d1 = _slope(base, 21)
    b = _slope(d1, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk(21d) of payables/inventory trend over
def f29wc_f29_working_capital_inventory_payvsinvtrend_21d_jerk_v130_signal(payables, inventory):
    r = payables / inventory.replace(0, np.nan)
    base = r - r.shift(63)
    d1 = _slope(base, 21)
    b = _slope(d1, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk(21d) of trend in payables coverage of
def f29wc_f29_working_capital_inventory_payvswctrend_21d_jerk_v131_signal(payables, receivables, inventory):
    nwc = (receivables + inventory).replace(0, np.nan)
    r = payables / nwc
    base = r - r.shift(126)
    d1 = _slope(base, 21)
    b = _slope(d1, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk(21d) of current-assets growth over a q
def f29wc_f29_working_capital_inventory_assetscgrowth_21d_jerk_v132_signal(assetsc):
    la = np.log(assetsc.replace(0, np.nan))
    base = la - la.shift(63)
    d1 = _slope(base, 21)
    b = _slope(d1, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk(63d) of current-assets drawdown from 2
def f29wc_f29_working_capital_inventory_assetscdd_63d_jerk_v133_signal(assetsc):
    peak = _rmax(assetsc, 252)
    base = assetsc / peak.replace(0, np.nan) - 1.0
    d1 = _slope(base, 63)
    b = _slope(d1, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk(63d) of current-asset-turnover z-score
def f29wc_f29_working_capital_inventory_revassetscz_63d_jerk_v134_signal(revenue, assetsc):
    r = revenue / assetsc.replace(0, np.nan)
    base = _z(r, 252)
    d1 = _slope(base, 63)
    b = _slope(d1, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk(21d) of trend in trade-asset share of
def f29wc_f29_working_capital_inventory_illiquidassetstrend_21d_jerk_v135_signal(inventory, receivables, assetsc):
    r = (inventory + receivables) / assetsc.replace(0, np.nan)
    base = r - r.shift(126)
    d1 = _slope(base, 21)
    b = _slope(d1, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk(21d) of inventory/revenue term ratio
def f29wc_f29_working_capital_inventory_invrevterm_21d_jerk_v136_signal(inventory, revenue):
    r = inventory / revenue.replace(0, np.nan)
    short = r.rolling(63, min_periods=21).mean()
    long = r.rolling(252, min_periods=126).mean()
    base = short / long.replace(0, np.nan) - 1.0
    d1 = _slope(base, 21)
    b = _slope(d1, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk(21d) of working-capital-intensity term
def f29wc_f29_working_capital_inventory_wcintterm_21d_jerk_v137_signal(receivables, inventory, payables, revenue):
    nwc = receivables + inventory - payables
    r = nwc / revenue.replace(0, np.nan)
    short = r.rolling(63, min_periods=21).mean()
    long = r.rolling(252, min_periods=126).mean()
    base = short - long
    d1 = _slope(base, 21)
    b = _slope(d1, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk(21d) of inventory-days minus DPO
def f29wc_f29_working_capital_inventory_invpayspread_21d_jerk_v138_signal(inventory, payables, cor):
    invd = inventory / cor.replace(0, np.nan)
    dpo = payables / cor.replace(0, np.nan)
    base = (invd - dpo).rolling(63, min_periods=21).mean()
    d1 = _slope(base, 21)
    b = _slope(d1, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk(21d) of DSO disagreement across short/
def f29wc_f29_working_capital_inventory_dsodispmulti_21d_jerk_v139_signal(receivables, revenue):
    r = receivables / revenue.replace(0, np.nan)
    a = r.rolling(63, min_periods=21).mean()
    b2 = r.rolling(126, min_periods=63).mean()
    c = r.rolling(252, min_periods=126).mean()
    base = pd.concat([a, b2, c], axis=1).std(axis=1)
    d1 = _slope(base, 21)
    b = _slope(d1, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk(63d) of stockpile-days range amplitude
def f29wc_f29_working_capital_inventory_invdaysrangeamp_63d_jerk_v140_signal(inventory, cor):
    r = np.log1p((inventory / cor.replace(0, np.nan)).clip(lower=0))
    hi = _rmax(r, 504)
    lo = _rmin(r, 504)
    base = hi - lo
    d1 = _slope(base, 63)
    b = _slope(d1, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk(21d) of signed-root of stockpile-days
def f29wc_f29_working_capital_inventory_invdayssignroot_21d_jerk_v141_signal(inventory, cor):
    r = inventory / cor.replace(0, np.nan)
    dev = r - r.rolling(252, min_periods=126).mean()
    base = np.sign(dev) * (dev.abs() ** 0.5)
    d1 = _slope(base, 21)
    b = _slope(d1, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk(5d) of tanh-squashed DSO momentum
def f29wc_f29_working_capital_inventory_dsotanh_5d_jerk_v142_signal(receivables, revenue):
    r = receivables / revenue.replace(0, np.nan)
    chg = r - r.shift(21)
    base = np.tanh(15.0 * chg)
    d1 = _slope(base, 5)
    b = _slope(d1, 5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk(63d) of signed-root of inventory/reven
def f29wc_f29_working_capital_inventory_invrevsignmag_63d_jerk_v143_signal(inventory, revenue):
    r = inventory / revenue.replace(0, np.nan)
    typ = r.rolling(252, min_periods=126).mean()
    base = np.sign(r - typ) * ((r - typ).abs() ** 0.5)
    d1 = _slope(base, 63)
    b = _slope(d1, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk(21d) of DSO-to-DPO ratio
def f29wc_f29_working_capital_inventory_dsovsdpo_21d_jerk_v144_signal(receivables, revenue, payables, cor):
    dso = receivables / revenue.replace(0, np.nan)
    dpo = payables / cor.replace(0, np.nan)
    base = (dso / dpo.replace(0, np.nan)).rolling(63, min_periods=21).mean()
    d1 = _slope(base, 21)
    b = _slope(d1, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk(21d) of CCC-z x inventory-build intera
def f29wc_f29_working_capital_inventory_cccXbuild_21d_jerk_v145_signal(inventory, receivables, payables, revenue, cor):
    ccc = _f29_ccc(inventory, receivables, payables, revenue, cor)
    li = np.log(inventory.replace(0, np.nan))
    build = (li - li.shift(63))
    base = (_z(ccc, 252) * build)
    d1 = _slope(base, 21)
    b = _slope(d1, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk(63d) of glut x destock interaction
def f29wc_f29_working_capital_inventory_glutXdestock_63d_jerk_v146_signal(inventory, revenue):
    r = inventory / revenue.replace(0, np.nan)
    glut = (_rank(r, 252)).clip(lower=0)
    li = np.log(inventory.replace(0, np.nan))
    destock = -(li - li.shift(63)).clip(upper=0)
    base = glut * destock
    d1 = _slope(base, 63)
    b = _slope(d1, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk(63d) of time DSO sat in top-quartile
def f29wc_f29_working_capital_inventory_dsostretchTime_63d_jerk_v147_signal(receivables, revenue):
    r = receivables / revenue.replace(0, np.nan)
    p = _rank(r, 252) + 0.5
    stretch = (p > 0.75).astype(float)
    frac = stretch.rolling(252, min_periods=126).mean()
    depth = (p - 0.75).clip(lower=0).rolling(63, min_periods=21).mean()
    base = frac + 2.0 * depth
    d1 = _slope(base, 63)
    b = _slope(d1, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk(21d) of fraction of last half-year inv
def f29wc_f29_working_capital_inventory_buildstreak_21d_jerk_v148_signal(inventory):
    li = np.log(inventory.replace(0, np.nan))
    up = (li > li.shift(21)).astype(float)
    base = up.rolling(126, min_periods=42).mean()
    d1 = _slope(base, 21)
    b = _slope(d1, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk(63d) of time stockpile-days falling
def f29wc_f29_working_capital_inventory_destockTime_63d_jerk_v149_signal(inventory, cor):
    r = inventory / cor.replace(0, np.nan)
    falling = (r < r.shift(21)).astype(float)
    frac = falling.rolling(252, min_periods=126).mean()
    li = np.log(inventory.replace(0, np.nan))
    depth = (-(li - li.shift(21)).clip(upper=0)).rolling(63, min_periods=21).mean()
    base = frac + 3.0 * depth
    d1 = _slope(base, 63)
    b = _slope(d1, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# jerk(63d) of fraction of last year working-
def f29wc_f29_working_capital_inventory_wcTighteningTime_63d_jerk_v150_signal(receivables, inventory, payables, revenue):
    nwc = receivables + inventory - payables
    wci = nwc / revenue.replace(0, np.nan)
    tight = (wci > wci.shift(63)).astype(float)
    base = tight.rolling(252, min_periods=126).mean()
    d1 = _slope(base, 63)
    b = _slope(d1, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f29wc_f29_working_capital_inventory_invdays_21d_jerk_v001_signal,
    f29wc_f29_working_capital_inventory_invdaysshortlong_21d_jerk_v002_signal,
    f29wc_f29_working_capital_inventory_invdaysz_63d_jerk_v003_signal,
    f29wc_f29_working_capital_inventory_invdaysrank_63d_jerk_v004_signal,
    f29wc_f29_working_capital_inventory_invdaysdd_63d_jerk_v005_signal,
    f29wc_f29_working_capital_inventory_dso_21d_jerk_v006_signal,
    f29wc_f29_working_capital_inventory_dsoz_63d_jerk_v007_signal,
    f29wc_f29_working_capital_inventory_dsorank_63d_jerk_v008_signal,
    f29wc_f29_working_capital_inventory_dsoyoy_63d_jerk_v009_signal,
    f29wc_f29_working_capital_inventory_dpo_21d_jerk_v010_signal,
    f29wc_f29_working_capital_inventory_dpoz_63d_jerk_v011_signal,
    f29wc_f29_working_capital_inventory_invrev_21d_jerk_v012_signal,
    f29wc_f29_working_capital_inventory_invrevz_63d_jerk_v013_signal,
    f29wc_f29_working_capital_inventory_invrevyoy_63d_jerk_v014_signal,
    f29wc_f29_working_capital_inventory_ccc_21d_jerk_v015_signal,
    f29wc_f29_working_capital_inventory_cccz_63d_jerk_v016_signal,
    f29wc_f29_working_capital_inventory_cccrank_63d_jerk_v017_signal,
    f29wc_f29_working_capital_inventory_cccyoy_63d_jerk_v018_signal,
    f29wc_f29_working_capital_inventory_wcint_21d_jerk_v019_signal,
    f29wc_f29_working_capital_inventory_wcintz_63d_jerk_v020_signal,
    f29wc_f29_working_capital_inventory_wcassetsgap_21d_jerk_v021_signal,
    f29wc_f29_working_capital_inventory_wcassetsz_63d_jerk_v022_signal,
    f29wc_f29_working_capital_inventory_invbuild_21d_jerk_v023_signal,
    f29wc_f29_working_capital_inventory_invbuild_63d_jerk_v024_signal,
    f29wc_f29_working_capital_inventory_invdd_63d_jerk_v025_signal,
    f29wc_f29_working_capital_inventory_invz_63d_jerk_v026_signal,
    f29wc_f29_working_capital_inventory_invrank_63d_jerk_v027_signal,
    f29wc_f29_working_capital_inventory_buildvscor_21d_jerk_v028_signal,
    f29wc_f29_working_capital_inventory_buildvsrev_21d_jerk_v029_signal,
    f29wc_f29_working_capital_inventory_recvsrev_21d_jerk_v030_signal,
    f29wc_f29_working_capital_inventory_invdaysterm_21d_jerk_v031_signal,
    f29wc_f29_working_capital_inventory_dsoterm_21d_jerk_v032_signal,
    f29wc_f29_working_capital_inventory_cccterm_21d_jerk_v033_signal,
    f29wc_f29_working_capital_inventory_invdaysvol_21d_jerk_v034_signal,
    f29wc_f29_working_capital_inventory_cccvol_63d_jerk_v035_signal,
    f29wc_f29_working_capital_inventory_invrevcv_63d_jerk_v036_signal,
    f29wc_f29_working_capital_inventory_invrevphase_63d_jerk_v037_signal,
    f29wc_f29_working_capital_inventory_cccswing_63d_jerk_v038_signal,
    f29wc_f29_working_capital_inventory_invdaysrngpos_63d_jerk_v039_signal,
    f29wc_f29_working_capital_inventory_cccrngpos_63d_jerk_v040_signal,
    f29wc_f29_working_capital_inventory_invshare_21d_jerk_v041_signal,
    f29wc_f29_working_capital_inventory_recshare_21d_jerk_v042_signal,
    f29wc_f29_working_capital_inventory_invassetscz_63d_jerk_v043_signal,
    f29wc_f29_working_capital_inventory_recassetsc_21d_jerk_v044_signal,
    f29wc_f29_working_capital_inventory_assetscz_63d_jerk_v045_signal,
    f29wc_f29_working_capital_inventory_invdaystrend_21d_jerk_v046_signal,
    f29wc_f29_working_capital_inventory_cccyoy2_21d_jerk_v047_signal,
    f29wc_f29_working_capital_inventory_wcinttrend_21d_jerk_v048_signal,
    f29wc_f29_working_capital_inventory_cccsignroot_21d_jerk_v049_signal,
    f29wc_f29_working_capital_inventory_invbuildtanh_5d_jerk_v050_signal,
    f29wc_f29_working_capital_inventory_glutreliefX_21d_jerk_v051_signal,
    f29wc_f29_working_capital_inventory_wcintdev_63d_jerk_v052_signal,
    f29wc_f29_working_capital_inventory_payvsinv_21d_jerk_v053_signal,
    f29wc_f29_working_capital_inventory_payvsinvz_63d_jerk_v054_signal,
    f29wc_f29_working_capital_inventory_nettrade_21d_jerk_v055_signal,
    f29wc_f29_working_capital_inventory_nettradez_63d_jerk_v056_signal,
    f29wc_f29_working_capital_inventory_hicccTime_63d_jerk_v057_signal,
    f29wc_f29_working_capital_inventory_buildonset_63d_jerk_v058_signal,
    f29wc_f29_working_capital_inventory_glutTime_63d_jerk_v059_signal,
    f29wc_f29_working_capital_inventory_invdaysdisp_21d_jerk_v060_signal,
    f29wc_f29_working_capital_inventory_dsodisp_21d_jerk_v061_signal,
    f29wc_f29_working_capital_inventory_dpodispslow_21d_jerk_v062_signal,
    f29wc_f29_working_capital_inventory_cccdispslow_21d_jerk_v063_signal,
    f29wc_f29_working_capital_inventory_invdaysfromtrough_21d_jerk_v064_signal,
    f29wc_f29_working_capital_inventory_cccrngpos126_21d_jerk_v065_signal,
    f29wc_f29_working_capital_inventory_invdaysdispmulti_21d_jerk_v066_signal,
    f29wc_f29_working_capital_inventory_wcstress_21d_jerk_v067_signal,
    f29wc_f29_working_capital_inventory_dpoterm_21d_jerk_v068_signal,
    f29wc_f29_working_capital_inventory_invdaysyoy_63d_jerk_v069_signal,
    f29wc_f29_working_capital_inventory_wcassetsyoy_63d_jerk_v070_signal,
    f29wc_f29_working_capital_inventory_dsovol_21d_jerk_v071_signal,
    f29wc_f29_working_capital_inventory_invrevdd_63d_jerk_v072_signal,
    f29wc_f29_working_capital_inventory_corcov_21d_jerk_v073_signal,
    f29wc_f29_working_capital_inventory_corcovaccel_21d_jerk_v074_signal,
    f29wc_f29_working_capital_inventory_revassetsc_21d_jerk_v075_signal,
    f29wc_f29_working_capital_inventory_nwcgrowth_21d_jerk_v076_signal,
    f29wc_f29_working_capital_inventory_nwcgrowth252_63d_jerk_v077_signal,
    f29wc_f29_working_capital_inventory_invdaysrngpos504_63d_jerk_v078_signal,
    f29wc_f29_working_capital_inventory_dsorngpos_63d_jerk_v079_signal,
    f29wc_f29_working_capital_inventory_wcintrank_63d_jerk_v080_signal,
    f29wc_f29_working_capital_inventory_invrevrank_63d_jerk_v081_signal,
    f29wc_f29_working_capital_inventory_invdayssm252_63d_jerk_v082_signal,
    f29wc_f29_working_capital_inventory_invdaysyoyacc_63d_jerk_v083_signal,
    f29wc_f29_working_capital_inventory_invdaysz126_21d_jerk_v084_signal,
    f29wc_f29_working_capital_inventory_invdaysswing_63d_jerk_v085_signal,
    f29wc_f29_working_capital_inventory_invdaysmindd_63d_jerk_v086_signal,
    f29wc_f29_working_capital_inventory_dsoswing_63d_jerk_v087_signal,
    f29wc_f29_working_capital_inventory_dsoz126_21d_jerk_v088_signal,
    f29wc_f29_working_capital_inventory_dsodd_63d_jerk_v089_signal,
    f29wc_f29_working_capital_inventory_dsorngpos504_63d_jerk_v090_signal,
    f29wc_f29_working_capital_inventory_dposm126_21d_jerk_v091_signal,
    f29wc_f29_working_capital_inventory_dporank_63d_jerk_v092_signal,
    f29wc_f29_working_capital_inventory_dpoyoy_63d_jerk_v093_signal,
    f29wc_f29_working_capital_inventory_invrevswing504_63d_jerk_v094_signal,
    f29wc_f29_working_capital_inventory_invrevema_21d_jerk_v095_signal,
    f29wc_f29_working_capital_inventory_invrevdisp_21d_jerk_v096_signal,
    f29wc_f29_working_capital_inventory_invrevz126_21d_jerk_v097_signal,
    f29wc_f29_working_capital_inventory_cccrangeamp_63d_jerk_v098_signal,
    f29wc_f29_working_capital_inventory_cccdpodiff_21d_jerk_v099_signal,
    f29wc_f29_working_capital_inventory_cccz126_21d_jerk_v100_signal,
    f29wc_f29_working_capital_inventory_cccdd_63d_jerk_v101_signal,
    f29wc_f29_working_capital_inventory_cccsignmag_21d_jerk_v102_signal,
    f29wc_f29_working_capital_inventory_wcintrngpos_63d_jerk_v103_signal,
    f29wc_f29_working_capital_inventory_wcintyoy_63d_jerk_v104_signal,
    f29wc_f29_working_capital_inventory_wcintvol_63d_jerk_v105_signal,
    f29wc_f29_working_capital_inventory_wcassetsrank_63d_jerk_v106_signal,
    f29wc_f29_working_capital_inventory_wcassetsdisp_21d_jerk_v107_signal,
    f29wc_f29_working_capital_inventory_invbuild126_21d_jerk_v108_signal,
    f29wc_f29_working_capital_inventory_invbuildema_21d_jerk_v109_signal,
    f29wc_f29_working_capital_inventory_invturndev_63d_jerk_v110_signal,
    f29wc_f29_working_capital_inventory_invcv_63d_jerk_v111_signal,
    f29wc_f29_working_capital_inventory_invswing_63d_jerk_v112_signal,
    f29wc_f29_working_capital_inventory_turnsm126_21d_jerk_v113_signal,
    f29wc_f29_working_capital_inventory_turnswing_63d_jerk_v114_signal,
    f29wc_f29_working_capital_inventory_turntrend_21d_jerk_v115_signal,
    f29wc_f29_working_capital_inventory_recinvspread_21d_jerk_v116_signal,
    f29wc_f29_working_capital_inventory_recturndpo_63d_jerk_v117_signal,
    f29wc_f29_working_capital_inventory_payturn_21d_jerk_v118_signal,
    f29wc_f29_working_capital_inventory_buildvscor252_63d_jerk_v119_signal,
    f29wc_f29_working_capital_inventory_buildvsrev126_21d_jerk_v120_signal,
    f29wc_f29_working_capital_inventory_recvsrev126_21d_jerk_v121_signal,
    f29wc_f29_working_capital_inventory_payvscor_21d_jerk_v122_signal,
    f29wc_f29_working_capital_inventory_invshareassets_21d_jerk_v123_signal,
    f29wc_f29_working_capital_inventory_paycorvsrev_21d_jerk_v124_signal,
    f29wc_f29_working_capital_inventory_invmixz_63d_jerk_v125_signal,
    f29wc_f29_working_capital_inventory_payrevint_21d_jerk_v126_signal,
    f29wc_f29_working_capital_inventory_nettraderank_63d_jerk_v127_signal,
    f29wc_f29_working_capital_inventory_nettradeyoy_63d_jerk_v128_signal,
    f29wc_f29_working_capital_inventory_payvsinvsm126_21d_jerk_v129_signal,
    f29wc_f29_working_capital_inventory_payvsinvtrend_21d_jerk_v130_signal,
    f29wc_f29_working_capital_inventory_payvswctrend_21d_jerk_v131_signal,
    f29wc_f29_working_capital_inventory_assetscgrowth_21d_jerk_v132_signal,
    f29wc_f29_working_capital_inventory_assetscdd_63d_jerk_v133_signal,
    f29wc_f29_working_capital_inventory_revassetscz_63d_jerk_v134_signal,
    f29wc_f29_working_capital_inventory_illiquidassetstrend_21d_jerk_v135_signal,
    f29wc_f29_working_capital_inventory_invrevterm_21d_jerk_v136_signal,
    f29wc_f29_working_capital_inventory_wcintterm_21d_jerk_v137_signal,
    f29wc_f29_working_capital_inventory_invpayspread_21d_jerk_v138_signal,
    f29wc_f29_working_capital_inventory_dsodispmulti_21d_jerk_v139_signal,
    f29wc_f29_working_capital_inventory_invdaysrangeamp_63d_jerk_v140_signal,
    f29wc_f29_working_capital_inventory_invdayssignroot_21d_jerk_v141_signal,
    f29wc_f29_working_capital_inventory_dsotanh_5d_jerk_v142_signal,
    f29wc_f29_working_capital_inventory_invrevsignmag_63d_jerk_v143_signal,
    f29wc_f29_working_capital_inventory_dsovsdpo_21d_jerk_v144_signal,
    f29wc_f29_working_capital_inventory_cccXbuild_21d_jerk_v145_signal,
    f29wc_f29_working_capital_inventory_glutXdestock_63d_jerk_v146_signal,
    f29wc_f29_working_capital_inventory_dsostretchTime_63d_jerk_v147_signal,
    f29wc_f29_working_capital_inventory_buildstreak_21d_jerk_v148_signal,
    f29wc_f29_working_capital_inventory_destockTime_63d_jerk_v149_signal,
    f29wc_f29_working_capital_inventory_wcTighteningTime_63d_jerk_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F29_WORKING_CAPITAL_INVENTORY_REGISTRY_JERK_001_150 = REGISTRY


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

    print("OK f29_working_capital_inventory_3rd_derivatives_001_150_claude: %d features pass" % n_features)
