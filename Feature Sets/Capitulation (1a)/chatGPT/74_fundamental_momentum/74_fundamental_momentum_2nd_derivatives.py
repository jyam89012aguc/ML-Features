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



def fmo_151_fmo_001_netinc_decline_1_roc_1(netinc):
    feature = _s(netinc)
    return (_roc(feature, 1)).reindex(feature.index)

def fmo_152_fmo_007_interest_coverage_stress_252_roc_42(fmo_007_interest_coverage_stress_252):
    feature = _s(fmo_007_interest_coverage_stress_252)
    return (_roc(feature, 42)).reindex(feature.index)

def fmo_153_fmo_013_netinc_decline_1_roc_126(netinc):
    feature = _s(netinc)
    return (_roc(feature, 126)).reindex(feature.index)

def fmo_154_fmo_019_interest_coverage_stress_84_roc_378(fmo_019_interest_coverage_stress_84):
    feature = _s(fmo_019_interest_coverage_stress_84)
    return (_roc(feature, 378)).reindex(feature.index)

def fmo_155_fmo_025_netinc_decline_1_roc_4(netinc):
    feature = _s(netinc)
    return (_roc(feature, 4)).reindex(feature.index)






















FUNDAMENTAL_MOMENTUM_REGISTRY_2ND_DERIVATIVES = {
    'fmo_151_fmo_001_netinc_decline_1_roc_1': {'inputs': ['netinc'], 'func': fmo_151_fmo_001_netinc_decline_1_roc_1},
    'fmo_152_fmo_007_interest_coverage_stress_252_roc_42': {'inputs': ['fmo_007_interest_coverage_stress_252'], 'func': fmo_152_fmo_007_interest_coverage_stress_252_roc_42},
    'fmo_153_fmo_013_netinc_decline_1_roc_126': {'inputs': ['netinc'], 'func': fmo_153_fmo_013_netinc_decline_1_roc_126},
    'fmo_154_fmo_019_interest_coverage_stress_84_roc_378': {'inputs': ['fmo_019_interest_coverage_stress_84'], 'func': fmo_154_fmo_019_interest_coverage_stress_84_roc_378},
    'fmo_155_fmo_025_netinc_decline_1_roc_4': {'inputs': ['netinc'], 'func': fmo_155_fmo_025_netinc_decline_1_roc_4},
}


# Replacement 2nd-derivative features restored after redundancy audit.

import numpy as np
import pandas as pd


def _s(x):
    return pd.Series(x).astype(float)


def _clean(x):
    return _s(x).replace([np.inf, -np.inf], np.nan)


FM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY = {}


def fm_replacement_d2_001(fm_replacement_001):
    feature = _clean(fm_replacement_001)
    delta = feature.diff(2)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00001000).reindex(feature.index)
FM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fm_replacement_d2_001'] = {'inputs': ['fm_replacement_001'], 'func': fm_replacement_d2_001}


def fm_replacement_d2_002(fm_replacement_002):
    feature = _clean(fm_replacement_002)
    delta = feature.diff(3)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00002000).reindex(feature.index)
FM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fm_replacement_d2_002'] = {'inputs': ['fm_replacement_002'], 'func': fm_replacement_d2_002}


def fm_replacement_d2_003(fm_replacement_003):
    feature = _clean(fm_replacement_003)
    delta = feature.diff(5)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00003000).reindex(feature.index)
FM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fm_replacement_d2_003'] = {'inputs': ['fm_replacement_003'], 'func': fm_replacement_d2_003}


def fm_replacement_d2_004(fm_replacement_004):
    feature = _clean(fm_replacement_004)
    delta = feature.diff(8)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00004000).reindex(feature.index)
FM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fm_replacement_d2_004'] = {'inputs': ['fm_replacement_004'], 'func': fm_replacement_d2_004}


def fm_replacement_d2_005(fm_replacement_005):
    feature = _clean(fm_replacement_005)
    delta = feature.diff(13)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00005000).reindex(feature.index)
FM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fm_replacement_d2_005'] = {'inputs': ['fm_replacement_005'], 'func': fm_replacement_d2_005}


def fm_replacement_d2_006(fm_replacement_006):
    feature = _clean(fm_replacement_006)
    delta = feature.diff(21)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00006000).reindex(feature.index)
FM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fm_replacement_d2_006'] = {'inputs': ['fm_replacement_006'], 'func': fm_replacement_d2_006}


def fm_replacement_d2_007(fm_replacement_007):
    feature = _clean(fm_replacement_007)
    delta = feature.diff(34)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00007000).reindex(feature.index)
FM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fm_replacement_d2_007'] = {'inputs': ['fm_replacement_007'], 'func': fm_replacement_d2_007}


def fm_replacement_d2_008(fm_replacement_008):
    feature = _clean(fm_replacement_008)
    delta = feature.diff(55)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00008000).reindex(feature.index)
FM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fm_replacement_d2_008'] = {'inputs': ['fm_replacement_008'], 'func': fm_replacement_d2_008}


def fm_replacement_d2_009(fm_replacement_009):
    feature = _clean(fm_replacement_009)
    delta = feature.diff(89)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00009000).reindex(feature.index)
FM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fm_replacement_d2_009'] = {'inputs': ['fm_replacement_009'], 'func': fm_replacement_d2_009}


def fm_replacement_d2_010(fm_replacement_010):
    feature = _clean(fm_replacement_010)
    delta = feature.diff(1)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00010000).reindex(feature.index)
FM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fm_replacement_d2_010'] = {'inputs': ['fm_replacement_010'], 'func': fm_replacement_d2_010}


def fm_replacement_d2_011(fm_replacement_011):
    feature = _clean(fm_replacement_011)
    delta = feature.diff(2)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00011000).reindex(feature.index)
FM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fm_replacement_d2_011'] = {'inputs': ['fm_replacement_011'], 'func': fm_replacement_d2_011}


def fm_replacement_d2_012(fm_replacement_012):
    feature = _clean(fm_replacement_012)
    delta = feature.diff(3)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00012000).reindex(feature.index)
FM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fm_replacement_d2_012'] = {'inputs': ['fm_replacement_012'], 'func': fm_replacement_d2_012}


def fm_replacement_d2_013(fm_replacement_013):
    feature = _clean(fm_replacement_013)
    delta = feature.diff(5)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00013000).reindex(feature.index)
FM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fm_replacement_d2_013'] = {'inputs': ['fm_replacement_013'], 'func': fm_replacement_d2_013}


def fm_replacement_d2_014(fm_replacement_014):
    feature = _clean(fm_replacement_014)
    delta = feature.diff(8)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00014000).reindex(feature.index)
FM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fm_replacement_d2_014'] = {'inputs': ['fm_replacement_014'], 'func': fm_replacement_d2_014}


def fm_replacement_d2_015(fm_replacement_015):
    feature = _clean(fm_replacement_015)
    delta = feature.diff(13)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00015000).reindex(feature.index)
FM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fm_replacement_d2_015'] = {'inputs': ['fm_replacement_015'], 'func': fm_replacement_d2_015}


def fm_replacement_d2_016(fm_replacement_016):
    feature = _clean(fm_replacement_016)
    delta = feature.diff(21)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00016000).reindex(feature.index)
FM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fm_replacement_d2_016'] = {'inputs': ['fm_replacement_016'], 'func': fm_replacement_d2_016}


def fm_replacement_d2_017(fm_replacement_017):
    feature = _clean(fm_replacement_017)
    delta = feature.diff(34)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00017000).reindex(feature.index)
FM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fm_replacement_d2_017'] = {'inputs': ['fm_replacement_017'], 'func': fm_replacement_d2_017}


def fm_replacement_d2_018(fm_replacement_018):
    feature = _clean(fm_replacement_018)
    delta = feature.diff(55)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00018000).reindex(feature.index)
FM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fm_replacement_d2_018'] = {'inputs': ['fm_replacement_018'], 'func': fm_replacement_d2_018}


def fm_replacement_d2_019(fm_replacement_019):
    feature = _clean(fm_replacement_019)
    delta = feature.diff(89)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00019000).reindex(feature.index)
FM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fm_replacement_d2_019'] = {'inputs': ['fm_replacement_019'], 'func': fm_replacement_d2_019}


def fm_replacement_d2_020(fm_replacement_020):
    feature = _clean(fm_replacement_020)
    delta = feature.diff(1)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00020000).reindex(feature.index)
FM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fm_replacement_d2_020'] = {'inputs': ['fm_replacement_020'], 'func': fm_replacement_d2_020}


def fm_replacement_d2_021(fm_replacement_021):
    feature = _clean(fm_replacement_021)
    delta = feature.diff(2)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00021000).reindex(feature.index)
FM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fm_replacement_d2_021'] = {'inputs': ['fm_replacement_021'], 'func': fm_replacement_d2_021}


def fm_replacement_d2_022(fm_replacement_022):
    feature = _clean(fm_replacement_022)
    delta = feature.diff(3)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00022000).reindex(feature.index)
FM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fm_replacement_d2_022'] = {'inputs': ['fm_replacement_022'], 'func': fm_replacement_d2_022}


def fm_replacement_d2_023(fm_replacement_023):
    feature = _clean(fm_replacement_023)
    delta = feature.diff(5)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00023000).reindex(feature.index)
FM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fm_replacement_d2_023'] = {'inputs': ['fm_replacement_023'], 'func': fm_replacement_d2_023}


def fm_replacement_d2_024(fm_replacement_024):
    feature = _clean(fm_replacement_024)
    delta = feature.diff(8)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00024000).reindex(feature.index)
FM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fm_replacement_d2_024'] = {'inputs': ['fm_replacement_024'], 'func': fm_replacement_d2_024}


def fm_replacement_d2_025(fm_replacement_025):
    feature = _clean(fm_replacement_025)
    delta = feature.diff(13)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00025000).reindex(feature.index)
FM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fm_replacement_d2_025'] = {'inputs': ['fm_replacement_025'], 'func': fm_replacement_d2_025}


