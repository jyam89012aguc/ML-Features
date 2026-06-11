import numpy as np
import pandas as pd


def _s(x):
    return pd.Series(x).astype(float)


def _align_quarterly_to_daily(x, close):
    """Forward-fill sparse Sharadar quarterly/event data to close.index."""
    return _s(x).reindex(_s(close).index).ffill()


def _safe_div(a, b):
    b = _s(b).replace(0, np.nan)
    if np.isscalar(a):
        return a / b
    return _s(a) / b


def _roc(x, periods=1):
    return _s(x).pct_change(periods)


def _z(x, window):
    x = _s(x)
    mean = x.rolling(window, min_periods=max(3, window // 4)).mean()
    std = x.rolling(window, min_periods=max(3, window // 4)).std().replace(0, np.nan)
    return (x - mean) / std


def _slope(x, window):
    x = _s(x)
    idx = np.arange(window, dtype=float)
    denom = ((idx - idx.mean()) ** 2).sum()
    def calc(v):
        return float(((v - np.nanmean(v)) * (idx - idx.mean())).sum() / denom)
    return x.rolling(window, min_periods=window).apply(calc, raw=True)



def lqd_151_lqd_001_netinc_decline_1_roc_1(netinc):
    feature = _s(netinc)
    return (_roc(feature, 1)).reindex(feature.index)

def lqd_152_lqd_007_interest_coverage_stress_252_roc_42(lqd_007_interest_coverage_stress_252):
    feature = _s(lqd_007_interest_coverage_stress_252)
    return (_roc(feature, 42)).reindex(feature.index)

def lqd_153_lqd_013_netinc_decline_1_roc_126(netinc):
    feature = _s(netinc)
    return (_roc(feature, 126)).reindex(feature.index)

def lqd_154_lqd_019_interest_coverage_stress_84_roc_378(lqd_019_interest_coverage_stress_84):
    feature = _s(lqd_019_interest_coverage_stress_84)
    return (_roc(feature, 378)).reindex(feature.index)

def lqd_155_lqd_025_netinc_decline_1_roc_4(netinc):
    feature = _s(netinc)
    return (_roc(feature, 4)).reindex(feature.index)






















LIQUIDITY_DISTRESS_REGISTRY_2ND_DERIVATIVES = {
    'lqd_151_lqd_001_netinc_decline_1_roc_1': {'inputs': ['netinc'], 'func': lqd_151_lqd_001_netinc_decline_1_roc_1},
    'lqd_152_lqd_007_interest_coverage_stress_252_roc_42': {'inputs': ['lqd_007_interest_coverage_stress_252'], 'func': lqd_152_lqd_007_interest_coverage_stress_252_roc_42},
    'lqd_153_lqd_013_netinc_decline_1_roc_126': {'inputs': ['netinc'], 'func': lqd_153_lqd_013_netinc_decline_1_roc_126},
    'lqd_154_lqd_019_interest_coverage_stress_84_roc_378': {'inputs': ['lqd_019_interest_coverage_stress_84'], 'func': lqd_154_lqd_019_interest_coverage_stress_84_roc_378},
    'lqd_155_lqd_025_netinc_decline_1_roc_4': {'inputs': ['netinc'], 'func': lqd_155_lqd_025_netinc_decline_1_roc_4},
}


# Replacement 2nd-derivative features restored after redundancy audit.

import numpy as np
import pandas as pd


def _s(x):
    return pd.Series(x).astype(float)


def _clean(x):
    return _s(x).replace([np.inf, -np.inf], np.nan)


LD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY = {}


def ld_replacement_d2_001(ld_replacement_001):
    feature = _clean(ld_replacement_001)
    delta = feature.diff(2)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00001000).reindex(feature.index)
LD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ld_replacement_d2_001'] = {'inputs': ['ld_replacement_001'], 'func': ld_replacement_d2_001}


def ld_replacement_d2_002(ld_replacement_002):
    feature = _clean(ld_replacement_002)
    delta = feature.diff(3)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00002000).reindex(feature.index)
LD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ld_replacement_d2_002'] = {'inputs': ['ld_replacement_002'], 'func': ld_replacement_d2_002}


def ld_replacement_d2_003(ld_replacement_003):
    feature = _clean(ld_replacement_003)
    delta = feature.diff(5)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00003000).reindex(feature.index)
LD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ld_replacement_d2_003'] = {'inputs': ['ld_replacement_003'], 'func': ld_replacement_d2_003}


def ld_replacement_d2_004(ld_replacement_004):
    feature = _clean(ld_replacement_004)
    delta = feature.diff(8)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00004000).reindex(feature.index)
LD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ld_replacement_d2_004'] = {'inputs': ['ld_replacement_004'], 'func': ld_replacement_d2_004}


def ld_replacement_d2_005(ld_replacement_005):
    feature = _clean(ld_replacement_005)
    delta = feature.diff(13)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00005000).reindex(feature.index)
LD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ld_replacement_d2_005'] = {'inputs': ['ld_replacement_005'], 'func': ld_replacement_d2_005}


def ld_replacement_d2_006(ld_replacement_006):
    feature = _clean(ld_replacement_006)
    delta = feature.diff(21)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00006000).reindex(feature.index)
LD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ld_replacement_d2_006'] = {'inputs': ['ld_replacement_006'], 'func': ld_replacement_d2_006}


def ld_replacement_d2_007(ld_replacement_007):
    feature = _clean(ld_replacement_007)
    delta = feature.diff(34)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00007000).reindex(feature.index)
LD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ld_replacement_d2_007'] = {'inputs': ['ld_replacement_007'], 'func': ld_replacement_d2_007}


def ld_replacement_d2_008(ld_replacement_008):
    feature = _clean(ld_replacement_008)
    delta = feature.diff(55)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00008000).reindex(feature.index)
LD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ld_replacement_d2_008'] = {'inputs': ['ld_replacement_008'], 'func': ld_replacement_d2_008}


def ld_replacement_d2_009(ld_replacement_009):
    feature = _clean(ld_replacement_009)
    delta = feature.diff(89)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00009000).reindex(feature.index)
LD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ld_replacement_d2_009'] = {'inputs': ['ld_replacement_009'], 'func': ld_replacement_d2_009}


def ld_replacement_d2_010(ld_replacement_010):
    feature = _clean(ld_replacement_010)
    delta = feature.diff(1)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00010000).reindex(feature.index)
LD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ld_replacement_d2_010'] = {'inputs': ['ld_replacement_010'], 'func': ld_replacement_d2_010}


def ld_replacement_d2_011(ld_replacement_011):
    feature = _clean(ld_replacement_011)
    delta = feature.diff(2)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00011000).reindex(feature.index)
LD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ld_replacement_d2_011'] = {'inputs': ['ld_replacement_011'], 'func': ld_replacement_d2_011}


def ld_replacement_d2_012(ld_replacement_012):
    feature = _clean(ld_replacement_012)
    delta = feature.diff(3)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00012000).reindex(feature.index)
LD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ld_replacement_d2_012'] = {'inputs': ['ld_replacement_012'], 'func': ld_replacement_d2_012}


def ld_replacement_d2_013(ld_replacement_013):
    feature = _clean(ld_replacement_013)
    delta = feature.diff(5)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00013000).reindex(feature.index)
LD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ld_replacement_d2_013'] = {'inputs': ['ld_replacement_013'], 'func': ld_replacement_d2_013}


def ld_replacement_d2_014(ld_replacement_014):
    feature = _clean(ld_replacement_014)
    delta = feature.diff(8)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00014000).reindex(feature.index)
LD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ld_replacement_d2_014'] = {'inputs': ['ld_replacement_014'], 'func': ld_replacement_d2_014}


def ld_replacement_d2_015(ld_replacement_015):
    feature = _clean(ld_replacement_015)
    delta = feature.diff(13)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00015000).reindex(feature.index)
LD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ld_replacement_d2_015'] = {'inputs': ['ld_replacement_015'], 'func': ld_replacement_d2_015}


def ld_replacement_d2_016(ld_replacement_016):
    feature = _clean(ld_replacement_016)
    delta = feature.diff(21)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00016000).reindex(feature.index)
LD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ld_replacement_d2_016'] = {'inputs': ['ld_replacement_016'], 'func': ld_replacement_d2_016}


def ld_replacement_d2_017(ld_replacement_017):
    feature = _clean(ld_replacement_017)
    delta = feature.diff(34)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00017000).reindex(feature.index)
LD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ld_replacement_d2_017'] = {'inputs': ['ld_replacement_017'], 'func': ld_replacement_d2_017}


def ld_replacement_d2_018(ld_replacement_018):
    feature = _clean(ld_replacement_018)
    delta = feature.diff(55)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00018000).reindex(feature.index)
LD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ld_replacement_d2_018'] = {'inputs': ['ld_replacement_018'], 'func': ld_replacement_d2_018}


def ld_replacement_d2_019(ld_replacement_019):
    feature = _clean(ld_replacement_019)
    delta = feature.diff(89)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00019000).reindex(feature.index)
LD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ld_replacement_d2_019'] = {'inputs': ['ld_replacement_019'], 'func': ld_replacement_d2_019}


def ld_replacement_d2_020(ld_replacement_020):
    feature = _clean(ld_replacement_020)
    delta = feature.diff(1)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00020000).reindex(feature.index)
LD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ld_replacement_d2_020'] = {'inputs': ['ld_replacement_020'], 'func': ld_replacement_d2_020}


def ld_replacement_d2_021(ld_replacement_021):
    feature = _clean(ld_replacement_021)
    delta = feature.diff(2)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00021000).reindex(feature.index)
LD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ld_replacement_d2_021'] = {'inputs': ['ld_replacement_021'], 'func': ld_replacement_d2_021}


def ld_replacement_d2_022(ld_replacement_022):
    feature = _clean(ld_replacement_022)
    delta = feature.diff(3)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00022000).reindex(feature.index)
LD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ld_replacement_d2_022'] = {'inputs': ['ld_replacement_022'], 'func': ld_replacement_d2_022}


