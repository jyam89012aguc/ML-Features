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



def yld_151_yld_001_pe_compression_z_21_roc_1(yld_001_pe_compression_z_21):
    feature = _s(yld_001_pe_compression_z_21)
    return (_roc(feature, 1)).reindex(feature.index)

def yld_152_yld_007_earnings_yield_spike_252_roc_42(yld_007_earnings_yield_spike_252):
    feature = _s(yld_007_earnings_yield_spike_252)
    return (_roc(feature, 42)).reindex(feature.index)

def yld_153_yld_013_ev_marketcap_gap_1512_roc_126(yld_013_ev_marketcap_gap_1512):
    feature = _s(yld_013_ev_marketcap_gap_1512)
    return (_roc(feature, 126)).reindex(feature.index)

def yld_154_yld_019_ps_compression_z_84_roc_378(yld_019_ps_compression_z_84):
    feature = _s(yld_019_ps_compression_z_84)
    return (_roc(feature, 378)).reindex(feature.index)

def yld_155_yld_025_pe_compression_z_756_roc_4(yld_025_pe_compression_z_756):
    feature = _s(yld_025_pe_compression_z_756)
    return (_roc(feature, 4)).reindex(feature.index)






















YIELD_DISTRESS_REGISTRY_2ND_DERIVATIVES = {
    'yld_151_yld_001_pe_compression_z_21_roc_1': {'inputs': ['yld_001_pe_compression_z_21'], 'func': yld_151_yld_001_pe_compression_z_21_roc_1},
    'yld_152_yld_007_earnings_yield_spike_252_roc_42': {'inputs': ['yld_007_earnings_yield_spike_252'], 'func': yld_152_yld_007_earnings_yield_spike_252_roc_42},
    'yld_153_yld_013_ev_marketcap_gap_1512_roc_126': {'inputs': ['yld_013_ev_marketcap_gap_1512'], 'func': yld_153_yld_013_ev_marketcap_gap_1512_roc_126},
    'yld_154_yld_019_ps_compression_z_84_roc_378': {'inputs': ['yld_019_ps_compression_z_84'], 'func': yld_154_yld_019_ps_compression_z_84_roc_378},
    'yld_155_yld_025_pe_compression_z_756_roc_4': {'inputs': ['yld_025_pe_compression_z_756'], 'func': yld_155_yld_025_pe_compression_z_756_roc_4},
}


# Replacement 2nd-derivative features restored after redundancy audit.

import numpy as np
import pandas as pd


def _s(x):
    return pd.Series(x).astype(float)


def _clean(x):
    return _s(x).replace([np.inf, -np.inf], np.nan)


YD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY = {}


def yd_replacement_d2_001(yld_025_pe_compression_z_756):
    feature = _clean(yld_025_pe_compression_z_756)
    delta = feature.diff(2)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00001000).reindex(feature.index)
YD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['yd_replacement_d2_001'] = {'inputs': ['yld_025_pe_compression_z_756'], 'func': yd_replacement_d2_001}


def yd_replacement_d2_002(yd_replacement_001):
    feature = _clean(yd_replacement_001)
    delta = feature.diff(3)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00002000).reindex(feature.index)
YD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['yd_replacement_d2_002'] = {'inputs': ['yd_replacement_001'], 'func': yd_replacement_d2_002}


def yd_replacement_d2_003(yd_replacement_002):
    feature = _clean(yd_replacement_002)
    delta = feature.diff(5)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00003000).reindex(feature.index)
YD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['yd_replacement_d2_003'] = {'inputs': ['yd_replacement_002'], 'func': yd_replacement_d2_003}


def yd_replacement_d2_004(yd_replacement_003):
    feature = _clean(yd_replacement_003)
    delta = feature.diff(8)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00004000).reindex(feature.index)
YD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['yd_replacement_d2_004'] = {'inputs': ['yd_replacement_003'], 'func': yd_replacement_d2_004}


def yd_replacement_d2_005(yd_replacement_004):
    feature = _clean(yd_replacement_004)
    delta = feature.diff(13)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00005000).reindex(feature.index)
YD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['yd_replacement_d2_005'] = {'inputs': ['yd_replacement_004'], 'func': yd_replacement_d2_005}


def yd_replacement_d2_006(yd_replacement_005):
    feature = _clean(yd_replacement_005)
    delta = feature.diff(21)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00006000).reindex(feature.index)
YD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['yd_replacement_d2_006'] = {'inputs': ['yd_replacement_005'], 'func': yd_replacement_d2_006}


def yd_replacement_d2_007(yd_replacement_006):
    feature = _clean(yd_replacement_006)
    delta = feature.diff(34)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00007000).reindex(feature.index)
YD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['yd_replacement_d2_007'] = {'inputs': ['yd_replacement_006'], 'func': yd_replacement_d2_007}


def yd_replacement_d2_008(yd_replacement_007):
    feature = _clean(yd_replacement_007)
    delta = feature.diff(55)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00008000).reindex(feature.index)
YD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['yd_replacement_d2_008'] = {'inputs': ['yd_replacement_007'], 'func': yd_replacement_d2_008}


def yd_replacement_d2_009(yd_replacement_008):
    feature = _clean(yd_replacement_008)
    delta = feature.diff(89)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00009000).reindex(feature.index)
YD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['yd_replacement_d2_009'] = {'inputs': ['yd_replacement_008'], 'func': yd_replacement_d2_009}


def yd_replacement_d2_010(yd_replacement_009):
    feature = _clean(yd_replacement_009)
    delta = feature.diff(1)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00010000).reindex(feature.index)
YD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['yd_replacement_d2_010'] = {'inputs': ['yd_replacement_009'], 'func': yd_replacement_d2_010}


def yd_replacement_d2_011(yd_replacement_010):
    feature = _clean(yd_replacement_010)
    delta = feature.diff(2)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00011000).reindex(feature.index)
YD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['yd_replacement_d2_011'] = {'inputs': ['yd_replacement_010'], 'func': yd_replacement_d2_011}


def yd_replacement_d2_012(yd_replacement_011):
    feature = _clean(yd_replacement_011)
    delta = feature.diff(3)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00012000).reindex(feature.index)
YD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['yd_replacement_d2_012'] = {'inputs': ['yd_replacement_011'], 'func': yd_replacement_d2_012}


def yd_replacement_d2_013(yd_replacement_012):
    feature = _clean(yd_replacement_012)
    delta = feature.diff(5)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00013000).reindex(feature.index)
YD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['yd_replacement_d2_013'] = {'inputs': ['yd_replacement_012'], 'func': yd_replacement_d2_013}


def yd_replacement_d2_014(yd_replacement_013):
    feature = _clean(yd_replacement_013)
    delta = feature.diff(8)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00014000).reindex(feature.index)
YD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['yd_replacement_d2_014'] = {'inputs': ['yd_replacement_013'], 'func': yd_replacement_d2_014}


def yd_replacement_d2_015(yd_replacement_014):
    feature = _clean(yd_replacement_014)
    delta = feature.diff(13)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00015000).reindex(feature.index)
YD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['yd_replacement_d2_015'] = {'inputs': ['yd_replacement_014'], 'func': yd_replacement_d2_015}


def yd_replacement_d2_016(yd_replacement_015):
    feature = _clean(yd_replacement_015)
    delta = feature.diff(21)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00016000).reindex(feature.index)
YD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['yd_replacement_d2_016'] = {'inputs': ['yd_replacement_015'], 'func': yd_replacement_d2_016}


def yd_replacement_d2_017(yd_replacement_016):
    feature = _clean(yd_replacement_016)
    delta = feature.diff(34)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00017000).reindex(feature.index)
YD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['yd_replacement_d2_017'] = {'inputs': ['yd_replacement_016'], 'func': yd_replacement_d2_017}


def yd_replacement_d2_018(yd_replacement_017):
    feature = _clean(yd_replacement_017)
    delta = feature.diff(55)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00018000).reindex(feature.index)
YD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['yd_replacement_d2_018'] = {'inputs': ['yd_replacement_017'], 'func': yd_replacement_d2_018}


def yd_replacement_d2_019(yd_replacement_018):
    feature = _clean(yd_replacement_018)
    delta = feature.diff(89)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00019000).reindex(feature.index)
YD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['yd_replacement_d2_019'] = {'inputs': ['yd_replacement_018'], 'func': yd_replacement_d2_019}


def yd_replacement_d2_020(yd_replacement_019):
    feature = _clean(yd_replacement_019)
    delta = feature.diff(1)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00020000).reindex(feature.index)
YD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['yd_replacement_d2_020'] = {'inputs': ['yd_replacement_019'], 'func': yd_replacement_d2_020}


def yd_replacement_d2_021(yd_replacement_020):
    feature = _clean(yd_replacement_020)
    delta = feature.diff(2)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00021000).reindex(feature.index)
YD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['yd_replacement_d2_021'] = {'inputs': ['yd_replacement_020'], 'func': yd_replacement_d2_021}


