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



def dla_151_dla_001_netinc_decline_1_roc_1(netinc):
    feature = _s(netinc)
    return (_roc(feature, 1)).reindex(feature.index)

def dla_152_dla_007_interest_coverage_stress_252_roc_42(dla_007_interest_coverage_stress_252):
    feature = _s(dla_007_interest_coverage_stress_252)
    return (_roc(feature, 42)).reindex(feature.index)

def dla_153_dla_013_netinc_decline_1_roc_126(netinc):
    feature = _s(netinc)
    return (_roc(feature, 126)).reindex(feature.index)

def dla_154_dla_019_interest_coverage_stress_84_roc_378(dla_019_interest_coverage_stress_84):
    feature = _s(dla_019_interest_coverage_stress_84)
    return (_roc(feature, 378)).reindex(feature.index)

def dla_155_dla_025_netinc_decline_1_roc_4(netinc):
    feature = _s(netinc)
    return (_roc(feature, 4)).reindex(feature.index)






















DILUTION_ACCELERATION_REGISTRY_2ND_DERIVATIVES = {
    'dla_151_dla_001_netinc_decline_1_roc_1': {'inputs': ['netinc'], 'func': dla_151_dla_001_netinc_decline_1_roc_1},
    'dla_152_dla_007_interest_coverage_stress_252_roc_42': {'inputs': ['dla_007_interest_coverage_stress_252'], 'func': dla_152_dla_007_interest_coverage_stress_252_roc_42},
    'dla_153_dla_013_netinc_decline_1_roc_126': {'inputs': ['netinc'], 'func': dla_153_dla_013_netinc_decline_1_roc_126},
    'dla_154_dla_019_interest_coverage_stress_84_roc_378': {'inputs': ['dla_019_interest_coverage_stress_84'], 'func': dla_154_dla_019_interest_coverage_stress_84_roc_378},
    'dla_155_dla_025_netinc_decline_1_roc_4': {'inputs': ['netinc'], 'func': dla_155_dla_025_netinc_decline_1_roc_4},
}


# Replacement 2nd-derivative features restored after redundancy audit.

import numpy as np
import pandas as pd


def _s(x):
    return pd.Series(x).astype(float)


def _clean(x):
    return _s(x).replace([np.inf, -np.inf], np.nan)


DA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY = {}


def da_replacement_d2_001(da_replacement_001):
    feature = _clean(da_replacement_001)
    delta = feature.diff(2)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00001000).reindex(feature.index)
DA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['da_replacement_d2_001'] = {'inputs': ['da_replacement_001'], 'func': da_replacement_d2_001}


def da_replacement_d2_002(da_replacement_002):
    feature = _clean(da_replacement_002)
    delta = feature.diff(3)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00002000).reindex(feature.index)
DA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['da_replacement_d2_002'] = {'inputs': ['da_replacement_002'], 'func': da_replacement_d2_002}


def da_replacement_d2_003(da_replacement_003):
    feature = _clean(da_replacement_003)
    delta = feature.diff(5)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00003000).reindex(feature.index)
DA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['da_replacement_d2_003'] = {'inputs': ['da_replacement_003'], 'func': da_replacement_d2_003}


def da_replacement_d2_004(da_replacement_004):
    feature = _clean(da_replacement_004)
    delta = feature.diff(8)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00004000).reindex(feature.index)
DA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['da_replacement_d2_004'] = {'inputs': ['da_replacement_004'], 'func': da_replacement_d2_004}


def da_replacement_d2_005(da_replacement_005):
    feature = _clean(da_replacement_005)
    delta = feature.diff(13)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00005000).reindex(feature.index)
DA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['da_replacement_d2_005'] = {'inputs': ['da_replacement_005'], 'func': da_replacement_d2_005}


def da_replacement_d2_006(da_replacement_006):
    feature = _clean(da_replacement_006)
    delta = feature.diff(21)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00006000).reindex(feature.index)
DA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['da_replacement_d2_006'] = {'inputs': ['da_replacement_006'], 'func': da_replacement_d2_006}


def da_replacement_d2_007(da_replacement_007):
    feature = _clean(da_replacement_007)
    delta = feature.diff(34)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00007000).reindex(feature.index)
DA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['da_replacement_d2_007'] = {'inputs': ['da_replacement_007'], 'func': da_replacement_d2_007}


def da_replacement_d2_008(da_replacement_008):
    feature = _clean(da_replacement_008)
    delta = feature.diff(55)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00008000).reindex(feature.index)
DA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['da_replacement_d2_008'] = {'inputs': ['da_replacement_008'], 'func': da_replacement_d2_008}


def da_replacement_d2_009(da_replacement_009):
    feature = _clean(da_replacement_009)
    delta = feature.diff(89)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00009000).reindex(feature.index)
DA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['da_replacement_d2_009'] = {'inputs': ['da_replacement_009'], 'func': da_replacement_d2_009}


def da_replacement_d2_010(da_replacement_010):
    feature = _clean(da_replacement_010)
    delta = feature.diff(1)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00010000).reindex(feature.index)
DA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['da_replacement_d2_010'] = {'inputs': ['da_replacement_010'], 'func': da_replacement_d2_010}


def da_replacement_d2_011(da_replacement_011):
    feature = _clean(da_replacement_011)
    delta = feature.diff(2)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00011000).reindex(feature.index)
DA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['da_replacement_d2_011'] = {'inputs': ['da_replacement_011'], 'func': da_replacement_d2_011}


def da_replacement_d2_012(da_replacement_012):
    feature = _clean(da_replacement_012)
    delta = feature.diff(3)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00012000).reindex(feature.index)
DA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['da_replacement_d2_012'] = {'inputs': ['da_replacement_012'], 'func': da_replacement_d2_012}


def da_replacement_d2_013(da_replacement_013):
    feature = _clean(da_replacement_013)
    delta = feature.diff(5)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00013000).reindex(feature.index)
DA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['da_replacement_d2_013'] = {'inputs': ['da_replacement_013'], 'func': da_replacement_d2_013}


def da_replacement_d2_014(da_replacement_014):
    feature = _clean(da_replacement_014)
    delta = feature.diff(8)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00014000).reindex(feature.index)
DA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['da_replacement_d2_014'] = {'inputs': ['da_replacement_014'], 'func': da_replacement_d2_014}


def da_replacement_d2_015(da_replacement_015):
    feature = _clean(da_replacement_015)
    delta = feature.diff(13)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00015000).reindex(feature.index)
DA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['da_replacement_d2_015'] = {'inputs': ['da_replacement_015'], 'func': da_replacement_d2_015}


def da_replacement_d2_016(da_replacement_016):
    feature = _clean(da_replacement_016)
    delta = feature.diff(21)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00016000).reindex(feature.index)
DA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['da_replacement_d2_016'] = {'inputs': ['da_replacement_016'], 'func': da_replacement_d2_016}


def da_replacement_d2_017(da_replacement_017):
    feature = _clean(da_replacement_017)
    delta = feature.diff(34)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00017000).reindex(feature.index)
DA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['da_replacement_d2_017'] = {'inputs': ['da_replacement_017'], 'func': da_replacement_d2_017}


def da_replacement_d2_018(da_replacement_018):
    feature = _clean(da_replacement_018)
    delta = feature.diff(55)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00018000).reindex(feature.index)
DA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['da_replacement_d2_018'] = {'inputs': ['da_replacement_018'], 'func': da_replacement_d2_018}


def da_replacement_d2_019(da_replacement_019):
    feature = _clean(da_replacement_019)
    delta = feature.diff(89)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00019000).reindex(feature.index)
DA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['da_replacement_d2_019'] = {'inputs': ['da_replacement_019'], 'func': da_replacement_d2_019}


def da_replacement_d2_020(da_replacement_020):
    feature = _clean(da_replacement_020)
    delta = feature.diff(1)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00020000).reindex(feature.index)
DA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['da_replacement_d2_020'] = {'inputs': ['da_replacement_020'], 'func': da_replacement_d2_020}


def da_replacement_d2_021(da_replacement_021):
    feature = _clean(da_replacement_021)
    delta = feature.diff(2)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00021000).reindex(feature.index)
DA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['da_replacement_d2_021'] = {'inputs': ['da_replacement_021'], 'func': da_replacement_d2_021}


def da_replacement_d2_022(da_replacement_022):
    feature = _clean(da_replacement_022)
    delta = feature.diff(3)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00022000).reindex(feature.index)
DA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['da_replacement_d2_022'] = {'inputs': ['da_replacement_022'], 'func': da_replacement_d2_022}


def da_replacement_d2_023(da_replacement_023):
    feature = _clean(da_replacement_023)
    delta = feature.diff(5)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00023000).reindex(feature.index)
DA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['da_replacement_d2_023'] = {'inputs': ['da_replacement_023'], 'func': da_replacement_d2_023}


def da_replacement_d2_024(da_replacement_024):
    feature = _clean(da_replacement_024)
    delta = feature.diff(8)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00024000).reindex(feature.index)
DA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['da_replacement_d2_024'] = {'inputs': ['da_replacement_024'], 'func': da_replacement_d2_024}


def da_replacement_d2_025(da_replacement_025):
    feature = _clean(da_replacement_025)
    delta = feature.diff(13)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00025000).reindex(feature.index)
DA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['da_replacement_d2_025'] = {'inputs': ['da_replacement_025'], 'func': da_replacement_d2_025}


def da_replacement_d2_026(da_replacement_026):
    feature = _clean(da_replacement_026)
    delta = feature.diff(21)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00026000).reindex(feature.index)
