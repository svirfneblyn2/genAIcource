from pathlib import Path
import csv
from collections import defaultdict
from datetime import datetime

HERE=Path(__file__).resolve().parent
SRC=HERE/'northstar_sales_messy.csv'
OUT=HERE/'local_outputs'
OUT.mkdir(exist_ok=True)

with SRC.open(newline='',encoding='utf-8') as f:
    raw=list(csv.DictReader(f))

# 1. profile
row_count=len(raw)
ids=[r['order_id'] for r in raw]
duplicates=len(ids)-len(set(ids))
missing_region=sum(1 for r in raw if not r['region'].strip())
invalid_returns=sum(1 for r in raw if int(r['returns'])>int(r['orders']))

# 2. deterministic cleaning choice for the demo:
#    - remove duplicate order_id, keep first occurrence
#    - normalize empty region to UNKNOWN
#    - normalize date separators
#    - DO NOT silently repair returns > orders; flag it in verification log
seen=set(); clean=[]
for r in raw:
    oid=r['order_id']
    if oid in seen: continue
    seen.add(oid)
    rr=dict(r)
    rr['region']=rr['region'].strip() or 'UNKNOWN'
    rr['date']=rr['date'].replace('/','-')
    clean.append(rr)

monthly=defaultdict(float); channel=defaultdict(float); spend=defaultdict(float); orders=defaultdict(int); returns=defaultdict(int)
for r in clean:
    month=r['date'][:7]
    monthly[month]+=float(r['revenue'])
    channel[r['channel']]+=float(r['revenue'])
    spend[r['channel']]+=float(r['ad_spend'])
    orders[r['channel']]+=int(r['orders'])
    returns[r['channel']]+=int(r['returns'])

total=sum(monthly.values())
top_channel=max(channel,key=channel.get)
first,last=sorted(monthly)[0],sorted(monthly)[-1]
growth=(monthly[last]/monthly[first]-1)*100

summary=[]
summary.append(f'Rows: raw={row_count}; clean={len(clean)}; duplicate order_ids removed={duplicates}.')
summary.append(f'Missing region values labeled UNKNOWN={missing_region}.')
summary.append(f'Domain anomalies retained for review (returns > orders)={invalid_returns}.')
summary.append(f'Total revenue (deduplicated) = ${total:,.2f}.')
summary.append(f'Top channel by revenue = {top_channel} (${channel[top_channel]:,.2f}).')
summary.append(f'Revenue change {first} -> {last} = {growth:+.1f}%.')
summary.append('Causal caveat: historical channel revenue/ROAS does not prove incremental effect. Do not reallocate budget solely from this descriptive analysis.')

(OUT/'analysis_summary.txt').write_text('\n'.join(summary)+'\n',encoding='utf-8')
with (OUT/'cleaned_sales.csv').open('w',newline='',encoding='utf-8') as f:
    w=csv.DictWriter(f,fieldnames=clean[0].keys()); w.writeheader(); w.writerows(clean)
with (OUT/'monthly_revenue.csv').open('w',newline='',encoding='utf-8') as f:
    w=csv.writer(f); w.writerow(['month','revenue']);
    for m in sorted(monthly): w.writerow([m,round(monthly[m],2)])
with (OUT/'channel_metrics.csv').open('w',newline='',encoding='utf-8') as f:
    w=csv.writer(f); w.writerow(['channel','revenue','ad_spend','descriptive_roas','return_rate']);
    for ch in sorted(channel):
        roas='' if spend[ch]==0 else round(channel[ch]/spend[ch],2)
        rr=round(returns[ch]/orders[ch],4)
        w.writerow([ch,round(channel[ch],2),round(spend[ch],2),roas,rr])

print('\n'.join(summary))