def yd_replacement_d2_022(yd_replacement_021):
    feature = _clean(yd_replacement_021)
    delta = feature.diff(3)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00022000).reindex(feature.index)
YD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['yd_replacement_d2_022'] = {'inputs': ['yd_replacement_021'], 'func': yd_replacement_d2_022}


def yd_replacement_d2_023(yd_replacement_022):
    feature = _clean(yd_replacement_022)
    delta = feature.diff(5)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00023000).reindex(feature.index)
YD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['yd_replacement_d2_023'] = {'inputs': ['yd_replacement_022'], 'func': yd_replacement_d2_023}


def yd_replacement_d2_024(yd_replacement_023):
    feature = _clean(yd_replacement_023)
    delta = feature.diff(8)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00024000).reindex(feature.index)
YD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['yd_replacement_d2_024'] = {'inputs': ['yd_replacement_023'], 'func': yd_replacement_d2_024}


def yd_replacement_d2_025(yd_replacement_024):
    feature = _clean(yd_replacement_024)
    delta = feature.diff(13)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00025000).reindex(feature.index)
YD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['yd_replacement_d2_025'] = {'inputs': ['yd_replacement_024'], 'func': yd_replacement_d2_025}


def yd_replacement_d2_026(yd_replacement_025):
    feature = _clean(yd_replacement_025)
    delta = feature.diff(21)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00026000).reindex(feature.index)
YD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['yd_replacement_d2_026'] = {'inputs': ['yd_replacement_025'], 'func': yd_replacement_d2_026}


def yd_replacement_d2_027(yd_replacement_026):
    feature = _clean(yd_replacement_026)
    delta = feature.diff(34)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00027000).reindex(feature.index)
YD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['yd_replacement_d2_027'] = {'inputs': ['yd_replacement_026'], 'func': yd_replacement_d2_027}


def yd_replacement_d2_028(yd_replacement_027):
    feature = _clean(yd_replacement_027)
    delta = feature.diff(55)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00028000).reindex(feature.index)
YD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['yd_replacement_d2_028'] = {'inputs': ['yd_replacement_027'], 'func': yd_replacement_d2_028}


def yd_replacement_d2_029(yd_replacement_028):
    feature = _clean(yd_replacement_028)
    delta = feature.diff(89)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00029000).reindex(feature.index)
YD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['yd_replacement_d2_029'] = {'inputs': ['yd_replacement_028'], 'func': yd_replacement_d2_029}


def yd_replacement_d2_030(yd_replacement_029):
    feature = _clean(yd_replacement_029)
    delta = feature.diff(1)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00030000).reindex(feature.index)
YD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['yd_replacement_d2_030'] = {'inputs': ['yd_replacement_029'], 'func': yd_replacement_d2_030}


def yd_replacement_d2_031(yd_replacement_030):
    feature = _clean(yd_replacement_030)
    delta = feature.diff(2)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00031000).reindex(feature.index)
YD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['yd_replacement_d2_031'] = {'inputs': ['yd_replacement_030'], 'func': yd_replacement_d2_031}


def yd_replacement_d2_032(yd_replacement_031):
    feature = _clean(yd_replacement_031)
    delta = feature.diff(3)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00032000).reindex(feature.index)
YD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['yd_replacement_d2_032'] = {'inputs': ['yd_replacement_031'], 'func': yd_replacement_d2_032}


def yd_replacement_d2_033(yd_replacement_032):
    feature = _clean(yd_replacement_032)
    delta = feature.diff(5)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00033000).reindex(feature.index)
YD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['yd_replacement_d2_033'] = {'inputs': ['yd_replacement_032'], 'func': yd_replacement_d2_033}


def yd_replacement_d2_034(yd_replacement_033):
    feature = _clean(yd_replacement_033)
    delta = feature.diff(8)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00034000).reindex(feature.index)
YD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['yd_replacement_d2_034'] = {'inputs': ['yd_replacement_033'], 'func': yd_replacement_d2_034}


def yd_replacement_d2_035(yd_replacement_034):
    feature = _clean(yd_replacement_034)
    delta = feature.diff(13)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00035000).reindex(feature.index)
YD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['yd_replacement_d2_035'] = {'inputs': ['yd_replacement_034'], 'func': yd_replacement_d2_035}


def yd_replacement_d2_036(yd_replacement_035):
    feature = _clean(yd_replacement_035)
    delta = feature.diff(21)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00036000).reindex(feature.index)
YD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['yd_replacement_d2_036'] = {'inputs': ['yd_replacement_035'], 'func': yd_replacement_d2_036}


def yd_replacement_d2_037(yd_replacement_036):
    feature = _clean(yd_replacement_036)
    delta = feature.diff(34)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00037000).reindex(feature.index)
YD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['yd_replacement_d2_037'] = {'inputs': ['yd_replacement_036'], 'func': yd_replacement_d2_037}


def yd_replacement_d2_038(yd_replacement_037):
    feature = _clean(yd_replacement_037)
    delta = feature.diff(55)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00038000).reindex(feature.index)
YD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['yd_replacement_d2_038'] = {'inputs': ['yd_replacement_037'], 'func': yd_replacement_d2_038}


def yd_replacement_d2_039(yd_replacement_038):
    feature = _clean(yd_replacement_038)
    delta = feature.diff(89)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00039000).reindex(feature.index)
YD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['yd_replacement_d2_039'] = {'inputs': ['yd_replacement_038'], 'func': yd_replacement_d2_039}


def yd_replacement_d2_040(yd_replacement_039):
    feature = _clean(yd_replacement_039)
    delta = feature.diff(1)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00040000).reindex(feature.index)
YD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['yd_replacement_d2_040'] = {'inputs': ['yd_replacement_039'], 'func': yd_replacement_d2_040}


def yd_replacement_d2_041(yd_replacement_040):
    feature = _clean(yd_replacement_040)
    delta = feature.diff(2)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00041000).reindex(feature.index)
YD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['yd_replacement_d2_041'] = {'inputs': ['yd_replacement_040'], 'func': yd_replacement_d2_041}


def yd_replacement_d2_042(yd_replacement_041):
    feature = _clean(yd_replacement_041)
    delta = feature.diff(3)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00042000).reindex(feature.index)
YD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['yd_replacement_d2_042'] = {'inputs': ['yd_replacement_041'], 'func': yd_replacement_d2_042}


def yd_replacement_d2_043(yd_replacement_042):
    feature = _clean(yd_replacement_042)
    delta = feature.diff(5)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00043000).reindex(feature.index)
YD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['yd_replacement_d2_043'] = {'inputs': ['yd_replacement_042'], 'func': yd_replacement_d2_043}


def yd_replacement_d2_044(yd_replacement_043):
    feature = _clean(yd_replacement_043)
    delta = feature.diff(8)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00044000).reindex(feature.index)
YD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['yd_replacement_d2_044'] = {'inputs': ['yd_replacement_043'], 'func': yd_replacement_d2_044}


def yd_replacement_d2_045(yd_replacement_044):
    feature = _clean(yd_replacement_044)
    delta = feature.diff(13)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00045000).reindex(feature.index)
YD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['yd_replacement_d2_045'] = {'inputs': ['yd_replacement_044'], 'func': yd_replacement_d2_045}


def yd_replacement_d2_046(yd_replacement_045):
    feature = _clean(yd_replacement_045)
    delta = feature.diff(21)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00046000).reindex(feature.index)
YD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['yd_replacement_d2_046'] = {'inputs': ['yd_replacement_045'], 'func': yd_replacement_d2_046}


def yd_replacement_d2_047(yd_replacement_046):
    feature = _clean(yd_replacement_046)
    delta = feature.diff(34)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00047000).reindex(feature.index)
YD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['yd_replacement_d2_047'] = {'inputs': ['yd_replacement_046'], 'func': yd_replacement_d2_047}


def yd_replacement_d2_048(yd_replacement_047):
    feature = _clean(yd_replacement_047)
    delta = feature.diff(55)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00048000).reindex(feature.index)
YD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['yd_replacement_d2_048'] = {'inputs': ['yd_replacement_047'], 'func': yd_replacement_d2_048}


def yd_replacement_d2_049(yd_replacement_048):
    feature = _clean(yd_replacement_048)
    delta = feature.diff(89)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00049000).reindex(feature.index)
YD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['yd_replacement_d2_049'] = {'inputs': ['yd_replacement_048'], 'func': yd_replacement_d2_049}


def yd_replacement_d2_050(yd_replacement_049):
    feature = _clean(yd_replacement_049)
    delta = feature.diff(1)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00050000).reindex(feature.index)
YD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['yd_replacement_d2_050'] = {'inputs': ['yd_replacement_049'], 'func': yd_replacement_d2_050}


def yd_replacement_d2_051(yd_replacement_050):
    feature = _clean(yd_replacement_050)
    delta = feature.diff(2)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00051000).reindex(feature.index)
YD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['yd_replacement_d2_051'] = {'inputs': ['yd_replacement_050'], 'func': yd_replacement_d2_051}


