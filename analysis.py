import pandas as pd, numpy as np
from scipy.stats import norm
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
df=pd.read_csv(ROOT/"data/users.csv")
rows=[]
for v in ["A","B"]:
 d=df[df.variant==v]
 rows.append({"variant":v,"users":len(d),"ctr":d.ctr.mean(),"conversion":d.purchase.mean(),
 "repeat_purchase":d.repeat_purchase.mean(),"engagement":d.engaged.mean(),
 "revenue":d.total_revenue.sum(),"revenue_per_user":d.total_revenue.mean()})
s=pd.DataFrame(rows)
a=s.iloc[0]; b=s.iloc[1]
metrics=[]
for m in ["ctr","conversion","repeat_purchase","engagement"]:
 metrics.append({"metric":m,"control":a[m],"treatment":b[m],"uplift_pct":(b[m]-a[m])/a[m]*100})
pd.DataFrame(metrics).to_csv(ROOT/"outputs/uplift_summary.csv",index=False)
na,nb=len(df[df.variant=="A"]),len(df[df.variant=="B"])
ca,cb=df.loc[df.variant=="A","purchase"].sum(),df.loc[df.variant=="B","purchase"].sum()
p1,p2=ca/na,cb/nb; pooled=(ca+cb)/(na+nb)
se=np.sqrt(pooled*(1-pooled)*(1/na+1/nb)); z=(p2-p1)/se; p=2*(1-norm.cdf(abs(z)))
diff=p2-p1; se2=np.sqrt(p1*(1-p1)/na+p2*(1-p2)/nb)
pd.DataFrame([{"control_conversion":p1,"treatment_conversion":p2,"absolute_difference":diff,
"relative_uplift_pct":(p2-p1)/p1*100,"z_stat":z,"p_value":p,
"ci_low":diff-1.96*se2,"ci_high":diff+1.96*se2,"significant_at_5pct":p<.05}]).to_csv(ROOT/"outputs/conversion_test.csv",index=False)
s.to_csv(ROOT/"outputs/experiment_summary.csv",index=False)
print(s.round(4).to_string(index=False))
print(pd.read_csv(ROOT/"outputs/conversion_test.csv").round(5).to_string(index=False))