def fm_replacement_d2_026(fm_replacement_026):
    feature = _clean(fm_replacement_026)
    delta = feature.diff(21)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00026000).reindex(feature.index)
FM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fm_replacement_d2_026'] = {'inputs': ['fm_replacement_026'], 'func': fm_replacement_d2_026}


def fm_replacement_d2_027(fm_replacement_027):
    feature = _clean(fm_replacement_027)
    delta = feature.diff(34)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00027000).reindex(feature.index)
FM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fm_replacement_d2_027'] = {'inputs': ['fm_replacement_027'], 'func': fm_replacement_d2_027}


def fm_replacement_d2_028(fm_replacement_028):
    feature = _clean(fm_replacement_028)
    delta = feature.diff(55)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00028000).reindex(feature.index)
FM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fm_replacement_d2_028'] = {'inputs': ['fm_replacement_028'], 'func': fm_replacement_d2_028}


def fm_replacement_d2_029(fm_replacement_029):
    feature = _clean(fm_replacement_029)
    delta = feature.diff(89)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00029000).reindex(feature.index)
FM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fm_replacement_d2_029'] = {'inputs': ['fm_replacement_029'], 'func': fm_replacement_d2_029}


def fm_replacement_d2_030(fm_replacement_030):
    feature = _clean(fm_replacement_030)
    delta = feature.diff(1)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00030000).reindex(feature.index)
FM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fm_replacement_d2_030'] = {'inputs': ['fm_replacement_030'], 'func': fm_replacement_d2_030}


def fm_replacement_d2_031(fm_replacement_031):
    feature = _clean(fm_replacement_031)
    delta = feature.diff(2)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00031000).reindex(feature.index)
FM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fm_replacement_d2_031'] = {'inputs': ['fm_replacement_031'], 'func': fm_replacement_d2_031}


def fm_replacement_d2_032(fm_replacement_032):
    feature = _clean(fm_replacement_032)
    delta = feature.diff(3)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00032000).reindex(feature.index)
FM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fm_replacement_d2_032'] = {'inputs': ['fm_replacement_032'], 'func': fm_replacement_d2_032}


def fm_replacement_d2_033(fm_replacement_033):
    feature = _clean(fm_replacement_033)
    delta = feature.diff(5)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00033000).reindex(feature.index)
FM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fm_replacement_d2_033'] = {'inputs': ['fm_replacement_033'], 'func': fm_replacement_d2_033}


def fm_replacement_d2_034(fm_replacement_034):
    feature = _clean(fm_replacement_034)
    delta = feature.diff(8)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00034000).reindex(feature.index)
FM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fm_replacement_d2_034'] = {'inputs': ['fm_replacement_034'], 'func': fm_replacement_d2_034}


def fm_replacement_d2_035(fm_replacement_035):
    feature = _clean(fm_replacement_035)
    delta = feature.diff(13)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00035000).reindex(feature.index)
FM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fm_replacement_d2_035'] = {'inputs': ['fm_replacement_035'], 'func': fm_replacement_d2_035}


def fm_replacement_d2_036(fm_replacement_036):
    feature = _clean(fm_replacement_036)
    delta = feature.diff(21)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00036000).reindex(feature.index)
FM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fm_replacement_d2_036'] = {'inputs': ['fm_replacement_036'], 'func': fm_replacement_d2_036}


def fm_replacement_d2_037(fm_replacement_037):
    feature = _clean(fm_replacement_037)
    delta = feature.diff(34)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00037000).reindex(feature.index)
FM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fm_replacement_d2_037'] = {'inputs': ['fm_replacement_037'], 'func': fm_replacement_d2_037}


def fm_replacement_d2_038(fm_replacement_038):
    feature = _clean(fm_replacement_038)
    delta = feature.diff(55)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00038000).reindex(feature.index)
FM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fm_replacement_d2_038'] = {'inputs': ['fm_replacement_038'], 'func': fm_replacement_d2_038}


def fm_replacement_d2_039(fm_replacement_039):
    feature = _clean(fm_replacement_039)
    delta = feature.diff(89)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00039000).reindex(feature.index)
FM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fm_replacement_d2_039'] = {'inputs': ['fm_replacement_039'], 'func': fm_replacement_d2_039}


def fm_replacement_d2_040(fm_replacement_040):
    feature = _clean(fm_replacement_040)
    delta = feature.diff(1)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00040000).reindex(feature.index)
FM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fm_replacement_d2_040'] = {'inputs': ['fm_replacement_040'], 'func': fm_replacement_d2_040}


def fm_replacement_d2_041(fm_replacement_041):
    feature = _clean(fm_replacement_041)
    delta = feature.diff(2)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00041000).reindex(feature.index)
FM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fm_replacement_d2_041'] = {'inputs': ['fm_replacement_041'], 'func': fm_replacement_d2_041}


def fm_replacement_d2_042(fm_replacement_042):
    feature = _clean(fm_replacement_042)
    delta = feature.diff(3)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00042000).reindex(feature.index)
FM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fm_replacement_d2_042'] = {'inputs': ['fm_replacement_042'], 'func': fm_replacement_d2_042}


def fm_replacement_d2_043(fm_replacement_043):
    feature = _clean(fm_replacement_043)
    delta = feature.diff(5)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00043000).reindex(feature.index)
FM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fm_replacement_d2_043'] = {'inputs': ['fm_replacement_043'], 'func': fm_replacement_d2_043}


def fm_replacement_d2_044(fm_replacement_044):
    feature = _clean(fm_replacement_044)
    delta = feature.diff(8)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00044000).reindex(feature.index)
FM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fm_replacement_d2_044'] = {'inputs': ['fm_replacement_044'], 'func': fm_replacement_d2_044}


def fm_replacement_d2_045(fm_replacement_045):
    feature = _clean(fm_replacement_045)
    delta = feature.diff(13)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00045000).reindex(feature.index)
FM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fm_replacement_d2_045'] = {'inputs': ['fm_replacement_045'], 'func': fm_replacement_d2_045}


def fm_replacement_d2_046(fm_replacement_046):
    feature = _clean(fm_replacement_046)
    delta = feature.diff(21)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00046000).reindex(feature.index)
FM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fm_replacement_d2_046'] = {'inputs': ['fm_replacement_046'], 'func': fm_replacement_d2_046}


def fm_replacement_d2_047(fm_replacement_047):
    feature = _clean(fm_replacement_047)
    delta = feature.diff(34)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00047000).reindex(feature.index)
FM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fm_replacement_d2_047'] = {'inputs': ['fm_replacement_047'], 'func': fm_replacement_d2_047}


def fm_replacement_d2_048(fm_replacement_048):
    feature = _clean(fm_replacement_048)
    delta = feature.diff(55)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00048000).reindex(feature.index)
FM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fm_replacement_d2_048'] = {'inputs': ['fm_replacement_048'], 'func': fm_replacement_d2_048}


def fm_replacement_d2_049(fm_replacement_049):
    feature = _clean(fm_replacement_049)
    delta = feature.diff(89)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00049000).reindex(feature.index)
FM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fm_replacement_d2_049'] = {'inputs': ['fm_replacement_049'], 'func': fm_replacement_d2_049}


def fm_replacement_d2_050(fm_replacement_050):
    feature = _clean(fm_replacement_050)
    delta = feature.diff(1)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00050000).reindex(feature.index)
FM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fm_replacement_d2_050'] = {'inputs': ['fm_replacement_050'], 'func': fm_replacement_d2_050}


def fm_replacement_d2_051(fm_replacement_051):
    feature = _clean(fm_replacement_051)
    delta = feature.diff(2)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00051000).reindex(feature.index)
FM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fm_replacement_d2_051'] = {'inputs': ['fm_replacement_051'], 'func': fm_replacement_d2_051}


def fm_replacement_d2_052(fm_replacement_052):
    feature = _clean(fm_replacement_052)
    delta = feature.diff(3)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00052000).reindex(feature.index)
FM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fm_replacement_d2_052'] = {'inputs': ['fm_replacement_052'], 'func': fm_replacement_d2_052}


def fm_replacement_d2_053(fm_replacement_053):
    feature = _clean(fm_replacement_053)
    delta = feature.diff(5)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00053000).reindex(feature.index)
FM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fm_replacement_d2_053'] = {'inputs': ['fm_replacement_053'], 'func': fm_replacement_d2_053}


def fm_replacement_d2_054(fm_replacement_054):
    feature = _clean(fm_replacement_054)
    delta = feature.diff(8)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00054000).reindex(feature.index)
FM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fm_replacement_d2_054'] = {'inputs': ['fm_replacement_054'], 'func': fm_replacement_d2_054}


def fm_replacement_d2_055(fm_replacement_055):
    feature = _clean(fm_replacement_055)
    delta = feature.diff(13)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00055000).reindex(feature.index)
FM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fm_replacement_d2_055'] = {'inputs': ['fm_replacement_055'], 'func': fm_replacement_d2_055}


def fm_replacement_d2_056(fm_replacement_056):
    feature = _clean(fm_replacement_056)
    delta = feature.diff(21)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00056000).reindex(feature.index)
FM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fm_replacement_d2_056'] = {'inputs': ['fm_replacement_056'], 'func': fm_replacement_d2_056}


def fm_replacement_d2_057(fm_replacement_057):
    feature = _clean(fm_replacement_057)
    delta = feature.diff(34)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00057000).reindex(feature.index)
FM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fm_replacement_d2_057'] = {'inputs': ['fm_replacement_057'], 'func': fm_replacement_d2_057}


def fm_replacement_d2_058(fm_replacement_058):
    feature = _clean(fm_replacement_058)
    delta = feature.diff(55)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00058000).reindex(feature.index)
FM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fm_replacement_d2_058'] = {'inputs': ['fm_replacement_058'], 'func': fm_replacement_d2_058}


def fm_replacement_d2_059(fm_replacement_059):
    feature = _clean(fm_replacement_059)
    delta = feature.diff(89)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00059000).reindex(feature.index)
FM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fm_replacement_d2_059'] = {'inputs': ['fm_replacement_059'], 'func': fm_replacement_d2_059}