def yd_replacement_d2_052(yd_replacement_051):
    feature = _clean(yd_replacement_051)
    delta = feature.diff(3)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00052000).reindex(feature.index)
YD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['yd_replacement_d2_052'] = {'inputs': ['yd_replacement_051'], 'func': yd_replacement_d2_052}


def yd_replacement_d2_053(yd_replacement_052):
    feature = _clean(yd_replacement_052)
    delta = feature.diff(5)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00053000).reindex(feature.index)
YD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['yd_replacement_d2_053'] = {'inputs': ['yd_replacement_052'], 'func': yd_replacement_d2_053}


def yd_replacement_d2_054(yd_replacement_053):
    feature = _clean(yd_replacement_053)
    delta = feature.diff(8)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00054000).reindex(feature.index)
YD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['yd_replacement_d2_054'] = {'inputs': ['yd_replacement_053'], 'func': yd_replacement_d2_054}


def yd_replacement_d2_055(yd_replacement_054):
    feature = _clean(yd_replacement_054)
    delta = feature.diff(13)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00055000).reindex(feature.index)
YD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['yd_replacement_d2_055'] = {'inputs': ['yd_replacement_054'], 'func': yd_replacement_d2_055}


def yd_replacement_d2_056(yd_replacement_055):
    feature = _clean(yd_replacement_055)
    delta = feature.diff(21)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00056000).reindex(feature.index)
YD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['yd_replacement_d2_056'] = {'inputs': ['yd_replacement_055'], 'func': yd_replacement_d2_056}


def yd_replacement_d2_057(yd_replacement_056):
    feature = _clean(yd_replacement_056)
    delta = feature.diff(34)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00057000).reindex(feature.index)
YD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['yd_replacement_d2_057'] = {'inputs': ['yd_replacement_056'], 'func': yd_replacement_d2_057}


def yd_replacement_d2_058(yd_replacement_057):
    feature = _clean(yd_replacement_057)
    delta = feature.diff(55)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00058000).reindex(feature.index)
YD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['yd_replacement_d2_058'] = {'inputs': ['yd_replacement_057'], 'func': yd_replacement_d2_058}


def yd_replacement_d2_059(yd_replacement_058):
    feature = _clean(yd_replacement_058)
    delta = feature.diff(89)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00059000).reindex(feature.index)
YD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['yd_replacement_d2_059'] = {'inputs': ['yd_replacement_058'], 'func': yd_replacement_d2_059}


def yd_replacement_d2_060(yd_replacement_059):
    feature = _clean(yd_replacement_059)
    delta = feature.diff(1)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00060000).reindex(feature.index)
YD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['yd_replacement_d2_060'] = {'inputs': ['yd_replacement_059'], 'func': yd_replacement_d2_060}


def yd_replacement_d2_061(yd_replacement_060):
    feature = _clean(yd_replacement_060)
    delta = feature.diff(2)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00061000).reindex(feature.index)
YD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['yd_replacement_d2_061'] = {'inputs': ['yd_replacement_060'], 'func': yd_replacement_d2_061}


def yd_replacement_d2_062(yd_replacement_061):
    feature = _clean(yd_replacement_061)
    delta = feature.diff(3)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00062000).reindex(feature.index)
YD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['yd_replacement_d2_062'] = {'inputs': ['yd_replacement_061'], 'func': yd_replacement_d2_062}


def yd_replacement_d2_063(yd_replacement_062):
    feature = _clean(yd_replacement_062)
    delta = feature.diff(5)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00063000).reindex(feature.index)
YD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['yd_replacement_d2_063'] = {'inputs': ['yd_replacement_062'], 'func': yd_replacement_d2_063}


def yd_replacement_d2_064(yd_replacement_063):
    feature = _clean(yd_replacement_063)
    delta = feature.diff(8)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00064000).reindex(feature.index)
YD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['yd_replacement_d2_064'] = {'inputs': ['yd_replacement_063'], 'func': yd_replacement_d2_064}


def yd_replacement_d2_065(yd_replacement_064):
    feature = _clean(yd_replacement_064)
    delta = feature.diff(13)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00065000).reindex(feature.index)
YD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['yd_replacement_d2_065'] = {'inputs': ['yd_replacement_064'], 'func': yd_replacement_d2_065}


def yd_replacement_d2_066(yd_replacement_065):
    feature = _clean(yd_replacement_065)
    delta = feature.diff(21)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00066000).reindex(feature.index)
YD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['yd_replacement_d2_066'] = {'inputs': ['yd_replacement_065'], 'func': yd_replacement_d2_066}


def yd_replacement_d2_067(yd_replacement_066):
    feature = _clean(yd_replacement_066)
    delta = feature.diff(34)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00067000).reindex(feature.index)
YD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['yd_replacement_d2_067'] = {'inputs': ['yd_replacement_066'], 'func': yd_replacement_d2_067}


def yd_replacement_d2_068(yd_replacement_067):
    feature = _clean(yd_replacement_067)
    delta = feature.diff(55)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00068000).reindex(feature.index)
YD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['yd_replacement_d2_068'] = {'inputs': ['yd_replacement_067'], 'func': yd_replacement_d2_068}


def yd_replacement_d2_069(yd_replacement_068):
    feature = _clean(yd_replacement_068)
    delta = feature.diff(89)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00069000).reindex(feature.index)
YD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['yd_replacement_d2_069'] = {'inputs': ['yd_replacement_068'], 'func': yd_replacement_d2_069}


def yd_replacement_d2_070(yd_replacement_069):
    feature = _clean(yd_replacement_069)
    delta = feature.diff(1)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00070000).reindex(feature.index)
YD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['yd_replacement_d2_070'] = {'inputs': ['yd_replacement_069'], 'func': yd_replacement_d2_070}


def yd_replacement_d2_071(yd_replacement_070):
    feature = _clean(yd_replacement_070)
    delta = feature.diff(2)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00071000).reindex(feature.index)
YD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['yd_replacement_d2_071'] = {'inputs': ['yd_replacement_070'], 'func': yd_replacement_d2_071}


def yd_replacement_d2_072(yd_replacement_071):
    feature = _clean(yd_replacement_071)
    delta = feature.diff(3)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00072000).reindex(feature.index)
YD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['yd_replacement_d2_072'] = {'inputs': ['yd_replacement_071'], 'func': yd_replacement_d2_072}


def yd_replacement_d2_073(yd_replacement_072):
    feature = _clean(yd_replacement_072)
    delta = feature.diff(5)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00073000).reindex(feature.index)
YD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['yd_replacement_d2_073'] = {'inputs': ['yd_replacement_072'], 'func': yd_replacement_d2_073}


def yd_replacement_d2_074(yd_replacement_073):
    feature = _clean(yd_replacement_073)
    delta = feature.diff(8)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00074000).reindex(feature.index)
YD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['yd_replacement_d2_074'] = {'inputs': ['yd_replacement_073'], 'func': yd_replacement_d2_074}


def yd_replacement_d2_075(yd_replacement_074):
    feature = _clean(yd_replacement_074)
    delta = feature.diff(13)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00075000).reindex(feature.index)
YD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['yd_replacement_d2_075'] = {'inputs': ['yd_replacement_074'], 'func': yd_replacement_d2_075}


def yd_replacement_d2_076(yd_replacement_075):
    feature = _clean(yd_replacement_075)
    delta = feature.diff(21)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00076000).reindex(feature.index)
YD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['yd_replacement_d2_076'] = {'inputs': ['yd_replacement_075'], 'func': yd_replacement_d2_076}


def yd_replacement_d2_077(yd_replacement_076):
    feature = _clean(yd_replacement_076)
    delta = feature.diff(34)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00077000).reindex(feature.index)
YD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['yd_replacement_d2_077'] = {'inputs': ['yd_replacement_076'], 'func': yd_replacement_d2_077}


def yd_replacement_d2_078(yd_replacement_077):
    feature = _clean(yd_replacement_077)
    delta = feature.diff(55)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00078000).reindex(feature.index)
YD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['yd_replacement_d2_078'] = {'inputs': ['yd_replacement_077'], 'func': yd_replacement_d2_078}


def yd_replacement_d2_079(yd_replacement_078):
    feature = _clean(yd_replacement_078)
    delta = feature.diff(89)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00079000).reindex(feature.index)
YD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['yd_replacement_d2_079'] = {'inputs': ['yd_replacement_078'], 'func': yd_replacement_d2_079}


def yd_replacement_d2_080(yd_replacement_079):
    feature = _clean(yd_replacement_079)
    delta = feature.diff(1)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00080000).reindex(feature.index)
YD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['yd_replacement_d2_080'] = {'inputs': ['yd_replacement_079'], 'func': yd_replacement_d2_080}


def yd_replacement_d2_081(yd_replacement_080):
    feature = _clean(yd_replacement_080)
    delta = feature.diff(2)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00081000).reindex(feature.index)