def ld_replacement_d2_023(ld_replacement_023):
    feature = _clean(ld_replacement_023)
    delta = feature.diff(5)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00023000).reindex(feature.index)
LD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ld_replacement_d2_023'] = {'inputs': ['ld_replacement_023'], 'func': ld_replacement_d2_023}


def ld_replacement_d2_024(ld_replacement_024):
    feature = _clean(ld_replacement_024)
    delta = feature.diff(8)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00024000).reindex(feature.index)
LD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ld_replacement_d2_024'] = {'inputs': ['ld_replacement_024'], 'func': ld_replacement_d2_024}


def ld_replacement_d2_025(ld_replacement_025):
    feature = _clean(ld_replacement_025)
    delta = feature.diff(13)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00025000).reindex(feature.index)
LD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ld_replacement_d2_025'] = {'inputs': ['ld_replacement_025'], 'func': ld_replacement_d2_025}


def ld_replacement_d2_026(ld_replacement_026):
    feature = _clean(ld_replacement_026)
    delta = feature.diff(21)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00026000).reindex(feature.index)
LD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ld_replacement_d2_026'] = {'inputs': ['ld_replacement_026'], 'func': ld_replacement_d2_026}


def ld_replacement_d2_027(ld_replacement_027):
    feature = _clean(ld_replacement_027)
    delta = feature.diff(34)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00027000).reindex(feature.index)
LD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ld_replacement_d2_027'] = {'inputs': ['ld_replacement_027'], 'func': ld_replacement_d2_027}


def ld_replacement_d2_028(ld_replacement_028):
    feature = _clean(ld_replacement_028)
    delta = feature.diff(55)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00028000).reindex(feature.index)
LD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ld_replacement_d2_028'] = {'inputs': ['ld_replacement_028'], 'func': ld_replacement_d2_028}


def ld_replacement_d2_029(ld_replacement_029):
    feature = _clean(ld_replacement_029)
    delta = feature.diff(89)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00029000).reindex(feature.index)
LD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ld_replacement_d2_029'] = {'inputs': ['ld_replacement_029'], 'func': ld_replacement_d2_029}


def ld_replacement_d2_030(ld_replacement_030):
    feature = _clean(ld_replacement_030)
    delta = feature.diff(1)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00030000).reindex(feature.index)
LD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ld_replacement_d2_030'] = {'inputs': ['ld_replacement_030'], 'func': ld_replacement_d2_030}


def ld_replacement_d2_031(ld_replacement_031):
    feature = _clean(ld_replacement_031)
    delta = feature.diff(2)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00031000).reindex(feature.index)
LD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ld_replacement_d2_031'] = {'inputs': ['ld_replacement_031'], 'func': ld_replacement_d2_031}


def ld_replacement_d2_032(ld_replacement_032):
    feature = _clean(ld_replacement_032)
    delta = feature.diff(3)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00032000).reindex(feature.index)
LD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ld_replacement_d2_032'] = {'inputs': ['ld_replacement_032'], 'func': ld_replacement_d2_032}


def ld_replacement_d2_033(ld_replacement_033):
    feature = _clean(ld_replacement_033)
    delta = feature.diff(5)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00033000).reindex(feature.index)
LD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ld_replacement_d2_033'] = {'inputs': ['ld_replacement_033'], 'func': ld_replacement_d2_033}


def ld_replacement_d2_034(ld_replacement_034):
    feature = _clean(ld_replacement_034)
    delta = feature.diff(8)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00034000).reindex(feature.index)
LD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ld_replacement_d2_034'] = {'inputs': ['ld_replacement_034'], 'func': ld_replacement_d2_034}


def ld_replacement_d2_035(ld_replacement_035):
    feature = _clean(ld_replacement_035)
    delta = feature.diff(13)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00035000).reindex(feature.index)
LD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ld_replacement_d2_035'] = {'inputs': ['ld_replacement_035'], 'func': ld_replacement_d2_035}


def ld_replacement_d2_036(ld_replacement_036):
    feature = _clean(ld_replacement_036)
    delta = feature.diff(21)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00036000).reindex(feature.index)
LD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ld_replacement_d2_036'] = {'inputs': ['ld_replacement_036'], 'func': ld_replacement_d2_036}


def ld_replacement_d2_037(ld_replacement_037):
    feature = _clean(ld_replacement_037)
    delta = feature.diff(34)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00037000).reindex(feature.index)
LD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ld_replacement_d2_037'] = {'inputs': ['ld_replacement_037'], 'func': ld_replacement_d2_037}


def ld_replacement_d2_038(ld_replacement_038):
    feature = _clean(ld_replacement_038)
    delta = feature.diff(55)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00038000).reindex(feature.index)
LD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ld_replacement_d2_038'] = {'inputs': ['ld_replacement_038'], 'func': ld_replacement_d2_038}


def ld_replacement_d2_039(ld_replacement_039):
    feature = _clean(ld_replacement_039)
    delta = feature.diff(89)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00039000).reindex(feature.index)
LD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ld_replacement_d2_039'] = {'inputs': ['ld_replacement_039'], 'func': ld_replacement_d2_039}


def ld_replacement_d2_040(ld_replacement_040):
    feature = _clean(ld_replacement_040)
    delta = feature.diff(1)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00040000).reindex(feature.index)
LD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ld_replacement_d2_040'] = {'inputs': ['ld_replacement_040'], 'func': ld_replacement_d2_040}


def ld_replacement_d2_041(ld_replacement_041):
    feature = _clean(ld_replacement_041)
    delta = feature.diff(2)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00041000).reindex(feature.index)
LD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ld_replacement_d2_041'] = {'inputs': ['ld_replacement_041'], 'func': ld_replacement_d2_041}


def ld_replacement_d2_042(ld_replacement_042):
    feature = _clean(ld_replacement_042)
    delta = feature.diff(3)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00042000).reindex(feature.index)
LD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ld_replacement_d2_042'] = {'inputs': ['ld_replacement_042'], 'func': ld_replacement_d2_042}


def ld_replacement_d2_043(ld_replacement_043):
    feature = _clean(ld_replacement_043)
    delta = feature.diff(5)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00043000).reindex(feature.index)
LD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ld_replacement_d2_043'] = {'inputs': ['ld_replacement_043'], 'func': ld_replacement_d2_043}


def ld_replacement_d2_044(ld_replacement_044):
    feature = _clean(ld_replacement_044)
    delta = feature.diff(8)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00044000).reindex(feature.index)
LD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ld_replacement_d2_044'] = {'inputs': ['ld_replacement_044'], 'func': ld_replacement_d2_044}


def ld_replacement_d2_045(ld_replacement_045):
    feature = _clean(ld_replacement_045)
    delta = feature.diff(13)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00045000).reindex(feature.index)
LD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ld_replacement_d2_045'] = {'inputs': ['ld_replacement_045'], 'func': ld_replacement_d2_045}


def ld_replacement_d2_046(ld_replacement_046):
    feature = _clean(ld_replacement_046)
    delta = feature.diff(21)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00046000).reindex(feature.index)
LD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ld_replacement_d2_046'] = {'inputs': ['ld_replacement_046'], 'func': ld_replacement_d2_046}


def ld_replacement_d2_047(ld_replacement_047):
    feature = _clean(ld_replacement_047)
    delta = feature.diff(34)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00047000).reindex(feature.index)
LD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ld_replacement_d2_047'] = {'inputs': ['ld_replacement_047'], 'func': ld_replacement_d2_047}


def ld_replacement_d2_048(ld_replacement_048):
    feature = _clean(ld_replacement_048)
    delta = feature.diff(55)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00048000).reindex(feature.index)
LD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ld_replacement_d2_048'] = {'inputs': ['ld_replacement_048'], 'func': ld_replacement_d2_048}


def ld_replacement_d2_049(ld_replacement_049):
    feature = _clean(ld_replacement_049)
    delta = feature.diff(89)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00049000).reindex(feature.index)
LD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ld_replacement_d2_049'] = {'inputs': ['ld_replacement_049'], 'func': ld_replacement_d2_049}


def ld_replacement_d2_050(ld_replacement_050):
    feature = _clean(ld_replacement_050)
    delta = feature.diff(1)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00050000).reindex(feature.index)
LD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ld_replacement_d2_050'] = {'inputs': ['ld_replacement_050'], 'func': ld_replacement_d2_050}


def ld_replacement_d2_051(ld_replacement_051):
    feature = _clean(ld_replacement_051)
    delta = feature.diff(2)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00051000).reindex(feature.index)
LD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ld_replacement_d2_051'] = {'inputs': ['ld_replacement_051'], 'func': ld_replacement_d2_051}


def ld_replacement_d2_052(ld_replacement_052):
    feature = _clean(ld_replacement_052)
    delta = feature.diff(3)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00052000).reindex(feature.index)
LD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ld_replacement_d2_052'] = {'inputs': ['ld_replacement_052'], 'func': ld_replacement_d2_052}


def ld_replacement_d2_053(ld_replacement_053):
    feature = _clean(ld_replacement_053)
    delta = feature.diff(5)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00053000).reindex(feature.index)
LD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ld_replacement_d2_053'] = {'inputs': ['ld_replacement_053'], 'func': ld_replacement_d2_053}


def ld_replacement_d2_054(ld_replacement_054):
    feature = _clean(ld_replacement_054)
    delta = feature.diff(8)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00054000).reindex(feature.index)
LD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ld_replacement_d2_054'] = {'inputs': ['ld_replacement_054'], 'func': ld_replacement_d2_054}


def ld_replacement_d2_055(ld_replacement_055):
    feature = _clean(ld_replacement_055)
    delta = feature.diff(13)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00055000).reindex(feature.index)
LD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ld_replacement_d2_055'] = {'inputs': ['ld_replacement_055'], 'func': ld_replacement_d2_055}


def ld_replacement_d2_056(ld_replacement_056):
    feature = _clean(ld_replacement_056)
    delta = feature.diff(21)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00056000).reindex(feature.index)
LD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ld_replacement_d2_056'] = {'inputs': ['ld_replacement_056'], 'func': ld_replacement_d2_056}


def ld_replacement_d2_057(ld_replacement_057):
    feature = _clean(ld_replacement_057)
    delta = feature.diff(34)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00057000).reindex(feature.index)