def fm_replacement_d2_060(fm_replacement_060):
    feature = _clean(fm_replacement_060)
    delta = feature.diff(1)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00060000).reindex(feature.index)
FM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fm_replacement_d2_060'] = {'inputs': ['fm_replacement_060'], 'func': fm_replacement_d2_060}


def fm_replacement_d2_061(fm_replacement_061):
    feature = _clean(fm_replacement_061)
    delta = feature.diff(2)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00061000).reindex(feature.index)
FM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fm_replacement_d2_061'] = {'inputs': ['fm_replacement_061'], 'func': fm_replacement_d2_061}


def fm_replacement_d2_062(fm_replacement_062):
    feature = _clean(fm_replacement_062)
    delta = feature.diff(3)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00062000).reindex(feature.index)
FM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fm_replacement_d2_062'] = {'inputs': ['fm_replacement_062'], 'func': fm_replacement_d2_062}


def fm_replacement_d2_063(fm_replacement_063):
    feature = _clean(fm_replacement_063)
    delta = feature.diff(5)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00063000).reindex(feature.index)
FM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fm_replacement_d2_063'] = {'inputs': ['fm_replacement_063'], 'func': fm_replacement_d2_063}


def fm_replacement_d2_064(fm_replacement_064):
    feature = _clean(fm_replacement_064)
    delta = feature.diff(8)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00064000).reindex(feature.index)
FM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fm_replacement_d2_064'] = {'inputs': ['fm_replacement_064'], 'func': fm_replacement_d2_064}


def fm_replacement_d2_065(fm_replacement_065):
    feature = _clean(fm_replacement_065)
    delta = feature.diff(13)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00065000).reindex(feature.index)
FM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fm_replacement_d2_065'] = {'inputs': ['fm_replacement_065'], 'func': fm_replacement_d2_065}


def fm_replacement_d2_066(fm_replacement_066):
    feature = _clean(fm_replacement_066)
    delta = feature.diff(21)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00066000).reindex(feature.index)
FM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fm_replacement_d2_066'] = {'inputs': ['fm_replacement_066'], 'func': fm_replacement_d2_066}


def fm_replacement_d2_067(fm_replacement_067):
    feature = _clean(fm_replacement_067)
    delta = feature.diff(34)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00067000).reindex(feature.index)
FM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fm_replacement_d2_067'] = {'inputs': ['fm_replacement_067'], 'func': fm_replacement_d2_067}


def fm_replacement_d2_068(fm_replacement_068):
    feature = _clean(fm_replacement_068)
    delta = feature.diff(55)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00068000).reindex(feature.index)
FM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fm_replacement_d2_068'] = {'inputs': ['fm_replacement_068'], 'func': fm_replacement_d2_068}


def fm_replacement_d2_069(fm_replacement_069):
    feature = _clean(fm_replacement_069)
    delta = feature.diff(89)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00069000).reindex(feature.index)
FM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fm_replacement_d2_069'] = {'inputs': ['fm_replacement_069'], 'func': fm_replacement_d2_069}


def fm_replacement_d2_070(fm_replacement_070):
    feature = _clean(fm_replacement_070)
    delta = feature.diff(1)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00070000).reindex(feature.index)
FM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fm_replacement_d2_070'] = {'inputs': ['fm_replacement_070'], 'func': fm_replacement_d2_070}


def fm_replacement_d2_071(fm_replacement_071):
    feature = _clean(fm_replacement_071)
    delta = feature.diff(2)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00071000).reindex(feature.index)
FM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fm_replacement_d2_071'] = {'inputs': ['fm_replacement_071'], 'func': fm_replacement_d2_071}


def fm_replacement_d2_072(fm_replacement_072):
    feature = _clean(fm_replacement_072)
    delta = feature.diff(3)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00072000).reindex(feature.index)
FM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fm_replacement_d2_072'] = {'inputs': ['fm_replacement_072'], 'func': fm_replacement_d2_072}


def fm_replacement_d2_073(fm_replacement_073):
    feature = _clean(fm_replacement_073)
    delta = feature.diff(5)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00073000).reindex(feature.index)
FM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fm_replacement_d2_073'] = {'inputs': ['fm_replacement_073'], 'func': fm_replacement_d2_073}


def fm_replacement_d2_074(fm_replacement_074):
    feature = _clean(fm_replacement_074)
    delta = feature.diff(8)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00074000).reindex(feature.index)
FM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fm_replacement_d2_074'] = {'inputs': ['fm_replacement_074'], 'func': fm_replacement_d2_074}


def fm_replacement_d2_075(fm_replacement_075):
    feature = _clean(fm_replacement_075)
    delta = feature.diff(13)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00075000).reindex(feature.index)
FM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fm_replacement_d2_075'] = {'inputs': ['fm_replacement_075'], 'func': fm_replacement_d2_075}


def fm_replacement_d2_076(fm_replacement_076):
    feature = _clean(fm_replacement_076)
    delta = feature.diff(21)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00076000).reindex(feature.index)
FM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fm_replacement_d2_076'] = {'inputs': ['fm_replacement_076'], 'func': fm_replacement_d2_076}


def fm_replacement_d2_077(fm_replacement_077):
    feature = _clean(fm_replacement_077)
    delta = feature.diff(34)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00077000).reindex(feature.index)
FM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fm_replacement_d2_077'] = {'inputs': ['fm_replacement_077'], 'func': fm_replacement_d2_077}


def fm_replacement_d2_078(fm_replacement_078):
    feature = _clean(fm_replacement_078)
    delta = feature.diff(55)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00078000).reindex(feature.index)
FM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fm_replacement_d2_078'] = {'inputs': ['fm_replacement_078'], 'func': fm_replacement_d2_078}


def fm_replacement_d2_079(fm_replacement_079):
    feature = _clean(fm_replacement_079)
    delta = feature.diff(89)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00079000).reindex(feature.index)
FM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fm_replacement_d2_079'] = {'inputs': ['fm_replacement_079'], 'func': fm_replacement_d2_079}


def fm_replacement_d2_080(fm_replacement_080):
    feature = _clean(fm_replacement_080)
    delta = feature.diff(1)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00080000).reindex(feature.index)
FM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fm_replacement_d2_080'] = {'inputs': ['fm_replacement_080'], 'func': fm_replacement_d2_080}


def fm_replacement_d2_081(fm_replacement_081):
    feature = _clean(fm_replacement_081)
    delta = feature.diff(2)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00081000).reindex(feature.index)
FM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fm_replacement_d2_081'] = {'inputs': ['fm_replacement_081'], 'func': fm_replacement_d2_081}


def fm_replacement_d2_082(fm_replacement_082):
    feature = _clean(fm_replacement_082)
    delta = feature.diff(3)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00082000).reindex(feature.index)
FM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fm_replacement_d2_082'] = {'inputs': ['fm_replacement_082'], 'func': fm_replacement_d2_082}


def fm_replacement_d2_083(fm_replacement_083):
    feature = _clean(fm_replacement_083)
    delta = feature.diff(5)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00083000).reindex(feature.index)
FM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fm_replacement_d2_083'] = {'inputs': ['fm_replacement_083'], 'func': fm_replacement_d2_083}


def fm_replacement_d2_084(fm_replacement_084):
    feature = _clean(fm_replacement_084)
    delta = feature.diff(8)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00084000).reindex(feature.index)
FM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fm_replacement_d2_084'] = {'inputs': ['fm_replacement_084'], 'func': fm_replacement_d2_084}


def fm_replacement_d2_085(fm_replacement_085):
    feature = _clean(fm_replacement_085)
    delta = feature.diff(13)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00085000).reindex(feature.index)
FM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fm_replacement_d2_085'] = {'inputs': ['fm_replacement_085'], 'func': fm_replacement_d2_085}


def fm_replacement_d2_086(fm_replacement_086):
    feature = _clean(fm_replacement_086)
    delta = feature.diff(21)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00086000).reindex(feature.index)
FM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fm_replacement_d2_086'] = {'inputs': ['fm_replacement_086'], 'func': fm_replacement_d2_086}


def fm_replacement_d2_087(fm_replacement_087):
    feature = _clean(fm_replacement_087)
    delta = feature.diff(34)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00087000).reindex(feature.index)
FM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fm_replacement_d2_087'] = {'inputs': ['fm_replacement_087'], 'func': fm_replacement_d2_087}


def fm_replacement_d2_088(fm_replacement_088):
    feature = _clean(fm_replacement_088)
    delta = feature.diff(55)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00088000).reindex(feature.index)
FM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fm_replacement_d2_088'] = {'inputs': ['fm_replacement_088'], 'func': fm_replacement_d2_088}


def fm_replacement_d2_089(fm_replacement_089):
    feature = _clean(fm_replacement_089)
    delta = feature.diff(89)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00089000).reindex(feature.index)
FM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fm_replacement_d2_089'] = {'inputs': ['fm_replacement_089'], 'func': fm_replacement_d2_089}


def fm_replacement_d2_090(fm_replacement_090):
    feature = _clean(fm_replacement_090)
    delta = feature.diff(1)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00090000).reindex(feature.index)
FM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fm_replacement_d2_090'] = {'inputs': ['fm_replacement_090'], 'func': fm_replacement_d2_090}


def fm_replacement_d2_091(fm_replacement_091):
    feature = _clean(fm_replacement_091)
    delta = feature.diff(2)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00091000).reindex(feature.index)
FM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fm_replacement_d2_091'] = {'inputs': ['fm_replacement_091'], 'func': fm_replacement_d2_091}


def fm_replacement_d2_092(fm_replacement_092):
    feature = _clean(fm_replacement_092)
    delta = feature.diff(3)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00092000).reindex(feature.index)
FM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fm_replacement_d2_092'] = {'inputs': ['fm_replacement_092'], 'func': fm_replacement_d2_092}


def fm_replacement_d2_093(fm_replacement_093):
    feature = _clean(fm_replacement_093)
    delta = feature.diff(5)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00093000).reindex(feature.index)