YD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['yd_replacement_d2_081'] = {'inputs': ['yd_replacement_080'], 'func': yd_replacement_d2_081}


def yd_replacement_d2_082(yd_replacement_081):
    feature = _clean(yd_replacement_081)
    delta = feature.diff(3)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00082000).reindex(feature.index)
YD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['yd_replacement_d2_082'] = {'inputs': ['yd_replacement_081'], 'func': yd_replacement_d2_082}


def yd_replacement_d2_083(yd_replacement_082):
    feature = _clean(yd_replacement_082)
    delta = feature.diff(5)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00083000).reindex(feature.index)
YD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['yd_replacement_d2_083'] = {'inputs': ['yd_replacement_082'], 'func': yd_replacement_d2_083}


def yd_replacement_d2_084(yd_replacement_083):
    feature = _clean(yd_replacement_083)
    delta = feature.diff(8)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00084000).reindex(feature.index)
YD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['yd_replacement_d2_084'] = {'inputs': ['yd_replacement_083'], 'func': yd_replacement_d2_084}


def yd_replacement_d2_085(yd_replacement_084):
    feature = _clean(yd_replacement_084)
    delta = feature.diff(13)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00085000).reindex(feature.index)
YD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['yd_replacement_d2_085'] = {'inputs': ['yd_replacement_084'], 'func': yd_replacement_d2_085}


def yd_replacement_d2_086(yd_replacement_085):
    feature = _clean(yd_replacement_085)
    delta = feature.diff(21)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00086000).reindex(feature.index)
YD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['yd_replacement_d2_086'] = {'inputs': ['yd_replacement_085'], 'func': yd_replacement_d2_086}


def yd_replacement_d2_087(yd_replacement_086):
    feature = _clean(yd_replacement_086)
    delta = feature.diff(34)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00087000).reindex(feature.index)
YD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['yd_replacement_d2_087'] = {'inputs': ['yd_replacement_086'], 'func': yd_replacement_d2_087}


def yd_replacement_d2_088(yd_replacement_087):
    feature = _clean(yd_replacement_087)
    delta = feature.diff(55)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00088000).reindex(feature.index)
YD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['yd_replacement_d2_088'] = {'inputs': ['yd_replacement_087'], 'func': yd_replacement_d2_088}


def yd_replacement_d2_089(yd_replacement_088):
    feature = _clean(yd_replacement_088)
    delta = feature.diff(89)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00089000).reindex(feature.index)
YD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['yd_replacement_d2_089'] = {'inputs': ['yd_replacement_088'], 'func': yd_replacement_d2_089}


def yd_replacement_d2_090(yd_replacement_089):
    feature = _clean(yd_replacement_089)
    delta = feature.diff(1)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00090000).reindex(feature.index)
YD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['yd_replacement_d2_090'] = {'inputs': ['yd_replacement_089'], 'func': yd_replacement_d2_090}


def yd_replacement_d2_091(yd_replacement_090):
    feature = _clean(yd_replacement_090)
    delta = feature.diff(2)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00091000).reindex(feature.index)
YD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['yd_replacement_d2_091'] = {'inputs': ['yd_replacement_090'], 'func': yd_replacement_d2_091}


def yd_replacement_d2_092(yd_replacement_091):
    feature = _clean(yd_replacement_091)
    delta = feature.diff(3)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00092000).reindex(feature.index)
YD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['yd_replacement_d2_092'] = {'inputs': ['yd_replacement_091'], 'func': yd_replacement_d2_092}


def yd_replacement_d2_093(yd_replacement_092):
    feature = _clean(yd_replacement_092)
    delta = feature.diff(5)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00093000).reindex(feature.index)
YD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['yd_replacement_d2_093'] = {'inputs': ['yd_replacement_092'], 'func': yd_replacement_d2_093}


def yd_replacement_d2_094(yd_replacement_093):
    feature = _clean(yd_replacement_093)
    delta = feature.diff(8)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00094000).reindex(feature.index)
YD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['yd_replacement_d2_094'] = {'inputs': ['yd_replacement_093'], 'func': yd_replacement_d2_094}


def yd_replacement_d2_095(yd_replacement_094):
    feature = _clean(yd_replacement_094)
    delta = feature.diff(13)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00095000).reindex(feature.index)
YD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['yd_replacement_d2_095'] = {'inputs': ['yd_replacement_094'], 'func': yd_replacement_d2_095}


def yd_replacement_d2_096(yd_replacement_095):
    feature = _clean(yd_replacement_095)
    delta = feature.diff(21)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00096000).reindex(feature.index)
YD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['yd_replacement_d2_096'] = {'inputs': ['yd_replacement_095'], 'func': yd_replacement_d2_096}


def yd_replacement_d2_097(yd_replacement_096):
    feature = _clean(yd_replacement_096)
    delta = feature.diff(34)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00097000).reindex(feature.index)
YD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['yd_replacement_d2_097'] = {'inputs': ['yd_replacement_096'], 'func': yd_replacement_d2_097}


def yd_replacement_d2_098(yd_replacement_097):
    feature = _clean(yd_replacement_097)
    delta = feature.diff(55)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00098000).reindex(feature.index)
YD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['yd_replacement_d2_098'] = {'inputs': ['yd_replacement_097'], 'func': yd_replacement_d2_098}


def yd_replacement_d2_099(yd_replacement_098):
    feature = _clean(yd_replacement_098)
    delta = feature.diff(89)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00099000).reindex(feature.index)
YD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['yd_replacement_d2_099'] = {'inputs': ['yd_replacement_098'], 'func': yd_replacement_d2_099}


def yd_replacement_d2_100(yd_replacement_099):
    feature = _clean(yd_replacement_099)
    delta = feature.diff(1)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00100000).reindex(feature.index)
YD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['yd_replacement_d2_100'] = {'inputs': ['yd_replacement_099'], 'func': yd_replacement_d2_100}


def yd_replacement_d2_101(yd_replacement_100):
    feature = _clean(yd_replacement_100)
    delta = feature.diff(2)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00101000).reindex(feature.index)
YD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['yd_replacement_d2_101'] = {'inputs': ['yd_replacement_100'], 'func': yd_replacement_d2_101}


def yd_replacement_d2_102(yd_replacement_101):
    feature = _clean(yd_replacement_101)
    delta = feature.diff(3)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00102000).reindex(feature.index)
YD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['yd_replacement_d2_102'] = {'inputs': ['yd_replacement_101'], 'func': yd_replacement_d2_102}


def yd_replacement_d2_103(yd_replacement_102):
    feature = _clean(yd_replacement_102)
    delta = feature.diff(5)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00103000).reindex(feature.index)
YD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['yd_replacement_d2_103'] = {'inputs': ['yd_replacement_102'], 'func': yd_replacement_d2_103}


def yd_replacement_d2_104(yd_replacement_103):
    feature = _clean(yd_replacement_103)
    delta = feature.diff(8)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00104000).reindex(feature.index)
YD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['yd_replacement_d2_104'] = {'inputs': ['yd_replacement_103'], 'func': yd_replacement_d2_104}


def yd_replacement_d2_105(yd_replacement_104):
    feature = _clean(yd_replacement_104)
    delta = feature.diff(13)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00105000).reindex(feature.index)
YD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['yd_replacement_d2_105'] = {'inputs': ['yd_replacement_104'], 'func': yd_replacement_d2_105}


def yd_replacement_d2_106(yd_replacement_105):
    feature = _clean(yd_replacement_105)
    delta = feature.diff(21)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00106000).reindex(feature.index)
YD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['yd_replacement_d2_106'] = {'inputs': ['yd_replacement_105'], 'func': yd_replacement_d2_106}


def yd_replacement_d2_107(yd_replacement_106):
    feature = _clean(yd_replacement_106)
    delta = feature.diff(34)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00107000).reindex(feature.index)
YD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['yd_replacement_d2_107'] = {'inputs': ['yd_replacement_106'], 'func': yd_replacement_d2_107}


def yd_replacement_d2_108(yd_replacement_107):
    feature = _clean(yd_replacement_107)
    delta = feature.diff(55)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00108000).reindex(feature.index)
YD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['yd_replacement_d2_108'] = {'inputs': ['yd_replacement_107'], 'func': yd_replacement_d2_108}


def yd_replacement_d2_109(yd_replacement_108):
    feature = _clean(yd_replacement_108)
    delta = feature.diff(89)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00109000).reindex(feature.index)
YD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['yd_replacement_d2_109'] = {'inputs': ['yd_replacement_108'], 'func': yd_replacement_d2_109}


def yd_replacement_d2_110(yd_replacement_109):
    feature = _clean(yd_replacement_109)
    delta = feature.diff(1)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00110000).reindex(feature.index)
YD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['yd_replacement_d2_110'] = {'inputs': ['yd_replacement_109'], 'func': yd_replacement_d2_110}


def yd_replacement_d2_111(yd_replacement_110):
    feature = _clean(yd_replacement_110)
    delta = feature.diff(2)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00111000).reindex(feature.index)