LD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ld_replacement_d2_057'] = {'inputs': ['ld_replacement_057'], 'func': ld_replacement_d2_057}


def ld_replacement_d2_058(ld_replacement_058):
    feature = _clean(ld_replacement_058)
    delta = feature.diff(55)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00058000).reindex(feature.index)
LD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ld_replacement_d2_058'] = {'inputs': ['ld_replacement_058'], 'func': ld_replacement_d2_058}


def ld_replacement_d2_059(ld_replacement_059):
    feature = _clean(ld_replacement_059)
    delta = feature.diff(89)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00059000).reindex(feature.index)
LD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ld_replacement_d2_059'] = {'inputs': ['ld_replacement_059'], 'func': ld_replacement_d2_059}


def ld_replacement_d2_060(ld_replacement_060):
    feature = _clean(ld_replacement_060)
    delta = feature.diff(1)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00060000).reindex(feature.index)
LD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ld_replacement_d2_060'] = {'inputs': ['ld_replacement_060'], 'func': ld_replacement_d2_060}


def ld_replacement_d2_061(ld_replacement_061):
    feature = _clean(ld_replacement_061)
    delta = feature.diff(2)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00061000).reindex(feature.index)
LD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ld_replacement_d2_061'] = {'inputs': ['ld_replacement_061'], 'func': ld_replacement_d2_061}


def ld_replacement_d2_062(ld_replacement_062):
    feature = _clean(ld_replacement_062)
    delta = feature.diff(3)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00062000).reindex(feature.index)
LD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ld_replacement_d2_062'] = {'inputs': ['ld_replacement_062'], 'func': ld_replacement_d2_062}


def ld_replacement_d2_063(ld_replacement_063):
    feature = _clean(ld_replacement_063)
    delta = feature.diff(5)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00063000).reindex(feature.index)
LD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ld_replacement_d2_063'] = {'inputs': ['ld_replacement_063'], 'func': ld_replacement_d2_063}


def ld_replacement_d2_064(ld_replacement_064):
    feature = _clean(ld_replacement_064)
    delta = feature.diff(8)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00064000).reindex(feature.index)
LD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ld_replacement_d2_064'] = {'inputs': ['ld_replacement_064'], 'func': ld_replacement_d2_064}


def ld_replacement_d2_065(ld_replacement_065):
    feature = _clean(ld_replacement_065)
    delta = feature.diff(13)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00065000).reindex(feature.index)
LD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ld_replacement_d2_065'] = {'inputs': ['ld_replacement_065'], 'func': ld_replacement_d2_065}


def ld_replacement_d2_066(ld_replacement_066):
    feature = _clean(ld_replacement_066)
    delta = feature.diff(21)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00066000).reindex(feature.index)
LD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ld_replacement_d2_066'] = {'inputs': ['ld_replacement_066'], 'func': ld_replacement_d2_066}


def ld_replacement_d2_067(ld_replacement_067):
    feature = _clean(ld_replacement_067)
    delta = feature.diff(34)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00067000).reindex(feature.index)
LD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ld_replacement_d2_067'] = {'inputs': ['ld_replacement_067'], 'func': ld_replacement_d2_067}


def ld_replacement_d2_068(ld_replacement_068):
    feature = _clean(ld_replacement_068)
    delta = feature.diff(55)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00068000).reindex(feature.index)
LD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ld_replacement_d2_068'] = {'inputs': ['ld_replacement_068'], 'func': ld_replacement_d2_068}


def ld_replacement_d2_069(ld_replacement_069):
    feature = _clean(ld_replacement_069)
    delta = feature.diff(89)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00069000).reindex(feature.index)
LD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ld_replacement_d2_069'] = {'inputs': ['ld_replacement_069'], 'func': ld_replacement_d2_069}


def ld_replacement_d2_070(ld_replacement_070):
    feature = _clean(ld_replacement_070)
    delta = feature.diff(1)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00070000).reindex(feature.index)
LD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ld_replacement_d2_070'] = {'inputs': ['ld_replacement_070'], 'func': ld_replacement_d2_070}


def ld_replacement_d2_071(ld_replacement_071):
    feature = _clean(ld_replacement_071)
    delta = feature.diff(2)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00071000).reindex(feature.index)
LD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ld_replacement_d2_071'] = {'inputs': ['ld_replacement_071'], 'func': ld_replacement_d2_071}


def ld_replacement_d2_072(ld_replacement_072):
    feature = _clean(ld_replacement_072)
    delta = feature.diff(3)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00072000).reindex(feature.index)
LD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ld_replacement_d2_072'] = {'inputs': ['ld_replacement_072'], 'func': ld_replacement_d2_072}


def ld_replacement_d2_073(ld_replacement_073):
    feature = _clean(ld_replacement_073)
    delta = feature.diff(5)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00073000).reindex(feature.index)
LD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ld_replacement_d2_073'] = {'inputs': ['ld_replacement_073'], 'func': ld_replacement_d2_073}


def ld_replacement_d2_074(ld_replacement_074):
    feature = _clean(ld_replacement_074)
    delta = feature.diff(8)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00074000).reindex(feature.index)
LD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ld_replacement_d2_074'] = {'inputs': ['ld_replacement_074'], 'func': ld_replacement_d2_074}


def ld_replacement_d2_075(ld_replacement_075):
    feature = _clean(ld_replacement_075)
    delta = feature.diff(13)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00075000).reindex(feature.index)
LD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ld_replacement_d2_075'] = {'inputs': ['ld_replacement_075'], 'func': ld_replacement_d2_075}


def ld_replacement_d2_076(ld_replacement_076):
    feature = _clean(ld_replacement_076)
    delta = feature.diff(21)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00076000).reindex(feature.index)
LD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ld_replacement_d2_076'] = {'inputs': ['ld_replacement_076'], 'func': ld_replacement_d2_076}


def ld_replacement_d2_077(ld_replacement_077):
    feature = _clean(ld_replacement_077)
    delta = feature.diff(34)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00077000).reindex(feature.index)
LD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ld_replacement_d2_077'] = {'inputs': ['ld_replacement_077'], 'func': ld_replacement_d2_077}


def ld_replacement_d2_078(ld_replacement_078):
    feature = _clean(ld_replacement_078)
    delta = feature.diff(55)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00078000).reindex(feature.index)
LD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ld_replacement_d2_078'] = {'inputs': ['ld_replacement_078'], 'func': ld_replacement_d2_078}


def ld_replacement_d2_079(ld_replacement_079):
    feature = _clean(ld_replacement_079)
    delta = feature.diff(89)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00079000).reindex(feature.index)
LD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ld_replacement_d2_079'] = {'inputs': ['ld_replacement_079'], 'func': ld_replacement_d2_079}


def ld_replacement_d2_080(ld_replacement_080):
    feature = _clean(ld_replacement_080)
    delta = feature.diff(1)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00080000).reindex(feature.index)
LD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ld_replacement_d2_080'] = {'inputs': ['ld_replacement_080'], 'func': ld_replacement_d2_080}


def ld_replacement_d2_081(ld_replacement_081):
    feature = _clean(ld_replacement_081)
    delta = feature.diff(2)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00081000).reindex(feature.index)
LD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ld_replacement_d2_081'] = {'inputs': ['ld_replacement_081'], 'func': ld_replacement_d2_081}


def ld_replacement_d2_082(ld_replacement_082):
    feature = _clean(ld_replacement_082)
    delta = feature.diff(3)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00082000).reindex(feature.index)
LD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ld_replacement_d2_082'] = {'inputs': ['ld_replacement_082'], 'func': ld_replacement_d2_082}


def ld_replacement_d2_083(ld_replacement_083):
    feature = _clean(ld_replacement_083)
    delta = feature.diff(5)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00083000).reindex(feature.index)
LD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ld_replacement_d2_083'] = {'inputs': ['ld_replacement_083'], 'func': ld_replacement_d2_083}


def ld_replacement_d2_084(ld_replacement_084):
    feature = _clean(ld_replacement_084)
    delta = feature.diff(8)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00084000).reindex(feature.index)
LD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ld_replacement_d2_084'] = {'inputs': ['ld_replacement_084'], 'func': ld_replacement_d2_084}


def ld_replacement_d2_085(ld_replacement_085):
    feature = _clean(ld_replacement_085)
    delta = feature.diff(13)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00085000).reindex(feature.index)
LD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ld_replacement_d2_085'] = {'inputs': ['ld_replacement_085'], 'func': ld_replacement_d2_085}


def ld_replacement_d2_086(ld_replacement_086):
    feature = _clean(ld_replacement_086)
    delta = feature.diff(21)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00086000).reindex(feature.index)
LD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ld_replacement_d2_086'] = {'inputs': ['ld_replacement_086'], 'func': ld_replacement_d2_086}


def ld_replacement_d2_087(ld_replacement_087):
    feature = _clean(ld_replacement_087)
    delta = feature.diff(34)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00087000).reindex(feature.index)
LD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ld_replacement_d2_087'] = {'inputs': ['ld_replacement_087'], 'func': ld_replacement_d2_087}


def ld_replacement_d2_088(ld_replacement_088):
    feature = _clean(ld_replacement_088)
    delta = feature.diff(55)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00088000).reindex(feature.index)
LD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ld_replacement_d2_088'] = {'inputs': ['ld_replacement_088'], 'func': ld_replacement_d2_088}


def ld_replacement_d2_089(ld_replacement_089):
    feature = _clean(ld_replacement_089)
    delta = feature.diff(89)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00089000).reindex(feature.index)
LD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ld_replacement_d2_089'] = {'inputs': ['ld_replacement_089'], 'func': ld_replacement_d2_089}


def ld_replacement_d2_090(ld_replacement_090):
    feature = _clean(ld_replacement_090)
    delta = feature.diff(1)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00090000).reindex(feature.index)
LD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ld_replacement_d2_090'] = {'inputs': ['ld_replacement_090'], 'func': ld_replacement_d2_090}


def ld_replacement_d2_091(ld_replacement_091):
    feature = _clean(ld_replacement_091)
    delta = feature.diff(2)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00091000).reindex(feature.index)
