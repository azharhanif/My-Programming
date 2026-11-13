import pandas as pd, numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from pathlib import Path
DATA=Path("data/water_samples.csv"); OUT=Path("outputs"); OUT.mkdir(exist_ok=True)
NUM=["pH","Turbidity_NTU","Nitrate_mg_L","Temperature_C","DissolvedO2_mg_L"]
def load_clean():
    df=pd.read_csv(DATA); print(df.head()); df.info(); print(df.describe(include="all")); print(df.isnull().sum())
    df["Date"]=pd.to_datetime(df.Date,errors="coerce")
    for c in NUM: df[c]=pd.to_numeric(df[c],errors="coerce")
    valid=df.SiteID.notna() & df.Date.notna() & df[NUM].notna().all(axis=1)
    valid &= (df["pH"].between(0,14)) & (df[["Turbidity_NTU","Nitrate_mg_L","DissolvedO2_mg_L"]]>=0).all(axis=1)
    clean=df.loc[valid].copy().sort_values(["SiteID","Date"])
    print("First row:",clean.iloc[0].to_dict())
    clean.to_csv(OUT/"cleaned_water_samples.csv",index=False)
    first=clean[clean.SiteID==clean.SiteID.iloc[0]]; plt.figure(); plt.plot(first.Date,first.Nitrate_mg_L,marker="o"); plt.title(f"Initial Nitrate Readings — {first.SiteID.iloc[0]}"); plt.xlabel("Date"); plt.ylabel("Nitrate (mg/L)"); plt.grid(); plt.tight_layout(); plt.savefig(OUT/"phase1_nitrate.png"); plt.close()
    return clean
def analyze(df,nitrate_threshold=10):
    d=df.copy()
    d["Health_Score"]=(7-(d["pH"]-7).abs())+(10-d["Turbidity_NTU"])+(8-d["Nitrate_mg_L"])+(d["DissolvedO2_mg_L"]/2)
    d["High_Nitrate"]=d.Nitrate_mg_L>nitrate_threshold
    summary=d.groupby("SiteID",as_index=False).agg(Mean_pH=("pH","mean"),Mean_Turbidity=("Turbidity_NTU","mean"),Mean_Nitrate=("Nitrate_mg_L","mean"),Mean_DissolvedO2=("DissolvedO2_mg_L","mean"),Mean_Classroom_Score=("Health_Score","mean"),High_Nitrate_Count=("High_Nitrate","sum"))
    anom=d.loc[d.High_Nitrate].copy()
    d.to_csv(OUT/"water_summary.csv",index=False); summary.to_csv(OUT/"site_summary.csv",index=False); anom.to_csv(OUT/"anomalies.csv",index=False)
    return d,summary,anom
def visualize(d):
    for site,g in d.groupby("SiteID"): plt.plot(g.Date,g.Nitrate_mg_L,marker="o",label=site)
    plt.title("Nitrate Concentration by Site"); plt.xlabel("Date"); plt.ylabel("Nitrate (mg/L)"); plt.legend(); plt.grid(); plt.tight_layout(); plt.savefig(OUT/"nitrate_trend.png"); plt.close()
    plt.figure(); plt.scatter(d.pH,d.Turbidity_NTU); plt.title("pH versus Turbidity"); plt.xlabel("pH"); plt.ylabel("Turbidity (NTU)"); plt.grid(); plt.savefig(OUT/"ph_turbidity.png"); plt.close()
    plt.figure(); plt.scatter(d.Nitrate_mg_L,d.DissolvedO2_mg_L); plt.title("Dissolved Oxygen versus Nitrate"); plt.xlabel("Nitrate (mg/L)"); plt.ylabel("Dissolved oxygen (mg/L)"); plt.grid(); plt.savefig(OUT/"nitrate_oxygen.png"); plt.close()
    fig=plt.figure(); ax=fig.add_subplot(111,projection="3d"); ax.scatter(d.Nitrate_mg_L,d.DissolvedO2_mg_L,d.pH,c=d.Turbidity_NTU); ax.set(xlabel="Nitrate (mg/L)",ylabel="Dissolved O2 (mg/L)",zlabel="pH",title="Water Samples in 3D"); fig.savefig(OUT/"water_3d.png"); plt.close(fig)
    q=d.sort_values("Date"); fig,ax=plt.subplots(); line,=ax.plot([],[],label="Nitrate"); ax.set_xlim(0,max(1,len(q)-1)); ax.set_ylim(0,float(q.Nitrate_mg_L.max())*1.1); ax.set(xlabel="Observation",ylabel="Nitrate (mg/L)",title="Nitrate Progression")
    def update(i): line.set_data(np.arange(i+1),q.Nitrate_mg_L.iloc[:i+1]); return line,
    ani=FuncAnimation(fig,update,frames=len(q),interval=300,blit=True)
    try: ani.save(OUT/"nitrate_animation.mp4",writer="ffmpeg",fps=3)
    except Exception as e: print("MP4 not saved; install FFmpeg:",e)
    plt.close(fig)
def main():
    df=load_clean(); d,s,a=analyze(df); visualize(d); print(s); print("Flagged nitrate samples:",len(a))
if __name__=="__main__": main()