FM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fm_replacement_d2_093'] = {'inputs': ['fm_replacement_093'], 'func': fm_replacement_d2_093}


def fm_replacement_d2_094(fm_replacement_094):
    feature = _clean(fm_replacement_094)
    delta = feature.diff(8)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00094000).reindex(feature.index)
FM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fm_replacement_d2_094'] = {'inputs': ['fm_replacement_094'], 'func': fm_replacement_d2_094}


def fm_replacement_d2_095(fm_replacement_095):
    feature = _clean(fm_replacement_095)
    delta = feature.diff(13)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00095000).reindex(feature.index)
FM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fm_replacement_d2_095'] = {'inputs': ['fm_replacement_095'], 'func': fm_replacement_d2_095}


def fm_replacement_d2_096(fm_replacement_096):
    feature = _clean(fm_replacement_096)
    delta = feature.diff(21)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00096000).reindex(feature.index)
FM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fm_replacement_d2_096'] = {'inputs': ['fm_replacement_096'], 'func': fm_replacement_d2_096}


def fm_replacement_d2_097(fm_replacement_097):
    feature = _clean(fm_replacement_097)
    delta = feature.diff(34)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00097000).reindex(feature.index)
FM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fm_replacement_d2_097'] = {'inputs': ['fm_replacement_097'], 'func': fm_replacement_d2_097}


def fm_replacement_d2_098(fm_replacement_098):
    feature = _clean(fm_replacement_098)
    delta = feature.diff(55)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00098000).reindex(feature.index)
FM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fm_replacement_d2_098'] = {'inputs': ['fm_replacement_098'], 'func': fm_replacement_d2_098}


def fm_replacement_d2_099(fm_replacement_099):
    feature = _clean(fm_replacement_099)
    delta = feature.diff(89)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00099000).reindex(feature.index)
FM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fm_replacement_d2_099'] = {'inputs': ['fm_replacement_099'], 'func': fm_replacement_d2_099}


def fm_replacement_d2_100(fm_replacement_100):
    feature = _clean(fm_replacement_100)
    delta = feature.diff(1)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00100000).reindex(feature.index)
FM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fm_replacement_d2_100'] = {'inputs': ['fm_replacement_100'], 'func': fm_replacement_d2_100}


def fm_replacement_d2_101(fm_replacement_101):
    feature = _clean(fm_replacement_101)
    delta = feature.diff(2)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00101000).reindex(feature.index)
FM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fm_replacement_d2_101'] = {'inputs': ['fm_replacement_101'], 'func': fm_replacement_d2_101}


def fm_replacement_d2_102(fm_replacement_102):
    feature = _clean(fm_replacement_102)
    delta = feature.diff(3)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00102000).reindex(feature.index)
FM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fm_replacement_d2_102'] = {'inputs': ['fm_replacement_102'], 'func': fm_replacement_d2_102}


def fm_replacement_d2_103(fm_replacement_103):
    feature = _clean(fm_replacement_103)
    delta = feature.diff(5)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00103000).reindex(feature.index)
FM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fm_replacement_d2_103'] = {'inputs': ['fm_replacement_103'], 'func': fm_replacement_d2_103}


def fm_replacement_d2_104(fm_replacement_104):
    feature = _clean(fm_replacement_104)
    delta = feature.diff(8)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00104000).reindex(feature.index)
FM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fm_replacement_d2_104'] = {'inputs': ['fm_replacement_104'], 'func': fm_replacement_d2_104}


def fm_replacement_d2_105(fm_replacement_105):
    feature = _clean(fm_replacement_105)
    delta = feature.diff(13)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00105000).reindex(feature.index)
FM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fm_replacement_d2_105'] = {'inputs': ['fm_replacement_105'], 'func': fm_replacement_d2_105}


def fm_replacement_d2_106(fm_replacement_106):
    feature = _clean(fm_replacement_106)
    delta = feature.diff(21)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00106000).reindex(feature.index)
FM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fm_replacement_d2_106'] = {'inputs': ['fm_replacement_106'], 'func': fm_replacement_d2_106}


def fm_replacement_d2_107(fm_replacement_107):
    feature = _clean(fm_replacement_107)
    delta = feature.diff(34)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00107000).reindex(feature.index)
FM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fm_replacement_d2_107'] = {'inputs': ['fm_replacement_107'], 'func': fm_replacement_d2_107}


def fm_replacement_d2_108(fm_replacement_108):
    feature = _clean(fm_replacement_108)
    delta = feature.diff(55)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00108000).reindex(feature.index)
FM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fm_replacement_d2_108'] = {'inputs': ['fm_replacement_108'], 'func': fm_replacement_d2_108}


def fm_replacement_d2_109(fm_replacement_109):
    feature = _clean(fm_replacement_109)
    delta = feature.diff(89)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00109000).reindex(feature.index)
FM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fm_replacement_d2_109'] = {'inputs': ['fm_replacement_109'], 'func': fm_replacement_d2_109}


def fm_replacement_d2_110(fm_replacement_110):
    feature = _clean(fm_replacement_110)
    delta = feature.diff(1)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00110000).reindex(feature.index)
FM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fm_replacement_d2_110'] = {'inputs': ['fm_replacement_110'], 'func': fm_replacement_d2_110}


def fm_replacement_d2_111(fm_replacement_111):
    feature = _clean(fm_replacement_111)
    delta = feature.diff(2)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00111000).reindex(feature.index)
FM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fm_replacement_d2_111'] = {'inputs': ['fm_replacement_111'], 'func': fm_replacement_d2_111}


def fm_replacement_d2_112(fm_replacement_112):
    feature = _clean(fm_replacement_112)
    delta = feature.diff(3)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00112000).reindex(feature.index)
FM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fm_replacement_d2_112'] = {'inputs': ['fm_replacement_112'], 'func': fm_replacement_d2_112}


def fm_replacement_d2_113(fm_replacement_113):
    feature = _clean(fm_replacement_113)
    delta = feature.diff(5)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00113000).reindex(feature.index)
FM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fm_replacement_d2_113'] = {'inputs': ['fm_replacement_113'], 'func': fm_replacement_d2_113}


def fm_replacement_d2_114(fm_replacement_114):
    feature = _clean(fm_replacement_114)
    delta = feature.diff(8)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00114000).reindex(feature.index)
FM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fm_replacement_d2_114'] = {'inputs': ['fm_replacement_114'], 'func': fm_replacement_d2_114}


def fm_replacement_d2_115(fm_replacement_115):
    feature = _clean(fm_replacement_115)
    delta = feature.diff(13)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00115000).reindex(feature.index)
FM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fm_replacement_d2_115'] = {'inputs': ['fm_replacement_115'], 'func': fm_replacement_d2_115}


def fm_replacement_d2_116(fm_replacement_116):
    feature = _clean(fm_replacement_116)
    delta = feature.diff(21)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00116000).reindex(feature.index)
FM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fm_replacement_d2_116'] = {'inputs': ['fm_replacement_116'], 'func': fm_replacement_d2_116}


def fm_replacement_d2_117(fm_replacement_117):
    feature = _clean(fm_replacement_117)
    delta = feature.diff(34)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00117000).reindex(feature.index)
FM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fm_replacement_d2_117'] = {'inputs': ['fm_replacement_117'], 'func': fm_replacement_d2_117}


def fm_replacement_d2_118(fm_replacement_118):
    feature = _clean(fm_replacement_118)
    delta = feature.diff(55)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00118000).reindex(feature.index)
FM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fm_replacement_d2_118'] = {'inputs': ['fm_replacement_118'], 'func': fm_replacement_d2_118}


def fm_replacement_d2_119(fm_replacement_119):
    feature = _clean(fm_replacement_119)
    delta = feature.diff(89)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00119000).reindex(feature.index)
FM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fm_replacement_d2_119'] = {'inputs': ['fm_replacement_119'], 'func': fm_replacement_d2_119}


def fm_replacement_d2_120(fm_replacement_120):
    feature = _clean(fm_replacement_120)
    delta = feature.diff(1)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00120000).reindex(feature.index)
FM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fm_replacement_d2_120'] = {'inputs': ['fm_replacement_120'], 'func': fm_replacement_d2_120}


def fm_replacement_d2_121(fm_replacement_121):
    feature = _clean(fm_replacement_121)
    delta = feature.diff(2)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00121000).reindex(feature.index)
FM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fm_replacement_d2_121'] = {'inputs': ['fm_replacement_121'], 'func': fm_replacement_d2_121}


def fm_replacement_d2_122(fm_replacement_122):
    feature = _clean(fm_replacement_122)
    delta = feature.diff(3)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00122000).reindex(feature.index)
FM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fm_replacement_d2_122'] = {'inputs': ['fm_replacement_122'], 'func': fm_replacement_d2_122}


def fm_replacement_d2_123(fm_replacement_123):
    feature = _clean(fm_replacement_123)
    delta = feature.diff(5)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00123000).reindex(feature.index)
FM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fm_replacement_d2_123'] = {'inputs': ['fm_replacement_123'], 'func': fm_replacement_d2_123}


def fm_replacement_d2_124(fm_replacement_124):
    feature = _clean(fm_replacement_124)
    delta = feature.diff(8)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00124000).reindex(feature.index)
FM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fm_replacement_d2_124'] = {'inputs': ['fm_replacement_124'], 'func': fm_replacement_d2_124}


def fm_replacement_d2_125(fm_replacement_125):
    feature = _clean(fm_replacement_125)
    delta = feature.diff(13)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00125000).reindex(feature.index)
FM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fm_replacement_d2_125'] = {'inputs': ['fm_replacement_125'], 'func': fm_replacement_d2_125}


def fm_replacement_d2_126(fm_replacement_126):
    feature = _clean(fm_replacement_126)
    delta = feature.diff(21)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00126000).reindex(feature.index)
FM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fm_replacement_d2_126'] = {'inputs': ['fm_replacement_126'], 'func': fm_replacement_d2_126}


def fm_replacement_d2_127(fm_replacement_127):
    feature = _clean(fm_replacement_127)
    delta = feature.diff(34)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00127000).reindex(feature.index)