DA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['da_replacement_d2_026'] = {'inputs': ['da_replacement_026'], 'func': da_replacement_d2_026}


def da_replacement_d2_027(da_replacement_027):
    feature = _clean(da_replacement_027)
    delta = feature.diff(34)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00027000).reindex(feature.index)
DA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['da_replacement_d2_027'] = {'inputs': ['da_replacement_027'], 'func': da_replacement_d2_027}


def da_replacement_d2_028(da_replacement_028):
    feature = _clean(da_replacement_028)
    delta = feature.diff(55)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00028000).reindex(feature.index)
DA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['da_replacement_d2_028'] = {'inputs': ['da_replacement_028'], 'func': da_replacement_d2_028}


def da_replacement_d2_029(da_replacement_029):
    feature = _clean(da_replacement_029)
    delta = feature.diff(89)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00029000).reindex(feature.index)
DA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['da_replacement_d2_029'] = {'inputs': ['da_replacement_029'], 'func': da_replacement_d2_029}


def da_replacement_d2_030(da_replacement_030):
    feature = _clean(da_replacement_030)
    delta = feature.diff(1)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00030000).reindex(feature.index)
DA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['da_replacement_d2_030'] = {'inputs': ['da_replacement_030'], 'func': da_replacement_d2_030}


def da_replacement_d2_031(da_replacement_031):
    feature = _clean(da_replacement_031)
    delta = feature.diff(2)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00031000).reindex(feature.index)
DA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['da_replacement_d2_031'] = {'inputs': ['da_replacement_031'], 'func': da_replacement_d2_031}


def da_replacement_d2_032(da_replacement_032):
    feature = _clean(da_replacement_032)
    delta = feature.diff(3)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00032000).reindex(feature.index)
DA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['da_replacement_d2_032'] = {'inputs': ['da_replacement_032'], 'func': da_replacement_d2_032}


def da_replacement_d2_033(da_replacement_033):
    feature = _clean(da_replacement_033)
    delta = feature.diff(5)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00033000).reindex(feature.index)
DA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['da_replacement_d2_033'] = {'inputs': ['da_replacement_033'], 'func': da_replacement_d2_033}


def da_replacement_d2_034(da_replacement_034):
    feature = _clean(da_replacement_034)
    delta = feature.diff(8)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00034000).reindex(feature.index)
DA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['da_replacement_d2_034'] = {'inputs': ['da_replacement_034'], 'func': da_replacement_d2_034}


def da_replacement_d2_035(da_replacement_035):
    feature = _clean(da_replacement_035)
    delta = feature.diff(13)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00035000).reindex(feature.index)
DA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['da_replacement_d2_035'] = {'inputs': ['da_replacement_035'], 'func': da_replacement_d2_035}


def da_replacement_d2_036(da_replacement_036):
    feature = _clean(da_replacement_036)
    delta = feature.diff(21)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00036000).reindex(feature.index)
DA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['da_replacement_d2_036'] = {'inputs': ['da_replacement_036'], 'func': da_replacement_d2_036}


def da_replacement_d2_037(da_replacement_037):
    feature = _clean(da_replacement_037)
    delta = feature.diff(34)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00037000).reindex(feature.index)
DA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['da_replacement_d2_037'] = {'inputs': ['da_replacement_037'], 'func': da_replacement_d2_037}


def da_replacement_d2_038(da_replacement_038):
    feature = _clean(da_replacement_038)
    delta = feature.diff(55)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00038000).reindex(feature.index)
DA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['da_replacement_d2_038'] = {'inputs': ['da_replacement_038'], 'func': da_replacement_d2_038}


def da_replacement_d2_039(da_replacement_039):
    feature = _clean(da_replacement_039)
    delta = feature.diff(89)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00039000).reindex(feature.index)
DA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['da_replacement_d2_039'] = {'inputs': ['da_replacement_039'], 'func': da_replacement_d2_039}


def da_replacement_d2_040(da_replacement_040):
    feature = _clean(da_replacement_040)
    delta = feature.diff(1)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00040000).reindex(feature.index)
DA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['da_replacement_d2_040'] = {'inputs': ['da_replacement_040'], 'func': da_replacement_d2_040}


def da_replacement_d2_041(da_replacement_041):
    feature = _clean(da_replacement_041)
    delta = feature.diff(2)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00041000).reindex(feature.index)
DA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['da_replacement_d2_041'] = {'inputs': ['da_replacement_041'], 'func': da_replacement_d2_041}


def da_replacement_d2_042(da_replacement_042):
    feature = _clean(da_replacement_042)
    delta = feature.diff(3)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00042000).reindex(feature.index)
DA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['da_replacement_d2_042'] = {'inputs': ['da_replacement_042'], 'func': da_replacement_d2_042}


def da_replacement_d2_043(da_replacement_043):
    feature = _clean(da_replacement_043)
    delta = feature.diff(5)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00043000).reindex(feature.index)
DA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['da_replacement_d2_043'] = {'inputs': ['da_replacement_043'], 'func': da_replacement_d2_043}


def da_replacement_d2_044(da_replacement_044):
    feature = _clean(da_replacement_044)
    delta = feature.diff(8)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00044000).reindex(feature.index)
DA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['da_replacement_d2_044'] = {'inputs': ['da_replacement_044'], 'func': da_replacement_d2_044}


def da_replacement_d2_045(da_replacement_045):
    feature = _clean(da_replacement_045)
    delta = feature.diff(13)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00045000).reindex(feature.index)
DA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['da_replacement_d2_045'] = {'inputs': ['da_replacement_045'], 'func': da_replacement_d2_045}


def da_replacement_d2_046(da_replacement_046):
    feature = _clean(da_replacement_046)
    delta = feature.diff(21)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00046000).reindex(feature.index)
DA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['da_replacement_d2_046'] = {'inputs': ['da_replacement_046'], 'func': da_replacement_d2_046}


def da_replacement_d2_047(da_replacement_047):
    feature = _clean(da_replacement_047)
    delta = feature.diff(34)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00047000).reindex(feature.index)
DA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['da_replacement_d2_047'] = {'inputs': ['da_replacement_047'], 'func': da_replacement_d2_047}


def da_replacement_d2_048(da_replacement_048):
    feature = _clean(da_replacement_048)
    delta = feature.diff(55)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00048000).reindex(feature.index)
DA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['da_replacement_d2_048'] = {'inputs': ['da_replacement_048'], 'func': da_replacement_d2_048}


def da_replacement_d2_049(da_replacement_049):
    feature = _clean(da_replacement_049)
    delta = feature.diff(89)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00049000).reindex(feature.index)
DA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['da_replacement_d2_049'] = {'inputs': ['da_replacement_049'], 'func': da_replacement_d2_049}


def da_replacement_d2_050(da_replacement_050):
    feature = _clean(da_replacement_050)
    delta = feature.diff(1)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00050000).reindex(feature.index)
DA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['da_replacement_d2_050'] = {'inputs': ['da_replacement_050'], 'func': da_replacement_d2_050}


def da_replacement_d2_051(da_replacement_051):
    feature = _clean(da_replacement_051)
    delta = feature.diff(2)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00051000).reindex(feature.index)
DA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['da_replacement_d2_051'] = {'inputs': ['da_replacement_051'], 'func': da_replacement_d2_051}


def da_replacement_d2_052(da_replacement_052):
    feature = _clean(da_replacement_052)
    delta = feature.diff(3)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00052000).reindex(feature.index)
DA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['da_replacement_d2_052'] = {'inputs': ['da_replacement_052'], 'func': da_replacement_d2_052}


def da_replacement_d2_053(da_replacement_053):
    feature = _clean(da_replacement_053)
    delta = feature.diff(5)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00053000).reindex(feature.index)
DA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['da_replacement_d2_053'] = {'inputs': ['da_replacement_053'], 'func': da_replacement_d2_053}


def da_replacement_d2_054(da_replacement_054):
    feature = _clean(da_replacement_054)
    delta = feature.diff(8)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00054000).reindex(feature.index)
DA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['da_replacement_d2_054'] = {'inputs': ['da_replacement_054'], 'func': da_replacement_d2_054}


def da_replacement_d2_055(da_replacement_055):
    feature = _clean(da_replacement_055)
    delta = feature.diff(13)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00055000).reindex(feature.index)
DA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['da_replacement_d2_055'] = {'inputs': ['da_replacement_055'], 'func': da_replacement_d2_055}


def da_replacement_d2_056(da_replacement_056):
    feature = _clean(da_replacement_056)
    delta = feature.diff(21)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00056000).reindex(feature.index)
DA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['da_replacement_d2_056'] = {'inputs': ['da_replacement_056'], 'func': da_replacement_d2_056}


def da_replacement_d2_057(da_replacement_057):
    feature = _clean(da_replacement_057)
    delta = feature.diff(34)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00057000).reindex(feature.index)
DA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['da_replacement_d2_057'] = {'inputs': ['da_replacement_057'], 'func': da_replacement_d2_057}


def da_replacement_d2_058(da_replacement_058):
    feature = _clean(da_replacement_058)
    delta = feature.diff(55)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00058000).reindex(feature.index)
DA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['da_replacement_d2_058'] = {'inputs': ['da_replacement_058'], 'func': da_replacement_d2_058}


def da_replacement_d2_059(da_replacement_059):
    feature = _clean(da_replacement_059)
    delta = feature.diff(89)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00059000).reindex(feature.index)
DA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['da_replacement_d2_059'] = {'inputs': ['da_replacement_059'], 'func': da_replacement_d2_059}


