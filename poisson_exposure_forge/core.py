import math,random,itertools
from .common import number,integer,identifier,unique_ids
def poisson(rng,lam):
 if lam==0:return 0
 limit=math.exp(-lam);p=1;k=0
 while p>limit:
  p*=rng.random();k+=1
  if k>10000:raise ValueError('random_budget')
 return k-1
def run(d):
 rows=d['entities'];unique_ids(rows);rng=random.Random(integer(d.get('seed',0),0,2**32));rate=number(d['rate_per_unit'],0,100)
 if len(rows)>5000:raise ValueError('size')
 out=[]
 for row in rows:
  exposure=number(row['exposure'],0,100);lam=exposure*rate
  if lam>100:raise ValueError('lambda_limit')
  out.append(dict(id=row['id'],exposure=exposure,expected=lam,count=poisson(rng,lam)))
 total_exp=sum(r['exposure']for r in out);return dict(rows=out,observed_rate=sum(r['count']for r in out)/total_exp if total_exp else None,expected_total=sum(r['expected']for r in out))