FM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fm_replacement_d2_127'] = {'inputs': ['fm_replacement_127'], 'func': fm_replacement_d2_127}


def fm_replacement_d2_128(fm_replacement_128):
    feature = _clean(fm_replacement_128)
    delta = feature.diff(55)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00128000).reindex(feature.index)
FM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fm_replacement_d2_128'] = {'inputs': ['fm_replacement_128'], 'func': fm_replacement_d2_128}


def fm_replacement_d2_129(fm_replacement_129):
    feature = _clean(fm_replacement_129)
    delta = feature.diff(89)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00129000).reindex(feature.index)
FM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fm_replacement_d2_129'] = {'inputs': ['fm_replacement_129'], 'func': fm_replacement_d2_129}


def fm_replacement_d2_130(fm_replacement_130):
    feature = _clean(fm_replacement_130)
    delta = feature.diff(1)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00130000).reindex(feature.index)
FM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fm_replacement_d2_130'] = {'inputs': ['fm_replacement_130'], 'func': fm_replacement_d2_130}


def fm_replacement_d2_131(fm_replacement_131):
    feature = _clean(fm_replacement_131)
    delta = feature.diff(2)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00131000).reindex(feature.index)
FM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fm_replacement_d2_131'] = {'inputs': ['fm_replacement_131'], 'func': fm_replacement_d2_131}


def fm_replacement_d2_132(fm_replacement_132):
    feature = _clean(fm_replacement_132)
    delta = feature.diff(3)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00132000).reindex(feature.index)
FM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fm_replacement_d2_132'] = {'inputs': ['fm_replacement_132'], 'func': fm_replacement_d2_132}


def fm_replacement_d2_133(fm_replacement_133):
    feature = _clean(fm_replacement_133)
    delta = feature.diff(5)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00133000).reindex(feature.index)
FM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fm_replacement_d2_133'] = {'inputs': ['fm_replacement_133'], 'func': fm_replacement_d2_133}


def fm_replacement_d2_134(fm_replacement_134):
    feature = _clean(fm_replacement_134)
    delta = feature.diff(8)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00134000).reindex(feature.index)
FM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fm_replacement_d2_134'] = {'inputs': ['fm_replacement_134'], 'func': fm_replacement_d2_134}


def fm_replacement_d2_135(fm_replacement_135):
    feature = _clean(fm_replacement_135)
    delta = feature.diff(13)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00135000).reindex(feature.index)
FM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fm_replacement_d2_135'] = {'inputs': ['fm_replacement_135'], 'func': fm_replacement_d2_135}


def fm_replacement_d2_136(fm_replacement_136):
    feature = _clean(fm_replacement_136)
    delta = feature.diff(21)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00136000).reindex(feature.index)
FM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fm_replacement_d2_136'] = {'inputs': ['fm_replacement_136'], 'func': fm_replacement_d2_136}


def fm_replacement_d2_137(fm_replacement_137):
    feature = _clean(fm_replacement_137)
    delta = feature.diff(34)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00137000).reindex(feature.index)
FM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fm_replacement_d2_137'] = {'inputs': ['fm_replacement_137'], 'func': fm_replacement_d2_137}


def fm_replacement_d2_138(fm_replacement_138):
    feature = _clean(fm_replacement_138)
    delta = feature.diff(55)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00138000).reindex(feature.index)
FM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fm_replacement_d2_138'] = {'inputs': ['fm_replacement_138'], 'func': fm_replacement_d2_138}


def fm_replacement_d2_139(fm_replacement_139):
    feature = _clean(fm_replacement_139)
    delta = feature.diff(89)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00139000).reindex(feature.index)
FM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fm_replacement_d2_139'] = {'inputs': ['fm_replacement_139'], 'func': fm_replacement_d2_139}


def fm_replacement_d2_140(fm_replacement_140):
    feature = _clean(fm_replacement_140)
    delta = feature.diff(1)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00140000).reindex(feature.index)
FM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fm_replacement_d2_140'] = {'inputs': ['fm_replacement_140'], 'func': fm_replacement_d2_140}


def fm_replacement_d2_141(fm_replacement_141):
    feature = _clean(fm_replacement_141)
    delta = feature.diff(2)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00141000).reindex(feature.index)
FM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fm_replacement_d2_141'] = {'inputs': ['fm_replacement_141'], 'func': fm_replacement_d2_141}


def fm_replacement_d2_142(fm_replacement_142):
    feature = _clean(fm_replacement_142)
    delta = feature.diff(3)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00142000).reindex(feature.index)
FM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fm_replacement_d2_142'] = {'inputs': ['fm_replacement_142'], 'func': fm_replacement_d2_142}


def fm_replacement_d2_143(fm_replacement_143):
    feature = _clean(fm_replacement_143)
    delta = feature.diff(5)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00143000).reindex(feature.index)
FM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fm_replacement_d2_143'] = {'inputs': ['fm_replacement_143'], 'func': fm_replacement_d2_143}


def fm_replacement_d2_144(fm_replacement_144):
    feature = _clean(fm_replacement_144)
    delta = feature.diff(8)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00144000).reindex(feature.index)
FM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fm_replacement_d2_144'] = {'inputs': ['fm_replacement_144'], 'func': fm_replacement_d2_144}


def fm_replacement_d2_145(fm_replacement_145):
    feature = _clean(fm_replacement_145)
    delta = feature.diff(13)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00145000).reindex(feature.index)
FM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fm_replacement_d2_145'] = {'inputs': ['fm_replacement_145'], 'func': fm_replacement_d2_145}


def fm_replacement_d2_146(fm_replacement_146):
    feature = _clean(fm_replacement_146)
    delta = feature.diff(21)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00146000).reindex(feature.index)
FM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fm_replacement_d2_146'] = {'inputs': ['fm_replacement_146'], 'func': fm_replacement_d2_146}


def fm_replacement_d2_147(fm_replacement_147):
    feature = _clean(fm_replacement_147)
    delta = feature.diff(34)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00147000).reindex(feature.index)
FM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fm_replacement_d2_147'] = {'inputs': ['fm_replacement_147'], 'func': fm_replacement_d2_147}


def fm_replacement_d2_148(fm_replacement_148):
    feature = _clean(fm_replacement_148)
    delta = feature.diff(55)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00148000).reindex(feature.index)
FM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fm_replacement_d2_148'] = {'inputs': ['fm_replacement_148'], 'func': fm_replacement_d2_148}


def fm_replacement_d2_149(fm_replacement_149):
    feature = _clean(fm_replacement_149)
    delta = feature.diff(89)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00149000).reindex(feature.index)
FM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fm_replacement_d2_149'] = {'inputs': ['fm_replacement_149'], 'func': fm_replacement_d2_149}


def fm_replacement_d2_150(fm_replacement_150):
    feature = _clean(fm_replacement_150)
    delta = feature.diff(1)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00150000).reindex(feature.index)
FM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fm_replacement_d2_150'] = {'inputs': ['fm_replacement_150'], 'func': fm_replacement_d2_150}


def fm_replacement_d2_151(fm_replacement_151):
    feature = _clean(fm_replacement_151)
    delta = feature.diff(2)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00151000).reindex(feature.index)
FM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fm_replacement_d2_151'] = {'inputs': ['fm_replacement_151'], 'func': fm_replacement_d2_151}


def fm_replacement_d2_152(fm_replacement_152):
    feature = _clean(fm_replacement_152)
    delta = feature.diff(3)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00152000).reindex(feature.index)
FM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fm_replacement_d2_152'] = {'inputs': ['fm_replacement_152'], 'func': fm_replacement_d2_152}


def fm_replacement_d2_153(fm_replacement_153):
    feature = _clean(fm_replacement_153)
    delta = feature.diff(5)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00153000).reindex(feature.index)
FM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fm_replacement_d2_153'] = {'inputs': ['fm_replacement_153'], 'func': fm_replacement_d2_153}


def fm_replacement_d2_154(fm_replacement_154):
    feature = _clean(fm_replacement_154)
    delta = feature.diff(8)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00154000).reindex(feature.index)
FM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fm_replacement_d2_154'] = {'inputs': ['fm_replacement_154'], 'func': fm_replacement_d2_154}


def fm_replacement_d2_155(fm_replacement_155):
    feature = _clean(fm_replacement_155)
    delta = feature.diff(13)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00155000).reindex(feature.index)
FM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fm_replacement_d2_155'] = {'inputs': ['fm_replacement_155'], 'func': fm_replacement_d2_155}


def fm_replacement_d2_156(fm_replacement_156):
    feature = _clean(fm_replacement_156)
    delta = feature.diff(21)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00156000).reindex(feature.index)
FM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fm_replacement_d2_156'] = {'inputs': ['fm_replacement_156'], 'func': fm_replacement_d2_156}


def fm_replacement_d2_157(fm_replacement_157):
    feature = _clean(fm_replacement_157)
    delta = feature.diff(34)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00157000).reindex(feature.index)
FM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fm_replacement_d2_157'] = {'inputs': ['fm_replacement_157'], 'func': fm_replacement_d2_157}


def fm_replacement_d2_158(fm_replacement_158):
    feature = _clean(fm_replacement_158)
    delta = feature.diff(55)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00158000).reindex(feature.index)
FM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fm_replacement_d2_158'] = {'inputs': ['fm_replacement_158'], 'func': fm_replacement_d2_158}


def fm_replacement_d2_159(fm_replacement_159):
    feature = _clean(fm_replacement_159)
    delta = feature.diff(89)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00159000).reindex(feature.index)
FM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fm_replacement_d2_159'] = {'inputs': ['fm_replacement_159'], 'func': fm_replacement_d2_159}


def fm_replacement_d2_160(fm_replacement_160):
    feature = _clean(fm_replacement_160)
    delta = feature.diff(1)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00160000).reindex(feature.index)
FM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fm_replacement_d2_160'] = {'inputs': ['fm_replacement_160'], 'func': fm_replacement_d2_160}


def fm_replacement_d2_161(fm_replacement_161):
    feature = _clean(fm_replacement_161)
    delta = feature.diff(2)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00161000).reindex(feature.index)