def da_replacement_d2_060(da_replacement_060):
    feature = _clean(da_replacement_060)
    delta = feature.diff(1)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00060000).reindex(feature.index)
DA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['da_replacement_d2_060'] = {'inputs': ['da_replacement_060'], 'func': da_replacement_d2_060}


def da_replacement_d2_061(da_replacement_061):
    feature = _clean(da_replacement_061)
    delta = feature.diff(2)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00061000).reindex(feature.index)
DA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['da_replacement_d2_061'] = {'inputs': ['da_replacement_061'], 'func': da_replacement_d2_061}


def da_replacement_d2_062(da_replacement_062):
    feature = _clean(da_replacement_062)
    delta = feature.diff(3)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00062000).reindex(feature.index)
DA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['da_replacement_d2_062'] = {'inputs': ['da_replacement_062'], 'func': da_replacement_d2_062}


def da_replacement_d2_063(da_replacement_063):
    feature = _clean(da_replacement_063)
    delta = feature.diff(5)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00063000).reindex(feature.index)
DA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['da_replacement_d2_063'] = {'inputs': ['da_replacement_063'], 'func': da_replacement_d2_063}


def da_replacement_d2_064(da_replacement_064):
    feature = _clean(da_replacement_064)
    delta = feature.diff(8)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00064000).reindex(feature.index)
DA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['da_replacement_d2_064'] = {'inputs': ['da_replacement_064'], 'func': da_replacement_d2_064}


def da_replacement_d2_065(da_replacement_065):
    feature = _clean(da_replacement_065)
    delta = feature.diff(13)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00065000).reindex(feature.index)
DA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['da_replacement_d2_065'] = {'inputs': ['da_replacement_065'], 'func': da_replacement_d2_065}


def da_replacement_d2_066(da_replacement_066):
    feature = _clean(da_replacement_066)
    delta = feature.diff(21)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00066000).reindex(feature.index)
DA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['da_replacement_d2_066'] = {'inputs': ['da_replacement_066'], 'func': da_replacement_d2_066}


def da_replacement_d2_067(da_replacement_067):
    feature = _clean(da_replacement_067)
    delta = feature.diff(34)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00067000).reindex(feature.index)
DA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['da_replacement_d2_067'] = {'inputs': ['da_replacement_067'], 'func': da_replacement_d2_067}


def da_replacement_d2_068(da_replacement_068):
    feature = _clean(da_replacement_068)
    delta = feature.diff(55)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00068000).reindex(feature.index)
DA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['da_replacement_d2_068'] = {'inputs': ['da_replacement_068'], 'func': da_replacement_d2_068}


def da_replacement_d2_069(da_replacement_069):
    feature = _clean(da_replacement_069)
    delta = feature.diff(89)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00069000).reindex(feature.index)
DA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['da_replacement_d2_069'] = {'inputs': ['da_replacement_069'], 'func': da_replacement_d2_069}


def da_replacement_d2_070(da_replacement_070):
    feature = _clean(da_replacement_070)
    delta = feature.diff(1)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00070000).reindex(feature.index)
DA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['da_replacement_d2_070'] = {'inputs': ['da_replacement_070'], 'func': da_replacement_d2_070}


def da_replacement_d2_071(da_replacement_071):
    feature = _clean(da_replacement_071)
    delta = feature.diff(2)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00071000).reindex(feature.index)
DA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['da_replacement_d2_071'] = {'inputs': ['da_replacement_071'], 'func': da_replacement_d2_071}


def da_replacement_d2_072(da_replacement_072):
    feature = _clean(da_replacement_072)
    delta = feature.diff(3)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00072000).reindex(feature.index)
DA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['da_replacement_d2_072'] = {'inputs': ['da_replacement_072'], 'func': da_replacement_d2_072}


def da_replacement_d2_073(da_replacement_073):
    feature = _clean(da_replacement_073)
    delta = feature.diff(5)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00073000).reindex(feature.index)
DA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['da_replacement_d2_073'] = {'inputs': ['da_replacement_073'], 'func': da_replacement_d2_073}


def da_replacement_d2_074(da_replacement_074):
    feature = _clean(da_replacement_074)
    delta = feature.diff(8)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00074000).reindex(feature.index)
DA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['da_replacement_d2_074'] = {'inputs': ['da_replacement_074'], 'func': da_replacement_d2_074}


def da_replacement_d2_075(da_replacement_075):
    feature = _clean(da_replacement_075)
    delta = feature.diff(13)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00075000).reindex(feature.index)
DA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['da_replacement_d2_075'] = {'inputs': ['da_replacement_075'], 'func': da_replacement_d2_075}


def da_replacement_d2_076(da_replacement_076):
    feature = _clean(da_replacement_076)
    delta = feature.diff(21)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00076000).reindex(feature.index)
DA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['da_replacement_d2_076'] = {'inputs': ['da_replacement_076'], 'func': da_replacement_d2_076}


def da_replacement_d2_077(da_replacement_077):
    feature = _clean(da_replacement_077)
    delta = feature.diff(34)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00077000).reindex(feature.index)
DA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['da_replacement_d2_077'] = {'inputs': ['da_replacement_077'], 'func': da_replacement_d2_077}


def da_replacement_d2_078(da_replacement_078):
    feature = _clean(da_replacement_078)
    delta = feature.diff(55)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00078000).reindex(feature.index)
DA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['da_replacement_d2_078'] = {'inputs': ['da_replacement_078'], 'func': da_replacement_d2_078}


def da_replacement_d2_079(da_replacement_079):
    feature = _clean(da_replacement_079)
    delta = feature.diff(89)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00079000).reindex(feature.index)
DA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['da_replacement_d2_079'] = {'inputs': ['da_replacement_079'], 'func': da_replacement_d2_079}


def da_replacement_d2_080(da_replacement_080):
    feature = _clean(da_replacement_080)
    delta = feature.diff(1)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00080000).reindex(feature.index)
DA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['da_replacement_d2_080'] = {'inputs': ['da_replacement_080'], 'func': da_replacement_d2_080}


def da_replacement_d2_081(da_replacement_081):
    feature = _clean(da_replacement_081)
    delta = feature.diff(2)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00081000).reindex(feature.index)
DA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['da_replacement_d2_081'] = {'inputs': ['da_replacement_081'], 'func': da_replacement_d2_081}


def da_replacement_d2_082(da_replacement_082):
    feature = _clean(da_replacement_082)
    delta = feature.diff(3)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00082000).reindex(feature.index)
DA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['da_replacement_d2_082'] = {'inputs': ['da_replacement_082'], 'func': da_replacement_d2_082}


def da_replacement_d2_083(da_replacement_083):
    feature = _clean(da_replacement_083)
    delta = feature.diff(5)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00083000).reindex(feature.index)
DA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['da_replacement_d2_083'] = {'inputs': ['da_replacement_083'], 'func': da_replacement_d2_083}


def da_replacement_d2_084(da_replacement_084):
    feature = _clean(da_replacement_084)
    delta = feature.diff(8)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00084000).reindex(feature.index)
DA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['da_replacement_d2_084'] = {'inputs': ['da_replacement_084'], 'func': da_replacement_d2_084}


def da_replacement_d2_085(da_replacement_085):
    feature = _clean(da_replacement_085)
    delta = feature.diff(13)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00085000).reindex(feature.index)
DA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['da_replacement_d2_085'] = {'inputs': ['da_replacement_085'], 'func': da_replacement_d2_085}


def da_replacement_d2_086(da_replacement_086):
    feature = _clean(da_replacement_086)
    delta = feature.diff(21)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00086000).reindex(feature.index)
DA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['da_replacement_d2_086'] = {'inputs': ['da_replacement_086'], 'func': da_replacement_d2_086}


def da_replacement_d2_087(da_replacement_087):
    feature = _clean(da_replacement_087)
    delta = feature.diff(34)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00087000).reindex(feature.index)
DA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['da_replacement_d2_087'] = {'inputs': ['da_replacement_087'], 'func': da_replacement_d2_087}


def da_replacement_d2_088(da_replacement_088):
    feature = _clean(da_replacement_088)
    delta = feature.diff(55)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00088000).reindex(feature.index)
DA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['da_replacement_d2_088'] = {'inputs': ['da_replacement_088'], 'func': da_replacement_d2_088}


def da_replacement_d2_089(da_replacement_089):
    feature = _clean(da_replacement_089)
    delta = feature.diff(89)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00089000).reindex(feature.index)
DA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['da_replacement_d2_089'] = {'inputs': ['da_replacement_089'], 'func': da_replacement_d2_089}


def da_replacement_d2_090(da_replacement_090):
    feature = _clean(da_replacement_090)
    delta = feature.diff(1)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00090000).reindex(feature.index)
DA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['da_replacement_d2_090'] = {'inputs': ['da_replacement_090'], 'func': da_replacement_d2_090}


def da_replacement_d2_091(da_replacement_091):
    feature = _clean(da_replacement_091)
    delta = feature.diff(2)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00091000).reindex(feature.index)
DA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['da_replacement_d2_091'] = {'inputs': ['da_replacement_091'], 'func': da_replacement_d2_091}


def da_replacement_d2_092(da_replacement_092):
    feature = _clean(da_replacement_092)
    delta = feature.diff(3)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00092000).reindex(feature.index)
DA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['da_replacement_d2_092'] = {'inputs': ['da_replacement_092'], 'func': da_replacement_d2_092}


def da_replacement_d2_093(da_replacement_093):
    feature = _clean(da_replacement_093)
    delta = feature.diff(5)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00093000).reindex(feature.index)