LD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ld_replacement_d2_091'] = {'inputs': ['ld_replacement_091'], 'func': ld_replacement_d2_091}


def ld_replacement_d2_092(ld_replacement_092):
    feature = _clean(ld_replacement_092)
    delta = feature.diff(3)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00092000).reindex(feature.index)
LD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ld_replacement_d2_092'] = {'inputs': ['ld_replacement_092'], 'func': ld_replacement_d2_092}


def ld_replacement_d2_093(ld_replacement_093):
    feature = _clean(ld_replacement_093)
    delta = feature.diff(5)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00093000).reindex(feature.index)
LD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ld_replacement_d2_093'] = {'inputs': ['ld_replacement_093'], 'func': ld_replacement_d2_093}


def ld_replacement_d2_094(ld_replacement_094):
    feature = _clean(ld_replacement_094)
    delta = feature.diff(8)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00094000).reindex(feature.index)
LD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ld_replacement_d2_094'] = {'inputs': ['ld_replacement_094'], 'func': ld_replacement_d2_094}


def ld_replacement_d2_095(ld_replacement_095):
    feature = _clean(ld_replacement_095)
    delta = feature.diff(13)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00095000).reindex(feature.index)
LD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ld_replacement_d2_095'] = {'inputs': ['ld_replacement_095'], 'func': ld_replacement_d2_095}


def ld_replacement_d2_096(ld_replacement_096):
    feature = _clean(ld_replacement_096)
    delta = feature.diff(21)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00096000).reindex(feature.index)
LD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ld_replacement_d2_096'] = {'inputs': ['ld_replacement_096'], 'func': ld_replacement_d2_096}


def ld_replacement_d2_097(ld_replacement_097):
    feature = _clean(ld_replacement_097)
    delta = feature.diff(34)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00097000).reindex(feature.index)
LD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ld_replacement_d2_097'] = {'inputs': ['ld_replacement_097'], 'func': ld_replacement_d2_097}


def ld_replacement_d2_098(ld_replacement_098):
    feature = _clean(ld_replacement_098)
    delta = feature.diff(55)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00098000).reindex(feature.index)
LD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ld_replacement_d2_098'] = {'inputs': ['ld_replacement_098'], 'func': ld_replacement_d2_098}


def ld_replacement_d2_099(ld_replacement_099):
    feature = _clean(ld_replacement_099)
    delta = feature.diff(89)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00099000).reindex(feature.index)
LD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ld_replacement_d2_099'] = {'inputs': ['ld_replacement_099'], 'func': ld_replacement_d2_099}


def ld_replacement_d2_100(ld_replacement_100):
    feature = _clean(ld_replacement_100)
    delta = feature.diff(1)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00100000).reindex(feature.index)
LD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ld_replacement_d2_100'] = {'inputs': ['ld_replacement_100'], 'func': ld_replacement_d2_100}


def ld_replacement_d2_101(ld_replacement_101):
    feature = _clean(ld_replacement_101)
    delta = feature.diff(2)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00101000).reindex(feature.index)
LD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ld_replacement_d2_101'] = {'inputs': ['ld_replacement_101'], 'func': ld_replacement_d2_101}


def ld_replacement_d2_102(ld_replacement_102):
    feature = _clean(ld_replacement_102)
    delta = feature.diff(3)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00102000).reindex(feature.index)
LD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ld_replacement_d2_102'] = {'inputs': ['ld_replacement_102'], 'func': ld_replacement_d2_102}


def ld_replacement_d2_103(ld_replacement_103):
    feature = _clean(ld_replacement_103)
    delta = feature.diff(5)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00103000).reindex(feature.index)
LD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ld_replacement_d2_103'] = {'inputs': ['ld_replacement_103'], 'func': ld_replacement_d2_103}


def ld_replacement_d2_104(ld_replacement_104):
    feature = _clean(ld_replacement_104)
    delta = feature.diff(8)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00104000).reindex(feature.index)
LD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ld_replacement_d2_104'] = {'inputs': ['ld_replacement_104'], 'func': ld_replacement_d2_104}


def ld_replacement_d2_105(ld_replacement_105):
    feature = _clean(ld_replacement_105)
    delta = feature.diff(13)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00105000).reindex(feature.index)
LD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ld_replacement_d2_105'] = {'inputs': ['ld_replacement_105'], 'func': ld_replacement_d2_105}


def ld_replacement_d2_106(ld_replacement_106):
    feature = _clean(ld_replacement_106)
    delta = feature.diff(21)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00106000).reindex(feature.index)
LD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ld_replacement_d2_106'] = {'inputs': ['ld_replacement_106'], 'func': ld_replacement_d2_106}


def ld_replacement_d2_107(ld_replacement_107):
    feature = _clean(ld_replacement_107)
    delta = feature.diff(34)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00107000).reindex(feature.index)
LD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ld_replacement_d2_107'] = {'inputs': ['ld_replacement_107'], 'func': ld_replacement_d2_107}


def ld_replacement_d2_108(ld_replacement_108):
    feature = _clean(ld_replacement_108)
    delta = feature.diff(55)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00108000).reindex(feature.index)
LD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ld_replacement_d2_108'] = {'inputs': ['ld_replacement_108'], 'func': ld_replacement_d2_108}


def ld_replacement_d2_109(ld_replacement_109):
    feature = _clean(ld_replacement_109)
    delta = feature.diff(89)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00109000).reindex(feature.index)
LD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ld_replacement_d2_109'] = {'inputs': ['ld_replacement_109'], 'func': ld_replacement_d2_109}


def ld_replacement_d2_110(ld_replacement_110):
    feature = _clean(ld_replacement_110)
    delta = feature.diff(1)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00110000).reindex(feature.index)
LD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ld_replacement_d2_110'] = {'inputs': ['ld_replacement_110'], 'func': ld_replacement_d2_110}


def ld_replacement_d2_111(ld_replacement_111):
    feature = _clean(ld_replacement_111)
    delta = feature.diff(2)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00111000).reindex(feature.index)
LD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ld_replacement_d2_111'] = {'inputs': ['ld_replacement_111'], 'func': ld_replacement_d2_111}


def ld_replacement_d2_112(ld_replacement_112):
    feature = _clean(ld_replacement_112)
    delta = feature.diff(3)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00112000).reindex(feature.index)
LD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ld_replacement_d2_112'] = {'inputs': ['ld_replacement_112'], 'func': ld_replacement_d2_112}


def ld_replacement_d2_113(ld_replacement_113):
    feature = _clean(ld_replacement_113)
    delta = feature.diff(5)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00113000).reindex(feature.index)
LD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ld_replacement_d2_113'] = {'inputs': ['ld_replacement_113'], 'func': ld_replacement_d2_113}


def ld_replacement_d2_114(ld_replacement_114):
    feature = _clean(ld_replacement_114)
    delta = feature.diff(8)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00114000).reindex(feature.index)
LD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ld_replacement_d2_114'] = {'inputs': ['ld_replacement_114'], 'func': ld_replacement_d2_114}


def ld_replacement_d2_115(ld_replacement_115):
    feature = _clean(ld_replacement_115)
    delta = feature.diff(13)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00115000).reindex(feature.index)
LD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ld_replacement_d2_115'] = {'inputs': ['ld_replacement_115'], 'func': ld_replacement_d2_115}


def ld_replacement_d2_116(ld_replacement_116):
    feature = _clean(ld_replacement_116)
    delta = feature.diff(21)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00116000).reindex(feature.index)
LD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ld_replacement_d2_116'] = {'inputs': ['ld_replacement_116'], 'func': ld_replacement_d2_116}


def ld_replacement_d2_117(ld_replacement_117):
    feature = _clean(ld_replacement_117)
    delta = feature.diff(34)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00117000).reindex(feature.index)
LD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ld_replacement_d2_117'] = {'inputs': ['ld_replacement_117'], 'func': ld_replacement_d2_117}


def ld_replacement_d2_118(ld_replacement_118):
    feature = _clean(ld_replacement_118)
    delta = feature.diff(55)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00118000).reindex(feature.index)
LD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ld_replacement_d2_118'] = {'inputs': ['ld_replacement_118'], 'func': ld_replacement_d2_118}


def ld_replacement_d2_119(ld_replacement_119):
    feature = _clean(ld_replacement_119)
    delta = feature.diff(89)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00119000).reindex(feature.index)
LD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ld_replacement_d2_119'] = {'inputs': ['ld_replacement_119'], 'func': ld_replacement_d2_119}


def ld_replacement_d2_120(ld_replacement_120):
    feature = _clean(ld_replacement_120)
    delta = feature.diff(1)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00120000).reindex(feature.index)
LD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ld_replacement_d2_120'] = {'inputs': ['ld_replacement_120'], 'func': ld_replacement_d2_120}


def ld_replacement_d2_121(ld_replacement_121):
    feature = _clean(ld_replacement_121)
    delta = feature.diff(2)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00121000).reindex(feature.index)
LD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ld_replacement_d2_121'] = {'inputs': ['ld_replacement_121'], 'func': ld_replacement_d2_121}


def ld_replacement_d2_122(ld_replacement_122):
    feature = _clean(ld_replacement_122)
    delta = feature.diff(3)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00122000).reindex(feature.index)
LD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ld_replacement_d2_122'] = {'inputs': ['ld_replacement_122'], 'func': ld_replacement_d2_122}


def ld_replacement_d2_123(ld_replacement_123):
    feature = _clean(ld_replacement_123)
    delta = feature.diff(5)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00123000).reindex(feature.index)
LD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ld_replacement_d2_123'] = {'inputs': ['ld_replacement_123'], 'func': ld_replacement_d2_123}


def ld_replacement_d2_124(ld_replacement_124):
    feature = _clean(ld_replacement_124)
    delta = feature.diff(8)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00124000).reindex(feature.index)
LD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ld_replacement_d2_124'] = {'inputs': ['ld_replacement_124'], 'func': ld_replacement_d2_124}


def ld_replacement_d2_125(ld_replacement_125):
    feature = _clean(ld_replacement_125)
    delta = feature.diff(13)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00125000).reindex(feature.index)
