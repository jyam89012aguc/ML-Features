# ML Pipeline — Two-Machine Setup Handoff

**Goal:** Run the financial ML pipeline across two machines that share one dataset.

- **Server** = Dell PowerEdge R640, 40 cores / 384 GB RAM, **Ubuntu 24.04 LTS**, no GPU.
  Does the heavy CPU/RAM work: data load, 60k-feature computation, pivots. Always on. Orchestrates runs.
- **Workstation** = desktop with **RTX 5060 16 GB**, **Windows 11 Pro**, always on.
  Does the GPU work: XGBoost training / sweeps / inference (the `cuda:0` steps).
- **Shared storage** = one folder lives on the server, mounted on the workstation, so both see the same `trading.duckdb` and `experiments/` parquet.

> **Key concept:** The server does NOT "use" the GPU over the network — that's impossible. Instead the server *dispatches the GPU steps to the workstation over SSH*, and the workstation runs them on its own card against the shared data.

```
   ┌──────────────────────────┐         SSH (dispatch GPU steps)        ┌───────────────────────────┐
   │  SERVER  (Ubuntu 24.04)  │ ───────────────────────────────────►   │ WORKSTATION (Win11 Pro)   │
   │  40C / 384 GB / no GPU    │                                        │  RTX 5060 16 GB           │
   │  • data load + features   │ ◄───── reads/writes same files ─────►  │  • XGBoost cuda:0 training │
   │  • CPU XGBoost (optional) │            (SMB share)                  │                           │
   │  • Samba server + SSH     │                                        │  • OpenSSH server         │
   └──────────────────────────┘                                        └───────────────────────────┘
            │  exports /srv/pipeline  ──────────  mounted as  P:\  on workstation
```

Pick names/IPs now and use them throughout:

| Item | Value (fill in) |
|---|---|
| Server IP | `192.168.1.10` (example — set static) |
| Server hostname | `mlserver` |
| Workstation IP | `192.168.1.20` (example — set static) |
| Workstation hostname | `mlgpu` |
| Login user (both) | `jyama` |
| Shared folder (server path) | `/srv/pipeline` |
| Shared folder (workstation drive) | `P:\` |

---

# PART A — Server (Ubuntu 24.04 LTS)

### A1. Install Ubuntu Server
1. Download **Ubuntu Server 24.04 LTS** ISO, flash to USB (Rufus/balenaEtcher).
2. Boot the R640 from USB. In the installer:
   - Set hostname `mlserver`, user `jyama`.
   - **Check "Install OpenSSH server"** when offered.
   - Use the whole disk (or your RAID volume). Finish and reboot.
3. From any machine, confirm you can log in: `ssh jyama@192.168.1.10`

### A2. Set a static IP
Edit the netplan file (name may vary):
```bash
sudo nano /etc/netplan/50-cloud-init.yaml
```
```yaml
network:
  version: 2
  ethernets:
    eno1:                      # use your real NIC name from `ip a`
      addresses: [192.168.1.10/24]
      routes:
        - to: default
          via: 192.168.1.1
      nameservers:
        addresses: [1.1.1.1, 8.8.8.8]
```
```bash
sudo netplan apply
```

### A3. Never sleep / never suspend
```bash
sudo systemctl mask sleep.target suspend.target hibernate.target hybrid-sleep.target
```
(Servers don't sleep by default, but this guarantees it.)

### A4. System packages + Python
```bash
sudo apt update && sudo apt -y upgrade
sudo apt -y install python3.12 python3.12-venv python3-pip git tmux samba htop
```

### A5. Create the project + Python virtual environment
```bash
sudo mkdir -p /srv/pipeline
sudo chown -R jyama:jyama /srv/pipeline
cd /srv/pipeline
# copy your pipeline files here (see A6)
python3.12 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt        # requirements.txt provided in PART C
```

### A6. Copy the pipeline + data onto the server
From the Windows workstation (PowerShell), push the project over SSH:
```powershell
scp -r "D:\pipeline 1a\*" jyama@192.168.1.10:/srv/pipeline/
```
Make sure `trading.duckdb` lands in `/srv/pipeline/trading.duckdb`.
Delete Windows cruft on the server: `find /srv/pipeline -name '__pycache__' -type d -exec rm -rf {} +`

### A7. Share the folder over the network (Samba)
```bash
sudo nano /etc/samba/smb.conf
```
Add at the bottom:
```ini
[pipeline]
   path = /srv/pipeline
   browseable = yes
   read only = no
   valid users = jyama
   create mask = 0664
   directory mask = 0775