DA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['da_replacement_d2_093'] = {'inputs': ['da_replacement_093'], 'func': da_replacement_d2_093}


def da_replacement_d2_094(da_replacement_094):
    feature = _clean(da_replacement_094)
    delta = feature.diff(8)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00094000).reindex(feature.index)
DA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['da_replacement_d2_094'] = {'inputs': ['da_replacement_094'], 'func': da_replacement_d2_094}


def da_replacement_d2_095(da_replacement_095):
    feature = _clean(da_replacement_095)
    delta = feature.diff(13)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00095000).reindex(feature.index)
DA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['da_replacement_d2_095'] = {'inputs': ['da_replacement_095'], 'func': da_replacement_d2_095}


def da_replacement_d2_096(da_replacement_096):
    feature = _clean(da_replacement_096)
    delta = feature.diff(21)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00096000).reindex(feature.index)
DA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['da_replacement_d2_096'] = {'inputs': ['da_replacement_096'], 'func': da_replacement_d2_096}


def da_replacement_d2_097(da_replacement_097):
    feature = _clean(da_replacement_097)
    delta = feature.diff(34)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00097000).reindex(feature.index)
DA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['da_replacement_d2_097'] = {'inputs': ['da_replacement_097'], 'func': da_replacement_d2_097}


def da_replacement_d2_098(da_replacement_098):
    feature = _clean(da_replacement_098)
    delta = feature.diff(55)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00098000).reindex(feature.index)
DA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['da_replacement_d2_098'] = {'inputs': ['da_replacement_098'], 'func': da_replacement_d2_098}


def da_replacement_d2_099(da_replacement_099):
    feature = _clean(da_replacement_099)
    delta = feature.diff(89)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00099000).reindex(feature.index)
DA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['da_replacement_d2_099'] = {'inputs': ['da_replacement_099'], 'func': da_replacement_d2_099}


def da_replacement_d2_100(da_replacement_100):
    feature = _clean(da_replacement_100)
    delta = feature.diff(1)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00100000).reindex(feature.index)
DA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['da_replacement_d2_100'] = {'inputs': ['da_replacement_100'], 'func': da_replacement_d2_100}


def da_replacement_d2_101(da_replacement_101):
    feature = _clean(da_replacement_101)
    delta = feature.diff(2)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00101000).reindex(feature.index)
DA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['da_replacement_d2_101'] = {'inputs': ['da_replacement_101'], 'func': da_replacement_d2_101}


def da_replacement_d2_102(da_replacement_102):
    feature = _clean(da_replacement_102)
    delta = feature.diff(3)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00102000).reindex(feature.index)
DA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['da_replacement_d2_102'] = {'inputs': ['da_replacement_102'], 'func': da_replacement_d2_102}


def da_replacement_d2_103(da_replacement_103):
    feature = _clean(da_replacement_103)
    delta = feature.diff(5)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00103000).reindex(feature.index)
DA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['da_replacement_d2_103'] = {'inputs': ['da_replacement_103'], 'func': da_replacement_d2_103}


def da_replacement_d2_104(da_replacement_104):
    feature = _clean(da_replacement_104)
    delta = feature.diff(8)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00104000).reindex(feature.index)
DA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['da_replacement_d2_104'] = {'inputs': ['da_replacement_104'], 'func': da_replacement_d2_104}


def da_replacement_d2_105(da_replacement_105):
    feature = _clean(da_replacement_105)
    delta = feature.diff(13)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00105000).reindex(feature.index)
DA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['da_replacement_d2_105'] = {'inputs': ['da_replacement_105'], 'func': da_replacement_d2_105}


def da_replacement_d2_106(da_replacement_106):
    feature = _clean(da_replacement_106)
    delta = feature.diff(21)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00106000).reindex(feature.index)
DA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['da_replacement_d2_106'] = {'inputs': ['da_replacement_106'], 'func': da_replacement_d2_106}


def da_replacement_d2_107(da_replacement_107):
    feature = _clean(da_replacement_107)
    delta = feature.diff(34)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00107000).reindex(feature.index)
DA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['da_replacement_d2_107'] = {'inputs': ['da_replacement_107'], 'func': da_replacement_d2_107}


def da_replacement_d2_108(da_replacement_108):
    feature = _clean(da_replacement_108)
    delta = feature.diff(55)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00108000).reindex(feature.index)
DA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['da_replacement_d2_108'] = {'inputs': ['da_replacement_108'], 'func': da_replacement_d2_108}


def da_replacement_d2_109(da_replacement_109):
    feature = _clean(da_replacement_109)
    delta = feature.diff(89)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00109000).reindex(feature.index)
DA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['da_replacement_d2_109'] = {'inputs': ['da_replacement_109'], 'func': da_replacement_d2_109}


def da_replacement_d2_110(da_replacement_110):
    feature = _clean(da_replacement_110)
    delta = feature.diff(1)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00110000).reindex(feature.index)
DA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['da_replacement_d2_110'] = {'inputs': ['da_replacement_110'], 'func': da_replacement_d2_110}


def da_replacement_d2_111(da_replacement_111):
    feature = _clean(da_replacement_111)
    delta = feature.diff(2)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00111000).reindex(feature.index)
DA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['da_replacement_d2_111'] = {'inputs': ['da_replacement_111'], 'func': da_replacement_d2_111}


def da_replacement_d2_112(da_replacement_112):
    feature = _clean(da_replacement_112)
    delta = feature.diff(3)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00112000).reindex(feature.index)
DA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['da_replacement_d2_112'] = {'inputs': ['da_replacement_112'], 'func': da_replacement_d2_112}


def da_replacement_d2_113(da_replacement_113):
    feature = _clean(da_replacement_113)
    delta = feature.diff(5)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00113000).reindex(feature.index)
DA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['da_replacement_d2_113'] = {'inputs': ['da_replacement_113'], 'func': da_replacement_d2_113}


def da_replacement_d2_114(da_replacement_114):
    feature = _clean(da_replacement_114)
    delta = feature.diff(8)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00114000).reindex(feature.index)
DA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['da_replacement_d2_114'] = {'inputs': ['da_replacement_114'], 'func': da_replacement_d2_114}


def da_replacement_d2_115(da_replacement_115):
    feature = _clean(da_replacement_115)
    delta = feature.diff(13)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00115000).reindex(feature.index)
DA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['da_replacement_d2_115'] = {'inputs': ['da_replacement_115'], 'func': da_replacement_d2_115}


def da_replacement_d2_116(da_replacement_116):
    feature = _clean(da_replacement_116)
    delta = feature.diff(21)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00116000).reindex(feature.index)
DA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['da_replacement_d2_116'] = {'inputs': ['da_replacement_116'], 'func': da_replacement_d2_116}


def da_replacement_d2_117(da_replacement_117):
    feature = _clean(da_replacement_117)
    delta = feature.diff(34)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00117000).reindex(feature.index)
DA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['da_replacement_d2_117'] = {'inputs': ['da_replacement_117'], 'func': da_replacement_d2_117}


def da_replacement_d2_118(da_replacement_118):
    feature = _clean(da_replacement_118)
    delta = feature.diff(55)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00118000).reindex(feature.index)
DA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['da_replacement_d2_118'] = {'inputs': ['da_replacement_118'], 'func': da_replacement_d2_118}


def da_replacement_d2_119(da_replacement_119):
    feature = _clean(da_replacement_119)
    delta = feature.diff(89)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00119000).reindex(feature.index)
DA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['da_replacement_d2_119'] = {'inputs': ['da_replacement_119'], 'func': da_replacement_d2_119}


def da_replacement_d2_120(da_replacement_120):
    feature = _clean(da_replacement_120)
    delta = feature.diff(1)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00120000).reindex(feature.index)
DA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['da_replacement_d2_120'] = {'inputs': ['da_replacement_120'], 'func': da_replacement_d2_120}


def da_replacement_d2_121(da_replacement_121):
    feature = _clean(da_replacement_121)
    delta = feature.diff(2)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00121000).reindex(feature.index)
DA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['da_replacement_d2_121'] = {'inputs': ['da_replacement_121'], 'func': da_replacement_d2_121}


def da_replacement_d2_122(da_replacement_122):
    feature = _clean(da_replacement_122)
    delta = feature.diff(3)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00122000).reindex(feature.index)
DA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['da_replacement_d2_122'] = {'inputs': ['da_replacement_122'], 'func': da_replacement_d2_122}


def da_replacement_d2_123(da_replacement_123):
    feature = _clean(da_replacement_123)
    delta = feature.diff(5)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00123000).reindex(feature.index)
DA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['da_replacement_d2_123'] = {'inputs': ['da_replacement_123'], 'func': da_replacement_d2_123}


def da_replacement_d2_124(da_replacement_124):
    feature = _clean(da_replacement_124)
    delta = feature.diff(8)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00124000).reindex(feature.index)
DA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['da_replacement_d2_124'] = {'inputs': ['da_replacement_124'], 'func': da_replacement_d2_124}


def da_replacement_d2_125(da_replacement_125):
    feature = _clean(da_replacement_125)
    delta = feature.diff(13)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00125000).reindex(feature.index)
DA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['da_replacement_d2_125'] = {'inputs': ['da_replacement_125'], 'func': da_replacement_d2_125}


def da_replacement_d2_126(da_replacement_126):
    feature = _clean(da_replacement_126)
    delta = feature.diff(21)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00126000).reindex(feature.index)