LD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ld_replacement_d2_125'] = {'inputs': ['ld_replacement_125'], 'func': ld_replacement_d2_125}


def ld_replacement_d2_126(ld_replacement_126):
    feature = _clean(ld_replacement_126)
    delta = feature.diff(21)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00126000).reindex(feature.index)
LD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ld_replacement_d2_126'] = {'inputs': ['ld_replacement_126'], 'func': ld_replacement_d2_126}


def ld_replacement_d2_127(ld_replacement_127):
    feature = _clean(ld_replacement_127)
    delta = feature.diff(34)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00127000).reindex(feature.index)
LD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ld_replacement_d2_127'] = {'inputs': ['ld_replacement_127'], 'func': ld_replacement_d2_127}


def ld_replacement_d2_128(ld_replacement_128):
    feature = _clean(ld_replacement_128)
    delta = feature.diff(55)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00128000).reindex(feature.index)
LD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ld_replacement_d2_128'] = {'inputs': ['ld_replacement_128'], 'func': ld_replacement_d2_128}


def ld_replacement_d2_129(ld_replacement_129):
    feature = _clean(ld_replacement_129)
    delta = feature.diff(89)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00129000).reindex(feature.index)
LD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ld_replacement_d2_129'] = {'inputs': ['ld_replacement_129'], 'func': ld_replacement_d2_129}


def ld_replacement_d2_130(ld_replacement_130):
    feature = _clean(ld_replacement_130)
    delta = feature.diff(1)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00130000).reindex(feature.index)
LD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ld_replacement_d2_130'] = {'inputs': ['ld_replacement_130'], 'func': ld_replacement_d2_130}


def ld_replacement_d2_131(ld_replacement_131):
    feature = _clean(ld_replacement_131)
    delta = feature.diff(2)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00131000).reindex(feature.index)
LD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ld_replacement_d2_131'] = {'inputs': ['ld_replacement_131'], 'func': ld_replacement_d2_131}


def ld_replacement_d2_132(ld_replacement_132):
    feature = _clean(ld_replacement_132)
    delta = feature.diff(3)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00132000).reindex(feature.index)
LD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ld_replacement_d2_132'] = {'inputs': ['ld_replacement_132'], 'func': ld_replacement_d2_132}


def ld_replacement_d2_133(ld_replacement_133):
    feature = _clean(ld_replacement_133)
    delta = feature.diff(5)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00133000).reindex(feature.index)
LD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ld_replacement_d2_133'] = {'inputs': ['ld_replacement_133'], 'func': ld_replacement_d2_133}


def ld_replacement_d2_134(ld_replacement_134):
    feature = _clean(ld_replacement_134)
    delta = feature.diff(8)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00134000).reindex(feature.index)
LD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ld_replacement_d2_134'] = {'inputs': ['ld_replacement_134'], 'func': ld_replacement_d2_134}


def ld_replacement_d2_135(ld_replacement_135):
    feature = _clean(ld_replacement_135)
    delta = feature.diff(13)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00135000).reindex(feature.index)
LD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ld_replacement_d2_135'] = {'inputs': ['ld_replacement_135'], 'func': ld_replacement_d2_135}


def ld_replacement_d2_136(ld_replacement_136):
    feature = _clean(ld_replacement_136)
    delta = feature.diff(21)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00136000).reindex(feature.index)
LD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ld_replacement_d2_136'] = {'inputs': ['ld_replacement_136'], 'func': ld_replacement_d2_136}


def ld_replacement_d2_137(ld_replacement_137):
    feature = _clean(ld_replacement_137)
    delta = feature.diff(34)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00137000).reindex(feature.index)
LD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ld_replacement_d2_137'] = {'inputs': ['ld_replacement_137'], 'func': ld_replacement_d2_137}


def ld_replacement_d2_138(ld_replacement_138):
    feature = _clean(ld_replacement_138)
    delta = feature.diff(55)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00138000).reindex(feature.index)
LD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ld_replacement_d2_138'] = {'inputs': ['ld_replacement_138'], 'func': ld_replacement_d2_138}


def ld_replacement_d2_139(ld_replacement_139):
    feature = _clean(ld_replacement_139)
    delta = feature.diff(89)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00139000).reindex(feature.index)
LD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ld_replacement_d2_139'] = {'inputs': ['ld_replacement_139'], 'func': ld_replacement_d2_139}


def ld_replacement_d2_140(ld_replacement_140):
    feature = _clean(ld_replacement_140)
    delta = feature.diff(1)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00140000).reindex(feature.index)
LD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ld_replacement_d2_140'] = {'inputs': ['ld_replacement_140'], 'func': ld_replacement_d2_140}


def ld_replacement_d2_141(ld_replacement_141):
    feature = _clean(ld_replacement_141)
    delta = feature.diff(2)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00141000).reindex(feature.index)
LD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ld_replacement_d2_141'] = {'inputs': ['ld_replacement_141'], 'func': ld_replacement_d2_141}


def ld_replacement_d2_142(ld_replacement_142):
    feature = _clean(ld_replacement_142)
    delta = feature.diff(3)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00142000).reindex(feature.index)
LD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ld_replacement_d2_142'] = {'inputs': ['ld_replacement_142'], 'func': ld_replacement_d2_142}


def ld_replacement_d2_143(ld_replacement_143):
    feature = _clean(ld_replacement_143)
    delta = feature.diff(5)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00143000).reindex(feature.index)
LD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ld_replacement_d2_143'] = {'inputs': ['ld_replacement_143'], 'func': ld_replacement_d2_143}


def ld_replacement_d2_144(ld_replacement_144):
    feature = _clean(ld_replacement_144)
    delta = feature.diff(8)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00144000).reindex(feature.index)
LD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ld_replacement_d2_144'] = {'inputs': ['ld_replacement_144'], 'func': ld_replacement_d2_144}


def ld_replacement_d2_145(ld_replacement_145):
    feature = _clean(ld_replacement_145)
    delta = feature.diff(13)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00145000).reindex(feature.index)
LD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ld_replacement_d2_145'] = {'inputs': ['ld_replacement_145'], 'func': ld_replacement_d2_145}


def ld_replacement_d2_146(ld_replacement_146):
    feature = _clean(ld_replacement_146)
    delta = feature.diff(21)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00146000).reindex(feature.index)
LD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ld_replacement_d2_146'] = {'inputs': ['ld_replacement_146'], 'func': ld_replacement_d2_146}


def ld_replacement_d2_147(ld_replacement_147):
    feature = _clean(ld_replacement_147)
    delta = feature.diff(34)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00147000).reindex(feature.index)
LD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ld_replacement_d2_147'] = {'inputs': ['ld_replacement_147'], 'func': ld_replacement_d2_147}


def ld_replacement_d2_148(ld_replacement_148):
    feature = _clean(ld_replacement_148)
    delta = feature.diff(55)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00148000).reindex(feature.index)
LD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ld_replacement_d2_148'] = {'inputs': ['ld_replacement_148'], 'func': ld_replacement_d2_148}


def ld_replacement_d2_149(ld_replacement_149):
    feature = _clean(ld_replacement_149)
    delta = feature.diff(89)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00149000).reindex(feature.index)
LD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ld_replacement_d2_149'] = {'inputs': ['ld_replacement_149'], 'func': ld_replacement_d2_149}


def ld_replacement_d2_150(ld_replacement_150):
    feature = _clean(ld_replacement_150)
    delta = feature.diff(1)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00150000).reindex(feature.index)
LD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ld_replacement_d2_150'] = {'inputs': ['ld_replacement_150'], 'func': ld_replacement_d2_150}


def ld_replacement_d2_151(ld_replacement_151):
    feature = _clean(ld_replacement_151)
    delta = feature.diff(2)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00151000).reindex(feature.index)
LD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ld_replacement_d2_151'] = {'inputs': ['ld_replacement_151'], 'func': ld_replacement_d2_151}


def ld_replacement_d2_152(ld_replacement_152):
    feature = _clean(ld_replacement_152)
    delta = feature.diff(3)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00152000).reindex(feature.index)
LD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ld_replacement_d2_152'] = {'inputs': ['ld_replacement_152'], 'func': ld_replacement_d2_152}


def ld_replacement_d2_153(ld_replacement_153):
    feature = _clean(ld_replacement_153)
    delta = feature.diff(5)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00153000).reindex(feature.index)
LD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ld_replacement_d2_153'] = {'inputs': ['ld_replacement_153'], 'func': ld_replacement_d2_153}


def ld_replacement_d2_154(ld_replacement_154):
    feature = _clean(ld_replacement_154)
    delta = feature.diff(8)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00154000).reindex(feature.index)
LD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ld_replacement_d2_154'] = {'inputs': ['ld_replacement_154'], 'func': ld_replacement_d2_154}


def ld_replacement_d2_155(ld_replacement_155):
    feature = _clean(ld_replacement_155)
    delta = feature.diff(13)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00155000).reindex(feature.index)
LD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ld_replacement_d2_155'] = {'inputs': ['ld_replacement_155'], 'func': ld_replacement_d2_155}


def ld_replacement_d2_156(ld_replacement_156):
    feature = _clean(ld_replacement_156)
    delta = feature.diff(21)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00156000).reindex(feature.index)
LD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ld_replacement_d2_156'] = {'inputs': ['ld_replacement_156'], 'func': ld_replacement_d2_156}


def ld_replacement_d2_157(ld_replacement_157):
    feature = _clean(ld_replacement_157)
    delta = feature.diff(34)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00157000).reindex(feature.index)
LD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ld_replacement_d2_157'] = {'inputs': ['ld_replacement_157'], 'func': ld_replacement_d2_157}


def ld_replacement_d2_158(ld_replacement_158):
    feature = _clean(ld_replacement_158)
    delta = feature.diff(55)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00158000).reindex(feature.index)
LD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ld_replacement_d2_158'] = {'inputs': ['ld_replacement_158'], 'func': ld_replacement_d2_158}


def ld_replacement_d2_159(ld_replacement_159):
    feature = _clean(ld_replacement_159)
    delta = feature.diff(89)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00159000).reindex(feature.index)
