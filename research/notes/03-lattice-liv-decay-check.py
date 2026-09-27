# Independent check of gamma -> e+ e- kinematics with Beane et al. eqs. (16),(17), b=1.
import numpy as np
from scipy.optimize import brentq
r=1.0
def E_boson(k):          # massless boson, eq. (16)
    s=np.sum(np.sin(np.asarray(k)/2)**2); return 2*np.arcsinh(np.sqrt(s))
def E_fermion(k,m):      # Wilson fermion, eq. (17), positive-energy root near continuum
    k=np.asarray(k); S1=np.sum(np.sin(k)**2); S2=np.sum(np.sin(k/2)**2)
    f=lambda E: np.sinh(E)**2 - S1 - (m + 2*r*(S2-np.sinh(E/2)**2))**2
    E0=np.sqrt(np.dot(k,k)+m*m); return brentq(f, 0.5*E0, 1.5*E0+1e-12)
m=1e-4
for d in ([1,0,0],[1,1,1]):
    n=np.array(d,float)/np.linalg.norm(d)
    print("direction",d)
    for K in (0.01,0.02,0.025,0.03,0.05):
        k=K*n; Eg=E_boson(k)
        best=min(E_fermion(x*k,m)+E_fermion((1-x)*k,m) for x in np.linspace(0.005,0.5,2000))
        print(f"  k={K:.3f}  E_gamma - min E_pair (collinear) = {Eg-best:+.2e}   predicted k_th={(64/(1+np.sum(n**4)))**0.25*np.sqrt(m):.4f}")