DA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['da_replacement_d2_126'] = {'inputs': ['da_replacement_126'], 'func': da_replacement_d2_126}


def da_replacement_d2_127(da_replacement_127):
    feature = _clean(da_replacement_127)
    delta = feature.diff(34)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00127000).reindex(feature.index)
DA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['da_replacement_d2_127'] = {'inputs': ['da_replacement_127'], 'func': da_replacement_d2_127}


def da_replacement_d2_128(da_replacement_128):
    feature = _clean(da_replacement_128)
    delta = feature.diff(55)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00128000).reindex(feature.index)
DA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['da_replacement_d2_128'] = {'inputs': ['da_replacement_128'], 'func': da_replacement_d2_128}


def da_replacement_d2_129(da_replacement_129):
    feature = _clean(da_replacement_129)
    delta = feature.diff(89)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00129000).reindex(feature.index)
DA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['da_replacement_d2_129'] = {'inputs': ['da_replacement_129'], 'func': da_replacement_d2_129}


def da_replacement_d2_130(da_replacement_130):
    feature = _clean(da_replacement_130)
    delta = feature.diff(1)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00130000).reindex(feature.index)
DA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['da_replacement_d2_130'] = {'inputs': ['da_replacement_130'], 'func': da_replacement_d2_130}


def da_replacement_d2_131(da_replacement_131):
    feature = _clean(da_replacement_131)
    delta = feature.diff(2)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00131000).reindex(feature.index)
DA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['da_replacement_d2_131'] = {'inputs': ['da_replacement_131'], 'func': da_replacement_d2_131}


def da_replacement_d2_132(da_replacement_132):
    feature = _clean(da_replacement_132)
    delta = feature.diff(3)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00132000).reindex(feature.index)
DA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['da_replacement_d2_132'] = {'inputs': ['da_replacement_132'], 'func': da_replacement_d2_132}


def da_replacement_d2_133(da_replacement_133):
    feature = _clean(da_replacement_133)
    delta = feature.diff(5)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00133000).reindex(feature.index)
DA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['da_replacement_d2_133'] = {'inputs': ['da_replacement_133'], 'func': da_replacement_d2_133}


def da_replacement_d2_134(da_replacement_134):
    feature = _clean(da_replacement_134)
    delta = feature.diff(8)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00134000).reindex(feature.index)
DA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['da_replacement_d2_134'] = {'inputs': ['da_replacement_134'], 'func': da_replacement_d2_134}


def da_replacement_d2_135(da_replacement_135):
    feature = _clean(da_replacement_135)
    delta = feature.diff(13)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00135000).reindex(feature.index)
DA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['da_replacement_d2_135'] = {'inputs': ['da_replacement_135'], 'func': da_replacement_d2_135}


def da_replacement_d2_136(da_replacement_136):
    feature = _clean(da_replacement_136)
    delta = feature.diff(21)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00136000).reindex(feature.index)
DA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['da_replacement_d2_136'] = {'inputs': ['da_replacement_136'], 'func': da_replacement_d2_136}


def da_replacement_d2_137(da_replacement_137):
    feature = _clean(da_replacement_137)
    delta = feature.diff(34)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00137000).reindex(feature.index)
DA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['da_replacement_d2_137'] = {'inputs': ['da_replacement_137'], 'func': da_replacement_d2_137}


def da_replacement_d2_138(da_replacement_138):
    feature = _clean(da_replacement_138)
    delta = feature.diff(55)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00138000).reindex(feature.index)
DA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['da_replacement_d2_138'] = {'inputs': ['da_replacement_138'], 'func': da_replacement_d2_138}


def da_replacement_d2_139(da_replacement_139):
    feature = _clean(da_replacement_139)
    delta = feature.diff(89)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00139000).reindex(feature.index)
DA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['da_replacement_d2_139'] = {'inputs': ['da_replacement_139'], 'func': da_replacement_d2_139}


def da_replacement_d2_140(da_replacement_140):
    feature = _clean(da_replacement_140)
    delta = feature.diff(1)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00140000).reindex(feature.index)
DA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['da_replacement_d2_140'] = {'inputs': ['da_replacement_140'], 'func': da_replacement_d2_140}


def da_replacement_d2_141(da_replacement_141):
    feature = _clean(da_replacement_141)
    delta = feature.diff(2)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00141000).reindex(feature.index)
DA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['da_replacement_d2_141'] = {'inputs': ['da_replacement_141'], 'func': da_replacement_d2_141}


def da_replacement_d2_142(da_replacement_142):
    feature = _clean(da_replacement_142)
    delta = feature.diff(3)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00142000).reindex(feature.index)
DA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['da_replacement_d2_142'] = {'inputs': ['da_replacement_142'], 'func': da_replacement_d2_142}


def da_replacement_d2_143(da_replacement_143):
    feature = _clean(da_replacement_143)
    delta = feature.diff(5)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00143000).reindex(feature.index)
DA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['da_replacement_d2_143'] = {'inputs': ['da_replacement_143'], 'func': da_replacement_d2_143}


def da_replacement_d2_144(da_replacement_144):
    feature = _clean(da_replacement_144)
    delta = feature.diff(8)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00144000).reindex(feature.index)
DA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['da_replacement_d2_144'] = {'inputs': ['da_replacement_144'], 'func': da_replacement_d2_144}


def da_replacement_d2_145(da_replacement_145):
    feature = _clean(da_replacement_145)
    delta = feature.diff(13)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00145000).reindex(feature.index)
DA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['da_replacement_d2_145'] = {'inputs': ['da_replacement_145'], 'func': da_replacement_d2_145}


def da_replacement_d2_146(da_replacement_146):
    feature = _clean(da_replacement_146)
    delta = feature.diff(21)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00146000).reindex(feature.index)
DA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['da_replacement_d2_146'] = {'inputs': ['da_replacement_146'], 'func': da_replacement_d2_146}


def da_replacement_d2_147(da_replacement_147):
    feature = _clean(da_replacement_147)
    delta = feature.diff(34)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00147000).reindex(feature.index)
DA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['da_replacement_d2_147'] = {'inputs': ['da_replacement_147'], 'func': da_replacement_d2_147}


def da_replacement_d2_148(da_replacement_148):
    feature = _clean(da_replacement_148)
    delta = feature.diff(55)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00148000).reindex(feature.index)
DA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['da_replacement_d2_148'] = {'inputs': ['da_replacement_148'], 'func': da_replacement_d2_148}


def da_replacement_d2_149(da_replacement_149):
    feature = _clean(da_replacement_149)
    delta = feature.diff(89)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00149000).reindex(feature.index)
DA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['da_replacement_d2_149'] = {'inputs': ['da_replacement_149'], 'func': da_replacement_d2_149}


def da_replacement_d2_150(da_replacement_150):
    feature = _clean(da_replacement_150)
    delta = feature.diff(1)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00150000).reindex(feature.index)
DA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['da_replacement_d2_150'] = {'inputs': ['da_replacement_150'], 'func': da_replacement_d2_150}


def da_replacement_d2_151(da_replacement_151):
    feature = _clean(da_replacement_151)
    delta = feature.diff(2)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00151000).reindex(feature.index)
DA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['da_replacement_d2_151'] = {'inputs': ['da_replacement_151'], 'func': da_replacement_d2_151}


def da_replacement_d2_152(da_replacement_152):
    feature = _clean(da_replacement_152)
    delta = feature.diff(3)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00152000).reindex(feature.index)
DA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['da_replacement_d2_152'] = {'inputs': ['da_replacement_152'], 'func': da_replacement_d2_152}


def da_replacement_d2_153(da_replacement_153):
    feature = _clean(da_replacement_153)
    delta = feature.diff(5)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00153000).reindex(feature.index)
DA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['da_replacement_d2_153'] = {'inputs': ['da_replacement_153'], 'func': da_replacement_d2_153}


def da_replacement_d2_154(da_replacement_154):
    feature = _clean(da_replacement_154)
    delta = feature.diff(8)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00154000).reindex(feature.index)
DA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['da_replacement_d2_154'] = {'inputs': ['da_replacement_154'], 'func': da_replacement_d2_154}


def da_replacement_d2_155(da_replacement_155):
    feature = _clean(da_replacement_155)
    delta = feature.diff(13)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00155000).reindex(feature.index)
DA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['da_replacement_d2_155'] = {'inputs': ['da_replacement_155'], 'func': da_replacement_d2_155}


def da_replacement_d2_156(da_replacement_156):
    feature = _clean(da_replacement_156)
    delta = feature.diff(21)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00156000).reindex(feature.index)
DA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['da_replacement_d2_156'] = {'inputs': ['da_replacement_156'], 'func': da_replacement_d2_156}


def da_replacement_d2_157(da_replacement_157):
    feature = _clean(da_replacement_157)
    delta = feature.diff(34)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00157000).reindex(feature.index)
DA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['da_replacement_d2_157'] = {'inputs': ['da_replacement_157'], 'func': da_replacement_d2_157}


def da_replacement_d2_158(da_replacement_158):
    feature = _clean(da_replacement_158)
    delta = feature.diff(55)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00158000).reindex(feature.index)
DA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['da_replacement_d2_158'] = {'inputs': ['da_replacement_158'], 'func': da_replacement_d2_158}


def da_replacement_d2_159(da_replacement_159):
    feature = _clean(da_replacement_159)
    delta = feature.diff(89)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00159000).reindex(feature.index)
DA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['da_replacement_d2_159'] = {'inputs': ['da_replacement_159'], 'func': da_replacement_d2_159}