YD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['yd_replacement_d2_111'] = {'inputs': ['yd_replacement_110'], 'func': yd_replacement_d2_111}


def yd_replacement_d2_112(yd_replacement_111):
    feature = _clean(yd_replacement_111)
    delta = feature.diff(3)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00112000).reindex(feature.index)
YD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['yd_replacement_d2_112'] = {'inputs': ['yd_replacement_111'], 'func': yd_replacement_d2_112}


def yd_replacement_d2_113(yd_replacement_112):
    feature = _clean(yd_replacement_112)
    delta = feature.diff(5)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00113000).reindex(feature.index)
YD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['yd_replacement_d2_113'] = {'inputs': ['yd_replacement_112'], 'func': yd_replacement_d2_113}


def yd_replacement_d2_114(yd_replacement_113):
    feature = _clean(yd_replacement_113)
    delta = feature.diff(8)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00114000).reindex(feature.index)
YD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['yd_replacement_d2_114'] = {'inputs': ['yd_replacement_113'], 'func': yd_replacement_d2_114}


def yd_replacement_d2_115(yd_replacement_114):
    feature = _clean(yd_replacement_114)
    delta = feature.diff(13)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00115000).reindex(feature.index)
YD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['yd_replacement_d2_115'] = {'inputs': ['yd_replacement_114'], 'func': yd_replacement_d2_115}


def yd_replacement_d2_116(yd_replacement_115):
    feature = _clean(yd_replacement_115)
    delta = feature.diff(21)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00116000).reindex(feature.index)
YD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['yd_replacement_d2_116'] = {'inputs': ['yd_replacement_115'], 'func': yd_replacement_d2_116}


def yd_replacement_d2_117(yd_replacement_116):
    feature = _clean(yd_replacement_116)
    delta = feature.diff(34)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00117000).reindex(feature.index)
YD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['yd_replacement_d2_117'] = {'inputs': ['yd_replacement_116'], 'func': yd_replacement_d2_117}


def yd_replacement_d2_118(yd_replacement_117):
    feature = _clean(yd_replacement_117)
    delta = feature.diff(55)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00118000).reindex(feature.index)
YD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['yd_replacement_d2_118'] = {'inputs': ['yd_replacement_117'], 'func': yd_replacement_d2_118}


def yd_replacement_d2_119(yd_replacement_118):
    feature = _clean(yd_replacement_118)
    delta = feature.diff(89)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00119000).reindex(feature.index)
YD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['yd_replacement_d2_119'] = {'inputs': ['yd_replacement_118'], 'func': yd_replacement_d2_119}


def yd_replacement_d2_120(yd_replacement_119):
    feature = _clean(yd_replacement_119)
    delta = feature.diff(1)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00120000).reindex(feature.index)
YD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['yd_replacement_d2_120'] = {'inputs': ['yd_replacement_119'], 'func': yd_replacement_d2_120}


def yd_replacement_d2_121(yd_replacement_120):
    feature = _clean(yd_replacement_120)
    delta = feature.diff(2)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00121000).reindex(feature.index)
YD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['yd_replacement_d2_121'] = {'inputs': ['yd_replacement_120'], 'func': yd_replacement_d2_121}


def yd_replacement_d2_122(yd_replacement_121):
    feature = _clean(yd_replacement_121)
    delta = feature.diff(3)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00122000).reindex(feature.index)
YD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['yd_replacement_d2_122'] = {'inputs': ['yd_replacement_121'], 'func': yd_replacement_d2_122}


def yd_replacement_d2_123(yd_replacement_122):
    feature = _clean(yd_replacement_122)
    delta = feature.diff(5)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00123000).reindex(feature.index)
YD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['yd_replacement_d2_123'] = {'inputs': ['yd_replacement_122'], 'func': yd_replacement_d2_123}


def yd_replacement_d2_124(yd_replacement_123):
    feature = _clean(yd_replacement_123)
    delta = feature.diff(8)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00124000).reindex(feature.index)
YD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['yd_replacement_d2_124'] = {'inputs': ['yd_replacement_123'], 'func': yd_replacement_d2_124}


def yd_replacement_d2_125(yd_replacement_124):
    feature = _clean(yd_replacement_124)
    delta = feature.diff(13)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00125000).reindex(feature.index)
YD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['yd_replacement_d2_125'] = {'inputs': ['yd_replacement_124'], 'func': yd_replacement_d2_125}


def yd_replacement_d2_126(yd_replacement_125):
    feature = _clean(yd_replacement_125)
    delta = feature.diff(21)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00126000).reindex(feature.index)
YD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['yd_replacement_d2_126'] = {'inputs': ['yd_replacement_125'], 'func': yd_replacement_d2_126}


def yd_replacement_d2_127(yd_replacement_126):
    feature = _clean(yd_replacement_126)
    delta = feature.diff(34)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00127000).reindex(feature.index)
YD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['yd_replacement_d2_127'] = {'inputs': ['yd_replacement_126'], 'func': yd_replacement_d2_127}


def yd_replacement_d2_128(yd_replacement_127):
    feature = _clean(yd_replacement_127)
    delta = feature.diff(55)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00128000).reindex(feature.index)
YD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['yd_replacement_d2_128'] = {'inputs': ['yd_replacement_127'], 'func': yd_replacement_d2_128}


def yd_replacement_d2_129(yd_replacement_128):
    feature = _clean(yd_replacement_128)
    delta = feature.diff(89)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00129000).reindex(feature.index)
YD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['yd_replacement_d2_129'] = {'inputs': ['yd_replacement_128'], 'func': yd_replacement_d2_129}


def yd_replacement_d2_130(yd_replacement_129):
    feature = _clean(yd_replacement_129)
    delta = feature.diff(1)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00130000).reindex(feature.index)
YD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['yd_replacement_d2_130'] = {'inputs': ['yd_replacement_129'], 'func': yd_replacement_d2_130}


def yd_replacement_d2_131(yd_replacement_130):
    feature = _clean(yd_replacement_130)
    delta = feature.diff(2)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00131000).reindex(feature.index)
YD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['yd_replacement_d2_131'] = {'inputs': ['yd_replacement_130'], 'func': yd_replacement_d2_131}


def yd_replacement_d2_132(yd_replacement_131):
    feature = _clean(yd_replacement_131)
    delta = feature.diff(3)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00132000).reindex(feature.index)
YD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['yd_replacement_d2_132'] = {'inputs': ['yd_replacement_131'], 'func': yd_replacement_d2_132}


def yd_replacement_d2_133(yd_replacement_132):
    feature = _clean(yd_replacement_132)
    delta = feature.diff(5)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00133000).reindex(feature.index)
YD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['yd_replacement_d2_133'] = {'inputs': ['yd_replacement_132'], 'func': yd_replacement_d2_133}


def yd_replacement_d2_134(yd_replacement_133):
    feature = _clean(yd_replacement_133)
    delta = feature.diff(8)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00134000).reindex(feature.index)
YD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['yd_replacement_d2_134'] = {'inputs': ['yd_replacement_133'], 'func': yd_replacement_d2_134}


def yd_replacement_d2_135(yd_replacement_134):
    feature = _clean(yd_replacement_134)
    delta = feature.diff(13)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00135000).reindex(feature.index)
YD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['yd_replacement_d2_135'] = {'inputs': ['yd_replacement_134'], 'func': yd_replacement_d2_135}


def yd_replacement_d2_136(yd_replacement_135):
    feature = _clean(yd_replacement_135)
    delta = feature.diff(21)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00136000).reindex(feature.index)
YD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['yd_replacement_d2_136'] = {'inputs': ['yd_replacement_135'], 'func': yd_replacement_d2_136}


def yd_replacement_d2_137(yd_replacement_136):
    feature = _clean(yd_replacement_136)
    delta = feature.diff(34)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00137000).reindex(feature.index)
YD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['yd_replacement_d2_137'] = {'inputs': ['yd_replacement_136'], 'func': yd_replacement_d2_137}


def yd_replacement_d2_138(yd_replacement_137):
    feature = _clean(yd_replacement_137)
    delta = feature.diff(55)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00138000).reindex(feature.index)
YD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['yd_replacement_d2_138'] = {'inputs': ['yd_replacement_137'], 'func': yd_replacement_d2_138}


# Base-universe derivative extensions for repaired first-base features.
YLD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY = {}


def _base_universe_d2(feature, idx):
    feature = _clean(feature) if '_clean' in globals() else _s(feature).replace([np.inf, -np.inf], np.nan)
    windows = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    lag = windows[idx % len(windows)]
    smooth = windows[(idx * 3 + 1) % len(windows)]
    delta = feature.diff(lag)
    local = feature - feature.rolling(max(3, smooth), min_periods=2).mean()
    out = delta + local.fillna(0.0) * (0.00037 * ((idx % 17) + 1))
    return out.replace([np.inf, -np.inf], np.nan).reindex(feature.index)