LD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ld_replacement_d2_159'] = {'inputs': ['ld_replacement_159'], 'func': ld_replacement_d2_159}


def ld_replacement_d2_160(ld_replacement_160):
    feature = _clean(ld_replacement_160)
    delta = feature.diff(1)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00160000).reindex(feature.index)
LD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ld_replacement_d2_160'] = {'inputs': ['ld_replacement_160'], 'func': ld_replacement_d2_160}


def ld_replacement_d2_161(ld_replacement_161):
    feature = _clean(ld_replacement_161)
    delta = feature.diff(2)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00161000).reindex(feature.index)
LD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ld_replacement_d2_161'] = {'inputs': ['ld_replacement_161'], 'func': ld_replacement_d2_161}


def ld_replacement_d2_162(ld_replacement_162):
    feature = _clean(ld_replacement_162)
    delta = feature.diff(3)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00162000).reindex(feature.index)
LD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ld_replacement_d2_162'] = {'inputs': ['ld_replacement_162'], 'func': ld_replacement_d2_162}


def ld_replacement_d2_163(ld_replacement_163):
    feature = _clean(ld_replacement_163)
    delta = feature.diff(5)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00163000).reindex(feature.index)
LD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ld_replacement_d2_163'] = {'inputs': ['ld_replacement_163'], 'func': ld_replacement_d2_163}


def ld_replacement_d2_164(ld_replacement_164):
    feature = _clean(ld_replacement_164)
    delta = feature.diff(8)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00164000).reindex(feature.index)
LD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ld_replacement_d2_164'] = {'inputs': ['ld_replacement_164'], 'func': ld_replacement_d2_164}


def ld_replacement_d2_165(ld_replacement_165):
    feature = _clean(ld_replacement_165)
    delta = feature.diff(13)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00165000).reindex(feature.index)
LD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ld_replacement_d2_165'] = {'inputs': ['ld_replacement_165'], 'func': ld_replacement_d2_165}


def ld_replacement_d2_166(ld_replacement_166):
    feature = _clean(ld_replacement_166)
    delta = feature.diff(21)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00166000).reindex(feature.index)
LD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ld_replacement_d2_166'] = {'inputs': ['ld_replacement_166'], 'func': ld_replacement_d2_166}


# Base-universe derivative extensions for repaired first-base features.
LQD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY = {}


def _base_universe_d2(feature, idx):
    feature = _clean(feature) if '_clean' in globals() else _s(feature).replace([np.inf, -np.inf], np.nan)
    windows = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    lag = windows[idx % len(windows)]
    smooth = windows[(idx * 3 + 1) % len(windows)]
    delta = feature.diff(lag)
    local = feature - feature.rolling(max(3, smooth), min_periods=2).mean()
    out = delta + local.fillna(0.0) * (0.00037 * ((idx % 17) + 1))
    return out.replace([np.inf, -np.inf], np.nan).reindex(feature.index)


def lqd_base_universe_d2_001_lqd_003_fcf_burn_to_cash_63(lqd_003_fcf_burn_to_cash_63):
    return _base_universe_d2(lqd_003_fcf_burn_to_cash_63, 1)
LQD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lqd_base_universe_d2_001_lqd_003_fcf_burn_to_cash_63'] = {'inputs': ['lqd_003_fcf_burn_to_cash_63'], 'func': lqd_base_universe_d2_001_lqd_003_fcf_burn_to_cash_63}


def lqd_base_universe_d2_002_lqd_004_debt_to_equity_84(lqd_004_debt_to_equity_84):
    return _base_universe_d2(lqd_004_debt_to_equity_84, 2)
LQD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lqd_base_universe_d2_002_lqd_004_debt_to_equity_84'] = {'inputs': ['lqd_004_debt_to_equity_84'], 'func': lqd_base_universe_d2_002_lqd_004_debt_to_equity_84}


def lqd_base_universe_d2_003_lqd_005_debt_to_assets_126(lqd_005_debt_to_assets_126):
    return _base_universe_d2(lqd_005_debt_to_assets_126, 3)
LQD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lqd_base_universe_d2_003_lqd_005_debt_to_assets_126'] = {'inputs': ['lqd_005_debt_to_assets_126'], 'func': lqd_base_universe_d2_003_lqd_005_debt_to_assets_126}


def lqd_base_universe_d2_004_lqd_012_accrual_gap_1260(lqd_012_accrual_gap_1260):
    return _base_universe_d2(lqd_012_accrual_gap_1260, 4)
LQD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lqd_base_universe_d2_004_lqd_012_accrual_gap_1260'] = {'inputs': ['lqd_012_accrual_gap_1260'], 'func': lqd_base_universe_d2_004_lqd_012_accrual_gap_1260}


def lqd_base_universe_d2_005_lqd_016_debt_to_equity_21(lqd_016_debt_to_equity_21):
    return _base_universe_d2(lqd_016_debt_to_equity_21, 5)
LQD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lqd_base_universe_d2_005_lqd_016_debt_to_equity_21'] = {'inputs': ['lqd_016_debt_to_equity_21'], 'func': lqd_base_universe_d2_005_lqd_016_debt_to_equity_21}


def lqd_base_universe_d2_006_lqd_017_debt_to_assets_42(lqd_017_debt_to_assets_42):
    return _base_universe_d2(lqd_017_debt_to_assets_42, 6)
LQD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lqd_base_universe_d2_006_lqd_017_debt_to_assets_42'] = {'inputs': ['lqd_017_debt_to_assets_42'], 'func': lqd_base_universe_d2_006_lqd_017_debt_to_assets_42}


def lqd_base_universe_d2_007_lqd_024_accrual_gap_504(lqd_024_accrual_gap_504):
    return _base_universe_d2(lqd_024_accrual_gap_504, 7)
LQD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lqd_base_universe_d2_007_lqd_024_accrual_gap_504'] = {'inputs': ['lqd_024_accrual_gap_504'], 'func': lqd_base_universe_d2_007_lqd_024_accrual_gap_504}


def lqd_base_universe_d2_008_lqd_027_fcf_burn_to_cash_1260(lqd_027_fcf_burn_to_cash_1260):
    return _base_universe_d2(lqd_027_fcf_burn_to_cash_1260, 8)
LQD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lqd_base_universe_d2_008_lqd_027_fcf_burn_to_cash_1260'] = {'inputs': ['lqd_027_fcf_burn_to_cash_1260'], 'func': lqd_base_universe_d2_008_lqd_027_fcf_burn_to_cash_1260}


def lqd_base_universe_d2_009_lqd_028_debt_to_equity_1512(lqd_028_debt_to_equity_1512):
    return _base_universe_d2(lqd_028_debt_to_equity_1512, 9)
LQD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lqd_base_universe_d2_009_lqd_028_debt_to_equity_1512'] = {'inputs': ['lqd_028_debt_to_equity_1512'], 'func': lqd_base_universe_d2_009_lqd_028_debt_to_equity_1512}


def lqd_base_universe_d2_010_lqd_029_debt_to_assets_63(lqd_029_debt_to_assets_63):
    return _base_universe_d2(lqd_029_debt_to_assets_63, 10)
LQD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lqd_base_universe_d2_010_lqd_029_debt_to_assets_63'] = {'inputs': ['lqd_029_debt_to_assets_63'], 'func': lqd_base_universe_d2_010_lqd_029_debt_to_assets_63}


def lqd_base_universe_d2_011_lqd_031_interest_coverage_stress_21(lqd_031_interest_coverage_stress_21):
    return _base_universe_d2(lqd_031_interest_coverage_stress_21, 11)
LQD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lqd_base_universe_d2_011_lqd_031_interest_coverage_stress_21'] = {'inputs': ['lqd_031_interest_coverage_stress_21'], 'func': lqd_base_universe_d2_011_lqd_031_interest_coverage_stress_21}


def lqd_base_universe_d2_012_lqd_036_accrual_gap_189(lqd_036_accrual_gap_189):
    return _base_universe_d2(lqd_036_accrual_gap_189, 12)
LQD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lqd_base_universe_d2_012_lqd_036_accrual_gap_189'] = {'inputs': ['lqd_036_accrual_gap_189'], 'func': lqd_base_universe_d2_012_lqd_036_accrual_gap_189}


def lqd_base_universe_d2_013_lqd_039_fcf_burn_to_cash_504(lqd_039_fcf_burn_to_cash_504):
    return _base_universe_d2(lqd_039_fcf_burn_to_cash_504, 13)
LQD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lqd_base_universe_d2_013_lqd_039_fcf_burn_to_cash_504'] = {'inputs': ['lqd_039_fcf_burn_to_cash_504'], 'func': lqd_base_universe_d2_013_lqd_039_fcf_burn_to_cash_504}


def lqd_base_universe_d2_014_lqd_040_debt_to_equity_756(lqd_040_debt_to_equity_756):
    return _base_universe_d2(lqd_040_debt_to_equity_756, 14)
LQD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lqd_base_universe_d2_014_lqd_040_debt_to_equity_756'] = {'inputs': ['lqd_040_debt_to_equity_756'], 'func': lqd_base_universe_d2_014_lqd_040_debt_to_equity_756}


def lqd_base_universe_d2_015_lqd_041_debt_to_assets_1008(lqd_041_debt_to_assets_1008):
    return _base_universe_d2(lqd_041_debt_to_assets_1008, 15)
LQD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lqd_base_universe_d2_015_lqd_041_debt_to_assets_1008'] = {'inputs': ['lqd_041_debt_to_assets_1008'], 'func': lqd_base_universe_d2_015_lqd_041_debt_to_assets_1008}


def lqd_base_universe_d2_016_lqd_043_interest_coverage_stress_1512(lqd_043_interest_coverage_stress_1512):
    return _base_universe_d2(lqd_043_interest_coverage_stress_1512, 16)
LQD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lqd_base_universe_d2_016_lqd_043_interest_coverage_stress_1512'] = {'inputs': ['lqd_043_interest_coverage_stress_1512'], 'func': lqd_base_universe_d2_016_lqd_043_interest_coverage_stress_1512}