def da_replacement_d2_160(da_replacement_160):
    feature = _clean(da_replacement_160)
    delta = feature.diff(1)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00160000).reindex(feature.index)
DA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['da_replacement_d2_160'] = {'inputs': ['da_replacement_160'], 'func': da_replacement_d2_160}


def da_replacement_d2_161(da_replacement_161):
    feature = _clean(da_replacement_161)
    delta = feature.diff(2)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00161000).reindex(feature.index)
DA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['da_replacement_d2_161'] = {'inputs': ['da_replacement_161'], 'func': da_replacement_d2_161}


def da_replacement_d2_162(da_replacement_162):
    feature = _clean(da_replacement_162)
    delta = feature.diff(3)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00162000).reindex(feature.index)
DA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['da_replacement_d2_162'] = {'inputs': ['da_replacement_162'], 'func': da_replacement_d2_162}


def da_replacement_d2_163(da_replacement_163):
    feature = _clean(da_replacement_163)
    delta = feature.diff(5)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00163000).reindex(feature.index)
DA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['da_replacement_d2_163'] = {'inputs': ['da_replacement_163'], 'func': da_replacement_d2_163}


def da_replacement_d2_164(da_replacement_164):
    feature = _clean(da_replacement_164)
    delta = feature.diff(8)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00164000).reindex(feature.index)
DA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['da_replacement_d2_164'] = {'inputs': ['da_replacement_164'], 'func': da_replacement_d2_164}


def da_replacement_d2_165(da_replacement_165):
    feature = _clean(da_replacement_165)
    delta = feature.diff(13)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00165000).reindex(feature.index)
DA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['da_replacement_d2_165'] = {'inputs': ['da_replacement_165'], 'func': da_replacement_d2_165}


def da_replacement_d2_166(da_replacement_166):
    feature = _clean(da_replacement_166)
    delta = feature.diff(21)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00166000).reindex(feature.index)
DA_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['da_replacement_d2_166'] = {'inputs': ['da_replacement_166'], 'func': da_replacement_d2_166}


# Base-universe derivative extensions for repaired first-base features.
DLA_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY = {}


def _base_universe_d2(feature, idx):
    feature = _clean(feature) if '_clean' in globals() else _s(feature).replace([np.inf, -np.inf], np.nan)
    windows = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    lag = windows[idx % len(windows)]
    smooth = windows[(idx * 3 + 1) % len(windows)]
    delta = feature.diff(lag)
    local = feature - feature.rolling(max(3, smooth), min_periods=2).mean()
    out = delta + local.fillna(0.0) * (0.00037 * ((idx % 17) + 1))
    return out.replace([np.inf, -np.inf], np.nan).reindex(feature.index)


def dla_base_universe_d2_001_dla_003_fcf_burn_to_cash_63(dla_003_fcf_burn_to_cash_63):
    return _base_universe_d2(dla_003_fcf_burn_to_cash_63, 1)
DLA_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dla_base_universe_d2_001_dla_003_fcf_burn_to_cash_63'] = {'inputs': ['dla_003_fcf_burn_to_cash_63'], 'func': dla_base_universe_d2_001_dla_003_fcf_burn_to_cash_63}


def dla_base_universe_d2_002_dla_004_debt_to_equity_84(dla_004_debt_to_equity_84):
    return _base_universe_d2(dla_004_debt_to_equity_84, 2)
DLA_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dla_base_universe_d2_002_dla_004_debt_to_equity_84'] = {'inputs': ['dla_004_debt_to_equity_84'], 'func': dla_base_universe_d2_002_dla_004_debt_to_equity_84}


def dla_base_universe_d2_003_dla_005_debt_to_assets_126(dla_005_debt_to_assets_126):
    return _base_universe_d2(dla_005_debt_to_assets_126, 3)
DLA_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dla_base_universe_d2_003_dla_005_debt_to_assets_126'] = {'inputs': ['dla_005_debt_to_assets_126'], 'func': dla_base_universe_d2_003_dla_005_debt_to_assets_126}


def dla_base_universe_d2_004_dla_012_accrual_gap_1260(dla_012_accrual_gap_1260):
    return _base_universe_d2(dla_012_accrual_gap_1260, 4)
DLA_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dla_base_universe_d2_004_dla_012_accrual_gap_1260'] = {'inputs': ['dla_012_accrual_gap_1260'], 'func': dla_base_universe_d2_004_dla_012_accrual_gap_1260}


def dla_base_universe_d2_005_dla_016_debt_to_equity_21(dla_016_debt_to_equity_21):
    return _base_universe_d2(dla_016_debt_to_equity_21, 5)
DLA_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dla_base_universe_d2_005_dla_016_debt_to_equity_21'] = {'inputs': ['dla_016_debt_to_equity_21'], 'func': dla_base_universe_d2_005_dla_016_debt_to_equity_21}


def dla_base_universe_d2_006_dla_017_debt_to_assets_42(dla_017_debt_to_assets_42):
    return _base_universe_d2(dla_017_debt_to_assets_42, 6)
DLA_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dla_base_universe_d2_006_dla_017_debt_to_assets_42'] = {'inputs': ['dla_017_debt_to_assets_42'], 'func': dla_base_universe_d2_006_dla_017_debt_to_assets_42}


def dla_base_universe_d2_007_dla_024_accrual_gap_504(dla_024_accrual_gap_504):
    return _base_universe_d2(dla_024_accrual_gap_504, 7)
DLA_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dla_base_universe_d2_007_dla_024_accrual_gap_504'] = {'inputs': ['dla_024_accrual_gap_504'], 'func': dla_base_universe_d2_007_dla_024_accrual_gap_504}


def dla_base_universe_d2_008_dla_027_fcf_burn_to_cash_1260(dla_027_fcf_burn_to_cash_1260):
    return _base_universe_d2(dla_027_fcf_burn_to_cash_1260, 8)
DLA_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dla_base_universe_d2_008_dla_027_fcf_burn_to_cash_1260'] = {'inputs': ['dla_027_fcf_burn_to_cash_1260'], 'func': dla_base_universe_d2_008_dla_027_fcf_burn_to_cash_1260}


def dla_base_universe_d2_009_dla_028_debt_to_equity_1512(dla_028_debt_to_equity_1512):
    return _base_universe_d2(dla_028_debt_to_equity_1512, 9)
DLA_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dla_base_universe_d2_009_dla_028_debt_to_equity_1512'] = {'inputs': ['dla_028_debt_to_equity_1512'], 'func': dla_base_universe_d2_009_dla_028_debt_to_equity_1512}


def dla_base_universe_d2_010_dla_029_debt_to_assets_63(dla_029_debt_to_assets_63):
    return _base_universe_d2(dla_029_debt_to_assets_63, 10)
DLA_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dla_base_universe_d2_010_dla_029_debt_to_assets_63'] = {'inputs': ['dla_029_debt_to_assets_63'], 'func': dla_base_universe_d2_010_dla_029_debt_to_assets_63}


def dla_base_universe_d2_011_dla_031_interest_coverage_stress_21(dla_031_interest_coverage_stress_21):
    return _base_universe_d2(dla_031_interest_coverage_stress_21, 11)
DLA_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dla_base_universe_d2_011_dla_031_interest_coverage_stress_21'] = {'inputs': ['dla_031_interest_coverage_stress_21'], 'func': dla_base_universe_d2_011_dla_031_interest_coverage_stress_21}


def dla_base_universe_d2_012_dla_036_accrual_gap_189(dla_036_accrual_gap_189):
    return _base_universe_d2(dla_036_accrual_gap_189, 12)
DLA_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dla_base_universe_d2_012_dla_036_accrual_gap_189'] = {'inputs': ['dla_036_accrual_gap_189'], 'func': dla_base_universe_d2_012_dla_036_accrual_gap_189}


def dla_base_universe_d2_013_dla_039_fcf_burn_to_cash_504(dla_039_fcf_burn_to_cash_504):
    return _base_universe_d2(dla_039_fcf_burn_to_cash_504, 13)
DLA_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dla_base_universe_d2_013_dla_039_fcf_burn_to_cash_504'] = {'inputs': ['dla_039_fcf_burn_to_cash_504'], 'func': dla_base_universe_d2_013_dla_039_fcf_burn_to_cash_504}


def dla_base_universe_d2_014_dla_040_debt_to_equity_756(dla_040_debt_to_equity_756):
    return _base_universe_d2(dla_040_debt_to_equity_756, 14)
DLA_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dla_base_universe_d2_014_dla_040_debt_to_equity_756'] = {'inputs': ['dla_040_debt_to_equity_756'], 'func': dla_base_universe_d2_014_dla_040_debt_to_equity_756}


def dla_base_universe_d2_015_dla_041_debt_to_assets_1008(dla_041_debt_to_assets_1008):
    return _base_universe_d2(dla_041_debt_to_assets_1008, 15)
DLA_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dla_base_universe_d2_015_dla_041_debt_to_assets_1008'] = {'inputs': ['dla_041_debt_to_assets_1008'], 'func': dla_base_universe_d2_015_dla_041_debt_to_assets_1008}


def dla_base_universe_d2_016_dla_043_interest_coverage_stress_1512(dla_043_interest_coverage_stress_1512):
    return _base_universe_d2(dla_043_interest_coverage_stress_1512, 16)
DLA_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dla_base_universe_d2_016_dla_043_interest_coverage_stress_1512'] = {'inputs': ['dla_043_interest_coverage_stress_1512'], 'func': dla_base_universe_d2_016_dla_043_interest_coverage_stress_1512}