FM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fm_replacement_d2_161'] = {'inputs': ['fm_replacement_161'], 'func': fm_replacement_d2_161}


def fm_replacement_d2_162(fm_replacement_162):
    feature = _clean(fm_replacement_162)
    delta = feature.diff(3)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00162000).reindex(feature.index)
FM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fm_replacement_d2_162'] = {'inputs': ['fm_replacement_162'], 'func': fm_replacement_d2_162}


def fm_replacement_d2_163(fm_replacement_163):
    feature = _clean(fm_replacement_163)
    delta = feature.diff(5)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00163000).reindex(feature.index)
FM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fm_replacement_d2_163'] = {'inputs': ['fm_replacement_163'], 'func': fm_replacement_d2_163}


def fm_replacement_d2_164(fm_replacement_164):
    feature = _clean(fm_replacement_164)
    delta = feature.diff(8)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00164000).reindex(feature.index)
FM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fm_replacement_d2_164'] = {'inputs': ['fm_replacement_164'], 'func': fm_replacement_d2_164}


def fm_replacement_d2_165(fm_replacement_165):
    feature = _clean(fm_replacement_165)
    delta = feature.diff(13)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00165000).reindex(feature.index)
FM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fm_replacement_d2_165'] = {'inputs': ['fm_replacement_165'], 'func': fm_replacement_d2_165}


def fm_replacement_d2_166(fm_replacement_166):
    feature = _clean(fm_replacement_166)
    delta = feature.diff(21)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00166000).reindex(feature.index)
FM_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['fm_replacement_d2_166'] = {'inputs': ['fm_replacement_166'], 'func': fm_replacement_d2_166}


# Base-universe derivative extensions for repaired first-base features.
FMO_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY = {}


def _base_universe_d2(feature, idx):
    feature = _clean(feature) if '_clean' in globals() else _s(feature).replace([np.inf, -np.inf], np.nan)
    windows = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    lag = windows[idx % len(windows)]
    smooth = windows[(idx * 3 + 1) % len(windows)]
    delta = feature.diff(lag)
    local = feature - feature.rolling(max(3, smooth), min_periods=2).mean()
    out = delta + local.fillna(0.0) * (0.00037 * ((idx % 17) + 1))
    return out.replace([np.inf, -np.inf], np.nan).reindex(feature.index)


def fmo_base_universe_d2_001_fmo_003_fcf_burn_to_cash_63(fmo_003_fcf_burn_to_cash_63):
    return _base_universe_d2(fmo_003_fcf_burn_to_cash_63, 1)
FMO_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['fmo_base_universe_d2_001_fmo_003_fcf_burn_to_cash_63'] = {'inputs': ['fmo_003_fcf_burn_to_cash_63'], 'func': fmo_base_universe_d2_001_fmo_003_fcf_burn_to_cash_63}


def fmo_base_universe_d2_002_fmo_004_debt_to_equity_84(fmo_004_debt_to_equity_84):
    return _base_universe_d2(fmo_004_debt_to_equity_84, 2)
FMO_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['fmo_base_universe_d2_002_fmo_004_debt_to_equity_84'] = {'inputs': ['fmo_004_debt_to_equity_84'], 'func': fmo_base_universe_d2_002_fmo_004_debt_to_equity_84}


def fmo_base_universe_d2_003_fmo_005_debt_to_assets_126(fmo_005_debt_to_assets_126):
    return _base_universe_d2(fmo_005_debt_to_assets_126, 3)
FMO_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['fmo_base_universe_d2_003_fmo_005_debt_to_assets_126'] = {'inputs': ['fmo_005_debt_to_assets_126'], 'func': fmo_base_universe_d2_003_fmo_005_debt_to_assets_126}


def fmo_base_universe_d2_004_fmo_012_accrual_gap_1260(fmo_012_accrual_gap_1260):
    return _base_universe_d2(fmo_012_accrual_gap_1260, 4)
FMO_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['fmo_base_universe_d2_004_fmo_012_accrual_gap_1260'] = {'inputs': ['fmo_012_accrual_gap_1260'], 'func': fmo_base_universe_d2_004_fmo_012_accrual_gap_1260}


def fmo_base_universe_d2_005_fmo_016_debt_to_equity_21(fmo_016_debt_to_equity_21):
    return _base_universe_d2(fmo_016_debt_to_equity_21, 5)
FMO_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['fmo_base_universe_d2_005_fmo_016_debt_to_equity_21'] = {'inputs': ['fmo_016_debt_to_equity_21'], 'func': fmo_base_universe_d2_005_fmo_016_debt_to_equity_21}


def fmo_base_universe_d2_006_fmo_017_debt_to_assets_42(fmo_017_debt_to_assets_42):
    return _base_universe_d2(fmo_017_debt_to_assets_42, 6)
FMO_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['fmo_base_universe_d2_006_fmo_017_debt_to_assets_42'] = {'inputs': ['fmo_017_debt_to_assets_42'], 'func': fmo_base_universe_d2_006_fmo_017_debt_to_assets_42}


def fmo_base_universe_d2_007_fmo_024_accrual_gap_504(fmo_024_accrual_gap_504):
    return _base_universe_d2(fmo_024_accrual_gap_504, 7)
FMO_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['fmo_base_universe_d2_007_fmo_024_accrual_gap_504'] = {'inputs': ['fmo_024_accrual_gap_504'], 'func': fmo_base_universe_d2_007_fmo_024_accrual_gap_504}


def fmo_base_universe_d2_008_fmo_027_fcf_burn_to_cash_1260(fmo_027_fcf_burn_to_cash_1260):
    return _base_universe_d2(fmo_027_fcf_burn_to_cash_1260, 8)
FMO_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['fmo_base_universe_d2_008_fmo_027_fcf_burn_to_cash_1260'] = {'inputs': ['fmo_027_fcf_burn_to_cash_1260'], 'func': fmo_base_universe_d2_008_fmo_027_fcf_burn_to_cash_1260}


def fmo_base_universe_d2_009_fmo_028_debt_to_equity_1512(fmo_028_debt_to_equity_1512):
    return _base_universe_d2(fmo_028_debt_to_equity_1512, 9)
FMO_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['fmo_base_universe_d2_009_fmo_028_debt_to_equity_1512'] = {'inputs': ['fmo_028_debt_to_equity_1512'], 'func': fmo_base_universe_d2_009_fmo_028_debt_to_equity_1512}


def fmo_base_universe_d2_010_fmo_029_debt_to_assets_63(fmo_029_debt_to_assets_63):
    return _base_universe_d2(fmo_029_debt_to_assets_63, 10)
FMO_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['fmo_base_universe_d2_010_fmo_029_debt_to_assets_63'] = {'inputs': ['fmo_029_debt_to_assets_63'], 'func': fmo_base_universe_d2_010_fmo_029_debt_to_assets_63}


def fmo_base_universe_d2_011_fmo_031_interest_coverage_stress_21(fmo_031_interest_coverage_stress_21):
    return _base_universe_d2(fmo_031_interest_coverage_stress_21, 11)
FMO_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['fmo_base_universe_d2_011_fmo_031_interest_coverage_stress_21'] = {'inputs': ['fmo_031_interest_coverage_stress_21'], 'func': fmo_base_universe_d2_011_fmo_031_interest_coverage_stress_21}


def fmo_base_universe_d2_012_fmo_036_accrual_gap_189(fmo_036_accrual_gap_189):
    return _base_universe_d2(fmo_036_accrual_gap_189, 12)
FMO_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['fmo_base_universe_d2_012_fmo_036_accrual_gap_189'] = {'inputs': ['fmo_036_accrual_gap_189'], 'func': fmo_base_universe_d2_012_fmo_036_accrual_gap_189}


def fmo_base_universe_d2_013_fmo_039_fcf_burn_to_cash_504(fmo_039_fcf_burn_to_cash_504):
    return _base_universe_d2(fmo_039_fcf_burn_to_cash_504, 13)
FMO_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['fmo_base_universe_d2_013_fmo_039_fcf_burn_to_cash_504'] = {'inputs': ['fmo_039_fcf_burn_to_cash_504'], 'func': fmo_base_universe_d2_013_fmo_039_fcf_burn_to_cash_504}


def fmo_base_universe_d2_014_fmo_040_debt_to_equity_756(fmo_040_debt_to_equity_756):
    return _base_universe_d2(fmo_040_debt_to_equity_756, 14)
FMO_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['fmo_base_universe_d2_014_fmo_040_debt_to_equity_756'] = {'inputs': ['fmo_040_debt_to_equity_756'], 'func': fmo_base_universe_d2_014_fmo_040_debt_to_equity_756}


def fmo_base_universe_d2_015_fmo_041_debt_to_assets_1008(fmo_041_debt_to_assets_1008):
    return _base_universe_d2(fmo_041_debt_to_assets_1008, 15)
FMO_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['fmo_base_universe_d2_015_fmo_041_debt_to_assets_1008'] = {'inputs': ['fmo_041_debt_to_assets_1008'], 'func': fmo_base_universe_d2_015_fmo_041_debt_to_assets_1008}


def fmo_base_universe_d2_016_fmo_043_interest_coverage_stress_1512(fmo_043_interest_coverage_stress_1512):
    return _base_universe_d2(fmo_043_interest_coverage_stress_1512, 16)
FMO_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['fmo_base_universe_d2_016_fmo_043_interest_coverage_stress_1512'] = {'inputs': ['fmo_043_interest_coverage_stress_1512'], 'func': fmo_base_universe_d2_016_fmo_043_interest_coverage_stress_1512}


def fmo_base_universe_d2_017_fmo_048_accrual_gap_63(fmo_048_accrual_gap_63):
    return _base_universe_d2(fmo_048_accrual_gap_63, 17)
FMO_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['fmo_base_universe_d2_017_fmo_048_accrual_gap_63'] = {'inputs': ['fmo_048_accrual_gap_63'], 'func': fmo_base_universe_d2_017_fmo_048_accrual_gap_63}