```
```bash
sudo smbpasswd -a jyama        # set the SMB password (used when mounting on Windows)
sudo systemctl restart smbd
sudo ufw allow samba           # if the firewall is on
sudo ufw allow ssh
```

✅ **Server done.** It's always-on, shares `/srv/pipeline`, and accepts SSH.

---

# PART B — Workstation (Windows 11 Pro)

### B1. Install Windows 11 Pro
- Install **Pro** (not Home — you need Remote Desktop host + OpenSSH server + Group Policy).
- Set hostname `mlgpu`, user `jyama`. Give it a **static IP** `192.168.1.20` (Settings → Network → Edit IP → Manual).

### B2. NVIDIA driver + CUDA
1. Install the latest **NVIDIA Studio/Game Ready driver** for the RTX 5060.
2. Verify: open PowerShell → `nvidia-smi` (should list the 5060 and a CUDA version).
   - XGBoost ships its own CUDA runtime in the wheel, so you do **not** need the full CUDA Toolkit — the driver is enough.

### B3. Python + GPU XGBoost
1. Install **Python 3.12** from python.org (check "Add to PATH").
2. In PowerShell:
```powershell
cd "D:\pipeline 1a"
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
```
3. Confirm GPU works:
```powershell
python -c "import xgboost as xgb; print(xgb.__version__); xgb.XGBClassifier(device='cuda:0', n_estimators=1).fit([[0,1],[1,0]],[0,1]); print('GPU OK')"
```

### B4. Enable OpenSSH Server (so the server can dispatch jobs)
PowerShell **as Administrator**:
```powershell
Add-WindowsCapability -Online -Name OpenSSH.Server~~~~0.0.1.0
Set-Service -Name sshd -StartupType Automatic
Start-Service sshd
New-NetFirewallRule -Name sshd -DisplayName "OpenSSH Server" -Enabled True -Direction Inbound -Protocol TCP -Action Allow -LocalPort 22
```
Make Python jobs use the venv when the server SSHes in — set the default shell and a clear command convention (PART D handles the exact call).

### B5. Always on — never sleep, never log off
PowerShell **as Administrator**:
```powershell
powercfg /setactive SCHEME_MIN                 # High performance
powercfg /change standby-timeout-ac 0
powercfg /change monitor-timeout-ac 0
powercfg /change disk-timeout-ac 0
powercfg /change hibernate-timeout-ac 0
powercfg /hibernate off
```
Then:
- **Disable fast startup:** Control Panel → Power Options → "Choose what the power buttons do" → uncheck "Turn on fast startup."
- **Don't lock on idle:** Settings → Accounts → Sign-in options → "If you've been away…" = Never.
- **Keep NVIDIA in max performance:** NVIDIA Control Panel → Manage 3D settings → Power management mode = "Prefer maximum performance."
- If the machine is physically secure, enable auto-login (`netplwiz` → uncheck "Users must enter a password") so it returns to a working desktop after a reboot.

### B6. Mount the server's shared folder as `P:\`
PowerShell:
```powershell
net use P: \\192.168.1.10\pipeline /user:jyama * /persistent:yes
```
(Enter the SMB password from A7.) Confirm `P:\trading.duckdb` is visible.
Now both machines read/write the **same** files.

✅ **Workstation done.** GPU verified, always-on, reachable by SSH, sharing data.

---

# PART C — Code changes for portability

These are small, mechanical edits so the **same code runs on both machines**, each using its own hardware. (Full list of files came from the earlier scan.)

### C1. `requirements.txt` (put in pipeline root, used by both A5 and B3)
```text
pandas>=2.2
numpy>=1.26
duckdb>=1.1
pyarrow>=16
xgboost>=2.1
scikit-learn>=1.5
shap>=0.46
```

### C2. Make all machine-specific paths env-var driven
In `00_pipeline_config.py`, replace the hardcoded `C:\`, `D:\`, `E:\` paths with environment lookups:
```python
import os
from pathlib import Path

# Root of everything = where this config lives (already portable)
ROOT = Path(__file__).resolve().parent

# Machine-specific roots come from env vars, with Linux defaults
SOURCE_DB_PATH    = Path(os.environ.get("PIPELINE_DB",        str(ROOT / "trading.duckdb")))
EXPERIMENT_BASE_DIR = Path(os.environ.get("PIPELINE_EXPDIR", str(ROOT / "experiments")))
BLUEPRINT31_DIR   = Path(os.environ.get("PIPELINE_BLUEPRINT", str(ROOT / "blueprint31")))
FEATURE_REGISTRY_DB = BLUEPRINT31_DIR / "feature_registry.duckdb"

