import unittest,math
from poisson_exposure_forge.core import run
class DomainTests(unittest.TestCase):
 def test_zero_exposure(self):self.assertEqual(run({'rate_per_unit':3,'entities':[dict(id='a',exposure=0)]})['rows'][0]['count'],0)
 def test_reproducible(self):
  d={'rate_per_unit':1,'entities':[dict(id='a',exposure=2)],'seed':13};self.assertEqual(run(d),run(d))
 def test_mean_variance(self):
  rows=run({'rate_per_unit':2,'entities':[dict(id=str(i),exposure=1)for i in range(5000)],'seed':123})['rows'];xs=[r['count']for r in rows];m=sum(xs)/len(xs);v=sum((x-m)**2 for x in xs)/len(xs);self.assertLess(abs(m-2),.1);self.assertLess(abs(v-2),.15)