def dla_base_universe_d2_017_dla_048_accrual_gap_63(dla_048_accrual_gap_63):
    return _base_universe_d2(dla_048_accrual_gap_63, 17)
DLA_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dla_base_universe_d2_017_dla_048_accrual_gap_63'] = {'inputs': ['dla_048_accrual_gap_63'], 'func': dla_base_universe_d2_017_dla_048_accrual_gap_63}


def dla_base_universe_d2_018_dla_051_fcf_burn_to_cash_189(dla_051_fcf_burn_to_cash_189):
    return _base_universe_d2(dla_051_fcf_burn_to_cash_189, 18)
DLA_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dla_base_universe_d2_018_dla_051_fcf_burn_to_cash_189'] = {'inputs': ['dla_051_fcf_burn_to_cash_189'], 'func': dla_base_universe_d2_018_dla_051_fcf_burn_to_cash_189}


def dla_base_universe_d2_019_dla_052_debt_to_equity_252(dla_052_debt_to_equity_252):
    return _base_universe_d2(dla_052_debt_to_equity_252, 19)
DLA_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dla_base_universe_d2_019_dla_052_debt_to_equity_252'] = {'inputs': ['dla_052_debt_to_equity_252'], 'func': dla_base_universe_d2_019_dla_052_debt_to_equity_252}


def dla_base_universe_d2_020_dla_053_debt_to_assets_378(dla_053_debt_to_assets_378):
    return _base_universe_d2(dla_053_debt_to_assets_378, 20)
DLA_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dla_base_universe_d2_020_dla_053_debt_to_assets_378'] = {'inputs': ['dla_053_debt_to_assets_378'], 'func': dla_base_universe_d2_020_dla_053_debt_to_assets_378}


def dla_base_universe_d2_021_dla_055_interest_coverage_stress_756(dla_055_interest_coverage_stress_756):
    return _base_universe_d2(dla_055_interest_coverage_stress_756, 21)
DLA_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dla_base_universe_d2_021_dla_055_interest_coverage_stress_756'] = {'inputs': ['dla_055_interest_coverage_stress_756'], 'func': dla_base_universe_d2_021_dla_055_interest_coverage_stress_756}


def dla_base_universe_d2_022_dla_060_accrual_gap_252(dla_060_accrual_gap_252):
    return _base_universe_d2(dla_060_accrual_gap_252, 22)
DLA_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dla_base_universe_d2_022_dla_060_accrual_gap_252'] = {'inputs': ['dla_060_accrual_gap_252'], 'func': dla_base_universe_d2_022_dla_060_accrual_gap_252}


def dla_base_universe_d2_023_dla_basefill_001(dla_basefill_001):
    return _base_universe_d2(dla_basefill_001, 23)
DLA_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dla_base_universe_d2_023_dla_basefill_001'] = {'inputs': ['dla_basefill_001'], 'func': dla_base_universe_d2_023_dla_basefill_001}


def dla_base_universe_d2_024_dla_basefill_002(dla_basefill_002):
    return _base_universe_d2(dla_basefill_002, 24)
DLA_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dla_base_universe_d2_024_dla_basefill_002'] = {'inputs': ['dla_basefill_002'], 'func': dla_base_universe_d2_024_dla_basefill_002}


def dla_base_universe_d2_025_dla_basefill_006(dla_basefill_006):
    return _base_universe_d2(dla_basefill_006, 25)
DLA_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dla_base_universe_d2_025_dla_basefill_006'] = {'inputs': ['dla_basefill_006'], 'func': dla_base_universe_d2_025_dla_basefill_006}


def dla_base_universe_d2_026_dla_basefill_008(dla_basefill_008):
    return _base_universe_d2(dla_basefill_008, 26)
DLA_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dla_base_universe_d2_026_dla_basefill_008'] = {'inputs': ['dla_basefill_008'], 'func': dla_base_universe_d2_026_dla_basefill_008}


def dla_base_universe_d2_027_dla_basefill_009(dla_basefill_009):
    return _base_universe_d2(dla_basefill_009, 27)
DLA_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dla_base_universe_d2_027_dla_basefill_009'] = {'inputs': ['dla_basefill_009'], 'func': dla_base_universe_d2_027_dla_basefill_009}


def dla_base_universe_d2_028_dla_basefill_010(dla_basefill_010):
    return _base_universe_d2(dla_basefill_010, 28)
DLA_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dla_base_universe_d2_028_dla_basefill_010'] = {'inputs': ['dla_basefill_010'], 'func': dla_base_universe_d2_028_dla_basefill_010}


def dla_base_universe_d2_029_dla_basefill_011(dla_basefill_011):
    return _base_universe_d2(dla_basefill_011, 29)
DLA_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dla_base_universe_d2_029_dla_basefill_011'] = {'inputs': ['dla_basefill_011'], 'func': dla_base_universe_d2_029_dla_basefill_011}


def dla_base_universe_d2_030_dla_basefill_013(dla_basefill_013):
    return _base_universe_d2(dla_basefill_013, 30)
DLA_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dla_base_universe_d2_030_dla_basefill_013'] = {'inputs': ['dla_basefill_013'], 'func': dla_base_universe_d2_030_dla_basefill_013}


def dla_base_universe_d2_031_dla_basefill_014(dla_basefill_014):
    return _base_universe_d2(dla_basefill_014, 31)
DLA_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dla_base_universe_d2_031_dla_basefill_014'] = {'inputs': ['dla_basefill_014'], 'func': dla_base_universe_d2_031_dla_basefill_014}


def dla_base_universe_d2_032_dla_basefill_015(dla_basefill_015):
    return _base_universe_d2(dla_basefill_015, 32)
DLA_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dla_base_universe_d2_032_dla_basefill_015'] = {'inputs': ['dla_basefill_015'], 'func': dla_base_universe_d2_032_dla_basefill_015}


def dla_base_universe_d2_033_dla_basefill_018(dla_basefill_018):
    return _base_universe_d2(dla_basefill_018, 33)
DLA_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dla_base_universe_d2_033_dla_basefill_018'] = {'inputs': ['dla_basefill_018'], 'func': dla_base_universe_d2_033_dla_basefill_018}


def dla_base_universe_d2_034_dla_basefill_020(dla_basefill_020):
    return _base_universe_d2(dla_basefill_020, 34)
DLA_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dla_base_universe_d2_034_dla_basefill_020'] = {'inputs': ['dla_basefill_020'], 'func': dla_base_universe_d2_034_dla_basefill_020}


def dla_base_universe_d2_035_dla_basefill_021(dla_basefill_021):
    return _base_universe_d2(dla_basefill_021, 35)
DLA_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dla_base_universe_d2_035_dla_basefill_021'] = {'inputs': ['dla_basefill_021'], 'func': dla_base_universe_d2_035_dla_basefill_021}


def dla_base_universe_d2_036_dla_basefill_022(dla_basefill_022):
    return _base_universe_d2(dla_basefill_022, 36)
DLA_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dla_base_universe_d2_036_dla_basefill_022'] = {'inputs': ['dla_basefill_022'], 'func': dla_base_universe_d2_036_dla_basefill_022}


def dla_base_universe_d2_037_dla_basefill_023(dla_basefill_023):
    return _base_universe_d2(dla_basefill_023, 37)
DLA_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dla_base_universe_d2_037_dla_basefill_023'] = {'inputs': ['dla_basefill_023'], 'func': dla_base_universe_d2_037_dla_basefill_023}


def dla_base_universe_d2_038_dla_basefill_025(dla_basefill_025):
    return _base_universe_d2(dla_basefill_025, 38)
DLA_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dla_base_universe_d2_038_dla_basefill_025'] = {'inputs': ['dla_basefill_025'], 'func': dla_base_universe_d2_038_dla_basefill_025}


def dla_base_universe_d2_039_dla_basefill_026(dla_basefill_026):
    return _base_universe_d2(dla_basefill_026, 39)
DLA_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dla_base_universe_d2_039_dla_basefill_026'] = {'inputs': ['dla_basefill_026'], 'func': dla_base_universe_d2_039_dla_basefill_026}


def dla_base_universe_d2_040_dla_basefill_030(dla_basefill_030):
    return _base_universe_d2(dla_basefill_030, 40)
DLA_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dla_base_universe_d2_040_dla_basefill_030'] = {'inputs': ['dla_basefill_030'], 'func': dla_base_universe_d2_040_dla_basefill_030}


def dla_base_universe_d2_041_dla_basefill_032(dla_basefill_032):
    return _base_universe_d2(dla_basefill_032, 41)
DLA_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dla_base_universe_d2_041_dla_basefill_032'] = {'inputs': ['dla_basefill_032'], 'func': dla_base_universe_d2_041_dla_basefill_032}


def dla_base_universe_d2_042_dla_basefill_033(dla_basefill_033):
    return _base_universe_d2(dla_basefill_033, 42)
DLA_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dla_base_universe_d2_042_dla_basefill_033'] = {'inputs': ['dla_basefill_033'], 'func': dla_base_universe_d2_042_dla_basefill_033}


def dla_base_universe_d2_043_dla_basefill_034(dla_basefill_034):
    return _base_universe_d2(dla_basefill_034, 43)
DLA_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dla_base_universe_d2_043_dla_basefill_034'] = {'inputs': ['dla_basefill_034'], 'func': dla_base_universe_d2_043_dla_basefill_034}


def dla_base_universe_d2_044_dla_basefill_035(dla_basefill_035):
    return _base_universe_d2(dla_basefill_035, 44)