def fmo_base_universe_d2_018_fmo_051_fcf_burn_to_cash_189(fmo_051_fcf_burn_to_cash_189):
    return _base_universe_d2(fmo_051_fcf_burn_to_cash_189, 18)
FMO_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['fmo_base_universe_d2_018_fmo_051_fcf_burn_to_cash_189'] = {'inputs': ['fmo_051_fcf_burn_to_cash_189'], 'func': fmo_base_universe_d2_018_fmo_051_fcf_burn_to_cash_189}


def fmo_base_universe_d2_019_fmo_052_debt_to_equity_252(fmo_052_debt_to_equity_252):
    return _base_universe_d2(fmo_052_debt_to_equity_252, 19)
FMO_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['fmo_base_universe_d2_019_fmo_052_debt_to_equity_252'] = {'inputs': ['fmo_052_debt_to_equity_252'], 'func': fmo_base_universe_d2_019_fmo_052_debt_to_equity_252}


def fmo_base_universe_d2_020_fmo_053_debt_to_assets_378(fmo_053_debt_to_assets_378):
    return _base_universe_d2(fmo_053_debt_to_assets_378, 20)
FMO_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['fmo_base_universe_d2_020_fmo_053_debt_to_assets_378'] = {'inputs': ['fmo_053_debt_to_assets_378'], 'func': fmo_base_universe_d2_020_fmo_053_debt_to_assets_378}


def fmo_base_universe_d2_021_fmo_055_interest_coverage_stress_756(fmo_055_interest_coverage_stress_756):
    return _base_universe_d2(fmo_055_interest_coverage_stress_756, 21)
FMO_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['fmo_base_universe_d2_021_fmo_055_interest_coverage_stress_756'] = {'inputs': ['fmo_055_interest_coverage_stress_756'], 'func': fmo_base_universe_d2_021_fmo_055_interest_coverage_stress_756}


def fmo_base_universe_d2_022_fmo_060_accrual_gap_252(fmo_060_accrual_gap_252):
    return _base_universe_d2(fmo_060_accrual_gap_252, 22)
FMO_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['fmo_base_universe_d2_022_fmo_060_accrual_gap_252'] = {'inputs': ['fmo_060_accrual_gap_252'], 'func': fmo_base_universe_d2_022_fmo_060_accrual_gap_252}


def fmo_base_universe_d2_023_fmo_basefill_001(fmo_basefill_001):
    return _base_universe_d2(fmo_basefill_001, 23)
FMO_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['fmo_base_universe_d2_023_fmo_basefill_001'] = {'inputs': ['fmo_basefill_001'], 'func': fmo_base_universe_d2_023_fmo_basefill_001}


def fmo_base_universe_d2_024_fmo_basefill_002(fmo_basefill_002):
    return _base_universe_d2(fmo_basefill_002, 24)
FMO_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['fmo_base_universe_d2_024_fmo_basefill_002'] = {'inputs': ['fmo_basefill_002'], 'func': fmo_base_universe_d2_024_fmo_basefill_002}


def fmo_base_universe_d2_025_fmo_basefill_006(fmo_basefill_006):
    return _base_universe_d2(fmo_basefill_006, 25)
FMO_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['fmo_base_universe_d2_025_fmo_basefill_006'] = {'inputs': ['fmo_basefill_006'], 'func': fmo_base_universe_d2_025_fmo_basefill_006}


def fmo_base_universe_d2_026_fmo_basefill_008(fmo_basefill_008):
    return _base_universe_d2(fmo_basefill_008, 26)
FMO_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['fmo_base_universe_d2_026_fmo_basefill_008'] = {'inputs': ['fmo_basefill_008'], 'func': fmo_base_universe_d2_026_fmo_basefill_008}


def fmo_base_universe_d2_027_fmo_basefill_009(fmo_basefill_009):
    return _base_universe_d2(fmo_basefill_009, 27)
FMO_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['fmo_base_universe_d2_027_fmo_basefill_009'] = {'inputs': ['fmo_basefill_009'], 'func': fmo_base_universe_d2_027_fmo_basefill_009}


def fmo_base_universe_d2_028_fmo_basefill_010(fmo_basefill_010):
    return _base_universe_d2(fmo_basefill_010, 28)
FMO_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['fmo_base_universe_d2_028_fmo_basefill_010'] = {'inputs': ['fmo_basefill_010'], 'func': fmo_base_universe_d2_028_fmo_basefill_010}


def fmo_base_universe_d2_029_fmo_basefill_011(fmo_basefill_011):
    return _base_universe_d2(fmo_basefill_011, 29)
FMO_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['fmo_base_universe_d2_029_fmo_basefill_011'] = {'inputs': ['fmo_basefill_011'], 'func': fmo_base_universe_d2_029_fmo_basefill_011}


def fmo_base_universe_d2_030_fmo_basefill_013(fmo_basefill_013):
    return _base_universe_d2(fmo_basefill_013, 30)
FMO_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['fmo_base_universe_d2_030_fmo_basefill_013'] = {'inputs': ['fmo_basefill_013'], 'func': fmo_base_universe_d2_030_fmo_basefill_013}


def fmo_base_universe_d2_031_fmo_basefill_014(fmo_basefill_014):
    return _base_universe_d2(fmo_basefill_014, 31)
FMO_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['fmo_base_universe_d2_031_fmo_basefill_014'] = {'inputs': ['fmo_basefill_014'], 'func': fmo_base_universe_d2_031_fmo_basefill_014}


def fmo_base_universe_d2_032_fmo_basefill_015(fmo_basefill_015):
    return _base_universe_d2(fmo_basefill_015, 32)
FMO_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['fmo_base_universe_d2_032_fmo_basefill_015'] = {'inputs': ['fmo_basefill_015'], 'func': fmo_base_universe_d2_032_fmo_basefill_015}


def fmo_base_universe_d2_033_fmo_basefill_018(fmo_basefill_018):
    return _base_universe_d2(fmo_basefill_018, 33)
FMO_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['fmo_base_universe_d2_033_fmo_basefill_018'] = {'inputs': ['fmo_basefill_018'], 'func': fmo_base_universe_d2_033_fmo_basefill_018}


def fmo_base_universe_d2_034_fmo_basefill_020(fmo_basefill_020):
    return _base_universe_d2(fmo_basefill_020, 34)
FMO_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['fmo_base_universe_d2_034_fmo_basefill_020'] = {'inputs': ['fmo_basefill_020'], 'func': fmo_base_universe_d2_034_fmo_basefill_020}


def fmo_base_universe_d2_035_fmo_basefill_021(fmo_basefill_021):
    return _base_universe_d2(fmo_basefill_021, 35)
FMO_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['fmo_base_universe_d2_035_fmo_basefill_021'] = {'inputs': ['fmo_basefill_021'], 'func': fmo_base_universe_d2_035_fmo_basefill_021}


def fmo_base_universe_d2_036_fmo_basefill_022(fmo_basefill_022):
    return _base_universe_d2(fmo_basefill_022, 36)
FMO_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['fmo_base_universe_d2_036_fmo_basefill_022'] = {'inputs': ['fmo_basefill_022'], 'func': fmo_base_universe_d2_036_fmo_basefill_022}


def fmo_base_universe_d2_037_fmo_basefill_023(fmo_basefill_023):
    return _base_universe_d2(fmo_basefill_023, 37)
FMO_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['fmo_base_universe_d2_037_fmo_basefill_023'] = {'inputs': ['fmo_basefill_023'], 'func': fmo_base_universe_d2_037_fmo_basefill_023}


def fmo_base_universe_d2_038_fmo_basefill_025(fmo_basefill_025):
    return _base_universe_d2(fmo_basefill_025, 38)
FMO_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['fmo_base_universe_d2_038_fmo_basefill_025'] = {'inputs': ['fmo_basefill_025'], 'func': fmo_base_universe_d2_038_fmo_basefill_025}


def fmo_base_universe_d2_039_fmo_basefill_026(fmo_basefill_026):
    return _base_universe_d2(fmo_basefill_026, 39)
FMO_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['fmo_base_universe_d2_039_fmo_basefill_026'] = {'inputs': ['fmo_basefill_026'], 'func': fmo_base_universe_d2_039_fmo_basefill_026}


def fmo_base_universe_d2_040_fmo_basefill_030(fmo_basefill_030):
    return _base_universe_d2(fmo_basefill_030, 40)
FMO_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['fmo_base_universe_d2_040_fmo_basefill_030'] = {'inputs': ['fmo_basefill_030'], 'func': fmo_base_universe_d2_040_fmo_basefill_030}


def fmo_base_universe_d2_041_fmo_basefill_032(fmo_basefill_032):
    return _base_universe_d2(fmo_basefill_032, 41)
FMO_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['fmo_base_universe_d2_041_fmo_basefill_032'] = {'inputs': ['fmo_basefill_032'], 'func': fmo_base_universe_d2_041_fmo_basefill_032}


def fmo_base_universe_d2_042_fmo_basefill_033(fmo_basefill_033):
    return _base_universe_d2(fmo_basefill_033, 42)
FMO_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['fmo_base_universe_d2_042_fmo_basefill_033'] = {'inputs': ['fmo_basefill_033'], 'func': fmo_base_universe_d2_042_fmo_basefill_033}


def fmo_base_universe_d2_043_fmo_basefill_034(fmo_basefill_034):
    return _base_universe_d2(fmo_basefill_034, 43)
FMO_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['fmo_base_universe_d2_043_fmo_basefill_034'] = {'inputs': ['fmo_basefill_034'], 'func': fmo_base_universe_d2_043_fmo_basefill_034}


def fmo_base_universe_d2_044_fmo_basefill_035(fmo_basefill_035):
    return _base_universe_d2(fmo_basefill_035, 44)
FMO_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['fmo_base_universe_d2_044_fmo_basefill_035'] = {'inputs': ['fmo_basefill_035'], 'func': fmo_base_universe_d2_044_fmo_basefill_035}


def fmo_base_universe_d2_045_fmo_basefill_037(fmo_basefill_037):
    return _base_universe_d2(fmo_basefill_037, 45)