def lqd_base_universe_d2_017_lqd_048_accrual_gap_63(lqd_048_accrual_gap_63):
    return _base_universe_d2(lqd_048_accrual_gap_63, 17)
LQD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lqd_base_universe_d2_017_lqd_048_accrual_gap_63'] = {'inputs': ['lqd_048_accrual_gap_63'], 'func': lqd_base_universe_d2_017_lqd_048_accrual_gap_63}


def lqd_base_universe_d2_018_lqd_051_fcf_burn_to_cash_189(lqd_051_fcf_burn_to_cash_189):
    return _base_universe_d2(lqd_051_fcf_burn_to_cash_189, 18)
LQD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lqd_base_universe_d2_018_lqd_051_fcf_burn_to_cash_189'] = {'inputs': ['lqd_051_fcf_burn_to_cash_189'], 'func': lqd_base_universe_d2_018_lqd_051_fcf_burn_to_cash_189}


def lqd_base_universe_d2_019_lqd_052_debt_to_equity_252(lqd_052_debt_to_equity_252):
    return _base_universe_d2(lqd_052_debt_to_equity_252, 19)
LQD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lqd_base_universe_d2_019_lqd_052_debt_to_equity_252'] = {'inputs': ['lqd_052_debt_to_equity_252'], 'func': lqd_base_universe_d2_019_lqd_052_debt_to_equity_252}


def lqd_base_universe_d2_020_lqd_053_debt_to_assets_378(lqd_053_debt_to_assets_378):
    return _base_universe_d2(lqd_053_debt_to_assets_378, 20)
LQD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lqd_base_universe_d2_020_lqd_053_debt_to_assets_378'] = {'inputs': ['lqd_053_debt_to_assets_378'], 'func': lqd_base_universe_d2_020_lqd_053_debt_to_assets_378}


def lqd_base_universe_d2_021_lqd_055_interest_coverage_stress_756(lqd_055_interest_coverage_stress_756):
    return _base_universe_d2(lqd_055_interest_coverage_stress_756, 21)
LQD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lqd_base_universe_d2_021_lqd_055_interest_coverage_stress_756'] = {'inputs': ['lqd_055_interest_coverage_stress_756'], 'func': lqd_base_universe_d2_021_lqd_055_interest_coverage_stress_756}


def lqd_base_universe_d2_022_lqd_060_accrual_gap_252(lqd_060_accrual_gap_252):
    return _base_universe_d2(lqd_060_accrual_gap_252, 22)
LQD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lqd_base_universe_d2_022_lqd_060_accrual_gap_252'] = {'inputs': ['lqd_060_accrual_gap_252'], 'func': lqd_base_universe_d2_022_lqd_060_accrual_gap_252}


def lqd_base_universe_d2_023_lqd_basefill_001(lqd_basefill_001):
    return _base_universe_d2(lqd_basefill_001, 23)
LQD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lqd_base_universe_d2_023_lqd_basefill_001'] = {'inputs': ['lqd_basefill_001'], 'func': lqd_base_universe_d2_023_lqd_basefill_001}


def lqd_base_universe_d2_024_lqd_basefill_002(lqd_basefill_002):
    return _base_universe_d2(lqd_basefill_002, 24)
LQD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lqd_base_universe_d2_024_lqd_basefill_002'] = {'inputs': ['lqd_basefill_002'], 'func': lqd_base_universe_d2_024_lqd_basefill_002}


def lqd_base_universe_d2_025_lqd_basefill_006(lqd_basefill_006):
    return _base_universe_d2(lqd_basefill_006, 25)
LQD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lqd_base_universe_d2_025_lqd_basefill_006'] = {'inputs': ['lqd_basefill_006'], 'func': lqd_base_universe_d2_025_lqd_basefill_006}


def lqd_base_universe_d2_026_lqd_basefill_008(lqd_basefill_008):
    return _base_universe_d2(lqd_basefill_008, 26)
LQD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lqd_base_universe_d2_026_lqd_basefill_008'] = {'inputs': ['lqd_basefill_008'], 'func': lqd_base_universe_d2_026_lqd_basefill_008}


def lqd_base_universe_d2_027_lqd_basefill_009(lqd_basefill_009):
    return _base_universe_d2(lqd_basefill_009, 27)
LQD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lqd_base_universe_d2_027_lqd_basefill_009'] = {'inputs': ['lqd_basefill_009'], 'func': lqd_base_universe_d2_027_lqd_basefill_009}


def lqd_base_universe_d2_028_lqd_basefill_010(lqd_basefill_010):
    return _base_universe_d2(lqd_basefill_010, 28)
LQD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lqd_base_universe_d2_028_lqd_basefill_010'] = {'inputs': ['lqd_basefill_010'], 'func': lqd_base_universe_d2_028_lqd_basefill_010}


def lqd_base_universe_d2_029_lqd_basefill_011(lqd_basefill_011):
    return _base_universe_d2(lqd_basefill_011, 29)
LQD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lqd_base_universe_d2_029_lqd_basefill_011'] = {'inputs': ['lqd_basefill_011'], 'func': lqd_base_universe_d2_029_lqd_basefill_011}


def lqd_base_universe_d2_030_lqd_basefill_013(lqd_basefill_013):
    return _base_universe_d2(lqd_basefill_013, 30)
LQD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lqd_base_universe_d2_030_lqd_basefill_013'] = {'inputs': ['lqd_basefill_013'], 'func': lqd_base_universe_d2_030_lqd_basefill_013}


def lqd_base_universe_d2_031_lqd_basefill_014(lqd_basefill_014):
    return _base_universe_d2(lqd_basefill_014, 31)
LQD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lqd_base_universe_d2_031_lqd_basefill_014'] = {'inputs': ['lqd_basefill_014'], 'func': lqd_base_universe_d2_031_lqd_basefill_014}


def lqd_base_universe_d2_032_lqd_basefill_015(lqd_basefill_015):
    return _base_universe_d2(lqd_basefill_015, 32)
LQD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lqd_base_universe_d2_032_lqd_basefill_015'] = {'inputs': ['lqd_basefill_015'], 'func': lqd_base_universe_d2_032_lqd_basefill_015}


def lqd_base_universe_d2_033_lqd_basefill_018(lqd_basefill_018):
    return _base_universe_d2(lqd_basefill_018, 33)
LQD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lqd_base_universe_d2_033_lqd_basefill_018'] = {'inputs': ['lqd_basefill_018'], 'func': lqd_base_universe_d2_033_lqd_basefill_018}


def lqd_base_universe_d2_034_lqd_basefill_020(lqd_basefill_020):
    return _base_universe_d2(lqd_basefill_020, 34)
LQD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lqd_base_universe_d2_034_lqd_basefill_020'] = {'inputs': ['lqd_basefill_020'], 'func': lqd_base_universe_d2_034_lqd_basefill_020}


def lqd_base_universe_d2_035_lqd_basefill_021(lqd_basefill_021):
    return _base_universe_d2(lqd_basefill_021, 35)
LQD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lqd_base_universe_d2_035_lqd_basefill_021'] = {'inputs': ['lqd_basefill_021'], 'func': lqd_base_universe_d2_035_lqd_basefill_021}


def lqd_base_universe_d2_036_lqd_basefill_022(lqd_basefill_022):
    return _base_universe_d2(lqd_basefill_022, 36)
LQD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lqd_base_universe_d2_036_lqd_basefill_022'] = {'inputs': ['lqd_basefill_022'], 'func': lqd_base_universe_d2_036_lqd_basefill_022}


def lqd_base_universe_d2_037_lqd_basefill_023(lqd_basefill_023):
    return _base_universe_d2(lqd_basefill_023, 37)
LQD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lqd_base_universe_d2_037_lqd_basefill_023'] = {'inputs': ['lqd_basefill_023'], 'func': lqd_base_universe_d2_037_lqd_basefill_023}


def lqd_base_universe_d2_038_lqd_basefill_025(lqd_basefill_025):
    return _base_universe_d2(lqd_basefill_025, 38)
LQD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lqd_base_universe_d2_038_lqd_basefill_025'] = {'inputs': ['lqd_basefill_025'], 'func': lqd_base_universe_d2_038_lqd_basefill_025}


def lqd_base_universe_d2_039_lqd_basefill_026(lqd_basefill_026):
    return _base_universe_d2(lqd_basefill_026, 39)
LQD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lqd_base_universe_d2_039_lqd_basefill_026'] = {'inputs': ['lqd_basefill_026'], 'func': lqd_base_universe_d2_039_lqd_basefill_026}


def lqd_base_universe_d2_040_lqd_basefill_030(lqd_basefill_030):
    return _base_universe_d2(lqd_basefill_030, 40)
LQD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lqd_base_universe_d2_040_lqd_basefill_030'] = {'inputs': ['lqd_basefill_030'], 'func': lqd_base_universe_d2_040_lqd_basefill_030}


def lqd_base_universe_d2_041_lqd_basefill_032(lqd_basefill_032):
    return _base_universe_d2(lqd_basefill_032, 41)
LQD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lqd_base_universe_d2_041_lqd_basefill_032'] = {'inputs': ['lqd_basefill_032'], 'func': lqd_base_universe_d2_041_lqd_basefill_032}


def lqd_base_universe_d2_042_lqd_basefill_033(lqd_basefill_033):
    return _base_universe_d2(lqd_basefill_033, 42)
LQD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lqd_base_universe_d2_042_lqd_basefill_033'] = {'inputs': ['lqd_basefill_033'], 'func': lqd_base_universe_d2_042_lqd_basefill_033}


def lqd_base_universe_d2_043_lqd_basefill_034(lqd_basefill_034):
    return _base_universe_d2(lqd_basefill_034, 43)
LQD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lqd_base_universe_d2_043_lqd_basefill_034'] = {'inputs': ['lqd_basefill_034'], 'func': lqd_base_universe_d2_043_lqd_basefill_034}


def lqd_base_universe_d2_044_lqd_basefill_035(lqd_basefill_035):
    return _base_universe_d2(lqd_basefill_035, 44)