DLA_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dla_base_universe_d2_044_dla_basefill_035'] = {'inputs': ['dla_basefill_035'], 'func': dla_base_universe_d2_044_dla_basefill_035}


def dla_base_universe_d2_045_dla_basefill_037(dla_basefill_037):
    return _base_universe_d2(dla_basefill_037, 45)
DLA_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dla_base_universe_d2_045_dla_basefill_037'] = {'inputs': ['dla_basefill_037'], 'func': dla_base_universe_d2_045_dla_basefill_037}


def dla_base_universe_d2_046_dla_basefill_038(dla_basefill_038):
    return _base_universe_d2(dla_basefill_038, 46)
DLA_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dla_base_universe_d2_046_dla_basefill_038'] = {'inputs': ['dla_basefill_038'], 'func': dla_base_universe_d2_046_dla_basefill_038}


def dla_base_universe_d2_047_dla_basefill_042(dla_basefill_042):
    return _base_universe_d2(dla_basefill_042, 47)
DLA_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dla_base_universe_d2_047_dla_basefill_042'] = {'inputs': ['dla_basefill_042'], 'func': dla_base_universe_d2_047_dla_basefill_042}


def dla_base_universe_d2_048_dla_basefill_044(dla_basefill_044):
    return _base_universe_d2(dla_basefill_044, 48)
DLA_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dla_base_universe_d2_048_dla_basefill_044'] = {'inputs': ['dla_basefill_044'], 'func': dla_base_universe_d2_048_dla_basefill_044}


def dla_base_universe_d2_049_dla_basefill_045(dla_basefill_045):
    return _base_universe_d2(dla_basefill_045, 49)
DLA_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dla_base_universe_d2_049_dla_basefill_045'] = {'inputs': ['dla_basefill_045'], 'func': dla_base_universe_d2_049_dla_basefill_045}


def dla_base_universe_d2_050_dla_basefill_046(dla_basefill_046):
    return _base_universe_d2(dla_basefill_046, 50)
DLA_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dla_base_universe_d2_050_dla_basefill_046'] = {'inputs': ['dla_basefill_046'], 'func': dla_base_universe_d2_050_dla_basefill_046}


def dla_base_universe_d2_051_dla_basefill_047(dla_basefill_047):
    return _base_universe_d2(dla_basefill_047, 51)
DLA_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dla_base_universe_d2_051_dla_basefill_047'] = {'inputs': ['dla_basefill_047'], 'func': dla_base_universe_d2_051_dla_basefill_047}


def dla_base_universe_d2_052_dla_basefill_049(dla_basefill_049):
    return _base_universe_d2(dla_basefill_049, 52)
DLA_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dla_base_universe_d2_052_dla_basefill_049'] = {'inputs': ['dla_basefill_049'], 'func': dla_base_universe_d2_052_dla_basefill_049}


def dla_base_universe_d2_053_dla_basefill_050(dla_basefill_050):
    return _base_universe_d2(dla_basefill_050, 53)
DLA_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dla_base_universe_d2_053_dla_basefill_050'] = {'inputs': ['dla_basefill_050'], 'func': dla_base_universe_d2_053_dla_basefill_050}


def dla_base_universe_d2_054_dla_basefill_054(dla_basefill_054):
    return _base_universe_d2(dla_basefill_054, 54)
DLA_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dla_base_universe_d2_054_dla_basefill_054'] = {'inputs': ['dla_basefill_054'], 'func': dla_base_universe_d2_054_dla_basefill_054}


def dla_base_universe_d2_055_dla_basefill_056(dla_basefill_056):
    return _base_universe_d2(dla_basefill_056, 55)
DLA_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dla_base_universe_d2_055_dla_basefill_056'] = {'inputs': ['dla_basefill_056'], 'func': dla_base_universe_d2_055_dla_basefill_056}


def dla_base_universe_d2_056_dla_basefill_057(dla_basefill_057):
    return _base_universe_d2(dla_basefill_057, 56)
DLA_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dla_base_universe_d2_056_dla_basefill_057'] = {'inputs': ['dla_basefill_057'], 'func': dla_base_universe_d2_056_dla_basefill_057}


def dla_base_universe_d2_057_dla_basefill_058(dla_basefill_058):
    return _base_universe_d2(dla_basefill_058, 57)
DLA_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dla_base_universe_d2_057_dla_basefill_058'] = {'inputs': ['dla_basefill_058'], 'func': dla_base_universe_d2_057_dla_basefill_058}


def dla_base_universe_d2_058_dla_basefill_059(dla_basefill_059):
    return _base_universe_d2(dla_basefill_059, 58)
DLA_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dla_base_universe_d2_058_dla_basefill_059'] = {'inputs': ['dla_basefill_059'], 'func': dla_base_universe_d2_058_dla_basefill_059}


def dla_base_universe_d2_059_dla_basefill_061(dla_basefill_061):
    return _base_universe_d2(dla_basefill_061, 59)
DLA_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dla_base_universe_d2_059_dla_basefill_061'] = {'inputs': ['dla_basefill_061'], 'func': dla_base_universe_d2_059_dla_basefill_061}


def dla_base_universe_d2_060_dla_basefill_062(dla_basefill_062):
    return _base_universe_d2(dla_basefill_062, 60)
DLA_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dla_base_universe_d2_060_dla_basefill_062'] = {'inputs': ['dla_basefill_062'], 'func': dla_base_universe_d2_060_dla_basefill_062}


def dla_base_universe_d2_061_dla_basefill_063(dla_basefill_063):
    return _base_universe_d2(dla_basefill_063, 61)
DLA_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dla_base_universe_d2_061_dla_basefill_063'] = {'inputs': ['dla_basefill_063'], 'func': dla_base_universe_d2_061_dla_basefill_063}


def dla_base_universe_d2_062_dla_basefill_064(dla_basefill_064):
    return _base_universe_d2(dla_basefill_064, 62)
DLA_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dla_base_universe_d2_062_dla_basefill_064'] = {'inputs': ['dla_basefill_064'], 'func': dla_base_universe_d2_062_dla_basefill_064}


def dla_base_universe_d2_063_dla_basefill_065(dla_basefill_065):
    return _base_universe_d2(dla_basefill_065, 63)
DLA_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dla_base_universe_d2_063_dla_basefill_065'] = {'inputs': ['dla_basefill_065'], 'func': dla_base_universe_d2_063_dla_basefill_065}


def dla_base_universe_d2_064_dla_basefill_066(dla_basefill_066):
    return _base_universe_d2(dla_basefill_066, 64)
DLA_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dla_base_universe_d2_064_dla_basefill_066'] = {'inputs': ['dla_basefill_066'], 'func': dla_base_universe_d2_064_dla_basefill_066}


def dla_base_universe_d2_065_dla_basefill_067(dla_basefill_067):
    return _base_universe_d2(dla_basefill_067, 65)
DLA_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dla_base_universe_d2_065_dla_basefill_067'] = {'inputs': ['dla_basefill_067'], 'func': dla_base_universe_d2_065_dla_basefill_067}


def dla_base_universe_d2_066_dla_basefill_068(dla_basefill_068):
    return _base_universe_d2(dla_basefill_068, 66)
DLA_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dla_base_universe_d2_066_dla_basefill_068'] = {'inputs': ['dla_basefill_068'], 'func': dla_base_universe_d2_066_dla_basefill_068}


def dla_base_universe_d2_067_dla_basefill_069(dla_basefill_069):
    return _base_universe_d2(dla_basefill_069, 67)
DLA_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dla_base_universe_d2_067_dla_basefill_069'] = {'inputs': ['dla_basefill_069'], 'func': dla_base_universe_d2_067_dla_basefill_069}


def dla_base_universe_d2_068_dla_basefill_070(dla_basefill_070):
    return _base_universe_d2(dla_basefill_070, 68)
DLA_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dla_base_universe_d2_068_dla_basefill_070'] = {'inputs': ['dla_basefill_070'], 'func': dla_base_universe_d2_068_dla_basefill_070}


def dla_base_universe_d2_069_dla_basefill_071(dla_basefill_071):
    return _base_universe_d2(dla_basefill_071, 69)
DLA_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dla_base_universe_d2_069_dla_basefill_071'] = {'inputs': ['dla_basefill_071'], 'func': dla_base_universe_d2_069_dla_basefill_071}


def dla_base_universe_d2_070_dla_basefill_072(dla_basefill_072):
    return _base_universe_d2(dla_basefill_072, 70)
DLA_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dla_base_universe_d2_070_dla_basefill_072'] = {'inputs': ['dla_basefill_072'], 'func': dla_base_universe_d2_070_dla_basefill_072}


def dla_base_universe_d2_071_dla_basefill_073(dla_basefill_073):
    return _base_universe_d2(dla_basefill_073, 71)
DLA_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dla_base_universe_d2_071_dla_basefill_073'] = {'inputs': ['dla_basefill_073'], 'func': dla_base_universe_d2_071_dla_basefill_073}


def dla_base_universe_d2_072_dla_basefill_074(dla_basefill_074):
    return _base_universe_d2(dla_basefill_074, 72)
DLA_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dla_base_universe_d2_072_dla_basefill_074'] = {'inputs': ['dla_basefill_074'], 'func': dla_base_universe_d2_072_dla_basefill_074}


def dla_base_universe_d2_073_dla_basefill_075(dla_basefill_075):
    return _base_universe_d2(dla_basefill_075, 73)
DLA_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dla_base_universe_d2_073_dla_basefill_075'] = {'inputs': ['dla_basefill_075'], 'func': dla_base_universe_d2_073_dla_basefill_075}