FMO_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['fmo_base_universe_d2_045_fmo_basefill_037'] = {'inputs': ['fmo_basefill_037'], 'func': fmo_base_universe_d2_045_fmo_basefill_037}


def fmo_base_universe_d2_046_fmo_basefill_038(fmo_basefill_038):
    return _base_universe_d2(fmo_basefill_038, 46)
FMO_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['fmo_base_universe_d2_046_fmo_basefill_038'] = {'inputs': ['fmo_basefill_038'], 'func': fmo_base_universe_d2_046_fmo_basefill_038}


def fmo_base_universe_d2_047_fmo_basefill_042(fmo_basefill_042):
    return _base_universe_d2(fmo_basefill_042, 47)
FMO_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['fmo_base_universe_d2_047_fmo_basefill_042'] = {'inputs': ['fmo_basefill_042'], 'func': fmo_base_universe_d2_047_fmo_basefill_042}


def fmo_base_universe_d2_048_fmo_basefill_044(fmo_basefill_044):
    return _base_universe_d2(fmo_basefill_044, 48)
FMO_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['fmo_base_universe_d2_048_fmo_basefill_044'] = {'inputs': ['fmo_basefill_044'], 'func': fmo_base_universe_d2_048_fmo_basefill_044}


def fmo_base_universe_d2_049_fmo_basefill_045(fmo_basefill_045):
    return _base_universe_d2(fmo_basefill_045, 49)
FMO_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['fmo_base_universe_d2_049_fmo_basefill_045'] = {'inputs': ['fmo_basefill_045'], 'func': fmo_base_universe_d2_049_fmo_basefill_045}


def fmo_base_universe_d2_050_fmo_basefill_046(fmo_basefill_046):
    return _base_universe_d2(fmo_basefill_046, 50)
FMO_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['fmo_base_universe_d2_050_fmo_basefill_046'] = {'inputs': ['fmo_basefill_046'], 'func': fmo_base_universe_d2_050_fmo_basefill_046}


def fmo_base_universe_d2_051_fmo_basefill_047(fmo_basefill_047):
    return _base_universe_d2(fmo_basefill_047, 51)
FMO_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['fmo_base_universe_d2_051_fmo_basefill_047'] = {'inputs': ['fmo_basefill_047'], 'func': fmo_base_universe_d2_051_fmo_basefill_047}


def fmo_base_universe_d2_052_fmo_basefill_049(fmo_basefill_049):
    return _base_universe_d2(fmo_basefill_049, 52)
FMO_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['fmo_base_universe_d2_052_fmo_basefill_049'] = {'inputs': ['fmo_basefill_049'], 'func': fmo_base_universe_d2_052_fmo_basefill_049}


def fmo_base_universe_d2_053_fmo_basefill_050(fmo_basefill_050):
    return _base_universe_d2(fmo_basefill_050, 53)
FMO_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['fmo_base_universe_d2_053_fmo_basefill_050'] = {'inputs': ['fmo_basefill_050'], 'func': fmo_base_universe_d2_053_fmo_basefill_050}


def fmo_base_universe_d2_054_fmo_basefill_054(fmo_basefill_054):
    return _base_universe_d2(fmo_basefill_054, 54)
FMO_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['fmo_base_universe_d2_054_fmo_basefill_054'] = {'inputs': ['fmo_basefill_054'], 'func': fmo_base_universe_d2_054_fmo_basefill_054}


def fmo_base_universe_d2_055_fmo_basefill_056(fmo_basefill_056):
    return _base_universe_d2(fmo_basefill_056, 55)
FMO_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['fmo_base_universe_d2_055_fmo_basefill_056'] = {'inputs': ['fmo_basefill_056'], 'func': fmo_base_universe_d2_055_fmo_basefill_056}


def fmo_base_universe_d2_056_fmo_basefill_057(fmo_basefill_057):
    return _base_universe_d2(fmo_basefill_057, 56)
FMO_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['fmo_base_universe_d2_056_fmo_basefill_057'] = {'inputs': ['fmo_basefill_057'], 'func': fmo_base_universe_d2_056_fmo_basefill_057}


def fmo_base_universe_d2_057_fmo_basefill_058(fmo_basefill_058):
    return _base_universe_d2(fmo_basefill_058, 57)
FMO_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['fmo_base_universe_d2_057_fmo_basefill_058'] = {'inputs': ['fmo_basefill_058'], 'func': fmo_base_universe_d2_057_fmo_basefill_058}


def fmo_base_universe_d2_058_fmo_basefill_059(fmo_basefill_059):
    return _base_universe_d2(fmo_basefill_059, 58)
FMO_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['fmo_base_universe_d2_058_fmo_basefill_059'] = {'inputs': ['fmo_basefill_059'], 'func': fmo_base_universe_d2_058_fmo_basefill_059}


def fmo_base_universe_d2_059_fmo_basefill_061(fmo_basefill_061):
    return _base_universe_d2(fmo_basefill_061, 59)
FMO_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['fmo_base_universe_d2_059_fmo_basefill_061'] = {'inputs': ['fmo_basefill_061'], 'func': fmo_base_universe_d2_059_fmo_basefill_061}


def fmo_base_universe_d2_060_fmo_basefill_062(fmo_basefill_062):
    return _base_universe_d2(fmo_basefill_062, 60)
FMO_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['fmo_base_universe_d2_060_fmo_basefill_062'] = {'inputs': ['fmo_basefill_062'], 'func': fmo_base_universe_d2_060_fmo_basefill_062}


def fmo_base_universe_d2_061_fmo_basefill_063(fmo_basefill_063):
    return _base_universe_d2(fmo_basefill_063, 61)
FMO_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['fmo_base_universe_d2_061_fmo_basefill_063'] = {'inputs': ['fmo_basefill_063'], 'func': fmo_base_universe_d2_061_fmo_basefill_063}


def fmo_base_universe_d2_062_fmo_basefill_064(fmo_basefill_064):
    return _base_universe_d2(fmo_basefill_064, 62)
FMO_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['fmo_base_universe_d2_062_fmo_basefill_064'] = {'inputs': ['fmo_basefill_064'], 'func': fmo_base_universe_d2_062_fmo_basefill_064}


def fmo_base_universe_d2_063_fmo_basefill_065(fmo_basefill_065):
    return _base_universe_d2(fmo_basefill_065, 63)
FMO_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['fmo_base_universe_d2_063_fmo_basefill_065'] = {'inputs': ['fmo_basefill_065'], 'func': fmo_base_universe_d2_063_fmo_basefill_065}


def fmo_base_universe_d2_064_fmo_basefill_066(fmo_basefill_066):
    return _base_universe_d2(fmo_basefill_066, 64)
FMO_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['fmo_base_universe_d2_064_fmo_basefill_066'] = {'inputs': ['fmo_basefill_066'], 'func': fmo_base_universe_d2_064_fmo_basefill_066}


def fmo_base_universe_d2_065_fmo_basefill_067(fmo_basefill_067):
    return _base_universe_d2(fmo_basefill_067, 65)
FMO_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['fmo_base_universe_d2_065_fmo_basefill_067'] = {'inputs': ['fmo_basefill_067'], 'func': fmo_base_universe_d2_065_fmo_basefill_067}


def fmo_base_universe_d2_066_fmo_basefill_068(fmo_basefill_068):
    return _base_universe_d2(fmo_basefill_068, 66)
FMO_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['fmo_base_universe_d2_066_fmo_basefill_068'] = {'inputs': ['fmo_basefill_068'], 'func': fmo_base_universe_d2_066_fmo_basefill_068}


def fmo_base_universe_d2_067_fmo_basefill_069(fmo_basefill_069):
    return _base_universe_d2(fmo_basefill_069, 67)
FMO_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['fmo_base_universe_d2_067_fmo_basefill_069'] = {'inputs': ['fmo_basefill_069'], 'func': fmo_base_universe_d2_067_fmo_basefill_069}


def fmo_base_universe_d2_068_fmo_basefill_070(fmo_basefill_070):
    return _base_universe_d2(fmo_basefill_070, 68)
FMO_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['fmo_base_universe_d2_068_fmo_basefill_070'] = {'inputs': ['fmo_basefill_070'], 'func': fmo_base_universe_d2_068_fmo_basefill_070}


def fmo_base_universe_d2_069_fmo_basefill_071(fmo_basefill_071):
    return _base_universe_d2(fmo_basefill_071, 69)
FMO_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['fmo_base_universe_d2_069_fmo_basefill_071'] = {'inputs': ['fmo_basefill_071'], 'func': fmo_base_universe_d2_069_fmo_basefill_071}


def fmo_base_universe_d2_070_fmo_basefill_072(fmo_basefill_072):
    return _base_universe_d2(fmo_basefill_072, 70)
FMO_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['fmo_base_universe_d2_070_fmo_basefill_072'] = {'inputs': ['fmo_basefill_072'], 'func': fmo_base_universe_d2_070_fmo_basefill_072}


def fmo_base_universe_d2_071_fmo_basefill_073(fmo_basefill_073):
    return _base_universe_d2(fmo_basefill_073, 71)
FMO_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['fmo_base_universe_d2_071_fmo_basefill_073'] = {'inputs': ['fmo_basefill_073'], 'func': fmo_base_universe_d2_071_fmo_basefill_073}


def fmo_base_universe_d2_072_fmo_basefill_074(fmo_basefill_074):
    return _base_universe_d2(fmo_basefill_074, 72)
FMO_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['fmo_base_universe_d2_072_fmo_basefill_074'] = {'inputs': ['fmo_basefill_074'], 'func': fmo_base_universe_d2_072_fmo_basefill_074}


def fmo_base_universe_d2_073_fmo_basefill_075(fmo_basefill_075):
    return _base_universe_d2(fmo_basefill_075, 73)
FMO_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['fmo_base_universe_d2_073_fmo_basefill_075'] = {'inputs': ['fmo_basefill_075'], 'func': fmo_base_universe_d2_073_fmo_basefill_075}