def yld_base_universe_d2_001_yld_002_pb_compression_z_42(yld_002_pb_compression_z_42):
    return _base_universe_d2(yld_002_pb_compression_z_42, 1)
YLD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['yld_base_universe_d2_001_yld_002_pb_compression_z_42'] = {'inputs': ['yld_002_pb_compression_z_42'], 'func': yld_base_universe_d2_001_yld_002_pb_compression_z_42}


def yld_base_universe_d2_002_yld_003_ps_compression_z_63(yld_003_ps_compression_z_63):
    return _base_universe_d2(yld_003_ps_compression_z_63, 2)
YLD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['yld_base_universe_d2_002_yld_003_ps_compression_z_63'] = {'inputs': ['yld_003_ps_compression_z_63'], 'func': yld_base_universe_d2_002_yld_003_ps_compression_z_63}


def yld_base_universe_d2_003_yld_005_ev_marketcap_gap_126(yld_005_ev_marketcap_gap_126):
    return _base_universe_d2(yld_005_ev_marketcap_gap_126, 3)
YLD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['yld_base_universe_d2_003_yld_005_ev_marketcap_gap_126'] = {'inputs': ['yld_005_ev_marketcap_gap_126'], 'func': yld_base_universe_d2_003_yld_005_ev_marketcap_gap_126}


def yld_base_universe_d2_004_yld_006_dividend_yield_spike_189(yld_006_dividend_yield_spike_189):
    return _base_universe_d2(yld_006_dividend_yield_spike_189, 4)
YLD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['yld_base_universe_d2_004_yld_006_dividend_yield_spike_189'] = {'inputs': ['yld_006_dividend_yield_spike_189'], 'func': yld_base_universe_d2_004_yld_006_dividend_yield_spike_189}


def yld_base_universe_d2_005_yld_008_valuation_history_depth_378(yld_008_valuation_history_depth_378):
    return _base_universe_d2(yld_008_valuation_history_depth_378, 5)
YLD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['yld_base_universe_d2_005_yld_008_valuation_history_depth_378'] = {'inputs': ['yld_008_valuation_history_depth_378'], 'func': yld_base_universe_d2_005_yld_008_valuation_history_depth_378}


def yld_base_universe_d2_006_yld_009_pe_compression_z_504(yld_009_pe_compression_z_504):
    return _base_universe_d2(yld_009_pe_compression_z_504, 6)
YLD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['yld_base_universe_d2_006_yld_009_pe_compression_z_504'] = {'inputs': ['yld_009_pe_compression_z_504'], 'func': yld_base_universe_d2_006_yld_009_pe_compression_z_504}


def yld_base_universe_d2_007_yld_010_pb_compression_z_756(yld_010_pb_compression_z_756):
    return _base_universe_d2(yld_010_pb_compression_z_756, 7)
YLD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['yld_base_universe_d2_007_yld_010_pb_compression_z_756'] = {'inputs': ['yld_010_pb_compression_z_756'], 'func': yld_base_universe_d2_007_yld_010_pb_compression_z_756}


def yld_base_universe_d2_008_yld_011_ps_compression_z_1008(yld_011_ps_compression_z_1008):
    return _base_universe_d2(yld_011_ps_compression_z_1008, 8)
YLD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['yld_base_universe_d2_008_yld_011_ps_compression_z_1008'] = {'inputs': ['yld_011_ps_compression_z_1008'], 'func': yld_base_universe_d2_008_yld_011_ps_compression_z_1008}


def yld_base_universe_d2_009_yld_014_dividend_yield_spike_63(yld_014_dividend_yield_spike_63):
    return _base_universe_d2(yld_014_dividend_yield_spike_63, 9)
YLD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['yld_base_universe_d2_009_yld_014_dividend_yield_spike_63'] = {'inputs': ['yld_014_dividend_yield_spike_63'], 'func': yld_base_universe_d2_009_yld_014_dividend_yield_spike_63}


def yld_base_universe_d2_010_yld_016_valuation_history_depth_21(yld_016_valuation_history_depth_21):
    return _base_universe_d2(yld_016_valuation_history_depth_21, 10)
YLD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['yld_base_universe_d2_010_yld_016_valuation_history_depth_21'] = {'inputs': ['yld_016_valuation_history_depth_21'], 'func': yld_base_universe_d2_010_yld_016_valuation_history_depth_21}


def yld_base_universe_d2_011_yld_021_ev_marketcap_gap_189(yld_021_ev_marketcap_gap_189):
    return _base_universe_d2(yld_021_ev_marketcap_gap_189, 11)
YLD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['yld_base_universe_d2_011_yld_021_ev_marketcap_gap_189'] = {'inputs': ['yld_021_ev_marketcap_gap_189'], 'func': yld_base_universe_d2_011_yld_021_ev_marketcap_gap_189}


def yld_base_universe_d2_012_yld_023_earnings_yield_spike_378(yld_023_earnings_yield_spike_378):
    return _base_universe_d2(yld_023_earnings_yield_spike_378, 12)
YLD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['yld_base_universe_d2_012_yld_023_earnings_yield_spike_378'] = {'inputs': ['yld_023_earnings_yield_spike_378'], 'func': yld_base_universe_d2_012_yld_023_earnings_yield_spike_378}


def yld_base_universe_d2_013_yld_024_valuation_history_depth_504(yld_024_valuation_history_depth_504):
    return _base_universe_d2(yld_024_valuation_history_depth_504, 13)
YLD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['yld_base_universe_d2_013_yld_024_valuation_history_depth_504'] = {'inputs': ['yld_024_valuation_history_depth_504'], 'func': yld_base_universe_d2_013_yld_024_valuation_history_depth_504}


def yld_base_universe_d2_014_yld_027_ps_compression_z_1260(yld_027_ps_compression_z_1260):
    return _base_universe_d2(yld_027_ps_compression_z_1260, 14)
YLD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['yld_base_universe_d2_014_yld_027_ps_compression_z_1260'] = {'inputs': ['yld_027_ps_compression_z_1260'], 'func': yld_base_universe_d2_014_yld_027_ps_compression_z_1260}


def yld_base_universe_d2_015_yld_029_ev_marketcap_gap_63(yld_029_ev_marketcap_gap_63):
    return _base_universe_d2(yld_029_ev_marketcap_gap_63, 15)
YLD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['yld_base_universe_d2_015_yld_029_ev_marketcap_gap_63'] = {'inputs': ['yld_029_ev_marketcap_gap_63'], 'func': yld_base_universe_d2_015_yld_029_ev_marketcap_gap_63}


def yld_base_universe_d2_016_yld_031_earnings_yield_spike_21(yld_031_earnings_yield_spike_21):
    return _base_universe_d2(yld_031_earnings_yield_spike_21, 16)
YLD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['yld_base_universe_d2_016_yld_031_earnings_yield_spike_21'] = {'inputs': ['yld_031_earnings_yield_spike_21'], 'func': yld_base_universe_d2_016_yld_031_earnings_yield_spike_21}


def yld_base_universe_d2_017_yld_032_valuation_history_depth_42(yld_032_valuation_history_depth_42):
    return _base_universe_d2(yld_032_valuation_history_depth_42, 17)
YLD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['yld_base_universe_d2_017_yld_032_valuation_history_depth_42'] = {'inputs': ['yld_032_valuation_history_depth_42'], 'func': yld_base_universe_d2_017_yld_032_valuation_history_depth_42}


def yld_base_universe_d2_018_yld_035_ps_compression_z_126(yld_035_ps_compression_z_126):
    return _base_universe_d2(yld_035_ps_compression_z_126, 18)
YLD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['yld_base_universe_d2_018_yld_035_ps_compression_z_126'] = {'inputs': ['yld_035_ps_compression_z_126'], 'func': yld_base_universe_d2_018_yld_035_ps_compression_z_126}


def yld_base_universe_d2_019_yld_037_ev_marketcap_gap_252(yld_037_ev_marketcap_gap_252):
    return _base_universe_d2(yld_037_ev_marketcap_gap_252, 19)
YLD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['yld_base_universe_d2_019_yld_037_ev_marketcap_gap_252'] = {'inputs': ['yld_037_ev_marketcap_gap_252'], 'func': yld_base_universe_d2_019_yld_037_ev_marketcap_gap_252}


def yld_base_universe_d2_020_yld_039_earnings_yield_spike_504(yld_039_earnings_yield_spike_504):
    return _base_universe_d2(yld_039_earnings_yield_spike_504, 20)
YLD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['yld_base_universe_d2_020_yld_039_earnings_yield_spike_504'] = {'inputs': ['yld_039_earnings_yield_spike_504'], 'func': yld_base_universe_d2_020_yld_039_earnings_yield_spike_504}


def yld_base_universe_d2_021_yld_040_valuation_history_depth_756(yld_040_valuation_history_depth_756):
    return _base_universe_d2(yld_040_valuation_history_depth_756, 21)