LQD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lqd_base_universe_d2_044_lqd_basefill_035'] = {'inputs': ['lqd_basefill_035'], 'func': lqd_base_universe_d2_044_lqd_basefill_035}


def lqd_base_universe_d2_045_lqd_basefill_037(lqd_basefill_037):
    return _base_universe_d2(lqd_basefill_037, 45)
LQD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lqd_base_universe_d2_045_lqd_basefill_037'] = {'inputs': ['lqd_basefill_037'], 'func': lqd_base_universe_d2_045_lqd_basefill_037}


def lqd_base_universe_d2_046_lqd_basefill_038(lqd_basefill_038):
    return _base_universe_d2(lqd_basefill_038, 46)
LQD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lqd_base_universe_d2_046_lqd_basefill_038'] = {'inputs': ['lqd_basefill_038'], 'func': lqd_base_universe_d2_046_lqd_basefill_038}


def lqd_base_universe_d2_047_lqd_basefill_042(lqd_basefill_042):
    return _base_universe_d2(lqd_basefill_042, 47)
LQD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lqd_base_universe_d2_047_lqd_basefill_042'] = {'inputs': ['lqd_basefill_042'], 'func': lqd_base_universe_d2_047_lqd_basefill_042}


def lqd_base_universe_d2_048_lqd_basefill_044(lqd_basefill_044):
    return _base_universe_d2(lqd_basefill_044, 48)
LQD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lqd_base_universe_d2_048_lqd_basefill_044'] = {'inputs': ['lqd_basefill_044'], 'func': lqd_base_universe_d2_048_lqd_basefill_044}


def lqd_base_universe_d2_049_lqd_basefill_045(lqd_basefill_045):
    return _base_universe_d2(lqd_basefill_045, 49)
LQD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lqd_base_universe_d2_049_lqd_basefill_045'] = {'inputs': ['lqd_basefill_045'], 'func': lqd_base_universe_d2_049_lqd_basefill_045}


def lqd_base_universe_d2_050_lqd_basefill_046(lqd_basefill_046):
    return _base_universe_d2(lqd_basefill_046, 50)
LQD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lqd_base_universe_d2_050_lqd_basefill_046'] = {'inputs': ['lqd_basefill_046'], 'func': lqd_base_universe_d2_050_lqd_basefill_046}


def lqd_base_universe_d2_051_lqd_basefill_047(lqd_basefill_047):
    return _base_universe_d2(lqd_basefill_047, 51)
LQD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lqd_base_universe_d2_051_lqd_basefill_047'] = {'inputs': ['lqd_basefill_047'], 'func': lqd_base_universe_d2_051_lqd_basefill_047}


def lqd_base_universe_d2_052_lqd_basefill_049(lqd_basefill_049):
    return _base_universe_d2(lqd_basefill_049, 52)
LQD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lqd_base_universe_d2_052_lqd_basefill_049'] = {'inputs': ['lqd_basefill_049'], 'func': lqd_base_universe_d2_052_lqd_basefill_049}


def lqd_base_universe_d2_053_lqd_basefill_050(lqd_basefill_050):
    return _base_universe_d2(lqd_basefill_050, 53)
LQD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lqd_base_universe_d2_053_lqd_basefill_050'] = {'inputs': ['lqd_basefill_050'], 'func': lqd_base_universe_d2_053_lqd_basefill_050}


def lqd_base_universe_d2_054_lqd_basefill_054(lqd_basefill_054):
    return _base_universe_d2(lqd_basefill_054, 54)
LQD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lqd_base_universe_d2_054_lqd_basefill_054'] = {'inputs': ['lqd_basefill_054'], 'func': lqd_base_universe_d2_054_lqd_basefill_054}


def lqd_base_universe_d2_055_lqd_basefill_056(lqd_basefill_056):
    return _base_universe_d2(lqd_basefill_056, 55)
LQD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lqd_base_universe_d2_055_lqd_basefill_056'] = {'inputs': ['lqd_basefill_056'], 'func': lqd_base_universe_d2_055_lqd_basefill_056}


def lqd_base_universe_d2_056_lqd_basefill_057(lqd_basefill_057):
    return _base_universe_d2(lqd_basefill_057, 56)
LQD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lqd_base_universe_d2_056_lqd_basefill_057'] = {'inputs': ['lqd_basefill_057'], 'func': lqd_base_universe_d2_056_lqd_basefill_057}


def lqd_base_universe_d2_057_lqd_basefill_058(lqd_basefill_058):
    return _base_universe_d2(lqd_basefill_058, 57)
LQD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lqd_base_universe_d2_057_lqd_basefill_058'] = {'inputs': ['lqd_basefill_058'], 'func': lqd_base_universe_d2_057_lqd_basefill_058}


def lqd_base_universe_d2_058_lqd_basefill_059(lqd_basefill_059):
    return _base_universe_d2(lqd_basefill_059, 58)
LQD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lqd_base_universe_d2_058_lqd_basefill_059'] = {'inputs': ['lqd_basefill_059'], 'func': lqd_base_universe_d2_058_lqd_basefill_059}


def lqd_base_universe_d2_059_lqd_basefill_061(lqd_basefill_061):
    return _base_universe_d2(lqd_basefill_061, 59)
LQD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lqd_base_universe_d2_059_lqd_basefill_061'] = {'inputs': ['lqd_basefill_061'], 'func': lqd_base_universe_d2_059_lqd_basefill_061}


def lqd_base_universe_d2_060_lqd_basefill_062(lqd_basefill_062):
    return _base_universe_d2(lqd_basefill_062, 60)
LQD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lqd_base_universe_d2_060_lqd_basefill_062'] = {'inputs': ['lqd_basefill_062'], 'func': lqd_base_universe_d2_060_lqd_basefill_062}


def lqd_base_universe_d2_061_lqd_basefill_063(lqd_basefill_063):
    return _base_universe_d2(lqd_basefill_063, 61)
LQD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lqd_base_universe_d2_061_lqd_basefill_063'] = {'inputs': ['lqd_basefill_063'], 'func': lqd_base_universe_d2_061_lqd_basefill_063}


def lqd_base_universe_d2_062_lqd_basefill_064(lqd_basefill_064):
    return _base_universe_d2(lqd_basefill_064, 62)
LQD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lqd_base_universe_d2_062_lqd_basefill_064'] = {'inputs': ['lqd_basefill_064'], 'func': lqd_base_universe_d2_062_lqd_basefill_064}


def lqd_base_universe_d2_063_lqd_basefill_065(lqd_basefill_065):
    return _base_universe_d2(lqd_basefill_065, 63)
LQD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lqd_base_universe_d2_063_lqd_basefill_065'] = {'inputs': ['lqd_basefill_065'], 'func': lqd_base_universe_d2_063_lqd_basefill_065}


def lqd_base_universe_d2_064_lqd_basefill_066(lqd_basefill_066):
    return _base_universe_d2(lqd_basefill_066, 64)
LQD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lqd_base_universe_d2_064_lqd_basefill_066'] = {'inputs': ['lqd_basefill_066'], 'func': lqd_base_universe_d2_064_lqd_basefill_066}


def lqd_base_universe_d2_065_lqd_basefill_067(lqd_basefill_067):
    return _base_universe_d2(lqd_basefill_067, 65)
LQD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lqd_base_universe_d2_065_lqd_basefill_067'] = {'inputs': ['lqd_basefill_067'], 'func': lqd_base_universe_d2_065_lqd_basefill_067}


def lqd_base_universe_d2_066_lqd_basefill_068(lqd_basefill_068):
    return _base_universe_d2(lqd_basefill_068, 66)
LQD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lqd_base_universe_d2_066_lqd_basefill_068'] = {'inputs': ['lqd_basefill_068'], 'func': lqd_base_universe_d2_066_lqd_basefill_068}


def lqd_base_universe_d2_067_lqd_basefill_069(lqd_basefill_069):
    return _base_universe_d2(lqd_basefill_069, 67)
LQD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lqd_base_universe_d2_067_lqd_basefill_069'] = {'inputs': ['lqd_basefill_069'], 'func': lqd_base_universe_d2_067_lqd_basefill_069}


def lqd_base_universe_d2_068_lqd_basefill_070(lqd_basefill_070):
    return _base_universe_d2(lqd_basefill_070, 68)
LQD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lqd_base_universe_d2_068_lqd_basefill_070'] = {'inputs': ['lqd_basefill_070'], 'func': lqd_base_universe_d2_068_lqd_basefill_070}


def lqd_base_universe_d2_069_lqd_basefill_071(lqd_basefill_071):
    return _base_universe_d2(lqd_basefill_071, 69)
LQD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lqd_base_universe_d2_069_lqd_basefill_071'] = {'inputs': ['lqd_basefill_071'], 'func': lqd_base_universe_d2_069_lqd_basefill_071}


def lqd_base_universe_d2_070_lqd_basefill_072(lqd_basefill_072):
    return _base_universe_d2(lqd_basefill_072, 70)
LQD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lqd_base_universe_d2_070_lqd_basefill_072'] = {'inputs': ['lqd_basefill_072'], 'func': lqd_base_universe_d2_070_lqd_basefill_072}


def lqd_base_universe_d2_071_lqd_basefill_073(lqd_basefill_073):
    return _base_universe_d2(lqd_basefill_073, 71)
LQD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lqd_base_universe_d2_071_lqd_basefill_073'] = {'inputs': ['lqd_basefill_073'], 'func': lqd_base_universe_d2_071_lqd_basefill_073}


def lqd_base_universe_d2_072_lqd_basefill_074(lqd_basefill_074):
    return _base_universe_d2(lqd_basefill_074, 72)
LQD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lqd_base_universe_d2_072_lqd_basefill_074'] = {'inputs': ['lqd_basefill_074'], 'func': lqd_base_universe_d2_072_lqd_basefill_074}


def lqd_base_universe_d2_073_lqd_basefill_075(lqd_basefill_075):
    return _base_universe_d2(lqd_basefill_075, 73)
LQD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lqd_base_universe_d2_073_lqd_basefill_075'] = {'inputs': ['lqd_basefill_075'], 'func': lqd_base_universe_d2_073_lqd_basefill_075}