# GPU vs CPU — server has no GPU, workstation does
XGBOOST_DEVICE = os.environ.get("XGBOOST_DEVICE", "cpu")
```
Do the same for the stray hardcoded paths in: `11_production_scorer.py`, `26_run_pipeline.py` (the `DOWNLOADS` variable → use `ROOT`), `import_partitioned_matrix.py`, `import_registry_model_matrix.py`, `34_organize_production.py`. The `E:\...parquet` lines inside the `if __name__ == "__main__"` blocks of the `yartseva_features/family*.py` files are test-only and can be left or pointed at env vars too.

### C3. Make every XGBoost call honor the device flag
~10 scripts hardcode `device="cuda:0"` (06, 07, 09, 10, 20–24, 30, 32, 33). Change each to import and use the config value instead:
```python
from pipeline_config import XGBOOST_DEVICE
...
xgb.XGBClassifier(device=XGBOOST_DEVICE, tree_method="hist", ...)
```
`tree_method="hist"` works on both CPU and GPU, so this is safe everywhere.

### C4. Set the env vars per machine
**Server** — add to `~/.bashrc` (or the systemd unit):
```bash
export XGBOOST_DEVICE=cpu
export PIPELINE_DB=/srv/pipeline/trading.duckdb
export PIPELINE_EXPDIR=/srv/pipeline/experiments
```
**Workstation** — PowerShell (System env vars, or per session):
```powershell
setx XGBOOST_DEVICE "cuda:0"
setx PIPELINE_DB "P:\trading.duckdb"
setx PIPELINE_EXPDIR "P:\experiments"
```
(`setx` is permanent; reopen the shell after running it.)

> After C2–C3, the **same scripts** run on both boxes — the server runs them on CPU, the workstation on the GPU, just by reading their own env vars.

---

# PART D — How a run flows (orchestration)

Two ways to run, simplest first.

### D1. Manual split (start here — prove it works)
On the **server**, inside a `tmux` session so it survives disconnect:
```bash
cd /srv/pipeline && source .venv/bin/activate
tmux new -s run1
python 00_pipeline_config.py     # setup
python 01a_load_data.py          # CPU
python 03_pivot_fundamentals.py  # CPU
python 04_compute_features.py    # CPU — the big 60k-feature job
python 05_prepare_ml.py          # CPU
```
Then run the **GPU step on the workstation** (PowerShell on `mlgpu`):
```powershell
cd "D:\pipeline 1a"; .\.venv\Scripts\Activate.ps1
python 06_train_and_evaluate.py  # GPU (reads P:\experiments, writes back)
```
Because both read/write the shared folder, the server's feature output is already visible to the workstation, and the workstation's model output flows back to the server.

### D2. Auto-dispatch (once D1 works)
Let the server launch the GPU step on the workstation automatically. From the server:
```bash
ssh jyama@192.168.1.20 'cd /d "D:\pipeline 1a" && .\.venv\Scripts\python.exe 06_train_and_evaluate.py'
```
Wire this into `26_run_pipeline.py`: keep the CPU steps as local `subprocess.run([sys.executable, script])`, but for the GPU steps (06, 07, 09, 10…) shell out over SSH to the workstation instead. One small function:
```python
GPU_STEPS = {"06_train_and_evaluate.py", "07_regularization_sweep.py",
             "09_walk_forward.py", "10_ensemble.py"}
def run_step(script):
    if script in GPU_STEPS:
        return subprocess.run(
            ["ssh", "jyama@192.168.1.20",
             f'cd /d "D:\\pipeline 1a" && .venv\\Scripts\\python.exe {script}'])
    return subprocess.run([sys.executable, script])
```

### D3. Your 6 parallel runs
Each run = its own feature set. Spread them:
- Run all 6 **feature computations on the server** in parallel (cap cores per run, e.g. `n_jobs=6` each so they don't oversubscribe 40 cores). Use 6 tmux windows or 6 systemd services.
- Send the **GPU training** for each to the workstation. The single 5060 will do them one-at-a-time (queue) — that's fine; training is the shorter leg. If GPU training becomes the bottleneck, that's the signal to add a second GPU later.

---

# PART E — Verification checklist

Run these before trusting a real job:

- [ ] `ssh jyama@192.168.1.10` works (server) and `ssh jyama@192.168.1.20` works (workstation, from server)
- [ ] Server: `systemctl status sleep.target` shows **masked**
- [ ] Workstation: `powercfg /a` shows sleep states unavailable; screen never sleeps
- [ ] Workstation: `nvidia-smi` lists the 5060; the XGBoost GPU test in B3 prints "GPU OK"
- [ ] Workstation: `P:\trading.duckdb` opens; create a file on `P:\` and confirm it appears in `/srv/pipeline` on the server
- [ ] Server: `python 00_pipeline_config.py` passes all gates with `XGBOOST_DEVICE=cpu`
- [ ] Workstation: `python 06_train_and_evaluate.py` runs on GPU and writes results the server can see
- [ ] Reboot both machines; confirm they come back to a logged-in, share-mounted, ready state with no manual steps

---

## Notes / gotchas
- **Network speed:** the 60k-feature matrices are large. If GPU steps feel I/O-bound reading over the share, put a 10GbE link between the two machines, or copy that run's parquet to the workstation's local SSD before training.
- **The 5060 is a consumer 16 GB card.** It accelerates *training*, but the heavy 60k-feature work is CPU/RAM-bound and stays on the server. Don't expect the GPU to speed up the whole pipeline — only the model-fit leg.
- **Keep `XGBOOST_DEVICE` correct per machine** — if the server ever gets `cuda:0` it will crash (no GPU); if the workstation gets `cpu` it just runs slower. The env vars in C4 handle this.
- **Backups:** `trading.duckdb` and `experiments/` are your real assets. Snapshot `/srv/pipeline` to a second disk or NAS on a schedule.