YLD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['yld_base_universe_d2_021_yld_040_valuation_history_depth_756'] = {'inputs': ['yld_040_valuation_history_depth_756'], 'func': yld_base_universe_d2_021_yld_040_valuation_history_depth_756}


def yld_base_universe_d2_022_yld_043_ps_compression_z_1512(yld_043_ps_compression_z_1512):
    return _base_universe_d2(yld_043_ps_compression_z_1512, 22)
YLD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['yld_base_universe_d2_022_yld_043_ps_compression_z_1512'] = {'inputs': ['yld_043_ps_compression_z_1512'], 'func': yld_base_universe_d2_022_yld_043_ps_compression_z_1512}


def yld_base_universe_d2_023_yld_047_earnings_yield_spike_42(yld_047_earnings_yield_spike_42):
    return _base_universe_d2(yld_047_earnings_yield_spike_42, 23)
YLD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['yld_base_universe_d2_023_yld_047_earnings_yield_spike_42'] = {'inputs': ['yld_047_earnings_yield_spike_42'], 'func': yld_base_universe_d2_023_yld_047_earnings_yield_spike_42}


def yld_base_universe_d2_024_yld_048_valuation_history_depth_63(yld_048_valuation_history_depth_63):
    return _base_universe_d2(yld_048_valuation_history_depth_63, 24)
YLD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['yld_base_universe_d2_024_yld_048_valuation_history_depth_63'] = {'inputs': ['yld_048_valuation_history_depth_63'], 'func': yld_base_universe_d2_024_yld_048_valuation_history_depth_63}


def yld_base_universe_d2_025_yld_051_ps_compression_z_189(yld_051_ps_compression_z_189):
    return _base_universe_d2(yld_051_ps_compression_z_189, 25)
YLD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['yld_base_universe_d2_025_yld_051_ps_compression_z_189'] = {'inputs': ['yld_051_ps_compression_z_189'], 'func': yld_base_universe_d2_025_yld_051_ps_compression_z_189}


def yld_base_universe_d2_026_yld_053_ev_marketcap_gap_378(yld_053_ev_marketcap_gap_378):
    return _base_universe_d2(yld_053_ev_marketcap_gap_378, 26)
YLD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['yld_base_universe_d2_026_yld_053_ev_marketcap_gap_378'] = {'inputs': ['yld_053_ev_marketcap_gap_378'], 'func': yld_base_universe_d2_026_yld_053_ev_marketcap_gap_378}


def yld_base_universe_d2_027_yld_055_earnings_yield_spike_756(yld_055_earnings_yield_spike_756):
    return _base_universe_d2(yld_055_earnings_yield_spike_756, 27)
YLD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['yld_base_universe_d2_027_yld_055_earnings_yield_spike_756'] = {'inputs': ['yld_055_earnings_yield_spike_756'], 'func': yld_base_universe_d2_027_yld_055_earnings_yield_spike_756}


def yld_base_universe_d2_028_yld_056_valuation_history_depth_1008(yld_056_valuation_history_depth_1008):
    return _base_universe_d2(yld_056_valuation_history_depth_1008, 28)
YLD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['yld_base_universe_d2_028_yld_056_valuation_history_depth_1008'] = {'inputs': ['yld_056_valuation_history_depth_1008'], 'func': yld_base_universe_d2_028_yld_056_valuation_history_depth_1008}


def yld_base_universe_d2_029_yld_061_ev_marketcap_gap_21(yld_061_ev_marketcap_gap_21):
    return _base_universe_d2(yld_061_ev_marketcap_gap_21, 29)
YLD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['yld_base_universe_d2_029_yld_061_ev_marketcap_gap_21'] = {'inputs': ['yld_061_ev_marketcap_gap_21'], 'func': yld_base_universe_d2_029_yld_061_ev_marketcap_gap_21}


def yld_base_universe_d2_030_yld_064_valuation_history_depth_84(yld_064_valuation_history_depth_84):
    return _base_universe_d2(yld_064_valuation_history_depth_84, 30)
YLD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['yld_base_universe_d2_030_yld_064_valuation_history_depth_84'] = {'inputs': ['yld_064_valuation_history_depth_84'], 'func': yld_base_universe_d2_030_yld_064_valuation_history_depth_84}


def yld_base_universe_d2_031_yld_067_ps_compression_z_252(yld_067_ps_compression_z_252):
    return _base_universe_d2(yld_067_ps_compression_z_252, 31)
YLD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['yld_base_universe_d2_031_yld_067_ps_compression_z_252'] = {'inputs': ['yld_067_ps_compression_z_252'], 'func': yld_base_universe_d2_031_yld_067_ps_compression_z_252}


def yld_base_universe_d2_032_yld_069_ev_marketcap_gap_504(yld_069_ev_marketcap_gap_504):
    return _base_universe_d2(yld_069_ev_marketcap_gap_504, 32)
YLD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['yld_base_universe_d2_032_yld_069_ev_marketcap_gap_504'] = {'inputs': ['yld_069_ev_marketcap_gap_504'], 'func': yld_base_universe_d2_032_yld_069_ev_marketcap_gap_504}


def yld_base_universe_d2_033_yld_071_earnings_yield_spike_1008(yld_071_earnings_yield_spike_1008):
    return _base_universe_d2(yld_071_earnings_yield_spike_1008, 33)
YLD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['yld_base_universe_d2_033_yld_071_earnings_yield_spike_1008'] = {'inputs': ['yld_071_earnings_yield_spike_1008'], 'func': yld_base_universe_d2_033_yld_071_earnings_yield_spike_1008}


def yld_base_universe_d2_034_yld_072_valuation_history_depth_1260(yld_072_valuation_history_depth_1260):
    return _base_universe_d2(yld_072_valuation_history_depth_1260, 34)
YLD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['yld_base_universe_d2_034_yld_072_valuation_history_depth_1260'] = {'inputs': ['yld_072_valuation_history_depth_1260'], 'func': yld_base_universe_d2_034_yld_072_valuation_history_depth_1260}


def yld_base_universe_d2_035_yld_basefill_004(yld_basefill_004):
    return _base_universe_d2(yld_basefill_004, 35)
YLD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['yld_base_universe_d2_035_yld_basefill_004'] = {'inputs': ['yld_basefill_004'], 'func': yld_base_universe_d2_035_yld_basefill_004}


def yld_base_universe_d2_036_yld_basefill_012(yld_basefill_012):
    return _base_universe_d2(yld_basefill_012, 36)
YLD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['yld_base_universe_d2_036_yld_basefill_012'] = {'inputs': ['yld_basefill_012'], 'func': yld_base_universe_d2_036_yld_basefill_012}


def yld_base_universe_d2_037_yld_basefill_015(yld_basefill_015):
    return _base_universe_d2(yld_basefill_015, 37)
YLD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['yld_base_universe_d2_037_yld_basefill_015'] = {'inputs': ['yld_basefill_015'], 'func': yld_base_universe_d2_037_yld_basefill_015}


def yld_base_universe_d2_038_yld_basefill_017(yld_basefill_017):
    return _base_universe_d2(yld_basefill_017, 38)
YLD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['yld_base_universe_d2_038_yld_basefill_017'] = {'inputs': ['yld_basefill_017'], 'func': yld_base_universe_d2_038_yld_basefill_017}


def yld_base_universe_d2_039_yld_basefill_018(yld_basefill_018):
    return _base_universe_d2(yld_basefill_018, 39)
YLD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['yld_base_universe_d2_039_yld_basefill_018'] = {'inputs': ['yld_basefill_018'], 'func': yld_base_universe_d2_039_yld_basefill_018}


def yld_base_universe_d2_040_yld_basefill_020(yld_basefill_020):
    return _base_universe_d2(yld_basefill_020, 40)
YLD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['yld_base_universe_d2_040_yld_basefill_020'] = {'inputs': ['yld_basefill_020'], 'func': yld_base_universe_d2_040_yld_basefill_020}


def yld_base_universe_d2_041_yld_basefill_022(yld_basefill_022):
    return _base_universe_d2(yld_basefill_022, 41)
YLD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['yld_base_universe_d2_041_yld_basefill_022'] = {'inputs': ['yld_basefill_022'], 'func': yld_base_universe_d2_041_yld_basefill_022}


def yld_base_universe_d2_042_yld_basefill_025(yld_basefill_025):
    return _base_universe_d2(yld_basefill_025, 42)
YLD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['yld_base_universe_d2_042_yld_basefill_025'] = {'inputs': ['yld_basefill_025'], 'func': yld_base_universe_d2_042_yld_basefill_025}


def yld_base_universe_d2_043_yld_basefill_026(yld_basefill_026):
    return _base_universe_d2(yld_basefill_026, 43)
YLD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['yld_base_universe_d2_043_yld_basefill_026'] = {'inputs': ['yld_basefill_026'], 'func': yld_base_universe_d2_043_yld_basefill_026}


def yld_base_universe_d2_044_yld_basefill_028(yld_basefill_028):
    return _base_universe_d2(yld_basefill_028, 44)
YLD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['yld_base_universe_d2_044_yld_basefill_028'] = {'inputs': ['yld_basefill_028'], 'func': yld_base_universe_d2_044_yld_basefill_028}


def yld_base_universe_d2_045_yld_basefill_030(yld_basefill_030):
    return _base_universe_d2(yld_basefill_030, 45)
YLD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['yld_base_universe_d2_045_yld_basefill_030'] = {'inputs': ['yld_basefill_030'], 'func': yld_base_universe_d2_045_yld_basefill_030}


def yld_base_universe_d2_046_yld_basefill_033(yld_basefill_033):
    return _base_universe_d2(yld_basefill_033, 46)
YLD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['yld_base_universe_d2_046_yld_basefill_033'] = {'inputs': ['yld_basefill_033'], 'func': yld_base_universe_d2_046_yld_basefill_033}


def yld_base_universe_d2_047_yld_basefill_034(yld_basefill_034):
    return _base_universe_d2(yld_basefill_034, 47)
YLD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['yld_base_universe_d2_047_yld_basefill_034'] = {'inputs': ['yld_basefill_034'], 'func': yld_base_universe_d2_047_yld_basefill_034}


def yld_base_universe_d2_048_yld_basefill_036(yld_basefill_036):
    return _base_universe_d2(yld_basefill_036, 48)
YLD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['yld_base_universe_d2_048_yld_basefill_036'] = {'inputs': ['yld_basefill_036'], 'func': yld_base_universe_d2_048_yld_basefill_036}


def yld_base_universe_d2_049_yld_basefill_038(yld_basefill_038):
    return _base_universe_d2(yld_basefill_038, 49)
YLD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['yld_base_universe_d2_049_yld_basefill_038'] = {'inputs': ['yld_basefill_038'], 'func': yld_base_universe_d2_049_yld_basefill_038}


def yld_base_universe_d2_050_yld_basefill_041(yld_basefill_041):
    return _base_universe_d2(yld_basefill_041, 50)
YLD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['yld_base_universe_d2_050_yld_basefill_041'] = {'inputs': ['yld_basefill_041'], 'func': yld_base_universe_d2_050_yld_basefill_041}


def yld_base_universe_d2_051_yld_basefill_042(yld_basefill_042):
    return _base_universe_d2(yld_basefill_042, 51)
YLD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['yld_base_universe_d2_051_yld_basefill_042'] = {'inputs': ['yld_basefill_042'], 'func': yld_base_universe_d2_051_yld_basefill_042}


def yld_base_universe_d2_052_yld_basefill_044(yld_basefill_044):
    return _base_universe_d2(yld_basefill_044, 52)
YLD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['yld_base_universe_d2_052_yld_basefill_044'] = {'inputs': ['yld_basefill_044'], 'func': yld_base_universe_d2_052_yld_basefill_044}


def yld_base_universe_d2_053_yld_basefill_045(yld_basefill_045):
    return _base_universe_d2(yld_basefill_045, 53)
YLD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['yld_base_universe_d2_053_yld_basefill_045'] = {'inputs': ['yld_basefill_045'], 'func': yld_base_universe_d2_053_yld_basefill_045}


def yld_base_universe_d2_054_yld_basefill_046(yld_basefill_046):
    return _base_universe_d2(yld_basefill_046, 54)
YLD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['yld_base_universe_d2_054_yld_basefill_046'] = {'inputs': ['yld_basefill_046'], 'func': yld_base_universe_d2_054_yld_basefill_046}


def yld_base_universe_d2_055_yld_basefill_049(yld_basefill_049):
    return _base_universe_d2(yld_basefill_049, 55)
YLD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['yld_base_universe_d2_055_yld_basefill_049'] = {'inputs': ['yld_basefill_049'], 'func': yld_base_universe_d2_055_yld_basefill_049}


def yld_base_universe_d2_056_yld_basefill_050(yld_basefill_050):
    return _base_universe_d2(yld_basefill_050, 56)
YLD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['yld_base_universe_d2_056_yld_basefill_050'] = {'inputs': ['yld_basefill_050'], 'func': yld_base_universe_d2_056_yld_basefill_050}


def yld_base_universe_d2_057_yld_basefill_052(yld_basefill_052):
    return _base_universe_d2(yld_basefill_052, 57)
YLD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['yld_base_universe_d2_057_yld_basefill_052'] = {'inputs': ['yld_basefill_052'], 'func': yld_base_universe_d2_057_yld_basefill_052}


def yld_base_universe_d2_058_yld_basefill_054(yld_basefill_054):
    return _base_universe_d2(yld_basefill_054, 58)
YLD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['yld_base_universe_d2_058_yld_basefill_054'] = {'inputs': ['yld_basefill_054'], 'func': yld_base_universe_d2_058_yld_basefill_054}


def yld_base_universe_d2_059_yld_basefill_057(yld_basefill_057):
    return _base_universe_d2(yld_basefill_057, 59)
YLD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['yld_base_universe_d2_059_yld_basefill_057'] = {'inputs': ['yld_basefill_057'], 'func': yld_base_universe_d2_059_yld_basefill_057}


def yld_base_universe_d2_060_yld_basefill_058(yld_basefill_058):
    return _base_universe_d2(yld_basefill_058, 60)
YLD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['yld_base_universe_d2_060_yld_basefill_058'] = {'inputs': ['yld_basefill_058'], 'func': yld_base_universe_d2_060_yld_basefill_058}


def yld_base_universe_d2_061_yld_basefill_059(yld_basefill_059):
    return _base_universe_d2(yld_basefill_059, 61)
YLD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['yld_base_universe_d2_061_yld_basefill_059'] = {'inputs': ['yld_basefill_059'], 'func': yld_base_universe_d2_061_yld_basefill_059}


def yld_base_universe_d2_062_yld_basefill_060(yld_basefill_060):
    return _base_universe_d2(yld_basefill_060, 62)
YLD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['yld_base_universe_d2_062_yld_basefill_060'] = {'inputs': ['yld_basefill_060'], 'func': yld_base_universe_d2_062_yld_basefill_060}


def yld_base_universe_d2_063_yld_basefill_062(yld_basefill_062):
    return _base_universe_d2(yld_basefill_062, 63)
YLD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['yld_base_universe_d2_063_yld_basefill_062'] = {'inputs': ['yld_basefill_062'], 'func': yld_base_universe_d2_063_yld_basefill_062}


def yld_base_universe_d2_064_yld_basefill_063(yld_basefill_063):
    return _base_universe_d2(yld_basefill_063, 64)
YLD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['yld_base_universe_d2_064_yld_basefill_063'] = {'inputs': ['yld_basefill_063'], 'func': yld_base_universe_d2_064_yld_basefill_063}


def yld_base_universe_d2_065_yld_basefill_065(yld_basefill_065):
    return _base_universe_d2(yld_basefill_065, 65)
YLD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['yld_base_universe_d2_065_yld_basefill_065'] = {'inputs': ['yld_basefill_065'], 'func': yld_base_universe_d2_065_yld_basefill_065}


def yld_base_universe_d2_066_yld_basefill_066(yld_basefill_066):
    return _base_universe_d2(yld_basefill_066, 66)
YLD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['yld_base_universe_d2_066_yld_basefill_066'] = {'inputs': ['yld_basefill_066'], 'func': yld_base_universe_d2_066_yld_basefill_066}


def yld_base_universe_d2_067_yld_basefill_068(yld_basefill_068):
    return _base_universe_d2(yld_basefill_068, 67)
YLD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['yld_base_universe_d2_067_yld_basefill_068'] = {'inputs': ['yld_basefill_068'], 'func': yld_base_universe_d2_067_yld_basefill_068}


def yld_base_universe_d2_068_yld_basefill_070(yld_basefill_070):
    return _base_universe_d2(yld_basefill_070, 68)
YLD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['yld_base_universe_d2_068_yld_basefill_070'] = {'inputs': ['yld_basefill_070'], 'func': yld_base_universe_d2_068_yld_basefill_070}


def yld_base_universe_d2_069_yld_basefill_073(yld_basefill_073):
    return _base_universe_d2(yld_basefill_073, 69)
YLD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['yld_base_universe_d2_069_yld_basefill_073'] = {'inputs': ['yld_basefill_073'], 'func': yld_base_universe_d2_069_yld_basefill_073}


def yld_base_universe_d2_070_yld_basefill_074(yld_basefill_074):
    return _base_universe_d2(yld_basefill_074, 70)
YLD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['yld_base_universe_d2_070_yld_basefill_074'] = {'inputs': ['yld_basefill_074'], 'func': yld_base_universe_d2_070_yld_basefill_074}


def yld_base_universe_d2_071_yld_basefill_075(yld_basefill_075):
    return _base_universe_d2(yld_basefill_075, 71)
YLD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['yld_base_universe_d2_071_yld_basefill_075'] = {'inputs': ['yld_basefill_075'], 'func': yld_base_universe_d2_071_yld_basefill_075}
